# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du B2 anglais. SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que mots_a1.py et phrases_a1.py. BROUILLON : a faire relire par un anglophone.
"""

NIVEAU = 'B2'

# « verbe | traduction | drapeaux » ; les formes sont calculees (irreguliers.py).
VERBES = """
accelerate | accélérer
acclaim | acclamer
accommodate | accueillir, s'adapter à
accuse | accuser
advise against | déconseiller
afford | s'offrir, se permettre
aim for | viser, aspirer à
allocate | attribuer, affecter
allude to | faire allusion à
anchor | ancrer | ex=The boat was anchored in the bay. # Le bateau était ancré dans la baie.
appreciate | apprécier
arouse | susciter, éveiller | ex=His strange behavior aroused suspicion. # Son comportement étrange a éveillé les soupçons.
arrange for | faire en sorte que, organiser | ex=I've arranged for a taxi to pick you up. # J'ai organisé un taxi pour venir te chercher.
aspire | aspirer
associate | associer
attain | obtenir, acquérir
attribute to | attribuer (à une cause)
authorize | autoriser | ex=Only the manager can authorize a refund. # Seul le gérant peut autoriser un remboursement.
award | décerner, attribuer
back | soutenir, appuyer
base | fonder, étayer
blame | blâmer
boost | relancer, stimuler
break apart | se disloquer, se briser en deux
break off | interrompre, annuler
bring about | provoquer, produire (un effet)
build up | bâtir, mettre en place
burden | peser sur, charger
capture | capturer, saisir | ex=The photo captures the mood of the city. # La photo saisit l'ambiance de la ville.
catch up | rattraper son retard | ex=I missed a week of class, so I need to catch up. # J'ai manqué une semaine de cours, je dois rattraper mon retard.
challenge | défier
characterize | caractériser | ex=The region is characterized by long, cold winters. # La région se caractérise par des hivers longs et froids.
circumvent | contourner, éviter
combine | combiner, concilier
commemorate | commémorer
commission | commander (une œuvre), charger de
compose | composer, rédiger | ex=Mozart composed his first symphony at eight. # Mozart a composé sa première symphonie à huit ans.
comprehend | comprendre | ex=It's hard to comprehend the size of the universe. # Il est difficile de comprendre la taille de l'univers.
compromise | compromettre
conceal | dissimuler
concede | concéder, admettre
conceive | concevoir
consent | consentir
contest | contester (juridiquement)
convey | transmettre, exprimer
cooperate | coopérer
cope with | faire face à
correspond to | correspondre à
counteract | contrecarrer, contrer
cross-check | recouper
curb | endiguer, contenir
dampen | atténuer, freiner
debate | débattre
decline | reculer, diminuer
deduce | déduire
delay | faire traîner, retarder
deliberate | délibérer
detail | détailler
devalue | dévaluer
dictate | dicter | ex=The teacher dictated a short text. # Le professeur a dicté un petit texte.
diminish | amoindrir
disadvantage | désavantager
discard | rejeter, abandonner (une idée)
disclose | divulguer, rendre public
dismantle | démonter | ex=We dismantled the bed to move it. # Nous avons démonté le lit pour le déménager.
dispute | contester | ex=Nobody disputes the facts. # Personne ne conteste les faits.
dissuade | dissuader | ex=Nothing could dissuade her from leaving. # Rien n'a pu la dissuader de partir.
eliminate | éliminer | ex=Our team was eliminated in the first round. # Notre équipe a été éliminée au premier tour.
emerge | émerger, apparaître
enact | promulguer
ensure | garantir, assurer
entail | entraîner, impliquer
enter into | conclure (un accord) | ex=The two companies entered into a partnership. # Les deux entreprises ont conclu un partenariat.
establish | établir, fonder
evade | esquiver, se soustraire à | ex=He was accused of evading taxes. # Il a été accusé de fraude fiscale.
face | affronter, faire face à
favor | favoriser | ex=The referee seemed to favor the home team. # L'arbitre semblait favoriser l'équipe locale.
foster | favoriser, encourager | ex=Teachers should foster curiosity. # Les enseignants devraient encourager la curiosité.
free | libérer, délivrer
glimpse | entrevoir | ex=I glimpsed a deer in the woods. # J'ai aperçu un cerf dans les bois.
go deeper into | approfondir
grade | noter, qualifier
grant | accorder, décerner
group | regrouper
highlight | mettre en évidence
hold on to | garder, s'accrocher à | ex=Hold on to your ticket, you'll need it. # Garde ton billet, tu en auras besoin.
hold up | retenir, retarder
host | accueillir, animer
illustrate | illustrer
impair | nuire à, altérer
infer | déduire
inhibit | freiner, inhiber
initiate | engager, amorcer
interact | interagir
interpret | interpréter
intervene | intervenir
involve | impliquer
irrigate | irriguer
lack | manquer de
leak | fuir, divulguer
long for | désirer ardemment | ex=After a long winter, we long for the sun. # Après un long hiver, nous rêvons de soleil.
make up | constituer
mediate | servir de médiateur
mitigate | atténuer
monitor | surveiller, contrôler
monopolize | monopoliser | ex=He always monopolizes the conversation. # Il monopolise toujours la conversation.
name | nommer, désigner
note | remarquer, constater
object | objecter
offset | compenser
optimize | optimiser | ex=We need to optimize our website for phones. # Nous devons optimiser notre site pour les téléphones.
outsource | externaliser
oversee | superviser
permit | autoriser, admettre
postpone | reporter, décaler
predict | prédire
presume | présumer
prevail | s'imposer
prioritize | donner la priorité à | ex=You need to prioritize your health. # Tu dois donner la priorité à ta santé.
prohibit | interdire (officiellement)
provide for | prévoir
pursue | poursuivre, suivre
push through | imposer, faire aboutir (qch)
put into perspective | relativiser | ex=The accident put my problems into perspective. # L'accident m'a fait relativiser mes problèmes.
ratify | ratifier
reason | raisonner
reconcile | concilier, réconcilier | ex=It's hard to reconcile work and family life. # C'est difficile de concilier travail et vie de famille.
rectify | corriger, réparer (une erreur)
refer to | se référer (à qch)
refrain from | s'abstenir de
regret | regretter
reinforce | renforcer
relocate | déplacer, délocaliser
render | rendre
retrain | se reconvertir
review | recenser, chroniquer
rule out | exclure
sanction | sanctionner
seal | sceller
secure | sécuriser, assurer
segment | segmenter
set out | exposer, se mettre en route
settle down | s'installer, se ranger | ex=They want to settle down and have kids. # Ils veulent s'installer et avoir des enfants.
shape | marquer, façonner
shorten | raccourcir, écourter
shriek | hurler
sidestep | éluder, contourner | ex=The politician sidestepped the question. # Le politicien a éludé la question.
sketch | esquisser
skimp on | lésiner sur | ex=Don't skimp on safety. # Ne lésine pas sur la sécurité.
smash | briser, fracasser
soften | adoucir
sort out | résoudre, régler
sound out | sonder, explorer
specify | préciser
speed up | accélérer
split | fendre ; diviser
spoil | gâcher, gâter
stir | remuer
stress | souligner, insister sur
structure | structurer, articuler
surpass | surpasser, dépasser
suspect | soupçonner
suspend | suspendre, exposer à
tackle | s'attaquer à
take effect | prendre effet
take into account | prendre en compte | ex=Take the traffic into account. # Tiens compte de la circulation.
take on | assumer, embaucher
take over | reprendre, assumer
tighten | resserrer, durcir
turn to | se tourner vers
twist | tordre, déformer
underestimate | sous-estimer
underline | souligner (au sens figuré)
underpin | étayer
unfold | se dérouler, déplier | ex=She unfolded the map on the table. # Elle a déplié la carte sur la table.
validate | valider
vary | varier
waste | gaspiller
yield | produire, céder
"""

# « adjectif | traduction | drapeaux » (gb=, ex=).
ADJECTIFS = """
abrupt | brusque
abstract | abstrait
ambiguous | ambigu
ambivalent | ambivalent
ancestral | ancestral
arbitrary | arbitraire
artificial | artificiel
authentic | authentique
believable | vraisemblable
biased | partial, biaisé
bilateral | bilatéral
binding | contraignant
categorical | catégorique
chemical | chimique
coherent | cohérent
colloquial | familier
comprehensive | complet, exhaustif
conclusive | concluant
concrete | concret
conscious | conscient | ex=She's very conscious of her accent. # Elle est très consciente de son accent.
consistent | constant, cohérent | ex=Her work is consistent and reliable. # Son travail est régulier et fiable.
constitutional | constitutionnel
contradictory | contradictoire
controversial | controversé
counterproductive | contre-productif
demonstrable | démontrable
dependent | dépendant
dogmatic | dogmatique
dubious | douteux
efficient | efficace
eloquent | éloquent
emerging | émergent
empirical | empirique
endearing | attachant
ethical | éthique
exceptional | exceptionnel | ex=He's an exceptional student. # C'est un élève exceptionnel.
exemplary | exemplaire
global | global
harmonious | harmonieux
illegitimate | illégitime
immoral | immoral
impartial | impartial
inalienable | inaliénable
inappropriate | inapproprié
indigenous | autochtone
indispensable | indispensable
inflationary | inflationniste
innovative | innovant
intense | intense
intentional | intentionnel
inviolable | inviolable
irrational | irrationnel
irrelevant | non pertinent
irreversible | irréversible
justified | justifié
lawful | légitime, licite
left-handed | gaucher
legitimate | légitime
likely | probable
macroeconomic | macroéconomique
mandatory | obligatoire
marginal | marginal
meaningless | insignifiant
moderate | modéré
moral | moral
multifaceted | aux multiples facettes
neutral | neutre
non-binding | non contraignant
nuanced | nuancé
obsolete | obsolète
one-sided | unilatéral
ornate | orné, chargé
outstanding | exceptionnel, remarquable
painful | douloureux
paradoxical | paradoxal
parliamentary | parlementaire
partial | partiel, partial
permanent | permanent
plausible | plausible
pragmatic | pragmatique | ex=We need a pragmatic solution. # Il nous faut une solution pragmatique.
preliminary | préliminaire
premature | prématuré
primary | primaire
prior | préalable
productive | productif
pronounced | prononcé, marqué
provisional | provisoire
questionable | douteux
radical | radical | ex=The company made some radical changes. # L'entreprise a fait des changements radicaux.
random | aléatoire | ex=The winners are chosen at random. # Les gagnants sont tirés au sort.
regional | régional
repeated | répété
representative | représentatif
rigorous | rigoureux
secondary | secondaire
sensationalist | sensationnaliste
sociological | sociologique
subjective | subjectif
subtle | subtil
superfluous | superflu
systematic | systématique | ex=We need a more systematic approach. # Il nous faut une approche plus systématique.
thorough | minutieux, approfondi | ex=The doctor did a thorough examination. # Le médecin a fait un examen approfondi.
toxic | toxique
unambiguous | univoque, clair
unbiased | impartial | ex=A good journalist tries to be unbiased. # Un bon journaliste essaie d'être impartial.
unconscious | inconscient, évanoui | ex=He was unconscious for a few minutes. # Il est resté inconscient quelques minutes.
unconventional | non conventionnel
undeniable | indéniable
understated | sobre
unethical | contraire à l'éthique
unfounded | infondé
unintentional | involontaire
unique | unique
universal | universel
unjustified | injustifié
unlikely | improbable
vague | vague
versatile | polyvalent
viable | viable
vindictive | vindicatif
vivid | vif, frappant | ex=I have vivid memories of that summer. # J'ai des souvenirs très vifs de cet été-là.
well-founded | bien fondé, solide
"""

# « adverbe | traduction | categorie | drapeaux ».
ADVERBES = """
allegedly | prétendument | Doute
anyway | de toute façon | Liaison
at best | tout au plus | Quantité
at once | aussitôt | Temps
at times | par moments | Temps
basically | en gros | Liaison
broadly speaking | dans les grandes lignes | Liaison
by far | de loin | Quantité
categorically | catégoriquement | Manière
conscientiously | consciencieusement | Manière
consistently | avec constance, rigoureusement | Manière
continually | en permanence | Fréquence
curiously | curieusement | Liaison
decisively | avec détermination | Manière
downright | carrément | Quantité
elsewhere | ailleurs | Lieu
emphatically | avec insistance | Manière
essentially | essentiellement | Liaison
far too | par trop | Quantité
flatly | catégoriquement, sans appel | Manière
fortunately | heureusement | Liaison
frankly | franchement | Liaison
gently | doucement | Manière
gradually | peu à peu | Temps
hesitantly | avec hésitation | Manière
immensely | extraordinairement | Quantité
in depth | de manière approfondie | Manière
in essence | en substance | Manière | ex=In essence, the two plans are the same. # En substance, les deux projets sont les mêmes.
incredibly | incroyablement | Quantité
inevitably | forcément | Cause et conséquence
intermittently | par intermittence | Fréquence
logically | logiquement | Cause et conséquence
mainly | principalement | Liaison
meanwhile | toutefois, pendant ce temps | Liaison
nearly | quasiment | Quantité
necessarily | nécessairement | Cause et conséquence
persistently | avec ténacité | Manière
personally | personnellement | Liaison | ex=Personally, I prefer the train. # Personnellement, je préfère le train.
precisely | précisément | Liaison
presumably | probablement | Liaison
prudently | avec circonspection | Manière
regrettably | malheureusement | Liaison
reluctantly | à contrecœur | Manière
repeatedly | à maintes reprises | Fréquence
seemingly | à ce qu'il paraît | Liaison
so far | jusqu'à présent | Temps
specifically | spécifiquement, en particulier | Liaison
strictly speaking | à proprement parler | Liaison
tacitly | tacitement | Manière
temporarily | temporairement | Temps | ex=The museum is temporarily closed. # Le musée est temporairement fermé.
ultimately | au bout du compte | Cause et conséquence
unambiguously | sans ambiguïté | Manière
unavoidably | immanquablement | Cause et conséquence
upwards | vers le haut | Lieu
utterly | tout à fait, complètement | Quantité
"""

# « expression | traduction | categorie | exemple anglais | exemple francais ».
EXPRESSIONS = """
after all | après tout | Discuter | After all, it's his decision. | Après tout, c'est sa décision.
as is well known | comme chacun sait | Discuter | As is well known, practice is the best teacher. | Comme chacun sait, la pratique est le meilleur maître.
as long as | pourvu que | Discuter | He agrees as long as there's no argument. | Il accepte pourvu qu'on ne se dispute pas.
at the end of the day | au bout du compte | Discuter | At the end of the day we saved money. | Au bout du compte, nous avons économisé.
at the last minute | à la dernière minute | Au quotidien | The appointment was cancelled at the last minute. | Le rendez-vous a été annulé à la dernière minute.
because of | à cause de | Discuter | They closed because of the building work. | Ils ont fermé à cause des travaux.
by hook or by crook | coûte que coûte | Au quotidien | He wanted to push it through by hook or by crook. | Il voulait l'imposer coûte que coûte.
by the skin of one's teeth | de justesse | Au quotidien | We caught the train by the skin of our teeth. | Nous avons attrapé le train de justesse.
contrary to expectations | contrairement aux attentes | Discuter | Contrary to expectations, sales rose. | Contrairement aux attentes, le chiffre d'affaires a augmenté.
even so | malgré tout | Discuter | It's expensive; even so, he bought it. | C'est cher ; malgré tout, il l'a acheté.
from the ground up | de fond en comble | Au quotidien | The house was renovated from the ground up. | La maison a été rénovée de fond en comble.
from time to time | de temps en temps | Au quotidien | We see each other from time to time. | Nous nous voyons de temps en temps.
generally speaking | en général | Nuance | Generally speaking the process takes a month. | En général la démarche prend un mois.
head over heels | éperdument (amoureux) | Réagir | She fell head over heels in love with him. | Elle est tombée éperdument amoureuse de lui.
I share that view | je partage cet avis | Donner son avis | I share that view entirely. | Je partage cet avis sans réserve.
if I'm not mistaken | si je ne me trompe pas | Nuance | If I'm not mistaken, we've met before. | Si je ne me trompe pas, nous nous connaissons déjà.
in accordance with | conformément à | Discuter | In accordance with the law, notice must be given. | Conformément à la loi, il faut prévenir.
in any case | en tout cas | Nuance | In any case, I'll let you know tomorrow. | En tout cas, je te préviens demain.
in full swing | en plein essor, battant son plein | Au quotidien | The preparations are in full swing. | Les préparatifs battent leur plein.
in hindsight | rétrospectivement | Discuter | In hindsight the decision was right. | Rétrospectivement, la décision était juste.
in no time | en un tournemain | Au quotidien | That's done in no time. | C'est réglé en un tournemain.
in order to | afin de | Discuter | They met in order to clear it up. | Ils se sont réunis afin de l'éclaircir.
in principle | en principe | Donner son avis | In principle I agree. | En principe, je suis d'accord.
in spite of | malgré | Discuter | We went out in spite of the rain. | Nous sommes sortis malgré la pluie.
in the blink of an eye | en un clin d'œil | Tournures | He finished in the blink of an eye. | Il a fini en un clin d'œil.
in the course of | au cours de | Discuter | In the course of the renovation, everything was replaced. | Au cours de la rénovation, tout a été refait.
in the end | en fin de compte | Discuter | In the end only the result counts. | En fin de compte, seul le résultat compte.
in the long run | à long terme | Discuter | In the long run the investment pays off. | À long terme, l'investissement est rentable.
in theory | en théorie | Nuance | In theory the system runs itself. | En théorie le système fonctionne tout seul.
in view of | compte tenu de | Discuter | In view of the situation we remain cautious. | Compte tenu de la situation, nous restons prudents.
insofar as | dans la mesure où | Discuter | That holds insofar as the data are correct. | Cela vaut dans la mesure où les données sont exactes.
instead of | au lieu de | Discuter | We went by train instead of by car. | Nous y sommes allés en train au lieu de la voiture.
it all depends on | tout dépend de | Nuance | It all depends on the budget. | Tout dépend du budget.
it's obvious | cela va de soi | Discuter | It's obvious that we have to act. | Il va de soi que nous devons agir.
just in case | au cas où | Au quotidien | Take the umbrella just in case. | Prends le parapluie au cas où.
mind you | notons-le bien | Discuter | That applies, mind you, only to new customers. | Cela vaut, notons-le bien, uniquement pour les nouveaux clients.
more or less | plus ou moins | Discuter | It took us more or less an hour. | Nous avons mis plus ou moins une heure.
not entirely | pas tout à fait | Nuance | I'm not entirely convinced. | Je ne suis pas tout à fait convaincu.
not to mention | sans parler de | Discuter | It costs time, not to mention money. | Cela coûte du temps, sans parler de l'argent.
not to mince words | ne pas mâcher ses mots | Tournures | My grandmother doesn't mince her words. | Ma grand-mère ne mâche pas ses mots.
not to say | pour ne pas dire | Discuter | That was unwise, not to say negligent. | C'était imprudent, pour ne pas dire négligent.
not to sleep a wink | ne pas fermer l'œil | Tournures | I didn't sleep a wink all night. | Je n'ai pas fermé l'œil de la nuit.
on closer inspection | à y regarder de plus près | Discuter | On closer inspection that isn't true. | À y regarder de plus près, c'est faux.
on one's own initiative | de son propre chef | Au quotidien | She explored the city on her own initiative. | Elle a exploré la ville de son propre chef.
owing to | en raison de | Discuter | He was delayed owing to traffic. | Il a été retardé en raison du trafic.
pleased to meet you | ravi de faire votre connaissance | Bavarder | Pleased to meet you, Mr. Berger. | Ravi de faire votre connaissance, monsieur Berger.
quite simply | purement et simplement | Discuter | That is quite simply wrong. | C'est purement et simplement faux.
sooner or later | tôt ou tard | Au quotidien | Sooner or later we'll have to move. | Tôt ou tard, nous devrons déménager.
thanks to | grâce à | Discuter | We got there thanks to your map. | Nous sommes arrivés grâce à ta carte.
that doesn't change the fact | cela n'y change rien | Discuter | That doesn't change the fact that the deadline applies. | Cela n'y change rien : le délai s'applique.
that said | cela dit | Nuance | That said, there's another problem. | Cela dit, il y a un autre problème.
that's a matter of opinion | c'est une question de point de vue | Donner son avis | Whether that's beautiful is a matter of opinion. | Savoir si c'est beau est une question de point de vue.
that's another story | c'est une autre histoire | Donner son avis | Whether it's worth it is another story. | Savoir si cela en vaut la peine est une autre histoire.
the be-all and end-all | l'essentiel, la clé | Discuter | Regular practice is the be-all and end-all. | S'exercer régulièrement, c'est l'essentiel.
the worst is yet to come | le pire reste à venir | Réagir | Don't celebrate too soon, the worst is yet to come. | Ne te réjouis pas trop vite, le pire reste à venir.
there's no denying it | on ne peut le nier | Donner son avis | The effort was great, there's no denying it. | L'effort a été considérable, on ne peut le nier.
there's no way around it | on ne peut pas y couper | Donner son avis | We have to save, there's no way around it. | Nous devons économiser, on ne peut pas y couper.
there's nothing to add | il n'y a rien à ajouter | Donner son avis | Well said — there's nothing to add. | Bien dit — il n'y a rien à ajouter.
to add up | s'accumuler, finir par coûter cher | Tournures | Travel costs really add up. | Les frais de voyage finissent par coûter cher.
to attract attention | être remarqué | Tournures | His study attracted international attention. | Son étude a été remarquée à l'international.
to back someone up | soutenir quelqu'un | Réagir | The team backed her up. | L'équipe l'a soutenue.
to backfire | avoir l'effet inverse | Tournures | The plan backfired. | Le plan a eu l'effet inverse.
to backtrack | faire volte-face | Discuter | The party backtracked. | Le parti a fait volte-face.
to be a drag | être barbant | Tournures | The meeting was a drag. | La réunion était barbante.
to be a piece of cake | être du gâteau | Tournures | The exam was a piece of cake. | L'examen a été du gâteau.
to be a thorn in the side | être une épine dans le pied | Réagir | The new building is a thorn in the neighbours' side. | Le nouveau bâtiment est une épine dans le pied des voisins.
to hold down the fort | tenir la boutique | Tournures | She's holding down the fort while the boss is away. | Elle tient la boutique pendant l'absence de la patronne.
to be in the bag | être dans la poche | Au quotidien | The contract is finally in the bag. | Le contrat est enfin dans la poche.
to be off one's rocker | être complètement fou | Tournures | He's off his rocker, but he's great. | Il est complètement fou, mais il est génial.
to be over the moon | être fou de joie | Réagir | The children were completely over the moon. | Les enfants étaient fous de joie.
to be over the worst | avoir passé le plus dur | Réagir | After the operation she's over the worst. | Après l'opération, elle a passé le plus dur.
to be reflected in | se traduire par | Tournures | The success is reflected in the figures. | Le succès se traduit par les chiffres.
to be stumped | ne pas piger | Réagir | With this task I'm completely stumped. | Sur cet exercice, je ne pige vraiment rien.
to be stunned | tomber des nues | Réagir | When I heard that I was stunned. | Quand j'ai entendu ça, je suis tombé des nues.
to be under pressure | être sous pression | Réagir | The team has been under pressure for weeks. | L'équipe est sous pression depuis des semaines.
to be worth it | valoir la peine | Au quotidien | The trip is worth it. | Le voyage vaut la peine.
to beat around the bush | tourner autour du pot | Tournures | Answer the question and don't beat around the bush. | Réponds et ne tourne pas autour du pot.
to bite one's tongue | se mordre la langue | Réagir | I had to bite my tongue. | J'ai dû me mordre la langue.
to bite the bullet | avaler la pilule | Réagir | We have to bite the bullet and pay. | Il faut avaler la pilule et payer.
to bury one's head in the sand | faire l'autruche | Réagir | Burying your head in the sand doesn't help. | Faire l'autruche n'aide en rien.
to call into question | remettre en question | Donner son avis | Nobody calls his competence into question. | Personne ne remet en question sa compétence.
to call the shots | faire la loi | Tournures | She's the one who calls the shots here. | Ici c'est elle qui fait la loi.
to carry weight | peser dans la balance | Discuter | This point hardly carries any weight. | Ce point pèse à peine dans la balance.
to come into force | entrer en vigueur | Tournures | The law comes into force in January. | La loi entre en vigueur en janvier.
to come into play | entrer en jeu | Tournures | This is where his experience comes into play. | C'est là que son expérience entre en jeu.
to cost a fortune | coûter une fortune | Tournures | The rent costs a fortune. | Le loyer coûte une fortune.
to cost an arm and a leg | coûter les yeux de la tête | Tournures | The apartment costs an arm and a leg. | L'appartement coûte les yeux de la tête.
to draw a conclusion | tirer une conclusion | Discuter | What conclusion can we draw from this? | Quelle conclusion pouvons-nous en tirer ?
to get cold feet | se dégonfler | Réagir | Just before signing he got cold feet. | Juste avant de signer, il s'est dégonflé.
to get one's act together | se bouger | Tournures | You need to get your act together. | Tu dois te bouger.
to get out of hand | déraper, échapper à tout contrôle | Réagir | The costs got completely out of hand. | Les coûts ont complètement dérapé.
to get things back on track | remettre les choses sur les rails | Au quotidien | The new manager got things back on track. | Le nouveau directeur a remis les choses sur les rails.
to get to the point | aller droit au but | Tournures | Let's get to the point — how much is it? | Allons droit au but, combien ça coûte ?
to give the cold shoulder | battre froid à quelqu'un | Réagir | Since the argument she's given him the cold shoulder. | Depuis la dispute, elle lui bat froid.
to give the impression | donner l'impression | Tournures | That gives the impression of arbitrariness. | Cela donne l'impression d'arbitraire.
to go down well | être bien accueilli | Tournures | The idea went down very well with customers. | L'idée a été très bien accueillie par les clients.
to have no clue | n'avoir aucune idée | Tournures | I have no clue where it is. | Je n'ai aucune idée d'où il est.
to have one's back to the wall | être dos au mur | Réagir | The company has its back to the wall. | L'entreprise est dos au mur.
to have one's head in the clouds | être dans la lune | Tournures | Sorry, my head was in the clouds. | Pardon, j'étais dans la lune.
to hit the nail on the head | taper dans le mille | Tournures | You hit the nail on the head with that idea. | Tu as tapé dans le mille avec cette idée.
to jog someone's memory | mettre sur la voie, rafraîchir la mémoire | Réagir | May I jog your memory? | Puis-je te rafraîchir la mémoire ?
to jump in at the deep end | se jeter à l'eau | Réagir | On his first day he had to jump in at the deep end. | Le premier jour de travail, il a dû se jeter à l'eau.
to keep one's fingers crossed | croiser les doigts | Réagir | I'm keeping my fingers crossed for you tomorrow! | Je croise les doigts pour toi demain !
to keep one's head above water | se maintenir à flot | Au quotidien | The business is just keeping its head above water. | L'entreprise se maintient tout juste à flot.
to lay claim to | revendiquer | Tournures | Both sides lay claim to the territory. | Les deux camps revendiquent le territoire.
to make a clean sweep | faire table rase | Au quotidien | It's time to make a clean sweep. | Il est temps de faire table rase.
to make ends meet | joindre les deux bouts | Au quotidien | On this salary you can hardly make ends meet. | Avec ce salaire, on peine à joindre les deux bouts.
to meet with resistance | se heurter à une résistance | Tournures | The proposal met with fierce resistance. | La proposition s'est heurtée à une vive résistance.
to prove to be | s'avérer être | Tournures | The idea proved to be right. | L'idée s'est avérée juste.
to pull out all the stops | remuer ciel et terre | Au quotidien | She pulled out all the stops to help. | Elle a remué ciel et terre pour aider.
to pull someone's leg | se moquer de quelqu'un | Tournures | Don't pull my leg. | Ne te moque pas de moi.
to put a stop to | mettre un terme à | Tournures | We need to put a stop to this. | Il faut mettre un terme à cela.
to put it in a nutshell | pour résumer l'essentiel | Discuter | To put it in a nutshell: money is missing. | Pour résumer l'essentiel : il manque de l'argent.
to put it mildly | c'est le moins qu'on puisse dire | Discuter | That was, to put it mildly, unwise. | C'était maladroit, c'est le moins qu'on puisse dire.
to put on the back burner | mettre en veilleuse | Au quotidien | We've put the project on the back burner. | Nous avons mis le projet en veilleuse.
to put your cards on the table | jouer cartes sur table | Tournures | Let's put our cards on the table. | Jouons cartes sur table.
to put your foot in it | faire une gaffe | Tournures | I put my foot in it in front of everyone. | J'ai fait une gaffe devant tout le monde.
to remain silent | garder le silence | Réagir | He remains silent about the accusations. | Face aux accusations, il garde le silence.
to stay on the ball | ne pas lâcher | Au quotidien | Stay on the ball, you're almost done. | Ne lâche pas, tu as presque fini.
to sweep under the rug | passer sous silence | Discuter | This problem mustn't be swept under the rug. | On ne doit pas passer ce problème sous silence.
to take a stand | prendre position | Donner son avis | The company hasn't taken a stand on this yet. | L'entreprise n'a pas encore pris position là-dessus.
to take account of | tenir compte de | Tournures | The plan takes account of the new rules. | Le plan tient compte des nouvelles règles.
to take for granted | tenir pour acquis | Tournures | Don't take it for granted. | Ne le tiens pas pour acquis.
to take into consideration | prendre en considération | Tournures | We're taking other solutions into consideration too. | Nous prenons aussi d'autres solutions en considération.
to take stock | faire le bilan | Tournures | At the end of the year we take stock. | En fin d'année, nous faisons le bilan.
to throw in the towel | jeter l'éponge | Tournures | Don't throw in the towel just yet. | Ne jette pas l'éponge tout de suite.
to tighten one's belt | se serrer la ceinture | Au quotidien | This year we have to tighten our belts. | Cette année, nous devons nous serrer la ceinture.
to tip the scales | faire pencher la balance | Tournures | In the end the price tipped the scales. | C'est le prix qui a finalement fait pencher la balance.
to turn a blind eye | fermer les yeux (sur qch) | Tournures | This time I'll turn a blind eye. | Cette fois, je ferme les yeux.
to turn things around | redresser la barre | Au quotidien | In the last quarter she turned things around. | Au dernier trimestre, elle a redressé la barre.
to work hand in hand | travailler main dans la main | Tournures | The two departments work hand in hand. | Les deux services travaillent main dans la main.
up to a point | jusqu'à un certain point | Nuance | You're right up to a point. | Tu as raison jusqu'à un certain point.
with all due respect | avec tout le respect que je vous dois | Discuter | With all due respect, I see it differently. | Avec tout le respect que je vous dois, je vois cela autrement.
"""
