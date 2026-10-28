# -*- coding: utf-8 -*-
"""Les noms du C1 anglais, par theme. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que noms_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'C1'

# (id, nom du theme en anglais, theme source dont on reprend l'icone)
THEMES = [
    ('family_c1', 'Family and relationships', 'alter_abschied_c1'),
    ('work_c1', 'Work and careers', 'arbeit_buero_c1'),
    ('food_c1', 'Food and cooking', 'kueche_kochen_c1'),
    ('home_c1', 'Home and DIY', 'garten_pflanzen_c1'),
    ('health_c1', 'Body and health', 'gesundheit_c1'),
    ('clothes_c1', 'Clothes and appearance', 'kleidung_c1'),
    ('nature_c1', 'Nature and the environment 1', 'umwelt_c1'),
    ('nature_c1_2', 'Nature and the environment 2', 'umwelt_c1'),
    ('travel_c1', 'Travel and transportation', 'verkehr_c1'),
    ('city_c1', 'The city', 'stadt_gebaeude_c1'),
    ('education_c1', 'School and studies', 'universitaet_c1'),
    ('culture_c1', 'Free time and culture 1', 'technik_kunst_c1'),
    ('culture_c1_2', 'Free time and culture 2', 'technik_kunst_c1'),
    ('sports_c1', 'Sports', 'sport_c1'),
    ('media_c1', 'Media and communication', 'bildung_medien_c1'),
    ('money_c1', 'Money and the economy 1', 'wirtschaft_verwaltung_c1'),
    ('money_c1_2', 'Money and the economy 2', 'wirtschaft_verwaltung_c1'),
    ('feelings_c1', 'Feelings and character', 'gefuehle_charakter_c1'),
    ('society_c1', 'Society and politics', 'gesellschaft_wandel_c1'),
    ('law_c1', 'Law and safety', 'recht_justiz_c1'),
    ('ideas_c1', 'Ideas and debate 1', 'ursache_wirkung_c1'),
    ('ideas_c1_2', 'Ideas and debate 2', 'ursache_wirkung_c1'),
    ('ideas_c1_3', 'Ideas and debate 3', 'ursache_wirkung_c1'),
]

NOMS = {
"family_c1": """
advance directive | les directives anticipées
attachment figure | la figure de référence
care home | la EHPAD, maison de soins
care worker | l'auxiliaire de vie
caring nature | la attention bienveillante | u
class group | le groupe classe
compulsory schooling | l'obligation scolaire
condolences | les condoléances
defiant phase | la période d'opposition
developmental step | l'étape de développement
discretion | la discrétion
duty of supervision | l'obligation de surveillance
estate settlement | le règlement de la succession
estrangement | l'éloignement, aliénation
falling-out | la brouille profonde
familiarity | la familiarité, intimité
frailty | la fragilité (grand âge)
funeral service | la cérémonie funéraire
generational change | le changement de génération
homework supervision | l'aide aux devoirs
isolation | l'isolement, solitude subie
learning environment | l'environnement d'apprentissage
obituary | la nécrologie, hommage
parenting style | le style éducatif
pension entitlement | le droit à la retraite
rapprochement | le rapprochement
resentment | la envie, malveillance
retirement | la retraite | u
role-model function | la fonction d'exemple
sense of security | le sentiment de sécurité affective | u
setting boundaries | la pose de limites
special educational need | le besoin de soutien scolaire
staff-to-child ratio | le taux d'encadrement
twilight years | les fin de vie, vieux jours
""",
"work_c1": """
adaptation | l'adaptation, ajustement
additional service | la prestation supplémentaire
appointment booking | la prise de rendez-vous
appreciation | la reconnaissance, estime
availability | la joignabilité, accessibilité
background | le parcours, itinéraire
burden | la charge, contrainte
cancellation | l'annulation
capacity utilization | le taux de charge, occupation
career path | la carrière, parcours professionnel
complaints handling | la gestion des réclamations
contract term | la durée du contrat
cost estimate | le devis
customs clearance | le dédouanement
cycle | le cycle, circuit
everyday working life | le quotidien professionnel | pl=everyday working lives
excess | la franchise (assurance)
finiteness | la caractère fini, finitude | u
freight costs | les frais de transport
goodwill | le geste commercial
interim storage | l'entrepôt intermédiaire
inventory management | la gestion des stocks | u
manager | le cadre dirigeant
notice period | le délai de préavis
on-call duty | l'astreinte, disponibilité
onboarding | la période de formation initiale
order picking | la préparation de commandes
order situation | le carnet de commandes
packaging unit | l'unité de conditionnement
pallet | la palette
parcel tracking | le suivi de colis
pressure to perform | la pression de la performance
processing | le traitement, exécution (d'un dossier)
rectification | la reprise, mise en conformité
renewal | le renouvellement, rénovation
resupply | le réapprovisionnement
saving | l'économie (réalisée)
service provided | la prestation de service
specialist advice | le conseil spécialisé | u
staff turnover | la rotation du personnel
supply bottleneck | la rupture d'approvisionnement
transhipment hub | la plateforme de transbordement
transit time | le durée (d'acheminement, de contrat)
transport damage | l'avarie de transport
unreasonable demand | l'exigence excessive, affront
waiting time | le temps d'attente
working atmosphere | l'ambiance de travail
""",
"food_c1": """
abstaining from consumption | le renoncement à consommer
bottling | la mise en conserve, stérilisation
browning | le coloration, brunissement
consistency | la consistance, texture
cooking time | le temps de cuisson
cutting technique | la manière de couper
daily rhythm | le rythme journalier
digital break | la pause numérique
dough handling | la conduite de la pâte
fermentation | la fermentation
infusion | l'infusion
intolerance | l'intolérance
lack of exercise | le manque d'activité physique
marinade | la marinade
maturation | l'affinage, maturation
mindfulness exercise | l'exercice de pleine conscience
nutritional value | la valeur nutritive
portion size | la taille des portions
preserving | la conservation (procédé)
recovery phase | la phase de récupération
roasted aroma | l'arôme de torréfaction
seasoning | l'assaisonnement
sequence of courses | l'ordre des plats
side dish | l'garniture, accompagnement
stimulant | le produit de plaisir (café, alcool…)
stock | le bouillon de cuisson, court-bouillon
way of eating | le régime alimentaire
way of life | la conduite de vie | pl=way of lives
well-being | le bien-être
""",
"home_c1": """
alloy | l'alliage
assembly instructions | la notice de montage
blank | l'ébauche, pièce brute
bracket | la fixation, support
building fabric | la structure du bâti
clamp | le serre-joint
coating | le revêtement
compost | le compost
custom work | le travail sur mesure
cutting | la bouture
densification | la densification
filler | l'enduit de rebouchage
final polish | la finition, dernière main
flowering period | la période de floraison
folding ruler | le mètre pliant
glut of produce | la surproduction de récolte
hardiness | la rusticité | u
heritage protection | la protection du patrimoine
housing shortage | la crise du logement
installation | la montage, pose
instructions | le mode d'emploi
insulation | l'isolation
interim use | l'occupation temporaire
local development plan | le plan local d'urbanisme
location | l'emplacement, exposition
manufacturing | la fabrication
modernization | la modernisation
mulch | le paillis
partial shade | la mi-ombre
post-processing | la reprise, retouche
precision of fit | la précision d'ajustement
primer | la sous-couche
pruning | la taille (des végétaux)
raised bed | le carré surélevé
rent index | le barème des loyers | pl=rent indexes
root system | le système racinaire
sandpaper | le papier de verre
saw blade | la lame de scie
seedling | le plant, jeune pousse
silicone | le silicone
sowing | le semis
spare parts list | la liste de pièces détachées
spirit level | le niveau à bulle
sublet | la sous-location
upkeep | l'entretien courant
vacancy | la vacance (de logements)
wall plug | la cheville
watering routine | le rythme d'arrosage
wear | l'usure
workbench | l'établi
workmanship | la façonnage, finition
""",
"health_c1": """
addictive behaviour | la conduite addictive | u
aftercare | le suivi post-thérapeutique
bed rest | le repos au lit
breathing technique | la technique respiratoire
care contract | le contrat de prise en charge
care level | le niveau de dépendance
chance of recovery | la chance de guérison
clinical picture | le tableau clinique
competitive pressure | la pression de la compétition
core tension | le gainage, tonus corporel
day care | l'accueil de jour
dependency | la dépendance
duty of documentation | l'obligation de traçabilité
exhaustion | l'épuisement
fine motor skills | la motricité fine
flexibility | la souplesse, mobilité
freedom from symptoms | l'absence de symptômes
handover | la transmission (dossier de soins)
home visit | la visite à domicile
hospice | l'unité de soins palliatifs
limit of endurance | la limite de résistance
medication administration | l'administration des médicaments
muscle soreness | les courbatures | u
overload | la surmenage, surcharge
package insert | la notice (de médicament)
pain management | le traitement de la douleur | u
pain threshold | le seuil de douleur
palliative care | les soins palliatifs
peak performance | la performance maximale
poor posture | la mauvaise posture
pre-existing condition | l'antécédent médical
qualified nurse | l'infirmier diplômé
reaction time | la capacité de réaction
recovery process | le processus de guérison
respite service | l'offre de répit
self-healing powers | les capacités d'auto-guérison
sense of balance | le sens de l'équilibre
short-term care | l'hébergement temporaire
side-effect profile | le profil d'effets secondaires
sleep disorder | le trouble du sommeil
stretching | l'étirement
torn ligament | la rupture ligamentaire
torn tendon | la rupture de tendon
training plan | le plan d'entraînement
vaccine protection | la protection vaccinale
warm-up | l'échauffement
work with relatives | l'accompagnement des proches
""",
"clothes_c1": """
colourfastness | la solidité des couleurs | u
comfort to wear | le confort de port
crease | le faux pli
cuff | le bord-côte, poignet
demeanour | la prestance, manière de se présenter
dress code | le code vestimentaire
fad | le phénomène de mode
fibre material | la matière fibreuse
fit | la coupe, tombé
handwork | le travail à la main
hem | l'ourlet
lining | la doublure
made-to-measure | le confection sur mesure
quality of workmanship | la qualité de fabrication
seam | la couture (ligne)
sewing pattern | le patron (couture)
""",
"nature_c1": """
animal keeping | la élevage, détention d'animaux
animal welfare | le bien-être animal | u
area under cultivation | la surface cultivée
bog | la tourbière, marais
breeding season | la période de nidification
bright spell | l'éclaircie
cargo | la cargaison, chargement
clearing | la clairière
cloud cover | la nébulosité
coastline | le littoral, trait de côte
conservation of resources | la préservation des ressources
conspecific | le congénère
crop rotation | la rotation des cultures
crop yield | le rendement de la récolte
direct marketing | la vente directe
disposal | l'élimination (des déchets)
distress at sea | la détresse en mer
drinking water supply | l'approvisionnement en eau potable
environmental compatibility | la compatibilité environnementale
environmental requirement | la contrainte environnementale
farm succession | la reprise de la ferme
fertilizer | l'engrais
fishing industry | la pêche (activité)
flight distance | la distance de fuite
fog bank | le banc de brouillard
food chain | la chaîne alimentaire
force of nature | la force de la nature | u
freighter | le cargo
frost line | la limite de gel
global warming | le réchauffement de la planète
greenhouse gas | le gaz à effet de serre | u
gust | la rafale
hail shower | l'averse de grêle
harbour basin | le bassin portuaire
harvest worker | le saisonnier agricole
heath | la lande
hibernation | l'hibernation
high-pressure system | l'anticyclone
land price | le prix du foncier
landing stage | l'embarcadère
""",
"nature_c1_2": """
landscape appearance | le paysage (aspect général)
litter | la portée (petits) | u
low tide | la marée basse
low-pressure system | la dépression
migratory behaviour | le comportement migratoire | u
milk yield | la production laitière
mineral resource | la ressource du sous-sol
muggy heat | la lourdeur, air moite | u
noise pollution | la nuisance sonore | u
outdoor run | l'espace de sortie, parcours
overfishing | la surpêche
pack | la meute, harde
particulate matter | les particules fines
pasture farming | l'économie pastorale
pest | le nuisible, ravageur
pollutant | le polluant
population figure | l'effectif (population animale)
prey animal | la proie
reforestation | le reboisement
renaturation | la renaturation
riparian zone | la zone riveraine
scree | l'éboulis
sea level | le niveau de la mer
severe weather warning | l'alerte météo
shallows | le haut-fond
snowmelt | la fonte des neiges
soil condition | la nature du sol
soil erosion | l'érosion des sols
soil fertility | la fertilité du sol
species extinction | l'extinction des espèces
steep slope | la pente raide
storm front | le front orageux
surf | le ressac, brisants
swarm | le banc, essaim, nuée
swell | la état de la mer, houle
temperature fluctuation | la variation de température
territorial behaviour | le comportement territorial | u
thaw | le dégel
tides | les marées
tree line | la limite des arbres
Wadden Sea | la mer des Wadden, estran
wildlife population | la population de gibier
wind direction | la direction du vent
wind force | la force du vent
""",
"travel_c1": """
alternative route | l'itinéraire de contournement
baggage drop-off | l'enregistrement des bagages
border crossing | le passage de frontière
charging infrastructure | l'infrastructure de recharge
commuting | le fait de faire la navette
detour | la déviation | gb=diversion
driving ban | l'interdiction de circuler
entry requirement | la condition d'entrée
expansion stage | la phase d'aménagement
frequency of service | le cadencement
length of stay | la durée de séjour
local public transport | le transport de proximité | u
long-distance transport | le transport longue distance | u
package holiday | le voyage à forfait
passenger numbers | le nombre de voyageurs
rebooking | le changement de réservation
right of way | la priorité
road safety | la sécurité routière | u
round trip | le circuit
route network | le réseau de lignes
traffic volume | le trafic, volume de circulation
transport transition | la transition des mobilités
travel health insurance | l'assurance maladie à l'étranger | u
trip cancellation | l'annulation de voyage
""",
"city_c1": """
green space | l'espace vert
local residents | les riverains
open space | l'espace libre
outlying district | le quartier périphérique
row of streets | l'enfilade de rues, îlot
sight line | la perspective visuelle
traffic calming | l'apaisement de la circulation
upgrading | la revalorisation, gentrification
""",
"education_c1": """
absence | l'absence
analysis | l'analyse, dépouillement | pl=analyses
approximation | l'approximation
basic research | la recherche fondamentale | u
breakthrough | la percée
change of school | le changement d'école
clarification | l'information, éclaircissement
comparability | la comparabilité
experts | le milieu spécialisé, les spécialistes
gain in knowledge | le gain de connaissance | u
grade conference | le conseil de classe
incidental finding | la découverte fortuite (examen)
life expectancy | l'espérance de vie
measurement accuracy | la précision de mesure
medical error | l'erreur médicale
note excusing absence | le justificatif d'absence
pathogen | l'agent pathogène
playground duty | la surveillance de récréation
progress | le progrès | u
re-examination | la vérification, contrôle
registration procedure | la procédure d'inscription
relapse | la rechute
report grade | la note du bulletin
reproducibility | la reproductibilité
school rules | le règlement intérieur
""",
"culture_c1": """
accompaniment | l'accompagnement
aftermath | les suite, conséquences
annual general meeting | l'assemblée générale annuelle
appeal for donations | l'appel aux dons
archive picture | la photo d'archive
audience reaction | la réaction du public
backlight | le contre-jour
balance of volume | l'équilibre des volumes
board meeting | la réunion du comité
bowing | la conduite d'archet
caption | la légende
characterization | la caractérisation des personnages
charitable status | l'utilité publique
chorus | le refrain
clubhouse | le local du club
colour cast | la dominante colorée
computing power | la puissance de calcul
conducting | la direction (d'orchestre)
declining membership | la perte d'adhérents
depth of field | la profondeur de champ
encryption | le chiffrement
ensemble | la formation, ensemble
exposure | l'exposition (photo)
figure of speech | l'image, figure de style
fingering | le doigté
focal length | la focale
framing | le cadrage
image editing | la retouche d'image
image rights | les droits d'image
imitation | l'imitation
improvisation | l'improvisation
instructor | le moniteur, encadrant
interface | l'interface
make | la facture, manière dont c'est fait
masterpiece | le chef-d'œuvre
melodic line | la conduite mélodique
membership fee | la cotisation
meter | le mètre (poésie)
mode of operation | le mode d'action, fonctionnement
narrative perspective | le point de vue narratif
""",
"culture_c1_2": """
networking | la mise en réseau
outage | la panne, défaillance
patronage | le haut patronage
performance rights | le droit de représentation
pitch | le registre (voix), ton
plot strand | le fil narratif
reading | la lecture, interprétation
register of associations | le registre des associations
reproduction | la restitution, reproduction
reverberation | la réverbération
role model | le modèle, exemple à suivre
scale | la gamme
score | la partition (d'orchestre)
sheet of music | la feuille de musique | u
shot | la prise de vue, enregistrement
stage direction | la didascalie
stage set | le décor de scène
staging | la mise en scène
statutes | les statuts
stylistic break | la rupture de style
surveillance | la surveillance
susceptibility to failure | la vulnérabilité aux pannes
timbre | le timbre
time signature | la mesure (rythmique)
treasurer's report | le rapport financier
upbeat | l'anacrouse ; coup d'envoi
usability | la facilité d'utilisation
use case | le cas d'usage
world premiere | la création (première mondiale)
youth development | la formation des jeunes
zeitgeist | l'esprit du temps
""",
"sports_c1": """
defensive line | la ligne défensive
fair play | le fair-play
goalscoring chance | l'occasion de but
league position | la place au classement
line-up | la composition d'équipe
play | l'action de jeu, combinaison
playmaker | le meneur de jeu
referee's decision | la décision arbitrale
relegation | la relégation
rule violation | l'infraction aux règles
stoppage time | le temps additionnel
substitution | le remplacement
training camp | le stage de préparation
""",
"media_c1": """
ability to retain | la capacité de mémorisation
access right | le droit d'accès
accuracy | la précision, exactitude
allusion | l'allusion (souvent moqueuse)
analysis report | le rapport d'analyse
buzzword | le slogan, mot-clé
casualness | la désinvolture, ton anodin | u
choice of words | le choix des mots
clipboard | le presse-papiers
compatibility | la compatibilité
correction | le rectificatif, démenti
credibility | la crédibilité
curriculum | le programme scolaire | pl=curricula
educational path | le parcours scolaire
empty phrase | la formule creuse
error message | le message d'erreur
exact wording | la teneur exacte, texte littéral
exaggeration | l'exagération
examination regulations | le règlement des examens
false report | la fausse nouvelle
field of study | la spécialité, filière
file format | le format de fichier
filter function | la fonction de filtrage
flaw in reasoning | l'erreur de raisonnement
general knowledge | la culture générale | u
generalization | la généralisation
half-knowledge | le demi-savoir, connaissances superficielles
hint | l'allusion, sous-entendu
idiom | l'expression idiomatique
interpretation | l'interprétation (d'un texte)
learning progress | le progrès d'apprentissage | u
log file | le fichier journal
login | la connexion, inscription
outrage | l'indignation
professional training | le perfectionnement professionnel
public | l'opinion publique, sphère publique | u
quickness of grasp | la faculté de compréhension
reporting | la couverture médiatique
rights management | la gestion des droits | u
search query | la requête de recherche
specialist knowledge | la compétence technique | u
talkativeness | la loquacité | u
technical term | le terme technique
tone of voice | le ton, intonation
transfer rate | le débit de transmission
tutoring | le cours particuliers, soutien scolaire
understatement | la litote, euphémisme
user account | le compte utilisateur
user interface | l'interface utilisateur
utterance | le propos, déclaration
wording | la formulation
""",
"money_c1": """
accident insurance | l'assurance accidents | u
advertising impact | l'impact publicitaire
area of responsibility | le domaine de compétence
assets | le patrimoine, fortune
bottleneck | le goulot d'étranglement, pénurie
brand awareness | la conscience de marque | u
building up reserves | la constitution de réserves
buying behaviour | le comportement d'achat | u
claim notification | la déclaration de sinistre
component | la composante, élément constitutif
consumer protection | la protection du consommateur
contribution rate | le taux de cotisation
cover limit | le plafond de garantie
creditworthiness | la solvabilité | u
customer retention | la fidélisation de la clientèle
default | le retard de paiement
depreciation | l'amortissement
dispute between experts | le litige d'expertise
diversification | la diversification, dispersion
economic climate | la conjoncture | u
execution | la exécution, réalisation
feature | la caractéristique, trait distinctif
implementation | la mise en œuvre
indebtedness | l'endettement | u
indication of origin | l'indication d'origine
insurance cover | la couverture d'assurance
insured event | le cas de prise en charge
interest rate | le taux d'intérêt
legal expenses cover | la protection juridique
levy | le prélèvement, taxe
loss of value | la perte de valeur
mass-produced goods | le produit de masse | plt
occupational disability | l'invalidité professionnelle
official decision | la décision administrative, notification
overdraft | le découvert
packaging waste | les déchets d'emballage | u
policyholder | le preneur d'assurance
premium payment | le paiement des cotisations
pricing | la politique de prix
quality seal | le label de qualité
""",
"money_c1_2": """
regional sourcing | la caractère régional
repayment | le amortissement (d'une dette)
reserve | la réserve, provision
retirement provision | la prévoyance vieillesse
returned direct debit | le rejet de prélèvement
right of termination | le droit de résiliation
risk surcharge | la surprime
settlement | le règlement (d'un sinistre)
shelf life | la durée de conservation | pl=shelf lives
standard | le critère, étalon
statutory warranty | la garantie légale
subsidy | la subvention, aide financière
takeover | le rachat, reprise
tax return | la déclaration d'impôts
tax-free allowance | l'abattement fiscal
tender | l'appel d'offres
third-party liability | la responsabilité civile
throwaway goods | le produit jetable | plt
value creation | la création de valeur
yield | le rendement
""",
"feelings_c1": """
absent-mindedness | la distraction, étourderie | u
assessment | l'appréciation, estimation
carelessness | l'légèreté, imprudence | u
character trait | le trait de caractère
consideration for others | les égards, considération
constancy | la constance, durabilité
delusion | l'aveuglement
design | la conception, mise en forme
expressiveness | la force expressive | u
food for thought | l'élément de réflexion
handwriting | la écriture ; patte, style personnel
high spirits | la témérité, exubérance
imaginative power | la faculté d'imagination
leniency | l'indulgence
mindfulness | la attention, pleine conscience | u
pensiveness | la gravité pensive | u
persistence | la persévérance, ténacité
postponement | le sursis, report
presumption | la présomption, arrogance
recurrence | le retour, récurrence
repression | le refoulement
self-conception | la conception de soi, image de son rôle
self-control | la maîtrise de soi
sense of entitlement | l'attitude d'attente
sequence | la succession, enchaînement
simultaneity | la simultanéité
sincerity | la sincérité
stubbornness | l'entêtement, caractère buté | u
tenacity | la ténacité, opiniâtreté
train of thought | le cheminement de pensée
transience | le caractère éphémère
urgency | l'urgence
vigilance | la vigilance
way of thinking | le mode de pensée
willpower | la force de volonté
wishful thinking | le vœu pieux, pensée illusoire
""",
"society_c1": """
balance of power | le rapport de majorité
ballot paper | le bulletin de vote | u
belonging | l'appartenance
budget debate | le débat budgétaire
chance of advancement | la chance de promotion sociale
change of power | l'alternance
claim to power | la prétention au pouvoir
conduct in office | l'exercice des fonctions
division | la division, clivage
draft bill | le projet de loi
formative influence | l'empreinte, marque formatrice
guiding principle | le modèle directeur, idéal affiché
lobbying | le lobbying
marginalized group | le groupe marginalisé
outflow | l'exode, départ (d'une région)
patronizing | la mise sous tutelle, paternalisme
population ageing | le vieillissement (de la population)
prosperity | la prospérité
social stratum | la couche sociale
taboo | le tabou
upheaval | le bouleversement
vote of confidence | la question de confiance
voter turnout | le taux de participation
""",
"law_c1": """
appeal | l'appel (recours)
arms build-up | le réarmement
arrest | l'arrestation
burden of proof | la charge de la preuve | pl=burden of proofs
case law | la jurisprudence
ceasefire | le cessez-le-feu
civil protection | la protection civile
civilian population | la population civile
compensation | l'indemnisation, dédommagement
contravention | l'infraction, contravention
crime scene | le lieu du crime
criminal complaint | la plainte pénale
deterrence | la dissuasion
disarmament | le désarmement
dissolution | la dissolution, résiliation
emergency services | les forces d'intervention
estate | la succession, héritage
evacuation | l'évacuation
expert opinion | l'expertise, rapport d'expert
forensics | la police scientifique, relevé d'indices | u
identity check | le contrôle d'identité
investigation | l'enquête (judiciaire)
legal remedy | la voie de recours
liability | la responsabilité juridique
manhunt | la recherche, avis de recherche
obligation | l'obligation, engagement
operational command | le commandement des opérations
patrol car | la voiture de patrouille
peace treaty | le traité de paix
people seeking protection | les personnes en quête de protection
place of refuge | le lieu de refuge
power of attorney | la procuration
precautionary measure | la mesure de précaution
probation | le sursis (avec mise à l'épreuve)
probation officer | l'agent de probation
questioning | l'audition, interrogatoire
reconstruction aid | l'aide à la reconstruction
regulatory offence | la contravention
requirement of consent | l'obligation d'accord préalable
search | la perquisition
security flaw | la faille de sécurité
seizure | la saisie
state of alert | l'état d'alerte
statute of limitations | la prescription
threat | la menace
trouble spot | le foyer de crise
withdrawal | la rétractation, révocation
witness protection | la protection des témoins
witness statement | le témoignage
""",
"ideas_c1": """
acceleration | l'accélération
accompanying phenomenon | le phénomène concomitant | pl=accompanying phenomena
accusation | le reproche, accusation
approval | l'approbation, accord
arbitrariness | l'arbitraire | u
arbitration | la conciliation, arbitrage
arrangement | l'arrangement, entente préalable
blessing | la bénédiction
caesura | la césure, rupture
charity | l'amour du prochain
chronicle | la chronique
clergy | le clergé
cluster | la multiplication, accumulation
compromise | le compromis
confession | la confession, aveu de foi
conscience | la conscience (morale)
contemporary witness | le témoin de l'époque
conviction | la conviction
devotion | l'office, recueillement
double standard | la deux poids deux mesures
downside | le revers, envers
driving force | la force motrice
easing | la détente, apaisement
equal treatment | l'égalité de traitement
escalation | l'exacerbation
expulsion | l'expulsion, déplacement forcé
extent | l'ampleur
faith community | la communauté religieuse
feedback loop | la rétroaction
feeling of guilt | le sentiment de culpabilité
forced labour | le travail forcé
forgiveness | le pardon | u
friction | la friction, frottement
given circumstance | la donnée, circonstance
giving in | le fait de céder
holiday custom | la coutume de fête
house of worship | l'édifice religieux
human dignity | la dignité humaine
hypocrisy | l'hypocrisie
impairment | l'altération, gêne
""",
"ideas_c1_2": """
inherited burden | le fardeau hérité
insight | le constat, connaissance acquise
insinuation | l'insinuation, procès d'intention
insistence | l'obstination, refus de céder
interaction | l'interaction réciproque
interplay | l'interaction, jeu combiné
justification | la justification
leverage | le moyen de pression
memorial | le mémorial (d'avertissement)
mercy | la miséricorde
monastery complex | l'ensemble monastique
occupation | l'occupation (militaire)
pastoral care | l'accompagnement spirituel
piece of evidence | la pièce justificative, preuve | u
piety | la piété
pilgrimage | le pèlerinage
point of contention | le point de désaccord
post-war period | l'après-guerre
power imbalance | le rapport de force inégal
pretext | le prétexte
provocation | la provocation
quid pro quo | la contrepartie
reasonableness | le caractère raisonnablement exigible | u
reconstruction | la reconstruction
rejection | le refus, rejet
relativization | la relativisation
remembrance | la commémoration
reunification | la réunification
search for meaning | la quête de sens
selflessness | le désintéressement | u
sense of duty | le sens du devoir
sense of justice | le sens de la justice | u
sense of responsibility | le sens des responsabilités
sermon | le sermon, prêche
side effect | l'effet secondaire
significance | la portée
source of error | la source d'erreur
stagnation | la stagnation
superstition | la superstition
tightening | l'aggravation, durcissement
""",
"ideas_c1_3": """
tolerance | la tolérance
trigger | le déclencheur
turnaround | le revirement
turning point | le tournant
ultimatum | l'ultimatum
unreservedness | l'absence de réserve | u
uprightness | la probité | u
upturn | l'essor, reprise
viability | la viabilité, solidité
weakening | l'atténuation
weighing up | la pesée du pour et du contre
weighting | la pondération
worldview | la conception du monde
""",
}
