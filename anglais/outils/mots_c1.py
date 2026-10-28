# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du C1 anglais. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que mots_a1.py et phrases_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'C1'

# « verbe | traduction | drapeaux » ; les formes sont calculees (irreguliers.py).
VERBES = """
acknowledge | reconnaître, accuser réception | ex=He acknowledged that he had made a mistake. # Il a reconnu qu'il avait fait une erreur.
adjourn | ajourner, lever (la séance) | ex=The meeting was adjourned until Monday. # La réunion a été ajournée à lundi.
allot | répartir, allouer
amaze | stupéfier, épater
approve | autoriser, approuver
approve of | approuver | ex=Her parents don't approve of her boyfriend. # Ses parents n'approuvent pas son petit ami.
archive | archiver
ascertain | établir, déterminer
avert | détourner, éviter (un danger)
backpedal | faire marche arrière
brush up | rafraîchir (des connaissances)
bundle | regrouper | ex=The software is bundled with the computer. # Le logiciel est fourni avec l'ordinateur.
camouflage | camoufler | ex=The soldiers camouflaged their tents. # Les soldats ont camouflé leurs tentes.
carry on | continuer, poursuivre
cast doubt on | mettre en doute | ex=New evidence cast doubt on his story. # De nouvelles preuves ont mis en doute sa version.
compensate for | compenser
compile | compiler, rassembler | ex=We compiled a list of all the restaurants. # Nous avons dressé la liste de tous les restaurants.
cover up | étouffer, dissimuler
cram | bachoter | ex=She crammed all night for the exam. # Elle a bachoté toute la nuit pour l'examen.
creep in | s'installer, se glisser | ex=A few mistakes crept in during the translation. # Quelques erreurs se sont glissées dans la traduction.
cushion | amortir, absorber (un choc)
de-escalate | désamorcer, faire baisser la tension
deem | juger, estimer (qch)
deepen | approfondir | ex=The course helped me deepen my knowledge. # Le cours m'a aidé à approfondir mes connaissances.
defer | reporter, différer | ex=You can defer payment until next month. # Vous pouvez reporter le paiement au mois prochain.
defuse | désamorcer, atténuer
derive | déduire, dériver
digress | digresser, s'éloigner du sujet
disapprove of | désapprouver
disconcert | déconcerter, choquer
discourage | décourager
dismay | consterner, bouleverser
dispel | dissiper
distort | fausser, altérer
dominate | dominer
draw on | faire appel à, se référer à
ease off | faiblir, retomber
embellish | enjoliver, broder
empathize with | se mettre à la place de | ex=It's hard to empathize with someone you've never met. # Il est difficile de se mettre à la place de quelqu'un qu'on n'a jamais rencontré.
enshrine | inscrire, graver dans un texte
entrust with | confier à
escalate | exacerber, radicaliser
exceed | dépasser, franchir
expire | expirer, arriver à échéance
factor in | tenir compte de | ex=Don't forget to factor in the cost of gas. # N'oublie pas de tenir compte du prix de l'essence.
feign | feindre, simuler
follow suit | emboîter le pas, suivre
follow up | assurer le suivi, relancer
forge | falsifier, contrefaire
forward | transférer, faire suivre
get through | traverser, tenir le coup
gloss over | glisser sur, passer sous silence
have a say | avoir voix au chapitre
hold out | tenir bon
infiltrate | infiltrer | ex=The police infiltrated the gang. # La police a infiltré le gang.
insinuate | insinuer | ex=Are you insinuating that I lied? # Tu insinues que j'ai menti ?
insist on | insister sur
inspect | inspecter
internalize | intérioriser | ex=Children internalize their parents' values. # Les enfants intériorisent les valeurs de leurs parents.
label | étiqueter, annoter
lead to | mener à, entraîner
leave aside | laisser de côté | ex=Leaving aside the cost, the plan is excellent. # Le coût mis à part, le projet est excellent.
lie ahead | être à venir, attendre (quelqu'un)
locate | situer, localiser
loosen | desserrer, assouplir | ex=He loosened his tie after the meeting. # Il a desserré sa cravate après la réunion.
memorize | graver dans la mémoire
narrow down | restreindre, affiner | ex=We've narrowed down the list to three candidates. # Nous avons réduit la liste à trois candidats.
obscure | masquer, obscurcir
outlast | survivre à, traverser le temps
outline | exposer dans les grandes lignes
outweigh | l'emporter sur
paralyze | paralyser | ex=The snowstorm paralyzed the city. # La tempête de neige a paralysé la ville.
paraphrase | paraphraser, contourner par une périphrase
pay for itself | être rentabilisé
penalize | sanctionner, réprimer
peter out | s'enliser, tourner court
placate | apaiser, calmer les esprits
play down | minimiser, banaliser
radiate | rayonner, diffuser
ramble | s'étendre à l'excès
ramp up | monter en puissance, démarrer
readjust | se réadapter, réajuster | ex=It took me weeks to readjust after the trip. # Il m'a fallu des semaines pour me réadapter après le voyage.
reaffirm | réaffirmer, confirmer avec force
rearrange | réorganiser | ex=We rearranged the furniture in the living room. # Nous avons réorganisé les meubles du salon.
refine | affiner, raffiner
refuse | refuser (de donner)
relent | revenir à de meilleurs sentiments, céder
renegotiate | renégocier
repurpose | réaffecter (un lieu, un fonds)
resume | reprendre (faux ami : résumer = summarize) | ex=The game resumed after the rain stopped. # Le match a repris quand la pluie s'est arrêtée.
rethink | repenser
retort | répliquer, rétorquer
revoke | révoquer, se rétracter
rub off on | déteindre sur
scale back | réduire progressivement
scrutinize | passer au crible, radiographier
sense | pressentir, deviner
shoulder | prendre sur ses épaules, assumer
shrug off | ignorer, faire fi de | ex=She shrugged off the criticism. # Elle a ignoré les critiques.
sift through | passer au crible
soothe | apaiser | ex=The music soothed the crying baby. # La musique a apaisé le bébé qui pleurait.
spur on | encourager, pousser | ex=The crowd spurred the runners on. # La foule a encouragé les coureurs.
stir up | attiser, provoquer | ex=His comments stirred up a lot of anger. # Ses commentaires ont provoqué beaucoup de colère.
stumble | trébucher
subsidize | subventionner
substantiate | corroborer, confirmer
sympathize | compatir | ex=I sympathize, but I can't help you. # Je compatis, mais je ne peux pas t'aider.
thwart | faire échouer, déjouer
tolerate | tolérer | ex=The teacher won't tolerate cheating. # Le professeur ne tolère pas la triche.
tough it out | tenir bon | ex=The job is hard, but I'll tough it out. # Le travail est dur, mais je vais tenir bon.
turn back | faire demi-tour, inverser
uncover | mettre au jour, révéler
unite | unifier, réunir (qn, qch)
urge | presser, pousser
vouch for | se porter garant de | ex=I can vouch for her honesty. # Je peux me porter garant de son honnêteté.
wear down | user, épuiser | ex=The long winter wore everyone down. # Le long hiver a épuisé tout le monde.
withhold | retenir, refuser de communiquer
withstand | résister, tenir bon
undermine | saper, affaiblir | ex=Constant criticism undermines her confidence. # Les critiques constantes sapent sa confiance.
bolster | renforcer, consolider | ex=The win bolstered the team's morale. # La victoire a renforcé le moral de l'équipe.
curtail | restreindre, écourter | ex=The new law curtails the power of the mayor. # La nouvelle loi restreint le pouvoir du maire.
deter | dissuader | ex=High prices deter many customers. # Les prix élevés dissuadent de nombreux clients.
alleviate | soulager, atténuer | ex=This medicine alleviates the pain. # Ce médicament soulage la douleur.
exacerbate | aggraver | ex=Stress can exacerbate the symptoms. # Le stress peut aggraver les symptômes.
jeopardize | compromettre, mettre en péril | ex=One mistake could jeopardize the whole project. # Une seule erreur pourrait compromettre tout le projet.
hinder | entraver, gêner | ex=The snow hindered the rescue efforts. # La neige a gêné les secours.
endorse | approuver, soutenir | ex=The mayor endorsed the new plan. # Le maire a soutenu le nouveau projet.
reiterate | réitérer | ex=She reiterated her support for the project. # Elle a réitéré son soutien au projet.
discern | discerner | ex=It was hard to discern any difference. # Il était difficile de discerner la moindre différence.
elicit | susciter, obtenir | ex=The question elicited a strong reaction. # La question a suscité une vive réaction.
encompass | englober | ex=The course encompasses all aspects of design. # Le cours englobe tous les aspects du design.
facilitate | faciliter | ex=The new app facilitates online payments. # La nouvelle application facilite les paiements en ligne.
forgo | renoncer à | ex=She forwent her bonus to save jobs. # Elle a renoncé à sa prime pour sauver des emplois.
garner | recueillir, obtenir | ex=The proposal garnered wide support. # La proposition a recueilli un large soutien.
hamper | entraver | ex=Bad weather hampered the search. # Le mauvais temps a entravé les recherches.
impede | gêner, freiner | ex=Nothing should impede your progress. # Rien ne devrait freiner tes progrès.
incur | encourir, engager (des frais) | ex=You may incur extra charges. # Des frais supplémentaires peuvent s'appliquer.
instigate | provoquer, être à l'origine de | ex=He instigated the reforms. # C'est lui qui est à l'origine des réformes.
navigate | naviguer, s'orienter dans | ex=It's hard to navigate the health care system. # Il est difficile de s'y retrouver dans le système de santé.
nurture | entretenir, cultiver | ex=Good teachers nurture curiosity. # Les bons enseignants cultivent la curiosité.
oust | évincer | ex=The board ousted the CEO. # Le conseil d'administration a évincé le PDG.
perpetuate | perpétuer | ex=Some movies perpetuate old stereotypes. # Certains films perpétuent de vieux stéréotypes.
plummet | chuter, s'effondrer | ex=Temperatures plummeted overnight. # Les températures ont chuté pendant la nuit.
proliferate | proliférer | ex=Fake news proliferates online. # Les fausses nouvelles prolifèrent en ligne.
refute | réfuter | ex=She refuted every argument. # Elle a réfuté chaque argument.
relinquish | céder, renoncer à | ex=He refused to relinquish control of the company. # Il a refusé de céder le contrôle de l'entreprise.
stem from | provenir de, découler de | ex=His fear stems from a childhood accident. # Sa peur vient d'un accident d'enfance.
undertake | entreprendre | ex=The city undertook a major renovation. # La ville a entrepris une grande rénovation.
uphold | maintenir, faire respecter | ex=The court upheld the decision. # Le tribunal a confirmé la décision.
warrant | justifier | ex=The situation doesn't warrant panic. # La situation ne justifie pas la panique.
waver | hésiter, vaciller | ex=She never wavered in her support. # Son soutien n'a jamais faibli.
come across | tomber sur ; donner l'impression | ex=I came across an old photo of you. # Je suis tombé sur une vieille photo de toi.
come up against | se heurter à | ex=We came up against a lot of resistance. # Nous nous sommes heurtés à beaucoup de résistance.
brush off | rejeter, ignorer | ex=He brushed off the criticism. # Il a balayé les critiques.
bring forward | avancer (une date), présenter | ex=The meeting has been brought forward to Monday. # La réunion a été avancée à lundi.
draw up | rédiger, établir | ex=The lawyer drew up the contract. # L'avocat a rédigé le contrat.
fall through | tomber à l'eau | ex=Our vacation plans fell through. # Nos projets de vacances sont tombés à l'eau.
iron out | aplanir, régler | ex=We need to iron out a few details. # Nous devons régler quelques détails.
lay off | licencier (pour raisons économiques) | ex=The factory laid off two hundred workers. # L'usine a licencié deux cents ouvriers.
live up to | être à la hauteur de | ex=The movie didn't live up to the hype. # Le film n'a pas été à la hauteur de sa réputation.
phase out | supprimer progressivement | ex=The old model is being phased out. # L'ancien modèle est progressivement retiré.
pull through | s'en sortir, se rétablir | ex=The doctors think he'll pull through. # Les médecins pensent qu'il va s'en sortir.
zero in on | se concentrer sur, cibler | ex=Let's zero in on the main problem. # Concentrons-nous sur le problème principal.
mull over | réfléchir longuement à | ex=I need to mull it over before I decide. # Il faut que j'y réfléchisse avant de décider.
bank on | compter sur | ex=Don't bank on getting a raise this year. # Ne compte pas sur une augmentation cette année.
root out | éradiquer, débusquer | ex=The new director wants to root out corruption. # Le nouveau directeur veut éradiquer la corruption.
scrape by | s'en sortir de justesse | ex=They scrape by on one salary. # Ils s'en sortent tout juste avec un seul salaire.
stave off | repousser, éviter | ex=They took out a loan to stave off bankruptcy. # Ils ont pris un prêt pour éviter la faillite.
"""

# « adjectif | traduction | drapeaux » (gb=, ex=).
ADJECTIFS = """
acceptable | acceptable, tolérable
accurate | exact, qui correspond
aimless | sans but | ex=He spent the afternoon in aimless wandering. # Il a passé l'après-midi à errer sans but.
amateurish | d'amateur, maladroit
astonishing | stupéfiant
authoritative | déterminant, faisant autorité
backward | arriéré, en retard
bearable | supportable (perte)
brisk | vif, énergique | ex=We went for a brisk walk along the river. # Nous avons fait une marche rapide le long de la rivière.
casual | décontracté, désinvolte | ex=The dress code is casual on Fridays. # Le vendredi, la tenue est décontractée.
clear-cut | net, tranché
coarse | grossier, rêche | ex=The fabric feels coarse. # Le tissu est rêche au toucher.
communicative | communicatif | ex=He's not very communicative in the morning. # Il n'est pas très bavard le matin.
compelling | convaincant, irrésistible
conciliatory | conciliant
concise | concis | ex=Keep your answers short and concise. # Fais des réponses courtes et concises.
conditional | sous conditions, relatif
considerable | considérable
contrived | artificiel, forcé | ex=The ending of the movie felt contrived. # La fin du film paraissait forcée.
conventional | traditionnel, classique
creeping | insidieux, rampant
cryptic | cryptique, obscur
dainty | menu, délicat
damaged | défectueux, abîmé
depressing | accablant, pesant
disarming | désarmant | ex=She has a disarming smile. # Elle a un sourire désarmant.
disconcerting | déconcertant, étrange
dispensable | superflu, dont on peut se passer
disproportionate | disproportionné
disputed | litigieux, contesté
distorted | déformé, faussé | ex=The media gave a distorted picture of events. # Les médias ont donné une image déformée des événements.
disturbing | troublant, perturbant
divisive | clivant
down-to-earth | terre-à-terre, sans prétention
elaborate | élaboré, complexe
erratic | irrégulier, imprévisible | ex=His behavior has become erratic. # Son comportement est devenu imprévisible.
excessive | excessif | ex=The fine seems excessive. # L'amende paraît excessive.
exhaustive | exhaustif
far-fetched | saugrenu, hors de propos
far-reaching | de grande portée
faulty | défectueux | ex=The fire was caused by faulty wiring. # L'incendie a été causé par un câblage défectueux.
final | définitif
flawless | parfait, sans défaut | ex=Her English is flawless. # Son anglais est parfait.
foreseeable | prévisible, à vue
forward-looking | porteur d'avenir
fragmentary | fragmentaire
gripping | captivant | ex=It's a gripping thriller. # C'est un thriller captivant.
groundbreaking | pionnier, qui montre la voie
hair-raising | terrifiant | ex=We had a hair-raising drive through the mountains. # Nous avons fait un trajet terrifiant dans les montagnes.
half-hearted | sans conviction, à moitié
idiosyncratic | singulier, à sa façon
illuminating | éclairant
immature | immature | ex=Stop being so immature! # Arrête d'être aussi puéril !
impeccable | impeccable
improper | impropre, inadéquat
inaccessible | inaccessible ; fermé
inaccurate | inexact
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
level-headed | posé, pondéré | ex=She stayed level-headed during the crisis. # Elle est restée posée pendant la crise.
long-winded | prolixe, verbeux
low-maintenance | peu exigeant en entretien
makeshift | de fortune
manageable | maniable, gérable
mature | abouti, mûri
meaningful | significatif, parlant
measurable | mesurable
methodical | méthodique | ex=He's very methodical in his work. # Il est très méthodique dans son travail.
minor | minime, négligeable
moving | émouvant
nationwide | national, dans tout le pays | ex=The company has stores nationwide. # L'entreprise a des magasins dans tout le pays.
negligent | négligent
noticeable | sensible, perceptible
novel | nouveau, inédit
opaque | opaque | ex=The decision-making process is completely opaque. # Le processus de décision est complètement opaque.
oppressive | oppressant, angoissant
outmoded | anachronique, d'un autre temps
outrageous | scandaleux, extravagant | ex=The prices at this hotel are outrageous. # Les prix de cet hôtel sont scandaleux.
overarching | supérieur, englobant
overwhelmed | débordé, submergé | ex=I feel overwhelmed by all this work. # Je me sens submergé par tout ce travail.
patchy | lacunaire
pedantic | pointilleux, tatillon
pending | pendant (devant un tribunal)
peripheral | périphérique
permissible | admissible, autorisé
pithy | frappant, ramassé
profound | profond, en profondeur
proper | correct, convenable | ex=You need proper shoes for hiking. # Il te faut de vraies chaussures pour la randonnée.
proven | prouvé, éprouvé | ex=It's a proven method. # C'est une méthode éprouvée.
rapid | rapide | ex=The city went through rapid growth. # La ville a connu une croissance rapide.
resolute | résolu, déterminé | ex=She remained resolute in her decision. # Elle est restée ferme dans sa décision.
restrained | retenu, mesuré
revealing | instructif, révélateur
seamless | sans faille, complet
selective | sélectif | ex=The college is very selective. # L'université est très sélective.
shameful | honteux | ex=The way they treated him was shameful. # La façon dont ils l'ont traité était honteuse.
short-lived | éphémère
sketchy | sommaire, louche
sober | sobre, lucide | ex=He's been sober for two years. # Il ne boit plus depuis deux ans.
sobering | qui ramène sur terre, décevant
spotless | sans défaut, immaculé
steady | constant, régulier
stilted | guindé, compassé
striking | frappant
stringent | strict, rigoureux | ex=The rules are very stringent. # Les règles sont très strictes.
subordinate | de rang inférieur, subordonné
supposed | prétendu, soi-disant
symptomatic | symptomatique
tailor-made | sur mesure
telling | significatif, caractéristique
telltale | révélateur (malgré soi)
tentative | timide, hésitant
terse | lapidaire, laconique
tireless | infatigable | ex=She's a tireless volunteer. # C'est une bénévole infatigable.
tortuous | tortueux, sinueux (raisonnement)
touching | touchant, attendrissant
transferable | transférable | ex=Communication skills are transferable to any job. # Les compétences en communication sont utiles dans n'importe quel emploi.
trivial | insignifiant, sans importance
unbearable | insupportable
unchallenged | incontesté, sans rival
uncommon | peu usité
uncontroversial | unanimement admis
undeterred | imperturbable
undisputed | incontesté
unfit | inapte, impropre
unforgiving | sans indulgence, inflexible
unifying | fédérateur, qui rapproche
unlawful | illégal, contraire au droit
unproductive | stérile, peu productif
unproven | non prouvé
unresolved | en suspens, non tranché
unrestricted | illimité, sans restriction | ex=Members have unrestricted access to the gym. # Les membres ont un accès illimité à la salle de sport.
unsettled | instable, changeant
unsparing | sans complaisance, impitoyable
unsubstantiated | non attesté, sans preuve
unsuitable | inadapté | ex=The movie is unsuitable for children. # Le film ne convient pas aux enfants.
untenable | intenable | ex=The situation became untenable. # La situation est devenue intenable.
unwieldy | encombrant ; rébarbatif
unyielding | intransigeant
upcoming | à venir, à l'ordre du jour
usable | utilisable, exploitable
verifiable | vérifiable
void | caduc, sans objet
wasteful | dispendieux, prodigue
well-versed | chevronné, versé
worthwhile | qui en vaut la peine | ex=Volunteering is a worthwhile experience. # Le bénévolat est une expérience qui en vaut la peine.
adamant | catégorique, inflexible | ex=She was adamant that she had locked the door. # Elle était catégorique : elle avait fermé la porte à clé.
astute | perspicace, astucieux | ex=That was an astute observation. # C'était une remarque perspicace.
blatant | flagrant | ex=It was a blatant lie. # C'était un mensonge flagrant.
commendable | louable | ex=Her honesty is commendable. # Son honnêteté est louable.
complacent | trop sûr de soi, suffisant | ex=We can't afford to be complacent. # Nous ne pouvons pas nous permettre de nous reposer sur nos lauriers.
conducive | propice | ex=The noise isn't conducive to studying. # Le bruit n'est pas propice à l'étude.
conspicuous | voyant, remarquable | ex=He felt conspicuous in his bright suit. # Il se sentait voyant dans son costume criard.
daunting | intimidant, décourageant | ex=Moving to a new country is a daunting task. # S'installer dans un nouveau pays est une tâche intimidante.
detrimental | nuisible, préjudiciable | ex=Smoking is detrimental to your health. # Le tabac est nuisible à la santé.
diligent | assidu, consciencieux | ex=She's a diligent student. # C'est une élève assidue.
elusive | insaisissable | ex=Success remained elusive. # Le succès restait insaisissable.
eminent | éminent | ex=He's an eminent scientist. # C'est un éminent scientifique.
feasible | faisable, réalisable | ex=Is the plan feasible? # Le projet est-il réalisable ?
fickle | inconstant, capricieux | ex=New England weather is notoriously fickle. # Le temps en Nouvelle-Angleterre est réputé capricieux.
hectic | trépidant, mouvementé | ex=It's been a hectic week. # Ça a été une semaine mouvementée.
imminent | imminent | ex=A storm is imminent. # Une tempête est imminente.
inadvertent | involontaire | ex=It was an inadvertent mistake. # C'était une erreur involontaire.
inherent | inhérent | ex=Every investment has inherent risks. # Tout investissement comporte des risques inhérents.
intricate | complexe, minutieux | ex=The carpet has an intricate pattern. # Le tapis a un motif complexe.
lucrative | lucratif | ex=It's a very lucrative business. # C'est une affaire très lucrative.
meticulous | méticuleux | ex=He keeps meticulous records. # Il tient des registres méticuleux.
mundane | banal, ordinaire | ex=Even mundane tasks can be fun. # Même les tâches banales peuvent être amusantes.
notorious | tristement célèbre, notoire | ex=The road is notorious for accidents. # La route est tristement célèbre pour ses accidents.
ominous | menaçant, inquiétant | ex=Ominous clouds gathered over the bay. # Des nuages menaçants s'amoncelaient au-dessus de la baie.
paramount | primordial | ex=Safety is paramount. # La sécurité est primordiale.
pervasive | omniprésent | ex=The smell of coffee was pervasive. # L'odeur du café était omniprésente.
poignant | poignant | ex=It was a poignant moment. # C'était un moment poignant.
precarious | précaire | ex=They live in a precarious situation. # Ils vivent dans une situation précaire.
prevalent | répandu | ex=The disease is prevalent in tropical areas. # La maladie est répandue dans les régions tropicales.
prolific | prolifique | ex=Stephen King is a prolific writer. # Stephen King est un écrivain prolifique.
prominent | important, en vue | ex=She's a prominent lawyer in Boston. # C'est une avocate en vue à Boston.
prudent | prudent, avisé | ex=It would be prudent to wait. # Il serait prudent d'attendre.
ruthless | impitoyable | ex=He's a ruthless businessman. # C'est un homme d'affaires impitoyable.
scrupulous | scrupuleux | ex=She's scrupulous about details. # Elle est scrupuleuse sur les détails.
staunch | fervent, loyal | ex=He's a staunch supporter of the Red Sox. # C'est un fervent supporter des Red Sox.
tedious | fastidieux | ex=Filling out forms is tedious. # Remplir des formulaires est fastidieux.
tenuous | ténu, fragile | ex=The link between the two events is tenuous. # Le lien entre les deux événements est ténu.
unprecedented | sans précédent | ex=The city saw unprecedented snowfall. # La ville a connu des chutes de neige sans précédent.
wary | méfiant | ex=Be wary of strangers online. # Méfie-toi des inconnus en ligne.
cumbersome | encombrant, lourd | ex=The old system was slow and cumbersome. # L'ancien système était lent et lourd.
adverse | défavorable, indésirable | ex=The drug has few adverse effects. # Le médicament a peu d'effets indésirables.
apprehensive | appréhensif, inquiet | ex=I'm a little apprehensive about the interview. # J'appréhende un peu l'entretien.
arduous | ardu, pénible | ex=The climb was long and arduous. # L'ascension a été longue et ardue.
bleak | sombre, morne | ex=The future looks bleak. # L'avenir s'annonce sombre.
candid | franc | ex=Thank you for your candid answer. # Merci pour ta réponse franche.
cogent | convaincant | ex=She made a cogent argument. # Elle a avancé un argument convaincant.
compulsive | compulsif | ex=He's a compulsive liar. # C'est un menteur compulsif.
far-reaching | de grande portée | ex=The reform will have far-reaching consequences. # La réforme aura des conséquences de grande portée.
"""

# « adverbe | traduction | categorie | drapeaux ».
ADVERBES = """
abruptly | brusquement | Manière
at worst | au pire | Nuance
conversely | inversement | Liaison
demonstrably | de façon avérée | Nuance
equally | de la même façon | Liaison
furthermore | en outre | Liaison
incidentally | au fait, d'ailleurs | Liaison
instead | au lieu de cela | Liaison
literally | littéralement | Nuance
noticeably | sensiblement | Quantité
or rather | ou plutôt, respectivement | Liaison
specially | spécialement | Manière
understandably | on le comprend | Nuance
unexpectedly | à l'improviste | Manière
without exception | sans exception | Quantité
albeit | quoique, bien que | Liaison | ex=It was a success, albeit a small one. # Ce fut un succès, quoique modeste.
arguably | sans doute, on peut dire que | Nuance | ex=It's arguably the best pizza in Boston. # C'est sans doute la meilleure pizza de Boston.
henceforth | désormais | Temps | ex=Henceforth, all meetings will be online. # Désormais, toutes les réunions auront lieu en ligne.
inadvertently | par inadvertance | Manière | ex=I inadvertently deleted the file. # J'ai supprimé le fichier par inadvertance.
invariably | invariablement | Fréquence | ex=He's invariably late. # Il est invariablement en retard.
notwithstanding | néanmoins, malgré cela | Liaison | ex=The weather notwithstanding, the game went ahead. # Malgré le temps, le match a eu lieu.
readily | volontiers, facilement | Manière | ex=She readily agreed to help. # Elle a volontiers accepté d'aider.
virtually | pratiquement | Quantité | ex=The town was virtually empty. # La ville était pratiquement vide.
wholeheartedly | sans réserve | Manière | ex=I wholeheartedly agree with you. # Je suis entièrement d'accord avec toi.
undeniably | indéniablement | Affirmation | ex=She's undeniably talented. # Elle a indéniablement du talent.
overwhelmingly | massivement | Quantité | ex=Voters overwhelmingly rejected the proposal. # Les électeurs ont massivement rejeté la proposition.
ostensibly | en apparence, soi-disant | Doute | ex=He left early, ostensibly to catch a train. # Il est parti tôt, soi-disant pour prendre un train.
scarcely | à peine | Quantité | ex=I could scarcely believe my eyes. # J'avais du mal à en croire mes yeux.
momentarily | un instant ; (américain) dans un instant | Temps | ex=The doctor will be with you momentarily. # Le médecin sera avec vous dans un instant.
inherently | intrinsèquement | Manière | ex=There's nothing inherently wrong with the idea. # L'idée n'a rien de mauvais en soi.
implicitly | implicitement | Manière | ex=She trusts him implicitly. # Elle lui fait entièrement confiance.
profoundly | profondément | Quantité | ex=The experience profoundly changed him. # L'expérience l'a profondément changé.
markedly | nettement | Quantité | ex=Sales have improved markedly. # Les ventes se sont nettement améliorées.
increasingly | de plus en plus | Quantité | ex=It's becoming increasingly difficult to find an apartment. # Il devient de plus en plus difficile de trouver un appartement.
hitherto | jusqu'ici | Temps | ex=The letter reveals hitherto unknown facts. # La lettre révèle des faits jusqu'ici inconnus.
thereby | de ce fait, ainsi | Cause et conséquence | ex=He trained hard, thereby improving his time. # Il s'est beaucoup entraîné, améliorant ainsi son temps.
predominantly | principalement | Quantité | ex=The neighborhood is predominantly residential. # Le quartier est principalement résidentiel.
seemingly | apparemment | Doute | ex=The task was seemingly simple. # La tâche était apparemment simple.
subsequently | par la suite | Temps | ex=He was arrested and subsequently released. # Il a été arrêté puis relâché.
candidly | franchement | Manière | ex=Candidly, I think it's a bad idea. # Franchement, je pense que c'est une mauvaise idée.
"""

# « expression | traduction | categorie | exemple anglais | exemple francais ».
EXPRESSIONS = """
against the backdrop of | dans le contexte de | Discuter | Against the backdrop of the crisis the sum looks small. | Dans le contexte de la crise, la somme paraît faible.
as things stand | en l'état des choses | Discuter | As things stand, the law won't happen. | En l'état des choses, la loi ne verra pas le jour.
Dear Sir or Madam | Madame, Monsieur | Bavarder | Dear Sir or Madam, I am hereby applying for the position. | Madame, Monsieur, je vous adresse ma candidature pour ce poste.
for all the criticism | malgré toutes les critiques | Discuter | For all the criticism, the project improved a great deal. | Malgré toutes les critiques, le projet a amélioré bien des choses.
for the sake of completeness | par souci d'exhaustivité | Discuter | For the sake of completeness, let's mention the third option. | Par souci d'exhaustivité, mentionnons la troisième variante.
for want of | à défaut de | Discuter | For want of better proposals, the old plan stayed. | À défaut de meilleures propositions, on en est resté à l'ancien plan.
I can only agree | je ne peux qu'approuver | Donner son avis | I can only agree, that was long overdue. | Je ne peux qu'approuver, cela n'avait que trop tardé.
I find that far-fetched | je trouve cela tiré par les cheveux | Donner son avis | I find that far-fetched; there's no evidence for it. | Je trouve cela tiré par les cheveux, rien ne le prouve.
I take the view | je suis d'avis | Donner son avis | I take the view that we gave up too early. | Je suis d'avis que nous avons abandonné trop tôt.
I would be grateful if | je vous serais reconnaissant de | Bavarder | I would be grateful if you could send me the documents. | Je vous serais reconnaissant de bien vouloir m'envoyer les documents.
I'm completely with you | je te suis entièrement | Donner son avis | I'm completely with you, this can't go on. | Je te suis entièrement, cela ne peut pas continuer ainsi.
I'm getting in touch regarding | je vous contacte au sujet de | Bavarder | I'm getting in touch regarding your inquiry from Monday. | Je vous contacte au sujet de votre demande de lundi.
I'm inclined to think | je penche pour l'idée | Donner son avis | I'm inclined to think we should wait. | Je penche pour l'idée que nous devrions attendre.
I'm skeptical about it | je suis sceptique là-dessus | Donner son avis | I'm skeptical about it; the figures don't convince me. | Je suis sceptique là-dessus, les chiffres ne me convainquent pas.
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
that takes the cake | c'est le comble | Réagir | And now a fee too? That takes the cake. | Et maintenant des frais en plus ? C'est le comble.
that's a mystery to me | c'est un mystère pour moi | Réagir | How he managed it is a mystery to me. | Comment il y est arrivé, c'est un mystère pour moi.
that's a weight off my mind | cela m'ôte un poids | Réagir | She arrived safely — that's a weight off my mind. | Elle est bien arrivée — cela m'ôte un poids.
to be on the table | être sur la table (en discussion) | Discuter | Several options are still on the table. | Plusieurs options sont encore sur la table.
to cause offense | choquer, offenser | Tournures | The ad caused great offense. | La publicité a beaucoup choqué.
to exert influence | exercer une influence | Tournures | No one may exert influence on the verdict. | Personne ne doit exercer d'influence sur le jugement.
to exert pressure | exercer une pression | Tournures | Investors are exerting pressure on the board. | Les investisseurs exercent une pression sur la direction.
to fall behind | prendre du retard | Au quotidien | The construction has fallen months behind. | Le chantier a pris des mois de retard.
to fall into oblivion | tomber dans l'oubli | Tournures | The craft has almost fallen into oblivion. | Ce métier est presque tombé dans l'oubli.
to file a report | porter plainte | Au quotidien | After the break-in he filed a report. | Après le cambriolage, il a porté plainte.
to file an appeal | former un recours | Au quotidien | She filed an appeal against the dismissal. | Elle a formé un recours contre le licenciement.
to give credence to | prêter foi à | Tournures | One shouldn't give credence to the rumour. | Il ne faut pas prêter foi à cette rumeur.
to harbor doubts | nourrir des doutes | Tournures | I harbor doubts about his story. | J'ai des doutes sur sa version.
to lodge a complaint | déposer une réclamation | Au quotidien | The customer lodged a complaint. | Le client a déposé une réclamation.
to lodge an objection | faire opposition | Au quotidien | You can lodge an objection against the notice. | On peut faire opposition à cette décision.
to make compromises | accepter des compromis | Tournures | Anyone who negotiates has to make compromises. | Qui négocie doit accepter des compromis.
to make concessions | faire des concessions | Tournures | Both sides had to make concessions. | Les deux parties ont dû faire des concessions.
to meet with approval | recueillir l'adhésion | Tournures | The draft met with broad approval. | Le projet a recueilli une large adhésion.
to put into practice | mettre en pratique | Au quotidien | The idea was never put into practice. | L'idée n'a jamais été mise en pratique.
to put up resistance | opposer une résistance | Tournures | Local residents put up fierce resistance. | Les riverains ont opposé une résistance acharnée.
to seethe with anger | bouillir de rage | Réagir | After the call he was seething with anger. | Après l'appel, il bouillait de rage.
to state for the record | déclarer au procès-verbal | Au quotidien | The witness stated for the record that he had seen nothing. | Le témoin a déclaré au procès-verbal n'avoir rien vu.
to submit a proposal | soumettre une proposition | Tournures | She submitted a proposal to the council. | Elle a soumis une proposition au conseil.
to voice concerns | émettre des réserves | Tournures | Several members voiced concerns. | Plusieurs membres ont émis des réserves.
to voice criticism | formuler des critiques | Tournures | The association voiced sharp criticism of the draft. | La fédération a formulé de vives critiques sur le projet.
you've got me there | là, je sèche | Réagir | When the law takes effect? You've got me there. | Quand la loi entre en vigueur ? Là, je sèche.
a blessing in disguise | un mal pour un bien | Tournures | Losing that job was a blessing in disguise. | Perdre ce poste a été un mal pour un bien.
a far cry from | bien loin de | Discuter | This apartment is a far cry from our old one. | Cet appartement est bien loin de notre ancien.
to cut corners | bâcler, rogner sur la qualité | Tournures | Don't cut corners on safety. | Ne rogne pas sur la sécurité.
to play devil's advocate | se faire l'avocat du diable | Discuter | Let me play devil's advocate for a moment. | Laissez-moi me faire l'avocat du diable un instant.
to get the hang of | prendre le coup de main | Au quotidien | You'll get the hang of it after a few days. | Tu prendras le coup de main en quelques jours.
to go the extra mile | faire un effort supplémentaire | Tournures | She always goes the extra mile for her clients. | Elle en fait toujours plus pour ses clients.
to hit the ground running | être opérationnel tout de suite | Tournures | The new manager hit the ground running. | La nouvelle responsable a été opérationnelle tout de suite.
to jump on the bandwagon | suivre le mouvement | Tournures | Everyone jumped on the bandwagon. | Tout le monde a suivi le mouvement.
to keep a low profile | se faire discret | Tournures | After the scandal, he kept a low profile. | Après le scandale, il s'est fait discret.
to learn the ropes | apprendre les ficelles | Au quotidien | It takes a few weeks to learn the ropes. | Il faut quelques semaines pour apprendre les ficelles du métier.
to miss the boat | rater le coche | Tournures | If you don't apply now, you'll miss the boat. | Si tu ne postules pas maintenant, tu vas rater le coche.
on the fence | indécis | Donner son avis | I'm still on the fence about the move. | Je suis encore indécis à propos du déménagement.
once in a blue moon | tous les trente-six du mois | Au quotidien | We go to the movies once in a blue moon. | Nous allons au cinéma tous les trente-six du mois.
to pull one's weight | faire sa part | Tournures | Everyone on the team has to pull their weight. | Chacun dans l'équipe doit faire sa part.
to read between the lines | lire entre les lignes | Discuter | If you read between the lines, she's not happy. | Si on lit entre les lignes, elle n'est pas contente.
second nature | une seconde nature | Tournures | After a while, driving becomes second nature. | Au bout d'un moment, conduire devient une seconde nature.
to take with a grain of salt | prendre avec des pincettes | Discuter | Take his advice with a grain of salt. | Prends ses conseils avec des pincettes.
the tip of the iceberg | la partie émergée de l'iceberg | Discuter | These complaints are just the tip of the iceberg. | Ces plaintes ne sont que la partie émergée de l'iceberg.
under the weather | patraque | Réagir | I'm feeling a bit under the weather today. | Je suis un peu patraque aujourd'hui.
up in the air | en suspens, incertain | Discuter | Our plans are still up in the air. | Nos projets sont encore incertains.
when push comes to shove | quand il le faut vraiment | Discuter | When push comes to shove, you can count on him. | Quand il le faut vraiment, on peut compter sur lui.
a level playing field | des conditions égales pour tous | Discuter | The new rules create a level playing field. | Les nouvelles règles mettent tout le monde sur un pied d'égalité.
across the board | à tous les niveaux, pour tous | Discuter | Prices went up across the board. | Les prix ont augmenté partout.
back to square one | retour à la case départ | Réagir | The deal fell through, so we're back to square one. | L'accord a échoué, nous revoilà à la case départ.
to bend over backwards | se mettre en quatre | Tournures | They bent over backwards to help us. | Ils se sont mis en quatre pour nous aider.
to bite off more than one can chew | avoir les yeux plus gros que le ventre | Tournures | I bit off more than I could chew with this project. | J'ai eu les yeux plus gros que le ventre avec ce projet.
to burn the midnight oil | travailler tard dans la nuit | Au quotidien | She burned the midnight oil before the exam. | Elle a travaillé tard dans la nuit avant l'examen.
to cut to the chase | en venir au fait | Discuter | Let's cut to the chase: how much does it cost? | Venons-en au fait : combien ça coûte ?
to get the ball rolling | lancer les choses | Au quotidien | Let's get the ball rolling with a quick introduction. | Lançons les choses avec une brève présentation.
to make a long story short | pour faire court | Discuter | To make a long story short, we missed the flight. | Pour faire court, nous avons raté l'avion.
off the top of my head | de mémoire, comme ça | Discuter | Off the top of my head, I'd say about fifty people. | Comme ça, je dirais une cinquantaine de personnes.
to play it by ear | improviser | Au quotidien | We don't have a plan; we'll play it by ear. | Nous n'avons pas de plan, nous improviserons.
a rule of thumb | une règle empirique | Discuter | As a rule of thumb, save ten percent of your income. | En règle générale, épargne dix pour cent de tes revenus.
the last straw | la goutte d'eau qui fait déborder le vase | Réagir | His rudeness was the last straw. | Son impolitesse a été la goutte d'eau qui a fait déborder le vase.
to think outside the box | sortir des sentiers battus | Discuter | We need to think outside the box. | Il faut sortir des sentiers battus.
to hit the books | se mettre à réviser | Au quotidien | Exams start Monday, so I have to hit the books. | Les examens commencent lundi, je dois me mettre à réviser.
to have a lot on one's plate | avoir beaucoup à faire | Au quotidien | I can't help this week; I have a lot on my plate. | Je ne peux pas aider cette semaine, j'ai beaucoup à faire.
the ball is in your court | la balle est dans ton camp | Discuter | I've made my offer; the ball is in your court. | J'ai fait mon offre ; la balle est dans ton camp.
to sit on the fence | ne pas prendre parti | Donner son avis | You can't sit on the fence forever. | Tu ne peux pas rester neutre éternellement.
to steal the show | voler la vedette | Tournures | The little dog stole the show. | Le petit chien a volé la vedette.
to touch base | faire le point, reprendre contact | Au quotidien | Let's touch base next week. | Faisons le point la semaine prochaine.
in the same boat | dans la même galère | Réagir | Don't worry, we're all in the same boat. | Ne t'inquiète pas, nous sommes tous dans la même galère.
to break the ice | briser la glace | Bavarder | He told a joke to break the ice. | Il a raconté une blague pour briser la glace.
to call it quits | arrêter les frais | Au quotidien | After ten years, they decided to call it quits. | Au bout de dix ans, ils ont décidé d'arrêter.
"""
