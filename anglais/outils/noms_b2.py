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
maintenance | la pension alimentaire
parents-in-law | les beaux-parents
relatives | la parenté
sister-in-law | la belle-sœur | pl=sisters-in-law
stepfather | le beau-père (remariage)
stepmother | la belle-mère (remariage)
""",
"work_b2": """
accountability | la reddition de comptes
agenda | l'ordre du jour
agreed objectives | les objectifs convenus
apprentice | l'apprenti(e)
burnout | l'usure
business trip | le voyage professionnel
career changer | le reconverti professionnel
charisma | le charisme
civil servant | le fonctionnaire
corporate culture | la culture d'entreprise
delegation | la délégation
digital nomad | le nomade numérique
employment contract | le contrat de travail
entrepreneur | l'entrepreneur
filing | le classement
flexitime | les horaires flexibles
freelancer | le profession libérale
head of department | le chef de service
human resources | les ressources humaines
indicator | l'indicateur
job automation | l'automatisation de l'emploi
labour flexibility | la flexibilité du travail
managing director | la directrice générale
mentor | le mentor
minutes | le procès-verbal
obsolescence | l'obsolescence
operational risk | le risque opérationnel
professional experience | l'expérience professionnelle
reference | le rapport, la référence
reputation | la réputation
retraining | la reconversion
salary negotiation | la négociation salariale
self-employed person | l'travailleur indépendant
shift worker | le travailleur posté
skilled labor shortage | la pénurie de main-d'œuvre
superior | le supérieur hiérarchique
tax advisor | le conseiller fiscal
team motivation | la motivation de l'équipe
template | le modèle, gabarit
temporary help | l'renfort, extra | u
vision | la vision
work-life balance | l'équilibre vie-travail
works council | le comité d'entreprise
""",
"food_b2": """
artichoke | l'artichaut
best-before date | la date de péremption
blender | mixeur
celery | le céleri | u
chard | la blette
culinary art | l'art culinaire | u
cultivation | la culture (agriculture)
currant | la groseille
cutting board | la planche à découper
digestibility | digestibilité
extractor hood | la hotte aspirante
fennel | le fenouil
fig | la figue
food processor | le robot de cuisine
food supplement | le complément alimentaire
frozen food | les surgelés
gooseberry | la groseille à maquereau
grater | la râpe
hob | la plaque de cuisson
kitchen hygiene | l'hygiène en cuisine
kohlrabi | le chou-rave
measuring jug | le verre doseur
organic product | le produit bio
pantry cupboard | le garde-manger
papaya | la papaye
pomegranate | la grenade
redcurrant | la groseille
snack bar | le snack, casse-croûte
spice blend | le mélange d'épices
spice rack | l'étagère à épices
supply | la réserve, provisions
sweet potato | patate douce | pl=sweet potatoes
tasting | dégustation
vegan | le végétalien
vegetarian | le végétarien
""",
"home_b2": """
attic | le grenier
bed linen | le linge de lit
clothes dryer | sèche-linge
condominium | l'appartement en copropriété
display cabinet | la vitrine
electricity contract | le contrat d'électricité
energy efficiency | l'efficacité énergétique
fitted carpet | la moquette
fitted kitchen | la cuisine équipée
heating costs | les frais de chauffage
housing market | le marché immobilier
lease agreement | le contrat de location
mattress | le matelas
property management | la syndic, gérance | u
rent cap | le plafonnement des loyers
sideboard | le buffet/vaisselier
utility costs | les charges locatives
""",
"health_b2": """
bladder | la vessie ; ampoule
blood pressure | la tension artérielle
buttocks | les fesses, postérieur
collarbone | la clavicule
corpse | le cadavre
family doctor | le médecin traitant
health insurance fund | la caisse d'assurance maladie
healthcare system | le système de santé
immune system | le système immunitaire
intestine | l'intestin
kneecap | la rotule
metabolism | le métabolisme
nervous system | le système nerveux
physiotherapy | la kinésithérapie
preventive checkup | l'examen préventif
pulse | le pouls
rib | la côte
shoulder blade | l'omoplate
sick note | l'arrêt de travail
spine | la colonne vertébrale
tendon | le tendon
waiting room | la salle d'attente
""",
"clothes_b2": """
blazer | le blazer
collar | le col
fashion trend | la tendance mode
fitting | l'essayage
linen | le lin
sole | la semelle
sustainability label | label de durabilité
tights | le collant
undershirt | le maillot de corps | gb=vest
""",
"nature_b2": """
air quality | la qualité de l'air
amphibian | l'amphibien
antlers | les bois (de cerf)
bat | la chauve-souris
beak | le bec
bird migration | la migration des oiseaux
black ice | le verglas | u
circular economy | l'économie circulaire
claw | la griffe
climate change | le changement climatique
climate neutrality | la neutralité climatique
cold snap | le coup de froid
crack | la fissure
eagle | l'aigle
ecological footprint | le bilan écologique
energy transition | la transition énergétique
environmental damage | le dommage environnemental
environmental policy | la politique environnementale
erosion | l'érosion
extreme weather | le phénomène météo extrême | u
fox | le renard
fur | le pelage, fourrure
habitat | l'habitat
heatwave | la canicule
hydrogen | l'hydrogène
lead | le plomb
mammal | le mammifère
natural disaster | la catastrophe naturelle
neutrality | la neutralité
offset | la compensation
pasture | le pâturage ; saule
precipitation | la précipitation
rain shower | l'averse
reptile | le reptile
resilience | la résilience
rock | le rocher
rodent | le rongeur
ruminant | le ruminant
single-use plastic | le plastique à usage unique | u
snowfall | la chute de neige
solar system | l'installation solaire
species protection | la protection des espèces
stream | le ruisseau
sustainable development | le développement durable
swamp | le marais
transition | la transition
water pollution | la pollution de l'eau | u
weather situation | la situation météorologique
wild animal | l'animal sauvage
wind power | l'énergie éolienne
""",
"travel_b2": """
changing trains | la correspondance
ferry connection | la liaison par ferry
multi-storey car park | le parking couvert
overnight stay | la nuitée
sustainable tourism | le tourisme durable
tour guide | le accompagnateur, guide
traffic rule | la règle de circulation
transport infrastructure | l'infrastructure routière
travel insurance | l'assurance voyage | u
vehicle registration document | la carte grise
""",
"city_b2": """
backyard | l'arrière-cour
church tower | le clocher
city wall | le rempart
commercial estate | la zone d'activité
dam | la digue, le barrage
gentrification | gentrification
market square | la place du marché
urban development | le développement urbain
urban planning | l'urbanisme
""",
"education_b2": """
dissertation | la thèse
doctoral studies | doctorat
education system | le système éducatif
equal opportunity | l'égalité des chances
exam anxiety | la peur des examens
examinations office | le service des examens
final examination | l'examen final
finding | la découverte
form teacher | le professeur principal
grade average | la moyenne générale
habilitation | l'habilitation
hall of residence | la résidence universitaire
high school diploma | le baccalauréat
master's thesis | le mémoire de master | pl=master's theses
methodology | la méthodologie
packed snack | le casse-croûte de la récréation
parents' evening | la journée de rencontre parents-professeurs
replication | la réplication
research grant | la bourse de recherche
school trip | le voyage scolaire
school yard | la cour de récréation
scientific paper | la publication scientifique | u
thesis | la thèse | pl=theses
university place | la place à l'université
variable | la variable
""",
"culture_b2": """
act | l'acte
admission ticket | le billet d'entrée
aesthetics | l'esthétique | u
ambivalence | l'ambivalence
applause | les applaudissements | u
artistic movement | le courant artistique
bewilderment | le désarroi
birthday party | la fête d'anniversaire
ceremony | la cérémonie
christening | le baptême
cohesion | la cohésion
collection | la collection
community | la communauté
composition | la composition
draft | le projet, esquisse
ending | le dénouement
festivity | festivité
funeral | l'enterrement
gardening | le jardinage
harmony | l'harmonie
hiking trail | le sentier de randonnée
host | l'hôte (qui reçoit)
literary criticism | la critique littéraire
lost generation | la génération perdue
melancholy | la mélancolie
membership | l'adhésion
narrative style | le style narratif
narrator | le narrateur
nostalgia | la nostalgie
passion | la passion
point of view | le point de vue
reading matter | la lecture, de quoi lire
rehearsal | la répétition
remorse | le remords
resignation | la résignation
ritual | le rituel
rootlessness | le déracinement | u
self-fulfillment | l'épanouissement personnel
social class | la classe sociale
social mobility | la mobilité sociale
social norm | la norme sociale
sociology | la sociologie
stereotype | le stéréotype
symbolism | le symbolisme
visual texture | la texture visuelle
volunteer role | la fonction bénévole
volunteer work | bénévolat
""",
"sports_b2": """
competitive sport | le sport de haut niveau
endurance sport | le sport d'endurance
opponent | l'adversaire
sport discipline | la discipline sportive
training session | la séance d'entraînement
""",
"media_b2": """
algorithmic bias | le biais algorithmique
algorithmic transparency | la transparence algorithmique
artificial intelligence | l'intelligence artificielle
automation | l'automatisation
backup copy | la copie de sauvegarde
browser | le navigateur
correspondent | le correspondant
cybersecurity | la cybersécurité
data protection | la protection des données
digitalization | la numérisation
disinformation | la désinformation
editorial bias | le biais éditorial
editorial team | la rédaction
irony | l'ironie
journalism | le journalisme
metaphor | la métaphore
newsroom | la rédaction
oversight | la supervision
persuasion | la persuasion
press conference | la conférence de presse
reliability | la fiabilité
retort | la réplique
rhetoric | la rhétorique
rhetorical emphasis | l'emphase rhétorique | pl=rhetorical emphases
scoop | le scoop
truthfulness | la véracité | u
""",
"money_b2": """
bank statement | le relevé de compte
bargain | la bonne affaire
consumer behavior | le comportement de consommation | u
deficit | le déficit
direct debit | le prélèvement automatique
gross domestic product | le produit intérieur brut
macroeconomics | la macroéconomie | u
price comparison | la comparaison de prix
productivity | la productivité
public debt | la dette publique
purchasing power | le pouvoir d'achat
recession | la récession
savings book | le livret d'épargne
stimulus | la relance | pl=stimuli
voucher | le bon d'achat
""",
"feelings_b2": """
affection | l'affection
amazement | l'étonnement
ambition | l'ambition
anguish | l'angoisse
assumption | la supposition
bedside table | la table de nuit
consolation | la consolation
despair | le désespoir
determination | l'acharnement
empathy | l'empathie
fate | le destin
gossip | le bavardage, les racontars
impatience | l'impatience
impulse | l'impulsion
instinct | l'instinct
likelihood | la probabilité
modesty | la modestie
pity | la pitié, le dommage
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
administrative act | l'acte administratif
alliance | l'alliance
anthropology | l'anthropologie
authority | l'administration, service public
Basic Law | la Loi fondamentale
censorship | la censure
citizen participation | la participation citoyenne
competitiveness | la compétitivité | u
consensus | le consensus
constituency | la circonscription
cultural mixing | le métissage
dignity | la dignité
diplomacy | la diplomatie
diplomatic tension | la tension diplomatique
displaced person | la personne déplacée
election campaign | la campagne électorale
ethnic group | l'ethnie
federalism | le fédéralisme
federation | la fédération, l'alliance
geopolitics | la géopolitique | u
globalization | la mondialisation
guide | le guide
impunity | l'impunité
interdependence | l'interdépendance
legacy | l'héritage culturel
legal protection | la protection légale
legislation | la législation
mediation | la médiation
ministry | le ministère
multinational | la multinationale
office holder | le titulaire d'une charge publique
offshoring | la délocalisation
parliamentary group | le groupe parlementaire
referendum | le référendum
sanction | la sanction
separation of powers | la séparation des pouvoirs
social criticism | la critique sociale
sovereignty | la souveraineté
supply chain | la chaîne d'approvisionnement
symbolic kinship | la parenté symbolique
tariff | le droit de douane
term of office | le mandat
universal declaration | la déclaration universelle
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
consciousness | la conscience | u
contradiction | la contradiction
controversy | la polémique
counterargument | le contre-argument
courtesy | la politesse
criterion | le critère | pl=criteria
data privacy | la confidentialité des données
deadlock | l'impasse
dilemma | le dilemme
emphasis | l'emphase | pl=emphases
ethics | l'éthique | u
euphemism | l'euphémisme
evidence | la preuve | u
exhumation | l'exhumation
existence | l'existence
fallacy | le sophisme
gene | le gène
genetics | la génétique | u
grave | la fosse
historical memory | la mémoire historique
integrity | l'intégrité
jargon | le jargon
limit | la limite
margin | la marge
moderator | le modérateur
morality | la morale
mutual commitment | l'engagement mutuel
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
register | le registre
scepticism | le scepticisme
speaking turn | le tour de parole
subtlety | la subtilité
synonym | le synonyme
tact | le tact
testimony | le témoignage
thinker | le penseur
tone | le ton
trade-off | la contrepartie
transparency | la transparence
""",
"time_b2": """
backlog | le retard accumulé
half-year | le semestre
lead time | le temps de préparation
leap year | l'année bissextile
period of time | le laps de temps
time zone | le fuseau horaire
transition phase | la phase de transition
""",
"everyday_b2": """
calculation | le calcul
colour gradient | le dégradé de couleurs
condition | la condition
difference | la différence, écart
disadvantage | l'inconvénient
element | l'élément
estimate | l'estimation
fraction | la fraction ; fracture
length | la longueur
outline | le contour
perspective | la perspective
quota | le quota/taux
section | la section, le passage
shading | la nuance, dégradé
width | la largeur
""",
}
