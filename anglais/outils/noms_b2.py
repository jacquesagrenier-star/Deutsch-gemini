# -*- coding: utf-8 -*-
"""Les noms du B2 anglais, par theme. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que noms_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'B2'

# (id, nom du theme en anglais, theme source dont on reprend l'icone)
THEMES = [
    ('family_b2', 'Family and relationships', 'familie_b2'),
    ('work_b2', 'Work and careers', 'arbeit_buero_b2'),
    ('food_b2', 'Food and cooking', 'obst_gemuese_b2'),
    ('home_b2', 'Home and DIY', 'wohnen_b2'),
    ('health_b2', 'Body and health', 'koerperteile_b2'),
    ('clothes_b2', 'Clothes and appearance', 'kleidung_b2'),
    ('nature_b2', 'Nature and the environment', 'tiere_b2'),
    ('travel_b2', 'Travel and transportation', 'verkehr_b2'),
    ('city_b2', 'The city', 'stadt_gebaeude_b2'),
    ('education_b2', 'School and studies', 'schule_b2'),
    ('culture_b2', 'Free time and culture', 'freizeit_hobbys_b2'),
    ('sports_b2', 'Sports', 'sport_b2'),
    ('media_b2', 'Media and communication', 'medien_technologie_b2'),
    ('money_b2', 'Money and the economy', 'la_macroeconomia'),
    ('feelings_b2', 'Feelings and character', 'nom_interior'),
    ('society_b2', 'Society and politics', 'politik_gesellschaft_b2'),
    ('ideas_b2', 'Ideas and debate 1', 'pensamiento_critico'),
    ('ideas_b2_2', 'Ideas and debate 2', 'pensamiento_critico'),
    ('time_b2', 'Time', 'zeit_kalender_b2'),
    ('everyday_b2', 'Everyday words', 'zahlen_mengen_b2'),
]

NOMS = {
"family_b2": """
adoption | l'adoption
blended family | la famille recomposée
descendant | le descendant
family cohesion | cohésion familiale
family tree | l'arbre généalogique
foster child | l'enfant placé
half-brother | le demi-frère
half-sister | la demi-sœur
legal guardian | le tuteur légal
child support | la pension alimentaire | u | ex=He pays child support every month. # Il verse une pension alimentaire tous les mois.
parents-in-law | les beaux-parents | plt
relatives | les proches, la famille | plt
sister-in-law | la belle-sœur | pl=sisters-in-law
stepfather | le beau-père
stepmother | la belle-mère
""",
"work_b2": """
accountability | l'obligation de rendre des comptes | u
agenda | l'ordre du jour
apprentice | l'apprenti(e)
burnout | l'épuisement professionnel | u
business trip | le voyage professionnel
charisma | le charisme
civil servant | le fonctionnaire
corporate culture | la culture d'entreprise
delegation | la délégation | ex=A delegation from Canada visited the factory. # Une délégation canadienne a visité l'usine.
digital nomad | le nomade numérique
employment contract | le contrat de travail
entrepreneur | l'entrepreneur
flextime | les horaires flexibles | u | gb=flexitime | ex=Our company offers flextime. # Notre entreprise propose des horaires flexibles.
freelancer | le, la freelance, l'indépendant(e)
head of department | le chef de service
human resources | les ressources humaines
indicator | l'indicateur
managing director | la directrice générale
mentor | le mentor
minutes | le compte rendu (de réunion) | plt
obsolescence | l'obsolescence
professional experience | l'expérience professionnelle
reference | le rapport, la référence
reputation | la réputation
retraining | la reconversion
salary negotiation | la négociation salariale
labor shortage | la pénurie de main-d'œuvre | u | gb=labour shortage
superior | le, la supérieur(e) hiérarchique | ex=You should discuss it with your superior. # Tu devrais en parler à ton supérieur.
tax advisor | le conseiller fiscal
template | le modèle
vision | la vision
work-life balance | l'équilibre vie-travail
""",
"food_b2": """
artichoke | l'artichaut
best-by date | la date limite de consommation | gb=best-before date | ex=The yogurt is past its best-by date. # Le yaourt a dépassé sa date limite.
blender | le mixeur
celery | le céleri | u
chard | la blette
currant | la groseille
cutting board | la planche à découper
range hood | la hotte | gb=cooker hood | ex=Turn on the range hood when you cook. # Allume la hotte quand tu cuisines.
fennel | le fenouil
fig | la figue
food processor | le robot de cuisine
food supplement | le complément alimentaire | ex=She takes a vitamin D food supplement in winter. # Elle prend un complément de vitamine D en hiver.
frozen food | les surgelés | u
gooseberry | la groseille à maquereau
grater | la râpe
stovetop | la plaque de cuisson | gb=hob | ex=The pot is still hot on the stovetop. # La casserole est encore chaude sur la plaque.
kohlrabi | le chou-rave
measuring cup | le verre doseur | gb=measuring jug | ex=Use a measuring cup for the flour. # Utilise un verre doseur pour la farine.
pantry | le garde-manger
papaya | la papaye
pomegranate | la grenade
spice rack | l'étagère à épices
supply | la réserve, l'approvisionnement
sweet potato | la patate douce | pl=sweet potatoes
tasting | la dégustation
vegan | le végétalien
vegetarian | le végétarien
""",
"home_b2": """
attic | le grenier | ex=We keep old toys in the attic. # Nous gardons de vieux jouets au grenier.
bed linen | le linge de lit
clothes dryer | le sèche-linge
condominium | l'appartement en copropriété
energy efficiency | l'efficacité énergétique
wall-to-wall carpet | la moquette | gb=fitted carpet | ex=The bedroom has wall-to-wall carpet. # La chambre est recouverte de moquette.
housing market | le marché immobilier
lease | le bail
mattress | le matelas
sideboard | le buffet (meuble)
utilities | les charges (eau, électricité) | plt | ex=Is the rent including utilities? # Le loyer inclut-il les charges ?
""",
"health_b2": """
bladder | la vessie | ex=Drinking water is good for your bladder. # Boire de l'eau est bon pour la vessie.
blood pressure | la tension artérielle
buttocks | les fesses | plt
collarbone | la clavicule
family doctor | le médecin de famille | ex=I've had the same family doctor for twenty years. # J'ai le même médecin de famille depuis vingt ans.
healthcare system | le système de santé
immune system | le système immunitaire
intestine | l'intestin | ex=Fiber is good for the intestines. # Les fibres sont bonnes pour l'intestin.
kneecap | la rotule
metabolism | le métabolisme
nervous system | le système nerveux
physical therapy | la kinésithérapie | u | gb=physiotherapy | ex=After the accident, he needed months of physical therapy. # Après l'accident, il a eu besoin de mois de kinésithérapie.
pulse | le pouls
rib | la côte
shoulder blade | l'omoplate
doctor's note | le certificat médical | gb=sick note | ex=You need a doctor's note if you miss more than two days. # Il faut un certificat médical si tu manques plus de deux jours.
spine | la colonne vertébrale
tendon | le tendon
waiting room | la salle d'attente
""",
"clothes_b2": """
blazer | le blazer
collar | le col
fashion trend | la tendance mode
linen | le lin
sole | la semelle
pantyhose | le collant | u | gb=tights | ex=She wore black pantyhose with her dress. # Elle portait un collant noir avec sa robe.
undershirt | le maillot de corps | gb=vest
""",
"nature_b2": """
air quality | la qualité de l'air
amphibian | l'amphibien
antlers | les bois (de cerf) | plt
bat | la chauve-souris
beak | le bec
black ice | le verglas | u
claw | la griffe
climate change | le changement climatique
cold snap | la vague de froid | ex=A sudden cold snap killed the flowers. # Une brusque vague de froid a tué les fleurs.
crack | la fissure
eagle | l'aigle
carbon footprint | l'empreinte carbone | ex=Flying less reduces your carbon footprint. # Prendre moins l'avion réduit ton empreinte carbone.
erosion | l'érosion
fox | le renard
fur | la fourrure | u | ex=The cat's fur is very soft. # Le pelage du chat est très doux.
habitat | l'habitat
heatwave | la canicule
hydrogen | l'hydrogène
lead | le plomb | u
mammal | le mammifère
natural disaster | la catastrophe naturelle
pasture | le pâturage
precipitation | la précipitation
rain shower | l'averse | ex=There may be a few rain showers this afternoon. # Il pourrait y avoir quelques averses cet après-midi.
reptile | le reptile
resilience | la résilience
rock | le rocher
rodent | le rongeur
ruminant | le ruminant
single-use plastic | le plastique à usage unique | u
snowfall | la chute de neige
solar system | le système solaire
stream | le ruisseau
sustainable development | le développement durable
swamp | le marais | ex=Alligators live in the swamp. # Des alligators vivent dans le marais.
water pollution | la pollution de l'eau | u
wild animal | l'animal sauvage
wind power | l'énergie éolienne | u
""",
"travel_b2": """
parking garage | le parking couvert | gb=multi-storey car park | ex=We left the car in the parking garage. # Nous avons laissé la voiture au parking.
tour guide | le, la guide
traffic rule | la règle de circulation
travel insurance | l'assurance voyage | u
""",
"city_b2": """
backyard | le jardin derrière la maison | gb=back garden
church tower | le clocher
city wall | le rempart
dam | le barrage
gentrification | la gentrification | u
urban planning | l'urbanisme
""",
"education_b2": """
dissertation | la thèse (de doctorat)
education system | le système éducatif
equal opportunity | l'égalité des chances
final exam | l'examen final | ex=The final exam is on Friday. # L'examen final a lieu vendredi.
finding | le résultat (d'une étude)
homeroom teacher | le professeur principal | gb=form teacher | ex=My homeroom teacher called my parents. # Mon professeur principal a appelé mes parents.
GPA | la moyenne générale | ex=She graduated with a 3.9 GPA. # Elle a obtenu son diplôme avec une moyenne de 3,9 sur 4.
dorm | la résidence universitaire | gb=hall of residence | ex=Freshmen usually live in a dorm. # Les étudiants de première année vivent souvent en résidence.
high school diploma | le diplôme de fin d'études secondaires
master's thesis | le mémoire de master | pl=master's theses
methodology | la méthodologie
parent-teacher conference | la réunion parents-professeurs | gb=parents' evening | ex=The parent-teacher conference is next Thursday. # La réunion parents-professeurs a lieu jeudi prochain.
research grant | la bourse de recherche
school trip | le voyage scolaire
schoolyard | la cour de récréation | gb=playground | ex=The kids are playing in the schoolyard. # Les enfants jouent dans la cour de récréation.
scientific paper | l'article scientifique
thesis | la thèse | pl=theses
variable | la variable
""",
"culture_b2": """
act | l'acte (de théâtre)
aesthetics | l'esthétique | u
ambivalence | l'ambivalence
applause | les applaudissements | u
artistic movement | le courant artistique
birthday party | la fête d'anniversaire
ceremony | la cérémonie
christening | le baptême
cohesion | la cohésion
collection | la collection
community | la communauté
composition | la composition
draft | le brouillon, l'ébauche
ending | le dénouement
festivity | la festivité
funeral | l'enterrement
gardening | le jardinage
harmony | l'harmonie
hiking trail | le sentier de randonnée
host | l'hôte (qui reçoit)
literary criticism | la critique littéraire
melancholy | la mélancolie
membership | l'adhésion
narrative style | le style narratif
narrator | le narrateur
nostalgia | la nostalgie | u | ex=He looks at old photos with nostalgia. # Il regarde ses vieilles photos avec nostalgie.
passion | la passion
point of view | le point de vue
rehearsal | la répétition
remorse | le remords
resignation | la résignation
ritual | le rituel
self-fulfillment | l'épanouissement personnel | u
social class | la classe sociale
social mobility | la mobilité sociale
social norm | la norme sociale
sociology | la sociologie
stereotype | le stéréotype
symbolism | le symbolisme
volunteer work | le bénévolat | u
""",
"sports_b2": """
competitive sport | le sport de haut niveau
endurance sport | le sport d'endurance
opponent | l'adversaire
workout | la séance d'entraînement | ex=I do a short workout every morning. # Je fais une courte séance de sport tous les matins.
""",
"media_b2": """
artificial intelligence | l'intelligence artificielle
automation | l'automatisation
browser | le navigateur
correspondent | le correspondant
cybersecurity | la cybersécurité
data protection | la protection des données
digitalization | la numérisation
disinformation | la désinformation
irony | l'ironie
journalism | le journalisme
metaphor | la métaphore
newsroom | la rédaction
oversight | la surveillance, l'oubli
persuasion | la persuasion
press conference | la conférence de presse
reliability | la fiabilité
rhetoric | la rhétorique
scoop | le scoop
""",
"money_b2": """
bank statement | le relevé de compte
bargain | la bonne affaire
deficit | le déficit
automatic payment | le prélèvement automatique | gb=direct debit | ex=I pay my phone bill by automatic payment. # Je paie ma facture de téléphone par prélèvement automatique.
gross domestic product | le produit intérieur brut
macroeconomics | la macroéconomie | u
productivity | la productivité
public debt | la dette publique
purchasing power | le pouvoir d'achat
recession | la récession
stimulus | la relance, le stimulus | pl=stimuli
coupon | le bon de réduction | gb=voucher | ex=I have a coupon for twenty percent off. # J'ai un bon de réduction de vingt pour cent.
""",
"feelings_b2": """
affection | l'affection
amazement | l'étonnement
ambition | l'ambition
anguish | l'angoisse
assumption | la supposition
consolation | la consolation
despair | le désespoir
determination | la détermination | u
empathy | l'empathie
fate | le destin
gossip | les ragots | u
impatience | l'impatience
impulse | l'impulsion
instinct | l'instinct
likelihood | la probabilité
modesty | la modestie
pity | la pitié
remedy | le remède
self-reflection | l'introspection
serenity | la sérénité
shame | la honte | u
suspicion | le soupçon
uncertainty | l'incertitude
unease | l'inquiétude
""",
"society_b2": """
abstention | l'abstention
alliance | l'alliance
anthropology | l'anthropologie
authority | l'autorité
censorship | la censure
competitiveness | la compétitivité | u
consensus | le consensus
constituency | la circonscription
dignity | la dignité
diplomacy | la diplomatie
election campaign | la campagne électorale
ethnic group | l'ethnie
federation | la fédération | ex=The national soccer federation chose a new coach. # La fédération nationale de football a choisi un nouvel entraîneur.
geopolitics | la géopolitique | u
globalization | la mondialisation | u | ex=Globalization has changed the job market. # La mondialisation a changé le marché du travail.
guide | le guide
impunity | l'impunité
interdependence | l'interdépendance
legacy | l'héritage
legislation | la législation
mediation | la médiation
ministry | le ministère
multinational | la multinationale
offshoring | la délocalisation
referendum | le référendum
sanction | la sanction
separation of powers | la séparation des pouvoirs
sovereignty | la souveraineté
supply chain | la chaîne d'approvisionnement
tariff | le droit de douane
term of office | le mandat | pl=terms of office
""",
"ideas_b2": """
ambiguity | l'ambiguïté
bias | le biais
bioethics | la bioéthique | u
clause | la clause
clinical trial | l'essai clinique
coherence | la cohérence
commemoration | la commémoration
concept | le concept
concession | la concession
consciousness | la conscience | u | ex=He lost consciousness after the fall. # Il a perdu connaissance après la chute.
contradiction | la contradiction
controversy | la polémique
counterargument | le contre-argument
courtesy | la politesse
criterion | le critère | pl=criteria
data privacy | la confidentialité des données
deadlock | l'impasse
dilemma | le dilemme
emphasis | l'accent (mis sur) | pl=emphases
ethics | l'éthique | u
euphemism | l'euphémisme
evidence | la preuve | u
existence | l'existence
fallacy | le sophisme
gene | le gène
genetics | la génétique | u
grave | la tombe
integrity | l'intégrité
jargon | le jargon
limit | la limite
margin | la marge
moderator | le modérateur
morality | la morale
nuance | la nuance
objection | l'objection
objectivity | l'objectivité
oblivion | l'oubli
""",
"ideas_b2_2": """
paradox | le paradoxe
precision | la précision
premise | la prémisse
principle | le principe
reasoning | le raisonnement
redress | la réparation
register | le registre (de langue)
skepticism | le scepticisme | u | ex=The plan was met with skepticism. # Le projet a été accueilli avec scepticisme.
subtlety | la subtilité
synonym | le synonyme
tact | le tact
testimony | le témoignage
thinker | le penseur
tone | le ton
trade-off | le compromis
transparency | la transparence
""",
"time_b2": """
backlog | le retard accumulé
leap year | l'année bissextile
time zone | le fuseau horaire
""",
"everyday_b2": """
calculation | le calcul
condition | la condition
difference | la différence
disadvantage | l'inconvénient
element | l'élément
estimate | l'estimation
fraction | la fraction
length | la longueur
outline | le contour
perspective | la perspective, le point de vue | ex=Living abroad gave me a new perspective. # Vivre à l'étranger m'a donné un nouveau regard.
quota | le quota | ex=There's a quota on fishing in these waters. # La pêche est soumise à un quota dans ces eaux.
section | la section, le passage
width | la largeur | ex=Measure the width of the window. # Mesure la largeur de la fenêtre.
""",
}
