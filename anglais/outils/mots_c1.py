# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du C1 anglais. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que mots_a1.py et phrases_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'C1'

# « verbe | traduction | drapeaux » ; les formes sont calculees (irreguliers.py).
VERBES = """
acknowledge | saluer, rendre hommage à
adjourn | ajourner, reporter
admonish | exhorter, rappeler à l'ordre
agree with | abonder dans le sens de, approuver
allot | répartir, allouer
amaze | stupéfier, épater
answer for | répondre de, se porter garant
approve | autoriser, approuver
approve of | approuver, donner son aval
archive | archiver
ascertain | établir, déterminer
avert | détourner, éviter (un danger)
backpedal | faire marche arrière
beset | harceler, mettre sous pression
brush up | rafraîchir (des connaissances)
bundle | regrouper, mutualiser
camouflage | camoufler, masquer
carry on | poursuivre, reprendre le flambeau
cast doubt on | mettre en doute
caution | avertir officiellement
cement | figer, bétonner
change tack | changer de cap, virer
compensate for | compenser
compile | rassembler, compiler
continue to exist | subsister, continuer d'exister
copy-edit | relire et corriger (un manuscrit)
counter with | opposer (un argument)
cover up | étouffer, dissimuler
cram | bachoter, potasser
creep in | s'installer (une mauvaise habitude) ; démolir
cushion | amortir, absorber (un choc)
de-escalate | désamorcer, faire baisser la tension
deem | juger, estimer (qch)
deepen | approfondir
defer | différer, mettre en attente
defuse | désamorcer, atténuer
delimit | délimiter, distinguer
deny officially | démentir
derive | déduire, dériver
digress | digresser, s'éloigner du sujet
disapprove of | désapprouver
disconcert | déconcerter, choquer
discourage | décourager
discuss in detail | discuter en détail, débattre de
dismay | consterner, bouleverser
dispel | dissiper (des doutes) ; distraire
distort | fausser, altérer
dominate | dominer
draw level | revenir à égalité, rattraper
draw on | faire appel à, se référer à
ease off | faiblir, retomber
ebb away | refluer, retomber
embellish | enjoliver, broder
emerge from | ressortir de, résulter
empathize with | comprendre par empathie, se représenter
enshrine | inscrire, graver dans un texte
entrust with | charger de, confier une mission
escalate | exacerber, radicaliser
exceed | dépasser, franchir
expire | expirer, arriver à échéance
factor in | prévoir dans le calcul, tenir compte de
fail to materialize | ne pas se produire, faire défaut
fall back | décrocher, retomber
fall below | rester en dessous de
fall to | revenir à, incomber
feed through | se répercuter, se faire sentir
feign | feindre, simuler
flag | s'essouffler, retomber
follow suit | emboîter le pas, suivre
follow up | relancer, creuser (une question)
forge | falsifier, contrefaire
forward | transmettre, faire suivre
get stuck in | mettre la main à la pâte ; empoigner
get through | tenir jusqu'au bout, traverser
gloss over | enjoliver, présenter sous un jour favorable
have a say | avoir voix au chapitre
have an effect | porter ses fruits, servir à quelque chose
help shape | contribuer à façonner
hold out | tenir jusqu'au bout
infiltrate | noyauter, infiltrer
inherit from | hériter de, prendre la succession de
insinuate | insinuer, imputer
insist on | insister, faire valoir avec force
inspect | consulter ; reconnaître
internalize | intérioriser, s'approprier
label | étiqueter, annoter
lead to | déboucher sur, se jeter dans
leak to | faire parvenir (discrètement) ; passer
leave aside | laisser de côté, exclure
lie ahead | être imminent
locate | situer, localiser
loosen | assouplir, desserrer
make clear | mettre les choses au clair
make sense | paraître évident, convaincre
memorize | graver dans la mémoire
minute | consigner, dresser le procès-verbal
misappropriate | détourner de sa destination
narrow down | circonscrire, restreindre
number | numéroter
obscure | masquer, obscurcir
outlast | survivre à, traverser le temps
outline | esquisser à grands traits
outweigh | contrebalancer, valoir
paralyse | paralyser
paraphrase | paraphraser, contourner par une périphrase
pay for itself | amortir, rentabiliser
penalize | sanctionner, réprimer
peter out | s'enliser, tourner court
placate | apaiser, calmer les esprits
play down | minimiser, banaliser
presuppose | présupposer, exiger comme condition
radiate | rayonner, diffuser
ramble | s'étendre à l'excès
ramp up | monter en puissance, démarrer
readjust | réajuster
reaffirm | réaffirmer, confirmer avec force
reallocate | réaffecter, redéployer
rearrange | réorganiser, permuter
refine | affiner, raffiner
refuse | refuser (de donner)
relent | revenir à de meilleurs sentiments, céder
renegotiate | renégocier
repurpose | réaffecter (un lieu, un fonds)
resume | reprendre (une activité, un dossier)
rethink | changer sa façon de penser
retort | répliquer, rétorquer
revoke | révoquer, se rétracter
rub off on | déteindre (au propre et au figuré)
scale back | réduire progressivement
scout out | explorer, aller reconnaître
scrutinize | passer au crible, radiographier
second | détacher (du personnel) ; arrêter
sense | pressentir, deviner
shoulder | prendre sur ses épaules, assumer
shrug off | encaisser sans broncher
sift through | trier, passer en revue ; apercevoir
slim down | alléger, dégraisser
soothe | adoucir, calmer
spread to | s'étendre, gagner
spur on | stimuler, aiguillonner
stir up | remuer, bouleverser
stray from | s'écarter, dévier
stumble | trébucher, vaciller
subdivide | subdiviser, structurer
submit later | fournir ultérieurement
subsidize | subventionner
substantiate | corroborer, confirmer
swot | bûcher, bosser (des révisions)
sympathize | compatir
testify to | témoigner de, attester
throttle back | réduire, brider
thwart | faire échouer, déjouer
tighten up | resserrer, alléger
title | intituler
tolerate | tolérer, souffrir
tough it out | s'accrocher, serrer les dents
turn back | faire demi-tour, inverser
uncover | mettre au jour, révéler
unite | unifier, réunir (qn, qch)
urge | presser, pousser
vouch | se porter garant
wear down | user, miner
weight | pondérer, hiérarchiser
withhold | priver de, refuser (une information)
withstand | résister, tenir bon
"""

# « adjectif | traduction | drapeaux » (gb=, ex=).
ADJECTIFS = """
acceptable | acceptable, tolérable
accurate | exact, qui correspond
aimless | sans méthode, au hasard
amateurish | d'amateur, maladroit
apparently | apparemment, de toute évidence
astonishing | stupéfiant
authoritative | déterminant, faisant autorité
backed up | étayé, sécurisé
backward | arriéré, en retard
bearable | supportable (perte)
beyond doubt | hors de doute
bombastic | pompeux, boursouflé
brisk | décidé, sans détour
buttoned-up | boutonné, peu communicatif
casual | fait en passant, désinvolte
clear-cut | clairement délimité, discriminant
coarse | grossier ; grave (faute)
communicative | communicatif, expansif
compelling | impératif, contraignant
conciliatory | conciliant
concise | concis, net
condensed | condensé, serré
conditional | sous conditions, relatif
confirmed | confirmé
considerable | considérable
contestable | contestable, attaquable
contrived | affecté, alambiqué
conventional | traditionnel, classique
creeping | insidieux, rampant
cryptic | cryptique, obscur
dainty | menu, délicat
damaged | défectueux, abîmé
depressing | accablant, pesant
disarming | désarmant
disconcerting | déconcertant, étrange
dispensable | superflu, dont on peut se passer
disproportionate | disproportionné
disputed | litigieux, contesté
distorted | faussé, déformé
disturbing | troublant, perturbant
dividing | qui sépare, clivant
divisive | clivant
documented | documenté
down-to-earth | terre-à-terre, sans prétention
easy-care | facile d'entretien
elaborate | coûteux en moyens, élaboré
endurable | tenable, endurable
erratic | par à-coups, versatile
error-free | sans faute
established | avéré
excessive | exagéré, excessif
exhaustive | exhaustif
fail-safe | à toute épreuve, redondant
far-fetched | saugrenu, hors de propos
far-reaching | de grande portée
faulty | erroné, comportant des erreurs
final | définitif
flawless | irréprochable
foreseeable | prévisible, à vue
forward-looking | porteur d'avenir
fragmentary | fragmentaire
generalizable | généralisable
gripping | poignant, saisissant
groundbreaking | pionnier, qui montre la voie
hair-raising | à faire dresser les cheveux
half-hearted | sans conviction, à moitié
hotly contested | disputé, âprement contesté
idiosyncratic | singulier, à sa façon
illuminating | éclairant
immature | immature, mal abouti
impeccable | impeccable
impermissible | non admissible, interdit
improper | impropre, inadéquat
inaccessible | inaccessible ; fermé
inaccurate | inexact, sans objet
inadequate | insuffisant
incidental | accessoire, secondaire
inconsistent | incohérent, discordant
indefensible | indéfendable
inevitable | inévitable
insensitive | peu délicat, maladroit
insignificant | insignifiant, sans importance
irreconcilable | irréconciliable, intransigeant
isolated | isolé, sporadique
justifiable | défendable, justifiable
lenient | indulgent
level-headed | posé, réfléchi
load-bearing | porteur, central
long-winded | prolixe, verbeux
low-maintenance | peu exigeant en entretien
makeshift | de fortune
manageable | maniable, gérable
mature | abouti, mûri
meaningful | significatif, parlant
measurable | mesurable
methodical | méthodique, ordonné
minor | minime, négligeable
model | modèle, irréprochable
moving | émouvant
nationwide | généralisé, sur tout le territoire
negligent | par négligence
non-transparent | opaque (procédure)
noticeable | sensible, perceptible
novel | d'un genre nouveau
opaque | opaque, obscur
oppressive | oppressant, angoissant
outmoded | anachronique, d'un autre temps
outrageous | aberrant, gros comme une maison
overarching | supérieur, englobant
overwhelmed | dépassé, débordé
patchy | lacunaire
pedantic | pointilleux, tatillon
pending | pendant (devant un tribunal)
peripheral | périphérique
permissible | admissible, autorisé
persevering | endurant, persévérant
pithy | frappant, ramassé
practised | aguerri, rodé
presumed | présumé
priority | prioritaire
professionally | dans les règles de l'art
profound | profond, en profondeur
promptly | dans un délai rapproché
proper | en bonne et due forme
proven | démontré, établi
quantifiable | quantifiable
rapid | fulgurant, très rapide
refuted | réfuté
repeatable | répétable
reproducible | reproductible
resolute | résolu, ferme
restrained | retenu, mesuré
revealing | instructif, révélateur
revised | remanié ; surmené
seamless | sans faille, complet
selective | ponctuel, par endroits
shameful | honteux, accablant
shattering | bouleversant, accablant
short-lived | éphémère
sketchy | à l'état d'ébauche
sober | sobre, lucide
sobering | qui ramène sur terre, décevant
species-appropriate | respectueux de l'espèce (animal)
spotless | sans défaut, immaculé
steady | constant, régulier
stilted | guindé, compassé
striking | frappant
stringent | rigoureux, qui se tient
subordinate | de rang inférieur, subordonné
supposed | prétendu, soi-disant
symptomatic | symptomatique
tailor-made | sur mesure
telling | significatif, caractéristique
telltale | révélateur (malgré soi)
tentative | timide, hésitant
terse | lapidaire, laconique
tireless | infatigable
tortuous | tortueux, sinueux (raisonnement)
touching | touchant, attendrissant
trained in | formé, à jour dans son poste
transferable | transposable, transmissible
trend-setting | qui donne le cap
trivial | insignifiant, sans importance
unbearable | insupportable
unchallenged | incontesté, sans rival
uncommon | peu usité
uncontroversial | unanimement admis
under-challenged | sous-employé, pas assez sollicité
undeterred | imperturbable
undisputed | incontesté
unfit | inapte, impropre
unforgiving | sans indulgence, inflexible
unifying | fédérateur, qui rapproche
unlawful | illégal, contraire au droit
unproductive | stérile, peu productif
unproven | non prouvé
unreserved | sans réserve
unresolved | en suspens, non tranché
unrestricted | sans restriction, entier
unsettled | instable, changeant
unsparing | sans complaisance, impitoyable
unsubstantiated | non attesté, sans preuve
unsuitable | inapproprié, mal adapté
untenable | insoutenable, intenable
unwieldy | encombrant ; rébarbatif
unyielding | intransigeant
upcoming | à venir, à l'ordre du jour
usable | utilisable, exploitable
verifiable | vérifiable
void | caduc, sans objet
wanton | délibéré, par pure malveillance
wasteful | dispendieux, prodigue
well-rehearsed | rodé (une équipe)
well-versed | chevronné, versé
woolly | flou, vaseux
worthwhile | qui vaut la peine
"""

# « adverbe | traduction | categorie | drapeaux ».
ADVERBES = """
abruptly | brusquement | Manière
although | étant entendu que | Liaison
any day | à coup sûr, largement | Nuance
at worst | au pire | Nuance
conversely | inversement | Liaison
demonstrably | de façon avérée | Nuance
equally | de la même façon | Liaison
especially as | d'autant plus que | Cause et conséquence
furthermore | en outre | Liaison
incidentally | au demeurant | Liaison
instead | au lieu de cela | Liaison
literally | littéralement | Nuance
noticeably | sensiblement | Quantité
on this | à ce sujet | Liaison
or rather | ou plutôt, respectivement | Liaison
pleasingly | heureusement | Nuance
specially | spécialement | Manière
understandably | on le comprend | Nuance
unexpectedly | à l'improviste | Manière
whereas | tandis que, alors que | Liaison
without exception | sans exception | Quantité
"""

# « expression | traduction | categorie | exemple anglais | exemple francais ».
EXPRESSIONS = """
against the backdrop of | dans le contexte de | Discuter | Against the backdrop of the crisis the sum looks small. | Dans le contexte de la crise, la somme paraît faible.
as things stand | en l'état des choses | Discuter | As things stand, the law won't happen. | En l'état des choses, la loi ne verra pas le jour.
Dear Sir or Madam | Madame, Monsieur | Bavarder | Dear Sir or Madam, I am hereby applying for the position. | Madame, Monsieur, je vous adresse ma candidature pour ce poste.
everything in me resists | tout en moi se rebiffe | Réagir | Everything in me resists signing that. | Tout en moi se rebiffe à l'idée de signer cela.
for all the criticism | malgré toutes les critiques | Discuter | For all the criticism, the project improved a great deal. | Malgré toutes les critiques, le projet a amélioré bien des choses.
for the sake of completeness | par souci d'exhaustivité | Discuter | For the sake of completeness, let's mention the third option. | Par souci d'exhaustivité, mentionnons la troisième variante.
for want of | à défaut de | Discuter | For want of better proposals, the old plan stayed. | À défaut de meilleures propositions, on en est resté à l'ancien plan.
I can only agree | je ne peux qu'approuver | Donner son avis | I can only agree, that was long overdue. | Je ne peux qu'approuver, cela n'avait que trop tardé.
I could jump out of my skin | je pourrais exploser | Réagir | With so much bureaucracy I could jump out of my skin. | Avec tant de bureaucratie, je pourrais exploser.
I find that far-fetched | je trouve cela tiré par les cheveux | Donner son avis | I find that far-fetched; there's no evidence for it. | Je trouve cela tiré par les cheveux, rien ne le prouve.
I take the liberty of pointing out | je me permets de vous signaler | Bavarder | I take the liberty of pointing out that the deadline ends tomorrow. | Je me permets de vous signaler que le délai expire demain.
I take the view | je suis d'avis | Donner son avis | I take the view that we gave up too early. | Je suis d'avis que nous avons abandonné trop tôt.
I would be grateful if | je vous serais reconnaissant de | Bavarder | I would be grateful if you could send me the documents. | Je vous serais reconnaissant de bien vouloir m'envoyer les documents.
I'm available for any questions | je reste à votre disposition | Bavarder | I'm happy to be available for any questions. | Je reste volontiers à votre disposition.
I'm completely with you | je te suis entièrement | Donner son avis | I'm completely with you, this can't go on. | Je te suis entièrement, cela ne peut pas continuer ainsi.
I'm getting in touch regarding | je vous contacte au sujet de | Bavarder | I'm getting in touch regarding your enquiry from Monday. | Je vous contacte au sujet de votre demande de lundi.
I'm inclined to think | je penche pour l'idée | Donner son avis | I'm inclined to think we should wait. | Je penche pour l'idée que nous devrions attendre.
I'm sceptical about it | je suis sceptique là-dessus | Donner son avis | I'm sceptical about it; the figures don't convince me. | Je suis sceptique là-dessus, les chiffres ne me convainquent pas.
I'm torn | je suis partagé | Réagir | I'm torn between the two offers. | Je suis partagé entre les deux offres.
in plain language | en clair | Discuter | In plain language: the money isn't enough. | En clair : l'argent ne suffit pas.
in return | en contrepartie | Discuter | He takes the shift, and in return he gets Friday off. | Il prend le quart, en contrepartie il a son vendredi.
in the cold light of day | à bien y regarder | Discuter | In the cold light of day the offer was no bargain. | À bien y regarder, l'offre n'était pas une aubaine.
in the course of this | dans la foulée | Discuter | The department moved; in the course of this the equipment was renewed. | Le service a déménagé ; dans la foulée, le matériel a été renouvelé.
in view of this | au vu de cela | Discuter | In view of this, the meeting was postponed. | Au vu de cela, la séance a été reportée.
it matters to me | cela me tient à cœur | Réagir | It matters to me that everyone is heard. | Cela me tient à cœur que tout le monde soit entendu.
kind regards | cordialement | Bavarder | Kind regards, Anna Berger. | Cordialement, Anna Berger.
let alone | et encore moins | Discuter | He didn't call, let alone apologise. | Il n'a pas appelé, et encore moins présenté ses excuses.
not by chance | ce n'est pas un hasard | Discuter | It's not by chance that the contract fell through. | Ce n'est pas un hasard si le contrat a échoué.
notwithstanding this | nonobstant cela | Discuter | Notwithstanding this, she stuck to her opinion. | Nonobstant cela, elle a maintenu son opinion.
please find attached | vous trouverez ci-joint | Bavarder | Please find attached the signed agreement. | Vous trouverez ci-joint la convention signée.
thank you in advance | merci d'avance | Bavarder | Thank you in advance for your reply. | Merci d'avance pour votre réponse.
that leaves me cold | cela me laisse froid | Réagir | Threats like that leave me cold. | De telles menaces me laissent froid.
that may be | c'est possible, mais | Discuter | That may be, but the figures say otherwise. | C'est possible, mais les chiffres disent autre chose.
that rubs me the wrong way | ça me hérisse | Réagir | All this secrecy rubs me the wrong way. | Ces cachotteries me hérissent.
that seems fishy to me | cela me semble louche | Réagir | The low price seems fishy to me. | Ce prix si bas me semble louche.
that sounds promising | voilà qui est intéressant | Donner son avis | Ten percent off? That sounds promising. | Dix pour cent de remise ? Voilà qui est intéressant.
that takes the biscuit | c'est la goutte d'eau | Réagir | And now the fee too? That takes the biscuit. | Et maintenant les frais en plus ? C'est la goutte d'eau.
that's a mystery to me | c'est un mystère pour moi | Réagir | How he managed it is a mystery to me. | Comment il y est arrivé, c'est un mystère pour moi.
that's a weight off my mind | cela m'ôte un poids | Réagir | She arrived safely — that's a weight off my mind. | Elle est bien arrivée — cela m'ôte un poids.
that's the last straw for my nerves | cela m'achève les nerfs | Réagir | The constant queries are the last straw for my nerves. | Ces questions incessantes m'achèvent les nerfs.
to be applied | s'appliquer, être applicable | Tournures | The rule is applied only domestically. | La règle ne s'applique qu'à l'intérieur du pays.
to be on the table | être en suspens | Discuter | The accusation is still on the table. | Le reproche reste en suspens.
to bring about a decision | provoquer une décision | Au quotidien | The vote is meant to finally bring about a decision. | Le vote doit enfin provoquer une décision.
to cause offence | faire scandale | Tournures | The advert caused great offence. | La publicité a fait grand scandale.
to charge | facturer | Au quotidien | The call-out is charged separately. | Le déplacement est facturé à part.
to clarify | faire la lumière | Tournures | An expert report is to clarify matters. | Une expertise doit faire la lumière.
to comply with | donner suite à | Tournures | He complied with the request. | Il a donné suite à la demande.
to confront | demander des comptes à | Tournures | The boss confronted him about the figures. | Le patron lui a demandé des comptes sur les chiffres.
to demonstrate | faire la preuve de | Tournures | She demonstrated her ability. | Elle a fait la preuve de son savoir-faire.
to exert influence | exercer une influence | Tournures | No one may exert influence on the verdict. | Personne ne doit exercer d'influence sur le jugement.
to exert pressure | exercer une pression | Tournures | Investors are exerting pressure on the board. | Les investisseurs exercent une pression sur la direction.
to fall behind | prendre du retard | Au quotidien | The construction has fallen months behind. | Le chantier a pris des mois de retard.
to fall into oblivion | tomber dans l'oubli | Tournures | The craft has almost fallen into oblivion. | Ce métier est presque tombé dans l'oubli.
to file a report | porter plainte | Au quotidien | After the break-in he filed a report. | Après le cambriolage, il a porté plainte.
to file an appeal | former un recours | Au quotidien | She filed an appeal against the dismissal. | Elle a formé un recours contre le licenciement.
to get under way | lancer | Au quotidien | Parliament got the law under way. | Le parlement a lancé la loi.
to give an account | rendre des comptes | Tournures | The board must give an account of the spending. | La direction doit rendre des comptes sur les dépenses.
to give credence to | prêter foi à | Tournures | One shouldn't give credence to the rumour. | Il ne faut pas prêter foi à cette rumeur.
to harbour doubts | nourrir des doutes | Tournures | I harbour doubts about this account. | Je nourris des doutes sur cette version.
to lay claim | revendiquer | Tournures | Both sides lay claim to the plot. | Les deux parties revendiquent le terrain.
to lodge a complaint | déposer une réclamation | Au quotidien | The customer lodged a complaint. | Le client a déposé une réclamation.
to lodge an objection | faire opposition | Au quotidien | You can lodge an objection against the notice. | On peut faire opposition à cette décision.
to make compromises | accepter des compromis | Tournures | Anyone who negotiates has to make compromises. | Qui négocie doit accepter des compromis.
to make concessions | faire des concessions | Tournures | Both sides had to make concessions. | Les deux parties ont dû faire des concessions.
to make provision | prendre des précautions | Au quotidien | You should make provision for emergencies. | Il faut prendre des précautions pour les cas d'urgence.
to meet with approval | recueillir l'adhésion | Tournures | The draft met with broad approval. | Le projet a recueilli une large adhésion.
to put into practice | mettre en pratique | Au quotidien | The idea was never put into practice. | L'idée n'a jamais été mise en pratique.
to put up resistance | opposer une résistance | Tournures | Local residents put up fierce resistance. | Les riverains ont opposé une résistance acharnée.
to report | faire rapport | Au quotidien | She reports to the committee monthly. | Elle fait rapport à la commission chaque mois.
to seethe with anger | bouillir de rage | Réagir | After the call he was seething with anger. | Après l'appel, il bouillait de rage.
to state for the record | déclarer au procès-verbal | Au quotidien | The witness stated for the record that he had seen nothing. | Le témoin a déclaré au procès-verbal n'avoir rien vu.
to submit a proposal | soumettre une proposition | Tournures | She submitted a proposal to the council. | Elle a soumis une proposition au conseil.
to voice concerns | émettre des réserves | Tournures | Several members voiced concerns. | Plusieurs membres ont émis des réserves.
to voice criticism | formuler des critiques | Tournures | The association voiced sharp criticism of the draft. | La fédération a formulé de vives critiques sur le projet.
you've got me there | là, je sèche | Réagir | When the law takes effect? You've got me there. | Quand la loi entre en vigueur ? Là, je sèche.
yours faithfully | veuillez agréer mes salutations distinguées | Bavarder | Yours faithfully, Dr Meier. | Veuillez agréer mes salutations distinguées, Dr Meier.
"""
