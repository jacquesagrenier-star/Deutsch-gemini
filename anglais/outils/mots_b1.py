# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du B1 anglais. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que mots_a1.py et phrases_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'B1'

# « verbe | traduction | drapeaux » ; les formes sont calculees (irreguliers.py).
VERBES = """
abandon | abandonner
abolish | supprimer
accompany | accompagner
accomplish | accomplir | ex=We accomplished a lot this week. # Nous avons accompli beaucoup de choses cette semaine.
accumulate | accumuler
acquire | acquérir
adapt | s'adapter, adapter
add up | additionner
address | s'adresser à, aborder
adjust | ajuster, régler | ex=You can adjust the seat. # Tu peux régler le siège.
admit | admettre
adopt | adopter (une loi, une décision)
advocate | défendre, prôner
agree | se mettre d'accord
agree on | convenir, s'accorder sur
alter | modifier
amuse | amuser
analyze | analyser | ex=Scientists analyzed the water samples. # Les scientifiques ont analysé les échantillons d'eau.
approach | s'approcher de, aborder
arrange | organiser, arranger
arrest | arrêter (police)
assemble | monter, assembler
assess | évaluer
assign | attribuer, assigner | ex=The teacher assigned us a lot of homework. # Le professeur nous a donné beaucoup de devoirs.
assist | aider, assister
assume | supposer
assure | assurer
attack | attaquer
attend | assister
attract | attirer
beat | battre
beg | supplier, mendier
bet | parier
bleed | saigner
bless | bénir
block | bloquer
bloom | fleurir
blow | souffler | ex=Blow out the candles! # Souffle les bougies !
brake | freiner
break in | entrer par effraction | ex=Someone broke in while we were away. # Quelqu'un est entré par effraction pendant notre absence.
break up | rompre
bring up | élever (un enfant), aborder (un sujet) | ex=She brought up three children on her own. # Elle a élevé trois enfants seule.
bump | cogner, heurter
care for | soigner, prendre soin de
carry out | réaliser, mettre en œuvre
catch a cold | attraper un rhume
catch up on | rattraper
cause | causer
chase | poursuivre
cheat | tromper, escroquer
check out | quitter l'hôtel (check-out)
claim | prétendre, affirmer
clarify | clarifier, tirer au clair
classify | classer | ex=The books are classified by subject. # Les livres sont classés par sujet.
click | cliquer
collaborate | collaborer
collapse | s'effondrer
collect | collectionner, collecter
come from | provenir, être originaire de
command | ordonner, commander | ex=The officer commanded them to stop. # L'officier leur a ordonné de s'arrêter.
commit | commettre, s'engager
communicate | communiquer, informer
comply with | respecter (une règle, un délai)
conclude | conclure, terminer
condemn | condamner | ex=Everyone condemned the attack. # Tout le monde a condamné l'attaque.
confess | avouer
confirm | confirmer
conquer | conquérir
consider | considérer
consist of | se composer de
console | consoler
consult | consulter
contribute | contribuer
control | contrôler
convict | condamner (en justice) | ex=He was convicted of theft. # Il a été condamné pour vol.
convince | convaincre
cool down | refroidir, se calmer
coordinate | coordonner
copy | copier, photocopier
damage | endommager
deal with | s'occuper de, gérer
deceive | tromper | ex=He deceived everyone about his past. # Il a trompé tout le monde sur son passé.
decorate | décorer
decrease | diminuer
defeat | vaincre | ex=The Red Sox defeated the Yankees. # Les Red Sox ont battu les Yankees.
defend | défendre
define | définir
delegate | déléguer
delve into | approfondir
demolish | démolir
demonstrate | démontrer, prouver
deny | nier
depend on | dépendre de
depict | représenter
deploy | déployer
describe | décrire
deserve | mériter
destroy | détruire
detain | retenir, détenir
devote | consacrer
digest | digérer
disappear | disparaître
disappoint | décevoir
discriminate | discriminer | ex=It's illegal to discriminate against job applicants. # Il est illégal de discriminer les candidats à un emploi.
dispose of | éliminer, jeter (des déchets)
disregard | ignorer, ne pas respecter
dissolve | dissoudre
distinguish | distinguer
distribute | distribuer, répartir
disturb | déranger
dive | plonger
divide | diviser
divorce | divorcer
document | documenter
donate | faire un don
doubt | douter de
drag | traîner
drown | se noyer
dump | jeter, déverser
edit | modifier, corriger
email | envoyer un courriel
emigrate | émigrer
emphasize | souligner
employ | employer, embaucher
endanger | mettre en danger
enlarge | agrandir
estimate | estimer
evaluate | évaluer | ex=The teacher evaluates our progress every month. # Le professeur évalue nos progrès chaque mois.
exaggerate | exagérer
exchange | échanger
exclude | exclure
exhaust | épuiser
expand | élargir, agrandir
experience | vivre, connaître
experiment | expérimenter
explode | exploser
explore | explorer
export | exporter
express | exprimer
extend | étendre
fall | tomber
fight | lutter, combattre
fill up | faire le plein
finance | financer
fine | mettre une amende à
flow | couler
force | forcer, obliger
forecast | prévoir
forgive | pardonner
found | fonder
frustrate | frustrer
fulfill | remplir, réaliser | ex=She finally fulfilled her dream. # Elle a enfin réalisé son rêve.
fund | financer
furnish | meubler | ex=They furnished the apartment with secondhand furniture. # Ils ont meublé l'appartement avec des meubles d'occasion.
gather | réunir
generate | produire
get around | se déplacer
get into debt | s'endetter | ex=Many students get into debt to pay for college. # Beaucoup d'étudiants s'endettent pour payer l'université.
get involved | s'engager, s'impliquer | ex=I'd like to get involved in the neighborhood association. # J'aimerais m'impliquer dans l'association du quartier.
get upset | se fâcher, être contrarié | ex=Don't get upset, it's only a game. # Ne te fâche pas, ce n'est qu'un jeu.
give back | rendre | ex=Can you give me back my pen? # Tu peux me rendre mon stylo ?
glue | coller
go bankrupt | faire faillite
govern | gouverner
grab | attraper
grasp | saisir, comprendre
guarantee | garantir
guess | deviner
guide | guider
hand out | distribuer
handle | gérer, manier | ex=She handles stress very well. # Elle gère très bien le stress.
harvest | récolter
heal | guérir
hesitate | hésiter
hide | cacher
hint at | suggérer, laisser entendre
hit | frapper
honk | klaxonner
hug | prendre dans ses bras
identify | identifier
ignore | ignorer
implement | mettre en œuvre
imply | impliquer
import | importer
impose | imposer
improvise | improviser
indicate | indiquer
infect | contaminer
inquire | se renseigner
insert | introduire
insist | insister
inspire | inspirer
insulate | isoler
insult | insulter
insure | assurer
integrate | intégrer
intend | avoir l'intention de
interrupt | interrompre
investigate | enquêter | ex=The police are investigating the robbery. # La police enquête sur le cambriolage.
join | rejoindre, adhérer à
jot down | noter
justify | justifier
kill | tuer
knock | frapper (à la porte)
lie down | s'allonger ; se calmer (vent, colère)
light | allumer
limit | limiter
look up | chercher (un mot) | ex=Look up the word in the dictionary. # Cherche le mot dans le dictionnaire.
lose weight | maigrir, perdre du poids
maintain | entretenir, maintenir
make an effort | s'efforcer
make fun of | se moquer de
market | commercialiser
massage | masser
master | maîtriser
melt | faire fondre
merge | fusionner
misunderstand | mal comprendre
mix up | confondre
mock | se moquer de
motivate | motiver
move in | emménager | ex=We moved in last week. # Nous avons emménagé la semaine dernière.
neglect | négliger
negotiate | négocier
notify | avertir, notifier
obey | obéir
obtain | obtenir
occupy | occuper | ex=The children were occupied with their games. # Les enfants étaient occupés par leurs jeux.
occur | arriver, se produire
offend | offenser, insulter
offer | offrir, proposer
operate | opérer
oppose | s'opposer à
overcome | surmonter
overlook | ne pas remarquer, donner sur
participate | participer
pass on | transmettre | ex=Could you pass on the message to your boss? # Tu pourrais transmettre le message à ton patron ?
perceive | percevoir
persuade | persuader
praise | louer, féliciter
pray | prier
present | présenter
preserve | conserver
pretend | faire semblant
prevent | empêcher
print out | imprimer
process | traiter, transformer
produce | produire, générer
program | programmer | ex=She programmed the oven to start at six. # Elle a programmé le four pour qu'il démarre à six heures.
promise | promettre
pronounce | prononcer
propose | proposer
protest | protester
prove | prouver
provide | fournir
provoke | provoquer | ex=His comment provoked an angry reaction. # Son commentaire a provoqué une réaction de colère.
pull out | arracher, retirer | ex=The dentist pulled out my tooth. # Le dentiste m'a arraché la dent.
pump up | gonfler
punish | punir
purchase | acheter
put back | remettre (à sa place) | ex=Put the milk back in the fridge. # Remets le lait au frigo.
put down | poser | ex=Put down your bags and sit down. # Pose tes sacs et assieds-toi.
put on weight | prendre du poids
qualify | se qualifier
question | remettre en question
quote | citer
read aloud | lire à voix haute
realize | se rendre compte, réaliser
rebel | se révolter
reflect | réfléchir
refute | réfuter
regulate | régler, organiser
reimburse | rembourser (des frais)
reject | refuser
relate | relier, s'identifier à | ex=I can relate to what you're saying. # Je comprends tout à fait ce que tu dis.
relieve | soulager
rely on | compter sur
renew | renouveler
repay | rembourser | ex=I'll repay you next week. # Je te rembourserai la semaine prochaine.
represent | représenter
reprimand | réprimander
reproach | reprocher
require | exiger, nécessiter
resign | démissionner
resist | résister | ex=I couldn't resist the chocolate cake. # Je n'ai pas pu résister au gâteau au chocolat.
respect | respecter
restore | restaurer, rétablir
result in | entraîner, aboutir à
reveal | révéler | ex=She revealed the secret to her sister. # Elle a révélé le secret à sa sœur.
reward | récompenser
ring | sonner
rise | monter, se lever
risk | risquer
run over | écraser (en voiture) | ex=The driver almost ran over a cat. # Le conducteur a failli écraser un chat.
select | sélectionner, choisir
set off | partir, démarrer
set up | installer, créer | ex=They set up a small company in 2020. # Ils ont créé une petite entreprise en 2020.
settle | s'installer, régler
shake | secouer
shatter | se briser, briser | ex=The glass shattered on the floor. # Le verre s'est brisé par terre.
shine | briller
simplify | simplifier
sow | semer
spare | épargner
speculate | spéculer
sponsor | parrainer
spread | diffuser, répandre
stagnate | stagner
stand out | se démarquer
starve | mourir de faim
step | marcher (sur)
stick to | s'en tenir à, respecter
sting | piquer
stink | puer | ex=The garbage stinks. # Les poubelles puent.
store | stocker, ranger
strengthen | renforcer
strike | frapper, faire grève
stroll | se promener
submit | déposer, soumettre (un dossier)
subscribe to | s'abonner à
suffer | souffrir
suffocate | étouffer
suggest | proposer
summarize | résumer
supervise | superviser
supply | approvisionner
suppose | supposer | ex=I suppose you're right. # Je suppose que tu as raison.
surround | entourer
swear | jurer
sweat | transpirer
switch | changer, passer | ex=Let's switch seats. # Changeons de place.
take in | accueillir, comprendre
take part in | participer à
take time off | prendre congé | ex=I'm taking some time off next month. # Je prends quelques jours de congé le mois prochain.
tear | déchirer, arracher
tease | taquiner
tell apart | distinguer | ex=I can't tell the twins apart. # Je n'arrive pas à distinguer les jumeaux.
testify | témoigner
threaten | menacer
tie | attacher
transfer | transférer, virer | ex=I transferred the money to your account. # J'ai viré l'argent sur ton compte.
transport | transporter
trigger | déclencher
turn around | se retourner, faire demi-tour | ex=Turn around at the next light. # Fais demi-tour au prochain feu.
turn into | se transformer en | ex=The caterpillar turned into a butterfly. # La chenille s'est transformée en papillon.
turn out | s'avérer
turn up | arriver, monter (le son)
type | taper (au clavier)
undo | défaire
update | mettre à jour
vaccinate | vacciner | ex=All the children were vaccinated. # Tous les enfants ont été vaccinés.
value | apprécier, évaluer
violate | enfreindre, violer
vote | voter
wave | faire signe de la main
weaken | affaiblir
weigh | peser
witness | être témoin de
work out | s'entraîner, marcher, trouver
worsen | aggraver
wrap | enrouler, emballer
state | déclarer, indiquer
affect | affecter, avoir un effet sur | ex=The weather affects my mood. # Le temps influe sur mon humeur.
find one's way | s'orienter, trouver son chemin | ex=I found my way without a map. # J'ai trouvé mon chemin sans carte.
fail | échouer
brood | ruminer | ex=Stop brooding and talk to him. # Arrête de ruminer et parle-lui.
take to heart | prendre à cœur | ex=She took his advice to heart. # Elle a pris son conseil à cœur.
play dice | jouer aux dés | ex=The kids played dice all evening. # Les enfants ont joué aux dés toute la soirée.
draw lots | tirer au sort
greet | saluer
X-ray | radiographier, faire une radio
wish for | souhaiter | ex=What did you wish for on your birthday? # Qu'est-ce que tu as souhaité pour ton anniversaire ?
afford | se permettre (financièrement) | ex=We can't afford a new car. # Nous n'avons pas les moyens d'acheter une nouvelle voiture.
go on a trip | partir en voyage
do the dishes | faire la vaisselle | ex=I'll cook if you do the dishes. # Je cuisine si tu fais la vaisselle.
stay together | rester ensemble
come to mind | venir à l'esprit
know one's way around | s'y connaître, se repérer | ex=He knows his way around Boston. # Il connaît bien Boston.
keep to oneself | rester dans son coin | ex=Our neighbor keeps to himself. # Notre voisin reste dans son coin.
naturalize | naturaliser
think over | réfléchir à qch
get along with | bien s'entendre avec | ex=Do you get along with your boss? # Tu t'entends bien avec ton patron ?
write down | noter, écrire
hinder | gêner, entraver | ex=The snow hindered the rescue efforts. # La neige a gêné les secours.
do odd jobs | faire des petits boulots | ex=He did odd jobs to pay for college. # Il a fait des petits boulots pour payer ses études.
stay overnight | passer la nuit, loger
serve | servir (à)
laze around | paresser | ex=On Sundays I just laze around. # Le dimanche, je paresse.
google | chercher sur Internet
put on makeup | se maquiller | ex=She puts on makeup before work. # Elle se maquille avant d'aller travailler.
tweet | publier sur les réseaux
buckle up | attacher sa ceinture | ex=Buckle up, we're leaving. # Attache ta ceinture, on part.
shave | raser
"""

# « adjectif | traduction | drapeaux » (gb=, ex=).
ADJECTIFS = """
absent | absent
absolute | absolu
accessible | accessible
acclaimed | acclamé
active | actif
adaptable | adaptable
adapted | adapté | ex=The movie was adapted from a novel. # Le film a été adapté d'un roman.
addicted | dépendant, accro
addictive | addictif
additional | supplémentaire
advanced | avancé
affordable | abordable
agricultural | agricole
allergic | allergique (à qch)
alternative | alternatif, autre
altruistic | altruiste
ambitious | ambitieux
ancient | ancien
annoying | agaçant
annual | annuel
anonymous | anonyme
anxious | anxieux, inquiet
approachable | accessible, abordable | ex=Our new boss is very approachable. # Notre nouvelle patronne est très accessible.
appropriate | approprié
approximate | approximatif
arid | aride
arrogant | arrogant
average | moyen
aware | conscient
balanced | équilibré
basic | basique
beneficial | bénéfique
big-hearted | généreux, au grand cœur
bilingual | bilingue
bland | fade
blind | aveugle
bored | qui s'ennuie
brilliant | génial
Catholic | catholique
certain | certain | ex=Are you certain about that? # Tu en es certain ?
chaotic | chaotique
chronic | chronique
civil | civil
classic | classique
close | proche
clumsy | maladroit
collective | collectif
committed | engagé, impliqué
common | commun
compassionate | compatissant | ex=She's a compassionate nurse. # C'est une infirmière pleine de compassion.
competent | compétent
competitive | compétitif
complete | complet, entier
complex | complexe
compulsory | obligatoire
conceited | prétentieux
confused | confus
confusing | confus
congested | encombré
conservative | conservateur
considerate | attentionné, prévenant
constant | constant
contagious | contagieux
contemporary | contemporain
continuous | continu
convinced | convaincu
convincing | convaincant
cosmetic | cosmétique
costly | coûteux
creative | créatif
critical | critique
cultural | culturel
deadly | mortel | ex=The storm was deadly. # La tempête a été meurtrière.
deaf | sourd
decisive | décisif
delicate | délicat
democratic | démocratique
desirable | souhaitable
desperate | désespéré | ex=He was desperate to find a job. # Il cherchait désespérément un emploi.
dignified | digne
diplomatic | diplomate
disabled | handicapé
disappointed | déçu
disappointing | décevant
disciplined | discipliné
disobedient | désobéissant
dissatisfied | insatisfait
distracted | distrait
diverse | divers
doubtful | douteux
dreadful | épouvantable
drunk | ivre, saoul
due | dû, à échéance
eager | impatient, désireux
ecological | écologique
educational | éducatif
electric | électrique
electronic | électronique | ex=Turn off all electronic devices. # Éteignez tous les appareils électroniques.
embarrassing | embarrassant, gênant
emotional | émotif
empathetic | empathique
emphatic | catégorique
English-speaking | anglophone | ex=Canada has English-speaking and French-speaking provinces. # Le Canada a des provinces anglophones et francophones.
enthusiastic | enthousiaste | ex=The students were very enthusiastic about the trip. # Les élèves étaient très enthousiastes à l'idée du voyage.
entitled | en droit de
envious | envieux
equal | égal
essential | essentiel
eternal | éternel | ex=Rome is called the Eternal City. # Rome est appelée la Ville éternelle.
even | plat, régulier | ex=The floor isn't even. # Le sol n'est pas plat.
everyday | quotidien, banal
exact | exact
excellent | excellent
exotic | exotique
expected | prévu, attendu
experienced | expérimenté
explicit | explicite
external | externe, extérieur
extra | supplémentaire
extreme | extrême
eye-catching | voyant, accrocheur
fair | juste, équitable
false | faux
fantastic | fantastique
fascinating | fascinant
fatal | mortel, fatal
favorable | favorable | ex=The weather is favorable for sailing. # Le temps est favorable à la voile.
fearful | craintif, anxieux
fearless | sans peur, intrépide | ex=The little girl is fearless on her bike. # La petite fille n'a peur de rien sur son vélo.
female | féminin, de sexe féminin
fertile | fertile
financial | financier
fit | en forme
fixed | fixe, ferme
fixed-term | à durée déterminée | ex=She has a fixed-term contract. # Elle a un contrat à durée déterminée.
fluent | courant (langue)
focused | concentré
following | suivant
formal | formel
former | ancien (précédent)
frequent | fréquent
fundamental | fondamental
further | autre, supplémentaire
future | futur
general | général
genuine | authentique
gifted | doué
gorgeous | magnifique
Gothic | gothique
grateful | reconnaissant
gross | brut
guilty | coupable
half | demi
harmful | nocif
helpful | serviable
hidden | caché
higher | supérieur
historic | historique
historical | historique
homemade | fait maison
hopeful | plein d'espoir | ex=We're hopeful that he'll recover. # Nous avons bon espoir qu'il se rétablisse.
hopeless | sans espoir
horizontal | horizontal | ex=Draw a horizontal line. # Trace une ligne horizontale.
horrible | horrible
human | humain
humorous | plein d'humour
ideal | idéal
idealistic | idéaliste
identical | identique
illegal | illégal
illogical | illogique
immediate | immédiat
impatient | impatient
impressive | impressionnant
inattentive | inattentif
inclusive | inclusif
incompetent | incompétent
incredible | incroyable
independent | autonome
indifferent | indifférent
indirect | indirect
individual | individuel
industrial | industriel
inexperienced | inexpérimenté
inferior | inférieur | ex=This copy is inferior to the original. # Cette copie est inférieure à l'original.
infinite | infini
informal | informel
inner | intérieur
innocent | innocent
instant | immédiat, sur le moment
insufficient | insuffisant
intensive | intensif, intense
intercultural | interculturel
intermediate | intermédiaire
international | international
intolerant | intolérant
leading | de premier plan, principal
legal | légal
liberal | libéral
limited | limité
literary | littéraire
live | en direct
local | local
logical | logique
long-lasting | durable
lukewarm | tiède
luxurious | luxueux
magnificent | magnifique
majestic | majestueux
manual | manuel
medical | médical
medieval | médiéval
mental | mental
misleading | trompeur
modest | modeste
monthly | mensuel
motivated | motivé
mountainous | montagneux
multilingual | plurilingue
municipal | municipal, urbain
muscular | musclé, musculaire | ex=He has strong, muscular arms. # Il a des bras forts et musclés.
mutual | mutuel
mysterious | mystérieux
naked | nu | ex=You can't see that with the naked eye. # On ne peut pas voir ça à l'œil nu.
national | national
negative | négatif
northern | du nord | ex=Maine is in the northern part of New England. # Le Maine est dans le nord de la Nouvelle-Angleterre.
nuclear | nucléaire
obedient | obéissant
obliged | tenu, obligé
odd | bizarre, rare
official | officiel
opposite | contraire
optimistic | optimiste
oral | oral
ordinary | ordinaire, courant
organic | biologique
organized | organisé
original | original, d'origine
oval | ovale
pale | pâle
parallel | parallèle
passionate | passionné | ex=He's passionate about jazz. # Il est passionné de jazz.
passive | passif
peaceful | pacifique
pedestrian | piétonnier
perfect | parfait
personal | personnel
pessimistic | pessimiste
petty | mesquin, tatillon
physical | physique, corporel
picturesque | pittoresque
plentiful | abondant
pointless | inutile, absurde
poisonous | toxique, vénéneux
political | politique
polluting | polluant
positive | positif
powerful | puissant
preferable | préférable
present | présent
preventive | préventif
professional | professionnel
progressive | progressiste
Protestant | protestant
public | public
punishable | punissable, répréhensible
pure | pur
qualified | qualifié
rational | rationnel
realistic | réaliste
reasonable | raisonnable
rebellious | rebelle
recent | récent
related | apparenté, lié
relative | relatif
relaxed | détendu
relevant | pertinent
reliable | fiable
remaining | restant | ex=Eat the remaining pizza before it gets cold. # Mange le reste de la pizza avant qu'elle refroidisse.
remarkable | notable
remote | reculé
responsible | responsable
retired | à la retraite
ripe | mûr
risky | risqué
rural | rural
sacred | sacré
satisfactory | satisfaisant
satisfied | satisfait
scientific | scientifique
seasonal | saisonnier
secret | secret
secular | laïque
self-assured | sûr de soi
self-evident | évident, bien entendu
selfless | désintéressé
sensible | sensé, raisonnable (faux ami : sensible = sensitive)
sensitive | sensible
severe | sévère
shared | partagé
sharp | pointu, tranchant, vif
significant | significatif
silly | bête
similar | semblable, similaire
single-parent | monoparental | ex=She grew up in a single-parent family. # Elle a grandi dans une famille monoparentale.
skilled | qualifié
social | social
societal | social, sociétal
solar | solaire
solid | solide
solvent | solvable
southern | du sud | ex=Florida is in the southern United States. # La Floride est dans le sud des États-Unis.
special | spécial
specific | précis, spécifique
spontaneous | spontané
square | carré
stable | stable
steep | raide, escarpé
still | immobile, calme
stingy | avare
stressed | stressé
stylistic | stylistique
successful | qui réussit, à succès
suitable | approprié, adapté
superficial | superficiel
supportive | solidaire
surprised | surpris
surprising | surprenant
suspicious | méfiant
sustainable | durable
swift | rapide
tactful | plein de tact | ex=Try to be tactful when you tell her. # Essaie d'avoir du tact quand tu le lui diras.
tactless | sans tact
talented | talentueux
technical | technique
temporary | temporaire
tense | tendu
thrifty | économe | ex=My grandmother was very thrifty. # Ma grand-mère était très économe.
tolerant | tolérant
total | total, entier
traditional | traditionnel
trained | formé, qualifié
transparent | transparent
unbeaten | invaincu
undecided | indécis | ex=Many voters are still undecided. # Beaucoup d'électeurs sont encore indécis.
understandable | compréhensible
undisciplined | indiscipliné
unequal | inégal
unexpected | inattendu
unfair | injuste
unfaithful | infidèle
unforgettable | inoubliable
unhealthy | malsain, mauvais pour la santé
uniform | uniforme, homogène
unknown | inconnu
unnecessary | inutile
unpredictable | imprévisible
unreasonable | déraisonnable
unreliable | peu fiable
unsuccessful | sans succès, raté
urban | urbain
valid | valable, valide
valuable | précieux
vegetarian | végétarien
vertical | vertical
violent | violent
violet | violet
viral | viral
virtual | virtuel
visible | visible
vital | vital
voluntary | bénévole
vulnerable | vulnérable
well-known | connu
whole | entier
whole wheat | complet (pain) | gb=wholemeal | ex=I prefer whole wheat bread. # Je préfère le pain complet.
widowed | veuf, veuve
wise | sage
withdrawn | renfermé, réservé
worldwide | mondial, dans le monde entier
worried | inquiet
worthless | sans valeur
written | écrit
yearly | annuel
youthful | juvénile, jeune
simultaneous | simultané | ex=The meeting has simultaneous translation. # La réunion bénéficie d'une traduction simultanée.
above-average | au-dessus de la moyenne
musical | musical, doué pour la musique | ex=The whole family is very musical. # Toute la famille est très musicale.
crooked | de travers, penché
cheerful | joyeux, gai
statistical | statistique | ex=There's no statistical difference between the groups. # Il n'y a pas de différence statistique entre les groupes.
damp | humide
other | autre, divers
mobile | mobile | ex=Mobile apps make banking easy. # Les applications mobiles facilitent les opérations bancaires.
"""

# « adverbe | traduction | categorie | drapeaux ».
ADVERBES = """
completely | complètement | Quantité
absolutely | absolument | Quantité
accordingly | en conséquence | Cause et conséquence
across | en travers | Lieu
admittedly | certes | Nuance
apart | séparément, l'un de l'autre | Lieu
apparently | apparemment | Liaison
at first | dans un premier temps | Temps
at last | enfin | Temps
at length | longuement | Temps
at night | la nuit | Temps
at noon | à midi | Temps
at present | actuellement (soutenu) | Temps
attentively | attentivement | Manière
automatically | automatiquement | Manière
backwards | en arrière | Lieu
barely | tout juste | Quantité
briefly | brièvement | Manière
by contrast | en revanche | Liaison | ex=The city is noisy. By contrast, the village is very quiet. # La ville est bruyante. En revanche, le village est très calme.
by mistake | par mégarde | Manière
by now | maintenant, déjà | Temps
commonly | communément | Fréquence
consequently | par conséquent | Cause et conséquence
considerably | considérablement | Quantité
deeply | profondément | Manière
deliberately | exprès | Manière
directly | directement | Manière
each time | chaque fois | Fréquence | ex=Each time I call, she's busy. # Chaque fois que j'appelle, elle est occupée.
easily | facilement | Manière
enormously | énormément | Quantité
entirely | entièrement | Quantité
ever | un jour, déjà (question) | Temps
excessively | excessivement | Quantité
exclusively | exclusivement | Quantité
explicitly | expressément | Manière
extremely | extrêmement | Quantité
firstly | premièrement | Liaison
for nothing | pour rien, gratuitement | Nuance
formally | formellement | Manière
freely | librement | Manière
fully | pleinement | Quantité
harshly | durement | Manière
highly | hautement | Quantité
how come | comment ça se fait | Question
however | cependant, toutefois | Liaison
in detail | en détail | Manière
in particular | en particulier | Liaison
in total | au total | Quantité
in turn | à tour de rôle, à son tour | Liaison | ex=The students answered in turn. # Les élèves ont répondu à tour de rôle.
indeed | effectivement | Affirmation
independently | de façon autonome | Manière
intensely | intensément | Manière
largely | en grande partie | Quantité
last | en dernier | Temps
legally | légalement | Manière
like this | comme ça | Manière | ex=Hold the pen like this. # Tiens le stylo comme ça.
likewise | également | Liaison
locally | localement | Lieu
merely | simplement | Quantité
moreover | de surcroît | Liaison
mostly | principalement | Quantité
namely | à savoir, en effet | Liaison
naturally | naturellement | Manière
nonetheless | néanmoins | Cause et conséquence
not yet | pas encore | Temps
notably | notablement | Quantité
nowhere | nulle part | Lieu
obviously | évidemment | Affirmation
officially | officiellement | Liaison
on purpose | exprès | Manière
on time | à temps | Temps
once again | encore une fois | Fréquence
openly | ouvertement | Manière
part-time | à temps partiel | Temps
partly | en partie | Quantité
patiently | patiemment | Manière
perfectly | parfaitement | Manière
perhaps | peut-être | Doute
plenty | largement, en abondance | Quantité
practically | pratiquement | Quantité
predominantly | majoritairement | Quantité
probably | probablement | Doute
purely | purement | Manière | ex=We met purely by chance. # Nous nous sommes rencontrés tout à fait par hasard.
radically | radicalement | Manière
rapidly | rapidement | Manière
reasonably | raisonnablement, assez | Quantité
rigorously | rigoureusement | Manière
secondly | deuxièmement | Liaison
secretly | en cachette | Manière
seriously | sérieusement, gravement | Manière
several times | à plusieurs reprises | Fréquence
shortly | bientôt, sous peu | Temps
sideways | de côté | Lieu | ex=The crab walks sideways. # Le crabe marche de côté.
simply | tout simplement | Manière
since then | depuis lors | Temps
sincerely | sincèrement | Manière | ex=I sincerely hope you get better soon. # J'espère sincèrement que tu iras vite mieux.
slightly | légèrement | Quantité
smoothly | sans accroc | Manière
solely | uniquement | Quantité
sometime | un jour ou l'autre | Temps | ex=Let's have lunch sometime next week. # Déjeunons ensemble un jour la semaine prochaine.
spontaneously | spontanément | Manière
strictly | strictement | Manière
strongly | fortement | Manière
sufficiently | suffisamment | Quantité
supposedly | prétendument | Doute
surprisingly | de façon surprenante | Manière
swiftly | rapidement, sans traîner | Manière
therefore | par conséquent | Liaison
thirdly | troisièmement | Liaison
this time | cette fois-ci | Temps
thoroughly | à fond | Manière
thus | ainsi, de ce fait | Cause et conséquence
truly | véritablement | Affirmation
undoubtedly | indubitablement | Affirmation
unfairly | injustement | Manière
urgently | d'urgence | Temps
visibly | visiblement | Manière
widely | largement | Manière
fairly | assez, plutôt | Quantité | ex=The test was fairly easy. # L'examen était assez facile.
hardly ever | presque jamais | Fréquence | ex=We hardly ever eat out. # Nous ne mangeons presque jamais au restaurant.
meanwhile | pendant ce temps | Temps | ex=I'll cook. Meanwhile, you can set the table. # Je cuisine. Pendant ce temps, tu peux mettre la table.
afterwards | ensuite, après | Temps | ex=We had dinner and went for a walk afterwards. # Nous avons dîné, puis nous sommes allés nous promener.
nearly | presque | Quantité | ex=It's nearly midnight. # Il est presque minuit.
a little while ago | tout à l'heure (passé) | Temps
in the future | à l'avenir | Temps | ex=In the future, please call before you come. # À l'avenir, appelle avant de venir.
in the end | finalement | Temps
at any time | à tout moment | Temps
in the morning | le matin | Temps
for weeks | pendant des semaines | Temps
for years | pendant des années | Temps
all the time | sans arrêt | Fréquence
again and again | sans cesse, à répétition | Fréquence
without any problems | sans problème | Manière | ex=The surgery went without any problems. # L'opération s'est déroulée sans problème.
substantially | nettement, considérablement | Quantité | ex=Prices have risen substantially. # Les prix ont nettement augmenté.
as a result | en conséquence de quoi | Cause et conséquence
apart from that | à part ça, sinon | Cause et conséquence
if need be | au besoin | Cause et conséquence
at any rate | du moins | Liaison
on the other hand | en revanche | Liaison
including | y compris | Quantité | ex=Ten people came, including my parents. # Dix personnes sont venues, y compris mes parents.
as far as i'm concerned | pour moi, si tu veux | Nuance
with each other | ensemble, l'un avec l'autre | Manière
at the latest | au plus tard | Temps
in the middle | au milieu | Lieu
by the way | au fait, d'ailleurs | Nuance
"""

# « expression | traduction | categorie | exemple anglais | exemple francais ».
EXPRESSIONS = """
All the best | Tous mes vœux | Bavarder | All the best for your new job! | Tous mes vœux pour ton nouveau travail !
among other things | entre autres | Discuter | We talked about the costs, among other things. | Nous avons parlé entre autres des coûts.
apart from | mis à part | Discuter | Apart from the price, everything is perfect. | Mis à part le prix, tout est parfait.
as a rule | en règle générale | Discuter | As a rule that takes two weeks. | En règle générale, cela prend deux semaines.
at first sight | à première vue | Discuter | At first sight the apartment seems small. | À première vue, l'appartement paraît petit.
at one's own expense | à ses propres frais | Au quotidien | She travelled at her own expense. | Elle a voyagé à ses propres frais.
Be that as it may | Quoi qu'il en soit | Discuter | Be that as it may, we have to carry on. | Quoi qu'il en soit, nous devons continuer.
by accident | par inadvertance | Au quotidien | I pressed the wrong key by accident. | J'ai appuyé par inadvertance sur la mauvaise touche.
by and large | dans l'ensemble | Discuter | By and large I'm satisfied. | Dans l'ensemble, je suis satisfait.
compared to | par rapport à | Discuter | Compared to yesterday it's cold. | Par rapport à hier, il fait froid.
from my point of view | de mon point de vue | Réagir | From my point of view, information is missing. | De mon point de vue, il manque des informations.
good to see you | content de te voir | Bavarder | Good to see you, do sit down! | Content de te voir, assieds-toi donc !
I agree with you | je suis d'accord avec toi | Réagir | I agree with you on that. | Je suis d'accord avec toi là-dessus.
I can imagine | Je m'en doute | Donner son avis | The move was exhausting. – I can imagine. | Le déménagement était fatigant. – Je m'en doute.
I can't believe it | je n'en reviens pas | Réagir | He won? I can't believe it! | Il a gagné ? Je n'en reviens pas !
I don't think so | je ne pense pas | Réagir | Is it going to rain? — I don't think so. | Il va pleuvoir ? — Je ne pense pas.
I doubt that | je doute que | Donner son avis | I doubt that he'll arrive on time. | Je doute qu'il arrive à l'heure.
I see it the same way | je vois les choses de la même façon | Donner son avis | I see it exactly the same way as you. | Je vois les choses exactement comme toi.
I'll be in touch | je te fais signe | Bavarder | I'll be in touch as soon as I know more. | Je te fais signe dès que j'en sais plus.
I'm against it | je suis contre | Donner son avis | I'm against it, that's too risky. | Je suis contre, c'est trop risqué.
I'm convinced | je suis convaincu | Donner son avis | I'm convinced it will work. | Je suis convaincu que ça va marcher.
I'm in favor | je suis pour | Donner son avis | I'm in favor of starting earlier. | Je suis pour qu'on commence plus tôt.
in a way | d'une certaine manière | Discuter | In a way you're right. | D'une certaine manière, tu as raison.
in other words | autrement dit | Discuter | In other words: we're starting over. | Autrement dit : nous recommençons depuis le début.
in private | en tête-à-tête | Au quotidien | Can we discuss this in private? | Pouvons-nous en parler en tête-à-tête ?
in the long term | à long terme | Au quotidien | In the long term it works out cheaper. | À long terme, ça revient moins cher.
it makes no sense | ça n'a pas de sens | Réagir | This paragraph makes no sense. | Ce paragraphe n'a pas de sens.
it's worth a try | ça vaut la peine d'essayer | Réagir | It's worth a try one more time. | Ça vaut la peine d'essayer encore une fois.
keep in touch | donne de tes nouvelles | Bavarder | Take care and keep in touch! | Porte-toi bien et donne de tes nouvelles !
little by little | peu à peu | Discuter | Little by little I understand more. | Peu à peu, je comprends davantage.
not least | notamment | Discuter | Not least because of the weather, we stayed home. | Notamment à cause du temps, nous sommes restés à la maison.
on the contrary | au contraire | Discuter | It wasn't boring, on the contrary! | Ce n'était pas ennuyeux, au contraire !
on the way | en chemin | Au quotidien | I'm already on the way to you. | Je suis déjà en chemin vers chez toi.
put differently | autrement dit | Discuter | Put differently: we have to save. | Autrement dit : nous devons économiser.
see you around | on se reverra | Bavarder | Bye, see you around! | Salut, on se reverra !
straight away | tout de suite | Discuter | She solved the problem straight away. | Elle a résolu le problème tout de suite.
strictly speaking | à proprement parler | Discuter | Strictly speaking that isn't allowed. | À proprement parler, ce n'est pas autorisé.
that is to say | c'est-à-dire | Discuter | He's an early retiree, that is to say he no longer works. | Il est préretraité, c'est-à-dire qu'il ne travaille plus.
that makes sense to me | ça me paraît logique | Donner son avis | Your explanation makes sense to me. | Ton explication me paraît logique.
that's beyond question | cela ne fait aucun doute | Donner son avis | His competence is beyond question. | Sa compétence ne fait aucun doute.
that's debatable | c'est discutable | Donner son avis | Whether that's nicer is debatable. | Que ce soit plus beau, c'est discutable.
that's fine by me | ça me va | Réagir | Meeting at seven is fine by me. | Ça me va de se voir à sept heures.
the pros and cons | le pour et le contre | Discuter | We weighed the pros and cons. | Nous avons pesé le pour et le contre.
there's a lot to be said for it | il y a de bonnes raisons | Donner son avis | There's a lot to be said for acting now. | Il y a de bonnes raisons d'agir maintenant.
throughout the year | tout au long de l'année | Au quotidien | Throughout the year we sit three exams. | Tout au long de l'année nous faisons trois examens.
to agree to | convenir de | Tournures | We agreed to meet on Tuesday. | Nous avons convenu de nous voir mardi.
to apologise for | s'excuser de | Tournures | He apologised for being late. | Il s'est excusé de son retard.
to apply for | postuler à | Tournures | He is applying for a job in Berlin. | Il postule à un poste à Berlin.
to attach importance to | attacher de l'importance à | Tournures | She attaches great importance to punctuality. | Elle attache une grande importance à la ponctualité.
to attend | participer à | Tournures | He is attending a language course. | Il participe à un cours de langue.
to back out | se rétracter | Tournures | He backed out at the last moment. | Il s'est rétracté au dernier moment.
to be afraid of | avoir peur de | Réagir | The child is afraid of the storm. | L'enfant a peur de l'orage.
to be an option | entrer en ligne de compte | Tournures | Moving is not an option for us. | Un déménagement n'entre pas en ligne de compte pour nous.
to be at stake | être en jeu | Tournures | There's a lot at stake this time. | Il y a beaucoup en jeu cette fois.
to be available | être à disposition | Tournures | I'm available to you for any questions. | Je reste à votre disposition pour toute question.
to be excited about | avoir hâte de, être enthousiaste | Réagir | I'm really excited about the trip. | J'ai vraiment hâte de faire ce voyage.
to be fed up | en avoir assez | Réagir | I'm fed up with this noise. | J'en ai assez de ce bruit.
to be honest | à vrai dire | Discuter | To be honest, I forgot. | À vrai dire, je l'ai oublié.
to be in a foul mood | être de mauvais poil | Tournures | He's in a foul mood today, don't ask him. | Aujourd'hui il est de mauvais poil, ne lui demande rien.
to be in fashion | être à la mode | Tournures | That cut is in fashion again. | Cette coupe est de nouveau à la mode.
to be on cloud nine | être au septième ciel | Réagir | Since the wedding she's been on cloud nine. | Depuis le mariage, elle est au septième ciel.
to be pleased about | se réjouir de (déjà arrivé) | Réagir | She was very pleased about the present. | Elle a été très contente du cadeau.
to be surprised at | s'étonner de | Réagir | I'm surprised at his reaction. | Je m'étonne de sa réaction.
to be up to date | être à jour | Tournures | He's up to date with everything. | Il est à jour sur tout ce qui se passe.
to bring up to date | mettre à jour | Tournures | He brought me up to date in five minutes. | Il m'a mis à jour en cinq minutes.
to call in sick | se déclarer malade | Au quotidien | I have to call in sick today. | Je dois me déclarer malade aujourd'hui.
to call it a day | en finir, arrêter | Au quotidien | Let's call it a day. | Pour aujourd'hui, nous arrêtons.
to carry out | mener à bien | Tournures | They carried out the study in six months. | Ils ont mené à bien l'étude en six mois.
to come across well | faire bonne impression | Tournures | He wants to come across well with everyone. | Il veut faire bonne impression auprès de tous.
to decide on | opter pour | Tournures | We decided on the smaller apartment. | Nous avons opté pour le plus petit appartement.
to fill out a form | remplir un formulaire | Au quotidien | Please fill out the form completely. | Veuillez remplir entièrement le formulaire.
to find an excuse | trouver une excuse | Au quotidien | He always finds an excuse. | Il trouve toujours une excuse.
to gain experience | acquérir de l'expérience | Tournures | You gain valuable experience during an internship. | En stage, on acquiert une expérience précieuse.
to get a word in | placer un mot | Tournures | She talks so much I can't get a word in. | Elle parle tellement que je n'arrive pas à placer un mot.
to get in touch | prendre contact | Au quotidien | Please get in touch with head office. | Veuillez prendre contact avec le siège.
to get on someone's nerves | taper sur les nerfs | Réagir | The constant ringing gets on my nerves. | Cette sonnerie continuelle me tape sur les nerfs.
to have access to | avoir accès à | Tournures | All students have access to the library. | Tous les étudiants ont accès à la bibliothèque.
to have an influence on | avoir une influence sur | Tournures | The weather has an influence on the harvest. | Le temps a une influence sur la récolte.
to hit the roof | sortir de ses gonds | Réagir | When he heard that, he hit the roof. | Quand il a entendu ça, il est sorti de ses gonds.
to come up with an idea | avoir une idée | Réagir | How did you come up with that idea? | Comment as-tu eu cette idée ?
to keep an eye on | jeter un œil | Tournures | Keep an eye on the pot. | Jette un œil à la casserole.
to keep one's word | tenir parole | Tournures | He always keeps his word. | Il tient toujours parole.
to keep pace with | suivre le rythme de | Tournures | Small firms can hardly keep pace. | Les petites entreprises peinent à suivre le rythme.
to keep track of | garder le fil de, suivre | Au quotidien | With so many appointments, I can hardly keep track of them. | Avec autant de rendez-vous, j'ai du mal à m'y retrouver.
to keep up to date | se tenir au courant | Au quotidien | I keep up to date through the news. | Je me tiens au courant par les informations.
to let off steam | vider son sac | Réagir | He needed to let off steam. | Il avait besoin de vider son sac.
to lose one's head | perdre la tête | Réagir | Even under stress she never loses her head. | Même sous le stress, elle ne perd jamais la tête.
to make an exception | faire une exception | Tournures | Today we'll make an exception. | Aujourd'hui, nous faisons une exception.
to make no difference | ne pas importer | Discuter | The price makes no difference here. | Le prix n'importe pas ici.
to make the best of it | en tirer le meilleur parti | Réagir | The weather is bad, let's make the best of it. | Le temps est mauvais, tirons-en le meilleur parti.
to meet a deadline | respecter un délai | Au quotidien | We absolutely have to meet the deadline. | Nous devons absolument respecter le délai.
to not feel like it | ne pas avoir envie | Réagir | Today I don't feel like cooking. | Aujourd'hui, je n'ai pas envie de cuisiner.
to partly agree | être d'accord en partie | Réagir | I partly agree with the report. | Je suis d'accord en partie avec le rapport.
to say hi to | dire bonjour de la part de | Bavarder | Say hi to your mother for me! | Dis bonjour à ta mère de ma part !
to pay a bill | régler une facture | Tournures | I still have to pay the bill. | Je dois encore régler la facture.
to play it safe | jouer la sécurité | Au quotidien | I'd rather play it safe and book early. | Je préfère jouer la sécurité et réserver tôt.
to put to the test | mettre à l'épreuve | Tournures | The move put our patience to the test. | Le déménagement a mis notre patience à l'épreuve.
to reckon with | s'attendre à | Tournures | We're reckoning with a delay. | Nous nous attendons à un retard.
to refer to | faire référence à | Tournures | I refer to your letter. | Je fais référence à votre courrier.
to refrain from | renoncer à | Tournures | We refrained from that plan. | Nous avons renoncé à ce plan.
to remain to be seen | rester à voir | Tournures | Whether it'll work remains to be seen. | Reste à voir si ça marchera.
to seize an opportunity | saisir une occasion | Au quotidien | He seized the opportunity at once. | Il a saisi l'occasion immédiatement.
to set in motion | mettre en route | Tournures | They set the plan in motion in January. | Ils ont mis en route le plan en janvier.
to set priorities | définir des priorités | Au quotidien | You have to set clear priorities. | Il faut définir des priorités claires.
to set the tone | donner le ton | Tournures | In this industry he sets the tone. | Dans ce secteur, c'est lui qui donne le ton.
to stand in the way | faire obstacle à | Tournures | Nothing stands in the way of the project any more. | Plus rien ne fait obstacle au projet.
to stay in touch | rester en contact | Tournures | We'll definitely stay in touch. | Nous restons en contact, c'est sûr.
to struggle with | avoir du mal avec | Réagir | I struggle with phrasal verbs. | J'ai du mal avec les verbes à particule.
to tackle something | s'attaquer à quelque chose | Au quotidien | Tomorrow we'll tackle the project. | Demain, nous nous attaquons au projet.
to take note of | prendre acte de | Tournures | We have taken note of your complaint. | Nous avons pris acte de votre réclamation.
to take notes | prendre des notes | Au quotidien | I take notes during the meeting. | Je prends des notes pendant la réunion.
to take one's time | prendre son temps | Au quotidien | Take your time with the answer. | Prends ton temps pour la réponse.
to work overtime | faire des heures supplémentaires | Au quotidien | This week I'm working a lot of overtime. | Cette semaine, je fais beaucoup d'heures supplémentaires.
to worry about | se faire du souci pour | Réagir | Don't worry about the exam. | Ne te fais pas de souci pour l'examen.
up to date | à jour | Au quotidien | The software is up to date. | Le logiciel est à jour.
what's new | quoi de neuf ? | Bavarder | Long time no talk, what's new? | Ça fait longtemps, quoi de neuf ?
it's about | il s'agit de | Discuter | The meeting is about the new budget. | Lors de la réunion, il s'agit du nouveau budget.
to play a role | jouer un rôle | Tournures | Luck played a big role in his success. | La chance a joué un grand rôle dans son succès.
to take responsibility | assumer la responsabilité | Tournures | She took responsibility for the project. | Elle a assumé la responsabilité du projet.
to make use of | faire appel à, mobiliser | Tournures | She made use of legal advice. | Elle a fait appel à un conseil juridique.
to come up | être abordé (sujet) | Discuter | The topic came up yesterday. | Le sujet a été abordé hier.
depending on | selon les cas | Discuter | Depending on the weather, we'll go. | Selon le temps qu'il fera, nous partirons.
to find a compromise | trouver un compromis | Tournures | In the end we found a compromise. | Finalement, nous avons trouvé un compromis.
Take care | Porte-toi bien | Bavarder | I have to go. Take care! | Je dois y aller. Porte-toi bien !
for one thing ... for another | d'une part ... d'autre part | Discuter | For one thing there's no money, for another no time. | D'une part il manque de l'argent, d'autre part du temps.
as far as … is concerned | en ce qui concerne | Discuter | As far as money is concerned, I'm careful. | En ce qui concerne l'argent, je suis prudent.
to assert oneself | s'imposer | Tournures | She asserted herself against the competition. | Elle s'est imposée face à la concurrence.
to make a name for oneself | se faire un nom | Tournures | He has made a name for himself as an architect. | Il s'est fait un nom comme architecte.
to lend a hand | mettre la main à la pâte | Au quotidien | Everyone lent a hand. | Tout le monde a mis la main à la pâte.
to take the floor | prendre la parole | Tournures | After him the director took the floor. | Après lui, la directrice a pris la parole.
"""
