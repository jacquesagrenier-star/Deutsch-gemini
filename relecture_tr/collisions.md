# Collisions turques — le controle mecanique

Produit par `python tests/relecture_tr.py --collisions`. **Aucune correction appliquee.**

Chaque ligne est un mot turc qui repond a PLUSIEURS mots allemands distincts de la meme categorie. La carte devient indecidable : quoi que l'apprenant reponde, il ne peut pas avoir raison.

Toutes ne sont pas des erreurs — deux quasi-synonymes allemands peuvent legitimement partager un mot turc si la langue n'en a pas deux. Mais chacune doit etre REGARDEE, et aucune relecture par lots ne peut les voir : le relecteur ne recoit qu'une centaine de cartes a la fois.


---

# Paires de genre — vues, et acceptees

Ces 37 groupes ne sont PAS des collisions a corriger. Le turc n'a pas de genre grammatical et ne feminise pas le nom de metier : « uzman » est la bonne reponse pour `der Experte` comme pour `die Expertin`. Inventer une forme feminine pour departager les deux cartes enseignerait une regle qui n'existe pas dans la langue.

Ils sont reconnus mecaniquement (voir `paire_de_genre`) et sortis du decompte, pour qu'une relance du controle ne les remette pas dans la pile a chaque fois.

- *noms* — **ab vatandaşı** ← der EU-Bürger, die EU-Bürgerin
- *noms* — **aday** ← der Kandidat, die Kandidatin
- *noms* — **aktör** ← der Schauspieler, die Schauspielerin
- *noms* — **aşçı** ← der Koch, die Köchin
- *noms* — **belediye başkanı** ← der Bürgermeister, die Bürgermeisterin
- *noms* — **beslenme danışmanı** ← der Ernährungsberater, die Ernährungsberaterin
- *noms* — **besteci** ← der Komponist, die Komponistin
- *noms* — **bilim insanı** ← der Wissenschaftler, die Wissenschaftlerin
- *noms* — **dava vekili** ← der Rechtsanwalt, die Rechtsanwältin
- *noms* — **dinleyici** ← der Zuhörer, die Zuhörerin
- *noms* — **düzenleyici** ← der Veranstalter, die Veranstalterin
- *noms* — **fizyoterapist** ← der Physiotherapeut, die Physiotherapeutin
- *noms* — **galip** ← der Sieger, die Siegerin
- *noms* — **garson** ← der Kellner, die Kellnerin
- *noms* — **göçmen** ← der Migrant, die Migrantin
- *noms* — **hasta** ← der Patient, die Patientin
- *noms* — **hayat arkadaşı** ← der Lebensgefährte, die Lebensgefährtin
- *noms* — **işveren** ← der Arbeitgeber, die Arbeitgeberin
- *noms* — **kaleci** ← der Tormann, die Torfrau
- *noms* — **katılımcı** ← der Teilnehmer, die Teilnehmerin
- *noms* — **koşucu** ← der Läufer, die Läuferin
- *noms* — **kuzen** ← der Cousin, die Cousine
- *noms* — **muhabir** ← der Reporter, die Reporterin
- *noms* — **polis memuru** ← die Polizistin, der Polizist
- *noms* — **sanatçı** ← die Künstlerin, der Künstler
- *noms* — **spor eğitmeni** ← der Fitnesstrainer, die Fitnesstrainerin
- *noms* — **stajyer** ← der Praktikant, die Praktikantin
- *noms* — **torun** ← der Enkel, die Enkelin
- *noms* — **tüketici** ← der Verbraucher, die Verbraucherin
- *noms* — **tıbbi sekreter** ← der Arzthelfer, die Arzthelferin
- *noms* — **usta** ← der Fachmann, die Fachfrau
- *noms* — **uzman** ← der Experte, die Expertin
- *noms* — **vatandaş** ← der Bürger, die Bürgerin
- *noms* — **yabancı** ← der Ausländer, die Ausländerin
- *noms* — **yaşlı bakıcısı** ← der Altenpfleger, die Altenpflegerin
- *noms* — **çevirmen** ← der Übersetzer, die Übersetzerin
- *noms* — **şehir rehberi** ← der Stadtführer, die Stadtführerin

