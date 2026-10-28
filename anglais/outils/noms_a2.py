# -*- coding: utf-8 -*-
"""Les noms du A2 anglais, par theme. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que noms_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'A2'

# (id, nom du theme en anglais, theme source dont on reprend l'icone)
THEMES = [
    ('family_a2', 'Family and relationships', 'familie_a2'),
    ('work_a2', 'Work and careers', 'berufe_a2'),
    ('food_a2', 'Food and cooking 1', 'obst_gemuese_a2'),
    ('food_a2_2', 'Food and cooking 2', 'obst_gemuese_a2'),
    ('home_a2', 'Home and DIY 1', 'moebel_haushalt_a2'),
    ('home_a2_2', 'Home and DIY 2', 'moebel_haushalt_a2'),
    ('health_a2', 'Body and health', 'koerperteile_a2'),
    ('clothes_a2', 'Clothes and appearance', 'el_aspecto'),
    ('nature_a2', 'Nature and the environment 1', 'natur_a2'),
    ('nature_a2_2', 'Nature and the environment 2', 'natur_a2'),
    ('travel_a2', 'Travel and transportation 1', 'reisen_urlaub_a2'),
    ('travel_a2_2', 'Travel and transportation 2', 'reisen_urlaub_a2'),
    ('city_a2', 'The city', 'stadt_gebaeude_a2'),
    ('education_a2', 'School and studies', 'los_estudios'),
    ('culture_a2', 'Free time and culture 1', 'el_cine'),
    ('culture_a2_2', 'Free time and culture 2', 'el_cine'),
    ('sports_a2', 'Sports', 'el_deporte'),
    ('media_a2', 'Media and communication', 'medien_technologie_a2'),
    ('money_a2', 'Money and the economy', 'einkaufen_geld_a2'),
    ('feelings_a2', 'Feelings and character', 'gefuehle_charakter_a2'),
    ('society_a2', 'Society and politics', 'politik_gesellschaft_a2'),
    ('law_a2', 'Law and safety', 'la_seguridad'),
    ('time_a2', 'Time', 'zeit_kalender_a2'),
    ('everyday_a2', 'Everyday words', 'grundwortschatz_a2'),
]

NOMS = {
"family_a2": """
acquaintance | la connaissance (personne) | ex=She's not a friend, just an acquaintance. # Ce n'est pas une amie, juste une connaissance.
ancestor | l'ancêtre
apology | l'excuse
argument | la dispute
birth | la naissance
childhood | l'enfance | u
conflict | le conflit
contact | le contact
daughter-in-law | la belle-fille | pl=daughters-in-law
decision | la décision
divorce | le divorce
experience | l'expérience
favor | le service, la faveur | ex=Can you do me a favor? # Tu peux me rendre un service ?
friendship | l'amitié
generation | la génération
godfather | le parrain
godmother | la marraine
great-grandfather | l'arrière-grand-père
inheritance | l'héritage
invitation | l'invitation
marital status | la situation familiale
marriage | le mariage (institution)
mother-in-law | la belle-mère | pl=mothers-in-law
old age | la vieillesse | u
relationship | la relation
relative | le parent (famille)
son-in-law | le gendre | pl=sons-in-law
spouse | le conjoint
stage | l'étape
support | le soutien | u
teenager | l'adolescent, l'adolescente
twin | le jumeau
visit | la visite | ex=Thanks for your visit! # Merci de ta visite !
youth | la jeunesse | u
father-in-law | le beau-père | pl=fathers-in-law
""",
"work_a2": """
actor | l'acteur
author | l'auteur
babysitter | le baby-sitter
budget | le budget
businessman | l'homme d'affaires | pl=businessmen
change | le changement
conversation | la conversation
dentist | le dentiste
department | le service
planner | l'agenda | gb=diary | ex=I wrote the date in my planner. # J'ai noté la date dans mon agenda.
employee | l'employé, l'employée
remote work | le télétravail | u
househusband | l'homme au foyer
ink | l'encre
job interview | l'entretien d'embauche
mechanic | le mécanicien
model | le mannequin
musician | le musicien
overtime | l'heure supplémentaire
retiree | le retraité, la retraitée | gb=pensioner | ex=Many retirees move to Florida. # Beaucoup de retraités partent vivre en Floride.
photographer | le photographe
pilot | le pilote
plumber | le plombier
position | le poste
programmer | le programmeur
promotion | la promotion
resume | le CV | gb=CV
secretary | la secrétaire
technician | le technicien
thief | le voleur | pl=thieves
turn | le tour | ex=It's your turn to choose the movie. # C'est ton tour de choisir le film.
veterinarian | le vétérinaire
workday | la journée de travail | gb=working day | ex=My workday starts at eight. # Ma journée de travail commence à huit heures.
workshop | l'atelier (formation)
""",
"food_a2": """
apricot | l'abricot
apron | le tablier
avocado | l'avocat | pl=avocados
baking sheet | la plaque de four
bean | le haricot
blackberry | la mûre
blueberry | la myrtille, le bleuet
bread roll | le petit pain | ex=I'd like two bread rolls, please. # Je voudrais deux petits pains, s'il vous plaît.
broccoli | le brocoli | u
cabbage | le chou | u
can opener | l'ouvre-boîte
cauliflower | le chou-fleur | u
cherry | la cerise
chocolate | le chocolat | u
coconut | la noix de coco
coffee machine | la machine à café
corkscrew | le tire-bouchon
corn | le maïs | u
counter | le comptoir
cream | la crème | u
dishes | la vaisselle | plt
dough | la pâte
drink menu | la carte des boissons | ex=Could we see the drink menu? # Pourrions-nous voir la carte des boissons ?
eggplant | l'aubergine | gb=aubergine
flavor | le goût
flour | la farine | u
frying pan | la poêle
grapefruit | le pamplemousse
honey | le miel | u
ingredient | l'ingrédient
jam | la confiture | u
kiwi | le kiwi
leek | le poireau
lemonade | la limonade
lid | le couvercle
lime | le citron vert
mango | la mangue
melon | le melon
mixing bowl | le saladier
mustard | la moutarde
""",
"food_a2_2": """
noodles | les nouilles | plt | ex=We had chicken soup with noodles. # Nous avons mangé une soupe au poulet avec des nouilles.
pea | le petit pois
peach | la pêche
pineapple | l'ananas
plum | la prune
pub | le pub
pumpkin | la citrouille, la courge | ex=We carve a pumpkin every Halloween. # Nous sculptons une citrouille chaque Halloween.
raspberry | la framboise
sausage | la saucisse
slice | la tranche
spice | l'épice
spinach | l'épinard | u
steam | la vapeur | u
strainer | la passoire
tangerine | la mandarine
vegetable | le légume
vinegar | le vinaigre
walnut | la noix
watermelon | la pastèque
whisk | le fouet
wooden spoon | la cuillère en bois
yogurt | le yaourt | u
zucchini | la courgette | gb=courgette
hunger | la faim | u | ex=After the hike, we were dying of hunger. # Après la randonnée, nous mourions de faim.
thirst | la soif | u | ex=Water is the best drink for thirst. # L'eau est la meilleure boisson contre la soif.
""",
"home_a2": """
armchair | le fauteuil
awning | le store (auvent)
basement | le sous-sol
basket | le panier
bookshelf | la bibliothèque (meuble)
brick | la brique
broom | le balai
bucket | le seau
cardboard | le carton (matière) | u
cardboard box | la boîte en carton
casserole dish | la cocotte
chain | la chaîne
coat hanger | le cintre | ex=Put your jacket on a coat hanger. # Mets ta veste sur un cintre.
coffee table | la table basse
detergent | la lessive
doorbell | la sonnette
drill | la perceuse
dust | la poussière | u
entrance hall | le hall d'entrée
envelope | l'enveloppe
fabric | le tissu
fan | le ventilateur
fence | la clôture
fireplace | la cheminée
first floor | le rez-de-chaussée | gb=ground floor | ex=The kitchen is on the first floor. # La cuisine est au rez-de-chaussée. | exgb=The kitchen is on the ground floor.
floor lamp | le lampadaire
floor plan | le plan (appartement)
front yard | le jardin devant la maison | gb=front garden | ex=The kids are playing in the front yard. # Les enfants jouent dans le jardin devant la maison.
hammer | le marteau
heater | l'appareil de chauffage
heating | le chauffage | u
hook | le crochet
household | le foyer, le ménage
housing | le logement
inner courtyard | la cour intérieure
ironing board | la planche à repasser
lampshade | l'abat-jour
landlady | la propriétaire (bailleuse) | ex=Our landlady lives upstairs. # Notre propriétaire habite à l'étage.
laundry | le linge (à laver) | u
laundry basket | le panier à linge
""",
"home_a2_2": """
leather | le cuir | u
mailbox | la boîte aux lettres | gb=letterbox
light bulb | l'ampoule | ex=Can you change the light bulb in the hall? # Tu peux changer l'ampoule de l'entrée ?
lock | la serrure
machine | la machine
metal | le métal
mop | la serpillière
mortgage | le prêt immobilier
move | le déménagement
moving box | le carton de déménagement
nightstand | la table de chevet
owner | le propriétaire
plant pot | le pot de fleurs
pliers | la pince | plt
poster | le poster
radiator | le radiateur
railing | la grille
renovation | les travaux
roof terrace | la terrasse sur le toit
roommate | le, la colocataire | gb=flatmate | ex=My roommate is from Ohio. # Mon colocataire vient de l'Ohio.
scissors | les ciseaux | plt
screw | la vis
screwdriver | le tournevis
sign | le panneau
outlet | la prise de courant | gb=socket
stain | la tache
stick | le bâton
stool | le tabouret
storage room | le débarras
tenant | le locataire
tile | le carreau
tool | l'outil
toolbox | la boîte à outils
trash can | la poubelle | gb=bin
tray | le plateau
vacuum cleaner | l'aspirateur
wastebasket | la corbeille à papier | gb=wastepaper bin | ex=Throw it in the wastebasket. # Jette-le dans la corbeille.
wool | la laine | u
terrace | la terrasse
piece of furniture | le meuble | pl=pieces of furniture | ex=This old chair is my favorite piece of furniture. # Cette vieille chaise est mon meuble préféré.
""",
"health_a2": """
allergy | l'allergie
ankle | la cheville
balance | l'équilibre
bandage | le pansement, le bandage
belly button | le nombril
bottom | les fesses
breathing | la respiration
cheek | la joue
chest | la poitrine
chin | le menton
cosmetics | les cosmétiques | plt | ex=She sells natural cosmetics online. # Elle vend des cosmétiques naturels en ligne.
cough syrup | le sirop contre la toux | ex=Take a spoonful of cough syrup before bed. # Prends une cuillerée de sirop contre la toux avant de dormir.
death | la mort
diet | le régime
dizziness | le vertige | u
doctor's office | le cabinet médical | gb=doctor's surgery
drop | la goutte
elbow | le coude
emergency | l'urgence
exam table | la table d'examen | gb=examination couch | ex=Please lie down on the exam table. # Allongez-vous sur la table d'examen, s'il vous plaît.
eyebrow | le sourcil
forehead | le front
handkerchief | le mouchoir | ex=He took a handkerchief out of his pocket. # Il a sorti un mouchoir de sa poche.
health insurance | l'assurance maladie | u
heel | le talon
lip | la lèvre
meditation | la méditation
nail | l'ongle
nausea | la nausée
operation | l'opération
palm | la paume
patient | le patient
perfume | le parfum
scale | la balance (pèse-personne) | gb=scales | plgb=scales | ex=I weigh myself on the bathroom scale. # Je me pèse sur la balance de la salle de bain. | exgb=I weigh myself on the bathroom scales.
stress | le stress
surgery | la chirurgie, l'opération
symptom | le symptôme
syringe | la seringue
tension | la tension
thigh | la cuisse
toe | l'orteil
tongue | la langue (organe)
treatment | le traitement
vaccine | le vaccin
weight | le poids
well-being | le bien-être | u
wound | la blessure
belly | le ventre
""",
"clothes_a2": """
appearance | l'allure, l'apparence
bathrobe | le peignoir | gb=dressing gown
beard | la barbe
bracelet | le bracelet
button | le bouton
clothing | les vêtements, habillement | u
cotton | le coton | u
fashion | la mode
garment | le vêtement
hairstyle | la coiffure
height | la taille (d'une personne)
makeup | le maquillage | u | ex=She never wears makeup to work. # Elle ne se maquille jamais pour aller travailler.
mustache | la moustache
necklace | le collier
piercing | le piercing
rain jacket | l'imperméable
sleeve | la manche
style | le style
swimsuit | le maillot de bain
tattoo | le tatouage | pl=tattoos
tie | la cravate
underwear | les sous-vêtements | u
wrinkle | la ride
wristwatch | la montre
zipper | la fermeture éclair | gb=zip
sandal | la sandale
underpants | le caleçon, le slip | plt
""",
"nature_a2": """
ant | la fourmi
trash bag | le sac poubelle | gb=bin bag | ex=Can you take out the trash bag? # Tu peux sortir le sac poubelle ?
blossom | la fleur, la floraison
branch | la branche
butterfly | le papillon
cave | la grotte
coast | la côte
countryside | la campagne | u
desert | le désert
dew | la rosée
dolphin | le dauphin
donkey | l'âne
drought | la sécheresse
east | l'est
energy | l'énergie | u
fire | l'incendie
frog | la grenouille
glacier | le glacier
goose | l'oie | pl=geese
greenhouse effect | l'effet de serre
ground | le sol
hail | la grêle
hedgehog | l'hérisson
hill | la colline
iron | le fer | u
land | la terre
landscape | le paysage
lawn | la pelouse
conservation | la protection de la nature | u
nest | le nid
north | le nord
parrot | le perroquet
pigeon | le pigeon
planet | la planète
plastic | le plastique | u
pollution | la pollution | u
rainbow | l'arc-en-ciel
rat | le rat
""",
"nature_a2_2": """
rose | la rose
seagull | la mouette
seed | la graine
shark | le requin
shore | la rive
smoke | la fumée
snail | l'escargot
solar energy | l'énergie solaire | u
south | le sud
squirrel | l'écureuil
sunshine | le soleil, l'ensoleillement | u
valley | la vallée
volcano | le volcan | pl=volcanoes
global warming | le réchauffement climatique | u
warmth | la chaleur | u
recycling | le recyclage, le tri des déchets | u
waterfall | la cascade
wave | la vague
weather forecast | les prévisions météo
west | l'ouest
whale | la baleine
wind energy | l'énergie éolienne | u
wolf | le loup | pl=wolves
dragon | le dragon
dwarf | le nain | pl=dwarfs | ex=Snow White lives with seven dwarfs. # Blanche-Neige vit avec sept nains.
goldfish | le poisson rouge
climate | le climat | u
snowman | le bonhomme de neige | pl=snowmen
""",
"travel_a2": """
accident | l'accident
accommodation | l'hébergement | u
agency | l'agence
arrival | l'arrivée
baggage carousel | le tapis à bagages
baggage claim | la récupération des bagages
boarding | l'embarquement
border | la frontière
campground | le terrain de camping | gb=campsite | ex=The campground is right next to the lake. # Le camping est juste à côté du lac.
check-in | l'enregistrement
city map | le plan de la ville
complaint | la réclamation
connecting flight | le vol de correspondance
connection | la correspondance, connexion
crosswalk | le passage piéton | gb=zebra crossing | ex=Always cross at the crosswalk. # Traverse toujours au passage piéton.
customs | la douane | plt
customs control | le contrôle douanier
bike lane | la piste cyclable | gb=cycle lane | ex=There's a new bike lane on Main Street. # Il y a une nouvelle piste cyclable sur Main Street.
day trip | l'excursion
departure | le départ
destination | la destination
distance | la distance
double room | la chambre double
engine | le moteur
flight attendant | l'agent de bord, l'hôtesse de l'air
foreigner | l'étranger
guidebook | le guide (livre)
guided tour | la visite guidée
helmet | le casque
holiday | le jour férié, la fête
information | le renseignement | u
insurance | l'assurance | u
intersection | le carrefour | gb=crossroads
itinerary | l'itinéraire
landing | l'atterrissage
noise | le bruit
pedestrian | le piéton
""",
"travel_a2_2": """
postcard | la carte postale
purpose | le but
reception | la réception
receptionist | le réceptionniste
route | l'itinéraire
safe | le coffre-fort
sand | le sable | u
school vacation | les vacances scolaires | gb=school holidays | ex=We go to the beach during school vacation. # Nous allons à la plage pendant les vacances scolaires.
security | la sécurité | u
shell | le coquillage
ship | le bateau, le navire
shovel | la pelle
sleeping pad | le tapis de sol | gb=sleeping mat | ex=Don't forget your sleeping pad. # N'oublie pas ton tapis de sol.
start | le début, le départ | ex=We missed the start of the movie. # Nous avons raté le début du film.
stay | le séjour
stopover | l'escale
takeoff | le décollage | gb=take-off | ex=Please turn off your phone before takeoff. # Veuillez éteindre votre téléphone avant le décollage.
tent | la tente
terminal | le terminal
ticket machine | le distributeur de billets
tire | le pneu | gb=tyre | ex=We had a flat tire on the way. # Nous avons crevé en route.
tour | la visite, l'excursion
traffic circle | le rond-point | gb=roundabout | ex=Turn right at the traffic circle. # Tournez à droite au rond-point.
vacation rental | la location de vacances | gb=holiday let
view | la vue
visa | le visa
airplane | l'avion | gb=aeroplane | ex=The airplane landed on time. # L'avion a atterri à l'heure.
beach umbrella | le parasol | ex=We sat under a beach umbrella all afternoon. # Nous sommes restés sous un parasol tout l'après-midi.
""",
"city_a2": """
block | le pâté de maisons
castle | le château
deadline | le délai, l'échéance
delivery | l'envoi
department store | le grand magasin
document | le document
entrance | l'entrée
fee | les frais
form | le formulaire
fountain | la fontaine
kiosk | le kiosque
loan | le prêt
middle | le milieu
paperwork | les papiers, les démarches | u | ex=There's a lot of paperwork for a visa. # Il y a beaucoup de démarches pour un visa.
pedestrian zone | la zone piétonne
residential neighborhood | le quartier résidentiel
savings | l'épargne | plt
skyscraper | le gratte-ciel
stamp | le timbre
street lamp | le réverbère
tax | l'impôt | u
port | le port
center | le centre | gb=centre
""",
"education_a2": """
admission | l'admission
doubt | le doute
effort | l'effort
enrollment | l'inscription
history | l'histoire | u
internship | le stage
kindergarten | la maternelle
knowledge | la connaissance | u
lecture hall | l'amphithéâtre
master's degree | le master | ex=She has a master's degree in biology. # Elle a un master en biologie.
note | la note (écrite), le mot
participant | le, la participant(e)
pencil case | la trousse
practice | la pratique, l'entraînement
principal | le directeur | gb=head teacher
research | la recherche | u
result | le résultat
scholarship | la bourse
text | le texte
textbook | le manuel scolaire
theory | la théorie
topic | le sujet, thème
university cafeteria | la cafétéria universitaire
pupil | l'élève
chalk | la craie
globe | le globe
seminar | le séminaire
lecture notes | les notes de cours | plt
""",
"culture_a2": """
angel | l'ange
anniversary | l'anniversaire (d'un événement)
artist | l'artiste
audience | le public | u
award | le prix
balloon | le ballon de baudruche
band | le groupe (de musique)
board game | le jeu de société
box office | le guichet
carnival | le carnaval
choir | le chœur
Christmas present | le cadeau de Noël
circus | le cirque
club | le club
comedy | la comédie
costume | le déguisement
craft | l'artisanat, le bricolage
crime novel | le roman policier, le polar | ex=I'm reading a crime novel set in Boston. # Je lis un polar qui se passe à Boston.
director | le réalisateur
drawing | le dessin
drum | le tambour
embarrassment | la gêne, la honte | ex=His face went red with embarrassment. # Son visage est devenu rouge de gêne.
excitement | l'excitation, l'enthousiasme | u | ex=The kids couldn't sleep from excitement. # Les enfants ne pouvaient pas dormir tant ils étaient excités.
exhibition | l'exposition
fair | la foire
Father's Day | la fête des pères
gallery | la galerie
genre | le genre
guitar case | l'étui à guitare
hike | la randonnée
interest | l'intérêt
laughter | le rire | u
lyrics | les paroles (d'une chanson) | plt
Mother's Day | la fête des mères
New Year's Eve | le réveillon du nouvel an
novel | le roman
orchestra | l'orchestre
parade | le défilé
poem | le poème
procession | la procession
""",
"culture_a2_2": """
puzzle | le puzzle
quiz | le quiz, jeu de questions
record | le disque
rhythm | le rythme
scene | la scène
script | le scénario
sculpture | la sculpture
showing | la séance
sketch | l'esquisse
string | la corde (d'un instrument)
subtitle | le sous-titre | ex=I watch movies with English subtitles. # Je regarde les films avec des sous-titres en anglais.
toast | le toast (on lève son verre)
tradition | la tradition
violin | le violon
witch | la sorcière
writer | l'écrivain
excursion | l'excursion
""",
"sports_a2": """
championship | le championnat
coach | l'entraîneur
soccer field | le terrain de football | gb=football pitch | ex=The soccer field is behind the school. # Le terrain de football est derrière l'école.
handball | le handball | u
jump | le saut
long-distance race | la course de fond
medal | la médaille
referee | l'arbitre
sports bag | le sac de sport
step | le pas
tournament | le tournoi
volleyball | le volley-ball
training | l'entraînement
hall | la salle, le hall
sports field | le terrain de sport | ex=The new sports field is behind the high school. # Le nouveau terrain de sport est derrière le lycée.
""",
"media_a2": """
accent | l'accent
ad | l'annonce, la pub | gb=advert
advertising | la publicité
advice | le conseil | u
article | l'article
cable | le câble
call | l'appel
channel | la chaîne
charger | le chargeur
data | les données | u
debate | le débat
device | l'appareil
e-book | le livre électronique | ex=I read e-books on my tablet. # Je lis des livres électroniques sur ma tablette.
explanation | l'explication
file | le fichier
folder | le dossier
front page | la une
gesture | le geste
headline | le titre
headphones | les écouteurs, le casque | plt
incident | l'incident
journalist | le journaliste
keyboard | le clavier
link | le lien
misunderstanding | le malentendu
net | le filet | ex=The ball hit the net. # Le ballon a touché le filet.
network | le réseau
opinion | l'opinion
computer | l'ordinateur
phone call | l'appel téléphonique
press | la presse
program | le programme | gb=programme
recipient | le destinataire
silence | le silence
source | la source
speaker | le haut-parleur
summary | le résumé
tablet | la tablette
translation | la traduction
user | l'utilisateur
Wi-Fi | le wifi | u | ex=What's the Wi-Fi password? # Quel est le mot de passe du wifi ?
""",
"money_a2": """
ATM | le distributeur de billets | gb=cash machine | ex=Is there an ATM near here? # Il y a un distributeur de billets près d'ici ? | exgb=Is there a cash machine near here?
bank account | le compte bancaire | ex=I need to open a bank account. # Je dois ouvrir un compte bancaire.
brochure | le prospectus, brochure
cent | le centime
checking account | le compte courant | gb=current account
debt | la dette
exchange | l'échange (achat)
expense | la dépense
flea market | le marché aux puces
gold | l'or | u
income | le revenu
loss | la perte
package | le colis | gb=parcel | ex=A package arrived for you this morning. # Un colis est arrivé pour toi ce matin.
pay stub | la fiche de paie | gb=payslip | ex=Keep your pay stubs for your taxes. # Garde tes fiches de paie pour tes impôts.
product | le produit
profit | le gain, le bénéfice
savings account | le compte épargne
service | le service
shopping cart | le caddie, le chariot | gb=shopping trolley | ex=The shopping cart is already full. # Le caddie est déjà plein.
silver | l'argent (métal) | u
vending machine | le distributeur automatique | ex=The vending machine only takes coins. # Le distributeur n'accepte que les pièces.
wallet | le portefeuille
discount | la réduction, le rabais
quality | la qualité
""",
"feelings_a2": """
attitude | l'attitude
boredom | l'ennui
character | le caractère
confusion | la confusion
curiosity | la curiosité
desire | le désir, l'envie | ex=He has a strong desire to travel. # Il a une forte envie de voyager.
farewell | l'adieu, le départ
flaw | le défaut
lie | le mensonge
mood | l'humeur
nervousness | la nervosité | u
patience | la patience | u
personality | la personnalité
pride | la fierté | u
relief | le soulagement
satisfaction | la satisfaction
surprise | la surprise
tear | la larme
trust | la confiance
voice | la voix
""",
"society_a2": """
candidate | le candidat
capital city | la capitale
democracy | la démocratie
election | l'élection
flag | le drapeau
god | le dieu
homeland | le pays d'origine
ID card | la carte d'identité
king | le roi
minister | le ministre
parliament | le parlement
permission | l'autorisation, permission | u
police | la police | u
political party | le parti politique | ex=Which political party do you vote for? # Pour quel parti politique votes-tu ?
queen | la reine
vote | le vote
war | la guerre
signature | la signature
Switzerland | la Suisse
Austrian | l'Autrichien
European | l'Européen
""",
"law_a2": """
alarm | l'alarme
ambulance | l'ambulance
danger | le danger
fine | l'amende
firefighter | le pompier
police station | le commissariat
report | le rapport, la déclaration
theft | le vol
witness | le témoin | pl=witnesses
""",
"time_a2": """
future | l'avenir
past | le passé
quarter of an hour | le quart d'heure
present | le cadeau ; le présent | ex=I'm looking for a present for my mother. # Je cherche un cadeau pour ma mère.
""",
"everyday_a2": """
amount | la quantité
attempt | la tentative
attention | l'attention
breakdown | la panne | ex=We had a breakdown on the highway. # Nous sommes tombés en panne sur l'autoroute.
case | le cas
chance | la chance, l'occasion
cube | le cube
cylinder | le cylindre
dozen | la douzaine
fault | la faute, le défaut
gentleman | le monsieur | pl=gentlemen | ex=This gentleman is asking for you. # Ce monsieur vous demande.
gram | le gramme
jar | le pot, le bocal
kilo | le kilo
liter | le litre
movement | le mouvement
oval | l'ovale
percent | le pour cent
pile | le tas, la pile | ex=There's a pile of laundry on the bed. # Il y a une pile de linge sur le lit.
posture | la posture
pyramid | la pyramide
quarter | le quart
reason | la raison
rectangle | le rectangle
risk | le risque
row | la rangée, file
rule | la règle
situation | la situation
solution | la solution
sphere | la sphère
sum | la somme
thanks | les remerciements | plt
third | le tiers | ex=A third of the students live on campus. # Un tiers des étudiants habitent sur le campus.
remainder | le reste | ex=I'll pay the remainder next month. # Je paierai le reste le mois prochain.
greeting | la salutation
""",
}
