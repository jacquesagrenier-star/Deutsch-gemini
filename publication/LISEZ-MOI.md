# wortando.com ne sert que l'app (11 nov. 2026)

Audit de lancement, point 2. Jusqu'ici, Cloudflare Pages publiait **le dépôt
entier** : `retours/journal-retours.md` (prénoms de testeurs),
`decisions/DECISIONS.md`, `CLAUDE.md`, `.claude/`, `tests/`, `audit/`…
répondaient 200 sur wortando.com. Rendre le dépôt GitHub privé n'y aurait rien
changé : Cloudflare publie ce qu'il reçoit.

## Comment

`publication/construire_site.py` copie dans `_site/` une **liste blanche** :
les fichiers de la racine que l'app charge, et quelques dossiers, chacun avec
les seules extensions utiles (pas de `.py`, `.md`, `.txt`, ni les dossiers
`outils/`, `lots/`, `sources/`). Il y ajoute une page `404.html` : sans elle,
Cloudflare sert l'app (code 200) pour n'importe quelle adresse inconnue, et un
fichier retiré ne répondrait jamais 404. Cloudflare ne publie plus que `_site/`.

Pourquoi pas `_redirects` ou une fonction Cloudflare : `_redirects` ne sait
que rediriger (pas répondre 404), et il faudrait y nommer chaque fichier
interne, ceux d'aujourd'hui et ceux de demain (une liste noire laisse fuir tout
ce qu'on oublie). Une fonction Cloudflare tournerait à chaque requête (quota
gratuit de 100 000 par jour), et vivrait dans `functions/`, qui est déjà le
dossier de Firebase.

`functions/` (Firebase) n'est pas touché : Cloudflare le traite exactement
comme aujourd'hui, et il ne fait pas partie de `_site/`.

## Ajouter un fichier que l'app charge

Une page, une image ou un JSON **nouveaux** sous un dossier déjà publié, avec
une extension déjà permise, sortent d'eux-mêmes. Un dossier nouveau, un
fichier nouveau à la racine ou une extension nouvelle : l'ajouter à
`FICHIERS_RACINE` ou `DOSSIERS` dans `construire_site.py`, sinon il répond 404
en ligne (et nulle part ailleurs : le parcours local sert le dépôt entier).

Contrôle, **hors de OneDrive** (le site pèse plus de 250 Mo) :

```bash
python publication/construire_site.py --sortie "$TEMP/_site" --verifier
```

Il liste ce qui est publié par dossier, puis les fichiers **cités** par le
site mais laissés dehors. Le 11 nov., il n'en restait que des mentions en
commentaire (outils, maquettes, scripts de tests).

## Éprouvé

- Branche jetable `site-public-essai` (export de `main` + `_site/` + un
  `wrangler.toml` qui dit à Cloudflare de ne publier que `_site/`) :
  l'app, ses données, scènes, thèmes, dictionnaire, ciel, voix de la visite,
  pages de confidentialité et de suppression du compte, liens Android
  (`.well-known/assetlinks.json`) répondent comme sur wortando.com ; les
  fichiers internes et toute adresse inconnue répondent **404**.
- Parcours de/es servis depuis `_site/` seul : voir le bilan de l'audit.

## Pas à pas pour Jacques (une seule fois)

**Avant** : la version qui contient `publication/` doit être publiée sur
`main` (elle ne change rien tant que le réglage n'est pas fait).

1. Ouvrir <https://dash.cloudflare.com> → **Workers & Pages** →
   **deutsch-gemini** → **Settings** (Paramètres) → **Build** (Builds &
   deployments) → **Build configuration** → **Edit**.
2. **Noter ou capturer les valeurs actuelles** (préréglage, commande de
   construction, dossier de sortie, dossier racine) : c'est le retour en
   arrière.
3. Mettre :
   - Framework preset : **None**
   - Build command : `python3 publication/construire_site.py`
   - Build output directory : `_site`
   - Root directory : laisser **vide**
4. **Save**. Rien ne change encore en ligne : le réglage vaut pour le
   **prochain** déploiement.
5. Le dire au chef. La session de l'audit pousse alors une branche d'essai :
   Cloudflare la construit avec le nouveau réglage, et on vérifie sa
   prévisualisation (404 sur les fichiers internes, app complète).
6. Si tout est bon : un déploiement de `main` (la prochaine version, ou un
   commit vide) met wortando.com à jour. Vérification :
   `https://wortando.com/CLAUDE.md` et `https://wortando.com/retours/journal-retours.md`
   doivent répondre « Cette page n'existe pas » ; l'app s'ouvre normalement.

**Retour en arrière** : remettre les valeurs notées à l'étape 2, puis
« Retry deployment » sur le dernier déploiement de production.

Si la construction échoue chez Cloudflare (« Build failed »), wortando.com
**reste sur le dernier déploiement réussi** : rien ne casse, la mise à jour
attend.

## Ce que ça ne règle pas

- L'ancienne adresse **GitHub Pages** (`…github.io/Deutsch-gemini/`) publie,
  elle aussi, tout le dépôt tant qu'il est public : c'est le dépôt privé (et
  la redirection préparée dans `demenagement/`) qui la fermera.
- Ce qui est **déjà** dans l'historique Git public (le journal des retours et
  ses prénoms) reste lisible sur GitHub tant que le dépôt est public.
