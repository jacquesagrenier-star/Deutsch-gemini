# Wortando Pflege : la fiche de publication (ligne 94 de la file)

14 nov. 2026, session architecture. Ce qu'il faudra faire le jour où la ligne 94 passe : **après la 98**
(séance en quatre parties) **et la 99** (salade du restaurant), avec le feu vert du chef. Rien de ce
fichier n'est fait ; rien n'est poussé.

Il y a trois dépôts de nature différente, chacun avec son chemin :

| Quoi | Où ça part | Qui le fait | Quand |
|---|---|---|---|
| `index.html`, `pflege/datos/`, les scènes, la page de l'examen, ses images | Cloudflare Pages, par le `push` sur `main` (`publication/construire_site.py`) | la session, au feu vert du chef | la version N |
| Les sons de l'examen (32), puis ceux des dialogues | **Firebase Hosting**, `audio/deposer.py` | la session, depuis le dossier principal | **avant** la version N |
| Les règles Firestore (`soinsExamensJson`) | la console Firebase | **Jacques**, à la main | entre la version N et la version N+1 |

## 1. Ce que sert Cloudflare (rien à déposer à la main)

`python publication/construire_site.py` copie dans `_site/` la seule liste blanche de l'app. Contrôle du
14 nov. sur les fichiers Pflege suivis : **141 sur 143 sont servis** (`pflege/datos/*.json`, les 8 scènes
`visuel/prototype/soins-*` — webp, masques, `scene-*.js`, traductions —, `visuel/prototype/telc-pflege/` —
`telc.html`, `examen.js`, `bareme.js`, `donnees/*.json`, `img/*.webp`). Les deux qui ne le sont pas sont des
outils (`telc-pflege/outils/a_traduire.py`, `voix_soins.py`) : c'est voulu.

À refaire le jour J (un fichier ajouté entre-temps hors des extensions permises répondrait 404) :

```bash
cd publication && python -c "import construire_site as c, subprocess; fs=[f for f in subprocess.run(['git','ls-files','..'],capture_output=True,text=True).stdout.split() if 'soins' in f or 'telc-pflege' in f or 'pflege/datos' in f]; print([f for f in fs if not c.publie(f[3:])])"
```

→ seuls les deux outils doivent sortir.

## 2. Les sons, sur Firebase Hosting

### 2.1 ⚠️ Depuis le dossier principal, jamais depuis un worktree

`firebase.json` publie **tout** `audio/mp3/` (`"public": "audio/mp3"`), et un dépôt Hosting **remplace le
site entier** par ce qu'il trouve. Un worktree n'a pas `audio/mp3/` (ou en a une partie) : y lancer le dépôt
effacerait en ligne toutes les voix de l'app (Aurora, l'espagnol, l'anglais, le DTZ…). Le dépôt se lance donc
**dans `C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI`**, où vivent les 32 fichiers depuis la
session examen :

```bash
cd "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
python audio/deposer.py --verifier
python audio/deposer.py
```

(`deposer.py` n'appelle que `firebase deploy --only hosting`, jamais les Cloud Functions.)

### 2.2 Les 32 sons de l'examen blanc (série 1)

- Sur le disque : `audio/mp3/dtz/soins/` du dossier principal (11,4 Mo, contrôlés par
  `audio/controler_sons.py` sans défaut selon la session examen).
- En ligne : `https://deutschai-b6fbb.web.app/dtz/soins/<fichier>` (`BASE_PISTES` de
  `visuel/prototype/dtz/commun.js` + le chemin du manifeste).
- Le manifeste : `visuel/prototype/telc-pflege/donnees/voix-soins.json` ({clé : fichier}), servi par
  Cloudflare. Une clé dont le fichier ne répond pas fait parler la page avec la voix du téléphone : rien ne
  casse, mais l'examen n'aurait pas ses voix. D'où le dépôt **avant** la version.
- État le 14 nov. : **pas en ligne** (`c300f1f7f36f4d6c.mp3` répond 404). Normal.

| Clé | Fichier | Ko | SHA-1 (12 premiers) |
|---|---|---|---|
| `s1-H1-consigne` | `soins/c300f1f7f36f4d6c.mp3` | 200 | `03461da0ca58` |
| `s1-H2-consigne` | `soins/b730112d2bddb9c0.mp3` | 239 | `01be9a07eee2` |
| `s1-H2g1` | `soins/37dd98ce9aeb72ff.mp3` | 821 | `5f591802e19f` |
| `s1-H2g2` | `soins/c0f3cff058dd7961.mp3` | 750 | `839e138642bd` |
| `s1-H2g3` | `soins/dd3f3e70f1624fd5.mp3` | 629 | `f40d1e16328a` |
| `s1-H2g4` | `soins/b8963c080024f950.mp3` | 772 | `031d7ae94b5c` |
| `s1-H2g5` | `soins/1bb163254a432be9.mp3` | 843 | `a2ef35c77ba4` |
| `s1-H3` | `soins/720bc97cd8ebcc3b.mp3` | 2196 | `6d2de36baad5` |
| `s1-H3-consigne` | `soins/c2feef53231ebc6a.mp3` | 240 | `75705cfa53eb` |
| `s1-H4-consigne` | `soins/9d234a6381134ac3.mp3` | 320 | `da640cd2aaca` |
| `s1-n0` | `soins/f3c91162c797751c.mp3` | 253 | `461d4d43286f` |
| `s1-n0b` | `soins/e6108180ccc47011.mp3` | 255 | `ce06a425bae3` |
| `s1-n1` | `soins/6dc7df68b453a066.mp3` | 373 | `1d9a24179cc5` |
| `s1-n2` | `soins/047c67385ee0e82f.mp3` | 304 | `657f3d598d30` |
| `s1-n21` | `soins/a6dc1b90df35ccee.mp3` | 292 | `4c3ef18c14d0` |
| `s1-n22` | `soins/eef294bca62a8cab.mp3` | 236 | `1642fa3d78cc` |
| `s1-n23` | `soins/30061cd978412f3f.mp3` | 244 | `780f83463422` |
| `s1-n3` | `soins/5afc060ca2571ca6.mp3` | 309 | `b0df66886202` |
| `s1-n4` | `soins/44c7a99c3db7661d.mp3` | 336 | `0c630bbef69c` |
| `s1-sp1a-0` | `soins/7bb3aa78c5bf711f.mp3` | 141 | `1eedf1510f8d` |
| `s1-sp1b-0` | `soins/4f177aab98246c6c.mp3` | 109 | `87647796f9dc` |
| `s1-sp1b-1` | `soins/e5f584e1411c1a7d.mp3` | 47 | `b7303deaaeed` |
| `s1-sp1b-2` | `soins/b1d325aa455f5041.mp3` | 53 | `8b0e807b9453` |
| `s1-sp2a-0` | `soins/884fa7808b53abb9.mp3` | 149 | `8d9201e9a397` |
| `s1-sp2b-schicht-0` | `soins/729e8c42bcdf3f37.mp3` | 70 | `5ef7b766759f` |
| `s1-sp2b-schicht-1` | `soins/7e592091ad21d8db.mp3` | 64 | `c9895b782dac` |
| `s1-sp2b-schmerz-0` | `soins/e4cac43bde1a7fcd.mp3` | 87 | `cfd6e0b9b850` |
| `s1-sp2b-schmerz-1` | `soins/19b4b6e4c40b0cc1.mp3` | 83 | `902236fe4d6a` |
| `s1-sp3-0` | `soins/26356114d7df7218.mp3` | 276 | `281f5435ce87` |
| `s1-sp3-1` | `soins/b216e27947096190.mp3` | 144 | `6548b437900e` |
| `s1-sp3-2` | `soins/22b5293ac7fbbf66.mp3` | 150 | `5ebe01e6a8c7` |
| `s1-sp3-3` | `soins/7ae5d104b31f9812.mp3` | 108 | `5c3af86bb011` |

Contrôle après le dépôt, chaque fichier doit répondre 200 :

```bash
python -c "import json,urllib.request as u; m=json.load(open('visuel/prototype/telc-pflege/donnees/voix-soins.json',encoding='utf-8')); print([k for k,v in m.items() if k[0]!='_' and u.urlopen(u.Request('https://deutschai-b6fbb.web.app/dtz/'+v,method='HEAD')).status!=200])"
```

### 2.3 Les sons des dialogues et de la grammaire (pas encore générés)

Chiffrage et voix : `pflege/VOIX.md` (session dialogues ; « chemin modèle » ≈ 34 000 caractères, ≈ 7,4 $
avec les reprises, dans la marge du plan ; « toutes les branches » demanderait un nouvel accord). Le jour où
ils existent, **même chemin que l'examen** :

- sur le disque : `audio/mp3/pflege/<empreinte>.mp3` du dossier principal ;
- en ligne : `https://deutschai-b6fbb.web.app/pflege/<empreinte>.mp3` ;
- un manifeste servi par Cloudflare, `pflege/datos/sons.json` ({clé : fichier}), sur le modèle de
  `voix-soins.json` ; la page qui joue les dialogues le lit, et retombe sur la voix du téléphone pour une
  clé absente ;
- avant la génération : les lectures des nombres versées dans `audio/lectures/de.json` ; après :
  `python audio/controler_sons.py --dossiers de` (aucun SATURE, CLIC ni TRAINE), puis le dépôt du § 2.1.

Ces sons partiront avec la version qui affiche les dialogues, pas avec la ligne 94 si la page n'est pas
prête : un son déposé sans page qui le lit ne sert à rien, mais ne gêne rien non plus.

## 3. Les règles Firestore (Jacques)

La version N **n'écrit pas** `soinsExamensJson` : les résultats des examens blancs restent sur l'appareil, et
aucune sauvegarde ne risque d'être refusée. Les règles ne bloquent donc pas la version N.

La remontée des examens blancs au suivi de l'admin vient en deux temps, **dans cet ordre** :

1. **Jacques colle** `securite/regles-soins/firestore-avec-soins.rules` dans la console
   (https://console.firebase.google.com/project/deutschai-b6fbb/firestore/rules, remplacer TOUT le texte,
   « Publier »). Par rapport à `firestore.rules` de `main` (vérifié le 14 nov., `origin/main` 9b70e02), il y
   a **une ligne** : `'soinsExamensJson'` dans `champsProgression()`. Par rapport aux règles qu'il a
   réellement collées le 12 nov. (cf0cfe6), il y en a **deux** : celle-ci et la règle des codes de la v1188
   (« un code utilisé ne se supprime jamais »), s'il ne l'a pas encore collée. Les deux partent ensemble.
2. On vérifie qu'une sauvegarde ordinaire passe toujours (le tableau de bord admin le dit).
3. **Puis seulement** la version N+1, qui écrit la clé (le code exact : `pflege/AGENCE-DONNEES.md`, § 2,
   « Le code, à appliquer APRÈS ») et remplace `firestore.rules` et `securite/firestore-corrige.rules` par
   le fichier collé (sinon `tests/verifier.py` refuse la clé).

Dans l'autre ordre, tout compte qui a passé un examen blanc verrait **toute** sa sauvegarde refusée.

⚠️ Le jour J, refaire la comparaison : si la ligne 98 ou la 99 a changé les règles, refaire le fichier à
partir des nouvelles (la seule ligne à ajouter est `'soinsExamensJson'`) et relancer le banc :

```bash
diff --strip-trailing-cr firestore.rules securite/regles-soins/firestore-avec-soins.rules
cd securite/essai-regles
REGLES=../regles-soins/firestore-avec-soins.rules AVEC_SOINS=1 firebase emulators:exec --only firestore --project demo-wortando "node essai.js"
```

→ attendu : 250 ok, 0 échec (banc du 14 nov.).

## 4. L'ordre du jour J

1. Feu vert du chef ; la ligne 94 en tête de `~/.wortando/file-publication.txt`.
2. Rebase de `claude/pflege-bcc9b8` sur `main` (après la 98 et la 99), puis les contrôles :
   `python tests/verifier.py`, `node tests/syntaxe.js`, `python tests/pflege.py`,
   `python tests/pflege_vocabulaire.py`, `python tests/pflege_dialogues.py`, `python tests/pflege_examen.py`,
   `node tests/pflege_certificat.js`, `python pflege/outils/construire_scenes.py --toutes --controle`.
3. Les parcours (verrou du navigateur, après avoir retiré `~/.wortando/stop-pflege`) :
   `--app de` et `--app es-moteur` contre les références de la version en cours → **0 écart** (les Soins
   sont derrière `essaiActif("soins")`, réservé à l'admin et aux comptes ouverts un à un : un compte ordinaire
   ne doit rien voir).
4. Les vérifications au navigateur, compte admin : la tuile Soins, un thème A2, une carte de verbe (la ligne
   « Perfekt : … »), une scène et son retour aux Soins, l'examen blanc jusqu'au résultat (enregistré, la ligne
   « Dernier examen blanc » à jour) et son retour, la carte « Suivi Soins » du tableau de bord.
5. Le dépôt des 32 sons (§ 2), depuis le dossier principal ; contrôle 200.
6. La version N (numéro posé par le PC à la fusion), `push` sur `main` ; `CLAUDE.md` : la ligne de la
   version dans la liste des références (« aucun écart »).
7. Une ligne au chef ; la proposition des règles à Jacques (§ 3), puis la version N+1.
