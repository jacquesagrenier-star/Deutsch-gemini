# Plan 12 — à relire avant de payer

Épisode 3 « Auf dem Radweg », Wortando. Dossier préparé le 16 septembre 2026
pour une relecture croisée, avant toute nouvelle génération d'image.

---

## 1. L'INTENTION

**À quoi sert ce plan.** Cinq secondes, aucun personnage cadré, pas de
dialogue. Le narrateur dit en allemand :

> *Rot für Räder. Grau für Menschen.*
> (Rouge pour les vélos. Gris pour les gens.)

C'est **la charge utile pédagogique de l'épisode**. Le reste raconte une
histoire — un Québécois arrivé à Berlin marche sur une piste cyclable sans
savoir que c'est une voie de circulation, un cycliste l'arrête et lui fait la
leçon. Ce plan-ci est le seul où l'on enseigne une règle, et c'est celui que
le spectateur doit retenir. L'application est une app d'apprentissage de
l'allemand ; la vidéo sert à faire retenir la phrase.

**Ce qui doit être lisible sans le son et sans le sous-titre.** Deux surfaces
distinctes, et ce que chacune sert :

- le **rouge** sert aux vélos → un pictogramme de vélo peint dessus le dit ;
- le **gris** sert aux piétons → **rien ne le dit pour l'instant.**

C'est le défaut central. La moitié de la phrase allemande n'est pas illustrée.

**Ce qui s'ajoutera ensuite.** La narration allemande (voix ElevenLabs) et un
sous-titre en bas de cadre, produit en cinq langues (fr, en, tr, uk, fa). Et
peut-être, au montage, les deux mots allemands posés sur les bandes
elles-mêmes — « Rot » sur le rouge, « Grau » sur le gris —, ce qui est neutre
pour les cinq langues puisque l'allemand est la cible commune.

**Contraintes de continuité.** Le plan qui précède (plan 06) est une plongée
sur les pieds du personnage **marchant sur la bande rouge** — c'est son
erreur. L'idée retenue est que le plan 12 reprenne **le même cadrage, à la
même hauteur**, avec ses baskets passées **sur le gris** : la coupe entre les
deux plans dit la règle sans un mot, et fait avancer la leçon et le récit au
même moment.

---

## 2. CE QUI A DÉJÀ ÉCHOUÉ, ET POURQUOI

Six versions, cinq payées (0,75 $). L'historique compte, parce que chaque
échec écarte une hypothèse.

| essai | consigne | résultat |
|---|---|---|
| 1 | « on one side… on the other… » | 70 % de rouge, ligne oblique |
| 2 | « split in half down the middle, **each half takes the same width** » | 67–70 % de rouge (mesuré sur 5 hauteurs) |
| 3 | « the photographer is **standing astride** that painted edge, one foot on the red and one on the grey » | une **barre noire peinte** au milieu de l'image, les deux pieds sur le rouge |
| 4 | « the sneakers are **NO LONGER** on the red. They are on the grey » | **DEUX paires** : celles qu'il porte, restées sur le rouge, et une paire vide posée sur le gris |
| 5 | « there is **ONE pair** of shoes and he is wearing it… both soles flat on the grey » | une seule paire — **toujours sur le rouge** |

**Trois enseignements, et ils se recoupent :**

1. **Une proportion abstraite ne se commande pas.** « La moitié », « la même
   largeur » : le modèle compose, il ne mesure pas.
2. **Ce que le prompt nomme, le modèle le fabrique — y compris dans une
   négation.** Dire « elles ne sont plus sur le rouge » a produit une paire
   sur le rouge.
3. **L'image de référence impose la position** comme elle impose un visage.
   Les essais 4 et 5 référençaient la photo des pieds sur le rouge ; les
   pieds y sont restés. (Même mécanisme que plus tôt dans l'épisode : le
   cycliste, généré avec le portrait du héros en référence, est sorti avec
   son visage.)

**Une piste écartée par le calcul, pas par l'opinion.** Ramener la frontière
au centre par recadrage ou par découpe demande de retirer 626 px de rouge, ce
qui laisse une moitié rouge de 455 px — alors que le vélo peint en mesure
857. Il faudrait un cadre de 1954 px de large ; la source en fait 1536. Le
pictogramme est trop gros pour une demi-image **à cette distance de caméra**.

**Une exigence abandonnée.** Le partage 50/50 était un axiome esthétique non
justifié : la phrase a deux moitiés symétriques, donc l'image devait les
refléter. Personne n'apprend mieux parce que les bandes sont égales. Il a été
abandonné au profit du vrai besoin — illustrer *Grau für Menschen*.

---

## 3. LE PROMPT PROPOSÉ

Génération **sans image de référence** (texte seul), précisément pour que rien
ne tire les pieds vers le rouge. Modèle : `nano-banana-pro`, format 9:16, 2K.

```
Looking straight down at a Berlin pavement, vertical frame, as if from the
eyes of someone standing on it. In the lower half of the picture a man's two
white leather sneakers stand side by side, still, both soles flat on GREY
PAVEMENT SLABS, with beige chino trousers coming down into the frame above
them. A straight painted edge runs up the picture to the left of the shoes.
Beyond that edge, filling the left of the frame, a bicycle strip painted a
faded dusty brick red, muted and desaturated, closer to weathered terracotta
than to bright red, with one white bicycle symbol painted on it. Daylight,
overcast and flat.
```

**Ce que la relecture doit chercher :**

- ce prompt peut-il encore produire des chaussures sur le rouge ? si oui,
  qu'est-ce qui, dans sa formulation, le permet ?
- y a-t-il un mot qui nomme une position qu'on ne veut PAS (le piège de
  l'essai 4) ?
- le passage de la plongée subjective à une génération sans référence
  risque-t-il de casser la parenté visuelle avec le plan 06 (teinte du rouge,
  style du pictogramme, hauteur de caméra) ? si oui, comment l'ancrer sans
  réintroduire une référence qui imposerait la position ?
- une autre construction dirait-elle *Grau für Menschen* plus sûrement que
  des chaussures — par exemple un pictogramme de piéton peint sur le gris,
  ou deux personnes marchant dessus ?

---

## 4. LES IMAGES JOINTES

Dans l'ordre de la planche :

1. `bande-rouge-pieds` — le plan 06, ses pieds **sur le rouge** (l'erreur).
   C'est le plan qui précède, et la parenté visuelle à préserver.
2. `deux-bandes-v3` — la plaque actuellement retenue : propre, mais 70/30 et
   surtout **le gris ne dit rien**.
3. `deux-bandes-v5` — l'essai à deux paires de chaussures.
4. `deux-bandes-v6` — l'essai à une seule paire, restée sur le rouge.
