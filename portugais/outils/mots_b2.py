# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du B2 portugais. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que mots_a1.py et phrases_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'B2'

# « infinitif | traduction | phrase | sa traduction | drapeaux » (formes : irreguliers.py).
VERBES = """
abolir | abolir, supprimer | A regra antiga foi abolida. | On a supprimé l'ancienne règle.
abordar | aborder | Ele aborda o assunto com prudência. | Il aborde le sujet avec prudence.
abranger | couvrir, englober | O curso abrange toda a gramática. | Le cours couvre toute la grammaire.
abster-se de | s'abstenir de | Ele absteve-se de qualquer comentário. | Il s'est abstenu de tout commentaire là-dessus.
acarretar | impliquer, entraîner | Este cargo acarreta muita responsabilidade. | Ce poste implique beaucoup de responsabilités.
acatar | respecter, se conformer à | Todos devem acatar as normas. | Tout le monde doit respecter les règles.
acelerar | accélérer | Aceleraram as obras antes do verão. | Ils ont accéléré les travaux avant l'été.
aclamar | acclamer | O público aclamou os músicos. | Le public a acclamé les musiciens.
acomodar | installer | Acomodaram os convidados na sala. | Ils ont installé les invités dans la salle.
acompanhar o andamento | suivre l'avancement | Eles acompanham o andamento com um painel. | Ils suivent l'avancement avec un tableau.
acusar | accuser | A imprensa acusou a empresa de inércia. | La presse reprochait à l'entreprise son inaction.
adaptar-se à mudança | s'adapter au changement | Eles adaptam-se à mudança com formação. | Ils s'adaptent au changement par la formation.
adiar | reporter, ajourner | Adiaram a reunião para segunda. | Ils ont reporté la réunion à lundi.
adotar | adopter | Eles adotaram uma postura prudente. | Ils ont adopté une position prudente.
agilizar | accélérer, simplifier | É preciso de agilizar os trâmites. | Il faut accélérer les démarches.
agrupar | regrouper | Agrupe os dados por região. | Regroupe les données par région.
almejar | viser, aspirer à | A empresa almeja uma posição de liderança. | L'entreprise vise une position de premier plan.
aludir | faire allusion à | Ele aludiu à crise sem nomeá-la. | Il a fait allusion à la crise sans la nommer.
amortecer | atténuer, freiner | A família amorteceu o choque. | La famille encaissa le choc.
amparar | protéger (juridiquement) | A lei ampara o inquilino. | La loi protège le locataire.
analisar um texto | analyser un texte | Eles analisam um texto por sessão. | Ils analysent un texte par séance.
ancorar | ancrer, inscrire | O direito está consagrado na Lei Fundamental. | Ce droit est inscrit dans la Loi fondamentale. | ex?
anular | annuler, lever | A exceção anula a regra inteira. | L'exception neutralise toute la règle.
aplicar-se | s'appliquer, être exact | Esta regra só se aplica a clientes novos. | Cette règle ne s'applique qu'aux nouveaux clients. | pron
apreciar | apprécier | Ele aprecia o detalhe mais do que o conjunto. | Il apprécie le détail plus que l'ensemble.
aprofundar | approfondir | O livro aprofunda-se na história do bairro. | Le livre approfondit l'histoire du quartier.
aspirar | aspirer | Quando jovem, ele aspirava a ser piloto. | Jeune, il aspirait à devenir pilote.
assumir | assumer | Ele assume a responsabilidade sem hesitar. | Il assume la responsabilité sans hésiter.
atirar | tirer ; congédier | O soldado atirou para o alto. | Le soldat a tiré en l'air.
atribuir | attribuer (à une cause) | O sucesso é atribuído a uma boa preparação. | On attribue le succès à une bonne préparation.
autorizar | autoriser | A câmara municipal autorizou o terraço. | La mairie a autorisé la terrasse.
basear-se | reposer (sur qch) | Esta suposição baseia-se em dados antigos. | Cette hypothèse repose sur des données anciennes. | pron
caber a | revenir à, correspondre | Essa decisão cabe à direção. | Cette décision revient à la direction.
calar | se taire | Ele calou-se para não piorar as coisas. | Il s'est tu pour ne pas aggraver les choses.
caracterizar | caractériser | A sobriedade caracteriza o estilo dele. | La sobriété caractérise son style.
carecer de | manquer de | O relatório carece de dados recentes. | Le rapport manque de données récentes.
ceder | céder | Nenhuma das partes quer ceder. | Aucune partie ne veut céder.
checar as fontes | recouper les sources | Eles checam as fontes antes de publicar. | Ils recoupent les sources avant de publier.
combater | combattre | Eles combatem a fraude com fiscalizações. | Ils combattent la fraude par des contrôles.
comover | émouvoir | A carta o comoveu. | La lettre l'a ému.
compensar | compenser | Eles compensam as emissões do voo. | Ils compensent les émissions du vol.
compor | composer | O júri é composto por cinco pessoas. | Le jury est composé de cinq personnes.
comprometer | compromettre | O erro compromete a credibilidade. | L'erreur compromet la crédibilité.
conceber | concevoir | Ele concebe a liberdade de outra maneira. | Il conçoit la liberté autrement.
conceder | concéder | Eu não concederia tanto tempo a ninguém. | Je n'accorderais autant de temps à personne.
concentrar | concentrer | Concentre o esforço no urgente. | Concentre l'effort sur l'urgent.
conciliar | concilier | É difícil conciliar trabalho e família. | Il est difficile de concilier travail et famille.
concretizar | préciser, concrétiser | Ele concretizou o seu plano. | Il a réalisé son plan.
condicionar | conditionner | Eles condicionam a ajuda a um relatório. | Ils conditionnent l'aide à un rapport.
conformar-se | se résigner (à qch) | Ela conformou-se com a recusa. | Elle s'est résignée au refus. | pron
confrontar | recouper | Confrontamos os resultados com os do ano passado. | Nous avons comparé les résultats avec ceux de l'année dernière.
conseguir fazer | réussir à faire, mener à bien | Eu gostaria de fazer macarrão mais vezes. | J'aimerais cuisiner des pâtes plus souvent.
consentir | consentir | O paciente consentiu por escrito. | Le patient a consenti par écrit.
constituir | constituer | Doze artigos compõem a lei. | Douze articles constituent la loi. | ex?
contornar | éluder, contourner | O ministro contornou a pergunta. | Le ministre a éludé la question.
contribuir | contribuer | Todos contribuíram para o presente. | Tout le monde a contribué au cadeau.
cooperar | coopérer | As duas cidades cooperam desde 2015. | Les deux villes coopèrent depuis 2015.
corresponder a | correspondre à | O resultado corresponde às nossas expectativas. | Le résultat correspond à nos attentes.
cruzar | croiser | A rua cruzava a linha do comboio. | La route croisait la voie ferrée.
culpar | blâmer | Não culpe o mensageiro. | N'accuse pas le messager.
dar bons resultados | faire ses preuves | O novo procedimento está a dar bons resultados no dia a dia. | Le nouveau procédé fait ses preuves au quotidien.
debater | débattre | Eles debateram a proposta por duas horas. | Ils ont débattu de la proposition deux heures.
deduzir | déduire | Daí deduzo que falta um dado. | J'en déduis qu'il manque une donnée.
deliberar | délibérer | O júri deliberou por duas horas. | Le jury a délibéré deux heures.
delinear-se | se dessiner, se profiler | A tendência já se delineava cedo. | La tendance s'était dessinée très tôt. | pron
depor | témoigner, exprimer | A testemunha depõe amanhã no tribunal. | Le témoin témoigne demain au tribunal.
depreender | déduire, prélever | Desta frase eu depreenderia outra coisa. | De cette phrase, je déduirais autre chose.
desabrochar | s'épanouir, se déployer | Nesta equipa ela realmente desabrocha. | Dans cette équipe, elle s'épanouit vraiment.
desaconselhar | déconseiller | O médico desaconselha viagens longas. | Le médecin déconseille les longs voyages.
desafiar | défier | Ele desafiou as conclusões do relatório. | Il a défié les conclusions du rapport.
desempenhar | exercer | Ele desempenhou o cargo durante dez anos. | Il a exercé la fonction pendant dix ans.
deslocar | déplacer | A enchente deslocava as pedras do caminho. | La crue déplaçait les pierres du chemin.
desmanchar-se | se disloquer, se briser en deux | Com um palhaço as crianças divertir-se-iam mais. | Avec un clown, les enfants s'amuseraient plus. | pron
desmentir | démentir | Eles desmentiram a notícia em uma hora. | Ils ont démenti la nouvelle en une heure.
desmontar | démonter ; réduire ; extraire | Depois da festa desmontamos as barracas. | Après la fête, nous démontons les tentes.
despedaçar | briser, fracasser | Uma queda despedaçaria o vaso na hora. | Une chute fracasserait le vase aussitôt.
desperdiçar | gaspiller | Não desperdice água. | Ne gaspille pas l'eau.
destacar | mettre en évidence | O relatório destaca dois pontos em especial. | Le rapport met deux points particulièrement en évidence.
destacar-se | se distinguer, se détacher | A torre destacava-se escura contra o céu. | La tour se détachait, sombre, sur le ciel. | pron
destinar | destiner | Eles destinam o dinheiro a bolsas de estudo. | Ils destinent l'argent à des bourses.
desvalorizar | dévaluer | Desvalorizaram a moeda em janeiro. | Ils ont dévalué la monnaie en janvier.
detalhar | détailler | Detalhe os gastos no anexo. | Détaille les dépenses en annexe.
dificultar | compliquer, rendre difficile | A neve dificulta o acesso. | La neige complique l'accès.
disputar | disputer | Duas empresas disputam o contrato. | Deux entreprises se disputent le contrat.
dissuadir | dissuader | Tentaram dissuadi-lo de viajar. | Ils ont essayé de le dissuader de voyager.
distorcer | déformer (des propos) | Os jornalistas distorceram as palavras dele. | Les journalistes ont déformé ses propos.
ditar | dicter | O tribunal ditou a sentença na terça. | Le tribunal a rendu sa sentence mardi.
encarar | aborder (un problème), concerner | A equipa encarou a tarefa com coragem. | L'équipe a abordé la tâche avec courage.
encarregar | charger (qn de qch) | Um escritório de advocacia foi encarregado disso. | On en chargea un cabinet.
encurtar | raccourcir, écourter | O trajeto novo encurta a viagem em vinte minutos. | Le nouveau tracé raccourcit le trajet de vingt minutes.
endurecer | durcir, aggraver | O governo endurece os controles. | Le gouvernement durcit les contrôles.
enfrentar | affronter, faire face à | Temos de enfrentar o problema. | Nous devons faire face au problème.
esboçar | esquisser | Ele esboçou um sorriso. | Il a esquissé un sourire.
esquivar-se | esquiver, éviter | Ele esquiva-se da pergunta com habilidade. | Il esquive habilement la question. | pron
esquivar-se de | éluder, éviter | Ele esquivou-se da pergunta com um sorriso. | Il a éludé la question avec un sourire.
estimular a economia | relancer l'économie | Eles estimulam a economia com obras públicas. | Ils relancent l'économie par les travaux publics.
estragar | gâcher ; s'abîmer | Com este calor o leite estraga rápido. | Par cette chaleur, le lait tourne vite.
estruturar | structurer, articuler | O autor estruturou o capítulo com clareza. | L'auteur a clairement structuré le chapitre.
expandir-se | s'étendre | A empresa expandiu-se para a Ásia. | L'entreprise s'est étendue en Asie. | pron
favorecer | favoriser | O clima ameno favorece o cultivo de uva. | Le climat doux favorise la viticulture.
fazer efeito | agir, faire effet ; paraître | O medicamento faz efeito depois de vinte minutos. | Le médicament fait effet après vingt minutes.
fazer participar | faire participer, associer | Já fiz a minha lição de casa. | J'ai déjà fait mes devoirs.
fazer um balanço | dresser le bilan | No fim do ano o clube faz um balanço do trabalho. | En fin d'année, l'association dresse le bilan de son travail.
fomentar | encourager, promouvoir | A escola fomentava o desporto com torneios. | L'école encourageait le sport par des tournois.
frisar | souligner, insister sur | A professora frisou a importância da revisão. | La professeure a insisté sur l'importance des révisions.
fundamentar | fonder, étayer | Fundamente bem os teus argumentos. | Étaye bien tes arguments.
gerar conteúdo | générer du contenu | O sistema gera conteúdo em segundos. | Le système génère du contenu en secondes.
ilustrar | illustrer, rendre concret | Um diagrama ilustra o processo. | Un schéma illustre le déroulement.
impor-se | s'imposer | Ela impôs-se contra todas as resistências. | Elle s'est imposée contre toutes les résistances. | pron
importar a | préoccuper, importer à (qn) | Isso não me importa. | Ça ne me préoccupe pas.
importar bens | importer des biens | Eles importam bens de vinte países. | Ils importent des biens de vingt pays.
indeferir | rejeter, écarter | O juiz indeferiu o pedido. | Le juge a rejeté la plainte.
inibir | freiner, inhiber | O frio inibiu o crescimento. | Le froid a freiné la croissance.
insistir em | insister sur, avoir une incidence sur | A professora insistiu nesse ponto. | La professeure a insisté sur ce point.
inspirar confiança | inspirer confiance | Ele inspira confiança desde o primeiro dia. | Il inspire confiance dès le premier jour.
interagir | interagir | Os grupos interagem pouco entre si. | Les groupes interagissent peu entre eux.
intervir diplomaticamente | intervenir par la voie diplomatique | Eles intervieram diplomaticamente no conflito. | Ils sont intervenus par la voie diplomatique dans le conflit.
intervir no debate | intervenir dans le débat | Ele interveio no debate no final. | Il est intervenu dans le débat à la fin.
investigar a fundo | enquêter à fond | Eles investigam a fundo desde 2020. | Ils enquêtent à fond depuis 2020.
ironizar | ironiser | Ele ironiza o próprio trabalho. | Il ironise sur son propre travail.
irrigar | irriguer, arroser | No verão eles irrigam os campos à noite. | En été, ils irriguent les champs la nuit.
julgar moralmente | juger moralement | Ele não julga ninguém moralmente. | Il ne juge moralement personne.
levar em conta | prendre en compte | Levamos em conta todas as sugestões recebidas. | Nous prenons en compte toutes les propositions reçues.
liderar | diriger | Ele lidera uma equipa de quinze pessoas. | Il dirige une équipe de quinze personnes.
mediar | servir de médiateur | Um terceiro país mediou entre as partes. | Un pays tiers a servi de médiateur.
menosprezar | sous-estimer, mépriser | O chefe dele menosprezava o trabalho dos estagiários. | Son chef méprisait le travail des stagiaires.
mexer | remuer ; émouvoir | Mexe a sopa devagar. | Remue la soupe lentement.
mitigar | atténuer | Eles mitigam o impacto com arborização. | Ils atténuent l'impact par la plantation d'arbres.
monopolizar | accaparer | Ele sempre monopoliza a atenção. | Il accapare toujours l'attention.
nomear | nommer, désigner | Ele nomeia o problema com muita precisão. | Il nomme le problème très précisément.
nuançar | nuancer | Ele sempre nuança as suas opiniões. | Il nuance toujours ses opinions.
objetar | objecter | Ele objetou que faltava informação. | Il a objecté qu'il manquait de l'information.
otimizar | optimiser | Eles otimizam o processo a cada trimestre. | Ils optimisent le processus chaque trimestre.
outorgar | accorder, décerner | A cidade outorgava uma bolsa todo ano. | La ville accordait une bourse chaque année.
pactuar | convenir, pactiser | Os partidos pactuavam o orçamento todo outono. | Les partis négociaient le budget chaque automne.
persuadir com dados | persuader par les chiffres | Ele persuade com dados, não com adjetivos. | Il persuade par les chiffres, pas par les adjectifs.
ponderar | peser (le pour et le contre) | É preciso de ponderar as vantagens e as desvantagens. | Il faut peser le pour et le contre.
prejudicar | nuire à, altérer | O barulho prejudica a concentração. | Le bruit nuit à la concentration.
preservar | préserver | Eles preservam as técnicas antigas. | Ils préservent les techniques anciennes.
prestar | rendre (un service), s'avérer | Com isso ela presta-nos um grande favor. | Elle nous rend ainsi un grand service.
presumir | présumer | Eles presumem que ele chegará na segunda. | Ils présument qu'il arrivera lundi.
priorizar | prioriser | Ele prioriza o urgente em vez do importante. | Il priorise l'urgent sur l'important.
processar | traiter, mener à bien | O banco processa o pagamento rapidamente. | La banque traite le paiement rapidement.
promulgar | promulguer, dispenser de | O governo promulga uma lei nova. | Le gouvernement promulgue une nouvelle loi.
propiciar | favoriser, provoquer | O diálogo propiciou um acordo. | Le dialogue a favorisé un accord.
providenciar | faire en sorte, ordonner | Eu providencio as bebidas para a festa. | Je me charge des boissons pour la fête.
publicar resultados | publier des résultats | Eles publicam resultados a cada trimestre. | Ils publient des résultats chaque trimestre.
quantificar | chiffrer, évaluer | O estudo quantificou a perda com precisão. | L'étude chiffrait précisément la perte.
rachar | fendre ; diviser | Ele rachou a lenha com o machado. | Il a fendu le bois à la hache.
raciocinar | raisonner | Ele raciocina em voz alta quando trabalha. | Il raisonne à voix haute quand il travaille.
ratificar | ratifier | O país ratificou o acordo em março. | Le pays a ratifié l'accord en mars.
rebater | réfuter point par point | Ele rebateu cada ponto com calma. | Il a réfuté chaque point avec calme.
redigir | rédiger | Ela vai redigir o relatório até sexta. | Elle rédige le rapport d'ici vendredi.
referir-se | se référer (à qch) | Refiro-me à sua carta de segunda-feira. | Je me réfère à votre courrier de lundi. | pron
reforçar | renforcer | A câmara municipal reforça a fiscalização no fim de semana. | La ville renforce les contrôles le week-end.
regulamentar | réglementer | Eles regulamentam o uso desses dados. | Ils réglementent l'usage de ces données.
relativizar | relativiser | Este número relativiza a primeira impressão. | Ce chiffre relativise la première impression.
render | rendre, rapporter | Quando jovem, eu rendia mais de manhã. | Jeune, j'étais plus productif le matin.
requalificar-se profissionalmente | se reconvertir | Ele requalifica-se a cada cinco anos. | Il se reconvertit tous les cinq ans.
resenhar | recenser, chroniquer | Ele resenha dois romances por mês. | Il chronique deux romans par mois.
resignar-se | se résigner | Ele resignou-se a esperar mais um ano. | Il s'est résigné à attendre une année de plus. | pron
respaldar | soutenir, appuyer | A família dele respaldava cada decisão sua. | Sa famille soutenait chacune de ses décisions.
ressaltar | souligner (au sens figuré) | Os números ressaltam a urgência. | Les chiffres soulignent l'urgence.
retomar | reprendre (une idée) | O orador retoma a objeção na hora. | L'orateur reprend aussitôt l'objection.
rever | réviser (un jugement) | Depois da conversa eu revejo a minha opinião. | Après l'entretien, je révise mon opinion.
sanar | corriger, réparer (une erreur) | Vamos sanar o problema na próxima versão. | Nous corrigerons le problème dans la prochaine version.
sancionar | sanctionner | Eles sancionaram as exportações. | Ils ont sanctionné les exportations.
sediar | organiser, transmettre (un message) | A cidade sedia o torneio. | La ville organise le tournoi.
segmentar | segmenter | Eles segmentam a população por idade. | Ils segmentent la population par âge.
selar | sceller, entériner | Um aperto de mão sela o acordo. | Une poignée de main scelle l'accord.
sentir saudade de | regretter (une absence) | Ele sente saudade do seu vilarejo a cada outono. | Il regrette son village chaque automne.
silenciar o passado | taire le passé | Durante anos o passado foi silenciado. | Pendant des années on a tu le passé.
sinalizar | caractériser, signaler | Uma placa sinaliza a saída de emergência. | Un panneau signale la sortie de secours.
sobrecarregar | peser sur, charger | Um imposto novo sobrecarregaria as empresas. | Une nouvelle taxe pèserait sur les entreprises.
sondar | sonder, explorer | Primeiro sondamos as possibilidades. | Nous sondons d'abord les possibilités.
suavizar | adoucir | Ele suavizou o tom no final. | Il a adouci le ton à la fin.
sublinhar | souligner | O relatório sublinhou a falta de pessoal. | Le rapport a souligné le manque de personnel.
suscitar | susciter | A proposta suscitou um grande debate. | La proposition a suscité un grand débat.
suspeitar | soupçonner | Suspeito que falta um dado. | Je soupçonne qu'il manque une donnée.
suspender | suspendre, exposer à | A federação suspende a regra por enquanto. | La fédération suspend la règle pour l'instant.
sustentar | étayer | O turismo sustentava a economia da cidadezinha. | Le tourisme soutenait l'économie du village.
terceirizar | externaliser | Eles terceirizam o atendimento ao cliente. | Ils externalisent le service client.
tornar-se desnecessário | devenir superflu | Depois da confirmação o pedido ficou desnecessário. | Après l'accord, la demande est devenue superflue.
treinar um modelo | entraîner un modèle | Eles treinam um modelo com dados públicos. | Ils entraînent un modèle sur des données publiques.
validar | valider | Eles validaram o método em três países. | Ils ont validé la méthode dans trois pays.
variar | varier | Os preços variam conforme a estação. | Les prix varient selon la saison.
vaticinar | prédire | Ninguém vai vaticinar o resultado deste jogo. | Personne ne prédira le résultat de ce match.
vazar | divulguer, filtrer | Alguém vazou o documento. | Quelqu'un a divulgué le document.
violar | porter atteinte à | A medida viola um direito básico. | La mesure porte atteinte à un droit fondamental.
vislumbrar | entrevoir | Já se vislumbra uma solução. | On entrevoit déjà une solution.
voltar-se para | se tourner vers | Ela voltou-se para um tema novo. | Elle s'est tournée vers un nouveau sujet.
"""

# « masculin | feminin | traduction | phrase | sa traduction | drapeaux ».
ADJECTIFS = """
abrangente | abrangente | complet, exhaustif | Ele deu um panorama completo. | Il a donné un aperçu complet. | ex?
abstrato | abstrata | abstrait | É um conceito abstrato. | C'est un concept abstrait.
ambivalente | ambivalente | ambivalent | Ele tem sentimentos ambivalentes. | Il a des sentiments ambivalents.
ambíguo | ambígua | ambigu | A resposta dele foi ambígua. | Sa réponse a été ambiguë.
ancestral | ancestral | ancestral | É uma prática ancestral. | C'est une pratique ancestrale.
antiético | antiética | contraire à l'éthique | O comportamento dele foi criticado como antiético. | Son comportement a été critiqué comme contraire à l'éthique.
arbitrário | arbitrária | arbitraire | A regra parece bem arbitrária. | La règle paraît plutôt arbitraire.
artificial | artificial | artificiel | É uma voz artificial. | C'est une voix artificielle.
autóctone | autóctone | autochtone | É uma espécie nativa. | C'est une espèce autochtone. | ex?
bem fundamentado | bem fundamentado | bien fondé, solide | A argumentação dele é bem fundamentada. | Son argumentation est bien fondée. | ex?
bilateral | bilateral | bilatéral | É um acordo bilateral. | C'est un accord bilatéral.
brusco | brusca | brusque | Ele tem um jeito um pouco brusco. | Il a des manières un peu brusques.
canhoto | canhota | gaucher | O meu irmão é canhoto. | Mon frère est gaucher.
carregado | carregada | chargé | O interior é carregado demais. | L'intérieur est trop chargé.
casual | casual | aléatoire, par hasard | Foi uma coincidência puramente casual. | Ce fut une coïncidence purement fortuite.
coerente | coerente | cohérent | É um discurso coerente. | C'est un discours cohérent.
coloquial | coloquial | familier | É uma expressão coloquial. | C'est une expression familière.
comprovável | comprovável | démontrable | O dano é comprovável. | Le dommage est démontrable.
conclusivo | conclusiva | concluant, cohérent | A prova não foi realmente conclusiva. | La preuve n'était pas vraiment concluante.
conforme | conforme | conforme | A montagem estava conforme as normas. | Le montage était réglementaire.
constitucional | constitucional | constitutionnel | É uma reforma constitucional. | C'est une réforme constitutionnelle.
contraditório | contraditória | contradictoire | Os dados são contraditórios. | Les données sont contradictoires.
contraproducente | contraproducente | contre-productif | Esta medida é contraproducente. | Cette mesure semble contre-productive.
controverso | controversa | controversé | É um tema controverso. | C'est un sujet controversé.
cortês | cortês | courtois | Foi uma resposta cortês. | Ce fut une réponse courtoise.
culto | culta | soutenu | Ele usa uma linguagem culta. | Il emploie un langage soutenu.
de duplo sentido | de duplo sentido | équivoque | O comentário dele teve duplo sentido. | Sa remarque était équivoque. | ex?
de grandes consequências | de grandes consequências | lourd de conséquences | A decisão teve grandes consequências. | La décision a eu de lourdes conséquences. | ex?
dependente | dependente | dépendant | Ele depende financeiramente dos pais. | Il dépend financièrement de ses parents. | ex?
determinante | determinante | déterminant | O preço foi determinante para a decisão. | Le prix a été déterminant pour la décision.
dogmático | dogmática | dogmatique | A postura dele às vezes parece dogmática. | Son attitude paraît parfois dogmatique.
doloroso | dolorosa | douloureux | É um capítulo doloroso. | C'est un chapitre douloureux.
eficiente | eficiente | efficient | É um processo muito eficiente. | C'est un processus très efficient.
eloquente | eloquente | éloquent | Foi um discurso eloquente. | Ce fut un discours éloquent.
emergente | emergente | émergent | É uma economia emergente. | C'est une économie émergente.
empático | empática | empathique | Ele tem um estilo empático. | Il a un style empathique.
empírico | empírica | empirique | É uma prova empírica. | C'est une preuve empirique.
escalável | escalável | extensible | O modelo é escalável. | Le modèle est extensible.
excecional | excecional | exceptionnel, remarquable | Ela teve um desempenho excecional. | Elle a fourni une performance exceptionnelle.
exemplar | exemplar | exemplaire | O comportamento dele foi exemplar. | Son comportement était exemplaire.
global | global | mondial | É um fenómeno global. | C'est un phénomène mondial.
grandiloquente | grandiloquente | grandiloquent | O tom soa grandiloquente. | Le ton paraît grandiloquent.
harmonioso | harmoniosa | harmonieux | É um conjunto harmonioso. | C'est un ensemble harmonieux.
ilegítimo | ilegítima | illégitime | Eles consideram a votação ilegítima. | Ils considèrent le vote illégitime.
imoral | imoral | immoral | O comportamento foi criticado como imoral. | Le comportement a été critiqué comme immoral.
imparcial | imparcial | impartial | Ele tenta ser imparcial. | Il essaie d'être impartial.
improvável | improvável | improbable | É improvável, mas possível. | C'est improbable mais possible.
inadequado | inadequada | inapproprié | O comportamento dele foi inadequado. | Son comportement était inapproprié.
incerto | incerta | incertain | O resultado é incerto. | Le résultat est incertain.
inclinado | inclinada | oblique, de travers | O quadro está um pouco torto. | Le tableau est un peu de travers. | ex?
inconsciente | inconsciente | inconscient | Ele fez isso inconscientemente. | Il l'a fait inconsciemment. | ex?
indiscutível | indiscutível | indéniable | O mérito dele é indiscutível. | Son mérite est incontesté.
indispensável | indispensável | indispensable | A água é indispensável para nós. | L'eau nous est indispensable.
inequívoco | inequívoca | univoque, clair | A resposta foi clara. | La réponse était claire et sans équivoque. | ex?
inflacionário | inflacionária | inflationniste | É uma espiral inflacionária. | C'est une spirale inflationniste.
infundado | infundada | infondé | O medo é totalmente infundado. | La peur est totalement infondée.
injustificado | injustificada | injustifié | A demissão foi injustificada. | Le licenciement était injustifié.
inovador | inovadora | novateur | É uma abordagem inovadora. | C'est une approche novatrice.
insignificante | insignificante | insignifiant | Para ela dinheiro não tem importância. | Pour elle, l'argent n'a aucune importance. | ex?
intencional | intencional | intentionnel | O efeito não foi intencional. | L'effet était non intentionnel.
intenso | intensa | intense | Foi um debate intenso. | Ce fut un débat intense.
inviolável | inviolável | inviolable | É um direito inviolável. | C'est un droit inviolable.
irracional | irracional | irrationnel | O medo dele era totalmente irracional. | Sa peur était totalement irrationnelle.
irrelevante | irrelevante | non pertinent | O comentário foi irrelevante para a discussão. | Le commentaire n'était pas pertinent pour la discussion.
irrenunciável | irrenunciável | auquel on ne peut renoncer | É um direito irrenunciável. | C'est un droit auquel on ne peut renoncer.
irreversível | irreversível | irréversible | A mudança seria irreversível. | Le changement serait irréversible.
justificado | justificada | justifié | A crítica foi justificada. | La critique était justifiée.
legítimo | legítima | légitime | É um pedido legítimo. | C'est une demande légitime.
macroeconómico | macroeconómica | macroéconomique | É um indicador macroeconómico. | C'est un indicateur macroéconomique.
marcante | marcante | prononcé, marqué | Ele tem um senso de humor marcante. | Il a un sens de l'humour très prononcé.
marginal | marginal | marginal | É um fenómeno marginal. | C'est un phénomène marginal.
matizado | matizada | nuancé | Ela tem uma opinião ponderada sobre isso. | Elle a une opinion nuancée sur le sujet. | ex?
minucioso | minuciosa | approfondi, minutieux | Ele fez o trabalho com muito cuidado. | Il a fait le travail de façon très minutieuse. | ex?
moderado | moderada | modéré | Ele mantém uma posição moderada. | Il garde une position modérée.
moral | moral | moral | Ele agiu por motivos morais. | Il a agi pour des raisons morales.
multifacetado | multifacetada | riche en facettes | A personalidade dele é multifacetada. | Sa personnalité a de nombreuses facettes.
neutro | neutra | neutre | O país declarou-se neutro. | Le pays s'est déclaré neutre.
não intencional | não intencional | involontaire | O erro foi sem querer. | L'erreur était involontaire. | ex?
obsoleto | obsoleta | obsolète | O sistema ficou obsoleto. | Le système est devenu obsolète.
oposto | oposta | opposé | Eles foram em direções opostas. | Ils sont partis dans des directions opposées.
ordinário | ordinária | ordinaire | É uma sessão ordinária do conselho. | C'est une séance ordinaire du conseil.
paradoxal | paradoxal | paradoxal | O resultado parece paradoxal. | Le résultat paraît paradoxal.
parcial | parcial | partiel | Só temos dados parciais. | Nous n'avons que des données partielles.
parlamentar | parlamentar | parlementaire | É um debate parlamentar. | C'est un débat parlementaire.
permanente | permanente | permanent | Ele conseguiu um contrato permanente. | Il a obtenu un contrat permanent.
plausível | plausível | plausible | É uma explicação plausível. | C'est une explication plausible.
polémico | polémica | polémique | É um assunto polémico. | C'est une affaire polémique.
posterior | posterior | postérieur | Em uma fase posterior vamos revisar. | Dans une phase postérieure nous le réviserons.
potente | potente | puissant |  |  | ex=?
pouco convencional | pouco convencional | non conventionnel | Ela tem um estilo de liderança pouco convencional. | Elle a un style de management non conventionnel.
pragmático | pragmática | pragmatique | Ele sempre resolve problemas de forma muito pragmática. | Il résout toujours les problèmes de façon très pragmatique.
preliminar | preliminar | préliminaire | São dados preliminares. | Ce sont des données préliminaires.
prematuro | prematura | prématuré | Seria prematuro anunciar. | Il serait prématuré de l'annoncer.
primário | primária | primaire | Ela estuda educação primária. | Il étudie l'enseignement primaire.
principal | principal | principal | A entrada principal está fechada. | L'entrée principale est fermée.
produtivo | produtiva | productif | Foi um dia produtivo. | Ce fut une journée productive.
provisório | provisória | provisoire | É um acordo provisório. | C'est un accord provisoire.
prévio | prévia | préalable | É necessário agendamento prévio. | Un rendez-vous préalable est requis.
próprio | própria | propre (à soi) | Ele tem o seu próprio escritório. | Il a son propre bureau.
questionável | questionável | contestable | O método é questionável. | La méthode est contestable.
químico | química | chimique | Evite produtos químicos fortes. | Évite les produits chimiques forts.
radical | radical | radical | Ele propôs uma mudança radical. | Il a proposé un changement radical.
refutável | refutável | réfutable | Esta teoria é cientificamente refutável. | Cette théorie est scientifiquement réfutable.
regenerativo | regenerativa | régénératif | Eles praticam uma agricultura regenerativa. | Ils pratiquent une agriculture régénérative.
regional | regional | régional | O comboio regional para em todos os vilarejos. | Le train régional s'arrête dans tous les villages.
repetido | repetida | répété | Houve atrasos repetidos. | Il y a eu des retards répétés.
representativo | representativa | représentatif | A pesquisa é representativa. | Le sondage est représentatif.
resoluto | resoluta | efficace, décidé | É uma chefe muito resoluta. | C'est une cheffe très efficace.
secundário | secundária | secondaire | O ponto tem um papel secundário. | Ce point joue un rôle secondaire.
sem compromisso | sem compromisso | non contraignant | A proposta é sem compromisso. | L'offre n'est pas contraignante.
semanal | semanal | hebdomadaire | Temos uma reunião semanal. | Nous avons une réunion hebdomadaire.
sensacionalista | sensacionalista | sensationnaliste | É uma manchete sensacionalista. | C'est un titre sensationnaliste.
silenciado | silenciada | passé sous silence | Foi um episódio silenciado durante anos. | Ce fut un épisode passé sous silence des années.
sistemático | sistemática | systématique | Ele enfrenta os problemas de forma sistemática. | Il aborde les problèmes de façon systématique.
sociológico | sociológica | sociologique | É um estudo sociológico. | C'est une étude sociologique.
subjetivo | subjetiva | subjectif | Claro que é uma opinião subjetiva. | C'est bien sûr une opinion subjective.
supérfluo | supérflua | superflu | Esta informação é desnecessária. | Cette information est superflue. | ex?
sutil | sutil | subtil | É uma diferença sutil. | C'est une différence subtile.
sóbrio | sóbria | sobre | Ele prefere um design sóbrio. | Il préfère un design sobre.
tendencioso | tendenciosa | tendancieux | O artigo foi escrito de forma bem tendenciosa. | L'article était rédigé de façon plutôt tendancieuse.
tóxico | tóxica | toxique | A embalagem tem o rótulo de tóxico. | L'emballage porte l'étiquette toxique.
universal | universal | universel | Ele busca um princípio universal. | Il cherche un principe universel.
vago | vaga | vague | Ele deu uma resposta vaga. | Il a donné une réponse vague.
verossímil | verossímil | vraisemblable | O personagem é verossímil. | Le personnage est vraisemblable.
versátil | versátil | polyvalent | Ele procura um perfil versátil. | Il cherche un profil polyvalent.
vinculante | vinculante | contraignant | O acordo é vinculante. | L'accord est contraignant.
vinculativo | vinculativa | contraignant, engageant | O horário é definitivo. | Le rendez-vous est ferme. | ex?
vingativo | vingativa | vindicatif | Depois da briga ele parecia bem vingativo. | Après la dispute, il semblait vraiment vindicatif.
viável | viável | viable | É um modelo viável a longo prazo. | C'est un modèle viable à long terme.
ético | ética | éthique | É uma decisão ética, não legal. | C'est une décision éthique, pas juridique.
"""

# « adverbe | traduction | categorie | phrase | sa traduction ».
ADVERBES = """
a contragosto | à contrecœur | Manière | Ele aceitou a contragosto. | Il a accepté à contrecœur.
a longo prazo | à la longue | Temps | A longo prazo o investimento compensa. | À long terme, l'investissement est rentable.
a olhos vistos | à vue d'œil | Quantité | A situação melhora a olhos vistos. | La situation s'améliore à vue d'œil.
a rigor | à proprement parler | Liaison | A rigor, isso não é um erro. | À proprement parler, ce n'est pas une erreur.
abaixo | en dessous | Lieu | Ficou-se dez por cento abaixo do orçamento. | On resta dix pour cent sous le budget.
acima | au-dessus | Lieu | Acima do vilarejo há um castelo antigo. | Au-dessus du village se dresse un vieux château.
ainda assim | néanmoins (soutenu) | Liaison | A crítica foi dura, mas ainda assim justa. | La critique était dure, néanmoins justifiée.
aos poucos | peu à peu | Temps | A frigideira está a esquentar aos poucos. | La poêle chauffe lentement.
aparentemente | apparemment | Doute | Aparentemente, está tudo em ordem. | Apparemment, tout est en ordre.
aqui no país | dans ce pays, chez nous | Lieu | Por aqui a gorjeta é opcional. | Dans ce pays, le pourboire est facultatif. | ex?
até agora | jusqu'à présent | Temps | Até agora não houve reclamações. | Jusqu'à présent, il n'y a eu aucune plainte.
até aqui | jusqu'ici | Temps | Lutamos muito para chegar até aqui. | Nous avons beaucoup lutté pour arriver jusqu'ici.
basicamente | en gros | Liaison | Basicamente, há duas opções. | En gros, il y a deux options.
categoricamente | catégoriquement | Manière | Ele negou categoricamente. | Il l'a nié catégoriquement.
com boa vontade | avec bienveillance | Manière | O chefe recebeu a proposta com boa vontade. | Le patron a accueilli la proposition avec bienveillance.
com consideração | avec égards | Manière | Por favor, tenham consideração com os vizinhos. | Veuillez vous comporter avec égards envers les voisins. | ex?
com determinação | avec détermination | Manière | O governo reagiu à crise com determinação. | Le gouvernement a réagi à la crise avec détermination.
com firmeza | avec constance, rigoureusement | Manière | Ele persegue os seus objetivos com firmeza. | Il poursuit ses objectifs avec constance.
com insistência | avec insistance | Manière | Ela alertou com insistência contra a reforma. | Elle a mis en garde avec insistance contre les travaux.
com persistência | avec ténacité | Manière | Ela insistiu nas perguntas com persistência. | Elle a insisté avec ténacité.
com prudência | avec circonspection | Manière | A motorista reagiu com prudência. | La conductrice a réagi avec circonspection.
com zelo | consciencieusement | Manière | Ela faz a ata com todo o zelo. | Elle tient le procès-verbal consciencieusement. | ex?
como se sabe | comme chacun sait | Liaison | Como se sabe, o alemão tem quatro casos. | Comme chacun sait, l'allemand a quatre cas.
concretamente | concrètement | Liaison | Concretamente, faltam duas assinaturas. | Concrètement, il manque deux signatures.
curiosamente | curieusement | Liaison | Curiosamente, ninguém tinha notado. | Curieusement, personne ne l'avait remarqué.
daí em diante | désormais | Temps | Daí em diante passaram a valer regras mais rígidas. | Désormais, des règles plus strictes s'appliquaient.
de antemão | d'avance | Temps | Obrigado desde já. | Merci d'avance. | ex?
de certa forma | en quelque sorte | Liaison | De certa forma ele é a cabeça do projeto. | Il est en quelque sorte la tête du projet.
de certo modo | dans une certaine mesure | Liaison |  |  | ex=?
de forma alguma | point du tout | Liaison | O problema não está resolvido de forma alguma. | Le problème n'est point du tout résolu.
de longe | de loin | Quantité | Esta é de longe a melhor solução. | C'est de loin la meilleure solution.
de modo algum | nullement | Nuance | Isso não é de modo algum óbvio. | Cela ne va nullement de soi.
de próprio punho | de sa propre main | Manière | O requerimento precisa de ser assinado de próprio punho. | La demande doit être signée de sa propre main.
de qualquer forma | de toute façon | Nuance | Eu já queria ir embora mais cedo de qualquer forma. | Je voulais de toute façon partir plus tôt.
de qualquer jeito | de toute manière | Nuance | Ele já sabia disso de qualquer jeito. | Il le savait de toute manière déjà.
demasiado | par trop | Quantité | A explicação foi complicada demais. | L'explication était par trop compliquée. | ex?
desmedidamente | démesurément | Quantité | Ele ficou profundamente decepcionado. | Il était démesurément déçu. | ex?
discretamente | discrètement | Manière | Ele saiu da sala discretamente. | Il a quitté la salle discrètement.
durante décadas | pendant des décennies | Temps | A fábrica ficou vazia durante décadas. | L'usine est restée vide pendant des décennies.
durante o dia | pendant la journée | Temps | Durante o dia não há ninguém em casa. | Pendant la journée, il n'y a personne à la maison.
em casa | à la maison | Lieu | No fim de semana preferimos ficar em casa. | Le week-end, nous préférons rester à la maison.
em essência | en substance | Manière | Em essência ele disse a mesma coisa. | Il a dit en substance la même chose.
em excesso | excessivement | Quantité | Não se deve usar sal em excesso. | Il ne faut pas utiliser excessivement de sel.
em linhas gerais | dans les grandes lignes | Liaison | Em linhas gerais, o plano é bom. | Dans les grandes lignes, le plan est bon.
em outros lugares | ailleurs | Lieu | Em outros lugares os rendas são ainda mais altos. | Ailleurs, les loyers sont encore plus élevés.
em que medida | dans quelle mesure | Question | Em que medida isso afeta o nosso departamento? | Dans quelle mesure cela concerne-t-il notre service ?
em quê | en quoi | Question | Em que consiste a diferença? | En quoi consiste la différence ? | ex?
em sua maioria | pour la plupart | Quantité | Os participantes eram, na sua maioria, estudantes. | Les participants étaient pour la plupart des étudiants. | ex?
em última análise | en définitive | Liaison | Em última análise, quem decide é o cliente. | En définitive, c'est le client qui décide.
essencialmente | essentiellement | Liaison | É essencialmente o mesmo problema. | C'est essentiellement le même problème.
felizmente | heureusement | Liaison | Felizmente ninguém se feriu. | Heureusement personne n'a été blessé.
francamente | franchement | Liaison | Francamente, não me convence. | Franchement, ça ne me convainc pas.
gradualmente | progressivement | Manière | A situação melhora gradualmente. | La situation s'améliore progressivement.
hesitante | avec hésitation | Manière | Ele respondeu à pergunta hesitante. | Il a répondu à la question avec hésitation.
há muito tempo | depuis longtemps | Temps | O problema já existia há muito tempo. | Le problème existait déjà depuis longtemps.
há pouco tempo | il y a peu | Temps | Há pouco tempo saiu um estudo novo sobre isso. | Il y a peu, une nouvelle étude est parue à ce sujet.
inclusive | même | Liaison | Até os especialistas enganam-se. | Même les experts se trompent. | ex?
inevitavelmente | inévitablement | Manière | Inevitavelmente, os preços vão subir. | Inévitablement, les prix vont augmenter.
justamente | justement | Liaison | Era justamente disso que eu queria falar. | C'est précisément de ça que je voulais parler.
lamentavelmente | malheureusement | Liaison | Lamentavelmente não podemos ajudá-lo. | Malheureusement nous ne pouvons pas vous aider.
logicamente | logiquement | Cause et conséquence | Coerentemente, o projeto foi interrompido. | Logiquement, le projet a été arrêté. | ex?
minimamente | de façon minime | Quantité | Os custos subiram só minimamente. | Les coûts n'ont augmenté que de façon minime.
muitíssimo | vachement, terriblement | Quantité | Estamos muitíssimo satisfeitos com o resultado. | Nous sommes on ne peut plus satisfaits du résultat.
necessariamente | nécessairement | Cause et conséquence | Mais pessoal não significa necessariamente um trabalho melhor. | Plus de personnel ne signifie pas nécessairement un meilleur travail.
nesse meio-tempo | dans l'intervalle | Temps | Nesse meio-tempo o software foi atualizado. | Dans l'intervalle, le logiciel a été mis à jour.
nesse sentido | à cet égard | Cause et conséquence | Nesse sentido ela tem toda a razão. | À cet égard, elle a tout à fait raison.
o quê | sur quoi, à quoi | Question |  |  | ex=?
palavra por palavra | mot pour mot | Manière | Ela traduziu a frase palavra por palavra. | Elle a traduit la phrase mot pour mot.
para a frente | en avant | Lieu | O projeto finalmente está a andar. | Le projet avance enfin. | ex?
para isso | à cette fin | Cause et conséquence | Para isso precisamos de uma autorização por escrito. | À cette fin, nous avons besoin d'une autorisation écrite.
passo a passo | par étapes | Manière | Seguimos a receita passo a passo. | Nous avons suivi la recette pas à pas.
pela experiência | d'expérience | Liaison | Pela experiência, isso demora mais do que o planeado. | D'expérience, cela dure plus longtemps que prévu.
pelo quê | par quoi | Question | O que causou o estrago? | Par quoi le dommage a-t-il été causé ? | ex?
por acaso | peut-être | Doute | Encontramo-nos por acaso no elevador hoje de manhã. | Nous nous sommes croisés dans l'ascenseur ce matin.
por assim dizer | pour ainsi dire | Liaison | Ela cresceu, por assim dizer, junto com o clube. | Elle a pour ainsi dire grandi avec le club.
por enquanto | pour l'instant | Temps | Por enquanto o projeto fica parado. | Le projet reste en suspens pour l'instant.
por necessidade | par nécessité, faute de mieux | Manière | Fomos obrigados a refazer os planos. | Nous avons dû revoir nos plans par nécessité. | ex?
por precaução | par précaution | Cause et conséquence | Leva um guarda-chuva por precaução. | Prends un parapluie par précaution.
por segurança | par sécurité | Cause et conséquence | Por segurança vou ligar mais uma vez. | Par sécurité, je rappelle encore une fois.
por um lado | d'une part | Liaison | Por um lado o emprego é bem pago, por outro é muito exigente. | D'une part le poste est bien payé, d'autre part très exigeant.
precisamente | précisément | Liaison | Era justamente disso que eu queria falar. | C'est précisément de ça que je voulais parler. | ex?
presumivelmente | prétendument | Doute | Supostamente aconteceu à noite. | Cela se serait prétendument produit la nuit. | ex?
principalmente | principalement | Liaison | O público era principalmente jovem. | Le public était principalement jeune.
repetidamente | à maintes reprises | Fréquence | Ele foi avisado sobre isso repetidas vezes. | On le lui a signalé à maintes reprises. | ex?
resumindo | bref | Cause et conséquence | Resumindo, o plano não funcionou. | Bref, le plan n'a pas fonctionné.
sem deixar dúvidas | sans ambiguïté | Manière | Ele disse não sem deixar dúvidas. | Il a dit non sans ambiguïté.
tacitamente | tacitement | Manière | O contrato é renovado automaticamente. | Le contrat est reconduit tacitement. | ex?
temporariamente | temporairement | Temps | O elevador está temporariamente fora de serviço. | L'ascenseur est temporairement hors service.
terminantemente | catégoriquement, sans appel | Manière | Ele recusou terminantemente. | Il a refusé sans appel.
"""

# « expression | traduction | categorie | phrase | sa traduction ».
EXPRESSIONS = """
a duras penas | à grand-peine | Tournures | Chegamos a duras penas. | Nous sommes arrivés à grand-peine.
a fim de | afin de | Discuter | Reuniram-se a fim de esclarecer. | Ils se sont réunis afin de l'éclaircir.
a todo vapor | en plein essor, battant son plein | Au quotidien | Os preparativos estão a todo vapor. | Les préparatifs battent leur plein.
acenar com | faire miroiter | Tournures | Acenaram para ele com uma promoção. | On lui a fait miroiter une promotion.
afinal de contas | après tout | Discuter | Afinal de contas, a decisão é dele. | Après tout, c'est sa décision.
ainda assim | toutefois | Discuter | O preço é alto, mas ainda assim vale a pena. | Le prix est élevé, toutefois cela en vaut la peine.
apertar o cinto | se serrer la ceinture | Au quotidien | Este ano vamos ter de apertar o cinto. | Cette année, nous devons nous serrer la ceinture.
apesar de | malgré | Discuter | Saímos apesar da chuva. | Nous sommes sortis malgré la pluie.
colocar em discussão | soumettre à la discussion | Tournures | Eu gostaria de colocar este ponto em discussão. | Je voudrais soumettre ce point à la discussion.
com todo o respeito | avec tout le respect que je vous dois | Discuter | Com todo o respeito, eu vejo de outra forma. | Avec tout le respect que je vous dois, je vois cela autrement.
como se sabe | comme chacun sait | Discuter | Como se sabe, a prática é o melhor professor. | Comme chacun sait, la pratique est le meilleur maître.
compartilho dessa opinião | je partage cet avis | Donner son avis | Compartilho totalmente dessa opinião. | Je partage cet avis sans réserve.
conseguir pagar as contas | joindre les deux bouts | Au quotidien | Com este salário mal dá para pagar as contas. | Avec ce salaire, on peine à joindre les deux bouts.
contanto que | pourvu que | Discuter | Ele aceita, contanto que não discutam. | Il accepte pourvu qu'on ne se dispute pas.
contra as expectativas | contrairement aux attentes | Discuter | Contra as expectativas, o faturamento subiu. | Contrairement aux attentes, le chiffre d'affaires a augmenté.
custe o que custar | coûte que coûte | Au quotidien | Ele queria impor isso custe o que custar. | Il voulait l'imposer coûte que coûte.
dar como certo | tenir pour acquis | Tournures | Não dê isso como certo. | Ne le tiens pas pour acquis.
dar um jeito | remédier à la situation | Tournures | Aqui é urgente dar um jeito. | Il faut ici remédier d'urgence à la situation.
de acordo com | conformément à | Discuter | De acordo com a lei, é preciso de avisar. | Conformément à la loi, il faut prévenir.
de cima a baixo | de fond en comble | Au quotidien | A casa foi reformada de cima a baixo. | La maison a été rénovée de fond en comble.
de qualquer forma | de toute façon | Discuter | De qualquer forma, já é tarde. | De toute façon, il est déjà tard.
definir os rumos | donner l'orientation | Tournures | Agora estão a ser definidos os rumos do futuro. | C'est maintenant qu'on donne l'orientation pour l'avenir.
desde que | pour autant que | Discuter | Nós vamos, desde que o tempo ajude. | Nous viendrons, pour autant que le temps le permette.
devido a | en raison de | Discuter | Ele atrasou-se devido ao trânsito. | Il a été retardé en raison du trafic.
diante de | compte tenu de | Discuter | Diante da situação, continuamos cautelosos. | Compte tenu de la situation, nous restons prudents.
dito isso | cela dit | Nuance | Dito isso, há outro problema. | Cela dit, il y a un autre problème.
em cima da hora | à la dernière minute | Au quotidien | O compromisso foi cancelado em cima da hora. | Le rendez-vous a été annulé à la dernière minute.
em consequência disso | par conséquent | Discuter | Choveu muito e, em consequência disso, o jogo foi cancelado. | Il pleuvait fort, par conséquent le match a été annulé.
em princípio | en principe | Nuance | A princípio saímos na quinta. | En principe nous partons jeudi.
em que posso ajudar | en quoi puis-je vous aider ? | Bavarder | Boa tarde, em que posso ajudar? | Bonjour, en quoi puis-je vous aider ?
em teoria | en théorie | Nuance | Em teoria o sistema funciona sozinho. | En théorie le système fonctionne tout seul.
em vez de | au lieu de | Discuter | Ligue em vez de escrever. | Appelle au lieu d'écrire.
empurrar com a barriga | remettre aux calendes grecques | Au quotidien | Não empurra a decisão com a barriga. | Ne remets pas la décision aux calendes grecques.
encher a barriga | s'en mettre plein la panse | Tournures | Enchemos a barriga no jantar. | On s'en est mis plein la panse au dîner.
enfiar a cabeça na areia | faire l'autruche | Réagir | Enfiar a cabeça na areia não ajuda. | Faire l'autruche n'aide en rien.
enfrentar resistência | se heurter à une résistance | Tournures | A proposta enfrentou forte resistência. | La proposition s'est heurtée à une vive résistance.
engolir o sapo | avaler la pilule | Réagir | Vamos ter de engolir o sapo e pagar. | Il faut avaler la pilule et payer.
entrar em vigor | entrer en vigueur | Tournures | A lei entra em vigor em janeiro. | La loi entre en vigueur en janvier.
estar contra a parede | être dos au mur | Réagir | A empresa está contra a parede. | L'entreprise est dos au mur.
estar de acordo | être d'accord entre soi | Donner son avis | Neste ponto estamos de acordo. | Nous sommes d'accord sur ce point.
estar em discussão | être en discussion | Tournures | Esta questão não está em discussão hoje. | Cette question n'est pas en discussion aujourd'hui.
estar firme no posto | être sur le pont | Tournures | Ela continua firme no posto depois de vinte anos. | Il est toujours sur le pont après vingt ans.
estar sob pressão | être sous pression | Réagir | A equipa está sob pressão há semanas. | L'équipe est sous pression depuis des semaines.
examinar com lupa | examiner de près | Tournures | O relatório foi examinado com lupa. | Le rapport a été examiné de très près.
falar pelos cotovelos | être un moulin à paroles | Tournures | A minha vizinha fala pelos cotovelos. | Ma voisine est un moulin à paroles.
falar às claras | parler franchement | Donner son avis | Vamos falar às claras: isso não basta. | Parlons franchement : ça ne suffit pas.
fazer as coisas direito | faire les choses à fond | Au quotidien | É-se para fazer, vamos fazer direito. | Tant qu'à faire, faisons les choses à fond.
fazer um balanço | tirer le bilan | Discuter | Vamos fazer o balanço deste ano. | Tirons le bilan de cette année.
fazer vista grossa | fermer les yeux | Tournures | O porteiro fez vista grossa. | Le concierge a fermé les yeux.
ficar de queixo caído | rester bouche bée | Tournures | Fiquei de queixo caído ao vê-lo. | Je suis resté bouche bée en le voyant.
ficar louco de alegria | être fou de joie | Réagir | As crianças ficaram loucas de alegria. | Les enfants étaient fous de joie.
graças a | grâce à | Discuter | Chegamos graças ao teu mapa. | Nous sommes arrivés grâce à ta carte.
indo direto ao ponto | pour résumer l'essentiel | Discuter | Indo direto ao ponto: falta dinheiro. | Pour résumer l'essentiel : il manque de l'argent.
ir além do escopo | dépasser le cadre | Discuter | Isso iria além do escopo desta reunião. | Cela dépasserait le cadre de cette réunion.
ir direto ao ponto | aller droit au but | Tournures | Vamos direto ao ponto: quanto custa? | Allons droit au but, combien ça coûte ?
isso já é outra história | c'est une autre histoire | Donner son avis | Vale-se a pena, isso já é outra história. | Savoir si cela en vaut la peine est une autre histoire.
isso não muda o facto | cela n'y change rien | Discuter | Isso não muda o facto de que o prazo vale. | Cela n'y change rien : le délai s'applique.
isto é | c'est-à-dire | Discuter | Falta uma assinatura, isto é, não está completo. | Il manque une signature, c'est-à-dire que ce n'est pas complet.
já ter passado o pior | avoir passé le plus dur | Réagir | Depois da operação ela já passou o pior. | Après l'opération, elle a passé le plus dur.
levar um balde de água fria | être déçu | Tournures | Ele levou um belo balde de água fria. | Il a été bien déçu.
mais cedo ou mais tarde | tôt ou tard | Au quotidien | Mais cedo ou mais tarde vamos ter de nos mudar. | Tôt ou tard, nous devrons déménager.
mais ou menos | plus ou moins | Discuter | Levamos mais ou menos uma hora. | Nous avons mis plus ou moins une heure.
manter silêncio | garder le silence | Réagir | Sobre as acusações ele mantém silêncio. | Face aux accusations, il garde le silence.
manter-se à tona | se maintenir à flot | Au quotidien | A empresa está mal se mantendo à tona. | L'entreprise se maintient tout juste à flot.
mesmo assim | malgré tout | Discuter | É caro; mesmo assim, ele comprou. | C'est cher ; malgré tout, il l'a acheté.
morder a língua | se mordre la langue | Réagir | Tive de morder a língua. | J'ai dû me mordre la langue.
mover céus e terras | remuer ciel et terre | Au quotidien | Ela moveu céus e terras para ajudar. | Elle a remué ciel et terre pour aider.
muito prazer em conhecê-lo | ravi de faire votre connaissance | Bavarder | Muito prazer em conhecê-lo, senhor Berger. | Ravi de faire votre connaissance, Monsieur Berger.
na medida em que | dans la mesure où | Discuter | Isso vale na medida em que os dados estejam certos. | Cela vaut dans la mesure où les données sont exactes.
no fim das contas | au bout du compte | Discuter | No fim das contas, economizamos. | Au bout du compte, nous avons économisé.
no final das contas | au bout du compte | Discuter | No final das contas, todos se beneficiaram. | Au bout du compte, tout le monde en a profité.
note-se bem | notons-le bien | Discuter | Isso vale, note-se bem, só para clientes novos. | Cela vaut, notons-le bien, uniquement pour les nouveaux clients.
num piscar de olhos | en un clin d'œil | Tournures | Ele terminou num piscar de olhos. | Il a fini en un clin d'œil.
não dá para deixar isso passar assim | on ne peut pas laisser dire cela | Donner son avis | Não dá para deixar isso passar assim, falta contexto. | On ne peut pas laisser dire cela, le contexte manque.
não dá para negar | on ne peut le nier | Donner son avis | O trabalho foi grande, não dá para negar. | L'effort a été considérable, on ne peut le nier.
não há nada a acrescentar | il n'y a rien à ajouter | Donner son avis | Bem dito — não há nada a acrescentar. | Bien dit — il n'y a rien à ajouter.
não pode ser descartado | indéniable | Donner son avis | Este argumento não pode ser descartado. | Cet argument est indéniable.
não pregar o olho | ne pas fermer l'œil | Tournures | Não preguei o olho a noite toda. | Je n'ai pas fermé l'œil de la nuit.
não tem como escapar disso | on ne peut pas y couper | Donner son avis | Precisamos de economizar, não tem como escapar disso. | Nous devons économiser, on ne peut pas y couper.
não ter a menor ideia | n'avoir aucune idée | Tournures | Não tenho a menor ideia de onde está. | Je n'ai aucune idée d'où il est.
não ter papas na língua | ne pas mâcher ses mots | Tournures | A minha avó não tem papas na língua. | Ma grand-mère ne mâche pas ses mots.
o essencial | l'essentiel, la clé | Discuter | Praticar com regularidade é o essencial. | S'exercer régulièrement, c'est l'essentiel.
o pior ainda está por vir | le pire reste à venir | Réagir | Não comemora cedo demais, o pior ainda está por vir. | Ne te réjouis pas trop vite, le pire reste à venir.
olhando mais de perto | à y regarder de plus près | Discuter | Olhando mais de perto, isso não é verdade. | À y regarder de plus près, c'est faux.
olhando para trás | rétrospectivement | Discuter | Olhando para trás, a decisão foi certa. | Rétrospectivement, la décision était juste.
ouso dizer | j'ose affirmer | Donner son avis | Ouso dizer que vai funcionar. | J'ose affirmer que cela fonctionne.
para dizer o mínimo | c'est le moins qu'on puisse dire | Discuter | Isso foi, para dizer o mínimo, imprudente. | C'était maladroit, c'est le moins qu'on puisse dire.
para não dizer | pour ne pas dire | Discuter | Isso foi imprudente, para não dizer irresponsável. | C'était imprudent, pour ne pas dire négligent.
pelo visto | apparemment | Nuance | Pelo visto ele não virá. | Apparemment il ne viendra pas.
perder a calma | perdre son calme | Réagir | Pouco antes do final ele perdeu a calma. | Juste avant la fin, il a perdu son calme.
perder o fio da meada | perdre le fil | Réagir | Na apresentação ela perdeu o fio da meada. | Pendant la présentation, elle a perdu le fil.
por causa de | à cause de | Discuter | Fecharam por causa das obras. | Ils ont fermé à cause des travaux.
por via das dúvidas | au cas où | Au quotidien | Leve o guarda-chuva por via das dúvidas. | Prends le parapluie au cas où.
procurar pelo em ovo | chercher midi à quatorze heures | Tournures | Não procure pelo em ovo. | Ne cherche pas midi à quatorze heures.
pura e simplesmente | purement et simplement | Discuter | Isso está pura e simplesmente errado. | C'est purement et simplement faux.
pôr as cartas na mesa | jouer cartes sur table | Tournures | Vamos pôr as cartas na mesa. | Jouons cartes sur table.
pôr obstáculos no caminho | mettre des bâtons dans les roues | Réagir | Puseram obstáculos no caminho dela em todo lugar. | On lui a mis des bâtons dans les roues partout.
pôr os pingos nos is | faire table rase | Au quotidien | Está na hora de pôr os pingos nos is. | Il est temps de faire table rase.
receber atenção | être remarqué | Tournures | O estudo dele recebeu atenção internacional. | Son étude a été remarquée à l'international.
refletir-se em | se traduire par | Tournures | O sucesso reflete-se nos números. | Le succès se traduit par les chiffres.
refrescar a memória | mettre sur la voie, rafraîchir la mémoire | Réagir | Posso refrescar a tua memória? | Puis-je te rafraîchir la mémoire ?
se não me engano | si je ne me trompe pas | Nuance | Se não me engano, já nos conhecemos. | Si je ne me trompe pas, nous nous connaissons déjà.
sem falar de | sans parler de | Discuter | Custa tempo, sem falar no dinheiro. | Cela coûte du temps, sans parler de l'argent.
ser doido de pedra | être complètement fou | Tournures | Ele é doido de pedra, mas é genial. | Il est complètement fou, mais il est génial.
ser muito procurado | être sollicité | Tournures | O serviço é muito procurado. | Le service est fortement sollicité.
ser uma pedra no sapato | être une épine dans le pied | Réagir | O prédio novo é uma pedra no sapato dos vizinhos. | Le nouveau bâtiment est une épine dans le pied des voisins.
ser unha e carne | être comme les deux doigts de la main | Tournures | Esses dois são unha e carne. | Ces deux-là sont inséparables.
ter como consequência | avoir pour conséquence | Tournures | A reforma teve como consequência custos mais altos. | La réforme a eu pour conséquence des coûts plus élevés.
tirar a situação do buraco | sortir de l'ornière | Au quotidien | No fim ela teve de tirar a situação do buraco. | À la fin, c'est elle qui a dû sortir l'affaire de l'ornière.
tomar posição | prendre position | Tournures | O partido teve de tomar uma posição clara. | Le parti a dû prendre clairement position.
trabalhar de mãos dadas | travailler main dans la main | Tournures | Os dois departamentos trabalham de mãos dadas. | Les deux services travaillent main dans la main.
tudo depende de | tout dépend de | Nuance | Tudo depende do orçamento. | Tout dépend du budget.
valer a pena | valoir la peine | Au quotidien | A viagem vale a pena. | Le voyage vaut la peine.
varrer para debaixo do tapete | passer sous silence | Discuter | Não se pode varrer este problema para debaixo do tapete. | On ne doit pas passer ce problème sous silence.
ver com outros olhos | voir d'un autre œil | Discuter | Desde então vejo a coisa com outros olhos. | Depuis, je vois la chose d'un autre œil.
às pressas | précipitamment | Au quotidien | Eles mudaram-se às pressas. | Ils ont déménagé précipitamment.
é questão de ponto de vista | c'est une question de point de vue | Donner son avis | É-se bonito, é questão de ponto de vista. | Savoir si c'est beau est une question de point de vue.
é óbvio | cela va de soi | Discuter | É óbvio que precisamos de agir. | Il va de soi que nous devons agir.
"""
