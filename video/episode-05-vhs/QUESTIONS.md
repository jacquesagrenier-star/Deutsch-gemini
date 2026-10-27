# Les deux épisodes suivants : ce qui reste à trancher

Préparé le 26 oct. 2026 (nuit), à la demande de Jacques : « prépare le prochain épisode vidéo
pour l'allemand et le prochain épisode vidéo pour l'espagnol ». **Rien n'est généré ni payé.**
Pour chaque point, une proposition et sa raison ; c'est à Jacques de trancher. Les feuilles
partent sur la proposition tant qu'il n'a rien dit.

| Épisode | Plans | Images | Coût estimé |
|---|---|---|---|
| 05 « Zweiter Stock » (VHS, allemand) | 17 (12 parlés) | 15 | ≈ 8,60 $ (≈ 10 $ si tout le décor est animé) |
| es-05 « La tienda de Ana » (espagnol) | 20 (14 parlés) | 10 | ≈ 7,15 $ (≈ 8,60 $) |
| **Total** | | **25** | **≈ 15,75 $** + une réserve de 2 $ par épisode pour les reprises |

Voix ElevenLabs : environ 1 700 crédits pour les deux, plus deux voix neuves pour le 05.

Fichiers :
- 05 : `scenes/05-vhs.json` et `video/episode-05-vhs/A-TOURNER.txt` (`SCENARIO.md` garde l'histoire) ;
- es-05 : `scenes/es-05-la-tienda.json` et `video/episode-es-05-la-tienda/A-TOURNER.txt` ;
- prompts des répliques : `video/prompts_repliques_suite.py`.

Contrôle `video/verifier_prompt.py` : **0 faute et 0 doute** sur les 26 prompts de répliques et
les 25 prompts d'images.

---

## Allemand : 05 « Zweiter Stock »

C'est le scénario v2 du 24 oct. Mark et Anna sont au même cours d'espagnol. Il apprend son
prénom de la bouche de la prof, et ils découvrent qu'ils habitent la même rue.

**0. Un point corrigé, à confirmer.** Dans le v2, Mark arrivait au **troisième** étage. C'est
faux. Qui compte comme à Montréal (le rez-de-chaussée = 1) monte un escalier de **moins**, pas
un de plus. Il arrive donc au **premier**, se croit au deuxième, et le Hausmeister lui récite :
« Erdgeschoss, erster Stock, zweiter Stock. Wir fangen bei null an. » Le gag et la leçon sont
les mêmes, mais un germanophone aurait vu l'erreur de calcul.

**1. La rue : la Lenaustraße (Neukölln, Reuterkiez) ?**
- **Proposition : oui.** C'est une vraie rue, courte, facile à dire, et peu connue : elle
  ancre le Kiez de Mark sans en faire une carte postale.
- Seul effet : le quartier de la série devient Neukölln. Aucun épisode n'a nommé le quartier
  jusqu'ici, donc rien ne le contredit.
- Autre choix : une rue inventée, si l'on préfère ne pas donner une vraie adresse (les
  numéros 8 et 12 existent).

**2. La même rue, pas le même immeuble (8 et 12) ?**
- **Proposition : oui.** C'est assez près pour se croiser (boulangerie, Späti, U-Bahn), et
  assez loin pour ne pas être voisins de palier, ce qui irait trop vite pour l'arc.

**3. La fin : le « du » taquiné, ou une fin sobre ?**
- **Proposition : le taquiné.**
  - Mark : « Auf Spanisch duzen wir uns schon… »
  - Anna : « Auf Deutsch noch nicht. »
  - Le narrateur : « Auf Spanisch: du. Auf Deutsch: noch Sie. Noch. »
- Pourquoi :
  - cette fin enseigne *duzen / siezen* ;
  - elle joue le trait d'Anna (l'humour sec) ;
  - elle **promet** le sommet de la série sans le **dépenser**.
- Pas de flirt : c'est une règle de politesse dite en souriant.
- Ils repartent ensemble de dos, puisqu'ils vont dans la même rue.
- Autre choix, plus sobre : « Bis nächsten Dienstag, Mark. »

**4. La voix du Hausmeister.**
- **Proposition : Voice Design, trois aperçus à écouter**, comme pour la boulangère le 23 oct.
  Une voix conçue n'appartient à personne.
- Profil : homme de 60 à 65 ans, Berlinois, voix grave et un peu rocailleuse, posée, **neutre**.
- Il porte la pointe sans la jouer, comme le Beamter de l'épisode 2, mais avec une autre voix.

**5. La voix de Carmen**, la prof, qui ne parle qu'espagnol.
- **Proposition : une voix de bibliothèque castillane**, femme de 50 à 55 ans, utilisée par son
  ID. On en propose trois à l'écoute, et l'accent est mesuré (`accent_es.py --v2`), comme pour
  Lucía.
- ⚠️ **Pas une voix de la série espagnole** (Lolita, Monica, Eva Dorado) : c'est la même raison
  que pour les visages.
- Anna et Mark disent leurs répliques espagnoles avec **leur** voix. Leur accent de débutants
  est voulu.

**6. La tenue de Mark : une doudoune marine ouverte sur un pull gris clair, gardée en classe ?**
- **Proposition : oui.** Il arrive en retard et s'assoit tout de suite : le récit le justifie.
- C'est aussi une image de référence de moins.
- Anna garde exactement sa tenue de 04 (manteau rouille), qui la fait reconnaître.

**7. « Pfand » devient l'épisode 06.** Rien à décider : on renumérote `05-pfand` le jour où le
05 est tourné.

## Espagnol : es-05 « La tienda de Ana »

**1. Pourquoi cet épisode.**
- Le document « La série espagnole : les scénarios » prévoyait :
  - en 4 « El metro », remplacé par « ¿Tú o usted? » ;
  - en 5 « La tienda de Ana ».
- **Proposition : la boutique.** C'est l'arc annoncé depuis le 21 oct. : la boutique d'Ana, les
  vêtements et les tailles, la bise.
- Il est réécrit pour tenir compte de ce qui a été tourné : Ana a déjà retrouvé Mark au bar
  (es-03). Elle le reconnaît (« ¡El chico del café! ») et il découvre que la boutique est à elle.
- « El metro » reste disponible pour un épisode suivant.

**2. Les prénoms ici ?**
- **Proposition : oui.** Ils ne les ont jamais échangés d'es-01 à es-04.
- « Por cierto… me llamo Ana. » « ¡Yo soy Mark! Encantado. »
- C'est le pas de l'arc espagnol, et ils restent au « usted ».

**3. Les trois écarts Mexique / Espagne : à valider.** Tous sont vrais :
- *chamarra / chaqueta* ;
- les tailles : CH-M-G au Mexique (*chica, mediana, grande*), *pequeña* en Espagne. À Madrid,
  « chica » veut dire une fille, d'où « ¿Chica? ¡Usted es un chico! » ;
- une bise au Mexique, deux à Madrid.

En plus, un gag **muet** : Mark (1,86 m) dans la petite veste.

**4. La chute : la bise ratée.**
- **Proposition : une image fixe.** Mark a fait **une** bise et recule. Ana, penchée par-dessus
  le comptoir, tend la joue **dans le vide** pour la deuxième. Puis : « ¡Dos, Mark! ¡Aquí son dos! »
- C'est comique et non romantique : un salut raté, sans faute de personne.
- Autre choix, sans contact :
  - la fin s'arrête aux prénoms ;
  - le narrateur dit la règle sur le plan d'ensemble (« En Madrid, dos besos »).

**5. Ana, patronne de la boutique ?**
- **Proposition : oui.** C'est ce que dit le document des scénarios (« a une boutique ») et
  c'est son moment : « Es mi tienda. »
- Autre choix : elle y travaille.

**6. La devanture en bleu.** Elle ne doit pas rappeler la boulangerie vert foncé de Berlin.
Un détail, signalé pour qu'on n'ait pas l'impression d'un décor recyclé.

**7. Aucune voix neuve.** Le narrateur est David Martin, Mark garde sa voix et Ana est Lolita.

---

## Ensuite, sur l'accord de Jacques

Pour chaque épisode :
1. les images, en commençant par le plan d'ensemble, regardé avant tout portrait ;
2. les voix ;
3. les clips Kling et H3 ;
4. le montage et les sous-titres (9 langues pour l'allemand, fr et en pour l'espagnol).

À faire **avant** les sous-titres :
- **05** : quatre répliques sont en espagnol (champ `langue_dite`). Il faut vérifier que
  `video/sous_titres.py` ne leur colle pas un mot à mot allemand.
- **05** : les traductions des 7 autres langues sont écrites, mais pas encore relues par un
  autre modèle.
- **es-05** : la note discrète « chaqueta (Espagne) · chamarra (Mexique) » ne s'incruste pas
  encore. C'est un manque déjà relevé pour es-02.
