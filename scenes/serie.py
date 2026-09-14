# -*- coding: utf-8 -*-
"""Le plan des 71 episodes : un theme x NIVEAU de l'app par episode.

    python scenes/serie.py          ->  scenes/serie.html

L'IDEE, ET POURQUOI ELLE CHANGE L'ECONOMIE DE LA SERIE
    Chaque episode s'appuie sur un theme qui EXISTE DEJA dans themes.json.
    Son vocabulaire est donc dans les cartes avant d'etre dans la video :
    l'apprenant reconnait au lieu de decouvrir, et tests/lexique.py passe par
    construction au lieu d'exiger un ajout a chaque fois.

    On n'ecrit plus un episode puis son lexique. On prend un lexique qui
    existe et on lui ecrit une situation.

LA REGLE DE COMPREHENSIBILITE
    Un texte se comprend quand il est fait de connu plus un peu de neuf.
    L'episode 1 l'a verifie sans le chercher : 26 mots de lexique, dont 22
    deja etudies. C'est ce rapport-la qu'il faut tenir, pas l'inverse.

L'ARC, ET POURQUOI IL EST CHRONOLOGIQUE
    Mark arrive, s'installe, travaille, vit. Les demarches viennent dans
    l'ordre ou la vie les impose -- l'Anmeldung avant le bail, le bail avant
    le compte en banque. Un apprenant qui arrive vraiment en Allemagne suit
    la meme sequence, et peut donc regarder la serie comme un mode d'emploi.

    Le passage du Sie au du (episode 21) est le sommet. Tout ce qui precede
    le prepare, tout ce qui suit en vit. Voir _arc dans personnages.json.
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# n, titre allemand, titre francais, theme, niveau, situation, ce que MARK doit
# savoir dire (c'est le programme oral), presence d'Anna, ACCROCHE DE VITRINE.
#
# ⚠️ LE NEUVIEME CHAMP EST UN OUTIL DE DIFFUSION, PAS DE PEDAGOGIE. Decision de
# Jacques : « ca va peut-etre servir beaucoup plus d'outil marketing que
# n'importe quoi d'autre. » Un episode de cours et un clip de reseau ont des
# exigences OPPOSEES -- le premier s'appuie sur les precedents, le second ne
# doit rien supposer ; le premier se comprend par la langue, le second doit
# etre lisible sans les mots. On ne decouvre pas apres coup qu'un episode fera
# une bonne vitrine : on l'ecrit en le sachant.
#
# ⚠️ ET L'EPISODE 46 N'EN SERA JAMAIS UN. C'est la seule surprise de la serie ;
# la diffuser, c'est la depenser.
#
# CONSEQUENCE SUR L'ORDRE DE PRODUCTION : les vitrines se tournent EN PREMIER,
# et ca ne coute rien -- autonomes par definition, elles n'attendent aucun
# episode precedent, et la plupart n'ont besoin d'aucun personnage recurrent,
# donc d'aucun ancrage. Ce sont aussi les moins cheres.
EPISODES = [
 # ================== ACTE I -- ARRIVER (1-15) ==================
 # Mark ne connait personne. Tout le monde le vouvoie, et lui aussi.
 # Anna apparait quatre fois : le guichet, la reconnaissance, le Kiez, la table.
 (1,"Ankunft in Berlin","Arrivée à Berlin","reisen_urlaub","A2",
  "Il atterrit, cherche ses bagages, demande son chemin au guichet.",
  "Demander où se trouve quelque chose, dire d'où l'on vient et pourquoi on est là.",
  "Elle est l'employée du guichet. Premiere rencontre.",
  None),
 (2,"Beim Bürgeramt","Au Bürgeramt","stadt_gebaeude","A2",
  "La declaration de domicile obligatoire. Le rendez-vous, le formulaire, la file.",
  "Prendre un rendez-vous, remplir un formulaire, epeler son nom et son adresse.",
  None,
  "Le rendez-vous au Buergeramt : dans six semaines. La tete de Mark "
  "suffit."),
 (3,"Rot heißt rot","Rouge veut dire rouge","verkehr","A2",
  "Il traverse une rue vide au rouge, puis attend sur la piste cyclable. Deux inconnus le reprennent.",
  "Comprendre une remarque d'un inconnu, s'excuser, demander ce qu'on a fait de travers.",
  None,
  "Il traverse une rue vide au rouge pendant que six personnes attendent "
  "sagement. Rien a traduire."),
 (4,"Die Wohnungsbesichtigung","La visite d'appartement","wohnen","A2",
  "Il visite un appartement avec une agente. Les pieces, le loyer, les charges.",
  "Poser des questions sur un logement, comprendre un prix, dire ce qu'on cherche.",
  None,
  None),
 (5,"Der Umzug","Le déménagement","moebel_haushalt","A2",
  "Il emmenage. Les meubles, les cartons, ce qui manque.",
  "Nommer les meubles, dire ce dont on a besoin, demander de l'aide.",
  None,
  None),
 (6,"Im Supermarkt","Au supermarché","einkaufen_geld","A2",
  "Les courses du premier soir. Et il la reconnait dans une allee, hors de son uniforme.",
  "Demander un produit, comprendre un prix, payer.",
  "LES RETROUVAILLES. Hors uniforme, en garde-robe quotidien. Il hesite avant d'oser.",
  None),
 (7,"Auf dem Wochenmarkt","Au marché","obst_gemuese","A2",
  "Le marche du samedi. Les fruits, les legumes, les quantites.",
  "Demander une quantite, choisir, comparer.",
  "Ils s'y croisent une seconde fois. Le quartier commence a les reunir.",
  None),
 (8,"Das Konto bei der Bank","Le compte en banque","einkaufen_geld","B1",
  "Ouvrir un compte. Les papiers, la carte, les frais.",
  "Expliquer ce qu'on veut ouvrir, comprendre des conditions, poser une question d'argent.",
  None,
  None),
 (9,"Der Handyvertrag","Le forfait de téléphone","medien_technologie","A2",
  "Un contrat de telephone. Les options, la duree, ce qu'on ne comprend pas.",
  "Demander des explications, dire qu'on n'a pas compris, refuser poliment.",
  None,
  None),
 (10,"Beim Arzt anmelden","S'inscrire chez le médecin","gesundheit","A2",
  "Trouver un medecin traitant, s'inscrire, la carte d'assurance.",
  "Prendre rendez-vous, dire de quoi on souffre, comprendre une consigne.",
  None,
  None),
 (11,"Im Restaurant","Au restaurant","essen_trinken","A2",
  "Un premier repas au restaurant. La carte, la commande, l'addition.",
  "Commander, demander une recommandation, payer et laisser un pourboire.",
  "Leur premier repas ensemble. Ils se vouvoient encore, et ca commence a peser.",
  None),
 (12,"Kleidung kaufen","Acheter des vêtements","kleidung","A2",
  "L'hiver arrive. Les tailles, les couleurs, l'essayage.",
  "Demander une taille, dire ce qui va ou pas, echanger un article.",
  None,
  None),
 (13,"Kochen für Gäste","Cuisiner pour des invités","kueche_kochen","A2",
  "Il cuisine pour la premiere fois chez lui.",
  "Suivre une recette, nommer les ustensiles, inviter quelqu'un.",
  "Elle est invitee. Premiere scene hors d'un lieu public.",
  None),
 (14,"Mit der S-Bahn durch Berlin","Berlin en S-Bahn","verkehr","A2",
  "Un trajet qui tourne mal : retard, correspondance, mauvaise direction.",
  "Lire un horaire, demander une correspondance, signaler un probleme.",
  None,
  "Le trajet qui tourne mal. Comprehensible sans un mot d'allemand."),
 (15,"Die Nachbarn","Les voisins","wohnen","B1",
  "La cage d'escalier, les regles de l'immeuble, le bruit du dimanche.",
  "Se presenter a un voisin, s'excuser, demander un service.",
  None,
  None),

 # ================== ACTE II -- S'INSTALLER (16-31) ==================
 # Le travail, les papiers, le premier hiver. ⚠️ C'est ici que le `du` apparait
 # POUR LA PREMIERE FOIS -- entre collegues, ou il est la norme des le premier
 # jour. L'apprenant voit donc que le `du` n'est pas une intimite mais un
 # USAGE, ce qui rend le `Sie` maintenu avec Anna beaucoup plus parlant.
 (16,"Das Wetter und die Jahreszeiten","Le temps et les saisons","wetter","A2",
  "Le premier hiver berlinois. Le froid, la neige, les jours courts.",
  "Parler du temps, dire comment on se sent, faire des projets selon la meteo.",
  None,
  None),
 (17,"Der erste Arbeitstag","Le premier jour de travail","arbeit_buero","B1",
  "Le bureau, les collegues, ce qu'on n'ose pas demander.",
  "Se presenter a une equipe, poser une question a un collegue, dire ce qu'on sait faire.",
  None,
  None),
 (18,"Hier duzen wir uns","Ici on se tutoie","berufe","A2",
  "Un collegue lui propose le tutoiement des le premier cafe. Au bureau c'est la norme. "
  "Mark decouvre que le `du` n'est pas toujours de l'intimite.",
  "Accepter un tutoiement, se presenter informellement, parler de son metier.",
  "Absente -- et c'est le point. Il rentre en se demandant pourquoi avec elle, non.",
  "LA PLUS FORTE. Le `du` des le premier cafe au bureau -- un fait "
  "culturel qui surprend meme ceux qui parlent allemand."),
 (19,"Termine und Absprachen","Rendez-vous et accords","arbeit_buero","B1",
  "Organiser une reunion, deplacer un rendez-vous, se mettre d'accord.",
  "Proposer une date, refuser, negocier un delai.",
  None,
  None),
 (20,"Der Sprachkurs","Le cours de langue","schule","A2",
  "Il s'inscrit a un cours du soir. La salle, le materiel, les autres.",
  "S'inscrire, demander une explication, parler de ses difficultes.",
  "Elle est dans la salle d'a cote, un niveau au-dessus. Trois secondes dans un couloir.",
  None),
 (21,"Die Mitschüler","Les camarades de cours","schule","B1",
  "Les autres apprenants : une Ukrainienne, un Turc, une Iranienne. Chacun son chemin.",
  "Raconter son parcours, comparer des experiences, encourager quelqu'un.",
  None,
  None),
 (22,"Das Paket","Le colis","stadt_gebaeude","B1",
  "Un colis de Montreal. La Post, le guichet, le voisin qui l'a pris.",
  "Recuperer un envoi, remplir un avis, remercier un voisin.",
  "C'est ELLE au guichet -- mutee a la Post du quartier. Ils rient du hasard.",
  None),
 (23,"Die Krankenversicherung","L'assurance maladie","gesundheit","B1",
  "Le systeme, la carte, ce qui est couvert et ce qui ne l'est pas.",
  "Comprendre une couverture, poser une question administrative, contester une facture.",
  None,
  None),
 (24,"Beim Arzt","Chez le médecin","koerperteile","A2",
  "Une vraie consultation. Ou on a mal, depuis quand, ce qu'on prend.",
  "Decrire une douleur, situer sur le corps, comprendre une ordonnance.",
  None,
  None),
 (25,"Ein Bewerbungsgespräch","Un entretien d'embauche","berufe","B1",
  "Un entretien pour un meilleur poste.",
  "Parler de son parcours, expliquer une motivation, poser des questions sur un poste.",
  None,
  None),
 (26,"Der Mietvertrag","Le bail","wohnen","B1",
  "Le contrat, le depot, ce qu'on signe sans tout comprendre.",
  "Lire une clause, demander une precision, refuser une condition.",
  None,
  None),
 (27,"Rechnungen und Fristen","Factures et délais","einkaufen_geld","B1",
  "Le GEZ, l'electricite, une mise en demeure qui fait peur pour rien.",
  "Comprendre un delai, contester, demander un echeancier.",
  None,
  None),
 (28,"Weihnachten allein","Noël seul","feste_feiertage","A2",
  "Berlin se vide. Il est seul pour la premiere fois depuis son arrivee.",
  "Souhaiter les fetes, refuser une invitation, dire qu'on va bien quand ce n'est pas vrai.",
  "Elle l'invite au dernier moment. Il dit non, puis il regrette. Premier vrai manque.",
  "Noel seul quand la ville se vide. Tout expatrie reconnait ca."),
 (29,"Die Familie am Telefon","La famille au téléphone","familie","A2",
  "Montreal appelle. Ce qu'on raconte et ce qu'on tait.",
  "Parler de sa famille, raconter sa semaine, rassurer quelqu'un.",
  None,
  None),
 (30,"Silvester","Le Nouvel An","feste_feiertage","B1",
  "Les feux d'artifice depuis un toit. Les voeux, les resolutions, le bruit.",
  "Souhaiter la nouvelle annee, faire une promesse, parler de l'avenir.",
  "Elle est la. Ils se vouvoient encore, a minuit, et c'est devenu absurde.",
  None),
 (31,"Im Fitnessstudio","À la salle de sport","sport","A2",
  "L'abonnement, les appareils, l'employe qui parle trop vite.",
  "S'inscrire a une activite, comprendre une consigne, dire ce qu'on veut travailler.",
  None,
  "L'employe de la salle de sport qui parle trop vite. Universel."),

 # ================== ACTE III -- APPARTENIR (32-49) ==================
 # Le Verein. En Allemagne, le `du` arrive avec le club, pas avec le guichet :
 # c'est le decor qui rend le sommet possible. ⚠️ SOMMET A L'EPISODE 46.
 (32,"Der Volleyballverein","Le club de volleyball","sport","B1",
  "Il pousse la porte d'un club de quartier. L'essai, l'equipe, les horaires.",
  "Demander a essayer, comprendre des regles, dire son niveau.",
  None,
  None),
 (33,"Das erste Training","Le premier entraînement","sport","B1",
  "Il joue mal, il rit, on le reprend. Au club, tout le monde se tutoie.",
  "Encourager, s'excuser d'une erreur, demander qu'on repete.",
  "Elle joue dans ce club depuis des annees. Il ne le savait pas.",
  None),
 (34,"Die Vereinssatzung","Les statuts du club","politik_gesellschaft","B1",
  "L'assemblee, la cotisation, le proces-verbal. L'Allemagne associative.",
  "Comprendre un ordre du jour, voter, poser une question en reunion.",
  None,
  None),
 (35,"Ein Auswärtsspiel","Un match à l'extérieur","verkehr","B1",
  "Le minibus, l'autoroute, la salle d'un autre quartier.",
  "Organiser un trajet a plusieurs, lire un itineraire, raconter un match.",
  None,
  None),
 (36,"Die Verletzung","La blessure","koerperteile","B1",
  "Une cheville. L'urgence, la radio, l'arret.",
  "Decrire un accident, comprendre un diagnostic, demander un arret de travail.",
  "Elle l'accompagne aux urgences. Elle reste. Personne ne lui a rien demande.",
  None),
 (37,"Das Wohnzimmer","Le salon","moebel_haushalt","B1",
  "Convalescent chez lui. L'appartement qu'il n'avait jamais vraiment meuble.",
  "Decrire un interieur, comparer des objets, expliquer un gout.",
  None,
  None),
 (38,"Was ich koche","Ce que je cuisine","kueche_kochen","B1",
  "Il cuisine quebecois pour l'equipe. Les mots qui n'existent pas en allemand.",
  "Expliquer une recette, decrire un gout, traduire l'intraduisible.",
  "Elle est la seule a poser des questions sur Montreal plutot que sur le sirop.",
  None),
 (39,"Streit in der Mannschaft","Dispute dans l'équipe","gefuehle_charakter","A2",
  "Deux joueurs s'accrochent. Mark doit prendre parti, ou pas.",
  "Dire son desaccord, calmer, refuser de choisir.",
  None,
  None),
 (40,"Musik am Abend","Musique le soir","musik_kunst","A2",
  "Un concert dans une cave de Kreuzberg. Trop fort pour parler.",
  "Donner son avis, decrire une impression, proposer de sortir.",
  "Ils n'arrivent pas a se parler de la soiree. Ils se textent toute la nuit.",
  None),
 (41,"Ein Ausflug an den See","Une sortie au lac","natur","A2",
  "Le premier beau dimanche. Le train regional, le lac, le silence.",
  "Decrire un paysage, proposer une excursion, parler de ce qu'on aime.",
  "Une journee entiere a deux. Toujours `Sie`. C'est devenu une blague entre eux.",
  None),
 (42,"Die Kollegin aus Kanada","La collègue du Canada","berufe","B1",
  "Une Quebecoise arrive au bureau. Avec elle, tout est facile -- et c'est le probleme.",
  "Comparer deux langues, expliquer un malentendu culturel, dire ce qui manque.",
  "Anna les voit ensemble au marche. Elle ne dit rien. Elle ne dit surtout rien.",
  None),
 (43,"Ein Missverständnis","Un malentendu","gefuehle_charakter","B1",
  "Une phrase mal comprise, et trois jours de silence.",
  "Expliquer un sentiment, demander pardon, dire ce qu'on a cru comprendre.",
  "C'est elle qui ecrit la premiere. Deux lignes, tres sobres.",
  None),
 (44,"Der Wochenmarkt im Frühling","Le marché au printemps","obst_gemuese","B1",
  "Les premieres asperges. Le meme marchand qu'a l'episode 7, un an apres.",
  "Choisir de saison, negocier, raconter une habitude.",
  "Ils se retrouvent la, ou tout a commence. Le marchand les croit ensemble.",
  None),
 (45,"Das Vorstellungsgespräch","L'entretien décisif","arbeit_buero","B2",
  "Le poste qui decide s'il reste a Berlin ou s'il rentre.",
  "Defendre une candidature, parler de long terme, poser une question difficile.",
  None,
  None),
 (46,"Sie oder du?","Sie ou du ?","gefuehle_charakter","B1",
  "LE SOMMET DE LA SERIE. Il a le poste, il reste. Elle propose le `du` -- et en "
  "allemand ce n'est pas une formalite : ca se propose, ca s'accepte, ca a un moment. "
  "Le basculement de langue EST le basculement de la relation.",
  "Proposer le tutoiement, accepter, dire ce qu'on ressent sans le surjouer.",
  "L'episode est le sien autant que le sien. Tout ce qui precede le prepare.",
  None),
 (47,"Das erste Du","Le premier « du »","sprache_kommunikation","C1",
  "Le lendemain. Ils se trompent encore, ils rient, ils se reprennent.",
  "Corriger quelqu'un gentiment, se reprendre, jouer avec le registre.",
  "Toute la scene est faite de leurs erreurs. C'est la plus tendre de la serie.",
  None),
 (48,"Ein Fest bei Freunden","Une fête chez des amis","feste_feiertage","B1",
  "Un anniversaire. Les cadeaux, les toasts, la petite gene sociale.",
  "Feliciter, offrir, remercier, prendre conge.",
  "Elle le presente a ses amis. Il n'est plus un nouvel arrivant.",
  None),
 (49,"Am Wochenende","Le week-end","freizeit_hobbys","A2",
  "Ce qu'on fait de son temps libre quand on a enfin du temps libre.",
  "Proposer une activite, accepter ou refuser, raconter son week-end.",
  None,
  None),

 # ================== ACTE IV -- VIVRE (50-63) ==================
 # Le `du` est installe avec Anna et le club ; le `Sie` reste partout ailleurs.
 # C'est la que l'apprenant apprend a CHOISIR son registre selon l'interlocuteur.
 (50,"Zusammenziehen?","Emménager ensemble ?","wohnen","B2",
  "La question posee trop tot, et ce qu'elle revele.",
  "Peser le pour et le contre, exprimer une reserve, differer une decision.",
  "Elle dit non. Pour de bonnes raisons. Il l'entend mal, puis il l'entend.",
  None),
 (51,"Der Handwerker","L'artisan","moebel_haushalt","A2",
  "Un chauffage qui lache en fevrier. Le devis, le rendez-vous, l'attente.",
  "Decrire une panne, demander un devis, se plaindre poliment.",
  None,
  "Le chauffage qui lache en fevrier, le devis, l'attente."),
 (52,"Beim Zahnarzt","Chez le dentiste","gesundheit","B1",
  "La douleur, la salle d'attente, les mots qu'on ne veut pas apprendre.",
  "Decrire une douleur precise, comprendre un traitement, demander le cout.",
  None,
  None),
 (53,"Die Steuererklärung","La déclaration d'impôts","einkaufen_geld","B2",
  "Le formulaire allemand dans toute sa gloire. Un collegue l'aide.",
  "Comprendre un document officiel, demander de l'aide, expliquer sa situation.",
  None,
  None),
 (54,"Mülltrennung","Le tri des déchets","umwelt","A2",
  "Les cinq poubelles, la consigne, la voisine qui surveille.",
  "Expliquer un geste, poser une question pratique, accepter une remarque.",
  None,
  "Les cinq poubelles et la voisine qui surveille. Vrai, drole, "
  "partageable."),
 (55,"Fahrrad statt Auto","Le vélo plutôt que la voiture","umwelt","B1",
  "Il achete un velo d'occasion. L'annonce, l'essai, la negociation.",
  "Acheter d'occasion, negocier, defendre une habitude.",
  None,
  None),
 (56,"Der Urlaub an der Ostsee","Les vacances sur la Baltique","reisen_urlaub","B1",
  "Une semaine a deux. La reservation, la pluie, le sable.",
  "Reserver, se plaindre d'un hebergement, raconter des vacances.",
  "Leur premier voyage. Le premier ou il ne traduit plus dans sa tete.",
  None),
 (57,"Tiere im Haus","Des animaux à la maison","tiere","A2",
  "Un chat trouve dans la cour. Le veterinaire, la litiere, le nom.",
  "Parler d'un animal, decrire un comportement, prendre une decision a deux.",
  None,
  "Le chat trouve dans la cour. Ne demande aucune langue."),
 (58,"Der Garten","Le jardin","natur","B1",
  "Un Schrebergarten, l'institution allemande. Les regles, les voisins, la haie.",
  "Comprendre un reglement, planter, discuter avec un voisin pointilleux.",
  None,
  "Les regles du Schrebergarten. L'Allemagne en un plan."),
 (59,"Das Fernsehen und die Nachrichten","La télévision et les nouvelles","medien_technologie","B1",
  "Il comprend enfin le journal televise. Et ce qu'il comprend le derange.",
  "Resumer une information, donner un avis, nuancer.",
  None,
  None),
 (60,"Politik am Küchentisch","La politique à la table de cuisine","politik_gesellschaft","A2",
  "Une elections locale. Il ne vote pas encore, et ca lui pese.",
  "Dire une opinion, ecouter un desaccord, poser une question naive sans honte.",
  "Ils ne sont pas d'accord. Pour la premiere fois, ca ne fait pas peur.",
  None),
 (61,"Ein schwieriges Gespräch","Une conversation difficile","gefuehle_charakter","B2",
  "Un desaccord qui compte. Dire ce qui ne va pas sans blesser.",
  "Exprimer un desaccord de fond, s'excuser, expliquer un sentiment complexe.",
  "C'est avec elle. La serie a gagne le droit d'avoir une scene comme celle-la.",
  None),
 (62,"Die Schwiegereltern","Les beaux-parents","familie","B1",
  "Le repas chez les parents d'Anna. Le `Sie` revient, et il brule.",
  "Se presenter a une famille, repondre a des questions personnelles, remercier.",
  "Sa mere le vouvoie. Son pere le tutoie d'emblee. Il ne sait plus quoi faire.",
  "Sa mere le vouvoie, son pere le tutoie. Il ne sait plus quoi faire."),
 (63,"Montreal im Sommer","Montréal en été","familie","A2",
  "Il rentre deux semaines. Tout est pareil et rien ne l'est.",
  "Raconter un pays a quelqu'un, comparer deux vies, expliquer un choix.",
  "Elle vient. Sa famille parle francais trop vite. Elle sourit et tient bon.",
  None),

 # ================== ACTE V -- RESTER (64-72) ==================
 # Les demarches longues, celles qui disent qu'on reste. Et la boucle.
 (64,"Die Aufenthaltserlaubnis","Le titre de séjour","politik_gesellschaft","B1",
  "L'Auslaenderbehoerde. Les papiers, les delais, la peur de l'arbitraire.",
  "Constituer un dossier, relancer une administration, comprendre une decision.",
  None,
  None),
 (65,"Ein neuer Job","Un nouvel emploi","arbeit_buero","B1",
  "Il change d'entreprise. La demission, le preavis, le certificat de travail.",
  "Demissionner, negocier un depart, demander une lettre de recommandation.",
  None,
  None),
 (66,"Die Universität","L'université","universitaet","A2",
  "Il reprend des cours du soir. L'inscription, les frais, l'emploi du temps.",
  "S'inscrire, comprendre un programme, organiser son temps.",
  None,
  None),
 (67,"Prüfungsangst","La peur de l'examen","schule","B1",
  "Le B1 officiel. L'inscription, la salle, les quatre epreuves.",
  "Parler d'une peur, demander des conseils, raconter une epreuve.",
  "Elle le fait reviser. Elle est meilleure prof que patiente.",
  None),
 (68,"Der Einbürgerungstest","Le test de naturalisation","politik_gesellschaft","B2",
  "Trente-trois questions sur un pays qu'il croyait connaitre.",
  "Repondre a des questions civiques, expliquer une institution, dire pourquoi on reste.",
  None,
  None),
 (69,"Was ich vermisse","Ce qui me manque","gefuehle_charakter","B1",
  "Ce qu'on perd en gagnant une vie ailleurs. Sans pathos.",
  "Exprimer un manque, nuancer un regret, dire ce qu'on ne regrette pas.",
  "Elle ecoute sans consoler. C'est exactement ce qu'il fallait.",
  None),
 (70,"Der Umzug, zum zweiten Mal","Le déménagement, la deuxième fois","wohnen","A2",
  "Un autre appartement, dans le meme Kiez. Cette fois ils sont deux a porter.",
  "Organiser un demenagement, demander de l'aide, remercier une equipe.",
  "Ils emmenagent. Trois ans apres le non de l'episode 50, et il n'a pas redemande.",
  None),
 (71,"Das Fest im Verein","La fête du club","vereinsleben","C1",
  "Le tournoi annuel, le barbecue, les discours trop longs. Il en fait un.",
  "Faire un discours court, remercier un groupe, raconter une anecdote.",
  "Il parle d'elle devant trente personnes, en allemand, sans preparer.",
  None),
 (72,"Ein Jahr in Berlin","Une vie à Berlin","zeit_kalender","B1",
  "Le meme aeroport qu'a l'episode 1. Il y accompagne quelqu'un qui arrive.",
  "Raconter des annees, comparer avant et apres, renseigner un inconnu.",
  "BOUCLE AVEC L'EPISODE 1. Le meme comptoir -- et cette fois c'est LUI qui "
  "reprend gentiment l'allemand d'un nouvel arrivant. Elle regarde.",
  None),
]


def themes_dispo():
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]
    d = {}
    for t in th:
        base = re.sub(r"_(a1|a2|b1|b2|c1)$", "", t["id"])
        d.setdefault(base, {"nom": t["nom_theme"], "niv": {}})
        d[base]["niv"][t["niveau"]] = len(t["mots"])
    return d


def html(dispo):
    e = lambda s: str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    o = ["""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Wortando &mdash; le plan des 71 &eacute;pisodes</title><style>
:root{color-scheme:light}
body{margin:0;background:#F2EEE2;color:#1C2430;
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:60rem;margin:0 auto;padding:2rem 1.25rem 5rem}
h1{font-size:1.7rem;margin:0 0 .25rem}
.sous{color:#6b6558;margin:0 0 2rem}
.note{background:#fff;border:1px solid #e2dcc9;border-radius:10px;padding:1rem 1.25rem;margin-bottom:2.5rem}
h2.bloc{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:#6b6558;
 margin:2.5rem 0 .75rem;border-bottom:1px solid #d8d1bd;padding-bottom:.3rem}
article{background:#fff;border:1px solid #e2dcc9;border-radius:10px;padding:1rem 1.15rem;margin-bottom:.9rem}
article.fait{border-color:#7a9a5b;background:#f6faf2}
article.sommet{border-color:#E8A23A;background:#fdf7ec}
.tete{display:flex;gap:.6rem;align-items:baseline;flex-wrap:wrap;margin-bottom:.5rem}
.num{font:600 1.05rem ui-monospace,Menlo,Consolas,monospace;color:#6b6558}
.de{font-size:1.1rem;font-weight:600}
.fr{color:#6b6558}
.tag{font-size:.72rem;background:#eae4d3;color:#5a5446;border-radius:4px;padding:.1rem .45rem}
.tag.n{background:#1C2430;color:#e8e4d8}
p{margin:.35rem 0}
.lab{font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:#6b6558}
.anna{border-left:3px solid #E8A23A;padding-left:.7rem;margin-top:.6rem}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) body{background:#15181d;color:#e8e4d8}
:root:not([data-theme="light"]) article,:root:not([data-theme="light"]) .note{background:#1e232a;border-color:#2e353f}
:root:not([data-theme="light"]) .fr,:root:not([data-theme="light"]) .sous,
:root:not([data-theme="light"]) .lab,:root:not([data-theme="light"]) h2.bloc{color:#9aa3ae}
:root:not([data-theme="light"]) .tag{background:#2e353f;color:#c9d1da}
:root:not([data-theme="light"]) article.fait{background:#1b2620;border-color:#4a6b3a}
:root:not([data-theme="light"]) article.sommet{background:#2a2318;border-color:#8a6a2a}}
</style></head><body><main>"""]
    o.append("<h1>Le plan des 30 épisodes</h1>")
    o.append('<p class="sous">Un thème de l\'app par épisode &middot; ~90 s chacun &middot; '
             'généré par <code>scenes/serie.py</code></p>')
    o.append("""<div class="note"><p><b>Le principe.</b> Chaque épisode s'appuie sur un thème
qui existe <b>déjà</b> dans <code>themes.json</code>. Son vocabulaire est donc dans les cartes
avant d'être dans la vidéo : l'apprenant <b>reconnaît</b> au lieu de découvrir.</p>
<p><b>Ce que ça change.</b> On n'écrit plus un épisode puis son lexique. On prend un lexique qui
existe et on lui écrit une situation. <code>tests/lexique.py</code> passe par construction.</p>
<p><b>Les répliques de Mark sont le programme.</b> Ce sont les phrases que l'apprenant devra
savoir produire — l'oral du DTZ et du B1. Celles d'Anna et des employés sont ce qu'il doit
savoir comprendre.</p></div>""")

    blocs = [(1, 9, "L'installation &mdash; les démarches d'un nouvel arrivant"),
             (10, 15, "Le quotidien &mdash; vivre dans le quartier"),
             (16, 20, "Le travail, et le basculement"),
             (21, 30, "La vie &mdash; une année complète")]
    for d0, d1, titre in blocs:
        o.append('<h2 class="bloc">%s &nbsp;·&nbsp; épisodes %d à %d</h2>' % (titre, d0, d1))
        for n, de, fr, th, niv, sit, mark, anna, vitrine in EPISODES:
            if not (d0 <= n <= d1):
                continue
            info = dispo.get(th)
            mots = info["niv"].get(niv, 0) if info else 0
            nom = info["nom"] if info else "THEME INTROUVABLE"
            cls = " class=\"fait\"" if n == 1 else (" class=\"sommet\"" if n == 45 else "")
            o.append("<article%s>" % cls)
            o.append('<div class="tete"><span class="num">%02d</span>'
                     '<span class="de">%s</span><span class="fr">%s</span>'
                     '<span class="tag n">%s</span><span class="tag">%s &middot; %d mots</span>%s</div>'
                     % (n, e(de), e(fr), niv, e(nom), mots,
                        '<span class="tag">TOURNÉ</span>' if n == 1 else ''))
            o.append("<p>%s</p>" % e(sit))
            o.append('<p><span class="lab">Mark doit savoir</span><br>%s</p>' % e(mark))
            if anna:
                o.append('<div class="anna"><span class="lab">Anna</span><br>%s</div>' % e(anna))
            o.append("</article>")
    o.append("</main></body></html>")
    return "\n".join(o)


def main():
    dispo = themes_dispo()
    perdus = [(n, th) for n, _, _, th, _, _, _, _, _ in EPISODES if th not in dispo]
    if perdus:
        sys.exit("  THEMES INTROUVABLES : %s" % perdus)
    maigres = [(n, th, niv, dispo[th]["niv"].get(niv, 0))
               for n, _, _, th, niv, _, _, _, _ in EPISODES if dispo[th]["niv"].get(niv, 0) < 10]
    if maigres:
        print("  ATTENTION, moins de 10 mots disponibles :")
        for n, th, niv, c in maigres:
            print("     episode %02d  %s %s  %d mots" % (n, th, niv, c))
    out = os.path.join(RACINE, "scenes", "serie.html")
    io.open(out, "w", encoding="utf-8", newline="").write(html(dispo))
    themes = {th for _, _, _, th, _, _, _, _, _ in EPISODES}
    print("  %d episodes, %d themes distincts, tous presents dans themes.json"
          % (len(EPISODES), len(themes)))
    print("  ->  scenes/serie.html")


if __name__ == "__main__":
    main()
