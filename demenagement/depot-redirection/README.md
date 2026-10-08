# Wortando a déménagé

L'application est maintenant à **https://deutsch-gemini.pages.dev/**.

Ce dépôt ne sert qu'à faire répondre l'ancienne adresse
(`jacquesagrenier-star.github.io/Deutsch-gemini/`) : chaque page renvoie vers la
même page à la nouvelle adresse, en gardant le chemin, la requête et le fragment.

| Fichier | Rôle |
|---|---|
| `index.html`, `404.html` | La redirection (identiques : GitHub Pages sert `404.html` pour toute adresse absente). |
| `firebase-messaging-sw.js`, `espanol/sw.js` | Remplacent les anciens service workers : vident le cache, se désinscrivent, rechargent les onglets. |
| `version.json`, `espanol/version.json` | Un numéro très haut : une ancienne app encore ouverte se recharge et tombe sur la redirection. |
| `.nojekyll` | Sert les fichiers tels quels. |

Préparé dans `demenagement/depot-redirection/` du dépôt de l'app ; procédure :
`demenagement/JOUR-J.md`.
