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
    ('academic_c1', 'Academic English', 'argumentation_c1'),
]

NOMS = {
"family_c1": """
advance directive | les directives anticipées
attachment figure | la figure de référence
care home | la EHPAD, maison de soins
care worker | l'auxiliaire de vie
compulsory schooling | l'obligation scolaire
condolences | les condoléances
discretion | la discrétion
estrangement | l'éloignement, aliénation
falling-out | la brouille | ex=The two brothers had a falling-out over money. # Les deux frères se sont brouillés pour une histoire d'argent.
familiarity | la familiarité, la connaissance | u | ex=Familiarity with the software is an advantage. # Une bonne connaissance du logiciel est un atout.
frailty | la fragilité (grand âge)
funeral service | la cérémonie funéraire
isolation | l'isolement | u | ex=Many elderly people suffer from isolation. # Beaucoup de personnes âgées souffrent de l'isolement.
obituary | la nécrologie, hommage
parenting style | le style éducatif
rapprochement | le rapprochement
resentment | le ressentiment | u
retirement | la retraite | u
twilight years | les vieux jours | plt
""",
"work_c1": """
adaptation | l'adaptation, ajustement
appreciation | la reconnaissance, estime
availability | la disponibilité | u
background | le parcours, les antécédents
burden | la charge, contrainte
cancellation | l'annulation
career path | le parcours professionnel | ex=She's thinking about changing her career path. # Elle pense à changer de voie professionnelle.
cost estimate | le devis | ex=Can you give me a cost estimate for the repairs? # Pouvez-vous me faire un devis pour les réparations ?
customs clearance | le dédouanement
cycle | le cycle, circuit
excess | l'excès
goodwill | la bonne volonté | u
manager | le, la responsable, le gérant
notice period | le délai de préavis
onboarding | l'intégration (d'un nouvel employé) | u | ex=Onboarding takes about two weeks. # L'intégration dure environ deux semaines.
pallet | la palette
renewal | le renouvellement | ex=Your passport is due for renewal. # Ton passeport doit être renouvelé.
saving | l'économie (réalisée)
staff turnover | la rotation du personnel | u
waiting time | le temps d'attente
""",
"food_c1": """
consistency | la consistance, texture
cooking time | le temps de cuisson
fermentation | la fermentation
infusion | l'infusion
intolerance | l'intolérance
marinade | la marinade
maturation | l'affinage, maturation
nutritional value | la valeur nutritive
portion size | la taille des portions
preserving | la conservation (procédé)
seasoning | l'assaisonnement
side dish | l'accompagnement (plat)
stimulant | le stimulant | ex=Caffeine is a mild stimulant. # La caféine est un léger stimulant.
stock | le bouillon (de cuisson)
way of life | le mode de vie | pl=ways of life
well-being | le bien-être
""",
"home_c1": """
alloy | l'alliage
assembly instructions | la notice de montage
bracket | le support, l'équerre
clamp | le serre-joint
coating | le revêtement
compost | le compost
cutting | la bouture
filler | l'enduit de rebouchage
folding ruler | le mètre pliant
housing shortage | la crise du logement
installation | l'installation, la pose
instructions | le mode d'emploi | plt
insulation | l'isolation
location | l'emplacement
manufacturing | la fabrication
modernization | la modernisation
mulch | le paillis
partial shade | la mi-ombre | u
primer | la sous-couche
pruning | la taille (des végétaux)
raised bed | le carré surélevé
root system | le système racinaire
sandpaper | le papier de verre
seedling | le plant, jeune pousse
silicone | le silicone
sowing | le semis
spirit level | le niveau à bulle
sublet | la sous-location | ex=I found a cheap sublet for the summer. # J'ai trouvé une sous-location bon marché pour l'été.
upkeep | l'entretien | u
vacancy | le logement vacant, le poste vacant
wall anchor | la cheville | gb=wall plug | ex=You'll need wall anchors to hang the shelf. # Il te faudra des chevilles pour accrocher l'étagère.
wear | l'usure | u
workbench | l'établi
workmanship | la qualité d'exécution, la finition | u
""",
"health_c1": """
addictive behavior | les conduites addictives | u
aftercare | le suivi post-thérapeutique
bed rest | le repos au lit
breathing technique | la technique respiratoire
day care | l'accueil de jour | u
dependency | la dépendance
exhaustion | l'épuisement
fine motor skills | la motricité fine | plt
flexibility | la souplesse, mobilité
handover | la passation, la transmission
home visit | la visite à domicile
hospice | l'unité de soins palliatifs
muscle soreness | les courbatures | u | ex=Muscle soreness usually disappears after two days. # Les courbatures disparaissent généralement au bout de deux jours.
overload | la surcharge, le surmenage
package insert | la notice (de médicament)
pain management | le traitement de la douleur | u
pain threshold | le seuil de douleur
palliative care | les soins palliatifs
peak performance | la performance maximale
poor posture | la mauvaise posture
pre-existing condition | l'antécédent médical
registered nurse | l'infirmier diplômé, l'infirmière diplômée | ex=She works as a registered nurse at Mass General. # Elle travaille comme infirmière diplômée au Mass General.
reaction time | le temps de réaction | ex=Alcohol slows down your reaction time. # L'alcool ralentit le temps de réaction.
sense of balance | le sens de l'équilibre
sleep disorder | le trouble du sommeil
stretching | les étirements | u
torn ligament | la rupture du ligament | ex=He's out for the season with a torn ligament. # Il est forfait pour la saison à cause d'une rupture du ligament.
training plan | le plan d'entraînement
warm-up | l'échauffement
""",
"clothes_c1": """
crease | le pli
cuff | le poignet, le revers
demeanor | l'allure, l'attitude | u | ex=Despite the bad news, she kept a calm demeanor. # Malgré la mauvaise nouvelle, elle a gardé une attitude calme.
dress code | le code vestimentaire
fad | la mode passagère
fit | la coupe, le tombé
hem | l'ourlet
lining | la doublure
seam | la couture
""",
"nature_c1": """
animal welfare | le bien-être animal | u
bog | la tourbière
breeding season | la période de nidification
cargo | la cargaison | u | ex=The ship was carrying a cargo of grain. # Le navire transportait une cargaison de céréales.
clearing | la clairière
cloud cover | la nébulosité
coastline | le littoral, trait de côte
crop rotation | la rotation des cultures | u | ex=Crop rotation keeps the soil healthy. # La rotation des cultures garde le sol en bonne santé.
crop yield | le rendement des cultures | ex=The drought reduced crop yields. # La sécheresse a réduit le rendement des cultures.
disposal | l'élimination (des déchets) | u
fertilizer | l'engrais
fishing industry | l'industrie de la pêche | ex=Gloucester depends on the fishing industry. # Gloucester dépend de l'industrie de la pêche.
fog bank | le banc de brouillard
food chain | la chaîne alimentaire
force of nature | la force de la nature | ex=My grandmother is a real force of nature. # Ma grand-mère est une vraie force de la nature.
freighter | le cargo
global warming | le réchauffement de la planète
greenhouse gas | le gaz à effet de serre | u
gust | la rafale
hail shower | l'averse de grêle
heath | la lande
hibernation | l'hibernation
high-pressure system | l'anticyclone
""",
"nature_c1_2": """
litter | la portée (petits) | u
low tide | la marée basse
low-pressure system | la dépression
noise pollution | la nuisance sonore | u
overfishing | la surpêche
pack | la meute
particulate matter | les particules fines
pest | le nuisible
pollutant | le polluant
prey | la proie | u
reforestation | le reboisement
sea level | le niveau de la mer
weather warning | l'alerte météo
shallows | le haut-fond | plt | ex=The children played in the shallows. # Les enfants jouaient là où l'eau était peu profonde.
snowmelt | la fonte des neiges
soil erosion | l'érosion des sols
surf | les vagues, le ressac | u
swarm | l'essaim, la nuée | ex=A swarm of bees flew over the garden. # Un essaim d'abeilles a survolé le jardin.
swell | la houle | u
thaw | le dégel
tides | les marées | plt
tree line | la limite des arbres
wind direction | la direction du vent
""",
"travel_c1": """
border crossing | le passage de frontière
commuting | les trajets domicile-travail | u | ex=Commuting takes up two hours of my day. # Les trajets me prennent deux heures par jour.
detour | la déviation | gb=diversion
public transit | les transports en commun | u | gb=public transport | ex=Boston has good public transit. # Boston a de bons transports en commun.
package tour | le voyage organisé | gb=package holiday | ex=We booked a package tour to Mexico. # Nous avons réservé un voyage organisé au Mexique.
right of way | la priorité
road safety | la sécurité routière | u | ex=The campaign is about road safety. # La campagne porte sur la sécurité routière.
round trip | l'aller-retour | ex=A round trip to New York costs about fifty dollars. # Un aller-retour pour New York coûte une cinquantaine de dollars.
""",
"city_c1": """
green space | l'espace vert
local residents | les riverains | plt
""",
"education_c1": """
absence | l'absence
analysis | l'analyse | pl=analyses
approximation | l'approximation
basic research | la recherche fondamentale | u
breakthrough | la percée
clarification | la clarification, la précision | ex=I'd like some clarification on this point. # J'aimerais une précision sur ce point.
comparability | la comparabilité
life expectancy | l'espérance de vie
medical error | l'erreur médicale
pathogen | l'agent pathogène | ex=The virus is a dangerous pathogen. # Le virus est un agent pathogène dangereux.
progress | le progrès | u
relapse | la rechute
school rules | le règlement intérieur | plt
""",
"culture_c1": """
accompaniment | l'accompagnement
aftermath | les suites, les conséquences | u
board meeting | la réunion du comité
caption | la légende
chorus | le refrain, le chœur
clubhouse | le local du club
depth of field | la profondeur de champ
encryption | le chiffrement
ensemble | la formation, ensemble
exposure | l'exposition (photo)
figure of speech | la figure de style, la façon de parler | pl=figures of speech | ex=Don't worry, it was just a figure of speech. # Ne t'inquiète pas, c'était une façon de parler.
imitation | l'imitation
improvisation | l'improvisation
instructor | le moniteur, encadrant
interface | l'interface
masterpiece | le chef-d'œuvre
membership fee | la cotisation
""",
"culture_c1_2": """
networking | le réseautage | u | ex=Networking is important in this industry. # Le réseautage est important dans ce secteur.
outage | la panne
pitch | la hauteur (d'un son), le ton | ex=Her voice rose in pitch when she got nervous. # Sa voix devenait plus aiguë quand elle était nerveuse.
reading | la lecture, l'interprétation
reproduction | la restitution, reproduction
role model | le modèle, l'exemple à suivre
scale | la gamme
score | la partition
sheet music | la partition | u | ex=She can play without sheet music. # Elle sait jouer sans partition.
shot | la prise de vue
stage direction | la didascalie
staging | la mise en scène | ex=The staging of the play was very modern. # La mise en scène de la pièce était très moderne.
surveillance | la surveillance | u | ex=The building is under video surveillance. # Le bâtiment est sous vidéosurveillance.
timbre | le timbre
time signature | la mesure (rythmique)
usability | la facilité d'utilisation
world premiere | la création (première mondiale)
zeitgeist | l'esprit du temps | u | ex=The song captured the zeitgeist of the sixties. # La chanson a saisi l'esprit des années soixante.
""",
"sports_c1": """
fair play | le fair-play
line-up | la composition d'équipe
playmaker | le meneur de jeu
relegation | la relégation
stoppage time | le temps additionnel
substitution | le remplacement
training camp | le stage de préparation
""",
"media_c1": """
accuracy | la précision, exactitude
allusion | l'allusion | ex=The title is an allusion to an old poem. # Le titre est une allusion à un vieux poème.
buzzword | le mot à la mode
choice of words | le choix des mots
clipboard | le presse-papiers
compatibility | la compatibilité
correction | le rectificatif, démenti
credibility | la crédibilité
curriculum | le programme scolaire | pl=curricula
error message | le message d'erreur
exaggeration | l'exagération
field of study | la spécialité, filière
file format | le format de fichier
general knowledge | la culture générale | u
generalization | la généralisation
hint | l'allusion, l'indice
idiom | l'expression idiomatique
interpretation | l'interprétation (d'un texte)
login | la connexion, inscription
outrage | l'indignation
public | l'opinion publique, sphère publique | u
reporting | la couverture médiatique
search query | la requête de recherche
technical term | le terme technique
tone of voice | le ton | ex=I didn't like his tone of voice. # Je n'ai pas aimé son ton.
tutoring | le soutien scolaire, les cours particuliers | u
understatement | la litote, euphémisme
user account | le compte utilisateur
user interface | l'interface utilisateur
wording | la formulation
""",
"money_c1": """
assets | les actifs, le patrimoine | plt | ex=The company sold some of its assets. # L'entreprise a vendu une partie de ses actifs.
bottleneck | le goulot d'étranglement
brand awareness | la conscience de marque | u
component | la composante, élément constitutif
consumer protection | la protection du consommateur
creditworthiness | la solvabilité | u
default | le défaut de paiement
depreciation | l'amortissement, la dépréciation | u | ex=A new car loses value through depreciation. # Une voiture neuve perd de la valeur avec la dépréciation.
diversification | la diversification, dispersion
execution | l'exécution | ex=The idea was good, but the execution was poor. # L'idée était bonne, mais l'exécution laissait à désirer.
feature | la caractéristique, trait distinctif
implementation | la mise en œuvre
insurance coverage | la couverture d'assurance | u | gb=insurance cover | ex=Check your insurance coverage before you travel. # Vérifie ta couverture d'assurance avant de voyager.
interest rate | le taux d'intérêt
levy | la taxe, le prélèvement
overdraft | le découvert | ex=I have an overdraft of two hundred dollars. # J'ai un découvert de deux cents dollars.
packaging waste | les déchets d'emballage | u
policyholder | l'assuré | ex=The policyholder must report the damage within a week. # L'assuré doit déclarer le sinistre dans la semaine.
pricing | la politique de prix
""",
"money_c1_2": """
repayment | le remboursement
reserve | la réserve, provision
settlement | le règlement, l'accord
shelf life | la durée de conservation | pl=shelf lives
standard | la norme, le niveau
subsidy | la subvention, aide financière
takeover | le rachat (d'une entreprise)
tax return | la déclaration d'impôts
tender | l'appel d'offres
yield | le rendement
""",
"feelings_c1": """
absent-mindedness | la distraction, étourderie | u
assessment | l'appréciation, estimation
carelessness | la négligence | u
character trait | le trait de caractère
delusion | l'illusion
design | la conception, mise en forme
food for thought | matière à réflexion | u
handwriting | l'écriture | u
high spirits | la bonne humeur | plt | ex=The team was in high spirits after the win. # L'équipe était de très bonne humeur après la victoire.
leniency | l'indulgence | u | ex=The judge showed leniency because of his age. # Le juge a fait preuve d'indulgence en raison de son âge.
mindfulness | la pleine conscience | u
persistence | la persévérance, ténacité
postponement | le report | ex=The rain caused a postponement of the game. # La pluie a provoqué le report du match.
recurrence | le retour, récurrence
repression | la répression, le refoulement | u | ex=The regime was known for its brutal repression. # Le régime était connu pour sa répression brutale.
self-control | la maîtrise de soi
sequence | la succession, enchaînement
sincerity | la sincérité
stubbornness | l'entêtement | u | ex=His stubbornness drives me crazy. # Son entêtement me rend fou.
tenacity | la ténacité, opiniâtreté
train of thought | le cheminement de pensée
urgency | l'urgence
vigilance | la vigilance
way of thinking | le mode de pensée
willpower | la force de volonté
wishful thinking | le vœu pieux, pensée illusoire
""",
"society_c1": """
balance of power | l'équilibre des pouvoirs | u | ex=The election changed the balance of power in Congress. # L'élection a changé l'équilibre des pouvoirs au Congrès.
ballot | le bulletin de vote | gb=ballot paper
belonging | l'appartenance | u
division | la division, clivage
guiding principle | le modèle directeur, idéal affiché
lobbying | le lobbying
aging population | le vieillissement de la population | u | gb=ageing population | ex=An aging population puts pressure on the health system. # Le vieillissement de la population pèse sur le système de santé.
prosperity | la prospérité
taboo | le tabou
upheaval | le bouleversement
vote of confidence | la question de confiance
voter turnout | le taux de participation
""",
"law_c1": """
appeal | l'appel (recours)
arrest | l'arrestation
burden of proof | la charge de la preuve | pl=burden of proofs
case law | la jurisprudence
ceasefire | le cessez-le-feu
compensation | l'indemnisation | u
crime scene | le lieu du crime
deterrence | la dissuasion
disarmament | le désarmement
emergency services | les services d'urgence | plt
estate | la succession, le domaine
evacuation | l'évacuation | ex=The fire alarm led to the evacuation of the building. # L'alarme incendie a entraîné l'évacuation du bâtiment.
forensics | la police scientifique | u
investigation | l'enquête
liability | la responsabilité (juridique) | u
manhunt | la chasse à l'homme | ex=Police launched a manhunt for the escaped prisoner. # La police a lancé une chasse à l'homme pour retrouver le détenu évadé.
obligation | l'obligation, engagement
patrol car | la voiture de patrouille
peace treaty | le traité de paix
power of attorney | la procuration
precautionary measure | la mesure de précaution | ex=As a precautionary measure, the school was closed. # Par mesure de précaution, l'école a été fermée.
probation | la mise à l'épreuve, le sursis | u
probation officer | l'agent de probation
questioning | l'interrogatoire | u
search | la perquisition, la fouille
security flaw | la faille de sécurité
seizure | la saisie
statute of limitations | la prescription | u | ex=The statute of limitations for this crime is five years. # La prescription pour ce délit est de cinq ans.
threat | la menace
withdrawal | le retrait
witness protection | la protection des témoins
witness statement | le témoignage
""",
"ideas_c1": """
acceleration | l'accélération | u | ex=This car has impressive acceleration. # Cette voiture a une accélération impressionnante.
accusation | le reproche, accusation
approval | l'approbation, accord
arbitration | la conciliation, arbitrage
arrangement | l'arrangement, entente préalable
blessing | la bénédiction
charity | l'association caritative, la charité | ex=She gives money to charity every month. # Elle donne de l'argent à des œuvres caritatives tous les mois.
chronicle | la chronique
clergy | le clergé
cluster | le groupe, la grappe | ex=A cluster of houses stood near the river. # Un groupe de maisons se dressait près de la rivière.
compromise | le compromis
confession | la confession, l'aveu
conscience | la conscience (morale)
conviction | la conviction
devotion | le dévouement | u | ex=Her devotion to her patients is remarkable. # Son dévouement envers ses patients est remarquable.
double standard | le deux poids, deux mesures
downside | le revers, envers
driving force | la force motrice
equal treatment | l'égalité de traitement | u | ex=All employees are entitled to equal treatment. # Tous les employés ont droit à l'égalité de traitement.
escalation | l'exacerbation
expulsion | l'expulsion, déplacement forcé
extent | l'ampleur
feedback loop | la rétroaction
forced labor | le travail forcé | u
forgiveness | le pardon | u
friction | la friction, frottement
house of worship | l'édifice religieux
human dignity | la dignité humaine
hypocrisy | l'hypocrisie
impairment | l'altération, gêne
""",
"ideas_c1_2": """
insight | la compréhension, l'éclairage
insinuation | l'insinuation, procès d'intention
insistence | l'obstination, refus de céder
interaction | l'interaction réciproque
interplay | l'interaction, jeu combiné
justification | la justification
leverage | le moyen de pression | u | ex=We have no leverage in these negotiations. # Nous n'avons aucun moyen de pression dans ces négociations.
memorial | le mémorial (d'avertissement)
mercy | la miséricorde
occupation | l'occupation (militaire), la profession
piece of evidence | la pièce justificative, preuve | u
pilgrimage | le pèlerinage
point of contention | le point de désaccord
post-war period | l'après-guerre | ex=The city grew quickly in the post-war period. # La ville a grandi rapidement dans l'après-guerre.
pretext | le prétexte
provocation | la provocation
quid pro quo | la contrepartie | ex=There's no quid pro quo; I'm helping you for free. # Il n'y a pas de contrepartie ; je t'aide gratuitement.
reconstruction | la reconstruction
rejection | le refus, rejet
remembrance | la commémoration
reunification | la réunification
sense of duty | le sens du devoir
sense of justice | le sens de la justice | u
sense of responsibility | le sens des responsabilités
sermon | le sermon, prêche
side effect | l'effet secondaire
significance | la portée
stagnation | la stagnation
superstition | la superstition
""",
"ideas_c1_3": """
tolerance | la tolérance
trigger | le déclencheur
turnaround | le redressement, le revirement | ex=The new CEO achieved a remarkable turnaround. # Le nouveau PDG a réussi un redressement remarquable.
turning point | le tournant
ultimatum | l'ultimatum
upturn | l'essor, la reprise
viability | la viabilité | u
worldview | la conception du monde
""",
# Ajoutes a la main (27 oct. 2026) : le vocabulaire savant le plus courant
# de l'anglais C1, que nos corpus n'ont pas (ils viennent de l'allemand).
"academic_c1": """
abundance | l'abondance | u | ex=The region has an abundance of fresh seafood. # La région regorge de fruits de mer frais.
adversity | l'adversité | u | ex=She showed great courage in the face of adversity. # Elle a fait preuve d'un grand courage face à l'adversité.
anomaly | l'anomalie | ex=The scientists noticed an anomaly in the data. # Les scientifiques ont remarqué une anomalie dans les données.
aptitude | l'aptitude | ex=He has a natural aptitude for languages. # Il a un don naturel pour les langues.
autonomy | l'autonomie | u | ex=Teenagers want more autonomy. # Les adolescents veulent plus d'autonomie.
benchmark | le point de référence | ex=This test is the benchmark for the industry. # Ce test est la référence du secteur.
catalyst | le catalyseur | ex=The protest was a catalyst for change. # La manifestation a été un catalyseur du changement.
constraint | la contrainte | ex=We have to work within budget constraints. # Nous devons travailler avec des contraintes budgétaires.
contingency | l'imprévu, l'éventualité | pl=contingencies | ex=We have a plan for every contingency. # Nous avons un plan pour chaque éventualité.
deficiency | la carence | pl=deficiencies | ex=Vitamin D deficiency is common in winter. # La carence en vitamine D est fréquente en hiver.
dichotomy | la dichotomie | pl=dichotomies | ex=The book explores the dichotomy between city and country. # Le livre explore l'opposition entre ville et campagne.
discrepancy | l'écart, la divergence | pl=discrepancies | ex=There's a discrepancy between the two reports. # Il y a un écart entre les deux rapports.
disparity | la disparité | pl=disparities | ex=The disparity between rich and poor is growing. # L'écart entre riches et pauvres se creuse.
endeavor | l'entreprise, l'effort | gb=endeavour | ex=Starting a business is a risky endeavor. # Créer une entreprise est une aventure risquée.
entity | l'entité | pl=entities | ex=The two companies are separate legal entities. # Les deux sociétés sont des entités juridiques distinctes.
facet | la facette | ex=The book covers every facet of his life. # Le livre couvre toutes les facettes de sa vie.
hierarchy | la hiérarchie | pl=hierarchies | ex=The company has a strict hierarchy. # L'entreprise a une hiérarchie stricte.
impetus | l'élan, l'impulsion | u | ex=The new law gave impetus to the reforms. # La nouvelle loi a donné de l'élan aux réformes.
incentive | la motivation, l'incitation | ex=The bonus is an incentive to work harder. # La prime incite à travailler davantage.
inception | la création, les débuts | u | ex=She has worked here since its inception. # Elle travaille ici depuis sa création.
jurisdiction | la compétence (juridique) | u | ex=The case is outside the court's jurisdiction. # L'affaire ne relève pas de la compétence du tribunal.
juxtaposition | la juxtaposition | ex=The juxtaposition of old and new buildings is striking. # La juxtaposition de bâtiments anciens et modernes est frappante.
magnitude | l'ampleur | u | ex=Nobody understood the magnitude of the problem. # Personne n'a compris l'ampleur du problème.
mandate | le mandat | ex=The government has a mandate to reform taxes. # Le gouvernement a reçu mandat de réformer les impôts.
misconception | l'idée fausse | ex=It's a common misconception that bats are blind. # C'est une idée reçue de croire que les chauves-souris sont aveugles.
momentum | l'élan, la dynamique | u | ex=The campaign is gaining momentum. # La campagne prend de l'ampleur.
notion | la notion, l'idée | ex=I have no notion of what he means. # Je n'ai aucune idée de ce qu'il veut dire.
outcome | le résultat, l'issue | ex=We're waiting for the outcome of the election. # Nous attendons l'issue de l'élection.
outset | le début | u | ex=I told you at the outset that it would be difficult. # Je t'ai dit dès le début que ce serait difficile.
paradigm | le paradigme | ex=The discovery led to a paradigm shift. # La découverte a entraîné un changement de paradigme.
pitfall | le piège, l'écueil | ex=The guide explains the pitfalls of buying a house. # Le guide explique les pièges de l'achat d'une maison.
prevalence | la fréquence, la prévalence | u | ex=The prevalence of obesity has increased. # La prévalence de l'obésité a augmenté.
proponent | le, la partisan(e) | ex=She's a strong proponent of public transit. # C'est une fervente partisane des transports en commun.
proximity | la proximité | u | ex=The hotel's main advantage is its proximity to the beach. # Le principal avantage de l'hôtel, c'est sa proximité avec la plage.
rationale | la raison d'être, la justification | ex=What's the rationale behind this decision? # Quelle est la logique de cette décision ?
remnant | le vestige, le reste | ex=These walls are remnants of the old fort. # Ces murs sont des vestiges de l'ancien fort.
repercussion | la répercussion | ex=The scandal had serious repercussions. # Le scandale a eu de graves répercussions.
scrutiny | l'examen minutieux | u | ex=The plan came under close scrutiny. # Le projet a été examiné de près.
setback | le revers, le contretemps | ex=The injury was a major setback for the team. # La blessure a été un sérieux revers pour l'équipe.
spectrum | le spectre, l'éventail | pl=spectrums | ex=The party attracts voters across the political spectrum. # Le parti attire des électeurs de tout l'éventail politique.
stance | la position | ex=What's your stance on this issue? # Quelle est ta position sur cette question ?
stigma | la stigmatisation, l'opprobre | u | ex=There's still a stigma attached to mental illness. # Les maladies mentales restent stigmatisées.
surplus | l'excédent | ex=The city has a budget surplus this year. # La ville a un excédent budgétaire cette année.
threshold | le seuil | ex=We are on the threshold of a new era. # Nous sommes au seuil d'une nouvelle ère.
trajectory | la trajectoire | pl=trajectories | ex=Her career has followed an upward trajectory. # Sa carrière a suivi une trajectoire ascendante.
trait | le trait (de caractère) | ex=Patience is her best trait. # La patience est sa meilleure qualité.
venture | l'entreprise (risquée) | ex=The new venture failed after a year. # La nouvelle entreprise a échoué au bout d'un an.
verdict | le verdict | ex=The jury reached a verdict after two days. # Le jury a rendu son verdict au bout de deux jours.
caveat | la réserve, la mise en garde | ex=There's one caveat: the offer ends Friday. # Une réserve : l'offre se termine vendredi.
cornerstone | la pierre angulaire | ex=Trust is the cornerstone of any relationship. # La confiance est la pierre angulaire de toute relation.
drawback | l'inconvénient | ex=The main drawback is the price. # Le principal inconvénient, c'est le prix.
foresight | la clairvoyance, la prévoyance | u | ex=Thanks to her foresight, we had enough food. # Grâce à sa prévoyance, nous avions assez de nourriture.
hindsight | le recul | u | ex=With hindsight, it was a bad decision. # Avec le recul, c'était une mauvaise décision.
loophole | la faille (juridique) | ex=They found a loophole in the law. # Ils ont trouvé une faille dans la loi.
milestone | l'étape importante, le jalon | ex=Graduating was a major milestone. # Obtenir son diplôme a été une étape importante.
nuisance | la nuisance, le désagrément | ex=The noise is a real nuisance. # Le bruit est une vraie nuisance.
overview | la vue d'ensemble | ex=Here's a quick overview of the project. # Voici un bref aperçu du projet.
shortcoming | le défaut, la lacune | ex=The report points out several shortcomings. # Le rapport souligne plusieurs lacunes.
tradeoff | le compromis | ex=There's always a tradeoff between speed and quality. # Il y a toujours un compromis entre vitesse et qualité.
underdog | l'outsider | ex=Everyone loves to cheer for the underdog. # Tout le monde aime encourager l'outsider.
""",
}
