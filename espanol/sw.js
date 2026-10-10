// LE SERVICE WORKER DE L'ANCIENNE APP ESPAGNOLE SE RETIRE (v736, 10 oct. 2026).
//
// Il servait sa copie de la page avant le reseau. L'app espagnole vit
// maintenant dans le meme moteur que l'allemande, a la racine, et cette page
// n'est plus qu'une redirection : une copie gardee ici ferait rouvrir
// l'ancienne app, indefiniment. Ce fichier remplace donc l'ancien des que le
// navigateur le revoit : il efface ses copies, se desinscrit, et recharge les
// pages ouvertes, qui tombent alors sur la redirection.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => {
    e.waitUntil((async () => {
        try{ for(const n of await caches.keys()) await caches.delete(n); }catch(err){}
        try{ await self.registration.unregister(); }catch(err){}
        try{
            for(const c of await self.clients.matchAll({ type: "window" })) c.navigate(c.url);
        }catch(err){}
    })());
});
