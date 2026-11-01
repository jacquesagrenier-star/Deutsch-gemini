# Scènes de Camille — les 35 (1er nov. 2026)

> Pour Jacques. Tout le japonais est un **brouillon** : il attend un natif.
> Planche des 32 images faites : `.claude/planche-scenes-camille.jpg`
> (dossier OneDrive du projet). Les scènes 2, 3 et 4 sont les prototypes d'avant
> Camille (eki, konbini, genkan), gardés tels quels.

Ce que tu as demandé le 1er nov. : « Fait la suite des 28 autres images […].
Puis crée les autres personnages. Les mots qui manquent. Puis la scène 35. »

## Ce qui est fait

1. **Les personnages** : Yui, Fumiko, Hiroshi, M. Sakamoto et Mme Kimura ont
   leur image de face (`personnages/<Nom>.png`, `video/personnages_japonais.py`).
   Ishida-sensei vient de la scène du cours, découpé (gratuit). Planche :
   `.claude/planche-personnages-camille.jpg`.
2. **Les 28 images** (27 + la scène 35), chacune avec ses personnages en
   référence, puis **zones, masques SAM 2 et lexique**, comme le pilote :
   24 à 38 zones par scène. Chaque masque a été regardé sur un rendu de ses
   contours ; quand SAM débordait (lanternes, plafonniers, néons), la zone a été
   redessinée en ellipses ou retirée.
3. **Les mots qui manquaient** : sur les 137, **43 étaient déjà au corpus**, en N2
   et N1 (浴衣, 花火, 鳥居, こたつ, 新幹線, 銭湯…). Les outils des scènes ne
   lisaient que le N5-N3. Les **87 autres** entrent par un catalogue,
   `japonais/cartes/scenes.json`, sur le modèle des expressions : id JMdict,
   lecture, traduction, domaine, et une note quand il le faut. Ils rejoignent les
   thèmes de l'app (`japonais/datos/themes.json` : 1 643 → 1 730 noms). Un seul
   mot reste hors corpus, **兼六園** (le nom du jardin), qui n'est pas dans JMdict.
   En passant, j'ai réparé `japonais/datos/construire.py`, qui s'arrêtait sur la
   ponctuation des expressions (« …と申します », « はい、チーズ ») ; les 164
   expressions du 25 oct. entrent donc aussi dans les données.
4. **La scène 35** (tu me l'as laissée) : **Ben**, un nouvel élève australien du
   cours de kanji, arrive au même parc qu'à la scène 7. C'est Camille qui
   l'accueille maintenant, en japonais poli. **Camille reste une deuxième
   année** : elle s'inscrit dans une école de japonais et garde ses heures au
   café. Un emploi de serveuse ne donne pas de visa de travail au Japon, d'où
   l'école. Le détail est dans la bible, scène 35.

## Les retouches

- **Sept reprises payées**, parce que le gag ne se voyait pas ou que l'image
  sentait le dessin :
  - le parapluie (11), maintenant jaune et minuscule ;
  - le colis (13), qui lui monte au menton ;
  - le rapace (22), qui était un oiseau flou ;
  - le renard (23) : elle le photographiait au lieu de le regarder dans les yeux ;
  - la table chauffante (30), qui était un dessin ;
  - le grand magasin (28) : le sac dans le sac était invisible ;
  - l'izakaya (26) : un collègue de trop.
- **Des kanji effacés à la main, gratuitement** (`effacer_texte.py`), parce
  qu'une scène ne porte jamais de mots :
  - les enseignes de la fête d'été (20) ;
  - les planchettes du menu de l'izakaya (26) ;
  - le carafon du réveillon (32) ;
  - deux caractères gravés, une plaque et une enseigne au sanctuaire (33).

## Coût

| | |
|---|---|
| Pilote (31 oct.) | 0,60 $ |
| Les cinq personnages | 0,75 $ |
| Les 27 images | 4,05 $ |
| 7 reprises + la scène 35 | 1,20 $ |
| **Total** | **6,60 $** (plafond 7,50 $) |

## Ce que je n'ai pas réglé

- **L'aéroport du père (31)** : les gens n'occupent que le milieu de l'image,
  avec beaucoup de plafond et de sol. C'est jouable, mais moins réussi que les
  autres ; une reprise coûterait 0,15 $.
- **Le gag de Kamakura** : c'est un faucon et non un milan (トンビ). La zone
  dit 鳥, « oiseau », donc c'est juste.
- **Les petits défauts de contour** : quelques assiettes et baguettes de
  l'izakaya et de la table chauffante ont des bords approximatifs ; on les
  touche quand même.
- **Rien n'est branché dans l'app** : `construire_scenes.py` ne connaît que
  konbini, eki et genkan. Les **couches N4 et N3** (les questions de chaque
  scène) ne sont pas écrites ; elles s'écrivent pour le japonais, elles ne se
  traduisent pas.
- **Les prototypes** eki, konbini et genkan datent d'avant Camille : elle n'y
  est pas.
- **Un natif** doit relire tout le japonais : les mots du catalogue, les
  lectures et les traductions.
