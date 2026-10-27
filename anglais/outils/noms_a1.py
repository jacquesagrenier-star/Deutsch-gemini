# -*- coding: utf-8 -*-
"""Les noms de l'A1 anglais, par theme. SOURCE : c'est ici qu'on corrige.

Une ligne = « mot | traduction francaise | drapeaux ». La base est l'anglais
AMERICAIN ; `gb=` donne le mot britannique quand il differe (la variante, voir
anglais/datos-gb). Drapeaux :
  pl=X    pluriel irregulier ou impose
  u       indenombrable : pas de pluriel (water, money, homework)
  plt     n'existe qu'au pluriel (pants, jeans, clothes) : pas de pluriel non plus
  gb=X    le mot britannique
  plgb=X  le pluriel du mot britannique, quand le calcul se tromperait
  ex=...  la phrase d'exemple imposee, « anglais # francais » (sinon : la banque)

Choisis le 27 oct. 2026 a partir de l'union des A1 allemand et espagnol (683
tetes anglaises), sans les nombres (ils vont dans les reperes) et sans les mots
trop lies a l'Espagne ou a l'Allemagne (paella, pretzel, Pfand).
"""

# (id, nom du theme en anglais, theme source dont on reprend l'icone)
THEMES = [
    ("family_a1",    "Family",                    "la_familia"),
    ("people_a1",    "People",                    "presentarse"),
    ("home_a1",      "The home",                  "la_casa"),
    ("food_a1",      "Food and drink",            "la_comida"),
    ("eatingout_a1", "Eating out",                "el_restaurante"),
    ("body_a1",      "Body and health",           "el_cuerpo"),
    ("clothes_a1",   "Clothes",                   "la_ropa"),
    ("city_a1",      "The city",                  "la_ciudad"),
    ("time_a1",      "Time and dates",            "el_tiempo"),
    ("animals_a1",   "Animals",                   "los_animales"),
    ("weather_a1",   "Weather and nature",        "el_clima"),
    ("shopping_a1",  "Shopping and money",        "las_compras"),
    ("travel_a1",    "Getting around",            "el_transporte"),
    ("school_a1",    "School",                    "la_escuela"),
    ("work_a1",      "Work",                      "el_trabajo"),
    ("freetime_a1",  "Free time",                 "el_ocio"),
    ("tech_a1",      "Media and technology",      "medien_technologie_a1"),
    ("feelings_a1",  "Feelings",                  "gefuehle_charakter_a1"),
    ("everyday_a1",  "Everyday words",            "la_vida_diaria"),
]

NOMS = {
"family_a1": """
family | la famille | pl=families
mother | la mère
father | le père
mom | la maman | gb=mum
dad | le papa
parents | les parents | plt
son | le fils
daughter | la fille
brother | le frère
sister | la sœur
siblings | les frères et sœurs | plt
child | l'enfant | pl=children
baby | le bébé | pl=babies
grandmother | la grand-mère
grandfather | le grand-père
grandparents | les grands-parents | plt
grandson | le petit-fils
granddaughter | la petite-fille
uncle | l'oncle
aunt | la tante
cousin | le cousin, la cousine
nephew | le neveu
niece | la nièce
husband | le mari
wife | la femme, l'épouse | pl=wives
boyfriend | le petit ami
girlfriend | la petite amie
partner | le, la partenaire
wedding | le mariage
birthday | l'anniversaire
""",
"people_a1": """
person | la personne | pl=people
man | l'homme | pl=men
woman | la femme | pl=women
boy | le garçon
girl | la fille
friend | l'ami, l'amie
neighbor | le voisin, la voisine | gb=neighbour
guest | l'invité, l'invitée
name | le nom
first name | le prénom
last name | le nom de famille | gb=surname
age | l'âge
address | l'adresse | pl=addresses
country | le pays | pl=countries
nationality | la nationalité | pl=nationalities
language | la langue
lady | la dame | pl=ladies
""",
"home_a1": """
house | la maison
home | le domicile, la maison
apartment | l'appartement | gb=flat
room | la pièce
kitchen | la cuisine
bedroom | la chambre
bathroom | la salle de bain
living room | le salon
dining room | la salle à manger
hallway | le couloir
stairs | l'escalier | plt
floor | le sol, l'étage
wall | le mur
door | la porte
window | la fenêtre
roof | le toit
ceiling | le plafond
balcony | le balcon | pl=balconies
garden | le jardin
garage | le garage
key | la clé
bed | le lit
table | la table
chair | la chaise
sofa | le canapé
closet | le placard, la penderie | gb=wardrobe
shelf | l'étagère | pl=shelves
lamp | la lampe
mirror | le miroir
picture | le tableau, l'image
rug | le tapis
curtain | le rideau
pillow | l'oreiller
blanket | la couverture
sheet | le drap
towel | la serviette (de bain)
shower | la douche
bathtub | la baignoire | gb=bath
toilet | les toilettes, la cuvette
sink | l'évier, le lavabo
faucet | le robinet | gb=tap
fridge | le frigo
stove | la cuisinière | gb=cooker
oven | le four
microwave | le micro-ondes
dishwasher | le lave-vaisselle
washing machine | la machine à laver
furniture | les meubles | u
rent | le loyer
""",
"food_a1": """
food | la nourriture | u
meal | le repas
breakfast | le petit-déjeuner
lunch | le déjeuner
dinner | le dîner
bread | le pain | u
butter | le beurre | u
cheese | le fromage | u
egg | l'œuf
meat | la viande | u
chicken | le poulet
fish | le poisson | pl=fish
ham | le jambon | u
rice | le riz | u
pasta | les pâtes | u
soup | la soupe
salad | la salade
sandwich | le sandwich | pl=sandwiches
pizza | la pizza
cake | le gâteau
cookie | le biscuit | gb=biscuit
candy | les bonbons | u | gb=sweets
ice cream | la glace | u
sugar | le sucre | u
salt | le sel | u
pepper | le poivre | u
oil | l'huile | u
fruit | le fruit
apple | la pomme
banana | la banane
orange | l'orange
lemon | le citron
strawberry | la fraise | pl=strawberries
grape | le raisin
pear | la poire
vegetable | le légume
potato | la pomme de terre | pl=potatoes
tomato | la tomate | pl=tomatoes
carrot | la carotte
onion | l'oignon
garlic | l'ail | u
mushroom | le champignon
cucumber | le concombre
drink | la boisson
water | l'eau | u
coffee | le café | u
tea | le thé | u
milk | le lait | u
juice | le jus | u
beer | la bière | u
wine | le vin | u
glass | le verre | pl=glasses
cup | la tasse
bottle | la bouteille
plate | l'assiette
bowl | le bol
knife | le couteau | pl=knives
fork | la fourchette
spoon | la cuillère
napkin | la serviette (de table)
pan | la poêle
pot | la casserole
""",
"eatingout_a1": """
restaurant | le restaurant
café | le café (l'endroit)
menu | la carte, le menu
waiter | le serveur
waitress | la serveuse | pl=waitresses
check | l'addition | gb=bill
tip | le pourboire
dish | le plat | pl=dishes
dessert | le dessert
order | la commande
reservation | la réservation
""",
"body_a1": """
body | le corps | pl=bodies
head | la tête
face | le visage
hair | les cheveux | u
eye | l'œil
ear | l'oreille
nose | le nez
mouth | la bouche
tooth | la dent | pl=teeth
neck | le cou
shoulder | l'épaule
arm | le bras
hand | la main
finger | le doigt
back | le dos
stomach | le ventre, l'estomac
leg | la jambe
knee | le genou
foot | le pied | pl=feet
heart | le cœur
skin | la peau | u
blood | le sang | u
health | la santé | u
doctor | le médecin
nurse | l'infirmier, l'infirmière
hospital | l'hôpital
pharmacy | la pharmacie | pl=pharmacies | gb=chemist's | plgb=—
medicine | le médicament
pill | le comprimé
prescription | l'ordonnance
pain | la douleur
headache | le mal de tête
fever | la fièvre
cold | le rhume
cough | la toux
flu | la grippe | u
appointment | le rendez-vous
""",
"clothes_a1": """
clothes | les vêtements | plt
shirt | la chemise
T-shirt | le t-shirt
blouse | le chemisier
sweater | le pull | gb=jumper
pants | le pantalon | plt | gb=trousers
jeans | le jean | plt
shorts | le short | plt
skirt | la jupe
dress | la robe | pl=dresses
jacket | la veste
coat | le manteau
suit | le costume
shoe | la chaussure
boot | la botte
sneaker | la basket | gb=trainer
sock | la chaussette
hat | le chapeau
cap | la casquette
scarf | l'écharpe | pl=scarves
glove | le gant
belt | la ceinture
pocket | la poche
bag | le sac
purse | le sac à main | gb=handbag
backpack | le sac à dos
umbrella | le parapluie
glasses | les lunettes | plt
sunglasses | les lunettes de soleil | plt
watch | la montre | pl=watches
ring | la bague
size | la taille
pajamas | le pyjama | plt | gb=pyjamas
""",
"city_a1": """
city | la ville | pl=cities
town | la petite ville
village | le village
street | la rue
road | la route
square | la place
corner | le coin
bridge | le pont
building | le bâtiment, l'immeuble
church | l'église | pl=churches
museum | le musée
library | la bibliothèque | pl=libraries
park | le parc
bank | la banque
post office | le bureau de poste
police officer | le policier, la policière
city hall | la mairie | gb=town hall
hotel | l'hôtel
movie theater | le cinéma | gb=cinema
theater | le théâtre | gb=theatre
neighborhood | le quartier | gb=neighbourhood
downtown | le centre-ville | u | gb=city centre
market | le marché
traffic light | le feu (de circulation)
sidewalk | le trottoir | gb=pavement
parking lot | le parking | gb=car park
gas station | la station-service | gb=petrol station
bench | le banc | pl=benches
tower | la tour
factory | l'usine | pl=factories
map | le plan, la carte
""",
"time_a1": """
time | le temps, l'heure | u
day | le jour, la journée
week | la semaine
month | le mois
year | l'an, l'année
weekend | le week-end
morning | le matin
afternoon | l'après-midi
evening | le soir
night | la nuit
noon | midi | u
midnight | minuit | u
hour | l'heure
minute | la minute
second | la seconde
Monday | lundi
Tuesday | mardi
Wednesday | mercredi
Thursday | jeudi
Friday | vendredi
Saturday | samedi
Sunday | dimanche
January | janvier | u
February | février | u
March | mars | u
April | avril | u
May | mai | u
June | juin | u
July | juillet | u
August | août | u
September | septembre | u
October | octobre | u
November | novembre | u
December | décembre | u
spring | le printemps
summer | l'été
fall | l'automne | gb=autumn
winter | l'hiver
season | la saison
date | la date
calendar | le calendrier
holiday | le jour férié | gb=bank holiday
Christmas | Noël | u
party | la fête | pl=parties
moment | le moment
century | le siècle | pl=centuries
""",
"animals_a1": """
animal | l'animal
pet | l'animal de compagnie
dog | le chien
cat | le chat
bird | l'oiseau
horse | le cheval
cow | la vache
pig | le cochon
sheep | le mouton | pl=sheep
goat | la chèvre
duck | le canard
rabbit | le lapin
mouse | la souris | pl=mice
bear | l'ours
lion | le lion
tiger | le tigre
elephant | l'éléphant
monkey | le singe
snake | le serpent
spider | l'araignée
bee | l'abeille
fly | la mouche | pl=flies
turtle | la tortue
zoo | le zoo
""",
"weather_a1": """
weather | le temps (qu'il fait) | u
sun | le soleil
rain | la pluie | u
snow | la neige | u
wind | le vent
cloud | le nuage
fog | le brouillard | u
storm | la tempête, l'orage
ice | la glace | u
temperature | la température
degree | le degré
heat | la chaleur | u
sky | le ciel | pl=skies
nature | la nature | u
tree | l'arbre
flower | la fleur
plant | la plante
grass | l'herbe | u
leaf | la feuille | pl=leaves
forest | la forêt
mountain | la montagne
river | la rivière, le fleuve
lake | le lac
sea | la mer
beach | la plage | pl=beaches
island | l'île
field | le champ
stone | la pierre
moon | la lune
star | l'étoile
air | l'air | u
world | le monde
""",
"shopping_a1": """
store | le magasin | gb=shop
supermarket | le supermarché
shopping | les courses, le shopping | u
money | l'argent | u
cash | l'argent liquide | u
price | le prix
customer | le client, la cliente
salesperson | le vendeur, la vendeuse | pl=salespeople | gb=shop assistant
checkout | la caisse
receipt | le ticket de caisse
credit card | la carte de crédit
coin | la pièce (de monnaie)
dollar | le dollar
euro | l'euro
sale | les soldes, la promotion
bakery | la boulangerie | pl=bakeries
gift | le cadeau
cart | le chariot | gb=trolley
fitting room | la cabine d'essayage
""",
"travel_a1": """
car | la voiture
bus | le bus | pl=buses
train | le train
subway | le métro | gb=underground | plgb=—
taxi | le taxi
bike | le vélo
motorcycle | la moto | gb=motorbike
truck | le camion | gb=lorry
plane | l'avion
boat | le bateau
airport | l'aéroport
train station | la gare | gb=railway station
bus stop | l'arrêt de bus
platform | le quai
ticket | le billet, le ticket
passport | le passeport
suitcase | la valise
luggage | les bagages | u
trip | le voyage
vacation | les vacances | gb=holiday
flight | le vol
passenger | le passager, la passagère
driver | le conducteur, la conductrice
traffic | la circulation | u
traffic jam | l'embouteillage
driver's license | le permis de conduire | gb=driving licence
gas | l'essence | u | gb=petrol
tourist | le, la touriste
way | le chemin
delay | le retard
""",
"school_a1": """
school | l'école
class | la classe, le cours | pl=classes
lesson | la leçon
teacher | le professeur, l'enseignant
student | l'élève, l'étudiant
classroom | la salle de classe
book | le livre
notebook | le cahier
pen | le stylo
pencil | le crayon
eraser | la gomme | gb=rubber
ruler | la règle
dictionary | le dictionnaire | pl=dictionaries
homework | les devoirs | u
exam | l'examen
test | le contrôle, le test
question | la question
answer | la réponse
word | le mot
sentence | la phrase
page | la page
letter | la lettre
grade | la note | gb=mark
subject | la matière
math | les maths | u | gb=maths
university | l'université | pl=universities
course | le cours
board | le tableau
paper | le papier | u
mistake | la faute, l'erreur
example | l'exemple
""",
"work_a1": """
work | le travail | u
job | l'emploi, le poste
office | le bureau
desk | le bureau (le meuble)
company | l'entreprise | pl=companies
boss | le, la chef | pl=bosses
colleague | le, la collègue
meeting | la réunion
salary | le salaire | pl=salaries
contract | le contrat
interview | l'entretien
computer | l'ordinateur
email | l'e-mail, le courriel
break | la pause
project | le projet
cook | le cuisinier, la cuisinière
baker | le boulanger, la boulangère
hairdresser | le coiffeur, la coiffeuse
engineer | l'ingénieur, l'ingénieure
lawyer | l'avocat, l'avocate
farmer | l'agriculteur, l'agricultrice
""",
"freetime_a1": """
hobby | le passe-temps | pl=hobbies
free time | le temps libre | u
sport | le sport
soccer | le football | u | gb=football
basketball | le basket | u
tennis | le tennis | u
game | le jeu, le match
team | l'équipe
player | le joueur, la joueuse
ball | la balle, le ballon
swimming pool | la piscine
gym | la salle de sport
music | la musique | u
song | la chanson
guitar | la guitare
piano | le piano
concert | le concert
movie | le film | gb=film
singer | le chanteur, la chanteuse
dance | la danse
photo | la photo
camera | l'appareil photo
walk | la promenade
art | l'art | u
painting | la peinture, le tableau
""",
"tech_a1": """
phone | le téléphone
cell phone | le téléphone portable | gb=mobile phone
laptop | l'ordinateur portable
screen | l'écran
internet | internet | u
website | le site web
app | l'application
message | le message
password | le mot de passe
television | la télévision
TV | la télé
radio | la radio
newspaper | le journal
magazine | le magazine
video | la vidéo
printer | l'imprimante
battery | la batterie, la pile | pl=batteries
remote control | la télécommande
news | les informations, les nouvelles | u
""",
"feelings_a1": """
feeling | le sentiment
love | l'amour | u
happiness | le bonheur | u
fear | la peur
anger | la colère | u
sadness | la tristesse | u
dream | le rêve
idea | l'idée
problem | le problème
worry | le souci | pl=worries
smile | le sourire
kiss | le bisou, le baiser | pl=kisses
luck | la chance | u
fun | l'amusement, le plaisir | u
help | l'aide | u
""",
"everyday_a1": """
thing | la chose
life | la vie | pl=lives
number | le nombre, le numéro
part | la partie
piece | le morceau
side | le côté
end | la fin
beginning | le début
place | l'endroit, le lieu
list | la liste
color | la couleur | gb=colour
shape | la forme
circle | le cercle
triangle | le triangle
group | le groupe
pair | la paire
half | la moitié | pl=halves
box | la boîte | pl=boxes
light | la lumière
plan | le projet, le plan
habit | l'habitude
""",
}
