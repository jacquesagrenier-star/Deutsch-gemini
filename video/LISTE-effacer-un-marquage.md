# Effacer un marquage peint d'un épisode — liste de contrôle

Écrite le 23 septembre 2026, après une journée entière passée dessus sur
l'épisode 03. Jacques : « assure-toi de garder dans la checklist tout ce que
tu as fait pour corriger, afin qu'on puisse s'en servir au besoin. »

Le cas traité : retirer les **vélos peints** de la piste cyclable, parce qu'un
vélo peint au sol est un panneau — et tout l'épisode repose sur le fait que
Mark ne lit pas la bande. Avec le pictogramme, le personnage n'est plus
distrait, il est bête.

---

## 0. AVANT TOUT : relire ce qu'on a demandé

**C'est l'étape que j'ai sautée, et elle m'a coûté la demi-journée.**

```bash
grep -n -i "pictogram\|bicycle symbol\|white pictogram" video/episode-NN-*/A-TOURNER.txt
```

Sur l'épisode 03, **quatre prompts nommaient le vélo** — plans 01, 03 et 06
(image *et* mouvement). Le prompt de mouvement du plan 06 disait en toutes
lettres `the white bicycle symbol, all moving past at an even speed`.
J'effaçais image par image ce que mes propres instructions commandaient.

> **Quand on passe du temps à retirer quelque chose d'une sortie, relire
> d'abord ce qu'on a demandé.**

---

## 1. Inventorier — à TAILLE RÉELLE, jamais sur une vignette

Trois fois dans la journée j'ai déclaré un plan propre en le jugeant sur une
vignette de 200 à 300 px. Trois fois c'était faux. Un pictogramme de 150 px
disparaît à cette échelle.

```bash
# la bande de chaque plan, découpée 1:1 sur sa plus grande région rougeâtre
python video/velo_un_plan.py --scene NN-nom --plan N --grille
```

⚠️ **Et échantillonner PLUSIEURS instants par plan.** Sur un plan à caméra
mobile, le marquage entre dans le cadre en cours de plan : au plan 06 il
apparaissait à 2,6 s alors que la première image était propre.

---

## 2. Choisir la route — dans cet ordre

### a) Le prompt (gratuit, et c'est la seule vraie correction)

Retirer la mention du marquage, et **décrire positivement la surface** :

> `The red strip's surface stays plain worn asphalt the whole way, marked only
> by the seams and the hairline cracks in it.`

⚠️ **Jamais une interdiction.** Ces modèles fabriquent ce qu'on leur interdit —
c'est la première règle de `verifier_prompt.py --lecons`.

⚠️ **Et le modèle ajoute le pictogramme DE LUI-MÊME**, même sans qu'on le
nomme : au plan 07, le master était propre et aucun prompt ne parlait de vélo,
et le clip en portait un. Pour lui, le pictogramme fait partie de l'objet
« piste cyclable rouge ». La clause positive est donc nécessaire sur **tout**
plan qui montre la bande.

### b) Le master, puis un plan fixe (gratuit)

Si le plan n'a pas besoin de mouvement (décor immobile, personne de dos) :

```bash
# greffer sur le master, puis
python video/plan_fixe.py --scene NN-nom --plan N --duree 6.5
python video/retenir.py --scene NN-nom --plan N --prise K
```

C'est ainsi que les plans 12 et 17 ont été réglés, à 0 $.

⚠️ `plan_fixe.py` refuse un plan avec un **visage** visible ou un **geste** qui
porte le plan. Une nuque immobile est une nuque immobile ; un visage figé six
secondes se lit comme un arrêt sur image.

### c) Le master, puis régénérer le clip (payant)

Quand le mouvement est nécessaire. Plans 06 et 18 : 2,90 $.

⚠️ **Sur un plan à caméra MOBILE, corriger le master ne suffit JAMAIS** : il ne
fixe que la première image. Le modèle invente le sol à mesure qu'il défile et y
remet ce que le prompt nomme. Il faut **aussi** l'étape (a).

### d) Retoucher le clip (gratuit, mais c'est un contournement)

En dernier recours, et seulement si la caméra est verrouillée.

---

## 3. Retoucher un clip : ce qui marche et ce qui ne marche pas

### Le fond médian est la clé

La caméra est verrouillée dans toute la série : la **médiane par pixel** sur
une quinzaine de trames garde le décor et **jette les passants**. On détecte
donc sur une image où personne ne cache la bande.

⚠️ **Sauf si la caméra bouge** (plan 06) ou si trop de monde traverse le cadre
(plan 07) : le fond médian est alors barbouillé et ne vaut rien.

### La zone : un rectangle ne suffit pas

Une bande en diagonale contre un trottoir de béton clair déborde de tout
rectangle. `zone_suivie()` prend, **ligne par ligne**, le premier et le dernier
pixel rougeâtre : le trottoir est dehors par construction.

### Le seuil : étalonné par plan, jamais global

| plan | couleur au centre de la bande | r−g | g−b |
|------|------------------------------|-----|-----|
| 06   | (173, 96, 84)                | 77  | **+12** |
| 17   | —                            | 60–70 | **−7** |

**La bande n'a pas la même couleur d'un plan à l'autre** : chaque clip est rendu
séparément. Et **la peau passe pour de la bande** — un teint à (210,165,150)
donne r−g = 45. C'est la cause racine de tous mes faux positifs : une main
repeinte en rose, puis un pantalon, puis 126 849 px de masque sur un gros plan
de visage. Le bleu les sépare (`g − b < 4`), mais **pas sur tous les plans**.

### Reboucher : `cv2.inpaint` pour les petites surfaces, la GREFFE pour les grandes

- **Petit glyphe** (≲ 200 × 100 px) → `cv2.inpaint` (Telea). Propre.
- **Grande surface** → `cv2.inpaint` tire la couleur du trottoir voisin et
  laisse une **plaque grise**, pire que le vélo. Il faut **greffer** : recopier
  un morceau de la même bande pris quelques centaines de pixels plus loin, avec
  un bord fondu. Une bande floue et uniforme n'a aucune texture à raccorder,
  donc la greffe est invisible.

⚠️ **La source de la greffe se prend dans le FOND MÉDIAN**, jamais dans l'image
courante : sinon, le jour où quelqu'un passe à l'endroit de la source, on le
greffe sur la piste.

⚠️ **Et vérifier ce que contient la source.** Au plan 18, au-dessus du vélo il y
a le passage piéton : la greffe a ramené ses barres blanches dans la bande.

### Ce qu'aucune retouche ne rattrape

Un marquage qui **dérive** d'une image à l'autre (plan 07). Ce qui se corrige
après coup est ce qui ne bouge pas. Là, il faut le prompt.

---

## 4. Remonter sans détruire le travail

⚠️ **`monter_avatar.py` RÉGÉNÈRE `_montage-avatar/` depuis `03-final/`.** Les
clips retouchés vivent dans `_montage-avatar/` : un remontage les écrase **sans
un mot**.

Deux façons de faire :

```bash
# A. remonter, puis RÉAPPLIQUER les retouches (elles sont des commandes)
python video/monter_avatar.py --scene NN-nom
python video/velo_un_plan.py --scene NN-nom --plan 8 --zone ... --greffe 118
# ...

# B. concaténer soi-même les clips déjà retouchés, dans l'ordre de _ordre.txt
ffmpeg -f concat -safe 0 -i _montage-avatar/_concat.txt -c copy EPISODE-NN.mp4
```

⚠️ **Relire `_plans.json` après CHAQUE remontage** : les instants de la
sonorisation bougent avec les durées. Une reprise qui change un plan de 0,75 s
décale tout ce qui suit.

⚠️ **Et une régénération de clip perd les retouches de montage faites dessus** :
la coupe de tête de 0,75 s du plan 07 a été perdue en le régénérant, et les
cris calés sur les bouches de l'ancienne prise ne tombaient plus.

---

## 5. Vérifier — sur le LIVRABLE, et nulle part ailleurs

**C'est la faute la plus chère de la journée.** J'ai annoncé six plans nettoyés
alors que trois l'étaient, parce que je regardais des comparaisons
avant/après construites sur le **fond médian** et jamais une trame du `.mp4`
final.

```bash
# extraire de vraies trames du fichier livré, à l'instant de chaque plan,
# recadrées sur la bande, à taille réelle
```

⚠️ **Ne jamais filtrer par `tail` la sortie d'un outil auquel on se fie.**
`retenir.py` a REFUSÉ mes prises du plan 17 pendant deux heures — avec le mot
`REFUS` et un code de sortie 1 — parce qu'elles ne partaient pas de l'image
**déclarée** du plan. Mes `tail -1` n'affichaient que la ligne d'explication
qui suit. Le contrôle avait raison ; c'est moi qui l'avais bâillonné.

---

## Récapitulatif de l'épisode 03

| plans | route | coût |
|-------|-------|------|
| 06, 18 | prompt corrigé + master greffé + clip régénéré | 2,90 $ |
| 07 | prompt corrigé (clause de surface nue) + clip régénéré | 0,97 $ |
| 12, 17 | master greffé + plan fixe | 0 $ |
| 02, 03, 08, 10, 19 | retouche du clip (masque au seuil ou greffe) | 0 $ |
| 01 | l'image de Jimmy n'en portait pas | — |

Les zones et seuils exacts sont dans `retours/journal-retours.md`, au
23 septembre 2026.
