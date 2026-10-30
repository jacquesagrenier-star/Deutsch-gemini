# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du A2 portugais. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que mots_a1.py et phrases_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'A2'

# « infinitif | traduction | phrase | sa traduction | drapeaux » (formes : irreguliers.py).
VERBES = """
abaixar-se | se baisser | Eu abaixo-me para amarrar os sapatos. | Je me baisse pour lacer mes chaussures. | pron
abrir mão de | renoncer | Abro mão de doces. | Je renonce aux sucreries.
acabar | finir | Acabo o trabalho às seis. | Je finis le travail à six heures.
acalmar-se | se calmer | Acalme-se, não foi nada. | Calme-toi, il n'y a rien. | pron
acampar | camper | Acampamos ao lado do lago. | Nous campons près du lac.
aceitar | accepter | Ele aceitou o convite na hora. | Il a accepté l'invitation tout de suite.
acender | allumer | Acende a luz, por favor. | Allume la lumière, s'il te plaît.
aconselhar | conseiller | O médico aconselha-me a fazer mais desporto. | Le médecin me conseille de faire plus de sport.
acontecer | se passer, arriver | Isso acontece com frequência. | Ça arrive souvent.
acostumar-se | s'habituer | Eu acostumei-me rápido com o horário. | Je me suis vite habitué à l'horaire. | pron
acrescentar | ajouter | Acrescente um pouco de sal. | Ajoute un peu de sel.
admirar | admirer | Admiro a paciência dela. | J'admire sa patience.
adoecer | tomber malade | Ele adoeceu bem antes das férias. | Il est tombé malade juste avant les vacances.
adorar | adorer | Ela adora os domingos no campo. | Elle adore les dimanches à la campagne.
adormecer | s'endormir | Adormeço na hora. | Je m'endors tout de suite.
afastar | éloigner | Afaste a cadeira do radiador. | Éloigne la chaise du radiateur.
agir | agir | Eu ajo na hora. | J'agis tout de suite.
agradar | plaire | A resposta dele não agradou a ninguém. | Sa réponse n'a plu à personne.
agradecer | remercier | Eu agradeço-te pela ajuda. | Je te remercie pour ton aide.
aguentar | supporter | Não aguento mais esse barulho. | Je ne supporte plus ce bruit.
alcançar | atteindre | Eu alcanço o meu objetivo. | J'atteins mon objectif.
alegrar | réjouir | Um pouco de música alegraria a festa. | Un peu de musique égaierait la fête.
alegrar-se | se réjouir | Eu cantaria uma música mais alegre. | Moi, je chanterais une chanson plus gaie. | pron
alimentar | nourrir | Alimente o cão de manhã. | Nourris le chien le matin.
alugar | louer | Alugamos um apartamento no centro. | Nous louons un appartement au centre.
amadurecer | mûrir | Os tomates amadurecem em agosto. | Les tomates mûrissent en août.
andar a cavalo | monter à cheval | A minha irmã anda a cavalo todo sábado. | Ma sœur monte à cheval tous les samedis.
anunciar | annoncer | Anunciam o voo pelo alto-falante. | Ils annoncent le vol au haut-parleur.
apaixonar-se | tomber amoureux | Ele apaixonou-se no verão. | Il est tombé amoureux l'été. | pron
aparecer | apparaître, paraître | Ele apareceu de repente. | Il est apparu soudainement.
apertar | serrer, appuyer | Aperte o botão vermelho. | Appuie sur le bouton rouge.
aplaudir | applaudir | Todos aplaudimos no final. | Nous avons tous applaudi à la fin.
apoiar | soutenir | A minha família sempre me apoia. | Ma famille me soutient toujours.
aposentar-se | prendre sa retraite | Ele aposenta-se no ano que vem. | Il prend sa retraite l'an prochain. | pron
apressar-se | se dépêcher | Eu apressei-me para apanhar o comboio. | Je me suis dépêché pour attraper le train. | pron
aproximar | approcher | Ele aproximou a cadeira de mim com um sorriso. | Il m'a approché la chaise avec un sourire.
aproximar-se | s'approcher | Um senhor aproximou-se para perguntar as horas. | Un monsieur s'est approché pour demander l'heure. | pron
aquecer | chauffer | Aquecemos a casa com energia solar. | Nous avons chauffé la maison à l'énergie solaire.
arejar | aérer | Ela arejou a sala antes da reunião. | Elle a aéré la pièce avant la rencontre.
arquivar | classer | Arquivo os documentos por data. | Je classe les documents par date.
arranjar | réparer, arranger | Vão arranjar o elevador na semana que vem. | Ils répareront l'ascenseur la semaine prochaine.
assar | cuire au four, faire (un gâteau) | A minha avó assava bolachas aos domingos. | Ma grand-mère faisait des biscuits au four le dimanche.
assustar | faire peur | O barulho assustou o gato. | Le bruit a fait peur au chat.
assustar-se | prendre peur | Eu assustei-me com o barulho. | J'ai eu peur à cause du bruit. | pron
aterrissar | atterrir | Aterrissamos em Lima às seis da manhã. | Nous avons atterri à Lima à six heures du matin.
atrasar-se | être en retard | Hoje vou atrasar-me um pouco. | Je suis un peu en retard aujourd'hui. | pron
atrever-se | oser | Não me atrevo a dizer isso a ele. | Je n'ose pas le lui dire. | pron
atuar | jouer (un rôle) | Ele atua em uma peça de teatro. | Il joue dans une pièce de théâtre.
aumentar | augmenter | A empresa aumenta os preços. | L'entreprise augmente les prix.
avaliar | juger | Eu avalio a situação de forma realista. | Je juge la situation de façon réaliste.
avançar | avancer | O projeto avança devagar. | Le projet avance lentement.
avisar | prévenir | Avise-me quando chegar. | Préviens-moi quand tu arrives.
baixar | télécharger | Eu baixaria o filme antes do voo. | Moi, je téléchargerais le film avant le vol.
bastar | suffire | Basta uma assinatura. | Une signature suffit.
bater | heurter | O carro bateu em um muro. | La voiture a heurté un mur.
beijar | embrasser | Eles beijaram-se na porta. | Ils se sont embrassés sur le pas de la porte.
brigar | se disputer | Eles brigaram com os vizinhos. | Ils se disputaient avec les voisins.
brilhar | sembler, briller | Hoje o sol está a brilhar. | Le soleil brille aujourd'hui.
brindar | trinquer | Brindamos com cava. | Nous trinquons au cava.
bronzear-se | bronzer | Ela bronzeia-se muito rápido. | Elle bronze très vite. | pron
caber | tenir (dans) | Não cabe mais nada na mala. | Rien ne tient de plus dans la valise.
cair | baisser, couler | Os preços estão a cair. | Les prix baissent.
calar-se | se taire | Em criança, ele nunca se calava. | Enfant, il ne se taisait jamais. | pron
calcular | calculer | Eu calculo os custos. | Je calcule les coûts.
caminhar | marcher | Caminhamos até a praia. | Nous avons marché jusqu'à la plage.
cancelar | annuler | Cancelaram o voo por causa da neblina. | Ils ont annulé le vol à cause du brouillard.
cancelar a inscrição | se désinscrire | Cancelo a minha inscrição no curso. | Je me désinscris du cours.
candidatar-se | postuler | Eu candidato-me à vaga. | Je postule pour le poste. | pron
cansar | fatiguer | A viagem cansou-me muito. | Le voyage m'a beaucoup fatigué.
casar-se | se marier | Eles casam-se em setembro. | Ils se marient en septembre. | pron
celebrar | célébrer, fêter | Celebramos o casamento no campo. | Nous avons célébré le mariage à la campagne.
cobrir | couvrir ; mettre (la table) | Ela cobriu a criança com um cobertor. | Elle a couvert l'enfant d'une couverture.
colar | coller, frapper | Colo a foto no caderno. | Je colle la photo dans le cahier.
colocar | placer | Coloque os livros na prateleira. | Place les livres sur l'étagère.
combinar | se donner rendez-vous | Combinamos às sete na praça. | On se retrouve à sept heures sur la place.
comentar | commenter | Comentamos a notícia na aula. | Nous commentons la nouvelle en classe.
comparar | comparer | Eu comparo os preços. | Je compare les prix.
compartilhar | partager | Compartilhei a foto com a família toda. | J'ai partagé la photo avec toute la famille.
competir | concourir | Ela competiu nos Jogos Olímpicos de 2016. | Elle a concouru aux Jeux olympiques de 2016.
completar | compléter | Completei o curso em seis meses. | J'ai terminé le cours en six mois.
comportar-se | se comporter | Ele comporta-se muito bem na aula. | Il se comporte très bien en classe. | pron
comunicar | signaler | Comunico o ocorrido. | Je signale l'incident.
concentrar-se | se concentrer | Eu concentro-me no trabalho. | Je me concentre sur le travail. | pron
conectar | connecter | Conecto o telemóvel ao wi-fi. | Je connecte le portable au wifi.
conferir | contrôler | Eu confiro as bilhetes. | Je contrôle les billets.
confiar | faire confiance | O meu avô não confiava nos bancos. | Mon grand-père ne faisait pas confiance aux banques.
congelar | congeler | Congelo o pão que sobra. | Je congèle le pain qui reste.
conhecer-se | se rencontrer, se connaître | Nós conhecemo-nos em Lisboa. | Nous nous sommes rencontrés à Lisboa. | pron
conseguir | réussir à, obtenir | Ele conseguiu terminar a faculdade. | Il a réussi à finir ses études.
constatar | constater | Constato um erro. | Je constate une erreur.
construir | construire | Eles estão a construir uma casa nova. | Ils construisent une nouvelle maison.
consumir | consommer | Consumimos menos água no inverno. | Nous consommons moins d'eau en hiver.
conter | contenir | A bebida contém açúcar. | La boisson contient du sucre.
continuar | continuer | Amanhã continuamos a conversa. | Nous continuons la conversation demain.
contradizer | contredire | Não te contradigo. | Je ne te contredis pas.
conversar | discuter | Conversamos com os vizinhos. | Nous avons discuté avec les voisins.
convidar | inviter | Fomos convidados para uma festa no sábado. | On nous a invités à une fête samedi.
conviver | vivre ensemble | Convivi com pessoas de muitos países. | J'ai vécu avec des gens de nombreux pays.
corrigir | corriger | A professora corrige os exercícios. | La professeure corrige les exercices.
cortar | couper | Corto a cebola em pedaços. | Je coupe l'oignon en morceaux.
costumar | avoir l'habitude de | Costumo tomar pequeno-almoço às oito. | J'ai l'habitude de déjeuner à huit heures.
costurar | coudre | Costuro o botão hoje à noite. | Je couds le bouton ce soir.
crescer | grandir, pousser | A planta cresce muito rápido. | La plante pousse très vite.
criar | créer | Ele cria esculturas de metal. | Il crée des sculptures en métal.
criticar | critiquer | Ele critica o programa sem assistir. | Il critique l'émission sans l'avoir vue.
cuidar-se | prendre soin de soi | Cuide-se bem. | Prends bien soin de toi. | pron
curar | guérir, soigner | Sem a pomada não curaria tão rápido. | Sans la pommade, ça ne guérirait pas aussi vite.
dar bronca | gronder, râler | O chefe raramente dá bronca. | Le chef gronde rarement.
dar certo | réussir (impersonnel) | O bolo sempre dá certo para mim. | Le gâteau me réussit toujours.
dar de presente | offrir | Dou um livro de presente ao meu pai. | J'offre un livre à mon père.
dar os parabéns | féliciter | Parabéns pelo teu aniversário. | Je te félicite pour ton anniversaire.
decidir | décider | Decidimos ficar aqui. | Nous décidons de rester ici.
decidir-se | se décider | Eu decido-me pelo vestido azul. | Je me décide pour la robe bleue. | pron
decolar | décoller | O avião decola às nove. | L'avion décolle à neuf heures.
deixar | laisser | Deixe as chaves na mesa. | Laisse les clés sur la table.
demitir | licencier | Demitiram dois funcionários. | Ils ont licencié deux employés.
demorar | mettre du temps | O comboio demora duas horas. | Le train met deux heures.
denunciar | porter plainte | Denuncio o roubo amanhã. | Je déclare le vol demain.
depositar | déposer (de l'argent) | Deposito o cheque hoje. | Je dépose le chèque aujourd'hui.
descascar | éplucher | Descasque as batatas, por favor. | Épluche les pommes de terre, s'il te plaît.
descobrir | découvrir | Descobrimos um vilarejo lindo. | Nous avons découvert un village magnifique.
desculpar-se | s'excuser | Ele desculpou-se pelo atraso. | Il s'est excusé du retard. | pron
desejar | souhaiter | Desejo muita sorte a ele. | Je lui souhaite bonne chance.
desembrulhar | déballer | As crianças desembrulham os presentes. | Les enfants déballent les cadeaux.
desenvolver | développer | Ele desenvolveu um produto novo. | Il a développé un nouveau produit.
designar | désigner | Designam duas pessoas para o projeto. | On détache deux personnes pour le projet.
desligar | éteindre | Desligue a televisão, por favor. | Éteins la télévision, s'il te plaît.
despachar | enregistrer (les bagages) | Despacho a mala grande. | J'enregistre la grande valise.
despedir-se | dire au revoir | Eu despeço-me dos meus colegas. | Je dis au revoir à mes collègues. | pron
despir-se | se déshabiller | Temo que seja tarde demais. | Je crains qu'il ne soit trop tard. | pron
determinar | déterminer | O chefe determinava as regras. | Le patron a déterminé les règles.
dever dinheiro | devoir de l'argent | Ele deve-me dinheiro desde março. | Il me doit de l'argent depuis mars.
discutir | se disputer, discuter | Vamos discutir o assunto amanhã com calma. | Nous discuterons du sujet demain, calmement.
dividir | partager, diviser | Divido a minha comida. | Je partage mon repas.
embarcar | embarquer | Embarcamos pelo portão doze. | Nous embarquons porte douze.
embrulhar | emballer, mettre dans la valise | Eu embrulho o presente. | J'emballe le cadeau.
emprestar | prêter | A minha irmã emprestava-me os livros dela. | Ma sœur me prêtait ses livres.
empurrar | pousser | Empurre a porta com força. | Pousse la porte avec force.
encher | remplir | Encha a garrafa antes de sair. | Remplis la bouteille avant de partir.
encontrar-se | se retrouver, se voir | Nós encontramo-nos na semana passada. | Nous nous sommes vus la semaine dernière. | pron
enfiar | mettre, enfoncer ; être coincé | Enfiei uma farpa no dedo. | Je me suis enfoncé une écharde dans le doigt.
engolir | avaler | Engula o comprimido com água. | Avale le comprimé avec de l'eau.
ensaiar | répéter (en musique) | Ensaiamos às quintas. | Nous répétons le jeudi.
entediar | ennuyer | O filme entediou-nos. | Le film nous a ennuyés.
entrar | entrer | Entre, a porta está aberta. | Entre, la porte est ouverte.
entrar em | entrer dans | Eu entro na sala. | J'entre dans la pièce.
entregar | remettre, livrer | Entrego o pacote amanhã. | Je livre le colis demain.
envelhecer | vieillir | Todos envelhecemos. | Nous vieillissons tous.
escapar | s'échapper | O cão escapou do jardim. | Le chien s'est échappé du jardin.
escovar | brosser | Escovo os dentes três vezes por dia. | Je me brosse les dents trois fois par jour.
espantar | étonner | A memória dele espantou-nos. | Sa mémoire nous a étonnés.
estar certo | être exact, voter | Isso está certinho. | C'est exactement ça.
estender | étendre (le linge) | Estendi a roupa lavada hoje de manhã. | J'ai étendu la lessive ce matin.
esticar | étirer | Estiquei as pernas depois da viagem. | J'ai étiré mes jambes après le voyage.
estrear | sortir (un film) | Todo ano ela estreava um vestido na feira. | Chaque année, elle portait une nouvelle robe à la foire.
esvaziar | vider | Eu esvaziaria a gaveta antes de mover. | Moi, je viderais le tiroir avant de le déplacer.
evitar | éviter | Evito usar o carro na cidade. | J'évite d'utiliser la voiture en ville.
examinar | examiner | A médica examina o paciente. | La médecin examine le patient.
exigir | exiger | Os funcionários exigem um salário maior. | Les employés exigent plus de salaire.
existir | exister | Esta empresa existe desde 1990. | Cette entreprise existe depuis 1990.
expor | exposer | Ele expõe os seus quadros em março. | Il expose ses tableaux en mars.
fabricar | fabriquer | A empresa fabrica carros. | L'entreprise fabrique des voitures.
falar ao telefone | téléphoner | Estou a falar ao telefone com a minha mãe. | Je téléphone à ma mère.
falhar | échouer, tomber en panne | O motor falha a frio. | Le moteur défaille à froid.
faltar | manquer | Falta uma cadeira. | Il manque une chaise.
fantasiar-se | se déguiser | Nós fantasiamo-nos no carnaval. | Nous nous déguisons au carnaval. | pron
fazer baldeação | changer (de train, bus) | Eu faço baldeação em Porto. | Je change à Porto.
fazer churrasco | griller, faire un barbecue | No verão fizemos muitos churrascos no jardim. | En été, nous avons souvent fait un barbecue au jardin.
fazer o check-in | s'enregistrer | Fazemos o check-in às três. | Nous nous enregistrons à trois heures.
fazer trabalhos manuais | bricoler, faire des travaux manuels | As crianças fazem um cartão para a vovó. | Les enfants bricolent une carte pour mamie.
fazer trilha | randonner | Com tempo bom eu gostaria de fazer uma trilha. | S'il faisait beau, j'aimerais bien faire une randonnée.
ferir | blesser | O acidente feriu três pessoas. | L'accident a blessé trois personnes.
ferver | bouillir | A água ferve a cem graus. | L'eau bout à cent degrés.
ficar a saber | apprendre (une info) | Eu fico a saber das novidades tarde. | J'apprends les nouvelles tard.
ficar contente | se réjouir | Eu ficaria feliz com as férias. | Je me réjouirais des vacances.
filmar | tourner (un film) | Eles filmam a cena na praia. | Ils tournent la scène sur la plage.
fixar | fixer | Vamos fixar o preço depois da reunião. | Nous fixerons le prix après la réunion.
formar-se | obtenir son diplôme | Ele forma-se no ano que vem. | Il obtient son diplôme l'an prochain. | pron
formular | formuler | Ela formulou a frase com clareza. | Elle a formulé la phrase clairement.
fotografar | photographier | Ela gosta de fotografar casas antigas. | Elle aime photographier les vieilles maisons.
fritar | frire | Frito as batatas no óleo. | Je fais frire les pommes de terre à l'huile.
fugir | fuir | Eles fugiram do país em 1939. | Ils ont fui le pays en 1939.
funcionar | fonctionner | O elevador não funciona. | L'ascenseur ne fonctionne pas.
girar | tourner | Eu giro a chave. | Je tourne la clé.
gravar | enregistrer | Eles gravam o disco em Lisboa. | Ils enregistrent l'album à Lisboa.
gritar | crier | Não precisa de gritar. | Il n'est pas nécessaire de crier.
herdar | hériter | Ele herdou a casa da avó. | Il a hérité de la maison de sa grand-mère.
hospedar-se | loger, séjourner | Ficamos hospedados no centro. | Nous logeons dans le centre. | pron
imaginar | s'imaginer, se présenter | Eu imagino que isso seja difícil. | Je m'imagine que c'est difficile.
impressionar | impressionner | O concerto impressiona-me muito. | Le concert m'impressionne beaucoup.
imprimir | imprimer | Imprimo o relatório agora. | J'imprime le rapport maintenant.
inaugurar | ouvrir, inaugurer | Vamos inaugurar uma loja nova. | Nous ouvrons un nouveau magasin.
incentivar | encourager, promouvoir | A escola incentiva crianças criativas. | L'école encourage les enfants créatifs.
incluir | inclure | O preço inclui o pequeno-almoço. | Le prix inclut le petit-déjeuner.
incomodar | déranger | O barulho incomodou-me a noite toda. | Le bruit m'a dérangé toute la nuit.
influenciar | influencer | O tempo influencia o meu humor. | Le temps influence mon humeur.
informar | informer | O canal informa a cada hora. | La chaîne informe toutes les heures.
inscrever | inscrire (quelqu'un) | Inscrevo o meu filho no curso. | J'inscris mon enfant au cours.
inscrever-se | s'inscrire | Eu inscrevo-me no curso. | Je m'inscris au cours. | pron
instalar | installer | Ele instalou o programa. | Il a installé le programme.
interessar | intéresser | Esse assunto interessa-me muito. | Ce sujet m'intéresse beaucoup.
interessar-se | s'intéresser | Eu interesso-me por música. | Je m'intéresse à la musique. | pron
interpretar | interpréter | Ele interpreta uma peça de Falla. | Il interprète une pièce de Falla.
inventar | inventer | Ele inventa boas desculpas. | Il invente de bonnes excuses.
investir | investir | Ele investe as economias em um apartamento. | Il investit ses économies dans un appartement.
ir buscar | aller chercher | Vou rapidinho buscar o pão. | Je vais vite chercher le pain.
irritar | fâcher | O comentário dele irritou a equipa toda. | Son commentaire a fâché toute l'équipe.
irritar-se | s'énerver | Fico irritado com o engarrafamento. | Je m'énerve à cause des embouteillages. | pron
juntar | réunir | Juntamos as mesas para o jantar. | Nous avons réuni les tables pour le dîner.
lançar | lancer | Ele lançou a bola bem longe. | Il a lancé la balle très loin.
levantar | lever, soulever | Levante a caixa com cuidado. | Soulève la boîte avec précaution.
machucar-se | se blesser | Eu machuco-me muito no desporto. | Je me blesse souvent en faisant du sport. | pron
manchar | tacher | O café manchou a toalha de mesa. | Le café a taché la nappe.
mandar | envoyer | Vou mandar-te uma foto. | Je t'envoie une photo.
manter | maintenir, garder | Mantenho uma rotina simples. | Je maintiens une routine simple.
marcar | marquer | Ele marcou dois golos. | Il a marqué deux buts.
marcar um encontro | se donner rendez-vous | Eu marco um encontro com amigos. | Je me donne rendez-vous avec des amis.
matricular-se | s'inscrire | Eu matriculo-me em setembro. | Je m'inscris en septembre. | pron
medir | mesurer | Meço a parede antes de comprar. | Je mesure le mur avant d'acheter.
melhorar | s'améliorer | O paciente melhora a cada dia. | Le patient s'améliore chaque jour.
memorizar | mémoriser | Memorizo dez palavras por dia. | Je mémorise dix mots par jour.
mencionar | mentionner | Vou mencionar isso rapidamente. | Je mentionne ça brièvement.
mentir | mentir | Ele mente quando está nervoso. | Il ment quand il est nerveux.
misturar | mélanger | Misture a farinha e o açúcar. | Mélange la farine et le sucre.
morder | mordre | O cão não morde. | Le chien ne mord pas.
morrer | mourir | Ele morreu aos noventa anos. | Il est mort à quatre-vingt-dix ans.
mover | bouger, déplacer | Mova a cadeira, por favor. | Déplace la chaise, s'il te plaît.
mudar | changer | A cidade está a mudar rápido. | La ville change vite.
mudar-se | déménager | Vamos nos mudar no mês que vem. | Nous déménageons le mois prochain. | pron
nascer | naître | Nasci em Toronto. | Je suis né à Toronto.
navegar | naviguer | Navego na internet à noite. | Je navigue sur internet le soir.
observar | observer | Eu observo os pássaros. | J'observe les oiseaux.
ocupar | occuper | O sofá ocupa muito espaço. | Le canapé occupe beaucoup de place.
odiar | détester | Ele odeia acordar cedo. | Il déteste se lever tôt.
olhar para | regarder | Ele olha para mim de um jeito simpático. | Il me regarde d'un air aimable.
opinar | donner son avis | O meu pai opinava sobre tudo sem saber nada. | Mon père donnait son avis sur tout sans rien savoir.
parabenizar | féliciter | A minha tia sempre nos parabenizava por carta. | Ma tante nous félicitait toujours par lettre.
parafusar | visser | Parafuso a estante na parede. | Je visse l'étagère au mur.
parecer | sembler, paraître | Parece-me uma boa ideia. | Ça me semble une bonne idée.
parecer-se | ressembler | Sempre me pareci com a minha mãe. | J'ai toujours ressemblé à ma mère. | pron
passear | se promener | Passeamos pela floresta. | Nous nous promenons dans la forêt.
pendurar | accrocher, raccrocher | Penduro o quadro na parede. | J'accroche le tableau au mur.
pensar bem | réfléchir | Estou a pensar nas minhas opções. | Je réfléchis à mes options.
pentear | coiffer | Penteie a menina antes da escola. | Coiffe la petite avant l'école.
perceber | remarquer | Percebo a diferença na hora. | Je remarque la différence tout de suite.
perder-se | se perdre | Eu perdi-me no centro histórico. | Je me suis perdu dans la vieille ville. | pron
perguntar-se | se demander | Eu pergunto-me se isso é verdade. | Je me demande si c'est vrai. | pron
permanecer | rester | Ele permaneceu calado durante toda a reunião. | Il est resté silencieux toute la réunion.
permitir | permettre | Eu permiti isso a ele. | Je le lui ai permis.
pertencer | appartenir | Ele pertence a uma associação de bairro. | Il appartient à une association de quartier.
pesquisar | faire des recherches | Ele pesquisa sobre energias limpas. | Il fait des recherches sur les énergies propres.
piorar | empirer | A dor piora à noite. | La douleur empire la nuit.
planear | planifier | Planeamos a viagem com antecedência. | Nous planifions le voyage à l'avance.
plantar | planter | Plantamos uma árvore todo ano. | Nous plantons un arbre chaque année.
poluir | polluer | Os carros poluem muito. | Les voitures polluent beaucoup.
possibilitar | permettre | A bolsa possibilita os estudos dele. | La bourse lui permet de faire des études.
possuir | posséder | Eu tenho um carro velho. | Je possède une vieille voiture. | ex?
pousar | atterrir | O avião pousa no horário. | L'avion atterrit à l'heure.
preencher | remplir | Preencha os dados pessoais. | Remplissez les données personnelles.
preferir | préférer | Prefiro ficar em casa. | Je préfère rester à la maison.
pregar | clouer | Prego o quadro na parede. | Je cloue le tableau au mur.
preocupar | inquiéter | O silêncio dele preocupa-me. | Son silence m'inquiète.
preocupar-se | s'inquiéter | Não se preocupe comigo. | Ne t'inquiète pas pour moi. | pron
prestar atenção | faire attention, surveiller | Eu prestava atenção a cada palavra. | Je faisais attention à chaque mot.
proibir | interdire | É proibido fumar aqui. | Il est interdit de fumer ici.
proteger | protéger | Protegemos os animais da floresta. | Nous protégeons les animaux de la forêt.
publicar | publier | Publicam o artigo na segunda. | Ils publient l'article lundi.
pular | sauter | Ele pula muito alto. | Il saute très haut.
puxar | tirer, jeter | Puxe a corda. | Tire sur la corde.
quebrar | tomber en panne, s'abîmer | A máquina de lavar quebrou. | La machine à laver est tombée en panne.
quebrar-se | se casser | O copo quebrou. | Le verre s'est cassé. | pron
queimar | brûler | A torrada queimou. | La tartine a brûlé.
queixar-se | se plaindre | Registrei queixa do roubo na esquadra. | J'ai porté plainte pour le vol au commissariat. | pron
reagir | réagir | Reajo rápido à mensagem. | Je réagis vite au message.
receitar | prescrire | Ele receitou-me uns comprimidos. | Il m'a prescrit des comprimés.
reciclar | recycler | Reciclamos o papel e o vidro. | Nous recyclons le papier et le verre.
reclamar | se plaindre | Eu reclamo do atendimento. | Je me plains du service.
recolher | ramasser, cueillir | Eu recolheria a roupa antes que chova. | Moi, je rentrerais le linge avant qu'il pleuve.
reconhecer | reconnaître | Eu reconheceria esse rosto em qualquer lugar. | Moi, je reconnaîtrais ce visage n'importe où.
recuperar | récupérer | Ele recuperou a voz em três dias. | Il a récupéré la voix en trois jours.
reduzir | réduire | Estou a reduzir o meu consumo. | Je réduis ma consommation.
reformar | rénover, refaire | Nós mesmos reformamos a cozinha. | Nous avons rénové la cuisine nous-mêmes.
regar | arroser | Rego as plantas duas vezes por semana. | J'arrose les plantes deux fois par semaine.
relaxar | se détendre | Relaxo lendo na praia. | Je me détends en lisant sur la plage.
remar | ramer | Remamos até a outra margem. | Nous avons ramé jusqu'à l'autre rive.
remover | enlever | Ele removeu o software antigo. | Il a enlevé l'ancien logiciel.
resolver | résoudre | Resolvemos o problema em uma hora. | Nous résolvons le problème en une heure.
resumir | résumer | Resuma a história em três frases. | Résume l'histoire en trois phrases.
retirar | retirer | Retiraram o produto do mercado. | Ils ont retiré le produit du marché.
revisar | réviser | Reviso as anotações antes da prova. | Je révise mes notes avant l'examen.
roubar | voler | Roubaram a carteira dele no metro. | On lui a volé le portefeuille dans le métro.
salvar | enregistrer, garder | Salve o arquivo antes de sair. | Enregistre le fichier avant de sortir.
secar | sécher | O cabelo vai secar em cinco minutos. | Les cheveux sécheront en cinq minutes.
seguir | suivre, continuer | Siga reto até a praça. | Continue tout droit jusqu'à la place.
segurar | tenir, maintenir | Segure a escada um momento. | Tiens l'échelle un instant.
separar | séparer | Eu separo o lixo. | Je trie les déchets.
separar-se | se séparer | Eles separaram-se no ano passado. | Ils se sont séparés l'an dernier. | pron
significar | signifier, vouloir dire | O que significa esta palavra? | Que signifie ce mot ?
soar | sonner, retentir | O piano soa desafinado. | Le piano sonne faux.
sobreviver | survivre | Eles sobreviveram dois dias sem água. | Ils ont survécu deux jours sans eau.
sofrer de | souffrir de | Ele sofre de uma doença crónica. | Il souffre d'une maladie chronique.
solicitar | demander, solliciter | Solicito uma consulta com hora marcada. | Je demande un rendez-vous.
soltar | lâcher | Não solte a minha mão. | Ne lâche pas ma main.
sonhar | rêver | Sonho em voltar um dia. | Je rêve de revenir un jour.
sorrir | sourire | Ela sorri em todas as fotos. | Elle sourit sur toutes les photos.
substituir | remplacer | Eu substituo a luminária velha. | Je remplace la vieille lampe.
suportar | supporter | Não suporto o barulho das obras. | Je ne supporte pas le bruit des travaux.
surgir | naître, se former | O problema surgiu de um erro. | Le problème est né d'une erreur.
surpreender | surprendre | A resposta dele surpreende-me. | Sa réponse me surprend.
temer | craindre | Temo que seja tarde demais. | Je crains qu'il ne soit trop tard.
tentar | essayer | Tento ligar de novo. | J'essaie d'appeler encore une fois.
ter vontade de | avoir envie de | Está com vontade de um café? | Tu as envie d'un café ?
testar | tester | Eu gostaria de testar isso. | J'aimerais tester ça.
tocar | toucher, jouer (d'un instrument) | Não toque no quadro. | Ne touche pas le tableau.
tomar | prendre | Tomamos um café juntos. | Nous prenons un café ensemble.
tossir | tousser | Tusso muito à noite. | Je tousse beaucoup la nuit.
traduzir | traduire | Traduzo o texto para o inglês. | Je traduis le texte en anglais.
transferir | transférer | Transferiram o escritório para o centro. | Ils ont transféré le bureau au centre.
transmitir | diffuser | Transmitem o jogo ao vivo. | Ils diffusent le match en direct.
tratar | traiter | O livro trata da guerra. | Le livre traite de la guerre.
treinar | s'entraîner | Treino três vezes por semana. | Je m'entraîne trois fois par semaine.
trocar de roupa | se changer (de vêtements) | Depois do trabalho eu troco de roupa. | Je me change après le travail.
ultrapassar | dépasser | Não ultrapasse na curva. | Ne double pas dans le virage.
utilizar | utiliser | Utilizei o dicionário para traduzir a carta. | J'ai utilisé le dictionnaire pour traduire la lettre.
valer a pena | valoir la peine | Isso vale muito a pena. | Ça vaut vraiment la peine.
varrer | balayer | Varro a cozinha toda manhã. | Je balaie la cuisine chaque matin.
verificar | vérifier, examiner | Eu verifico a conta. | Je vérifie la facture.
zangar-se | se fâcher | Sem os comprimidos, as costas doer-me-iam muito. | Sans les comprimés, j'aurais très mal au dos. | pron
"""

# « masculin | feminin | traduction | phrase | sa traduction | drapeaux ».
ADJECTIFS = """
a tempo | a tempo | à temps | Chegamos a tempo. | Nous sommes arrivés à temps.
aconchegante | aconchegante | confortable, convivial | O café é muito aconchegante. | Le café est très confortable.
adulto | adulta | adulte | Ela já é uma pessoa adulta. | C'est déjà une personne adulte.
afinado | afinada | accordé, juste | O piano não está afinado. | Le piano n'est pas accordé.
agradável | agradável | agréable | A temperatura hoje está agradável. | La température est agréable aujourd'hui.
americano | americana | américain | É um carro americano. | C'est une voiture américaine.
amplo | ampla | vaste | A sala é ampla e luminosa. | Le salon est vaste et lumineux.
animado | animada | aventureux, qui aime sortir | Os meus amigos estão sempre animados para fazer programas. | Mes amis aiment beaucoup sortir et bouger.
antipático | antipática | antipathique | O chefe é um pouco antipático. | Le patron est un peu antipathique.
antiquado | antiquada | démodé | O estilo dele é meio antiquado. | Son style est un peu démodé.
apressado | apressada | pressé, urgent | Estou com pressa. | Je suis pressé. | ex?
artístico | artística | artistique | Ele tem um talento artístico enorme. | Il a un talent artistique énorme.
atencioso | atenciosa | attentionné | O empregado de mesa foi muito atencioso. | Le serveur a été très attentionné.
atraente | atraente | séduisant | É uma pessoa muito atraente. | C'est une personne très séduisante.
atrasado | atrasada | en retard | O voo está atrasado. | Le vol est en retard.
atrevido | atrevida | insolent, effronté | O aluno foi bem atrevido. | L'élève était plutôt insolent.
atual | atual | actuel | É um tema muito atual. | C'est un sujet très actuel.
austríaco | austríaca | autrichien | Conheço bem a cozinha austríaca. | Je connais bien la cuisine autrichienne.
autoconfiante | autoconfiante | sûr de soi | Ela mostra-se muito autoconfiante. | Elle se présente avec beaucoup d'assurance.
automático | automática | automatique | O pagamento é automático. | Le paiement est automatique.
belo | bela | beau | Ele escreveu um texto belo e simples. | Il a écrit un texte beau et simple.
bem organizado | bem organizado | clair, bien structuré |  |  | ex=?
bem-comportado | bem-comportada | sage, obéissant | Hoje a criança foi muito bem-comportada. | L'enfant a été très sage aujourd'hui.
bem-vindo | bem-vinda | bienvenu |  |  | ex=?
bravo | brava | fâché | Ela está brava comigo. | Elle est fâchée contre moi.
breve | breve | bref | Foi uma reunião breve. | Ce fut une réunion brève.
burro | burra | stupide | Foi uma ideia parva. | C'était une idée stupide. | ex?
cacheado | cacheada | bouclé, frisé | A minha filha tem o cabelo cacheado. | Ma fille a les cheveux bouclés.
calado | calada | silencieux | Ele ficou calado o jantar inteiro. | Il est resté silencieux tout le dîner.
calmo | calma | calme, tranquille | O lago é claro e calmo. | Le lac est clair et calme.
cansativo | cansativa | fatigant, exigeant | A trilha foi muito cansativa. | La randonnée était très fatigante.
capaz | capaz | capable | Ele é capaz de fazer isso sozinho. | Il est capable de le faire seul.
careca | careca | chauve | O meu tio é careca. | Mon oncle est chauve.
carinhoso | carinhosa | affectueux | Ela é muito carinhosa com a avó. | Elle est très affectueuse avec sa grand-mère.
castanho | castanha | châtain | Ele tem cabelo castanho. | Il a les cheveux châtains.
central | central | central | É um bairro muito central. | C'est un quartier très central.
certo | certa | correct | A tua resposta estava certa. | Ta réponse était correcte.
chinês | chinesa | chinois |  |  | ex=?
chique | chique | chic | É um restaurante chique. | C'est un restaurant chic.
ciumento | ciumenta | jaloux | Ele fica ciumento à toa. | Il devient jaloux pour rien.
clássico | clássica | classique | Ele ouve música clássica. | Il écoute de la musique classique.
complicado | complicada | compliqué | É um caso complicado. | C'est un cas compliqué.
comum | comum | habituel, ordinaire | É um dia completamente comum. | C'est une journée tout à fait ordinaire.
confortável | confortável | confortable | O assento é muito confortável. | Le siège est très confortable.
conhecido | conhecida | connu | Ela é uma cantora conhecida. | C'est une chanteuse connue.
contagiante | contagiante | entraînant | É uma melodia contagiante. | C'est une mélodie entraînante.
corajoso | corajosa | courageux | Ele foi muito corajoso naquele momento. | Il a été très courageux à ce moment-là.
cordial | cordial | cordial, chaleureux | Uma saudação cordial a todos. | Un salut cordial à tous.
cru | crua | cru | A carne ainda está crua. | La viande est encore crue.
cruel | cruel | cruel | Foi um comentário cruel. | Ce fut un commentaire cruel.
cuidadoso | cuidadosa | soigneux | Ele é muito cuidadoso com as ferramentas. | Il est très soigneux avec ses outils.
curioso | curiosa | curieux | As crianças são curiosas por natureza. | Les enfants sont curieux par nature.
de acordo | de acordo | d'accord | Estamos de acordo. | Nous sommes d'accord.
denso | densa | dense | A neblina estava muito densa. | Le brouillard était très dense.
desagradável | desagradável | désagréable | A conversa foi muito desagradável. | La conversation était très désagréable.
desarrumado | desarrumada | en désordre | O quarto dele está desarrumado. | Sa chambre est en désordre.
desempregado | desempregada | au chômage | Ele está desempregado há um mês. | Il est au chômage depuis un mois.
diferente | diferente | différent | Temos opiniões diferentes. | Nous avons des opinions différentes.
digital | digital | numérique | Tenho o bilhete digital. | J'ai le billet numérique.
direto | direta | direct | É um voo direto. | C'est un vol direct.
discreto | discreta | discret | Ele prefere uma homenagem discreta. | Il préfère un hommage discret.
disponível | disponível | disponible | Não há quartos disponíveis. | Il n'y a pas de chambres disponibles.
distante | distante | lointain, éloigné | É um primo distante. | C'est un cousin éloigné.
divorciado | divorciada | divorcé | Os meus pais são divorciados. | Mes parents sont divorcés.
duplo | dupla | double | Quero um quarto duplo. | Je veux une chambre double.
ecológico | ecológica | écologique | Compro produtos ecológicos. | J'achète des produits écologiques.
económico | económica | économique, bon marché | É um hotel muito económico. | C'est un hôtel très économique.
educado | educada | poli | É um menino muito educado. | C'est un garçon très poli.
eficaz | eficaz | efficace | É um método muito eficaz. | C'est une méthode très efficace.
egoísta | egoísta | égoïste | Não seja egoísta. | Ne sois pas égoïste.
elegante | elegante | élégant | Ele vai muito elegante ao casamento. | Il va très élégant au mariage.
em conta | em conta | avantageux, bon marché | A oferta está muito em conta. | L'offre est très avantageuse.
em dinheiro | em dinheiro | en espèces | Pago em dinheiro. | Je paie en espèces.
emocionado | emocionada | ému, enthousiaste | Ele estava muito emocionado. | Il était très ému.
emocionante | emocionante | émouvant, palpitant | Foi um final emocionante. | Ce fut une fin émouvante.
empolgante | empolgante | excitant | O primeiro dia de aula foi empolgante. | Le premier jour d'école était excitant.
envergonhado | envergonhada | gêné, honteux | Ele estava envergonhado com o erro. | Il avait honte de son erreur.
errado | errada | faux | Infelizmente a conta estava errada. | La facture était malheureusement fausse.
escasso | escassa | rare, insuffisant | A água é escassa no verão. | L'eau est rare en été.
escrito | escrita | écrit, par écrit | Por favor, dê-me uma resposta por escrito. | Donnez-moi une réponse écrite, s'il vous plaît.
esforçado | esforçada | travailleur, appliqué | A estudante é muito esforçada. | L'étudiante est très travailleuse.
esgotado | esgotada | épuisé | O concerto estava esgotado. | Le concert affichait complet.
especialista | especialista | expert | Ela é especialista em direito trabalhista. | Elle est experte en droit du travail.
esperto | esperta | éveillé, vif | É uma menina muito esperta. | C'est une petite fille très éveillée.
espesso | espessa | épais | O molho está grosso demais. | La sauce est trop épaisse. | ex?
esquisito | esquisita | bizarre, drôle | Está com um cheiro esquisito. | Ça sent bizarre.
estranho | estranha | bizarre, étrange | Ele comportou-se de um jeito estranho. | Il s'est comporté bizarrement.
estressante | estressante | stressant | Às vezes o trabalho é estressante. | Le travail est parfois stressant.
estudioso | estudiosa | studieux | A minha irmã é muito estudiosa. | Ma sœur est très studieuse.
estúpido | estúpida | stupide | Foi uma decisão estúpida. | Ce fut une décision stupide.
europeu | europeia | européen | É possível que financiem a obra com fundos europeus. | Il est possible qu'ils financent les travaux avec des fonds européens.
evidente | evidente | évident | É evidente que ele não quer vir. | Il est évident qu'il ne veut pas venir.
exaustivo | exaustiva | épuisant | Foi um jogo exaustivo. | Ce fut un match épuisant.
exigente | exigente | exigeant | É um professor muito exigente. | C'est un professeur très exigeant.
extenso | extensa | étendu | O relatório é extenso demais. | Le rapport est trop étendu.
falante | falante | bavard | O meu avô é muito falante. | Mon grand-père est très bavard.
familiar | familiar | familial | É uma empresa familiar. | C'est une entreprise familiale.
famoso | famosa | célèbre | É um quadro muito famoso. | C'est un tableau très célèbre.
farto | farta | las, excédé | Estou farto de esperar. | J'en ai assez d'attendre.
festivo | festiva | férié, festif | Segunda-feira é feriado. | Lundi est un jour férié. | ex?
fiel | fiel | fidèle | É um amigo fiel. | C'est un ami fidèle.
firme | firme | ferme | O colchão é firme demais. | Le matelas est trop ferme.
flexível | flexível | souple | Ele é muito flexível para a idade. | Il est très souple pour son âge.
fraco | fraca | faible | Sinto-me um pouco fraco. | Je me sens un peu faible.
fresco | fresca | frais | Compramos peixe fresco. | Nous achetons du poisson frais.
frágil | frágil | fragile | Cuidado, o pacote é frágil. | Attention, le colis est fragile.
furioso | furiosa | furieux | Ele ficou furioso ao saber. | Il est devenu furieux en l'apprenant.
generoso | generosa | généreux | Ele é muito generoso com os amigos. | Il est très généreux avec ses amis.
gigante | gigante | géant | Havia uma tela gigante na praça. | Il y avait un écran géant sur la place.
gorduroso | gordurosa | gras, gros | Este molho é gorduroso demais para mim. | Cette sauce est trop grasse pour moi.
gratuito | gratuita | gratuit | O serviço é gratuito. | Le service est gratuit.
grave | grave | grave | Não é nada grave. | Ce n'est rien de grave.
grego | grega | grec | Ela estuda a história grega. | Elle étudie l'histoire grecque.
grávida | grávida | enceinte | A minha irmã está grávida. | Ma sœur est enceinte.
honesto | honesta | honnête | É uma pessoa honesta. | C'est une personne honnête.
horrível | horrível | affreux, terrible | O tempo estava horrível. | Le temps était affreux.
hospitaleiro | hospitaleira | hospitalier | A família foi muito hospitaleira. | La famille était très hospitalière.
humilde | humilde | humble | Ele vem de uma família humilde. | Il vient d'une famille humble.
hábil | hábil | habile | Ele é muito habilidoso com as mãos. | Il est très habile de ses mains. | ex?
idoso | idosa | âgé | Ele cuida do pai idoso. | Il s'occupe de son père âgé.
imenso | imensa | immense | Daqui o mar parece imenso. | D'ici la mer paraît immense.
impopular | impopular | impopulaire | A decisão foi muito impopular. | La décision était très impopulaire.
impossível | impossível | impossible | Isso é simplesmente impossível. | C'est tout simplement impossible.
impreciso | imprecisa | imprécis | As informações dele eram imprecisas. | Ses informations étaient imprécises.
imprudente | imprudente | imprudent | Isso foi bem imprudente da tua parte. | C'était plutôt imprudent de ta part.
incluído | incluída | inclus | O pequeno-almoço está incluído. | Le petit-déjeuner est inclus.
incomum | incomum | inhabituel | Hoje está quente fora do normal. | Le temps est inhabituellement chaud aujourd'hui. | ex?
infantil | infantil | enfantin | É literatura infantil. | C'est de la littérature enfantine.
informativo | informativa | informatif | É um programa informativo. | C'est une émission informative.
inseguro | insegura | peu sûr | A ponte está insegura desde a enchente. | Le pont est peu sûr depuis la crue.
inteligente | inteligente | intelligent | Ele deu uma resposta inteligente. | Il a donné une réponse intelligente.
interessado | interessada | intéressé | Ele está interessado no curso. | Il est intéressé par le cours.
interessante | interessante | intéressant | O livro é realmente interessante. | Le livre est vraiment intéressant.
inútil | inútil | inutile | Esse aparelho é inútil. | Cet appareil est inutile.
justo | justa | ajusté, serré | A calça é muito justa. | Le pantalon est très ajusté.
juvenil | juvenil | juvénile | Ele joga na liga juvenil. | Il joue dans la ligue juvénile.
leal | leal | loyal | Ele foi leal à empresa por vinte anos. | Il a été loyal envers l'entreprise vingt ans.
lindo | linda | beau | É um vilarejo lindo. | C'est un beau village.
loiro | loira | blond | A filha dele é loira. | Sa fille est blonde.
louco | louca | fou | É uma ideia maluca, mas pode funcionar. | C'est une idée folle, mais ça peut marcher. | ex?
luminoso | luminosa | lumineux | A sala é muito luminosa. | Le salon est très lumineux.
luxemburguês | luxemburguesa | luxembourgeois | Ela tem passaporte luxemburguês. | Elle a un passeport luxembourgeois.
maciço | maciça | massif | Houve uma resposta maciça ao apelo. | Il y a eu une réponse massive à l'appel.
mal-educado | mal-educada | peu aimable | O empregado de mesa foi bem mal-educado. | Le serveur était plutôt peu aimable.
maldoso | maldosa | méchant, mesquin | Foi um comentário maldoso. | C'était une remarque méchante.
maravilhoso | maravilhosa | merveilleux | A comida estava maravilhosa. | Le repas était merveilleux.
marinho | marinha | marin | Ele estuda a fauna marinha. | Il étudie la faune marine.
masculino | masculina | masculin, mâle | A palavra é masculina: der Tisch. | Le mot est masculin : der Tisch.
material | material | matériel | Os danos materiais foram menores. | Les dégâts matériels ont été mineurs.
mobiliado | mobiliada | meublé | Procuramos um apartamento mobiliado. | Nous cherchons un appartement meublé.
moderno | moderna | moderne | Ele mora em um apartamento moderno. | Il habite un appartement moderne.
mole | mole | mou | O colchão é mole demais. | Le matelas est trop mou.
monótono | monótona | monotone | O trabalho na linha de montagem é monótono. | Le travail à la chaîne est monotone.
moreno | morena | brun | Ele é moreno e alto. | Il est brun et grand.
morto | morta | mort | Infelizmente a planta morreu. | La plante est malheureusement morte. | ex?
mudo | muda | muet | Ele ficou mudo de surpresa. | Il est resté muet de surprise.
máximo | máxima | maximum | A velocidade máxima é cem. | La vitesse maximale est de cent.
médio | média | moyen | Um tamanho médio serve-me. | Une taille moyenne me va.
mínimo | mínima | minimum | O esforço mínimo não basta. | L'effort minimum ne suffit pas.
na moda | na moda | à la mode | Esse corte está na moda de novo. | Cette coupe est de nouveau à la mode.
nascido | nascida | né | Eu nasci em Lyon. | Je suis né à Lyon. | ex?
natural | natural | naturel | É um produto natural. | C'est un produit naturel.
nervoso | nervosa | nerveux | Fico nervoso antes da prova. | Je suis nerveux avant l'examen.
noivo | noiva | fiancé | A minha irmã está noiva. | Ma sœur est fiancée.
normal | normal | normal | O comportamento é completamente normal. | Ce comportement est tout à fait normal.
numeroso | numerosa | nombreux | É uma família numerosa. | C'est une famille nombreuse.
objetivo | objetiva | objectif | Ele tenta ser objetivo. | Il essaie d'être objectif.
on-line | on-line | en ligne | Comprei a passagem on-line. | J'ai acheté le billet en ligne.
organizado | organizada | rangé, ordonné | É uma pessoa muito organizada. | C'est une personne très ordonnée.
orgulhoso | orgulhosa | fier |  |  | ex=?
paciente | paciente | patient | É preciso de ser paciente com as crianças. | Il faut être patient avec les enfants.
perigoso | perigosa | dangereux | Essa rua é perigosa à noite. | Cette rue est dangereuse la nuit.
pobre | pobre | pauvre | Naquela época a família era muito pobre. | La famille était très pauvre à l'époque.
pontual | pontual | ponctuel | Ele é sempre pontual. | Il est toujours ponctuel.
pouco claro | pouco claro | pas clair | A situação ainda não está clara. | La situation n'est pas encore claire. | ex?
pouco nítido | pouco nítido | peu clair | A letra dele é bem difícil de ler. | Son écriture est plutôt peu claire. | ex?
preciso | precisa | nécessaire | Não precisa. | Ce n'est pas nécessaire.
preguiçoso | preguiçosa | paresseux | Aos domingos sou preguiçoso. | Le dimanche je suis paresseux.
previsível | previsível | prévisible | O final é previsível demais. | La fin est trop prévisible.
privado | privada | privé | É uma reunião privada. | C'est une réunion privée.
profundo | profunda | profond | O lago é muito profundo. | Le lac est très profond.
proibido | proibida | interdit | É proibido entrar. | Il est interdit d'entrer.
provável | provável | probable | É provável que chova. | Il est probable qu'il pleuve.
prático | prática | pratique | Esta ferramenta é muito prática. | Cet outil est très pratique.
que trabalha | que trabalha | actif professionnellement | Os dois pais trabalham fora. | Les deux parents travaillent. | ex?
querido | querida | populaire, apprécié | Esta professora é muito querida. | Cette enseignante est très appréciée.
refrescante | refrescante | rafraîchissant | O banho foi muito refrescante. | Le bain a été très rafraîchissant.
relaxante | relaxante | relaxant | É uma música relaxante. | C'est une musique relaxante.
religioso | religiosa | religieux | É uma festa religiosa. | C'est une fête religieuse.
renovável | renovável | renouvelable | Usamos energia renovável. | Nous utilisons de l'énergie renouvelable.
rentável | rentável | rentable | O negócio não é rentável. | L'affaire n'est pas rentable.
repousante | repousante | reposant | As férias foram muito relaxantes. | Les vacances étaient très reposantes. | ex?
reservado | reservada | réservé | Esta mesa está reservada. | Cette table est réservée.
resistente | resistente | résistant | É um material muito resistente. | C'est un matériau très résistant.
rigoroso | rigorosa | strict, sévère | O nosso professor é muito rigoroso. | Notre professeur est très strict.
romântico | romântica | romantique | Foi uma noite romântica. | C'était une soirée romantique.
ruivo | ruiva | roux | A namorada dele é ruiva. | Sa copine est rousse.
russo | russa | russe | Ele lê literatura russa. | Il lit de la littérature russe.
rígido | rígida | rigide, raide | A escola aplicava regras muito rígidas. | L'école appliquait des règles très strictes.
satisfeito | satisfeita | rassasié | Obrigado, estou satisfeito. | Merci, je n'ai plus faim.
seguro | segura | sûr | Esta rua é segura para bicicletas. | Cette rue est sûre pour les vélos.
selvagem | selvagem | sauvage | É um animal selvagem. | C'est un animal sauvage.
sem fio | sem fio | sans fil | Uso auscultadores sem fio. | J'utilise des écouteurs sans fil.
sem importância | sem importância | peu important | São gestos cotidianos, sem importância. | Ce sont des gestes quotidiens, sans importance.
silencioso | silenciosa | silencieux, calme | O motor é muito silencioso. | Le moteur est très silencieux.
simples | simples | simple | O vestido dela é simples e bonito. | Sa robe est simple et jolie.
sincero | sincera | sincère | Seja sincero comigo. | Sois sincère avec moi.
sociável | sociável | sociable | O meu avô é uma pessoa sociável. | Mon grand-père est une personne sociable.
solitário | solitária | seul, solitaire | Depois da mudança ela sentia-se sozinha. | Après le déménagement, elle se sentait seule. | ex?
suficiente | suficiente | suffisant | Não há tempo suficiente. | Il n'y a pas assez de temps.
sujo | suja | sale | O rio está muito sujo. | La rivière est très sale.
suíço | suíça | suisse | É uma palavra suíça. | C'est un mot suisse.
tanto faz | tanto faz | égal, indifférent | Para mim, a hora tanto faz. | L'heure m'est égale.
teimoso | teimosa | têtu | Ele é teimoso como o pai. | Il est têtu comme son père.
terrível | terrível | affreux, terrible | A comida estava terrível. | Le repas était affreux.
teórico | teórica | théorique | A prova teórica é na segunda. | L'examen théorique est lundi.
trabalhador | trabalhadora | travailleur | Ele é muito trabalhador. | Il est très travailleur.
turístico | turística | touristique | O bairro é muito turístico. | Le quartier est très touristique.
tímido | tímida | timide | Ele é tímido com desconhecidos. | Il est timide avec les inconnus.
típico | típica | typique | É um prato típico da região. | C'est un plat typique de la région.
ultrapassado | ultrapassada | dépassé, désuet | Esta técnica está ultrapassada. | Cette technologie est dépassée.
urgente | urgente | urgent | É uma entrega urgente. | C'est un envoi urgent.
valente | valente | courageux | O menino foi muito valente no médico. | Le garçon a été très courageux chez le médecin.
variado | variada | varié | O dia a dia aqui é variado. | Le quotidien ici est varié.
útil | útil | utile | É uma ferramenta muito útil. | C'est un outil très utile.
"""

# « adverbe | traduction | categorie | phrase | sa traduction ».
ADVERBES = """
adiante | en avant | Lieu | Siga em frente e verá a igreja. | Continue tout droit et tu verras l'église. | ex?
agora mesmo | tout de suite | Temps | Agora mesmo não posso falar. | Là tout de suite je ne peux pas parler.
agorinha | à l'instant, tout juste | Temps | Acabei de falar com ela por telefone. | Je viens juste de lui parler au téléphone. | ex?
além disso | en outre, de plus | Liaison | O apartamento é barato, além disso é central. | L'appartement est bon marché, de plus il est central.
anteontem | avant-hier | Temps | Anteontem chegou a encomenda. | Avant-hier le colis est arrivé.
antigamente | autrefois | Temps | Antigamente havia um mercado aqui. | Autrefois il y avait un marché ici.
anualmente | annuellement | Temps | O relatório é publicado anualmente. | Le rapport paraît annuellement.
ao lado | à côté | Lieu | A minha colega trabalha na sala ao lado. | Ma collègue travaille à côté.
ao redor | autour | Lieu | Havia muita gente ao redor. | Il y avait beaucoup de monde autour.
aos domingos | le dimanche | Fréquence | Aos domingos as lojas ficam fechadas. | Le dimanche, les magasins sont fermés.
aos sábados | le samedi | Fréquence | Aos sábados a feira é maior. | Le samedi, le marché est le plus grand.
aproximadamente | environ | Quantité | Leva aproximadamente uma hora. | Ça prend environ une heure.
assim | de cette manière, par là | Cause et conséquence | Ele praticou muito e assim passou na prova. | Il s'est beaucoup entraîné et a de cette manière réussi l'examen.
atrás | derrière | Lieu | O carro está atrás do prédio. | La voiture est derrière l'immeuble.
atualmente | actuellement | Temps | Atualmente moro em Coimbra. | Actuellement je vis à Coimbra.
até | même, voire | Nuance | Estava frio, até nevou. | Il faisait froid, il a même neigé.
certamente | certainement | Liaison | Certamente foi um mal-entendido. | C'était certainement un malentendu.
cinco vezes | cinq fois | Fréquence | Toquei a campainha cinco vezes. | J'ai sonné cinq fois.
claramente | clairement, distinctement | Manière | Ela explicou claramente. | Il l'a expliqué clairement.
claro | bien sûr | Liaison | Claro que eu ajudo-te. | Bien sûr que je t'aide.
com calma | calmement | Manière | Fale com calma, não há pressa. | Parle tranquillement, rien ne presse.
com cuidado | prudemment | Manière | Dirija com cuidado, por favor! | Conduis prudemment, s'il te plaît !
com que frequência | combien de fois | Question |  |  | ex=?
com segurança | sûrement, en sécurité | Manière | A criança está sentada com segurança na cadeirinha. | L'enfant est assis en sécurité dans son siège.
constantemente | constamment | Fréquence | O telefone toca constantemente. | Le téléphone sonne constamment.
corretamente | correctement | Manière | Preencha o formulário corretamente. | Remplis le formulaire correctement.
cá | ici | Lieu | Venha cá um momento. | Viens ici un instant.
de onde | d'où | Question | Não faço ideia de onde ele está. | Je n'ai aucune idée d'où il est.
de outro jeito | autrement, différemment | Manière | Eu faria o trabalho de outro jeito. | Je ferais le travail autrement.
de repente | soudain | Manière | De repente a luz apagou. | Soudain, la lumière s'est éteinte.
de volta | en arrière, de retour | Lieu |  |  | ex=?
depois de amanhã | après-demain | Temps | Depois de amanhã começa o curso. | Après-demain, le cours commence.
diariamente | quotidiennement | Temps | O serviço funciona diariamente. | Le service fonctionne quotidiennement.
do outro lado | de l'autre côté | Lieu | A padaria fica do outro lado da rua. | La boulangerie est de l'autre côté de la rue.
duas vezes | deux fois | Fréquence | Toquei a campainha duas vezes. | J'ai sonné deux fois.
educadamente | poliment | Manière | Ele pediu ajuda educadamente. | Il a poliment demandé de l'aide.
em algum lugar | quelque part | Lieu | O meu documento deve estar em algum lugar aqui. | Ma carte d'identité doit être quelque part ici.
em breve | prochainement | Temps | Em breve nos cinemas. | Prochainement au cinéma.
em compensação | en revanche, pour cela | Liaison | O hotel é caro, em compensação é muito sossegado. | L'hôtel est cher, mais en revanche très calme.
em conjunto | ensemble, en commun | Manière | Planeamos o projeto em conjunto. | Nous avons planifié le projet ensemble.
em frente | en face | Lieu | A farmácia fica em frente. | La pharmacie est en face.
embora | parti, absent | Lieu | Ela foi embora sem dizer uma palavra. | Elle est partie sans un mot.
enquanto | pendant que | Temps | Leio enquanto espero o comboio. | Je lis pendant que j'attends le train.
enquanto isso | entre-temps | Temps | Enquanto isso, prepare os documentos. | Entre-temps, prépare les documents.
errado | de travers, incorrectement | Manière | Escrevi o endereço errado. | J'ai écrit l'adresse de travers.
especialmente | particulièrement | Quantité | Hoje está especialmente frio. | Aujourd'hui, il fait particulièrement froid.
eventualmente | éventuellement | Temps | Eventualmente pode haver atrasos. | Il peut éventuellement y avoir des retards.
exatamente | exactement, précisément | Manière | É exatamente isso que eu disse. | C'est exactement ce que j'ai dit.
finalmente | finalement | Temps | Finalmente ele aceitou o cargo. | Finalement il a accepté le poste.
frequentemente | fréquemment | Fréquence | Ela viaja frequentemente a trabalho. | Il voyage fréquemment pour le travail.
gentilmente | aimablement | Manière | Ele recebeu-nos gentilmente. | Il nous a reçus aimablement.
geralmente | généralement | Fréquence | Geralmente faz bom tempo em maio. | Généralement il fait beau en mai.
habitualmente | habituellement | Fréquence | Habitualmente compro no mercado. | Habituellement j'achète au marché.
imediatamente | immédiatement | Temps | Chame um médico imediatamente. | Appelez immédiatement un médecin.
infelizmente | malheureusement | Liaison | Infelizmente o curso já está lotado. | Malheureusement, le cours est déjà complet.
jamais | jamais | Fréquence | Jamais disse isso. | Je n'ai jamais dit ça.
longe | loin | Lieu | O aeroporto fica muito longe. | L'aéroport est très loin.
lá | là-bas | Lieu | Vemo-nos lá, na praça. | On se voit là-bas, sur la place.
mais | plus, davantage | Quantité | Hoje o tempo está mais para fresco. | Le temps est plutôt frais aujourd'hui.
mais ou menos | à peu près | Quantité | O livro custa mais ou menos vinte euros. | Le livre coûte à peu près vingt euros.
mensalmente | mensuellement | Temps | A mensalidade é paga mensalmente. | La cotisation se paie mensuellement.
mesmo assim | malgré tout | Cause et conséquence | Estava a chover, mesmo assim fomos passear. | Il pleuvait, malgré tout nous sommes allés nous promener.
na frente | devant | Lieu | As crianças sentam na frente no Autocarro. | Les enfants sont assis à l'avant du bus.
na verdade | en fait, à vrai dire | Nuance | Na verdade eu queria ter chegado mais cedo. | En fait, je voulais venir plus tôt.
nada | rien | Quantité | O peixinho dourado nada no seu aquário. | Le poisson rouge nage dans son bocal.
naquela época | à l'époque | Temps | Naquela época não havia telemóveis. | Alors il n'y avait pas de portables.
ninguém | personne, nul | Quantité | Não tinha ninguém em casa. | Personne n'était à la maison.
no máximo | tout au plus | Quantité | Ficamos no máximo uma hora. | Nous restons une heure tout au plus.
no mínimo | au moins | Quantité | O curso dura no mínimo três meses. | Le cours dure au moins trois mois.
normalmente | normalement | Fréquence | Normalmente janto às nove. | Normalement je dîne à neuf heures.
ocasionalmente | occasionnellement | Fréquence | Ocasionalmente trabalhamos aos sábados. | Occasionnellement nous travaillons le samedi.
onde quer que | n'importe où | Lieu |  |  | ex=?
ontem à noite | hier soir | Temps | Ontem à noite jantamos na casa dos meus pais. | Hier soir nous avons dîné chez mes parents.
outro dia | l'autre jour | Temps | Outro dia eu encontrei o teu irmão. | L'autre jour, j'ai rencontré ton frère.
para baixo | vers le bas | Lieu | Eu arredondaria para baixo. | Moi, j'arrondirais vers le bas.
para cima | vers le haut | Lieu | A escada leva para cima. | L'escalier mène en haut.
para cá | par ici (vers moi) | Lieu | Vem para cá, por favor! | Viens ici, s'il te plaît !
para onde | où (direction) | Question |  |  | ex=?
pelo menos | au moins | Nuance | Pelo menos liga-me! | Appelle-moi au moins !
periodicamente | périodiquement | Fréquence | Os dados são revistos periodicamente. | Les données sont révisées périodiquement.
perto | près | Lieu | O museu fica perto daqui. | Le musée est près d'ici.
por | par | Quantité | O curso custa vinte euros por hora. | Le cours coûte vingt euros de l'heure.
por esse motivo | pour cette raison | Cause et conséquence | Por esse motivo a reunião foi adiada. | Pour cette raison, la séance a été reportée.
por muito tempo | longtemps | Temps | Esperei-te por muito tempo. | Je t'ai attendu longtemps.
posteriormente | par la suite | Temps | Posteriormente, provou-se que era falso. | Par la suite on a démontré que c'était faux.
previamente | au préalable | Temps | É preciso de reservar previamente. | Il faut réserver au préalable.
quanto tempo | combien de temps | Question |  |  | ex=?
quatro vezes | quatre fois | Fréquence | Liguei quatro vezes. | J'ai appelé quatre fois.
recentemente | récemment | Temps | A lei mudou recentemente. | La loi a changé récemment.
regularmente | régulièrement | Fréquence | Ela vai à academia regularmente. | Elle va régulièrement à la salle de sport.
semanalmente | chaque semaine | Temps | A equipa reúne-se semanalmente. | L'équipe se réunit chaque semaine.
senão | sinon | Cause et conséquence | Senão o telhado desabaria. | Le toit s'effondrerait sinon.
simultaneamente | simultanément | Temps | Os dois factos ocorreram simultaneamente. | Les deux événements se sont produits simultanément.
sinceramente | honnêtement | Manière | Sinceramente, não me convence. | Sincèrement, ça ne me convainc pas.
terminado | fini, passé | Temps | Está praticamente terminado. | C'est pratiquement terminé.
tomara que | espérons que | Liaison | Tomara que o tempo melhore. | Espérons que le temps s'améliore.
totalmente | totalement | Quantité | Depois do trabalho estou totalmente cansado. | Après le travail, je suis totalement épuisé.
três vezes | trois fois | Fréquence | Vou nadar três vezes por semana. | Je vais nager trois fois par semaine.
ultimamente | dernièrement | Temps | Ultimamente durmo pouco. | Dernièrement je dors peu.
uma vez | une fois | Fréquence | Vou nadar uma vez por semana. | Je vais nager une fois par semaine.
à noite | le soir | Temps | À noite eu geralmente leio um livro. | Le soir, je lis généralement un livre.
à parte | à part | Lieu | Guarde esse documento à parte. | Range ce document à part.
às quartas | le mercredi | Fréquence | Às quartas o consultório fica fechado. | Le mercredi, le cabinet est fermé.
às quintas | le jeudi | Fréquence | Às quintas eu vou nadar. | Le jeudi, je vais nager.
às segundas | le lundi (habituellement) | Temps | Às segundas eu sempre tenho desporto. | Le lundi, j'ai toujours du sport.
às sextas | le vendredi | Fréquence | Às sextas eu só trabalho até as duas. | Le vendredi, je ne travaille que jusqu'à deux heures.
às terças | le mardi | Fréquence | Às terças eu tenho curso de alemão. | Le mardi, j'ai un cours d'allemand.
"""

# « expression | traduction | categorie | phrase | sa traduction ».
EXPRESSIONS = """
acabar de | venir de | Au quotidien | Acabei de chegar em casa. | Je viens d'arriver à la maison.
ao lado de | à côté de | Au quotidien | O museu fica ao lado da igreja. | Le musée est à côté de l'église.
ao vivo | en direct | Au quotidien | O concerto é transmitido ao vivo. | Le concert est diffusé en direct.
apanhar o comboio | prendre le train | Au quotidien | Vamos apanhar o comboio para Porto. | Nous prenons le train pour Porto.
arrumar a cama | faire le lit | Tournures | Arrumo a cama antes de sair. | Je fais le lit avant de sortir.
Boa sorte | Bonne chance (réussite) | Bavarder | Boa sorte na prova! | Bonne chance pour l'examen !
boa viagem | bon voyage | Bavarder | Boa viagem e dá notícias! | Bon voyage et donne des nouvelles !
boas festas | bonnes fêtes | Politesse | Boas festas a todos. | Bonnes fêtes à tous.
Bom descanso | Bonne fin de journée (après le travail) | Bavarder | Estou indo – bom descanso! | J'y vais – bonne soirée !
com atraso | en retard | Au quotidien | O comboio chegou com atraso. | Le train est arrivé en retard.
com muito prazer | avec plaisir | Politesse | Acompanho o senhor com muito prazer. | Je vous accompagne avec plaisir.
combinar de se encontrar | prendre rendez-vous (avec un ami) | Au quotidien | Combinamos de nos encontrar na sexta. | Nous avons convenu de nous voir vendredi.
cometer um erro | faire une erreur | Tournures | Todo mundo comete um erro de vez em quando. | Tout le monde fait une erreur de temps en temps.
como foi o seu dia | comment s'est passée ta journée ? | Bavarder | Senta aí, como foi o teu dia? | Assieds-toi, comment s'est passée ta journée ?
Como o senhor está | Comment allez-vous ? | Bavarder | Bom dia, senhora Meier, como a senhora está? | Bonjour Madame Meier, comment allez-vous ?
cuidar de | s'occuper de | Au quotidien | A minha vizinha cuida do gato. | Ma voisine s'occupe du chat.
dar uma volta | faire un tour | Au quotidien | Vamos dar uma volta pelo centro. | Allons faire un tour dans le centre.
de férias | en vacances | Au quotidien | Estamos de férias por duas semanas. | Nous sommes en vacances deux semaines.
De jeito nenhum | En aucun cas | Donner son avis | De jeito nenhum eu viajo com este tempo. | En aucun cas je ne roule par ce temps.
de repente | tout d'un coup | Discuter | De repente ficou tudo em silêncio. | Tout d'un coup, le silence s'est fait.
deixar recado | laisser un message | Au quotidien | Por favor, deixe um recado. | Veuillez laisser un message.
desmarcar um compromisso | annuler un rendez-vous | Au quotidien | Infelizmente preciso de desmarcar o compromisso. | Je dois malheureusement annuler le rendez-vous.
E assim por diante | Et ainsi de suite | Discuter | Precisamos de pão, leite e assim por diante. | Il nous faut du pain, du lait et ainsi de suite.
e mesmo assim | et pourtant | Discuter | Estava frio e mesmo assim fomos nadar. | Il faisait froid et pourtant nous sommes allés nager.
entrar em acordo | se mettre d'accord | Au quotidien | Entramos em acordo sobre o preço. | Nous nous sommes mis d'accord sur le prix.
estar com dor de cabeça | avoir mal à la tête | Réagir | Estou com dor de cabeça desde hoje de manhã. | J'ai mal à la tête depuis ce matin.
estou bem | je vais bien | Réagir | Obrigado por perguntar, estou bem. | Merci de demander, je vais bien.
estou com calor | j'ai chaud | Réagir | Estou com calor, vou tirar a jaqueta. | J'ai chaud, j'enlève ma veste.
estou com frio | j'ai froid | Réagir | Fecha a janela, por favor, estou com frio. | Ferme la fenêtre s'il te plaît, j'ai froid.
estressar-se com | s'emporter à propos de | Réagir | Não se estressa com o atraso. | Ne t'emporte pas à propos du retard.
eu agradeço | je t'en remercie | Politesse | Eu agradeço de verdade. | Je t'en remercie vraiment.
eu vejo isso de outro jeito | je ne vois pas les choses ainsi | Donner son avis | Eu vejo isso de outro jeito, deixa eu explicar. | Je ne vois pas les choses ainsi, laisse-moi expliquer.
faxinar o apartamento | faire le ménage | Au quotidien | Aos sábados eu faço faxina no apartamento. | Le samedi, je fais le ménage.
fazer fila | faire la queue | Tournures | Tivemos de fazer fila por uma hora. | Nous avons dû faire la queue une heure.
fazer uma pergunta | poser une question | Tournures | Posso fazer uma pergunta? | Puis-je poser une question ?
fazer uma sugestão | faire une proposition | Tournures | Posso fazer uma sugestão? | Puis-je faire une proposition ?
feliz aniversário | joyeux anniversaire | Politesse | Feliz aniversário, vovó! | Joyeux anniversaire, mamie !
foi engano | vous vous êtes trompé de numéro | Au quotidien | Desculpe, foi engano. | Désolé, vous vous êtes trompé de numéro.
interessar-se por | s'intéresser à | Tournures | Eu interesso-me por música. | Je m'intéresse à la musique.
ir ao médico | aller chez le médecin | Au quotidien | Se piorar, vá ao médico. | Si ça empire, va chez le médecin.
irritar-se com | s'énerver contre | Réagir | Fico irritado com o barulho. | Je m'énerve contre le bruit.
lavar a roupa | faire la lessive | Au quotidien | Quem lava a roupa esta semana? | Qui fait la lessive cette semaine ?
mais uma vez | encore une fois | Au quotidien | O senhor pode explicar isso mais uma vez? | Pouvez-vous expliquer cela encore une fois ?
marcar uma consulta | prendre rendez-vous | Tournures | Eu queria marcar uma consulta no médico. | Je voudrais prendre rendez-vous chez le médecin.
nem pensar | pas question | Réagir | Emprestar o carro para ele? Nem pensar. | Lui prêter la voiture ? Pas question.
No momento | En ce moment | Au quotidien | No momento estou a procurar um apartamento novo. | En ce moment, je cherche un nouvel appartement.
não há de quê | il n'y a pas de quoi | Politesse | — Obrigado. — Não há de quê. | — Merci. — Il n'y a pas de quoi.
não tenho certeza | je ne suis pas sûr | Donner son avis | Não tenho certeza se isso está certo. | Je ne suis pas sûr que ce soit vrai.
O mais rápido possível | Le plus vite possible | Au quotidien | Por favor, responda o mais rápido possível. | Répondez le plus vite possible, s'il vous plaît.
Onde fica | Où se trouve… ? (surtout en Amérique latine) | Au quotidien | Com licença, onde fica o museu? | Excusez-moi, où se trouve le musée ?
Para mim tanto faz | Ça m'est égal | Donner son avis | Pizza ou macarrão? – Para mim tanto faz. | Pizza ou pâtes ? – Ça m'est égal.
para terminar | pour finir | Discuter | Para terminar, eu gostaria de agradecer. | Pour finir, je voudrais remercier.
passar numa prova | réussir un examen | Tournures | Ela passou na prova com nota máxima. | Elle a réussi l'examen avec la meilleure note.
pedir emprestado | emprunter | Au quotidien | Pedi o carro emprestado a ele. | Je lui ai emprunté la voiture.
perder o Autocarro | rater le bus | Au quotidien | Perdi o Autocarro e tive de ir a pé. | J'ai raté le bus et j'ai dû marcher.
Por exemplo | Par exemple | Discuter | Leva alguma coisa quente, por exemplo um cachecol. | Prends quelque chose de chaud, par exemple une écharpe.
por sorte | heureusement | Réagir | Por sorte não aconteceu nada. | Heureusement il ne s'est rien passé.
por um lado | d'un côté | Discuter | Por um lado é caro, por outro é muito prático. | D'un côté c'est cher, de l'autre très pratique.
praticar desporto | faire du sport | Tournures | Pratico desporto de manhã. | Je fais du sport le matin.
quanto tempo | ça fait longtemps | Bavarder | Olá, Tom, quanto tempo! | Salut Tom, ça fait longtemps !
Que azar | Quelle malchance | Réagir | O comboio já foi – que azar! | Le train est parti – quelle malchance !
que importa | qu'importe | Réagir | Vamos chegar atrasados, mas que importa. | Nous arriverons tard, mais qu'importe.
quem sabe | qui sait | Réagir | Quem sabe se ele voltará. | Qui sait s'il reviendra.
Quer deixar um recado | Voulez-vous laisser un message ? | Au quotidien | Ele não está no momento. Quer deixar um recado? | Il n'est pas là pour le moment. Voulez-vous laisser un message ?
sacar dinheiro | retirer de l'argent | Au quotidien | Ainda preciso de sacar dinheiro. | Je dois encore retirer de l'argent.
sem dúvida | sans aucun doute | Donner son avis | Sem dúvida é a melhor solução. | C'est sans aucun doute la meilleure solution.
sem falta | sans faute | Au quotidien | Devolvo amanhã sem falta. | Je te le rends demain sans faute.
ser pontual | être ponctuel | Au quotidien | Na Alemanha é importante ser pontual. | En Allemagne, il est important d'être ponctuel.
seria possível | serait-il possible… ? | Politesse | Seria possível mudar a consulta? | Serait-il possible de déplacer le rendez-vous ?
Sou da opinião | Je suis d'avis | Donner son avis | Sou da opinião de que deveríamos esperar. | Je suis d'avis que nous devrions attendre.
Também acho | Je suis du même avis | Donner son avis | O filme foi chato. – Também acho. | Le film était ennuyeux. – Je suis du même avis.
tenho certeza | je suis sûr | Donner son avis | Tenho certeza de que ele vem. | Je suis sûr qu'il viendra.
ter interesse em | s'intéresser à | Tournures | Ele tem muito interesse em história. | Il s'intéresse beaucoup à l'histoire.
tirar uma foto | prendre une photo | Au quotidien | Vamos tirar uma foto juntos! | Prenons une photo ensemble !
tomar sol | prendre le soleil | Au quotidien | Tomamos sol a tarde inteira. | Nous prenons le soleil tout l'après-midi.
tomar uma decisão | prendre une décision | Tournures | Precisamos de tomar uma decisão logo. | Nous devons bientôt prendre une décision.
um momento | un instant, ne quittez pas | Au quotidien | Um momento, não desligue, por favor. | Un instant, ne quittez pas, s'il vous plaît.
um pouco de | un peu de | Au quotidien | Põe-me um pouco de açúcar. | Mets-moi un peu de sucre.
voltar a | refaire, recommencer à | Au quotidien | Volte a ler com calma. | Relis-le calmement.
É verdade | C'est vrai | Donner son avis | O caminho é mais curto. – É verdade. | Le chemin est plus court. – C'est vrai.
"""
