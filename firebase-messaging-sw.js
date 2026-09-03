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
// L'ORDRE COMPTE. Le cache est installé en premier et Firebase est chargé
// ensuite, dans un try/catch. Si gstatic ne répond pas -- réseau coupé, soit
// exactement le cas où le cache sert le plus -- on perd les notifications
// pour cette session, mais le démarrage instantané survit. L'inverse serait
// absurde : une importScripts en échec au sommet du fichier empêcherait le
// gestionnaire de fetch d'être seulement installé.

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
// Variante « compat » du SDK Firebase : les service workers ne supportent pas
// les imports ES module utilisés ailleurs dans index.html, et importScripts
// est la méthode que Firebase recommande pour ce fichier précis.
try{
    importScripts('https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js');
    importScripts('https://www.gstatic.com/firebasejs/10.8.0/firebase-messaging-compat.js');

    firebase.initializeApp({
        apiKey: "AIzaSyDK9aTVTxDWWrGSIuydHtjSvUTaEguu45U",
        authDomain: "deutschai-b6fbb.firebaseapp.com",
        projectId: "deutschai-b6fbb",
        storageBucket: "deutschai-b6fbb.firebasestorage.app",
        messagingSenderId: "915434419015",
        appId: "1:915434419015:web:bfd33c9e8ba5948af99262"
    });

    const messaging = firebase.messaging();

    messaging.onBackgroundMessage((payload) => {
        const title = (payload.notification && payload.notification.title) || "Wortando";
        const options = {
            body: (payload.notification && payload.notification.body) || "",
            icon: "https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/branding/wortando-app-icon.png",
            badge: "https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/branding/wortando-app-icon.png"
        };
        self.registration.showNotification(title, options);
    });
}catch(err){
    // gstatic injoignable : pas de notifications pour cette session. Le cache
    // de démarrage ci-dessus, lui, est déjà en place et reste intact.
}
