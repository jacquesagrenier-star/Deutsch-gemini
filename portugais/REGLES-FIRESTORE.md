# Les règles Firestore du portugais

**Publiées le 30 oct. 2026** par le chef d'orchestre, à la demande de Jacques
(« Coller des règles Firestone pour que la progression j'aimerais qu'on le
fasse. »). Les règles qui étaient en ligne avant ont été sauvegardées dans
`~/.wortando/regles-console-2026-10-30.txt`. La progression portugaise suit
donc d'un appareil à l'autre ; la variante du Brésil utilise les mêmes
collections (mêmes mots, même ordre que le Portugal).

Pour mémoire, les deux blocs publiés (projet `deutschai-b6fbb`, Firestore
Database → Règles), placés juste après ceux de l'anglais (`usersEn`,
`resumesEn`). Ce sont les règles du japonais et de l'anglais, avec le nom des
collections du portugais. Le même texte est dans `firestore.rules` du dépôt.

```
    match /usersPt/{uid} {
      allow get: if request.auth != null && (request.auth.uid == uid || isAdmin());
      allow list: if isAdmin();
      allow write: if request.auth != null && request.auth.uid == uid;
    }
    match /resumesPt/{uid} {
      allow get, list: if isAdmin();
      allow write: if request.auth != null && (request.auth.uid == uid || isAdmin());
    }
```
