# -*- coding: utf-8 -*-
"""Prononcer l'anglais : les regles, pour un francophone, au format de
espanol/datos/prononciation.json. SOURCE : on corrige ici, puis
python anglais/outils/construire.py.

Chaque regle : id, graphie, api, court, explication, exemples (mot | sens).
`gb` : ce qui change dans le cours britannique (court et explication), sinon
la regle est la meme.
"""

GROUPES = [
("voyelles", [
 {"id": "i-court-long", "graphie": "i · ee · ea", "api": "[ɪ] · [iː]",
  "court": "ship ≠ sheep : un i court, un i long",
  "explication": "Le français n'a qu'un i ; l'anglais en a deux. Le i court [ɪ] est relâché, presque un « é » fermé : ship, sit, live. Le i long [iː] est tendu et tenu : sheep, seat, leave. Les confondre change le mot : live (vivre) ≠ leave (partir).",
  "exemples": "ship | le bateau\nsheep | le mouton\nsit | être assis\nseat | le siège\nlive | vivre\nleave | partir"},
 {"id": "a-trois", "graphie": "a", "api": "[æ] · [eɪ] · [ɑː]",
  "court": "cat, cake, car : trois a",
  "explication": "La lettre a se lit de trois façons. [æ], entre « a » et « è », bouche bien ouverte : cat, apple, black. [eɪ], « éï », quand un e muet suit : cake, name, late. [ɑː], un a profond : car, father.",
  "exemples": "cat | le chat\napple | la pomme\ncake | le gâteau\nname | le nom\ncar | la voiture\nfather | le père"},
 {"id": "u-court", "graphie": "u · o", "api": "[ʌ]",
  "court": "cup, sun, mother : un « eu » bref",
  "explication": "Le son [ʌ] est un « eu » bref et ouvert, la bouche à peine ouverte. Il s'écrit souvent u (bus, sun, cup), parfois o (mother, love, Monday). Jamais « u » à la française.",
  "exemples": "bus | le bus\nsun | le soleil\ncup | la tasse\nmother | la mère\nlove | l'amour\nMonday | lundi"},
 {"id": "schwa", "graphie": "a · e · o (sans accent)", "api": "[ə]",
  "court": "les voyelles sans accent s'effacent",
  "explication": "Dans une syllabe sans accent, la voyelle devient un « e » neutre très bref, le schwa [ə] : banana « be-NA-ne », teacher « TI-tcheur », doctor, the. C'est le son le plus fréquent de l'anglais : le prononcer, c'est déjà avoir l'accent.",
  "exemples": "banana | la banane\nteacher | le professeur\ndoctor | le médecin\nabout | à propos de\nsofa | le canapé"},
 {"id": "diphtongues", "graphie": "o · i · ay · ow", "api": "[oʊ] · [aɪ] · [eɪ] · [aʊ]",
  "court": "go, my, day, now : des voyelles qui glissent",
  "explication": "Beaucoup de voyelles anglaises glissent d'un son à l'autre. go « gôou », home ; my « maï », time ; day « déï », say ; now « naou », house. Un « o » tout rond à la française sonne étranger : il faut le faire glisser.",
  "exemples": "go | aller\nhome | la maison\nmy | mon, ma\ntime | le temps\nday | le jour\nnow | maintenant\nhouse | la maison"},
]),
("consonnes", [
 {"id": "th-sourd", "graphie": "th", "api": "[θ]",
  "court": "three, think : la langue entre les dents",
  "explication": "Le th de three se fait en posant le bout de la langue entre les dents et en soufflant, sans vibration. Ni « s » ni « f » : three (trois) ≠ free (libre) ≠ « sri ». Il revient dans thank you, think, bathroom.",
  "exemples": "three | trois\nthink | penser\nthank you | merci\nbathroom | la salle de bain\nThursday | jeudi"},
 {"id": "th-sonore", "graphie": "th", "api": "[ð]",
  "court": "the, this : le même, avec la voix",
  "explication": "Même position de la langue, mais la gorge vibre : the, this, that, mother, father. Ni « d » ni « z ». C'est le th des petits mots les plus fréquents : the, they, there.",
  "exemples": "the | le, la, les\nthis | ce, ceci\nmother | la mère\nfather | le père\nbrother | le frère"},
 {"id": "h", "graphie": "h", "api": "[h]",
  "court": "house, hello : le h se souffle",
  "explication": "Le h anglais s'entend : un souffle léger, comme sur une vitre qu'on embue. house, hello, happy, hotel. L'oublier change le mot : hear (entendre) ≠ ear (l'oreille). Quelques mots ont un h muet : hour, honest.",
  "exemples": "house | la maison\nhello | bonjour\nhappy | heureux\nhotel | l'hôtel\nhear | entendre\near | l'oreille"},
 {"id": "r", "graphie": "r", "api": "[ɹ]",
  "court": "le r ne racle pas : la langue recule",
  "explication": "Le r anglais ne se fait pas dans la gorge. La langue se recourbe vers l'arrière sans toucher le palais, les lèvres s'arrondissent un peu : red, very, sorry. En américain, il s'entend aussi en fin de mot : car, water, teacher.",
  "exemples": "red | rouge\nvery | très\nsorry | désolé\ncar | la voiture\nwater | l'eau",
  "gb": {"court": "le r ne racle pas, et se tait en fin de mot",
         "explication": "Le r anglais ne se fait pas dans la gorge : la langue se recourbe vers l'arrière sans toucher le palais (red, very, sorry). En anglais britannique, il ne se prononce pas en fin de mot ni devant une consonne : car « kaa », water « OUO-te », teacher « TI-tche »."}},
 {"id": "w", "graphie": "w · wh", "api": "[w]",
  "court": "water, what : un « ou » rapide",
  "explication": "Le w est un « ou » très bref qui glisse vers la voyelle : water « OUO-ter », window, we, what. Jamais un « v ».",
  "exemples": "water | l'eau\nwindow | la fenêtre\nwe | nous\nwhat | que, quoi\nWednesday | mercredi"},
 {"id": "t-flap", "graphie": "t · tt", "api": "[ɾ]",
  "court": "water, city : le t devient presque un d",
  "explication": "En américain, un t entre deux voyelles se dit très vite, comme un d léger : water « OUA-deur », city « SI-di », better « BÈ-deur ». C'est l'un des sons qui font l'accent américain.",
  "exemples": "water | l'eau\ncity | la ville\nbetter | meilleur\npretty | joli\nthirty | trente",
  "gb": {"court": "water, city : le t reste un t net",
         "explication": "En anglais britannique, le t entre deux voyelles reste un vrai t, net : water « OUO-te », city « SI-ti », better « BÈ-te ». (L'américain, lui, en fait presque un d.)"}},
 {"id": "muettes", "graphie": "k · w · d · s · t", "api": "—",
  "court": "knife, write, Wednesday : des lettres muettes",
  "explication": "Certaines lettres ne se prononcent pas : le k devant n (knife, know), le w devant r (write, wrong), le premier d de Wednesday « OUÈNZ-déï », le s d'island, le t de listen. Il faut les apprendre avec le mot.",
  "exemples": "knife | le couteau\nknow | savoir\nwrite | écrire\nwrong | faux\nWednesday | mercredi\nlisten | écouter"},
]),
("fins", [
 {"id": "s-final", "graphie": "-s · -es", "api": "[s] · [z] · [ɪz]",
  "court": "cats, dogs, buses : trois -s",
  "explication": "Le -s du pluriel et de la 3ᵉ personne se dit [s] après un son sourd (cats, books, works), [z] après un son sonore (dogs, days, plays), et « iz » après s, sh, ch, x (buses, watches, boxes). Il ne s'efface jamais.",
  "exemples": "cats | les chats\nbooks | les livres\ndogs | les chiens\ndays | les jours\nbuses | les bus\nboxes | les boîtes"},
 {"id": "ed-final", "graphie": "-ed", "api": "[t] · [d] · [ɪd]",
  "court": "worked, played, wanted : trois -ed",
  "explication": "Le -ed du passé se dit [t] après un son sourd (worked « weurkt », stopped), [d] après un son sonore (played, lived), et « id » seulement après t ou d (wanted, needed). Le plus souvent, on n'ajoute pas de syllabe.",
  "exemples": "worked | a travaillé\nstopped | s'est arrêté\nplayed | a joué\nlived | a vécu\nwanted | a voulu\nneeded | a eu besoin"},
]),
("accent", [
 {"id": "accent", "graphie": "ˈ", "api": "[ˈ]",
  "court": "une syllabe forte par mot",
  "explication": "Chaque mot a une syllabe plus forte, plus longue et plus haute ; les autres s'effacent. Elle n'est pas toujours à la fin, comme en français : TEAcher, baNAna, comPUter, hoTEL, PHOto. Mal placée, elle rend un mot méconnaissable : il faut l'apprendre avec le mot.",
  "exemples": "teacher | le professeur\nbanana | la banane\ncomputer | l'ordinateur\nhotel | l'hôtel\nphoto | la photo\nbreakfast | le petit-déjeuner"},
]),
]

TITRES = {
    "pron_kicker": "Prononcer l'anglais",
    "pron_intro": "L'anglais ne se lit pas comme il s'écrit : une même lettre a plusieurs sons. Ces règles couvrent les sons qui changent le plus pour un francophone. Touche un mot pour l'entendre.",
    "pron_voyelles": "Les voyelles",
    "pron_consonnes": "Les consonnes",
    "pron_fins": "Les fins de mots",
    "pron_accent": "L'accent tonique",
}
