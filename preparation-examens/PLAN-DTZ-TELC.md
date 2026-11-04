# Préparation aux examens : un bloc DTZ, un bloc telc Deutsch A2·B1

Plan du 4 nov. 2026, session « examens DTZ / telc » (branche `claude/examens-dtz-telc-774170`). Rangé dans
`preparation-examens/` et non dans `examens/`, qui est ignoré par git (les listes officielles du Goethe, pas redistribuées).
Décision de Jacques du 4 nov. (`decisions/DECISIONS.md`) : « ma vision, c'est d'avoir un bloc pour se préparer au
DTZ, puis un bloc pour se préparer à l'examen A2 B1. Donc, il y a du matériel, ce que je comprends qu'on va pouvoir
utiliser dans les deux. »

**Droits d'auteur** : on reprend le FORMAT des épreuves (durées, types de tâches, nombre de questions), jamais leur
CONTENU. Aucun texte, aucun son, aucune image des modèles officiels du telc, du Goethe-Institut ou de Klett.

---

## En bref, pour Jacques

- **Il existe déjà beaucoup de choses, et presque tout est commun** : la page « Comprendre l'examen » (elle décrit les
  trois examens), les quatre épreuves de `pruefung.json` (Écouter 120 questions, Lire 22 textes, Écrire 27 tâches,
  Parler 35), la barre de niveau A2 / B1 / C1, Mark Garnier et Anna, le micro, la voix et les vidéos.
- **Propre au DTZ, déjà construit** : l'oral avec Anna et Mark (`dtz-oral.html`, en ligne en essai admin, 23 vidéos), et
  sur une branche pas encore publiée, Écouter et Lire au format DTZ avec l'examen blanc sur 45 (`visuel/prototype/dtz/`).
- **Propre au telc, rien n'existe encore** : les Sprachbausteine, l'ordre lire puis écouter, le courriel à comprendre
  puis à écrire, la réponse courte, les messages de répondeur à noter, l'oral sans image avec l'avis défendu.
  « Comprendre l'examen » le dit d'ailleurs elle-même : « Les Sprachbausteine du telc n'y sont pas encore ».
- **Ce que je propose** : la tuile garde son nom et montre deux grandes cartes, « Se préparer au DTZ » et « Se préparer
  au telc Deutsch A2·B1 ». Chacune ouvre son panneau avec le matériel commun (dans l'ordre de son examen) et ses parties
  propres. Le moteur est le même : la page DTZ reçoit un « profil d'examen » au lieu d'avoir le DTZ en dur.
- **Pour le telc, Mark et Anna jouent les mêmes rôles** : à l'oral, Anna est l'examinatrice et Mark l'autre candidat
  (une répétition, comme au DTZ). À l'écrit, les textes viennent de la vie de Mark à Berlin : son répondeur, ses
  courriels, son courrier.
- **Aucune dépense dans ce plan.** L'oral du telc commence avec la voix du téléphone. Les vidéos viendront plus tard,
  chiffrées : environ 9 $ de Kling et 2 500 crédits ElevenLabs, d'après le coût de l'oral du DTZ. Rien ne sera produit
  sans votre accord écrit dans cette session.
- **Trois questions pour vous**, en bas du document (« À trancher »).

---

## 1. L'inventaire : ce qui existe, et à qui ça sert

C = commun aux deux blocs · D = propre au DTZ · T = propre au telc · G = Goethe B1 ou C1 (ni l'un ni l'autre)

### 1.1 Dans l'app en ligne (`index.html`, `main`)

| élément | où | état | pour |
|---|---|---|---|
| La tuile « Préparation aux examens » | `data-orbid="pruefung"`, `orbPanelData("pruefung")` vers la ligne 44060 | tous ; cachée en espagnol (règle CSS l. 3400) | C, c'est elle qui devient « deux blocs » |
| « Comprendre l'examen » | `<section id="pruefungInfo">`, `openPruefungInfo()` ; textes `pruefung_info_*` de `grammaire.json`, 9 langues | tous | voir le détail ci-dessous |
| — l'intro (trois examens, deux à deux niveaux) | `pruefung_info_intro` | | C |
| — « Les quatre parties, au DTZ » | `pruefung_info_hoeren/lesen/schreiben/sprechen` | | D, mais les durées d'Écrire et de Lire valent presque pour le telc |
| — « Le résultat, au DTZ » (20/45, 33/45, B1 global) | `pruefung_info_resultat` | | D |
| — « DTZ, telc A2·B1, Goethe B1 : ce qui n'est pas pareil » | `pruefung_info_unterschied` | | C (c'est la seule description du telc dans l'app) |
| — « Perdre des points sans faute de langue » (registre, consigne à moitié traitée, silence) | `pruefung_info_regel1-3` | | C |
| — « Et le C1 ? » | `pruefung_info_c1` | | G |
| — la note (le centre d'examen fait foi) | `pruefung_info_note` | | C |
| La barre de niveau A2 / B1 / C1 | `renderPruefungNiveauBar()` | tous | C |
| **Écouter** : 120 questions (40 A2, 40 B1, 40 C1), audio + choix à 3, explication | `pruefung.json` → `hoeren`, `startPruefungHoeren()` | tous, 9 langues | C (format générique, ni Teile du DTZ ni du telc) |
| **Lire** : 22 textes (annonce, Aushang, Hausordnung, lettre d'administration, courriel, forum…) avec questions | `lesen`, `startPruefungLesen()` | tous | C ; les « Forumsbeiträge » et le C1 : G |
| **Écrire** : 27 tâches à remettre dans l'ordre (`chunks`) | `schreiben`, `startPruefungSchreiben()` | tous | Formeller Brief (13) et Informelle E-Mail (6) : C (lettre du DTZ, courriel du telc) ; Kurze Nachricht A2 (3) : C, et base de la « réponse courte » du telc ; Forumsbeitrag (2) : G ; Erörterung C1 (3) : G |
| **Parler** : 35 réponses à reconstruire | `sprechen`, `startPruefungSprechen()` | tous | Über sich sprechen (10) : C ; Über Erfahrungen sprechen (5) : D ; Gemeinsam planen (7) : C ; Fragen stellen A2 (4) : G (Goethe A2) ; Thema präsentieren / Präsentation (5) : G ; Vortrag / Diskussion C1 (4) : G |
| L'essai **`dtz_oral`** « Mark t'aide à préparer le DTZ : l'oral » | option du panneau, `ouvrirDtzOral()`, `ESSAIS.dtz_oral` (admin) | admin, français | D (voir 1.2) |
| Le micro pour la page du cadre | `microPourCadre()`, message « micro » | tous | C (sert à tout oral ouvert dans le cadre) |
| La couverture du vocabulaire | mémoire « Couverture examens A2-B1 » : B1 93,6 %, DTZ 91,2 %, A2 87,1 % | | C ; le telc A2·B1 n'a pas été mesuré à part (à vérifier : existe-t-il une liste propre ?) |

### 1.2 L'oral du DTZ avec Mark et Anna (`visuel/prototype/dtz-oral.html`, en ligne en essai admin)

Session « Préparation au DTZ avec Mark et Anna » (local_6daf28f4…). Je n'y touche pas.

| élément | pour | réutilisable au telc ? |
|---|---|---|
| Le moteur : bulles, vidéo d'abord puis voix puis téléphone, micro ou clavier, mesure par critères, verdict A2 / B1 annoncé par Anna, la limite écrite (ni grammaire ni prononciation), aller directement à une section (4 nov.) | C | oui, tel quel : c'est le cœur de l'oral du telc |
| Partie 1a se présenter (Mark d'abord, en modèle ; mots-clés de la feuille) et 1b la question de suite | C | oui : le telc commence aussi par se présenter et répondre à quelques questions |
| Partie 2a la photo, 2b raconter et comparer | D | non : le telc n'a pas d'image |
| Partie 3 planifier avec Mark (un Ausflug, 5 tours, Mark relance ou se range) | C par la forme | le mécanisme, oui ; le sujet doit changer (un autre projet que l'Ausflug, pour qu'un élève qui fait les deux ne répète pas) |
| Les 23 vidéos Kling et les 25 voix (`visuel/prototype/dtz/video`, `voix`) | D | en partie : `a_danke_mark` (« Und jetzt Sie, bitte. Stellen Sie sich vor. »), `m_ok`, `m_ok2`, `m_nein`, `m_nachfrage`, `a_ende_B1`, `a_ende_A2`, `a_ende_moins` (« im Sprechen ») ; `a_bienvenue` et `m_vorstellung` probablement (à réécouter) ; les autres (photos, Ausflug) non |
| Les juges `JUGES.p1a`, `p1b`, `p3` | C | oui ; le telc demande un juge de plus pour l'avis (voir 3.5) |

### 1.3 Écouter et Lire au format DTZ (branche `claude/dtz-hoeren-lesen-965077`, PAS encore sur `main`)

Session « DTZ : écouter et lire, avec Mark et Anna » (local_4a10c4f4…). Je n'y touche pas.

| élément | pour | réutilisable au telc ? |
|---|---|---|
| `dtz.html` + `commun.js` : voix, minuterie, feuille de réponses, tirage (séries 1-3 réservées à l'examen blanc), inscription des parties (`DTZ.partie()`, `DTZ.examen()`), verdict global | C par nature, D par son texte | oui, si le titre, l'ordre des épreuves et le barème deviennent un **profil d'examen** au lieu d'être fixés (« Le DTZ avec Mark et Anna », 45 questions, 20 et 33) |
| `hoeren-lesen.js`, `donnees/hoeren.json` (4 Teile, 20 items), `donnees/lesen.json` (5 Teile, 25 items), série 1 | D | les **textes** peuvent nourrir l'entraînement du telc (le répondeur de Mark, la radio, les petites annonces), le **format** non |
| Lesen Teil 5 : une lettre formelle à trous, 3 choix par trou | D | c'est presque un Sprachbaustein : **le même moteur de texte à trous sert aux deux** |
| `tests/dtz.py` (format, réponses, feuille non devinable, mots clés au corpus), `outils/relecture.py` → `RELECTURE-DE.md` | D | à généraliser par profil (`tests/examens.py --examen telc`) ou à copier pour le telc |
| Mark Garnier, Gartenstraße 12 ; Hausverwaltung Kern (Frau Brandt) | C | oui, les mêmes personnes dans les deux blocs |
| Les mots clés de chaque item envoyés à la répétition espacée (`etats` / `reponse`) | C | oui |

### 1.4 Ce que l'élève voit aujourd'hui, en résumé

Le panneau montre « Comprendre l'examen », puis Écouter, Lire, Écrire, Parler, et pour l'admin l'oral du DTZ. Rien ne
dit « DTZ » ou « telc » avant d'ouvrir « Comprendre l'examen » ; les exercices mélangent DTZ, Goethe B1 et C1.

---

## 2. Le panneau : un bloc par examen

**Décidé par Jacques le 4 nov.** (`decisions/DECISIONS.md` : « trois blocs », puis « un bloc par examen »). La tuile
montre « Comprendre l'examen » en tête, commun, puis **quatre blocs** : **DTZ**, **telc Deutsch A2·B1**,
**Goethe-Zertifikat B1**, **C1**. Ses mots : « je mettrais des blocs différents si on est capable de nourrir des
blocs de la bonne façon. » Il n'y a plus de ligne « Autres examens ».

**La règle d'ouverture** : un bloc ne s'ouvre aux testeurs que lorsqu'il est nourri au format de son examen, avec
assez d'exercices. D'ici là, il reste en essai admin. Un bloc sans aucun exercice ne s'affiche pas du tout
(`blocNourri()`).

**Construit** (essai `examens_blocs`, 9 langues) :

| bloc | niveaux | ordre des épreuves | les quatre épreuves communes (après filtre) | propre au bloc |
|---|---|---|---|---|
| DTZ | A2, B1 | écouter, lire, écrire, parler | 80 écoutes, 49 questions de lecture, 21 écrits, 22 oraux | l'oral avec Anna et Mark (essai `dtz_oral`) ; bientôt Écouter et Lire au format DTZ |
| telc A2·B1 | A2, B1 | lire, écrire, écouter, parler | 80, 49, 21, 17 (sans le récit sur image du DTZ) | les Sprachbausteine (4 lettres) |
| Goethe B1 | B1 | lire, écouter, écrire, parler | 40, 27, 13, 12 (dont le message de forum et l'exposé) | rien encore |
| C1 | C1 | lire, écouter, écrire, parler | 40, 6, 4, 4 | les feuilles de conjugaison (B2-C1 compris) |

Les 4 « Fragen stellen » (oral A2, au format du Goethe A2) n'entrent dans aucun bloc, puisque aucun des quatre examens
ne les pose. Ils restent dans le panneau d'avant (essai coupé). **Pas de paquet de vocabulaire dans les blocs** : la
v471 l'a retiré de cette tuile, à la demande de Jacques (« ça donne l'impression qu'avec seulement ces mots-là on va
être préparé »). Le vocabulaire par niveau reste dans les paquets de mots.

La section suivante (deux cartes et « Autres examens ») était la première proposition, **remplacée** par celle-ci.

### La forme proposée le 4 nov. au matin (remplacée)

La tuile « Préparation aux examens » ouvre un panneau avec :

1. **Se préparer au DTZ** (grande carte) → ouvre le panneau `pruefung_dtz`.
2. **Se préparer au telc Deutsch A2·B1** (grande carte) → ouvre le panneau `pruefung_telc`.
3. « Comprendre l'examen », qui reste commun (il compare les trois).
4. *Question 2 :* une ligne discrète « Goethe B1 et C1 », qui garde le panneau d'aujourd'hui pour l'exposé, le forum et le C1.

Le panneau de chaque bloc :

| | bloc DTZ (`pruefung_dtz`) | bloc telc (`pruefung_telc`) |
|---|---|---|
| comprendre | « Le DTZ en bref » : les quatre parties, le résultat (les cartes actuelles) | « Le telc A2·B1 en bref » : ses parties dans son ordre, son résultat (nouvelle carte, chiffres relevés dans le manuel) |
| commun, dans l'ordre de l'examen | Écouter → Lire → Écrire → Parler (les exercices de `pruefung.json`, sans Goethe ni C1) | **Lire → Écrire (courriel) → Écouter → Parler**, les mêmes exercices |
| propre | Écouter et Lire avec Mark (Teile du DTZ) · l'oral avec Anna et Mark · l'examen blanc (sur 45) | les Sprachbausteine · le courriel à comprendre puis à écrire · la réponse courte · les répondeurs à noter · l'oral avec Anna et Mark (sans image, l'avis) · l'examen blanc |

Technique : deux entrées de plus dans `orbPanelData()`, deux portes nommées (`ouvrirBlocDtz()`, `ouvrirBlocTelc()`, car
`orbAction()` appelle sans argument), et le retour de `pruefungInfo` vers le bloc d'où l'on vient. **Essai admin
d'abord** (`ESSAIS.examens_blocs`, `etat: "admin"`) : tant que l'essai est coupé, le panneau d'aujourd'hui reste tel quel
pour les élèves. Les titres en 9 langues (fr, en, tr, uk, fa, ar, pt, pl, ru) dès la première version, puisque
l'allemand a ces 9 interfaces. Le parcours `--app de` doit rester à 0 écart tant que l'essai est coupé ; l'espagnol ne
voit pas la tuile.

L'option « l'oral » de l'essai `dtz_oral` passe dans le bloc DTZ telle quelle, avec le titre que lui donne sa session
(« Mark et Anna t'aident à préparer le DTZ »).

### La variante écartée

Une seule liste avec deux en-têtes « DTZ » et « telc » : plus simple, mais le matériel commun apparaîtrait deux fois,
ou une seule fois sous un troisième en-tête « Pour les deux », ce qui renvoie l'élève au mélange d'aujourd'hui.

---

## 3. Ce qui manque au telc Deutsch A2·B1, et comment Mark et Anna y entrent

Source : la page « Comprendre l'examen » de l'app. **Avant de construire, première étape : relever le format exact
dans le manuel officiel du telc A2·B1** (nombre de questions par partie, durées, points, seuils A2 / B1), comme la
session du DTZ l'a fait dans le Prüfungshandbuch, pour le format seulement. Ma recherche du 4 nov. n'a pas trouvé de
tableau officiel en ligne. Aucun chiffre de barème n'est inventé d'ici là.

### 3.1 L'ordre : lire d'abord (45 min), puis écouter (environ 35 min)
- L'examen blanc du telc suit l'ordre réel : Lire → Sprachbausteine, courriel à comprendre, courriel à écrire (35 min
  en tout) → Écouter → la réponse courte (10 min). Minuteries par partie, son entendu le nombre de fois du format.
- Le panneau du bloc range déjà les exercices communs dans cet ordre.
- Mark, en ouverture : « Au telc, on commence par lire. Garde ton énergie pour l'écoute, elle vient tard. »

### 3.2 Les Sprachbausteine (texte à trous, choisir le mot)
- Un courriel ou une lettre à trous ; pour chaque trou, choisir le mot qui convient (le nombre de choix et la forme
  des deux parties, 3 choix par trou ou une liste de mots, sont à relever dans le manuel).
- **Moteur commun avec le Lesen Teil 5 du DTZ** (lettre à trous, 3 choix) : un seul module « texte à trous ».
- Les textes sont ceux de la vie de Mark : un courriel à la Hausverwaltung Kern, une lettre de son école de langue, un
  message à un voisin.
- Après chaque trou, Mark explique en une phrase pourquoi (le cas après la préposition, le verbe à la fin après
  « weil », l'article), avec un lien vers la fiche de grammaire de l'app qui l'enseigne (les fiches et leurs boutons
  M'ENTRAÎNER existent).
- Les mots clés (prépositions, connecteurs, articles) vont à la répétition espacée.

### 3.3 Un courriel à comprendre, un courriel à écrire, une réponse courte
- **Comprendre** : Mark reçoit un courriel (d'une collègue, de son club, de la Hausverwaltung) ; questions au format du
  telc. Les textes de Lire de `pruefung.json` (E-Mail, Behördenbrief) servent à l'entraînement libre.
- **Écrire** : l'élève répond à ce même courriel, à la place de Mark ou pour lui-même. La consigne donne 3 ou 4 points
  à traiter. La page juge sur critères, comme l'oral : les points traités, le registre (du / Sie, formule d'appel et
  salutation qui vont ensemble), la longueur, les connecteurs. Elle dit aussi ce qu'elle ne juge pas (la grammaire).
  Un courriel modèle de Mark, après coup. Les 19 lettres et courriels de `pruefung.json` restent l'échauffement (les
  remettre dans l'ordre).
- **La réponse courte (10 min)** : un message court à qui répondre en quelques phrases (Anna demande si Mark vient
  samedi, un voisin demande un service). Base : les 3 « Kurze Nachricht » A2, à étoffer au B1.

### 3.4 L'écoute qui finit par des messages de répondeur à noter
- Le répondeur de Mark existe déjà au DTZ (Hören Teil 1) : les mêmes voix, un autre format. L'élève **écrit**
  l'information demandée (une heure, un nom, un numéro, un jour), au lieu de cocher.
- Un nouveau type de réponse : la saisie courte, corrigée avec tolérance (« 14 Uhr », « 14:00 », « vierzehn Uhr » ; un
  nom mal orthographié signalé mais compté selon la règle du manuel). Les nombres sont dits en lettres
  (`audio/lectures/de.json`).
- Les autres parties de l'écoute du telc, au format relevé dans le manuel ; les textes du DTZ peuvent servir à
  l'entraînement.

### 3.5 L'oral : environ 15 min, à deux, sans préparation, sans image
Une page `visuel/prototype/telc-oral.html`, **copie du moteur de `dtz-oral.html`** (pas une réécriture : même micro,
même vidéo, mêmes juges), avec l'accord de la session de l'oral. Anna est l'examinatrice, Mark l'autre candidat,
c'est une répétition.

**L'organisation est celle de l'oral du DTZ** (décision de Jacques du 4 nov., « DTZ, l'oral : sections et exercices » :
« Même organisation pour le futur bloc telc »). La session de l'oral du DTZ la construit, et le telc **reprend sa
mécanique** au lieu d'en écrire une autre :
- l'accueil de l'oral liste les sections avec leur état (fait, 2 / 4…) et propose l'examen complet ;
- dans une section, une page par exercice, avec « Section N · titre », des points de progression qu'on peut toucher
  pour sauter à un exercice, « ‹ » vers la liste et « Continuer » en bas ;
- en fin de section, un récapitulatif des réponses et du retour d'Anna, puis Refaire la section, Section suivante ou
  Toutes les sections ;
- l'examen complet enchaîne les sections, avec l'estimation A2 / B1 à la fin seulement.

Seules les sections changent. Le telc en a trois au lieu des cinq du DTZ (1a, 1b, 2a, 2b, 3). Je les écris dans les
données de la page telc quand la mécanique du DTZ sera posée. Les mêmes trois niveaux (liste, exercice, récapitulatif)
valent aussi pour l'écrit du telc (Sprachbausteine, courriels, répondeurs), pour que les deux blocs se ressemblent.

Les trois sections :

1. **Se présenter** et répondre à quelques questions d'Anna : la partie 1 du DTZ, avec d'autres questions de suite.
2. **Planifier ensemble** avec Mark : le mécanisme de la partie 3 du DTZ (Mark propose, relance si c'est trop court, se
   range sur un refus argumenté), avec **un autre sujet** que l'Ausflug du DTZ : par exemple une fête de fin de cours,
   ou aider un ami à déménager. Les points de la feuille sont écrits pour le telc.
3. **Donner et justifier son avis** sur une question à deux points de vue (par exemple « Faut-il avoir une voiture en
   ville ? », « Apprendre une langue en cours ou seul ? ») :
   - Anna pose la question ; Mark donne d'abord son avis, avec une raison et un exemple ;
   - l'élève donne le sien, Mark **réagit** (il est d'accord en partie, ou il objecte poliment), et l'élève doit
     répondre à cette objection ;
   - un nouveau juge `p_avis` : un avis clairement dit (« Ich finde… », « Meiner Meinung nach… »), une raison, un
     exemple, une réaction à Mark (« Da hast du recht, aber… », « Das sehe ich anders, weil… »), une conclusion ou un
     compromis ;
   - Mark ne prend pas toujours le même côté : il défend le côté opposé à celui que l'élève choisit d'abord, pour qu'il
     y ait vraiment quelque chose à quoi réagir.
- Verdict A2 / B1 par partie et global, annoncé par Anna ; les vidéos de fin du DTZ (`a_ende_*`) servent telles quelles.
- La voix : d'abord le téléphone. La vidéo ensuite, **sur accord** : une quinzaine de nouveaux clips (Anna : l'accueil,
  les consignes des parties 2 et 3, les questions de suite, la question d'avis ; Mark : la planification, son avis,
  ses objections), soit environ 9 $ de Kling Avatar v2 Standard et 2 500 crédits ElevenLabs v2, d'après le coût de
  l'oral du DTZ (23 clips, 11,72 $). Chiffre exact annoncé avant.

### 3.6 Le verdict du telc
- Le barème du telc A2·B1 (points par partie, seuils A2 / B1, règle de réussite écrit / oral) est relevé dans le
  manuel, puis rangé dans le profil d'examen. Le verdict sur 45 du DTZ ne s'applique pas tel quel.
- Une carte « Le résultat, au telc A2·B1 » dans « Le telc en bref », à côté de celle du DTZ.

---

## 4. Le moteur commun : un profil d'examen

La page `visuel/prototype/dtz/` de la session « écouter et lire » est construite par inscriptions (`DTZ.partie()`,
`DTZ.examen()`) : elle ne connaît aucune épreuve en particulier. Pour qu'elle serve aux deux blocs, il manque seulement
un **profil** passé à l'ouverture (`?examen=dtz` ou `?examen=telc`) :

```
EXAMENS = {
  dtz:  { titre, ordre: ["H", "L", "S", "Sp"], bareme: {...20/45, 33/45...}, global: regleDtz },
  telc: { titre, ordre: ["L", "SB", "S", "H", "SK", "Sp"], bareme: {...relevé dans le manuel...}, global: regleTelc }
}
```

Chaque module (`hoeren-lesen.js` pour le DTZ, `telc-*.js` pour le telc) ne s'inscrit que dans le profil auquel il
appartient. Les modules communs (le texte à trous, la feuille de réponses, la minuterie, la saisie courte) servent aux
deux.

**Fait par la session « écouter et lire » le 4 nov.** (commit `6595ae0`, branche `claude/dtz-hoeren-lesen-965077`, pas
encore sur `main`). La forme retenue est la sienne : la page telc pose `window.PROFIL_EXAMEN` **avant** de charger
`commun.js` :
- `{id: "telc", titre, intro, sur, a2, b1}`, ou `{id, titre, intro, niveau: points => "b1" | "a2" | "moins"}` quand le
  barème n'est pas une somme à seuils ;
- `id` préfixe le stockage local (`wortando_telc_…`) : les examens blancs du telc ne se mêlent pas à ceux du DTZ ;
- sans profil, c'est le DTZ (45, 20, 33, l'intro de Mark) ; `niveauHL()` et `niveauGlobal()` suivent le profil.

Restent propres au DTZ dans `hoeren-lesen.js` : ses Teile, ses textes et l'ordre écouter → lire. Le module telc reprend
ses fonctions de rendu (`rendreDoc`, `rendreQuestion`, `feuilleReponses`) ; s'il en faut dans `commun.js`, je les
demande à cette session. **Toute autre modification de `commun.js` lui passe en correctif**, pendant que deux autres
sessions s'y branchent.

---

## 5. L'ordre de construction proposé

Le DTZ a priorité jusqu'au 14 novembre (décision du 3 nov.) ; le telc vise la fin novembre. Aucune étape ne touche aux
fichiers des deux sessions DTZ.

| # | quoi | taille | qui touche quoi |
|---|---|---|---|
| 0 | Relever le format officiel du telc A2·B1 (format seul) → `preparation-examens/FORMAT-TELC.md` | petite | moi |
| 1 | **Le panneau à deux blocs**, essai admin `examens_blocs`, 9 langues ; le bloc DTZ reprend ce qui existe, le bloc telc montre le commun dans son ordre et « bientôt » pour le reste | petite | moi, `index.html` (lignes du panneau annoncées aux deux sessions avant) |
| 2 | ~~Le profil d'examen dans `commun.js`~~ **fait** (`6595ae0`, session « écouter et lire ») ; la page telc attend que sa branche arrive sur `main` | — | la session « écouter et lire » |
| 3 | **Les Sprachbausteine**, série 1, avec le moteur de texte à trous commun et les explications de Mark | moyenne | moi : `visuel/prototype/telc/` (ou `dtz/telc-*.js`) |
| 4 | Lire au format du telc et le courriel à comprendre | moyenne | moi |
| 5 | Écrire : le courriel et la réponse courte, jugés sur critères | moyenne | moi |
| 6 | Écouter au format du telc, avec les répondeurs à noter (saisie courte) | moyenne | moi |
| 7 | **L'oral du telc** (`telc-oral.html`, copie du moteur de l'oral du DTZ **avec son organisation sections / exercices / récapitulatif**, ses trois sections à lui), voix du téléphone ; après que la session de l'oral a posé cette organisation | grosse | moi, avec l'accord de la session de l'oral pour copier son moteur |
| 8 | L'examen blanc du telc et son verdict | moyenne | moi |
| 9 | Contrôle `tests/telc.py` (comme `tests/dtz.py`), `RELECTURE-DE.md` pour le germanophone, puis les 8 autres langues d'interface | moyenne | moi |
| 10 | Sur accord : les vidéos de l'oral du telc (chiffrées avant) | dépense | moi |
| 11 | Ouverture aux élèves (`etat: "tous"`) après la relecture germanophone | | Jacques |

Les étapes 0 et 1 peuvent se faire tout de suite après votre accord. Les étapes 3 à 8 sont les « grosses pièces ».

### Où on en est (4 nov. 2026, après le feu vert de Jacques)

Jacques a retenu la proposition du chef : « Ouais, vas-y avec ta proposition. » (`decisions/DECISIONS.md`, 4 nov.,
« le panneau »). La tuile montre donc « Comprendre l'examen » en tête, les deux blocs, puis « Autres examens ».

- **0. Fait** : `preparation-examens/FORMAT-TELC.md`, relevé dans le Übungstest 1 gratuit du telc (format seul). Il
  donne le barème exact : 240 points, 60 par compétence ; B1 = 70 % du total, 70 % dans 3 compétences et 40 % dans
  chacune. Il précise aussi l'oral (≈ 15 min, une minute de réflexion avant la partie 3).
- **1. Fait** (branche, en essai admin `examens_blocs` ; depuis, quatre blocs, voir section 2) :
  - `panneauBlocsExamens()` et `panneauBlocExamen()`, en 9 langues ;
  - `filtreExamen()` : les quatre épreuves communes, sans le C1 ni les tâches du Goethe. Le DTZ garde 80 écoutes,
    49 questions de lecture, 21 écrits et 22 oraux ; le telc garde la même chose, sauf le récit sur image du DTZ
    (17 oraux) ;
  - d'abord « Autres examens » (le panneau d'avant), remplacé le jour même par les blocs Goethe B1 et C1 ;
  - le retour des sous-panneaux vers la tuile (`retourOrbPanel()`) ; sans l'essai, rien ne change.
- **2. Fait** par la session « écouter et lire » : `PROFIL_EXAMEN`, `PROFIL.tuiles` et `commun.css` (`6595ae0`,
  `88d5b79`). Ma branche a fusionné la sienne : elle se publie **après** elle.
- **3. Fait, à relire** :
  - `visuel/prototype/telc/telc.html`, `sprachbausteine.js` et `donnees/sprachbausteine.json` : 4 lettres de Mark
    (la gérance, la Volkshochschule, la fête d'Anna, le club de sport), 10 trous chacune ;
  - une page par trou, des points de progression, un récapitulatif (Refaire / Section suivante / Toutes les sections),
    comme l'oral du DTZ ;
  - le contrôle : `python tests/telc.py` ;
  - ce qui reste : l'interface en français seulement (comme la page du DTZ), aucun mot clé envoyé à la répétition
    espacée, la relecture germanophone.
- **Ensuite** : 4 (Lire et le courriel à comprendre), 5, 6, puis 7 quand l'organisation de l'oral du DTZ sera posée.

---

## 5 bis. Les blocs Goethe B1 et C1 : quand pourront-ils s'ouvrir ?

⚠️ Les formats ci-dessous viennent de ce que je sais des examens, **pas encore d'un relevé** : avant de construire,
les relever dans les modèles gratuits (Goethe : *Modellsatz* B1 et C1 ; telc : *Übungstest* C1), comme pour le telc
A2·B1 (`FORMAT-TELC.md`), et pour le format seulement.

### Goethe-Zertifikat B1

**Le format, à vérifier** : un examen **modulaire**. Chaque module (Lesen, Hören, Schreiben, Sprechen) se réussit
seul, à 60 %, et on peut le repasser seul.
- Lesen, environ 65 min, 5 parties : un blog, des articles, des annonces à associer, des avis, un règlement.
- Hören, environ 40 min, 4 parties : annonces, visite guidée, conversation, débat radio.
- Schreiben, 60 min : un courriel personnel, **un message de forum qui donne son avis**, un courriel formel court.
- Sprechen, environ 15 min, à deux : planifier ensemble, puis **présenter un thème** (expérience, situation dans son
  pays, avantages et inconvénients, avis), puis réagir à l'exposé de l'autre et répondre à ses questions.

**Ce qui existe** :
- les épreuves communes au B1 (40 écoutes, 27 questions de lecture) ;
- 2 messages de forum et 3 exposés à remettre dans l'ordre, et 2 réactions à un exposé ;
- la carte « DTZ, telc A2·B1, Goethe B1 : ce qui n'est pas pareil » ;
- la planification avec Mark (l'oral du DTZ), réutilisable.

**Ce qui manque** :
- les parties de Lesen et de Hören au format Goethe ;
- l'écrit libre (3 tâches jugées sur critères, comme l'écrit du telc) ;
- l'exposé à l'oral : Mark présente d'abord un thème sur quatre « diapositives », puis l'élève fait le sien et
  répond aux questions d'Anna ;
- le verdict par module (60 %).

**L'effort** : du même ordre que le telc, une fois celui-ci fait. La page telc, le moteur commun, l'écrit jugé sur
critères et l'oral en sections servent tels quels ; il faut surtout **écrire les contenus** (au moins 3 séries par
partie) et l'exposé. Ouverture possible **après le telc**, vers la mi-décembre si le telc ouvre fin novembre.

### C1 (Goethe-Zertifikat C1 et telc Deutsch C1)

**Le format, à vérifier** : les deux examens C1 ne se ressemblent pas plus que le DTZ et le Goethe B1.
- Goethe C1 : modulaire ; Lesen, Hören, Schreiben (une prise de position argumentée et un texte formel), Sprechen à
  deux (un exposé, puis une discussion pour convaincre l'autre).
- telc C1 : un bloc écrit avec Lesen et Sprachbausteine, Hören, Schreiben, puis l'oral (exposé, discussion, résumé).

Il faudra sans doute **choisir l'un des deux** comme modèle du bloc, ou faire deux blocs C1 : c'est à Jacques de
trancher, une fois les formats relevés.

**Ce qui existe** :
- 40 écoutes C1 ;
- 2 textes de lecture (un commentaire, un texte documentaire, 6 questions) ;
- 3 argumentations (Erörterung) et 1 lettre formelle à remettre dans l'ordre ;
- 2 exposés et 2 discussions ;
- la carte « Et le C1 ? » (pas de liste officielle de vocabulaire au-delà du B1 ; argumenter, concéder, résumer) ;
- les feuilles de conjugaison B2-C1 (passif, Konjunktiv I, Futur II, participe étendu) ;
- le vocabulaire C1 du cours, dans les paquets de mots.

**Ce qui manque** :
- presque tout le format : les parties de Lesen et de Hören au format choisi ;
- les Sprachbausteine C1, si c'est le telc ;
- l'écrit argumenté jugé sur critères ;
- l'oral (exposé, discussion où Mark défend l'autre camp, ce qui reprend la partie 3 de l'oral du telc) ;
- le verdict.

Les contenus C1 sont plus longs et plus difficiles à écrire juste : la relecture germanophone comptera davantage.

**L'effort** : le plus grand des quatre. Il faut 2 à 3 fois le travail du Goethe B1, à cause de la longueur des
textes et de la relecture. Ouverture possible **après le Goethe B1**, au début de 2027. D'ici là, le bloc reste en
essai admin, avec ce qui existe.

### Le calendrier qui en découle (proposition, pas décision)

| bloc | s'ouvre aux testeurs quand… | date visée |
|---|---|---|
| DTZ | Écouter et Lire, l'écrit, l'oral et l'examen blanc sont faits et relus | 14 nov. (décision du 3 nov.) |
| telc A2·B1 | ses 7 parties, l'oral en sections et l'examen blanc sont faits et relus | fin novembre |
| Goethe B1 | son format est relevé, ses parties et son exposé sont faits et relus | mi-décembre |
| C1 | le modèle (Goethe ou telc) est choisi, son format relevé, ses parties faites et relues | début 2027 |

---

## 6. À trancher par Jacques (tranché le 4 nov.)

1. **La forme du panneau** : deux grandes cartes, chacune ouvrant son panneau (recommandé), ou une seule liste à deux
   en-têtes ?
2. **Le Goethe B1 et le C1** (l'exposé, le message de forum, l'argumentation C1) ne sont ni du DTZ ni du telc. Je
   propose une ligne discrète « Goethe B1 et C1 » qui garde le panneau d'aujourd'hui. Ou faut-il les retirer de la
   tuile ?
3. **Le feu vert** pour construire dans l'ordre du point 5 : d'abord le format, le panneau et les Sprachbausteine, puis
   le reste du telc.

Réponses de Jacques, le 4 nov. (`decisions/DECISIONS.md`) :
- 1 et 2 : un bloc par examen (DTZ, telc A2·B1, Goethe B1, C1), voir section 2 ;
- 3 : feu vert, en commençant par le panneau puis les Sprachbausteine ;
- la relecture germanophone des lettres, c'est lui qui la fera faire : `retours/A-RELIRE-TELC.md`, dérivé par
  `python visuel/prototype/telc/outils/relecture.py`.

Encore ouvert : pour le C1, le modèle (Goethe C1, telc C1, ou deux blocs), une fois les formats relevés.
