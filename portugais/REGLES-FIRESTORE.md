# Les règles Firestore du portugais (à coller)

Sans ces deux blocs, l'essai portugais marche quand même, mais la progression
reste sur l'appareil (elle ne suit pas d'un téléphone à l'autre).

**Où** : console Firebase → projet `deutschai-b6fbb` → Firestore Database →
Règles. **Sauvegarder d'abord** les règles en place (copier-coller dans un
fichier), puis ajouter ces deux blocs juste après ceux de l'anglais
(`usersEn`, `resumesEn`), avant les deux accolades de fin, et Publier.

Ce sont exactement les règles du japonais et de l'anglais, avec le nom des
collections du portugais. Le même texte est déjà dans `firestore.rules` du
dépôt.

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
