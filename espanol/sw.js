// Service worker de Wortando Español. Un seul role : que la page s'affiche
// sans attendre le reseau.
//
// Contrairement a l'app allemande, il n'y a pas de notifications ici (pas de
// comptes, pas de Firebase), donc ce fichier n'a qu'un travail. Si des
// notifications arrivaient un jour, elles devraient venir DANS ce fichier :
// un navigateur n'accepte qu'un service worker par portee, et en enregistrer
// un second remplacerait celui-ci sans aucun message d'erreur.

const CACHE = "wortando-es-v2";   // bump apres le fork : l ancienne page etait figee

// La page est rangee sous UNE seule cle, quelle que soit l'adresse exacte
// demandee -- « / », « /index.html » ou « /?v=2 » designent la meme page.
function clavePagina(){
    return new URL("index.html", self.registration.scope).toString();
}

self.addEventListener("install", (e) => {
    // On remplit le cache des l'installation plutot qu'au premier passage :
    // sans ca, il faudrait trois ouvertures avant d'en voir l'effet.
    e.waitUntil((async () => {
        try{
            const cache = await caches.open(CACHE);
            await cache.put(clavePagina(), await fetch(clavePagina(), { cache: "reload" }));
        }catch(err){
            // Hors ligne a l'installation : le cache se remplira au premier
            // passage reussi.
        }
        await self.skipWaiting();
    })());
});

self.addEventListener("activate", (e) => {
    e.waitUntil((async () => {
        const nombres = await caches.keys();
        await Promise.all(nombres.filter(n => n !== CACHE).map(n => caches.delete(n)));
        await self.clients.claim();
    })());
});

self.addEventListener("fetch", (e) => {
    const req = e.request;

    // REGLE A NE JAMAIS ASSOUPLIR : on n'intercepte QUE la page elle-meme.
    // vocabulario.json, les paquets du dictionnaire et version.json passent
    // droit et n'entrent jamais dans le cache. Un service worker qui deborde
    // de son role est la premiere cause de version figee et de donnees
    // perimees -- des defauts invisibles au developpement et impossibles a
    // deboguer a distance.
    if(req.method !== "GET" || req.mode !== "navigate") return;

    let url;
    try{ url = new URL(req.url); }catch(err){ return; }
    if(url.origin !== self.location.origin) return;

    const clave = clavePagina();
    // « ?v=NNN » est le geste de mise a jour de l'app (comprobarVersion dans
    // index.html) : il reclame explicitement du frais, on court-circuite donc
    // le cache. Sans cette exception, la mise a jour ne passerait jamais.
    const exigeFresco = url.searchParams.has("v");

    // Le rafraichissement part TOUJOURS, meme quand on repond depuis le cache :
    // la copie sur disque se met a jour en arriere-plan, et l'ouverture
    // suivante a deja la derniere version.
    const deLaRed = fetch(req).then((rep) => {
        if(rep && rep.ok && rep.status === 200){
            caches.open(CACHE).then(c => c.put(clave, rep.clone())).catch(() => {});
        }
        return rep;
    }).catch(() => null);
    e.waitUntil(deLaRed);

    e.respondWith((async () => {
        if(!exigeFresco){
            const enCache = await caches.match(clave);
            if(enCache) return enCache;          // instantane : aucun reseau
        }
        const rep = await deLaRed;
        if(rep) return rep;
        const respaldo = await caches.match(clave);
        if(respaldo) return respaldo;            // hors ligne : on sert la copie
        return Response.error();
    })());
});
