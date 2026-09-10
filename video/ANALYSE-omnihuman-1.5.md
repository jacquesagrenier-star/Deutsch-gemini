# OmniHuman 1.5 — ce qui est publié, et ce que ça vaut pour nous
### 10 septembre 2026

La veille du 9 septembre désignait OmniHuman 1.5 comme « la piste la plus
prometteuse », sur la foi de la fiche Artlist et de deux blogues. Voici ce que
disent le papier de recherche, la page officielle du projet, les plateformes
qui le revendent et les gens qui l'ont essayé.

**Le résultat principal est un désaveu partiel de la veille d'hier**, et il
vient des tableaux du papier lui-même.

---

## 1. Le chiffre que personne ne cite : le « 1.5 » n'achète pas de lip-sync

Le papier (*OmniHuman-1.5: Instilling an Active Mind in Avatars via Cognitive
Simulation*, ByteDance, arXiv 2508.19209) publie ses mesures. Sur **Sync-C**,
la métrique de synchronisation labiale — plus haut vaut mieux :

**Table 4 gauche — animation de portrait, jeu de test CelebV-HQ** (c'est notre
cas : un visage, cadrage serré)

| méthode | IQA ↑ | ASE ↑ | **Sync-C ↑** | FID ↓ | FVD ↓ |
|---|---|---|---|---|---|
| SadTalker | 2,953 | 1,812 | 3,843 | 36,648 | 171,848 |
| Hallo | 3,505 | 2,262 | 4,130 | 35,961 | 53,992 |
| EchoMimic | 3,307 | 2,128 | 3,136 | 35,373 | 54,715 |
| Loopy | 3,780 | 2,492 | 4,849 | 33,204 | 49,153 |
| Hallo-3 | 3,451 | 2,257 | 3,933 | 38,481 | 42,125 |
| **OmniHuman-1** | 3,875 | 2,656 | **5,199** | 31,435 | 46,393 |
| **OmniHuman-1.5** | 3,817 | 2,663 | **5,053** | 31,320 | 45,771 |

**Table 4 droite — corps entier, jeu de test CyberHost**

| méthode | Sync-C ↑ | FID ↓ | FVD ↓ | HKC ↑ | **HKV ↑** |
|---|---|---|---|---|---|
| Skyreel-A1 | 2,983 | 69,619 | 70,678 | 0,786 | 28,840 |
| FantasyTalking | 3,548 | 52,332 | 47,052 | 0,838 | 18,845 |
| OmniAvatar | 6,589 | 42,163 | 43,998 | 0,795 | 56,574 |
| MultiTalk | 6,868 | 37,308 | 32,783 | 0,817 | 62,753 |
| **OmniHuman-1** | **7,443** | 31,641 | 27,031 | 0,898 | 47,561 |
| **OmniHuman-1.5** | **7,243** | 31,160 | 27,642 | 0,875 | **72,113** |

**Dans les deux tableaux, la version 1.5 est légèrement EN DESSOUS de la
version 1 sur le lip-sync.** Et le papier le dit lui-même, sans détour :

> « In the portrait scenario, our model **performs on par with the strong
> OmniHuman-1 baseline**. We attribute this to the limited motion range in
> portrait videos, which challenges objective metrics in capturing subtle
> facial expressiveness. »

**Ce que le 1.5 apporte vraiment est dans la dernière colonne : HKV, la
dynamique des gestes — 72,1 contre 47,6, soit +52 %.** C'est là qu'est la
contribution, et elle est cohérente avec l'architecture : un grand modèle de
langue lit le SENS de la réplique et planifie la performance (« System 2 »),
un transformeur de diffusion la rend (« System 1 »). On n'a pas amélioré la
bouche : on a ajouté une tête qui décide de ce que le corps fait.

### Pourquoi ça nous concerne précisément

Nos plans sont des **gros plans verticaux** d'une personne dans un hall
d'aéroport. La dynamique des gestes à grande échelle est exactement l'axe que
nous n'utilisons pas — et c'est le seul où le 1.5 gagne. L'axe dont nous avons
besoin, la précision de la bouche, est celui où il fait jeu égal avec son
prédécesseur, voire un cheveu en dessous.

⚠️ **La fiche Artlist dit l'inverse** : *« prioritizing lip-sync precision over
general motion »*. Ce n'est pas ce que mesure le papier. C'est une formule de
catalogue, et je l'ai reprise telle quelle hier.

---

## 2. Ce qui reste vrai, et qui ne dépend d'aucun classement

**L'argument structurel tient entièrement.** Il ne repose pas sur un score :

Seedance reçoit une fenêtre de parole ÉCRITE DANS LE PROMPT et fait ce qu'il
veut de ces nombres — mesuré hier : de +0,11 à +1,96 s d'écart sur six prises.
Un modèle **piloté par l'audio** n'a pas de fenêtre demandée à ignorer : le son
conditionne chaque instant de la génération. **Le décalage d'attaque qu'on
mesure depuis deux jours ne peut pas exister dans cette famille.** Ce n'est pas
un avantage de degré, c'est un défaut qui disparaît.

Et sur le classement absolu, la famille OmniHuman mène bien : 7,44 et 7,24
contre 6,87 (MultiTalk) et 6,59 (OmniAvatar). Le blogue qui disait
« OmniHuman mène pour la constance du lip-sync » avait raison — mais pas grâce
au 1.5.

---

## 3. Ce que le papier ne dit pas, et qui manque

- **Aucune section de limites, aucun cas d'échec.** Pour un papier de cette
  ampleur, c'est notable. La seule discussion de risque porte sur les usages
  malveillants.
- **Aucune ligne « vérité terrain ».** Les tableaux donnent Sync-C pour huit
  méthodes et jamais pour de la vraie vidéo. On ne peut donc pas savoir si
  5,053 est proche du réel ou loin. **C'est exactement le piège où notre mesure
  en dB nous a mis quatre fois** : une échelle sans étalon ne dit pas où l'on
  est, seulement qui est devant qui.
- **Pas un mot sur les langues.** 15 000 heures de vidéo filtrée, des jeux de
  test tournés vers l'anglais (CelebV-HQ, c'est du visage de célébrité). Le
  trou est le même qu'hier : **zéro preuve sur l'allemand.**

---

## 4. Les spécifications utiles pour décider

| | ce qui est publié |
|---|---|
| entrée | une image + une piste audio, **plus un prompt texte facultatif** |
| résolution | **480p en base**, un modèle de super-résolution séparé monte à 720p/1080p |
| durée | le papier annonce « plus d'une minute » par génération autorégressive ; les plateformes plafonnent à **30 s** (60 s en 720p chez certaines) |
| locuteurs | un seul par piste, mais le multi-personnage existe en routant une piste par personnage |
| caméra et fond | la page officielle montre la caméra qui **suit, zoome et tourne autour** du sujet, à partir d'une seule image |

Deux points valent d'être retenus. **Le 480p natif** : ce qu'on voit en 1080p
est remonté après coup, ce qui n'est pas la même chose qu'une génération native
— à regarder de près sur une bouche en gros plan. Et **la caméra qui bouge et
le fond qui vit** répondent, sur leurs exemples au moins, à l'inquiétude posée
hier : « un modèle avatar anime une image fixe, nos plans ont un hall vivant
derrière ».

---

## 5. Ce que rapportent ceux qui l'ont essayé

Un comparatif pratique (GoTranscript, une entreprise de transcription — elle ne
vend pas d'avatar), qui met OmniHuman face à Créatify Aurora et WAN 2.6 :

> « a smile all the way through and **we see a lot of teeth** with the
> lip-sync »
>
> il « **took the longest to generate** » des trois, et coûte plus de crédits
> qu'Aurora
>
> « I **had to prompt it multiple times** to get the result I was looking for »

**Le sourire permanent est un risque réel pour notre épisode**, et il porte un
nom depuis hier : c'est un défaut de **synchronie cinétique** — l'expression
contredit les mots. Mark arrive d'un vol de nuit et demande son chemin ; Anna
est une employée d'aéroport polie. Un visage qui sourit toutes dents dehors du
début à la fin dirait autre chose que la réplique.

**Et une critique à écarter, mais qu'il faut avoir lue.** Le premier résultat
« critique » du web s'intitule *« OmniHuman 1.5 Review 2026: Zero Scenarios It
Wins »*. Le titre promet une démolition ; l'article ne relève **aucun artefact,
aucune erreur de synchronisation, aucune mesure**. Son reproche réel est que le
prix n'est pas présenté comme celui des concurrents — et il recommande trois
fois les produits de son propre éditeur. À classer avec les blogues d'hier.

---

## 6. Le prix, hors Artlist

| plateforme | tarif |
|---|---|
| WaveSpeedAI | 0,12 $/s |
| fal (OmniHuman-1) | 0,14 $/s |
| fal (OmniHuman-1.5) | 0,16 $/s |

Pour nous : **un plan de 5 s coûte 0,60 à 0,80 $**, les douze plans **7 à
10 $**. À comparer aux 2 400 crédits Artlist du re-tournage Seedance. Même si
le coût en crédits chez Artlist se révélait mauvais, cette piste reste
accessible ailleurs pour le prix d'un repas.

---

## 7. Ce que j'en conclus

**a) L'essai reste à faire, pour la raison structurelle — pas pour le score.**
Le décalage d'attaque disparaît par construction. C'est le seul argument qui
compte, et il survit intact à la lecture des tableaux.

**b) Essayer OmniHuman-1 aussi, si Artlist le propose.** Sur le portrait, c'est
lui qui a le meilleur Sync-C des deux (5,199 contre 5,053), et il est moins
cher partout ailleurs. Le catalogue nous pousse vers le numéro le plus élevé ;
la mesure ne le justifie pas pour un gros plan.

**c) Deux défauts à guetter, nommés d'avance pour ne pas juger à l'impression :**
1. **Le sourire permanent et les dents.** L'expression doit correspondre à la
   réplique, pas à la moyenne des vidéos d'entraînement.
2. **La bouche sur p/b/m, f/v/w, a/ä et u/o/ü/ö** — la liste d'hier. Rien
   d'autre n'est visible en gros plan.

**d) C'est le moment d'installer SyncNet.** On va devoir comparer une prise
OmniHuman à une prise Seedance + sync.so. Notre mesure en dB s'est trompée
quatre fois et `controler_bouche.py` dit lui-même qu'il ne peut pas arbitrer
une qualité. Sans étalon commun, cet essai se jugera à l'œil — c'est-à-dire
comme les précédents.

**e) Ce que l'essai ne pourra pas dire.** Aucune source ne mesure l'allemand,
et un plan ne fait pas une preuve. Mais un plan mesuré vaut mieux que dix
blogues, et nous n'avons rien de mieux à espérer du web sur ce point.

---

*Sources : arXiv 2508.19209 (papier OmniHuman-1.5, ByteDance) — tableaux et
citations vérifiés dans le texte ; page officielle omnihuman-lab.github.io/v1_5 ;
tarifs fal.ai et WaveSpeedAI ; comparatif pratique GoTranscript ; revue Versely
(écartée, intérêt commercial déclaré dans le texte).*
