// SERVICE WORKER DE REMPLACEMENT -- filet de securite du demenagement.
//
// Ce fichier existe DEUX FOIS, a l'identique, sous les noms exacts des
// anciens service workers (demenagement/verifier_redirection.py le controle) :
//   firebase-messaging-sw.js   (l'app allemande, portee /Deutsch-gemini/)
//   espanol/sw.js              (Wortando Español, portee /Deutsch-gemini/espanol/)
//
// POURQUOI. L'ancien service worker sert index.html DEPUIS LE CACHE du
// telephone : un testeur qui ouvre l'icone ne demande jamais la page au
// reseau, donc ne verrait jamais la redirection. Mais le navigateur, lui,
// re-telecharge regulierement le FICHIER du service worker (a chaque
// navigation, au plus tard toutes les 24 h) et installe la nouvelle version
// s'il a change. C'est cette porte qu'on emprunte : la nouvelle version vide
// les caches, se desinscrit et recharge les onglets ouverts, qui tombent alors
// sur la page de redirection.
//
// ⚠️ CE QU'ON PERD : les notifications sur l'ancienne adresse. Ce fichier
// remplace celui qui les affichait, et en se desinscrivant il coupe
// l'abonnement push de cette adresse. Elles n'ont plus de raison d'y etre :
// l'app vit a la nouvelle adresse, ou la personne les reactive (un nouveau
// site doit redemander la permission de toute facon).
//
// Rien d'autre ici : pas de gestionnaire de fetch, donc tout passe au reseau
// des l'installation.

self.addEventListener("install", () => {
    self.skipWaiting();
});

self.addEventListener("activate", (e) => {
    e.waitUntil((async () => {
        // On prend d'abord la main sur tous les onglets de la portee, pour
        // pouvoir les recharger plus bas.
        try{ await self.clients.claim(); }catch(err){}
        try{
            const noms = await caches.keys();
            await Promise.all(noms.map((n) => caches.delete(n)));
        }catch(err){}
        try{ await self.registration.unregister(); }catch(err){}
        // Les onglets encore ouverts sur l'ancienne app : on les recharge, ils
        // recoivent la page de redirection (plus de cache, plus de worker).
        try{
            const onglets = await self.clients.matchAll({ type: "window", includeUncontrolled: true });
            for(const c of onglets){
                try{ await c.navigate(c.url); }catch(err){}
            }
        }catch(err){}
    })());
});
