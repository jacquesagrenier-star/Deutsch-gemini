// Service worker unique de Wortando. Il doit être servi depuis la racine de
// l'app (même dossier qu'index.html). Deux rôles, dans cet ordre :
//
//   1. CACHE DE DÉMARRAGE (v257) -- il sert index.html depuis le disque du
//      téléphone, sans aucun aller-retour réseau.
//   2. NOTIFICATIONS (Firebase Cloud Messaging) -- il reçoit et affiche les
//      notifications quand l'onglet n'est pas au premier plan.
//
// POURQUOI LES DEUX ICI. Un navigateur n'accepte qu'un seul service worker
// par portée : enregistrer un second fichier remplacerait celui-ci et
// supprimerait les notifications. Ils doivent donc cohabiter.
//
// ⚠️ CE FICHIER NE TOUCHE PLUS AU RÉSEAU À SON DÉMARRAGE (v657). Il chargeait
// deux scripts Firebase depuis gstatic, synchronement, au sommet -- donc à
// chaque réveil du worker, et toute requête de l'app attendait derrière. Voir
// le bloc NOTIFICATIONS plus bas : c'est là qu'est l'explication complète, et
// c'est la correction la plus importante de la journée du 21 septembre.
//
// La règle qui reste : rien de bloquant au sommet de ce fichier. Un service
// worker est réévalué en entier à chaque réveil, et tout ce qu'on y met au
// premier niveau se paie sur la latence de la PREMIÈRE requête qui le réveille
// -- une dette invisible en développement, où tout répond en dix millisecondes.

// ============ 1. CACHE DE DÉMARRAGE ============
//
// Ce que ça corrige : quand on ouvre l'app par un lien, Safari laisse à
// l'écran sa PHOTO de la visite précédente -- l'accueil -- tant que la
// nouvelle page n'a rien peint. C'est l'éclair d'accueil qu'on voyait avant
// la vidéo d'ouverture. La v256 a ramené le coût du premier rendu de 85 ko à
// 5 ko, mais il restait un plancher qu'aucune optimisation du fichier ne peut
// franchir : le temps de l'aller-retour réseau lui-même. Servie depuis le
// disque, la page n'attend plus rien.

const CACHE = "wortando-page-v1";

// La page est rangée sous UNE seule clé, quelle que soit l'adresse exacte
// demandée -- « / », « /index.html » ou « /?v=257 » désignent la même page.
function clePage(){
    return new URL("index.html", self.registration.scope).toString();
}

// CE QUI EST « LA PAGE », ET CE QUI NE L'EST PAS.
//
// Le gestionnaire de fetch annonçait depuis toujours qu'il n'interceptait que
// la page de l'app. Il ne le vérifiait pas : toute navigation de même origine
// recevait index.html depuis le cache. Naviguer vers /confidentialite.html
// affichait donc Wortando -- ce qui aurait fait refuser la soumission au Play
// Store, Google exigeant une URL de politique de confidentialité lisible.
//
// La portée du service worker EST le dossier de l'app. La page, c'est ce
// dossier lui-même ou son index.html. Tout le reste du domaine passe droit.
const DOSSIER_APP = new URL(self.registration.scope).pathname;

function estLaPage(url){
    const p = url.pathname;
    return p === DOSSIER_APP
        || p === DOSSIER_APP + "index.html"
        // « /app » sans barre finale : le navigateur redirige, mais la
        // première requête porte encore le chemin nu.
        || p + "/" === DOSSIER_APP;
}

self.addEventListener("install", (e) => {
    // On remplit le cache dès l'installation plutôt qu'au premier passage :
    // sans ça, il faudrait trois ouvertures avant d'en voir l'effet.
    e.waitUntil((async () => {
        try{
            const cache = await caches.open(CACHE);
            await cache.put(
                clePage(),
                await fetch(clePage(), { cache: "reload" })
            );
        }catch(err){
            // Hors ligne au moment de l'installation : le cache se remplira
            // tout seul au premier passage réussi.
        }
        await self.skipWaiting();
    })());
});

self.addEventListener("activate", (e) => {
    e.waitUntil((async () => {
        const noms = await caches.keys();
        await Promise.all(noms.filter(n => n !== CACHE).map(n => caches.delete(n)));
        await self.clients.claim();
    })());
});

self.addEventListener("fetch", (e) => {
    const req = e.request;

    // RÈGLE À NE JAMAIS ASSOUPLIR : on n'intercepte QUE la page elle-même.
    // Firestore, l'authentification, les JSON de vocabulaire sur GitHub, les
    // polices Google, version.json -- tout passe droit et n'entre jamais dans
    // le cache. Un service worker qui déborde de son rôle est la première
    // cause de version figée et de données périmées, et ces défauts-là sont
    // invisibles au développement et impossibles à déboguer à distance.
    if(req.method !== "GET" || req.mode !== "navigate") return;

    let url;
    try{ url = new URL(req.url); }catch(err){ return; }
    if(url.origin !== self.location.origin) return;
    // LA VERIFICATION QUI MANQUAIT. Sans elle, la politique de
    // confidentialité, une page de mentions légales ou n'importe quelle autre
    // page du domaine recevaient l'application à la place d'elles-mêmes.
    if(!estLaPage(url)) return;

    const cle = clePage();
    // « ?v=NNN » est le geste de mise à jour de l'app (verifierNouvelleVersion
    // dans index.html) : il réclame explicitement du frais, on court-circuite
    // donc le cache. Sans cette exception, la mise à jour ne passerait jamais.
    const exigeDuFrais = url.searchParams.has("v");

    // Le rafraîchissement part TOUJOURS, même quand on répond depuis le cache :
    // la copie sur disque se met ainsi à jour en arrière-plan, et l'ouverture
    // suivante a déjà la dernière version. waitUntil garde le service worker
    // en vie le temps que ça se termine.
    const duReseau = fetch(req).then((rep) => {
        if(rep && rep.ok && rep.status === 200){
            caches.open(CACHE).then(c => c.put(cle, rep.clone())).catch(() => {});
        }
        return rep;
    }).catch(() => null);
    e.waitUntil(duReseau);

    e.respondWith((async () => {
        if(!exigeDuFrais){
            const enCache = await caches.match(cle);
            if(enCache) return enCache;        // instantané : aucun réseau
        }
        const rep = await duReseau;
        if(rep) return rep;
        const secours = await caches.match(cle);
        if(secours) return secours;            // hors ligne : on sert la copie
        return Response.error();
    })());
});

// ============ 2. NOTIFICATIONS ============
//
// ⚠️ PLUS AUCUN `importScripts` AU DÉMARRAGE (v657), ET C'EST LA CORRECTION LA
// PLUS IMPORTANTE DU 21 SEPTEMBRE. Ce fichier chargeait deux scripts Firebase
// depuis gstatic, SYNCHRONEMENT, au sommet — donc À CHAQUE DÉMARRAGE DU
// WORKER, et non une fois pour toutes.
//
// CE QUE ÇA COÛTAIT, et personne ne le voyait :
//
//   Toute sous-ressource demandée par une page contrôlée traverse le service
//   worker, MÊME vers une autre origine. Chrome tue un worker inactif après une
//   trentaine de secondes ; la requête suivante doit donc le RÉVEILLER, et le
//   réveil réévalue ce fichier en entier — deux téléchargements réseau — avant
//   que le premier `fetch` ne soit seulement dispatché. Chaque mp3 d'Aurora
//   attendait derrière ça, dépassait la garde de 1,5 s, et finissait sur la
//   voix Windows.
//
// LES QUATRE OBSERVATIONS DE JACQUES, QUI NE TENAIENT ENSEMBLE QUE COMME ÇA :
//   - « le son des confettis est simultané »   -> un `blob:` ne traverse JAMAIS
//                                                 le service worker
//   - le même fichier dans un onglet nu : instantané, même pendant la panne
//                                              -> onglet non contrôlé
//   - mauvais au début, puis « très très bien » après une cinquantaine de
//     cartes                                   -> le trafic garde le worker en vie
//   - ⚠️ « j'ai attendu quelques minutes, ça n'a rien changé »
//                                              -> attendre ENDORT le worker.
//                                                 C'est le seul fait que toutes
//                                                 mes autres explications
//                                                 contredisaient.
//
// Le push est donc traité NATIVEMENT. Web Push est livré par le navigateur à
// cet événement de toute façon ; `onBackgroundMessage` n'en était qu'une
// enveloppe. Le worker démarre maintenant sans toucher au réseau.
//
// ⚠️ IL FAUT TOUJOURS APPELER showNotification(). Sans ça Chrome affiche
// lui-même « ce site a été mis à jour en arrière-plan », ce qui est pire que
// pas de notification du tout.
const ICONE = "https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/branding/wortando-app-icon.png";

self.addEventListener("push", (e) => {
    let titre = "Wortando", corps = "";
    try{
        // FCM envoie soit un bloc `notification`, soit un bloc `data` seul.
        // On lit les deux : choisir en aurait fait disparaître un des deux
        // types de message, en silence.
        const p = e.data ? e.data.json() : {};
        const n = p.notification || p.data || {};
        titre = n.title || titre;
        corps = n.body || "";
    }catch(err){
        // Charge utile illisible ou absente : on notifie quand même, sans
        // texte. Se taire ici laisserait Chrome écrire son message générique.
    }
    e.waitUntil(self.registration.showNotification(titre, {
        body: corps, icon: ICONE, badge: ICONE
    }));
});

// Toucher la notification ramène à l'app plutôt que d'ouvrir un onglet de plus.
self.addEventListener("notificationclick", (e) => {
    e.notification.close();
    e.waitUntil((async () => {
        const cible = new URL("index.html", self.registration.scope).toString();
        const ouverts = await self.clients.matchAll({ type: "window", includeUncontrolled: true });
        for(const c of ouverts){
            if(c.url.startsWith(self.registration.scope) && "focus" in c) return c.focus();
        }
        if(self.clients.openWindow) return self.clients.openWindow(cible);
    })());
});
