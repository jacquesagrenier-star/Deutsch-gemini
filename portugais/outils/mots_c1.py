# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du C1 portugais. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que mots_a1.py et phrases_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'C1'

# « infinitif | traduction | phrase | sa traduction | drapeaux » (formes : irreguliers.py).
VERBES = """
advertir | exhorter, rappeler à l'ordre | Ele foi advertido duas vezes. | On l'a rappelé à l'ordre deux fois.
advertir formalmente | mettre en demeure, adresser un avertissement | O empregador o adverte por escrito. | L'employeur lui adresse un avertissement écrit.
afetar | éprouver, mettre à mal | O estresse afetou a saúde dele. | Le stress a eu un effet sur sa santé.
afirmar com insistência | protester de, assurer avec insistance | Ela afirmou repetidas vezes que não sabia de nada. | Elle a affirmé et réaffirmé n'avoir rien su.
afrouxar | assouplir, desserrer | Ele afrouxou o parafuso meia volta. | Il desserra la vis d'un demi-tour.
agravar-se | exacerber, radicaliser | A situação agrava-se dia após dia. | La situation s'aggrave de jour en jour. | pron
aguentar firme | s'accrocher, serrer les dents | Nos primeiros meses é preciso de aguentar firme. | Les premiers mois, il faut serrer les dents.
ajudar a construir | contribuer à façonner | Os alunos ajudam a decorar a sala. | Les élèves contribuent à aménager la salle.
alastrar-se | s'étendre, gagner | O fogo alastra-se para o sítio vizinho. | Le feu gagne la ferme voisine. | pron
amolecer | assouplir, amollir | A chuva amoleceu o solo. | La pluie détrempait le sol.
andar junto com | aller de pair avec | A reforma veio junto com cortes. | La réforme s'accompagnait de coupes.
animar | remonter le moral | Às vezes uma ligação anima mais do que um conselho. | Un appel remonte parfois plus le moral qu'un conseil.
apalpar | palper, tâter, explorer | O médico apalpou a barriga. | Le médecin a palpé le ventre.
apaziguar | arbitrer, concilier | Ela apaziguou os ânimos com voz calma. | Elle apaisait d'une voix calme.
aperfeiçoar | affiner, raffiner | Aperfeiçoamos o processo passo a passo. | Nous affinons le procédé pas à pas.
apurar | établir, déterminer | Ainda estamos a apurar quem é o responsável. | Nous cherchons encore à établir qui est compétent.
camuflar | camoufler, masquer | A construção estava camuflada como celeiro. | La construction était camouflée en grange.
carregar nos ombros | prendre sur ses épaules, assumer | Eu carregaria o telemóvel antes de sair. | Moi, je chargerais le téléphone avant de partir.
causar estranheza | déconcerter, choquer | O tom dele causa-me estranheza. | Son ton me déconcerte.
cimentar | figer, bétonner | A decisão cimentou a divisão. | La décision a figé la division.
cobrar | rappeler à l'ordre, relancer (un paiement) | A companhia de energia cobra depois de quatro semanas. | Les services municipaux relancent au bout de quatre semaines.
comover profundamente | remuer, bouleverser | A lembrança o comoveu profundamente. | Le souvenir le bouleversait.
concordar com | abonder dans le sens de, approuver | Nisso só posso concordar com ela. | Là, je ne peux que l'approuver.
conjecturar | conjecturer, présumer | Só se pode especular por que ele foi embora. | On ne peut que conjecturer pourquoi il est parti. | ex?
consternar | consterner, bouleverser | A notícia consterna todos os funcionários. | La nouvelle consterne tout le personnel.
contextualizar | classer, situer | É preciso de contextualizar o número. | Il faut situer ce chiffre dans son contexte.
contrapor | opposer (un argument) | Ele não há nada a contrapor a isso. | Il n'a rien à y opposer.
dar asas | donner des ailes, stimuler | Isso daria asas a qualquer um. | Cela donnerait des ailes à n'importe qui.
dar continuidade | poursuivre, reprendre le flambeau | Ela dá continuidade ao consultório do pai. | Elle poursuit le cabinet de son père.
dar meia-volta | faire demi-tour, inverser | Com este tempo vamos dar meia-volta. | Par ce temps, nous faisons demi-tour.
dar palpite | avoir voix au chapitre | Nesta questão todos querem dar palpite. | Sur cette question, tous veulent avoir voix au chapitre.
dar peso a | pondérer, hiérarchiser | Damos mais peso à experiência do que às notas. | Nous pondérons l'expérience plus fortement que les notes.
dar resultado | porter ses fruits, servir à quelque chose | O esforço deu resultado no final. | L'effort a fini par porter ses fruits.
deixar boquiaberto | stupéfier, épater | A solução simples deixa todos boquiabertos. | La solution simple stupéfie tout le monde.
deixar claro | mettre les choses au clair | Quero deixar uma coisa clara. | Je voudrais mettre une chose au clair.
deixar de existir | disparaître, être supprimé | Com a nova regra a taxa deixa de existir. | Avec la nouvelle règle, la taxe disparaît.
deixar de fora | laisser de côté, exclure | Hoje vamos deixar esta questão de fora. | Nous laissons cette question de côté aujourd'hui.
delimitar | circonscrire, restreindre | Eu delimitaria isso com mais rigor. | Je délimiterais cela plus nettement.
derivar | déduire, faire dériver | Ele derivava tudo de uma única frase. | Il déduisait tout d'une seule phrase.
desanimar | décourager | O primeiro fracasso desanima muita gente. | Le premier échec en décourage beaucoup.
desaprovar | désapprouver | A diretoria desaprova este procedimento. | Le comité désapprouve cette manière de faire.
desarmar | désamorcer, atténuer | Uma frase bastou para amenizar a situação. | Une phrase a suffi à désamorcer la situation. | ex?
desbotar | déteindre (au propre et au figuré) | A serenidade dele contagia toda a equipa. | Son calme déteint sur toute l'équipe. | ex?
desembocar | déboucher sur, se jeter dans | O debate geralmente desemboca na mesma briga. | Le débat débouche le plus souvent sur la même dispute.
desescalar | désamorcer, faire baisser la tension | Um tom calmo muitas vezes acalma mais do que argumentos. | Un ton calme désamorce souvent plus que des arguments. | ex?
desgastar | user, miner | A longa espera desgasta a família. | La longue attente mine la famille.
desviar da finalidade | détourner de sa destination | Eu não desviaria isso da sua finalidade. | Je ne détournerais pas une chose pareille de son usage.
desviar-se | s'écarter, dévier | Na África viver-se-iam coisas bem diferentes. | En Afrique, on vivrait de tout autres choses. | pron
discutir a fundo | discuter en détail, débattre de | Naquela época discutiam-se questões bem diferentes. | À l'époque, on débattait de tout autres questions.
disfarçar | camoufler, dissimuler | A pintura só disfarça as rachaduras. | La peinture ne fait que camoufler les fissures.
dispersar-se | s'éparpiller, se disperser | Com tantas ideias é fácil dispersar-se. | On s'éparpille facilement avec autant d'idées. | pron
disponibilizar | mettre à disposition | O estado disponibiliza os recursos. | Le Land met les moyens à disposition.
dissipar | dissiper (des doutes) ; distraire | Uma olhada no processo dissipa qualquer dúvida. | Un coup d'œil au dossier dissipe tout doute.
divagar | digresser, s'éloigner du sujet | A palestra divagou várias vezes. | L'exposé s'est égaré plusieurs fois.
dourar a pílula | enjoliver, présenter sous un jour favorable | Eu não douraria a pílula. | Je n'enjoliverais rien là-dedans.
encaixar | encaisser sans broncher | Ele aguenta críticas surpreendentemente bem. | Il encaisse la critique étonnamment bien. | ex?
encaminhar | transmettre, faire suivre | Vou encaminhar o pedido ao departamento responsável. | Je transmets la demande au service compétent.
encobrir | étouffer, dissimuler | Eu não encobriria nada. | Je n'étoufferais rien.
enfeitar | enjoliver, broder | Ele enfeita todas as histórias. | Il enjolive chaque histoire.
entregar depois | fournir ultérieurement | Por favor, entregue depois os comprovantes que faltam. | Veuillez fournir les justificatifs manquants ultérieurement.
enxugar | resserrer, alléger | Enxugamos o processo em vinte minutos. | Nous resserrons le déroulement de vingt minutes.
errar | manquer, rater | Acho que viramos na rua errada. | Je crois que nous avons tourné dans la mauvaise rue.
esboçar-se | amorcer, s'esquisser | Sem a horta alimentar-nos-íamos pior. | Sans le potager, nous nous nourririons moins bien. | pron
esmorecer | s'essouffler, retomber | Depois de dois meses o interesse esmorece. | Au bout de deux mois, l'intérêt retombe.
esquadrinhar | passer au crible, radiographier |  |  | ex=?
estar por vir | être imminent | A prova estava bem próxima. | L'examen était tout proche.
estar suspenso | être suspendu, reposer | O processo fica suspenso até o laudo. | La procédure est suspendue jusqu'à l'expertise.
estender-se demais | s'étendre à l'excès | Na introdução ele estende-se demais. | Dans l'introduction, il s'étend trop.
estudar intensamente | bachoter, potasser | Ela estudou fórmulas até de manhã. | Elle bûchait des formules jusqu'au matin.
esvaziar-se | s'enliser, tourner court | A iniciativa esvaziou-se depois de dois anos. | L'initiative s'est enlisée au bout de deux ans. | pron
etiquetar | étiqueter, annoter | Todas as caixas estão etiquetadas. | Toutes les caisses sont étiquetées.
expirar | expirer, arriver à échéance | O subsídio termina no fim do ano. | L'aide arrive à échéance à la fin de l'année. | ex?
falsificar | falsifier, contrefaire | Ele falsifica a assinatura do pai. | Il falsifie la signature de son père.
fazer sentido | paraître évident, convaincre | Isso não faz sentido para mim. | Cela ne me paraît pas évident.
ficar abaixo de | rester en dessous de | O valor fica bem abaixo do limite. | La valeur reste nettement sous la limite.
ficar para trás | décrocher, retomber | Sem investimentos a região fica para trás. | Sans investissements, la région décroche.
gravar na memória | graver dans la mémoire | Uma imagem grava-se melhor do que uma lista. | Une image se grave mieux qu'une liste.
herdar de | hériter de, prendre la succession de | A filha herda a empresa. | La fille hérite de l'entreprise.
igualar | revenir à égalité, rattraper | Ela igualou no ano passado. | Elle égalisa l'an dernier.
incluir no cálculo | prévoir dans le calcul, tenir compte de | Eu incluiria uma margem de segurança. | Je prévoirais une marge.
infiltrar-se | noyauter, infiltrer | O grupo foi infiltrado por dentro. | Le groupe a été noyauté de l'intérieur. | pron
inserir | insérer, intégrer | Inserimos um parágrafo neste ponto. | Nous insérons un paragraphe à cet endroit.
insistir na pergunta | relancer, creuser (une question) | A jornalista insiste com o ministro. | La journaliste relance le ministre.
instalar-se | s'installer (une mauvaise habitude) ; démolir | Isso instalar-se-ia rápido. | Cela s'installerait vite. | pron
interiorizar | intérioriser, s'approprier | Ele interiorizou totalmente essa atitude. | Il a complètement intériorisé cette attitude.
intitular | intituler | Que título damos ao capítulo? | Comment intitulons-nous le chapitre ? | ex?
irradiar | rayonner, diffuser | O forno irradiava calor. | Le poêle dégageait de la chaleur.
minimizar | minimiser, banaliser | O relatório minimiza os riscos. | Le rapport minimise les risques.
mudar a destinação | réaffecter (un lieu, un fonds) | Eu mudaria a função da sala. | Je changerais l'affectation de la pièce.
mudar de rumo | changer de cap, virer | Depois das críticas o partido muda de rumo. | Après les critiques, le parti change de cap.
numerar | numéroter | Por favor, numere as páginas em sequência. | Veuillez numéroter les pages en continu.
omitir | taire, passer sous silence | Ele omite a parte mais importante. | Il tait la partie la plus importante.
pagar-se | amortir, rentabiliser | O sistema paga-se em sete anos. | L'installation s'amortit en sept ans. | pron
parafrasear | paraphraser, contourner par une périphrase | Cite ou parafraseie, mas indique a fonte. | Citez ou paraphrasez, mais nommez la source.
paralisar | paralyser | O medo de errar paralisa a equipa toda. | La peur de l'erreur paralyse toute l'équipe.
participar das decisões | codécider, participer aux décisions | A comissão de funcionários participa das decisões de contratação. | Le comité d'entreprise codécide des embauches.
premiar | distinguer, récompenser | A câmara municipal premia três projetos por ano. | La ville récompense chaque année trois projets.
pressentir | pressentir, deviner | Ela já pressentia a resposta. | Elle devinait déjà la réponse.
pressionar | presser, pousser | Os credores o pressionam há meses. | Les créanciers le harcèlent depuis des mois.
pressupor | présupposer, exiger comme condition | Ele simplesmente pressupôs que todos estavam a saber. | Il a simplement présumé que tout le monde était au courant.
prorrogar | prolonger | Prorrogamos o contrato por dois anos. | Nous prolongeons le contrat de deux ans.
pôr em dúvida | mettre en doute | Ela pôs o método em dúvida. | Elle mettait la méthode en doute.
ralar nos estudos | bûcher, bosser (des révisions) | No fim de semana ralamos na gramática. | Le week-end, on bûche la grammaire.
reafirmar | réaffirmer, confirmer avec force | Ela reafirma o compromisso mais uma vez por escrito. | Elle réaffirme son engagement une fois de plus par écrit.
reajustar | réajuster | Ela reajustou os valores. | Elle réajustait les valeurs.
recorrer a | faire appel à, se référer à | Para a comparação recorremos a dados mais antigos. | Pour la comparaison, nous nous référons à des données plus anciennes.
recuar | faire marche arrière | Depois das críticas a empresa recua. | Après les critiques, l'entreprise fait marche arrière.
recuperar terreno | combler un retard | Ela recuperou terreno no segundo semestre. | Elle rattrapait au second semestre.
redigir por extenso | rédiger en toutes lettres | Os tópicos ainda precisam de ser redigidos por extenso. | Les notes doivent encore être rédigées en toutes lettres.
refrescar | rafraîchir (des connaissances) | Antes da viagem vou refrescar o meu espanhol. | Avant le voyage, je rafraîchis mon espagnol.
registrar em ata | consigner, dresser le procès-verbal | Quem faz a ata da reunião? | Qui rédige le procès-verbal de la séance ?
remanejar | réaffecter, redéployer | Remanejamos recursos de A para B. | Nous réaffectons des moyens de A vers B.
remeter a | renvoyer à ; expulser | O texto remete a três estudos mais antigos. | Le texte renvoie à trois études plus anciennes.
renegociar | renégocier | Ainda temos de renegociar o preço. | Nous devons renégocier le prix.
reorganizar | réorganiser, permuter | Trocamos os dois capítulos de lugar. | Nous intervertissons les deux chapitres. | ex?
repensar | changer sa façon de penser | Aqui precisamos de repensar tudo. | Ici, il nous faut repenser fondamentalement.
repercutir | se répercuter, se faire sentir | O efeito só repercutiu tarde. | L'effet ne s'est fait sentir que tardivement.
replicar | répliquer, rétorquer | Ela responde a isso com uma frase só. | Elle n'y réplique qu'une phrase. | ex?
requerer | demander officiellement, déposer une demande | Ela solicita a prorrogação do visto. | Elle demande une prolongation du visa. | ex?
responder por | répondre de, se porter garant | Ele responde pelo seu pessoal. | Il répond de ses gens.
revogar | révoquer, se rétracter | O banco revogou a aprovação. | La banque révoqua son accord.
sair do controle | déborder, prendre des proportions excessives | A discussão sempre sai do controle. | La discussion déborde à chaque fois.
seguir o exemplo | emboîter le pas, suivre | Dois países seguiram o exemplo. | Deux pays ont suivi le mouvement.
ser devido a | revenir de droit, être dû | O primeiro lugar era dela por mérito. | La première place lui est revenue de droit.
ser fiador | se porter garant | Ele foi fiador de um amigo. | Il s'est porté garant pour un ami.
ser óbvio | aller de soi, s'imposer | A explicação era óbvia desde o começo. | L'explication s'imposait dès le départ.
sobreviver a | survivre à, traverser le temps | O edifício sobrevive a todos os seus construtores. | L'édifice survit à tous ses bâtisseurs.
solidarizar-se | compatir | Todos se solidarizaram com a família. | Tous ont compati avec la famille. | pron
sonegar | priver de, refuser (une information) | A informação nos foi sonegada. | L'information nous a été cachée.
subdividir | subdiviser, structurer | Subdividimos o relatório em quatro partes. | Nous subdivisons le rapport en quatre parties.
subsidiar | subventionner | O estado subsidia metade da reforma. | Le Land subventionne les travaux pour moitié.
suceder | succéder à | O filho o sucedeu na empresa. | Son fils lui succéda dans l'entreprise.
ter direito a | revenir de droit à | Ela tem direito a trinta dias de férias. | Elle a droit à trente jours de congé.
testemunhar | témoigner de, attester | Dois vizinhos testemunham o incidente. | Deux voisins témoignent de l'incident.
tolerar | tolérer, souffrir | A situação foi tolerada durante anos. | La situation a été tolérée pendant des années.
tropeçar | trébucher, vaciller | Até empresas experientes às vezes tropeçam. | Même des entreprises expérimentées vacillent parfois.
unificar | unifier, réunir (qn, qch) | Bismarck unificou o Império Alemão. | Bismarck a unifié l'Empire allemand.
voltar a cobrar | revenir à la charge, relancer | A empresa nunca voltou a cobrar. | L'entreprise n'a jamais relancé.
"""

# « masculin | feminin | traduction | phrase | sa traduction | drapeaux ».
ADJECTIFS = """
a médio prazo | a médio prazo | à moyen terme | A médio prazo a compra compensa. | À moyen terme, l'achat est rentable.
abrupto | abrupta | abrupt, brutal |  |  | ex=?
absurdo | absurda | saugrenu, hors de propos | A ideia nem é tão absurda assim. | L'idée n'est pas si saugrenue que ça.
aceitável | aceitável | acceptable, tolérable | Uma perda assim ainda é aceitável, por pouco. | Une telle perte est tout juste tolérable.
adaptado ao cargo | adaptado ao cargo | formé, à jour dans son poste | Depois de três meses ela estava totalmente adaptada ao cargo. | Au bout de trois mois, elle était pleinement formée. | ex?
adequado à espécie | adequado à espécie | respectueux de l'espèce (animal) | Uma criação adequada à espécie exige mais espaço. | Un élevage respectueux de l'espèce demande plus de place. | ex?
admissível | admissível | licite, recevable | Aqui não cabe recurso. | Un recours n'est pas recevable ici. | ex?
afetado | afetada | guindé, compassé | Forneceram água aos povoados afetados. | Ils ont fourni de l'eau aux villages touchés.
amador | amadora | d'amateur, maladroit | O arranjo parece coisa de amador. | La réparation a l'air d'un travail d'amateur.
anacrónico | anacrónica | anachronique, d'un autre temps | O tom parece anacrónico. | Le ton paraît d'un autre temps.
angustiante | angustiante | oppressant, angoissant | Um silêncio angustiante. | Un silence oppressant.
aos saltos | aos saltos | par à-coups, versatile | A procura evolui aos saltos. | La demande évolue par à-coups.
aparentemente | aparentemente | apparemment, de toute évidence | Aparentemente, está tudo em ordem. | Apparemment, tout est en ordre.
bem pensado | bem pensado | bien pensé, réfléchi | O projeto é pensado nos mínimos detalhes. | Le projet est réfléchi jusque dans le détail. | ex?
caduco | caduca | caduc, sans objet | Com a nova lei a regra perde o efeito. | Avec la nouvelle loi, la règle devient caduque. | ex?
característico | característica | significatif, caractéristique | O significativo é o que não foi dito. | Ce qui est significatif, c'est ce qui n'a pas été dit. | ex?
chocante | chocante | bouleversant, accablant | Os números são chocantes. | Les chiffres sont accablants.
com erros | com erros | erroné, comportant des erreurs | O cálculo estava errado. | Le calcul était erroné. | ex?
comovente | comovente | émouvant | Um discurso comovente. | Un discours émouvant.
comprovado | comprovada | attesté, documenté | A relação está bem comprovada. | Le lien est bien attesté.
comunicativo | comunicativa | communicatif, expansif | Depois do segundo café ela ficou falante. | Après le deuxième café, elle est devenue communicative. | ex?
conciliador | conciliadora | conciliant | Ele terminou em tom conciliador. | Il a conclu sur un ton conciliant.
conciso | concisa | concis, net | Um título conciso fica na memória. | Un titre ramassé reste en mémoire.
condensado | condensada | condensé, serré | A palestra foi muito condensada. | L'exposé était très condensé.
condicional | condicional | sous conditions, relatif | A afirmação só é verdadeira em parte. | L'affirmation n'est que partiellement vraie. | ex?
confirmado | confirmada | confirmé | O horário ainda não foi confirmado. | La date n'est pas encore confirmée.
conforme a lei | conforme a lei | conforme à la loi | Vamos agir conforme a lei. | Nous agirons conformément à la loi.
conforme as normas | conforme as normas | réglementaire | A montagem estava conforme as normas. | Le montage était réglementaire.
consensual | consensual | unanimement admis | O método não é consensual. | La méthode n'est pas unanimement admise.
considerável | considerável | considérable | O esforço foi considerável. | L'effort a été considérable.
consistente | consistente | solide, fondé (argument) | A objeção dele é consistente. | Son objection est fondée.
contestável | contestável | contestable, attaquable | A decisão é juridicamente contestável. | La décision est juridiquement contestable.
contido | contida | retenu, mesuré | A reação foi contida. | La réaction a été mesurée.
convencional | convencional | traditionnel, classique | Os métodos convencionais não bastam aqui. | Les méthodes classiques ne suffisent pas ici.
danificado | danificada | défectueux, abîmé | A tubulação está danificada em dois pontos. | La conduite est abîmée à deux endroits.
de comum acordo | de comum acordo | d'un commun accord | O contrato foi rescindido de comum acordo. | Le contrat a été résilié d'un commun accord.
de longo alcance | de longo alcance | de grande portée | A decisão tem consequências de longo alcance. | La décision a des conséquences de grande portée.
de passagem | de passagem | fait en passant, désinvolte | Ele mencionou isso de passagem. | Il l'a mentionné tout à fait en passant.
de pouca manutenção | de pouca manutenção | peu exigeant en entretien | A bomba exige pouca manutenção e é silenciosa. | La pompe demande peu d'entretien et est silencieuse. | ex?
decidido | decidida | décidé, sans détour | Ela apresentou-se de forma enérgica. | Elle s'est présentée sans détour. | ex?
defensável | defensável | défendable, justifiable | Um risco desse tamanho é justificável. | Un risque de cet ordre est défendable. | ex?
definitivo | definitiva | définitif | A recusa é definitiva. | Le refus est définitif.
dentro do prazo | dentro do prazo | dans les délais | O pedido chegou dentro do prazo. | La demande est arrivée dans les délais.
deprimente | deprimente | accablant, pesant | As notícias eram deprimentes. | Les nouvelles étaient accablantes.
desarmante | desarmante | désarmant | Ela sorriu de forma desarmante. | Elle a souri de façon désarmante.
desproporcional | desproporcional | disproportionné | A pena parece desproporcional. | La sanction paraît disproportionnée.
devidamente | devidamente | en bonne et due forme | A entrega foi feita devidamente. | La remise s'est faite en bonne et due forme.
dispensável | dispensável | superflu, dont on peut se passer | O segundo parágrafo é dispensável. | Le second paragraphe est superflu.
disputado | disputada | disputé, âprement contesté | O mercado é muito disputado. | Le marché est âprement disputé.
distorcido | distorcida | faussé, déformé | A imagem está distorcida pela seleção. | L'image est faussée par la sélection.
divisivo | divisiva | clivant | O tema é polarizador. | Le sujet est clivant. | ex?
do mesmo nível | do mesmo nível | de même rang | Os dois objetivos têm o mesmo peso. | Les deux objectifs sont de même rang. | ex?
documentado | documentada | documenté | Cada passo está documentado. | Chaque étape est documentée.
durável | durável | durable, qui dure | Aparelhos duráveis no fim saem mais baratos. | Les appareils durables coûtent moins cher au bout du compte.
efémero | efémera | éphémère | A tendência foi efémera. | La tendance a été éphémère.
em breve | em breve | dans un délai rapproché | Entraremos em contacto em breve. | Nous revenons vers vous rapidement.
em tópicos | em tópicos | sous forme de notes | A ata está só em tópicos. | Le procès-verbal n'est qu'en notes.
embasado | embasada | étayé, sécurisé | A tese está bem embasada. | La thèse est bien étayée.
enigmático | enigmática | cryptique, obscur | A resposta dele foi enigmática. | Sa réponse était cryptique.
entrosado | entrosada | rodé (une équipe) | A equipa é bem entrosada. | L'équipe est bien rodée.
esbanjador | esbanjadora | dispendieux, prodigue | Ele desperdiça tempo. | Il use du temps de façon dispendieuse. | ex?
esboçado | esboçada | à l'état d'ébauche | A tarefa só foi esboçada em linhas gerais. | La tâche n'a été esquissée que dans les grandes lignes.
esclarecedor | esclarecedora | éclairant | Uma palestra curta, mas esclarecedora. | Un exposé bref, mais éclairant.
exagerado | exagerada | exagéré, excessif | A crítica foi exagerada. | La critique était excessive.
feito por profissional | feito por profissional | dans les règles de l'art | O descarte precisa de ser feito de forma tecnicamente correta. | L'élimination doit se faire dans les règles de l'art. | ex?
fora da realidade | fora da realidade | déconnecté du réel | O cronograma está totalmente fora da realidade. | Le calendrier est totalement déconnecté du réel.
fragmentado | fragmentada | fragmentaire | A lembrança é fragmentada. | Le souvenir est fragmentaire.
funcional | funcional | approprié, fonctionnel | A mobília é funcional, não bonita. | L'aménagement est fonctionnel, pas beau.
fácil de cuidar | fácil de cuidar | facile d'entretien | O tecido é fácil de cuidar. | Le tissu est facile d'entretien.
generalizável | generalizável | généralisable | Um caso isolado não é generalizável. | Un cas isolé n'est pas généralisable.
gradual | gradual | insidieux, rampant | A decadência foi gradual. | Le délabrement a été insidieux.
grosseiro | grosseira | grossier ; grave (faute) | Um erro grave percorre o texto inteiro. | Une faute grossière traverse tout le texte. | ex?
imaculado | imaculada | sans défaut, immaculé | Uma superfície sem defeito. | Une surface sans le moindre défaut. | ex?
imaturo | imatura | immature, mal abouti | O conceito parece imaturo. | Le concept paraît mal abouti.
impecável | impecável | impeccable | O comportamento dele foi impecável. | Son comportement était impeccable.
imperturbável | imperturbável | imperturbable |  |  | ex=?
implacável | implacável | sans complaisance, impitoyable | O relatório é implacável. | Le rapport est sans complaisance.
imprescindível | imprescindível | indispensable, incontournable | Aqui a confiança é imprescindível. | La confiance est ici indispensable.
improdutivo | improdutiva | stérile, peu productif | A busca foi improdutiva. | La recherche est restée stérile.
inaceitável | inaceitável | inacceptable, hors de proportion | Este prazo é simplesmente inaceitável. | Ce délai est tout simplement inacceptable.
inacessível | inacessível | inaccessible ; fermé | O arquivo continua inacessível ao público. | L'archive reste inaccessible au public.
inadmissível | inadmissível | non admissible, interdit | Este corte é inadmissível. | Ce raccourci est inadmissible.
incansável | incansável | infatigable | Ele defendeu a causa incansavelmente. | Il a plaidé infatigablement pour la cause. | ex?
incoerente | incoerente | incohérent, discordant | Duas informações são discrepantes. | Deux indications sont incohérentes. | ex?
incontestado | incontestada | incontesté, sans rival | Ela lidera a lista de forma absoluta. | Elle est en tête de la liste sans rival. | ex?
incontestável | incontestável | incontesté | Os factos em si são incontestáveis. | Les faits eux-mêmes sont incontestés.
incorreto | incorreta | inexact, sans objet | Esta suposição é simplesmente incorreta. | Cette hypothèse est tout simplement inexacte.
indulgente | indulgente | indulgent | O examinador foi tolerante. | L'examinateur était indulgent. | ex?
inevitável | inevitável | inévitable | Uma certa perda é inevitável. | Une certaine perte est inévitable.
injustificável | injustificável | indéfendable | Este atraso é injustificável. | Ce retard est indéfendable.
insensível | insensível | peu délicat, maladroit | A formulação foi insensível. | La formulation était peu délicate.
insistente | insistente | insistant, pressant | Ela alertou com insistência contra a reforma. | Elle a mis en garde avec insistance contre les travaux. | ex?
instável | instável | instable, changeant | Uma vida instável entre três cidades. | Une vie instable entre trois villes.
insuportável | insuportável | insupportable | O barulho era insuportável. | Le bruit était insupportable.
insustentável | insustentável | insoutenable, intenable | A situação ficou insustentável. | La situation est devenue intenable.
intransigente | intransigente | intransigeant | Neste ponto ele continuou inflexível. | Sur ce point il est resté intransigeant. | ex?
irreconciliável | irreconciliável | irréconciliable, intransigeant | As posições são irreconciliáveis. | Les positions sont irréconciliables.
irregular | irregular | contraire au règlement | A pegada foi irregular. | La prise était contraire au règlement.
irrestrito | irrestrita | sans restriction, entier | Ele tem a minha confiança total. | Il a ma confiance entière. | ex?
isolado | isolada | isolé, sporadique | Houve objeções isoladas. | Il y a eu des objections isolées.
lacunar | lacunar | lacunaire | A tradição é cheia de lacunas. | La tradition transmise est lacunaire. | ex?
lacónico | lacónica | lapidaire, laconique | A resposta foi lacónica: não. | La réponse fut lapidaire : non.
manejável | manejável | maniable, gérable | Neste tamanho o arquivo continua manejável. | À cette taille, le fichier reste gérable.
mensurável | mensurável | mesurable | Não se vê nenhum progresso mensurável. | Aucun progrès mesurable n'est visible.
meticuloso | meticulosa | pointilleux, tatillon | Ela é pedante, mas confiável. | Elle est tatillonne, mais fiable. | ex?
metódico | metódica | méthodique, ordonné | Ela agiu de forma metódica. | Elle a procédé méthodiquement.
negligente | negligente | par négligence | Isso foi negligência grave. | C'était une négligence grave. | ex?
nitidamente delimitado | nitidamente delimitado | clairement délimité, discriminant | Os dois conceitos não são nitidamente delimitados. | Les deux notions ne sont pas clairement délimitées. | ex?
não provado | não provado | non prouvé | A acusação até agora não foi provada. | L'accusation est jusqu'ici non prouvée. | ex?
obscuro | obscura | opaque, obscur | A situação de propriedade é nebulosa. | Les rapports de propriété sont obscurs. | ex?
peculiar | peculiar | singulier, à sa façon | O estilo dele é peculiar, mas inconfundível. | Son style est singulier, mais reconnaissable entre tous.
pendente | pendente | en attente, non encore reçu | O processo ainda está pendente. | La procédure est encore pendante.
perceptível | perceptível | sensible, perceptible | Os preços subiram de forma perceptível. | Les prix ont sensiblement augmenté.
periférico | periférica | périphérique | É uma questão secundária. | C'est une question périphérique. | ex?
permitido | permitida | admissible, autorisé | A velocidade máxima permitida é oitenta. | La vitesse maximale autorisée est de quatre-vingts.
perseverante | perseverante | endurant, persévérant | Ela trabalha com perseverança e sem alarde. | Elle travaille avec persévérance et sans bruit. | ex?
perturbador | perturbadora | troublant, perturbant | As imagens são perturbadoras. | Les images sont troublantes.
pioneiro | pioneira | pionnier, qui montre la voie | Uma contribuição pioneira para o debate. | Une contribution pionnière au débat.
pomposo | pomposa | pompeux, boursouflé | O estilo é empolado e cansativo. | Le style est pompeux et fatigant. | ex?
ponderado | ponderada | posé, réfléchi | Ela tem uma opinião ponderada sobre isso. | Elle a une opinion nuancée sur le sujet.
por amostragem | por amostragem | par sondage | A fiscalização é feita só por amostragem. | Le contrôle ne se fait que par sondage.
pouco prático | pouco prático | inapproprié, mal adapté | A estrutura do formulário é pouco prática. | La structure du formulaire est mal adaptée. | ex?
pouco usado | pouco usado | peu usité | Esta expressão hoje está em desuso. | Cette tournure est aujourd'hui peu usitée. | ex?
prioritário | prioritária | prioritaire | Esta tarefa deve ser tratada com prioridade. | Cette tâche est à traiter en priorité. | ex?
prolixo | prolixa | prolixe, verbeux | A introdução é prolixa. | L'introduction est verbeuse.
pronto para publicação | pronto para publicação | prêt à imprimer, impeccable | O primeiro rascunho dele está quase pronto para publicar. | Son premier jet est presque prêt à imprimer. | ex?
propenso a falhas | propenso a falhas | sujet aux pannes | O equipamento antigo vive dando defeito. | L'ancienne installation est sujette aux pannes. | ex?
pé no chão | pé no chão | terre-à-terre, sans prétention | Apesar do sucesso, ela continua com os pés no chão. | Malgré le succès, elle est restée simple. | ex?
qualquer | qualquer | quelconque, au choix | Isso poderia acontecer a qualquer momento. | Ça pourrait arriver à tout moment.
quantificável | quantificável | quantifiable | O benefício é difícil de quantificar. | L'utilité est difficilement quantifiable. | ex?
que separa | que separa | qui sépare, clivant | Entre os dois há mais coisas que separam do que unem. | Entre les deux, il y a plus de ce qui sépare que de ce qui unit. | ex?
que une | que une | fédérateur, qui rapproche | A música tem algo que une as pessoas. | La musique a quelque chose de fédérateur.
rebuscado | rebuscada | affecté, alambiqué | Ele escreve num alemão rebuscado. | Il écrit dans un allemand alambiqué.
redigido por extenso | redigido por extenso | rédigé en toutes lettres | Precisamos de um texto redigido, não de tópicos. | Il nous faut un texte rédigé, pas des notes. | ex?
refutado | refutada | réfuté | Desde 2010 a tese é considerada refutada. | La thèse est réputée réfutée depuis 2010.
repetível | repetível | répétable |  |  | ex=?
reproduzível | reproduzível | reproductible | O experimento é reproduzível. | L'expérience est reproductible.
revelador | reveladora | instructif, révélateur | A comparação é reveladora. | La comparaison est révélatrice.
revisto | revista | remanié ; surmené | Esta é a versão revista. | C'est la version remaniée.
revolucionário | revolucionária | révolutionnaire | O método foi revolucionário para a época. | La méthode était révolutionnaire à son époque.
sem comprovação | sem comprovação | non attesté, sans preuve | A afirmação continua sem comprovação. | L'affirmation reste sans preuve.
sem contradições | sem contradições | sans contradiction | O texto é surpreendentemente livre de contradições. | Le texte est étonnamment exempt de contradictions. | ex?
sem convicção | sem convicção | sans conviction, à moitié | A tentativa foi sem convicção e não deu em nada. | La tentative était sans conviction et sans suite.
sem dúvida | sem dúvida | hors de doute | É sem dúvida a melhor opção. | C'est sans doute la meilleure option.
sem erros | sem erros | sans faute | A redação dela estava sem erros. | Sa rédaction était sans faute.
sem planeamento | sem planeamento | sans méthode, au hasard | Construído sem planeamento, pago caro. | Construit sans plan, payé cher.
sem reservas | sem reservas | sans réserve | Ela concordou sem reservas. | Elle a approuvé sans réserve.
sem transparência | sem transparência | opaque (procédure) | A licitação não teve transparência. | L'attribution était opaque. | ex?
sintomático | sintomática | symptomatique | O incidente é sintomático da situação. | L'incident est symptomatique de la situation.
sob medida | sob medida | sur mesure |  |  | ex=?
sobrecarregado | sobrecarregada | dépassé, débordé | Por momentos a linha ficou sobrecarregada. | Par moments, la ligne était saturée.
subaproveitado | subaproveitada | sous-employé, pas assez sollicité | Neste cargo ela está claramente subaproveitada. | Dans ce poste, elle est nettement sous-employée.
subordinado | subordinada | de rang inférieur, subordonné | Esta reivindicação é atendida com menor prioridade. | Cette créance est servie en rang inférieur. | ex?
suportável | suportável | supportable (perte) | Perder uma noite é suportável. | La perte d'une soirée est supportable.
suposto | suposta | prétendu, soi-disant | O suposto erro não era erro nenhum. | Le prétendu défaut n'en était pas un.
tocante | tocante | touchant, attendrissant | A preocupação dela foi tocante. | Sa sollicitude était touchante.
tortuoso | tortuosa | tortueux, sinueux (raisonnement) | A justificativa é tortuosa. | La justification est tortueuse.
trabalhoso | trabalhosa | coûteux en moyens, élaboré | A restauração foi trabalhosa. | La restauration a été coûteuse en moyens.
transferível | transferível | transposable, transmissible | O resultado não se aplica a outros países. | Le résultat n'est pas transposable à d'autres pays. | ex?
vergonhoso | vergonhosa | honteux, accablant | A participação foi vergonhosamente baixa. | La participation a été honteusement faible. | ex?
verificável | verificável | vérifiable | Cada número precisa de ser verificável. | Chaque chiffre doit être vérifiable.
vertiginoso | vertiginosa | fulgurant, très rapide | Os preços sobem num ritmo vertiginoso. | Les prix montent de façon fulgurante.
"""

# « adverbe | traduction | categorie | phrase | sa traduction ».
ADVERBES = """
admito | il faut l'admettre | Nuance | Admito: eu tinha esquecido o compromisso. | Il faut l'admettre, j'avais oublié le rendez-vous.
ainda mais porque | d'autant plus que | Cause et conséquence | Devíamos sair mais cedo, ainda mais porque está a chover. | Nous devrions partir plus tôt, d'autant plus qu'il pleut.
ainda por cima | par-dessus le marché | Liaison | Chovia e, ainda por cima, o aquecimento estava desligado. | Il pleuvait, et par-dessus le marché le chauffage était éteint.
ao passo que | tandis que, alors que | Liaison | O norte cresce, ao passo que o sul encolhe. | Le nord croît, tandis que le sud se rétracte.
bruscamente | brusquement | Manière | A conversa foi interrompida bruscamente. | La conversation s'est interrompue brusquement.
com certeza | à coup sûr, largement | Nuance | Uma boa ferramenta vale o preço com certeza. | Un bon outil vaut largement son prix.
compreensivelmente | on le comprend | Nuance | Compreensivelmente, ela ficou decepcionada. | On comprend qu'elle ait été déçue.
comprovadamente | de façon avérée | Nuance | A substância é comprovadamente nociva. | Cette substance est nocive de façon avérée.
da mesma forma | de même | Liaison | Os preços sobem, e os rendas também. | Les prix montent, de même les loyers. | ex?
de resto | au demeurant | Liaison | Aliás, considero o prazo suficiente. | Au demeurant, je trouve le délai suffisant. | ex?
em segredo | en secret | Manière | No íntimo ela torcia por uma recusa. | En secret, elle espérait un refus. | ex?
em todo caso | en tout cas | Nuance | Eu, pelo menos, considero o plano arriscado. | En tout cas, moi, je trouve le plan risqué. | ex?
em vez disso | au lieu de cela | Liaison | Ele não veio; em vez disso, mandou uma mensagem. | Il n'est pas venu ; au lieu de cela, il a envoyé un message.
literalmente | littéralement | Nuance | Trabalhamos literalmente a noite inteira. | Nous avons littéralement travaillé toute la nuit.
motivo pelo qual | raison pour laquelle | Liaison | Choveu, motivo pelo qual ficamos em casa. | Il pleuvait, raison pour laquelle nous sommes restés à la maison.
na época | à l'époque | Temps | Na época isso era considerado moderno. | À l'époque, cela passait pour moderne.
nessa medida | dans cette mesure | Liaison | Nesse ponto eu concordo com o senhor. | Dans cette mesure, je vous suis. | ex?
nisso | ce faisant, à cette occasion | Liaison | Nisso eu tenho uma opinião completamente diferente. | Là, je suis d'un avis complètement différent.
ou | ou plutôt, respectivement | Liaison | O pedido deve ser feito por escrito ou por e-mail. | La demande doit être faite par écrit, ou plutôt par courriel.
predominantemente | majoritairement | Quantité | Os participantes eram, na sua maioria, estudantes. | Les participants étaient majoritairement des étudiants. | ex?
sem exceção | sans exception | Quantité | Todos os membros, sem exceção, concordaram. | Tous les membres sans exception ont donné leur accord.
sendo que | étant entendu que | Liaison | O plano é bom, sendo que os custos ainda estão em aberto. | Le plan est bon, étant entendu que les coûts restent ouverts.
sensivelmente | sensiblement | Quantité | O ar ficou sensivelmente mais fresco. | L'air est devenu sensiblement plus frais.
sobre isso | à ce sujet | Liaison | Ele foi avisado sobre isso repetidas vezes. | On le lui a signalé à maintes reprises.
vice-versa | inversement | Liaison |  |  | ex=?
é preciso admitir | il faut l'admettre | Nuance | É preciso de admitir que o primeiro rascunho era melhor. | Il faut l'admettre, le premier projet était meilleur. | ex?
"""

# « expression | traduction | categorie | phrase | sa traduction ».
EXPRESSIONS = """
a meu ver | à mon sens | Donner son avis | A meu ver, falta base à proposta. | À mon sens, la proposition manque de fondement.
acho isso forçado | je trouve cela tiré par les cheveux | Donner son avis | Acho isso forçado, não há prova nenhuma. | Je trouve cela tiré par les cheveux, rien ne le prouve.
apesar de todas as críticas | malgré toutes les critiques | Discuter | Apesar de todas as críticas, o projeto melhorou muita coisa. | Malgré toutes les critiques, le projet a amélioré bien des choses.
apresentar reclamação | déposer une réclamation | Au quotidien | O cliente apresentou uma reclamação. | Le client a déposé une réclamation.
apresentar uma proposta | soumettre une proposition | Tournures | Ela apresentou uma proposta ao conselho. | Elle a soumis une proposition au conseil.
causar escândalo | faire scandale | Tournures | A propaganda causou grande escândalo. | La publicité a fait grand scandale.
continuar no ar | être en suspens | Discuter | A acusação continua no ar. | Le reproche reste en suspens.
correr um risco | prendre un risque | Tournures | Com este investimento a empresa corre um risco. | Avec cet investissement, l'entreprise prend un risque.
dar crédito | prêter foi à | Tournures | Não se deve dar crédito ao boato. | Il ne faut pas prêter foi à cette rumeur.
desde já | merci d'avance | Bavarder | Desde já, muito obrigado pelo seu retorno. | Merci d'avance pour votre réponse.
diante disso | au vu de cela | Discuter | Diante disso, a reunião foi adiada. | Au vu de cela, la séance a été reportée.
do jeito que as coisas estão | en l'état des choses | Discuter | Do jeito que as coisas estão, a lei não vai sair. | En l'état des choses, la loi ne verra pas le jour.
em troca | en contrepartie | Discuter | Ele assume o turno e, em troca, ganha a sexta de folga. | Il prend le quart, en contrepartie il a son vendredi.
em última instância | en dernière analyse | Discuter | Em última instância, quem decide é o cliente. | En dernière analyse, c'est le client qui décide.
entro em contacto a respeito de | je vous contacte au sujet de | Bavarder | Entro em contacto a respeito da sua solicitação de segunda-feira. | Je vous contacte au sujet de votre demande de lundi.
estar fora de si | être hors de soi | Réagir | Ela estava fora de si de alegria. | Elle était hors d'elle de joie.
estou a ponto de explodir | je pourrais exploser | Réagir | Com tanta burocracia, estou a ponto de explodir. | Avec tant de bureaucratie, je pourrais exploser.
estou dividido | je suis partagé | Réagir | Estou dividido entre as duas ofertas. | Je suis partagé entre les deux offres.
fazer concessões | faire des concessions | Tournures | Os dois lados tiveram de fazer concessões. | Les deux parties ont dû faire des concessions.
ferver de raiva | bouillir de rage | Réagir | Depois da ligação ele estava a ferver de raiva. | Après l'appel, il bouillait de rage.
ficaria grato se | je vous serais reconnaissant de | Bavarder | Ficaria grato se o senhor pudesse enviar-me os documentos. | Je vous serais reconnaissant de bien vouloir m'envoyer les documents.
fico à disposição para esclarecimentos | je reste à votre disposition | Bavarder | Fico à disposição para quaisquer esclarecimentos. | Je reste volontiers à votre disposition.
impor como condição | imposer comme condition | Au quotidien | A autoridade impôs a proteção acústica como condição. | L'administration a imposé la protection contre le bruit comme condition.
isso acaba com os meus nervos | cela m'achève les nerfs | Réagir | Essas perguntas o tempo todo acabam com os meus nervos. | Ces questions incessantes m'achèvent les nerfs.
isso já é demais | c'est la goutte d'eau | Réagir | Agora ainda tem taxa? Isso já é demais. | Et maintenant les frais en plus ? C'est la goutte d'eau.
isso me parece estranho | cela me semble louche | Réagir | O preço baixo parece-me estranho. | Ce prix si bas me semble louche.
isso não me afeta | cela me laisse froid | Réagir | Ameaças assim não me afetam. | De telles menaces me laissent froid.
manifestar preocupações | émettre des réserves | Tournures | Vários membros manifestaram preocupações. | Plusieurs membres ont émis des réserves.
muito menos | et encore moins | Discuter | Ele não ligou, muito menos pediu desculpas. | Il n'a pas appelé, et encore moins présenté ses excuses.
na falta de | à défaut de | Discuter | Na falta de propostas melhores, ficou o plano antigo. | À défaut de meilleures propositions, on en est resté à l'ancien plan.
nesse processo | dans la foulée | Discuter | O departamento mudou-se e, nesse processo, a tecnologia foi renovada. | Le service a déménagé ; dans la foulée, le matériel a été renouvelé.
no contexto de | dans le contexte de | Discuter | No contexto da crise, a quantia parece pequena. | Dans le contexte de la crise, la somme paraît faible.
no fundo | au fond | Discuter | No fundo, já concordamos há muito tempo. | Au fond, nous sommes d'accord depuis longtemps.
não é por acaso | ce n'est pas un hasard | Discuter | Não é por acaso que o contrato fracassou. | Ce n'est pas un hasard si le contrat a échoué.
obter aprovação | recueillir l'adhésion | Tournures | O projeto obteve ampla aprovação. | Le projet a recueilli une large adhésion.
olhando com mais atenção | en y regardant de plus près | Discuter | Olhando com mais atenção, a conta não batia. | En y regardant de plus près, le compte n'y était pas.
para mim é importante | cela me tient à cœur | Réagir | Para mim é importante que todos sejam ouvidos. | Cela me tient à cœur que tout le monde soit entendu.
para mim é um mistério | c'est un mystère pour moi | Réagir | Como ele conseguiu isso é um mistério para mim. | Comment il y est arrivé, c'est un mystère pour moi.
para que fique completo | par souci d'exhaustivité | Discuter | Para que fique completo, cabe mencionar a terceira variante. | Par souci d'exhaustivité, mentionnons la troisième variante.
pedir a palavra | demander la parole | Discuter | No fim do debate, o presidente da câmara pediu a palavra. | À la fin du débat, le maire a demandé la parole.
pedir explicações a | demander des comptes à | Tournures | O chefe pediu explicações a ele sobre os números. | Le patron lui a demandé des comptes sur les chiffres.
permito-me lembrá-lo de que | je me permets de vous signaler | Bavarder | Permito-me lembrá-lo de que o prazo termina amanhã. | Je me permets de vous signaler que le délai expire demain.
pode ser | c'est possible, mais | Discuter | Pode ser, mas os números dizem outra coisa. | C'est possible, mais les chiffres disent autre chose.
prezados senhores e senhoras | Madame, Monsieur | Bavarder | Prezados senhores e senhoras, venho por meio desta candidatar-me à vaga. | Madame, Monsieur, je vous adresse ma candidature pour ce poste.
que alívio | cela m'ôte un poids | Réagir | Ela chegou bem — que alívio. | Elle est bien arrivée — cela m'ôte un poids.
segue em anexo | vous trouverez ci-joint | Bavarder | Segue em anexo o acordo assinado. | Vous trouverez ci-joint la convention signée.
só posso concordar com isso | je ne peux qu'approuver | Donner son avis | Só posso concordar com isso, já passou da hora. | Je ne peux qu'approuver, cela n'avait que trop tardé.
tirar conclusões | tirer des conclusions | Tournures | Daí podem-se tirar conclusões claras. | On peut en tirer des conclusions claires.
tomar precauções | prendre des précautions | Au quotidien | Para uma emergência é bom tomar precauções. | Il faut prendre des précautions pour les cas d'urgence.
tomar providências | prendre des dispositions | Au quotidien | Tomamos providências para o inverno. | Nous avons pris des dispositions pour l'hiver.
trocando em miúdos | en clair | Discuter | Trocando em miúdos: o dinheiro não dá. | En clair : l'argent ne suffit pas.
tudo em mim resiste | tout en moi se rebiffe | Réagir | Tudo em mim resiste a assinar isso. | Tout en moi se rebiffe à l'idée de signer cela.
vejo isso com ceticismo | je suis sceptique là-dessus | Donner son avis | Vejo isso com ceticismo, os números não me convencem. | Je suis sceptique là-dessus, les chiffres ne me convainquent pas.
"""
