# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes de l'A1 anglais. SOURCE : c'est ici qu'on corrige.

Meme forme que noms_a1.py : « mot | traduction | drapeaux ». Les formes des
verbes (3e personne, preterit, participe, -ing) et des adjectifs (comparatif,
superlatif) sont CALCULEES par construire.py ; les irreguliers sont dans
IRREGULIERS ci-dessous, avec la forme britannique quand elle differe
(learned / learnt, gotten / got).
"""

VERBES = """
be | être
have | avoir
do | faire
go | aller
come | venir
get | obtenir, recevoir, devenir
make | faire, fabriquer
take | prendre
give | donner
say | dire
tell | dire, raconter
see | voir
look | regarder
watch | regarder (un écran, un match)
hear | entendre
listen | écouter
know | savoir, connaître
think | penser, croire
believe | croire
want | vouloir
need | avoir besoin de
like | aimer (bien)
love | aimer, adorer
hate | détester
prefer | préférer
eat | manger
drink | boire
cook | cuisiner
sleep | dormir
wake up | se réveiller
get up | se lever
wash | laver
clean | nettoyer
live | habiter, vivre
work | travailler
study | étudier
learn | apprendre
teach | enseigner
read | lire
write | écrire
speak | parler (une langue)
talk | parler, discuter
ask | demander, poser (une question)
answer | répondre
understand | comprendre
explain | expliquer
repeat | répéter
spell | épeler
play | jouer
sing | chanter
dance | danser
swim | nager
run | courir
walk | marcher
drive | conduire
ride | faire du (vélo, cheval)
fly | voler, prendre l'avion
travel | voyager
visit | visiter, rendre visite à
stay | rester, séjourner
leave | partir, quitter
arrive | arriver
come back | revenir
go out | sortir
wait | attendre
meet | rencontrer, retrouver
call | appeler
help | aider
buy | acheter
sell | vendre
pay | payer
cost | coûter
spend | dépenser, passer (du temps)
open | ouvrir
close | fermer
start | commencer
begin | commencer
finish | finir
stop | arrêter, s'arrêter
put | mettre, poser
bring | apporter
carry | porter
wear | porter (un vêtement)
put on | mettre (un vêtement)
take off | enlever (un vêtement)
find | trouver
look for | chercher
lose | perdre
win | gagner
forget | oublier
remember | se souvenir de
feel | se sentir, sentir
laugh | rire
cry | pleurer
smile | sourire
sit down | s'asseoir
stand | être debout
show | montrer
send | envoyer
try | essayer
use | utiliser
change | changer
move | bouger, déménager
turn | tourner
draw | dessiner
paint | peindre
cut | couper
break | casser
fix | réparer
build | construire
grow | grandir, pousser
celebrate | fêter, célébrer
invite | inviter
thank | remercier
hope | espérer
order | commander
book | réserver
rent | louer
park | se garer
count | compter
choose | choisir
decide | décider
happen | arriver, se passer
become | devenir
keep | garder
let | laisser
mean | vouloir dire
hurt | faire mal
rain | pleuvoir
snow | neiger
shop | faire les courses
relax | se détendre
kiss | embrasser
pack | faire (sa valise), emballer
save | économiser, sauvegarder
earn | gagner (de l'argent)
smell | sentir
taste | goûter, avoir un goût
sit | être assis
lie down | s'allonger
hang | accrocher, pendre
pick up | aller chercher (quelqu'un), ramasser
prepare | préparer
clean up | ranger
smoke | fumer
"""

# base : (preterit, participe) -- et la forme britannique si elle differe,
# en troisieme position : (preterit GB, participe GB).
IRREGULIERS = {
    "be": ("was/were", "been"), "have": ("had", "had"), "do": ("did", "done"),
    "go": ("went", "gone"), "come": ("came", "come"),
    "get": ("got", "gotten", ("got", "got")), "make": ("made", "made"),
    "take": ("took", "taken"), "give": ("gave", "given"), "say": ("said", "said"),
    "tell": ("told", "told"), "see": ("saw", "seen"), "hear": ("heard", "heard"),
    "know": ("knew", "known"), "think": ("thought", "thought"), "eat": ("ate", "eaten"),
    "drink": ("drank", "drunk"), "sleep": ("slept", "slept"), "wake": ("woke", "woken"),
    "read": ("read", "read"), "write": ("wrote", "written"), "speak": ("spoke", "spoken"),
    "understand": ("understood", "understood"), "teach": ("taught", "taught"),
    "sing": ("sang", "sung"), "swim": ("swam", "swum"), "run": ("ran", "run"),
    "drive": ("drove", "driven"), "ride": ("rode", "ridden"), "fly": ("flew", "flown"),
    "leave": ("left", "left"), "meet": ("met", "met"), "buy": ("bought", "bought"),
    "sell": ("sold", "sold"), "pay": ("paid", "paid"), "cost": ("cost", "cost"),
    "spend": ("spent", "spent"), "begin": ("began", "begun"), "put": ("put", "put"),
    "bring": ("brought", "brought"), "wear": ("wore", "worn"), "find": ("found", "found"),
    "lose": ("lost", "lost"), "win": ("won", "won"), "forget": ("forgot", "forgotten"),
    "feel": ("felt", "felt"), "sit": ("sat", "sat"), "stand": ("stood", "stood"),
    "send": ("sent", "sent"), "draw": ("drew", "drawn"), "cut": ("cut", "cut"),
    "break": ("broke", "broken"), "build": ("built", "built"), "grow": ("grew", "grown"),
    "choose": ("chose", "chosen"), "become": ("became", "become"), "keep": ("kept", "kept"),
    "let": ("let", "let"), "mean": ("meant", "meant"), "hurt": ("hurt", "hurt"),
    "learn": ("learned", "learned", ("learned / learnt", "learned / learnt")),
    "smell": ("smelled", "smelled", ("smelled / smelt", "smelled / smelt")),
    "hang": ("hung", "hung"), "lie": ("lay", "lain"),
    "spell": ("spelled", "spelled", ("spelled / spelt", "spelled / spelt")),
    "dream": ("dreamed", "dreamed", ("dreamed / dreamt", "dreamed / dreamt")),
}

# Le -ing et le passe qui doublent la consonne finale (stop -> stopped).
# Une liste, pas une regle : la regle depend de l'accent (begin -> beginning,
# visit -> visiting), et l'americain ne double pas travel (traveled), le
# britannique si (travelled).
DOUBLENT = {"stop", "shop", "plan", "swim", "run", "sit", "cut", "put", "get",
            "begin", "forget", "win", "let", "prefer", "hug", "drop", "chat"}
DOUBLENT_GB = {"travel", "cancel"}

ADJECTIFS = """
big | grand, gros
small | petit
little | petit (affectif)
tall | grand (de taille)
short | court, petit (de taille)
long | long
old | vieux, âgé
young | jeune
new | nouveau, neuf
good | bon, bien
bad | mauvais
nice | sympa, agréable
beautiful | beau, magnifique
pretty | joli
ugly | laid
happy | heureux, content
sad | triste
tired | fatigué
hungry | qui a faim
thirsty | qui a soif
hot | chaud, très chaud
cold | froid
warm | chaud (agréable)
cool | frais
cheap | bon marché
expensive | cher
easy | facile
difficult | difficile
hard | dur, difficile
fast | rapide
slow | lent
early | en avance, tôt
late | en retard, tard
rich | riche
poor | pauvre
full | plein
empty | vide
clean | propre
dirty | sale
closed | fermé
free | libre, gratuit
busy | occupé
ready | prêt
sick | malade | gb=ill
strong | fort
heavy | lourd
light | léger, clair
dark | sombre, foncé
quiet | calme, silencieux
loud | bruyant, fort
funny | drôle
interesting | intéressant
boring | ennuyeux
important | important
right | juste, correct
wrong | faux, incorrect
true | vrai
different | différent
favorite | préféré | gb=favourite
friendly | aimable, sympathique
kind | gentil
angry | en colère
afraid | effrayé (qui a peur)
sure | sûr
great | génial, super
delicious | délicieux
sweet | sucré, mignon
fresh | frais
married | marié
single | célibataire
high | haut
low | bas
wet | mouillé
dry | sec
sunny | ensoleillé
rainy | pluvieux
cloudy | nuageux
windy | venteux
dangerous | dangereux
famous | célèbre
red | rouge
blue | bleu
green | vert
yellow | jaune
black | noir
white | blanc
gray | gris | gb=grey
brown | marron, brun
orange | orange
pink | rose
purple | violet
wide | large
narrow | étroit
healthy | en bonne santé, sain
colorful | coloré | gb=colourful
thick | épais
thin | mince, fin
round | rond
flat | plat
deep | profond
broken | cassé
sour | acide
bitter | amer
salty | salé
spicy | épicé
awake | éveillé
serious | sérieux
in love | amoureux
athletic | sportif
soft | doux, mou
smooth | lisse
straight | droit
huge | énorme
tiny | minuscule
tight | serré
American | américain
Canadian | canadien
French | français
English | anglais
German | allemand
Spanish | espagnol
"""
# Pas de comparatif : on n'est pas « plus marie » ni « plus rouge » (pour les
# couleurs, on peut, mais ce n'est pas ce que l'A1 doit en retenir).
SANS_COMPARATIF = {"married", "single", "closed", "free", "ready", "wrong", "right", "true",
                   "favorite", "afraid", "broken", "awake", "in love", "American", "Canadian", "French", "English", "German", "Spanish", "round", "flat", "red", "blue", "green", "yellow", "black", "white",
                   "gray", "brown", "orange", "pink", "purple", "delicious", "important"}
COMPARATIFS_IRREGULIERS = {"good": ("better", "the best"), "bad": ("worse", "the worst"),
                           "little": ("smaller", "the smallest")}
# Une syllabe, ou deux en -y : -er / -est. Les autres : more / most. Cette
# liste ne tranche que les cas que le compte des syllabes rate.
COURTS = {"quiet": ("quieter", "the quietest"), "simple": ("simpler", "the simplest"),
          "dry": ("drier", "the driest")}

# kategorie = l'etiquette affichee telle quelle (en francais).
ADVERBES = """
very | très | Quantité
too | trop, aussi | Quantité
a lot | beaucoup | Quantité
a little | un peu | Quantité
enough | assez | Quantité
really | vraiment | Manière
well | bien | Manière
quickly | vite, rapidement | Manière
slowly | lentement | Manière
together | ensemble | Manière
also | aussi | Manière
only | seulement | Manière
almost | presque | Manière
maybe | peut-être | Manière
always | toujours | Fréquence
usually | d'habitude | Fréquence
often | souvent | Fréquence
sometimes | parfois | Fréquence
never | jamais | Fréquence
again | encore, de nouveau | Fréquence
now | maintenant | Temps
today | aujourd'hui | Temps
tomorrow | demain | Temps
yesterday | hier | Temps
tonight | ce soir | Temps
soon | bientôt | Temps
later | plus tard | Temps
already | déjà | Temps
still | encore, toujours | Temps
yet | encore, déjà (questions, négations) | Temps
then | puis, ensuite, alors | Temps
first | d'abord | Temps
here | ici | Lieu
there | là, là-bas | Lieu
home | à la maison, chez soi | Lieu
outside | dehors | Lieu
inside | à l'intérieur | Lieu
upstairs | en haut (à l'étage) | Lieu
downstairs | en bas | Lieu
everywhere | partout | Lieu
far | loin | Lieu
after that | ensuite, après ça | Temps
over there | là-bas | Lieu
on the left | à gauche | Lieu
on the right | à droite | Lieu
straight ahead | tout droit | Lieu
rarely | rarement | Fréquence
hardly ever | presque jamais | Fréquence
loudly | fort, bruyamment | Manière
quietly | doucement, sans bruit | Manière
right away | tout de suite | Temps
luckily | heureusement | Manière
unfortunately | malheureusement | Manière
"""
