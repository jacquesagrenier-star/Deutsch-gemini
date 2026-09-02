# Collisions turques — le controle mecanique

Produit par `python tests/relecture_tr.py --collisions`. **Aucune correction appliquee.**

Chaque ligne est un mot turc qui repond a PLUSIEURS mots allemands distincts de la meme categorie. La carte devient indecidable : quoi que l'apprenant reponde, il ne peut pas avoir raison.

Toutes ne sont pas des erreurs — deux quasi-synonymes allemands peuvent legitimement partager un mot turc si la langue n'en a pas deux. Mais chacune doit etre REGARDEE, et aucune relecture par lots ne peut les voir : le relecteur ne recoit qu'une centaine de cartes a la fois.


---

# Collisions acceptees, avec leur raison

Le turc n'a reellement qu'un mot la ou l'allemand en a deux : forcer une difference y produirait un contresens ou une tournure que personne ne dit. Chaque ligne porte sa justification, et vient de `collisions-acceptees.txt`.

- *adjectifs* — **ciddi** ← ernst, ernsthaft
  - ernst et ernsthaft sont deux quasi-synonymes allemands ; le turc dit « ciddi » pour les deux. La relecture du 2 septembre a rejete « vahim » comme contresens (vahim = grave, desastreux), et il n'existe pas de troisieme mot naturel.
- *adjectifs* — **resmî** ← offiziell, amtlich
  - offiziell et amtlich se disent tous deux « resmî ». La relecture du 2 septembre a rejete « devlet onaylı » (= certifie par l'Etat) comme contresens sur « ein amtliches Dokument », qui est simplement « resmî bir belge ».
- *noms* — **alan** ← der Bereich, die Fläche
  - Bereich (domaine) et Flaeche (superficie) se disent « alan ». « yuzey » designe la surface exterieure d'un objet, pas la superficie d'un terrain.
- *noms* — **anlam** ← die Bedeutung, der Sinn
  - Bedeutung et Sinn se disent « anlam ». « mana » est vieilli.
- *noms* — **araç** ← das Fahrzeug, das Mittel
  - Fahrzeug et Mittel se disent « araç ». « vasıta » designe un vehicule, ce qui inverse la distinction au lieu de la creer.
- *noms* — **ateş** ← das Fieber, das Feuer
  - HOMONYME turc : « ateş » veut dire fievre ET feu. « alev » est la flamme, pas le feu.
- *noms* — **avukat** ← der Anwalt, der Rechtsanwalt, die Rechtsanwältin
  - Anwalt et Rechtsanwalt sont le meme metier ; « dava vekili » est une appellation juridique obsolete.
- *noms* — **ağ** ← das Netz, das Netzwerk
  - Netz et Netzwerk se disent « ağ ». « şebeke » s'applique aux reseaux electriques ou telephoniques, pas informatiques.
- *noms* — **danışman** ← der Berater, der Betreuer
  - Berater et Betreuer se disent « danışman ». « refakatçi » est un accompagnateur de malade.
- *noms* — **değişiklik** ← die Änderung, die Veränderung
  - Aenderung et Veraenderung se disent « değişiklik ». « başkalaşım » est une metamorphose.
- *noms* — **duvar** ← die Wand, die Mauer
  - Wand et Mauer se disent « duvar ». « taş duvar » (mur en pierre) est inutilement restrictif.
- *noms* — **geri bildirim** ← die Rückmeldung, das Feedback
  - Rueckmeldung et Feedback se disent « geri bildirim ». « dönüş » est trop vague.
- *noms* — **geri dönüşüm** ← das Recycling, die Wiederverwertung
  - Recycling et Wiederverwertung se disent « geri dönüşüm ».
- *noms* — **gerçeklik** ← die Realität, die Wirklichkeit
  - Realitaet et Wirklichkeit se disent « gerçeklik ». « hakikat » est litteraire.
- *noms* — **hırsız** ← der Dieb, der Einbrecher
  - Dieb et Einbrecher se disent « hırsız ». « soyguncu » est un braqueur a main armee.
- *noms* — **kanepe** ← das Sofa, die Couch
  - Sofa et Couch se disent « kanepe ». « divan » est vieilli.
- *noms* — **kat** ← die Etage, das Vielfache
  - HOMONYME turc : « kat » veut dire etage ET multiple.
- *noms* — **kaynak** ← die Quelle, die Ressource
  - Quelle et Ressource se disent « kaynak ». « rezerv » est une reserve.
- *noms* — **korku** ← die Angst, die Furcht
  - Angst et Furcht se disent « korku ». « dehşet » est la terreur.
- *noms* — **manzara** ← die Landschaft, die Aussicht
  - Landschaft et Aussicht se disent « manzara ». « peyzaj » designe l'amenagement paysager.
- *noms* — **pazar** ← der Sonntag, der Markt
  - HOMONYME turc : « pazar » veut dire dimanche ET marche.
- *noms* — **uygulama** ← die App, die Anwendung
  - App et Anwendung se disent « uygulama ». « kullanım » veut dire utilisation.
- *noms* — **uzman** ← der Experte, die Expertin, der Fachmann, die Fachfrau
  - Experte, Expertin, Fachmann et Fachfrau : deux paires de genre pour deux quasi-synonymes. « usta » (artisan) a ete rejete comme incoherent avec la phrase.
- *noms* — **yağ** ← das Öl, das Fett
  - HOMONYME turc : « yağ » couvre l'huile et la graisse. « katı yağ » est la margarine.
- *noms* — **yönetmelik** ← die Vorschrift, die Verordnung
  - Vorschrift et Verordnung se disent « yönetmelik ». « talimat » est une consigne.
- *noms* — **çöp kovası** ← der Mülleimer, die Mülltonne
  - Muelleimer et Muelltonne se disent « çöp kovası ». « çöp konteyneri » est un grand conteneur.
- *noms* — **ölçü** ← der Takt, das Maß
  - HOMONYME turc : « ölçü » est la mesure au sens general ET la mesure musicale. « tempo » est la vitesse du morceau.
- *verbes* — **açmak** ← öffnen, aufmachen
  - öffnen et aufmachen sont le meme verbe a deux registres ; le turc dit « açmak » pour les deux. « açıvermek », essaye pour les distinguer, ajoute une nuance de rapidite que l'allemand n'a pas.
- *verbes* — **başlamak** ← beginnen, anfangen
  - beginnen et anfangen sont interchangeables en allemand ; le turc dit « başlamak ». « girişmek », essaye pour beginnen, est un contresens : il veut dire s'attaquer a quelque chose avec fougue.
- *verbes* — **kapatmak** ← schließen, zumachen
  - schliessen et zumachen, meme cas. « kapayıvermek » ajoutait la meme nuance parasite.
- *verbes* — **yapmak** ← machen, tun
  - machen et tun se disent tous deux « yapmak ». « etmek », essaye pour tun, n'existe pratiquement qu'en verbe compose et ne tient pas seul.


---

# Paires de genre — vues, et acceptees

Ces 33 groupes ne sont PAS des collisions a corriger. Le turc n'a pas de genre grammatical et ne feminise pas le nom de metier : « uzman » est la bonne reponse pour `der Experte` comme pour `die Expertin`. Inventer une forme feminine pour departager les deux cartes enseignerait une regle qui n'existe pas dans la langue.

Ils sont reconnus mecaniquement (voir `paire_de_genre`) et sortis du decompte, pour qu'une relance du controle ne les remette pas dans la pile a chaque fois.

- *noms* — **ab vatandaşı** ← der EU-Bürger, die EU-Bürgerin
- *noms* — **aday** ← der Kandidat, die Kandidatin
- *noms* — **aşçı** ← der Koch, die Köchin
- *noms* — **belediye başkanı** ← der Bürgermeister, die Bürgermeisterin
- *noms* — **beslenme danışmanı** ← der Ernährungsberater, die Ernährungsberaterin
- *noms* — **besteci** ← der Komponist, die Komponistin
- *noms* — **bilim insanı** ← der Wissenschaftler, die Wissenschaftlerin
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
- *noms* — **vatandaş** ← der Bürger, die Bürgerin
- *noms* — **yabancı** ← der Ausländer, die Ausländerin
- *noms* — **yaşlı bakıcısı** ← der Altenpfleger, die Altenpflegerin
- *noms* — **çevirmen** ← der Übersetzer, die Übersetzerin
- *noms* — **şehir rehberi** ← der Stadtführer, die Stadtführerin

