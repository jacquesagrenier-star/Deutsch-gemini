# Les quatre épisodes suivants -- à valider avec Jacques

Préparés le 22 oct. 2026 pendant son absence (« prépare les deux prochaines vidéos : deux de plus
en espagnol, deux de plus en allemand ; on regarde ça ensemble à mon retour »). **Rien n'est
généré** : ni image, ni voix, ni clip. Ce fichier fixe l'histoire de chaque épisode ; l'écriture
complète (scènes, géographie, prompts) suit dans `scenes/` et `video/episode-*/A-TOURNER.txt`.

Le fil des deux séries : chaque épisode est une démarche du quotidien ET une différence de langue
ou de culture qui fait rire (le Bürgeramt, le feu rouge ; « carro / coche », « ahorita »). Ton :
humour, sourires, personnages attachants. Les règles de `.claude/histoire-personnages.md` tiennent :
pas de flirt, Anna sans compagnon, la famille de Mark loin.

---

## Espagnol (A1) -- Mark en Madrid

### es-03 « El café » -- les retrouvailles au bar
- **Lieu :** un bar de quartier à Madrid, le matin (comptoir en zinc, tostadas, machine à café).
- **Le gag :** Mark commande à la mexicaine, « ¿Me regala un café? » (au Mexique : « donnez-moi »).
  En Espagne, « regalar » veut dire offrir : le serveur, hilare, « ¿Regalar? ¡Aquí se paga! ».
- **Les retrouvailles :** au comptoir, Ana (l'aéroport, épisode 1) le reconnaît : « ¡El chico del
  aeropuerto! ». Elle lui souffle la formule de Madrid : « ¿Me pones un café? ».
- **La suite :** le serveur : « ¿Solo, cortado o con leche? » ; Mark ne connaît pas « cortado » ;
  Ana commande « un café con leche y una tostada con tomate », Mark l'imite.
- **La fin :** le narrateur, le lendemain : Mark entre et dit, du premier coup, « ¿Me pones un
  café? ». Le serveur : « ¡Muy bien, mexicano! ».
- **Ce qu'on apprend :** commander au bar, les trois cafés, le petit-déjeuner espagnol, regalar /
  poner. Ana reste chaleureuse, rien de plus (pas de flirt).

### es-04 « ¿Tú o usted? » -- le premier jour au travail
- **Lieu :** un bureau moderne et clair à Madrid, le lundi de son premier jour.
- **Le gag 1 :** Mark, poli à la mexicaine, vouvoie tout le monde. Lucía, collègue d'une trentaine
  d'années : « ¡Tutéame, hombre! Aquí todos nos tuteamos. »
- **Le gag 2 :** Mark demande au groupe « ¿Ustedes comen aquí? » ; Lucía : « Aquí decimos
  vosotros. » Mark : « ¿Vosotros… coméis? » (le verbe change aussi).
- **Le retournement final :** dans l'ascenseur, Mark, fier, tutoie un monsieur âgé : « Hola, ¿qué
  tal estás? » Le monsieur : « ¡De usted, joven! » (avec les aînés, on vouvoie encore). Puis on
  apprend que c'est le directeur.
- **Ce qu'on apprend :** tú / usted en Espagne, vosotros / ustedes, se présenter au travail.

## Allemand (A2) -- Mark in Berlin

### 04 « Schrippe » -- les retrouvailles à la boulangerie
- **Lieu :** une boulangerie du Kiez de Mark, le matin.
- **Le gag :** Mark : « Ein Brötchen, bitte. » La boulangère berlinoise : « Hier heißt das
  Schrippe! ». Puis il demande « einen Pfannkuchen » et reçoit un beignet : à Berlin, un
  « Pfannkuchen » est ce que le reste de l'Allemagne appelle un « Berliner ».
- **Les retrouvailles (l'arc de la série) :** derrière lui dans la file, Anna, en vêtements de tous
  les jours, le reconnaît : « Sind Sie nicht… der Mann vom Flughafen? ». Toujours Sie. Elle explique
  Schrippe / Semmel, Pfannkuchen / Berliner, et conclut : « Und ein Berliner… das bin ich. »
- **La fin :** le narrateur : « Mark kennt jetzt drei Wörter für Brot. Ihren Namen kennt er noch
  nicht. » (le prénom reste pour plus tard).
- **⚠️ À trancher :** l'arc prévoyait les retrouvailles « à l'épicerie » (idée de Jacques) ; la
  boulangerie sert mieux le gag des mots. À choisir au retour.

### 05 « Pfand » -- la consigne
- **Lieu :** devant un Späti, le soir, puis l'automate de consigne d'un supermarché.
- **Le gag :** Mark jette sa bouteille vide à la poubelle. Un voisin (homme d'une cinquantaine
  d'années) : « Halt! Das ist doch Pfand! » Vingt-cinq centimes la bouteille ; Mark n'y croit pas.
- **La suite :** Mark rapporte un sac de bouteilles à l'automate ; une est refusée (pas de logo).
  Il reçoit son ticket : 2,40 €.
- **La fin :** Mark pose la bouteille refusée À CÔTÉ de la poubelle (la coutume berlinoise, pour
  ceux qui ramassent les bouteilles). Le voisin hoche la tête : « Jetzt sind Sie ein Berliner. »
- **Ce qu'on apprend :** Pfand, les nombres et les prix, le Späti, une coutume de la ville.

---

# ÉTAT AU RETOUR DE JACQUES -- tout est écrit, rien n'est généré

Écrits par deux agents Fable d'après les histoires ci-dessus, puis contrôlés :
`verifier_prompt.py --scene` → **0 faute, 0 doute sur les quatre**. Les prompts des épisodes déjà
tournés (es-01, es-02) sont inchangés.

| Épisode | Plans | Images à faire | Coût estimé |
|---|---|---|---|
| es-03 « El café » | 18 | 8 | ≈ 9,15 $ |
| es-04 « ¿Tú o usted? » | 19 | 10 | ≈ 9,45 $ |
| 04 « Schrippe » | 18 (13 parlés) | 10 | ≈ 8,60 $ (7,80 avec deux plans fixes) |
| 05 « Pfand » | 19 (9 parlés) | 14 | ≈ 9,20 $ (8,00 avec trois plans fixes) |
| **Total** | | **42** | **≈ 36 $** + crédits ElevenLabs pour les voix |

Fichiers : `scenes/es-03-el-cafe.json`, `scenes/es-04-tu-o-usted.json`, `scenes/04-schrippe.json`,
`scenes/05-pfand.json` ; une feuille `A-TOURNER.txt` par épisode (géographie, objets, ordre de
fabrication, devis) dans `video/episode-*/` ; les prompts des répliques dans
`video/episode-*/_essai-avatar/prompts/` (générés par `video/prompts_repliques_es.py` et le nouveau
`video/prompts_repliques_de.py`).

## Les nouveaux personnages (voix à choisir à l'oreille)
- **es-03** le serveur : visage repris du fonctionnaire allemand (Beamter), comme la voisine
  d'es-02 reprenait la dame de l'épisode 3.
- **es-04** Lucía, la collègue : visage neuf, depuis le texte. Le directeur : visage du cycliste
  de l'épisode 3 (risque : on ne l'a jamais vu sans casque ; repli : visage neuf).
- **04** la boulangère : visage et voix neufs (accent berlinois).
- **05** le voisin du Späti : proposé en caméo du cycliste de l'épisode 3 (même Kiez), voix reprise ;
  alternative « inconnu » décrite dans le JSON.
- Ana (es) et Anna (de) ont besoin chacune d'une image en tenue de tous les jours, dérivée de leur
  image d'aéroport (jamais depuis le texte).

## À trancher ensemble
1. **04** : retrouvailles à la boulangerie (le gag Schrippe / Pfannkuchen) plutôt qu'à l'épicerie
   prévue dans l'arc ?
2. **04, plan 16** : Anna dit « Weil Berliner Menschen sind. Zum Beispiel ich. » plutôt que « das bin
   ich » (elle est BerlinerIN : le pluriel garde le gag et un allemand juste).
3. **05, plan 19** : « Ein Berliner? Oder ein Pfannkuchen? » suppose qu'on a vu l'épisode 4 (on peut
   le couper sans rien réécrire).
4. **es-03 / es-04** : es-03 se passe un dimanche, es-04 le lundi suivant ; Mark et Ana restent au
   « usted » ; le serveur tutoie Mark.
5. **es-04, plan 13** : « en Canarias dicen « ustedes », como tú » -- à garder ou à remplacer par
   « como en México ».
6. Les caméos (Beamter → serveur ; cycliste → directeur et voisin) : oui ou visages neufs.

## Décidé le 22 oct. (soir)
- **Plus de visage d'une série à l'autre.** Jacques, sur le serveur d'es-03 qui reprenait le
  fonctionnaire de Berlin : « ça n'a pas de sens ». Le serveur a son propre visage (fait).
  **es-04 :** le directeur ne reprend PAS le cycliste allemand -- visage neuf à décrire.
  **05 :** le cycliste en voisin du Späti reste possible (même série, même Kiez).
  ⚠️ **es-02, déjà publié :** la voisine mexicaine reprend le visage de la dame du feu rouge de
  l'épisode 3 allemand -- le même défaut. DÉCIDÉ par Jacques (26 oct. : « on avait tout décidé »).

## Décidé le 24 oct. 2026 -- la suite de la série allemande
- **04 « Schrippe » : nouvelle fin.** Jacques : « il n'y a rien qui nous dit qu'ils vont se revoir ». Au plan 18 Mark se demande s'il l'attend et n'ose pas (« Soll ich auf sie warten? … Nein. Das ist komisch. ») ; plan 19 neuf : Anna sort et part à gauche, Mark s'éloigne à droite, dos tourné ; le narrateur : « Wird Mark sie wiedersehen? ». Le spectateur voit ce que Mark ne voit pas.
- **L'épisode suivant (05) : la Volkshochschule.** Mark s'inscrit à un cours d'allemand ; dans le couloir, il retrouve Anna, qui y suit un cours d'espagnol, même soir, chaque semaine. Ils découvrent qu'ils habitent le même quartier, et c'est là que la relation se développe. Jacques : pas de deuxième boulangerie (« ce ne sont pas des nouveaux mots »). **« Pfand » passe en 06** (scène déjà écrite sous 05-pfand : renuméroter le moment venu).
