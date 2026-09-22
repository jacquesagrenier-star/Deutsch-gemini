# -*- coding: utf-8 -*-
"""Les fautes de prompt qu'on a deja payees -- et qu'on ne repaiera plus.

    python video/verifier_prompt.py --scene 02-beim-buergeramt
    python video/verifier_prompt.py <un fichier de prompt>

POURQUOI CE FICHIER EXISTE, ET POURQUOI IL EST UN PROGRAMME ET PAS UNE NOTE.

Le 16 septembre 2026, Jacques : << j'ai l'impression qu'on n'apprend pas de nos
erreurs suffisamment >>. Il avait raison, et la preuve etait dans le depot :
chaque faute ci-dessous etait DEJA ecrite quelque part -- dans A-TOURNER.txt,
dans OU-ON-EN-EST.txt, dans le journal des retours -- et chacune a ete refaite
malgre tout.

Une lecon rangee dans un document se relit quand on y pense. Celle-ci s'execute
avant chaque depense : `omnihuman.py` appelle ce controle avant de televerser
quoi que ce soit, et refuse de payer sur une faute connue. C'est la seule forme
de memoire qui ait tenu jusqu'ici dans ce projet -- la meme idee que
`tests/verifier.py` pour l'application.

⚠️ CE QU'IL NE SAIT PAS FAIRE. Il lit du texte, pas une intention : il
   n'attrapera jamais une direction de jeu fausse, un contresens, une phrase
   allemande maladroite. Il attrape ce qui est ATTRAPABLE, c'est-a-dire ce
   qu'on a deja paye deux fois. Passer le controle ne veut pas dire que le
   prompt est bon.

⚠️ ET CHAQUE REGLE PORTE SA DATE ET SON COUT. Sans ca, la liste devient un
   reglement qu'on ne discute plus. Une regle dont la cause a disparu doit
   pouvoir etre retiree -- il suffit de savoir d'ou elle venait.
"""
import argparse
import glob
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Les fautes. (code, gravite, motif, titre, ce qu'elle a coute, comment faire)
# --------------------------------------------------------------------------
#   "faute"  -> on ne depense pas. Elle nous a deja coute une prise.
#   "doute"  -> on previent et on continue. Elle demande un coup d'oeil.
REGLES = [
    ("garde-negative", "faute",
     # ⚠️ ELARGIE LE 16 SEPT. 2026, APRES UNE RELECTURE CROISEE.
     #    La premiere version n'enumerait que les formulations exactes de
     #    l'episode 2 : elle ne voyait donc QUE le passe. Un relecteur
     #    exterieur a propose << No feet or shoes touch the red lane >> en
     #    le presentant comme une garde POSITIVE -- et le controle l'a
     #    laisse passer sans broncher.
     #
     #    La forme dangereuse n'est pas un vocabulaire, c'est une
     #    STRUCTURE : une negation qui nomme un ACTEUR et une ACTION. Pour
     #    la refuser, le modele doit d'abord se representer l'acteur en
     #    train d'agir -- et c'est precisement ce qu'il fabrique.
     r"(?i)(\b(no head|no hair|no face|no shoulder|no blurred figure|"
     r"no part of anyone|is NEVER seen|nobody walks in|nobody passes)\b"
     r"|\bno\s+\w+(?:\s+(?:or|and)\s+\w+)?\s+"
     r"(?:touch|touches|enter|enters|appear|appears|walk|walks|pass|"
     r"passes|cross|crosses|stand|stands|move|moves|is seen|are seen)\b"
     # ⚠️ ELARGIE UNE DEUXIEME FOIS LE MEME JOUR, ET CA COMPTE.
     #    16 sept. 2026, au soir : les deux premieres prises d'avatar de
     #    l'episode 3 reviennent avec les deux personnages TOURNES VERS
     #    L'OBJECTIF. Le prompt disait << He NEVER faces the camera >>.
     #    1,23 $, et un champ/contrechamp detruit -- deux hommes qui
     #    devaient se parler regardent le spectateur.
     #
     #    La regle avait pourtant ete elargie quelques heures plus tot,
     #    a << no <acteur> <action> >>. Elle ratait << never >>.
     #
     #    ET C'EST LA LECON DERRIERE LA LECON : enumerer des FORMES de
     #    negation est un jeu qu'on perd, parce que chaque elargissement
     #    arrive APRES la depense. On couvre les charnieres usuelles --
     #    no, never, does not -- en sachant que la liste restera
     #    incomplete. La vraie parade n'est pas le controle : c'est de
     #    ne pas ECRIRE de garde negative, et de decrire un etat.
     r"|\b(?:he|she|they|it|his|her|their)\s+\w{0,12}\s?"
     r"(?:never|does not|doesn't|do not|don't|will not|won't)\s+\w+"
     r"|\b(?:never|does not|doesn't)\s+(?:face|faces|look|looks|turn|"
     r"turns|move|moves|leave|leaves)\b)",
     u"La garde qui enumere ce qu'il ne faut pas montrer",
     u"16 sept. 2026 : QUATRE prises sur six (09, 13, 15, 17). On a obtenu une "
     u"nuque, des cheveux, une epaule, un bras, une silhouette floue -- "
     u"exactement les mots de l'interdiction, du cote precis ou elle "
     u"s'appliquait. ~2,80 $ et une demi-journee.",
     u"Ces modeles n'ont aucun canal pour les negations : le schema de l'API "
     u"n'a ni negative_prompt ni seed, donc tout ce qu'on ecrit decrit ce "
     u"qu'il faut MONTRER. Remplir la place plutot que l'interdire : << To his "
     u"left the counter runs on, bare except for the sign and the stamp, and "
     u"behind it a plain pale-green wall. >>"),

    ("absent-qui-agit", "faute",
     # ⚠️ ELARGIE LE 16 SEPT. 2026 AU SOIR, APRES UNE SILHOUETTE ENTREE PAR
     #    LA DROITE au plan 16. Le bloc de decor des ONZE prompts disait
     #    << his eyes rest on a fixed point just beyond the right edge of the
     #    frame, THE WAY ONE LOOKS AT SOMEONE ONE IS SPEAKING TO >>. La
     #    derniere proposition ne decrit pas un regard : elle DECLARE UNE
     #    PERSONNE juste hors du cadre, et le modele l a fait entrer.
     #
     #    La regle ne voyait que les formulations de l episode 2 -- des objets
     #    qu une main hors champ devait prendre. Elle couvre maintenant aussi
     #    les PERSONNES hors champ qu on nomme sans y penser, en croyant
     #    decrire une direction de regard.
     r"(?i)(until it is taken|when he takes it|once he takes it|"
     r"hands? it to (him|her)|as (he|she) takes"
     r"|someone (\w+ ){0,3}(is speaking|is talking|he is addressing)"
     r"|the (person|man|woman) (he|she) is (speaking|talking) to"
     r"|the way one looks at someone)",
     u"Une consigne que seule la personne hors champ pourrait accomplir",
     u"16 sept. 2026, plan 13 : << the hand stays out until it is taken >>, "
     u"alors qu'un autre paragraphe interdit qu'on voie Mark. Personne ne peut "
     u"prendre la feuille. Le modele a tranche : il l'a ramenee vers lui, puis "
     u"elle a disparu. 0,73 $.",
     u"Une action ne peut dependre que de ce qui est DANS le cadre. Ecrire "
     u"l'etat final voulu : << it simply stays offered >>."),

    ("geste-qui-revient", "faute",
     r"(?i)(comes? back down|come back to the counter|lets the arm come back|"
     r"lowers the (arm|hand)|brings? it back|returns? (it )?to the counter)",
     u"Un geste qu'on demande d'annuler avant la fin du plan",
     u"16 sept. 2026, plan 13 : << lets the arm come back down to the counter >>. "
     u"Le modele a obei, et le geste central du plan -- tendre le formulaire -- "
     u"etait detruit. Signale par Jacques avant moi. 0,73 $.",
     u"Un plan de quatre secondes montre UN etat, et il le tient jusqu'a la "
     u"derniere image. Ce qui est tendu reste tendu."),

    ("trop-de-temps", "doute",
     None,   # compte les marqueurs, voir plus bas
     u"Plus de trois temps dans un plan de quatre secondes",
     u"16 sept. 2026, plan 13 : taper la feuille, la tendre, parler, attendre. "
     u"Le geste ajoute n'a jamais ete visible, et il a probablement brouille "
     u"l'ordre du reste.",
     u"OmniHuman est pilote par l'audio : il fait la bouche et des "
     u"micro-mouvements. Ce n'est pas un metteur en scene. Decrire un ETAT, pas "
     u"un enchainement."),

    ("geste-deja-dans-l-image", "doute",
     r"(?i)(First he (holds|picks|lifts|takes|reaches)|then holds it out|"
     r"picks up the)",
     u"Un geste qu'on demande de COMMENCER, alors que l'image le montre fini",
     u"16 sept. 2026, plan 13 : l'image maitresse montre la feuille DEJA "
     u"tendue, et le prompt demandait de la tendre. Le modele a du inventer un "
     u"avant et un apres -- d'ou le bras qui revient.",
     u"Ouvrir l'image avant d'ecrire. Si le geste y est deja fait, dire << "
     u"exactly as in the image >> et ne rien demander d'autre."),

    ("camera-qui-bouge", "doute",
     r"(?i)(zoom in|push[- ]in|dolly|pan (left|right)|tracking shot)",
     u"Un mouvement de camera dans une serie a camera verrouillee",
     u"Regle de la serie depuis l'episode 1 : tous les plans sont fixes, sinon "
     u"les raccords ne tiennent pas entre deux plans generes separement.",
     u"⚠️ LE REMEDE A CHANGE LE 16 SEPT. 2026 AU SOIR, et le motif est "
     u"embarrassant : cette regle PRESCRIVAIT une phrase a trois negations "
     u"-- << no zoom, no push-in, no camera movement of any kind >> -- dans "
     u"un fichier dont la toute premiere regle explique que ces modeles "
     u"fabriquent ce qu'on leur interdit. Et la caméra a recadré en cours "
     u"de plan sur la reprise du plan 09. On decrit donc un ETAT : "
     u"<< The camera is locked on a tripod and stays there for the whole "
     u"shot: the same lens, the same height, the same distance. >> Et pour "
     u"la queue : << The framing holds to the very end: in the last frame he "
     u"is the same size and in the same place in the picture as in the "
     u"first. >>"),

    # ----------------------------------------------------------------------
    # CE QUE L'EPISODE 1 A DEJA PAYE (video/PROCEDURE-episode.md, section
    # << Les cinq pieges, chacun paye d'une prise >>).
    #
    # ⚠️ TOUS ETAIENT DEJA ECRITS quand on a tourne l'episode 2, et l'un d'eux
    # -- << minimal negation >> -- a quand meme coute quatre prises. C'est
    # exactement la remarque de Jacques le 16 septembre : une lecon rangee dans
    # un document se relit quand on y pense. Elles s'executent maintenant.
    # ----------------------------------------------------------------------
    ("pas-de-verbe-de-parole", "faute",
     None,   # cherche une liste de verbes, voir controler()
     u"Aucun vrai verbe de parole dans le prompt",
     u"Episode 1 : c'est le remede que donne le guide d'OmniHuman pour les "
     u"bouches qui bougent mal -- << Unnatural lip movements: add explicit "
     u"speaking verbs >>. Nos premiers prompts le mettaient en derniere ligne "
     u"comme une contrainte technique, et les levres etaient fausses.",
     u"Ecrire ce qu'il DIT, avec un verbe : he says, he asks, he answers, he "
     u"greets, he explains, he names, he lists, he repeats."),

    ("fin-sans-intention", "faute",
     None,   # cherche le bloc d'apres-parole, voir controler()
     u"Rien apres la parole : l'avatar retombe en poker-face",
     u"Episode 1, documente : sans bloc d'apres-parole, le visage se fige des "
     u"que le son s'arrete. Et la moitie d'un plan de quatre secondes est du "
     u"silence -- duree_audio n'est PAS la duree du plan.",
     u"Finir par ce qu'il veut pendant qu'il se tait : << he listens without "
     u"speaking >>, et ce qui vit -- il cligne, il respire, il attend. Une "
     u"queue de plan a besoin d'une INTENTION, pas seulement de gestes."),

    ("verbe-sans-plafond", "doute",
     r"(?i)\b(lifts?|raises?) (his|her|one) (hand|arm|eyebrows?)\b",
     u"Un verbe fort sans amplitude : il sera sur-joue",
     u"Episode 1, une prise : << she lifts one hand >> -- la main est partie en "
     u"l'air. Le modele obeit au verbe s'il n'a rien d'autre.",
     u"Nommer l'amplitude AVEC le geste : << lifts one hand a few centimetres "
     u"from the counter and settles it back >>."),

    ("qualificatifs-empiles", "doute",
     None,   # compte les attenuateurs, voir controler()
     u"Des attenuations empilees : ce sera sous-joue jusqu'a l'invisible",
     u"Episode 1, une prise : << a small, gentle, closed-lipped smile... "
     u"nothing broad >> a donne presque rien. LE MODELE OBEIT AUX "
     u"MODIFICATEURS PLUS QU'AU VERBE.",
     u"Decrire l'etat d'arrivee plutot que des limites : << a half-smile that "
     u"reaches his eyes >>, et s'arreter la."),

    ("decrit-ce-que-l-image-porte", "doute",
     r"(?i)(depth of field|\b\d{2}mm\b|bokeh|soft overhead|"
     u"he wears|she wears|his hair is|her hair is|the lighting is)",
     u"Le prompt decrit ce que l'image montre deja",
     u"Episode 1 : << soft overhead terminal lighting, shallow depth of field, "
     u"50mm >> ajoutes sur la foi d'un guide TEXTE-vers-video, ou rien "
     u"n'existe avant le prompt. Ici l'image existe, et leur fiche le dit : "
     u"<< Do not describe static visual details already visible in the input "
     u"image. >>",
     u"Ne decrire que ce qui BOUGE : le visage, le regard, le geste, la "
     u"respiration."),

    ("minutage-en-secondes", "faute",
     r"(?i)\b(at|after|for|during)\s+\d+([.,]\d+)?\s*(s\b|sec|second)",
     u"Une fenetre de parole donnee en secondes",
     u"Episode 1 : c'etait la panne de Seedance -- il recevait des chiffres et "
     u"faisait ce qu'il voulait, de +0,11 a +1,96 s d'ecart. Chez un modele "
     u"pilote par l'audio, les reintroduire referait le defaut.",
     u"Le son porte deja le minutage : << let his face follow the voice >>."),

    ("objet-qui-se-materialise", "doute",
     None,   # objet nomme + plan large sans dire ce que tiennent les mains
     u"Un objet nomme, des mains dont on ne dit rien : il apparaitra dedans",
     u"16 sept. 2026, plan 15 : la replique enumere deux documents, le prompt "
     u"disait seulement << one hand may rise slightly >>, et une page A4 "
     u"couverte de texte s'est MATERIALISEE dans sa main en cours de plan -- "
     u"elle n'est pas dans l'image de depart. Signale par Jacques : << elle "
     u"apparait d'un seul coup, ce n'est pas du tout realiste >>. 0,70 $.",
     u"MEME CAUSE QUE LA GARDE NEGATIVE, et c'est le principe general : ce que "
     u"le prompt NOMME, le modele le fabrique -- meme quand la phrase parle de "
     u"ce que le personnage DIT et non de ce qu'on voit. Dans un plan ou les "
     u"mains sont visibles, dire ce qu'elles tiennent, y compris rien : << his "
     u"hands rest on the counter, open and empty, and they stay there >>."),

    ("icone-nommee-par-son-nom", "faute",
     r"(?i)\b(ampelm(ae|ä)nnchen|ampelmann|berlin man|"
     r"east berlin (man|figure|signal))\b",
     u"Une icone appelee par son nom : c'est l'enseigne qui vient, pas l'objet",
     u"16 sept. 2026, DEUX images de mark-marche perdues (0,30 $). Le prompt "
     u"decrivait pourtant le chapeau et les deux bras tendus. Le modele a "
     u"boulonne un PANNEAU CARRE ROUGE sur le mat -- avec la pose du VERT "
     u"coloriee en rouge -- et laisse dans le boitier une silhouette "
     u"quelconque. Jacques : << il l'a mis sur le poteau et non dans le feu "
     u"lui-meme >>.",
     u"Le nom propre d'une icone convoque l'imagerie qui l'entoure -- "
     u"panneaux, autocollants, vitrines a souvenirs -- et aucun luxe de "
     u"detail ne dit assez fermement OU elle est posee. Deux remedes, dans "
     u"cet ordre : (1) NE PAS LA NOMMER, decrire la lampe seule, << the upper "
     u"round lens is lit and glows an even plain red >> ; (2) la DESSINER et "
     u"l'incruster -- video/ampelmann.py. Un dessin ne derive pas, il est "
     u"gratuit, et les huit plans recoivent la meme icone au pixel pres."),

    ("evenement-qui-se-planifie", "doute",
     r"(?i)(then|next|after that)[^.]{0,80}(rides? into|walks? into|"
     r"enters?|comes? into|appears?)",
     u"Une ENTREE decrite comme un evenement : le modele choisit quand",
     u"22 sept. 2026, plan 18 : << Then a cyclist RIDES INTO THE PICTURE >>. "
     u"Jacques : << le cycliste arrive un peu tard ; il faut qu'on voie entrer "
     u"son pneu avant >>. Un evenement se PLANIFIE ; le modele l'a mis a 1,6 s "
     u"d'un plan de 4 s. 1,69 $ de reprise.",
     u"Decrire l'ETAT DE LA PREMIERE IMAGE : << In the very first frame the "
     u"front wheel is already crossing the bottom edge >>. Mieux encore, si "
     u"une prise existe : en extraire l'image ou l'action est deja engagee et "
     u"partir de la -- l'entree disparait au lieu de se regler."),

    ("taille-par-adjectif", "doute",
     r"(?i)(close to the camera|large|huge|very big|fills the frame)",
     u"La taille d'un personnage donnee par un adjectif",
     u"22 sept. 2026, plan 18 : << close to the camera at first and large >>. "
     u"A 1,6 s le cycliste occupait tout l'ecran -- Mark, le feu et la rue "
     u"avaient disparu derriere un blouson jaune. L'adjectif a ete obei.",
     u"Borner par la TRAJECTOIRE, pas par un adjectif : << ridden at the far "
     u"side of the lane so that the waiting man stays visible the whole way "
     u"past >>. Une taille se deduit d'un chemin, elle ne se decrete pas."),

    ("repere-hors-champ", "doute",
     r"(?i)\b(her|his) (knees?|shoes?|feet|ankles?|boots?|waist)\b",
     u"Un decor accroche a une partie du corps qui n'est pas dans le cadre",
     u"22 sept. 2026, dame-feu, releve par Jimmy AVANT l'envoi : la bordure de "
     u"granit << at the level of her knees >> et les dalles << running right up "
     u"to her shoes >>, alors que l'image est coupee a mi-cuisse. Pour obeir, le "
     u"modele doit dezoomer -- et le visage retrecit, ce qui est precisement ce "
     u"qu'un plan destine a l'avatar ne peut pas se permettre. Rien depense.",
     u"Ouvrir l'image et n'accrocher le decor qu'a ce qu'on y VOIT : << up to the "
     u"hem of her coat and the tote bag hanging from her arm >>. Un repere hors "
     u"champ n'est pas une precision, c'est un ordre de recadrer."),

    ("corps-sans-contact", "doute",
     None,   # voir controler() : il faut une ligne de coupe
     u"Quelqu'un pose sur une surface, sans dire ou l'image coupe",
     u"22 sept. 2026, dame-trottoir, 0,15 $, ET C'EST JACQUES QUI L'A VU, pas "
     u"le controle ni moi : le manteau et le sac s'arretent EN L'AIR au-dessus "
     u"du pave -- ni jambes, ni pieds, ni ombre, ni point de contact. J'avais "
     u"mesure la tete et declare la geographie bonne sur une image ou la dame "
     u"ne touche pas le sol dont ce plan doit justement prouver qu'elle y est. "
     u"⚠️ ET CETTE REGLE-LA NE L'AURAIT PAS ARRETEE : le prompt disait bien "
     u"<< seen from the waist up >>. C'est sol-bord-a-bord qui l'attrape -- la "
     u"coupe etait ANNULEE par un sol demande bord a bord. La presente regle "
     u"couvre l'autre cas, celui ou rien ne dit ou l'image s'arrete.",
     u"Un plan qui doit dire SUR QUELLE SURFACE quelqu'un se tient doit soit "
     u"montrer le contact -- << her shoes stand on the slabs, with their "
     u"shadow under them >> -- soit couper franchement au-dessus : << the "
     u"bottom edge of the picture crosses her coat just below the tote bag >>. "
     u"Entre les deux, le modele termine le corps en l'air."),

    ("sol-bord-a-bord", "doute",
     r"(?i)(fills? the whole foreground|from edge to edge"
     r"|fill(s|ing)? the bottom of the picture)",
     u"Un sol demande bord a bord : la camera recule, le visage retrecit",
     u"22 sept. 2026, dame-trottoir, 0,15 $. La geographie etait juste du "
     u"premier coup -- trottoir devant, bordure, bande rouge derriere -- mais "
     u"<< the pavement fills the whole foreground ... from edge to edge >> a "
     u"gagne contre << seen from the waist up >> : la tete est sortie a 10,5 % "
     u"de la hauteur au lieu des 18 % de dame-feu.png. Un recadrage rattrape le "
     u"visage mais perd le feu rouge, qui est ce dont elle parle.",
     u"Sur une image qui part chez OmniHuman, poser d'abord LA LIGNE DE COUPE "
     u"-- << the bottom edge of the picture crosses her coat just below the "
     u"tote bag >> -- et ne decrire le sol que DERRIERE le personnage. Un sol "
     u"qu'on veut voir en entier est un ordre de reculer la camera."),

    ("nom-du-geste", "doute",
     r"(?i)(shrug|shrugs|facepalm|thumbs up|eye ?roll|fist pump)",
     u"Le geste appele par son nom : c'est la caricature qui vient",
     u"22 sept. 2026, plan 18, releve par Jimmy avant l'envoi : << raises both "
     u"arms into a shrug >> plus << his shoulders lifted >>. Meme mecanisme que "
     u"l'icone nommee par son nom -- une abstraction convoque son imagerie. Sur "
     u"un homme VU DE DOS, des epaules qui montent se lisent comme une tete qui "
     u"s'enfonce.",
     u"Ecrire la GEOMETRIE d'arrivee et rien d'autre : << his open empty hands "
     u"come up level with his chest, one out to either side of him, his elbows "
     u"bent and carried away from his body, his palms turned up >>. Le nom du "
     u"geste est ce que le SPECTATEUR doit comprendre, pas ce qu'on ecrit."),

    ("negations-en-nombre", "doute",
     None,   # compte, voir controler()
     u"Trop de negations -- le guide du modele demande le contraire",
     u"Le guide d'OmniHuman met << clarity, non-contradiction, and minimal "
     u"negation >> en tete de ses principes. Nos prompts d'episode 1 en "
     u"alignaient QUATORZE, dont cinq d'affilee sur l'arriere-plan -- "
     u"precisement le passage qui echouait.",
     u"Un modele qui doit se representer << personne ne s'avance >> doit "
     u"d'abord se representer quelqu'un qui s'avance. Leurs propres exemples "
     u"sont positifs : << The leaves in the background sway. >>"),
]

# --------------------------------------------------------------------------
# LES ACQUIS -- ce qui MARCHE, etabli par une reussite, pas par une opinion.
# --------------------------------------------------------------------------
# ⚠️ POURQUOI CETTE SECONDE LISTE EXISTE. Demande de Jacques, 16 sept. 2026 :
#    << quand on reussit a faire ce qu'on souhaite, rentre-le dans la liste des
#    criteres a toujours passer avant d'effectuer tout prompt >>.
#
#    Jusque-la ce fichier n'avait que des FAUTES. Une liste de fautes empeche
#    de refaire ; elle n'apprend pas a faire. Chaque solution -- la retouche
#    plutot que la composition, le retrait de la reference, l'icone dessinee --
#    a du etre redecouverte, et presque toujours apres avoir paye.
#
#    (titre, date, ce qui l'a etabli, comment s'en servir)
ACQUIS = [
    (u"Une reference de MATIERE n'est pas une reference de DISPOSITION",
     u"22 sept. 2026",
     u"Plan 04. Pour remettre la dame sur le trottoir, on a reference "
     u"carrefour-rouge.png -- le meme coin, vide -- en croyant y prendre la "
     u"geographie. Or sa disposition est l'INVERSE de celle qu'on veut : chez "
     u"elle la bande rouge est au premier plan, en bas du cadre, et le pave "
     u"derriere. Le prompt disait << the grey slabs OF THE SECOND REFERENCE "
     u"fill the bottom of the picture >> : on demandait le bas d'une image "
     u"dont le bas est rouge.",
     u"Dire pour QUOI on reference, dans le prompt et dans la feuille : << POUR "
     u"LA MATIERE SEULEMENT : la teinte et le grain >>. Et ouvrir les deux "
     u"images cote a cote avant d'ecrire -- deux photos du meme lieu peuvent "
     u"etre prises depuis des cotes opposes de la rue."),

    (u"Un ancrage doit viser ce qui est DANS le cadre",
     u"22 sept. 2026",
     u"Plan 04, releve par Jimmy sur l'image. Le prompt ancrait la bordure de "
     u"granit << at the level of her knees >> et le pave << running right up to "
     u"her shoes >>. La dame est coupee a mi-cuisse : ni genoux ni chaussures "
     u"dans le cadre. Le modele aurait dezoome pour les faire apparaitre, "
     u"violant << do not resize her >> et retrecissant le visage -- qui est "
     u"justement ce dont OmniHuman a besoin.",
     u"Ancrer sur ce qu'on VOIT : le manteau, le sac, le bord du cadre. Et se "
     u"souvenir qu'en projection 2D, ce qui est plus LOIN est plus HAUT dans "
     u"l'image : << below her >> pour un element en arriere-plan est faux, et "
     u"ramene l'element au premier plan."),

    (u"Partir d'une IMAGE DE LA PRISE supprime l'entree au lieu de la regler",
     u"22 sept. 2026",
     u"Plan 18. Deux prompts d'affilee ont echoue a faire entrer un cycliste au "
     u"bon moment : trop tard, puis trop gros. Jacques : << le plan pourrait "
     u"commencer exactement sur l'image ou on voit le cycliste >>. On a extrait "
     u"la 2,6e seconde de la prise existante -- chute-depart.png -- et le plan "
     u"ouvre sur les deux hommes deja en place. Il ne reste que deux temps, et "
     u"le temps le plus difficile a piloter a disparu.",
     u"Quand un plan doit COMMENCER au milieu d'une action, ne pas la faire "
     u"demarrer : en extraire une image dans une prise existante et partir de "
     u"la. C'est gratuit, la continuite du decor est parfaite au pixel, et rien "
     u"ne reste a minuter. ⚠️ Verifier que l'image est NETTE : celle de 1,6 s "
     u"etait en bouge, et c'est la premiere image du dernier plan."),

    (u"Imprimer le prompt EXACT avant l'envoi, pas une simulation",
     u"22 sept. 2026",
     u"Plan 18. mouvement.py bornait le bloc << PROMPT DE MOUVEMENT >> avec $ "
     u"en mode multiligne -- ou $ marque la fin de CHAQUE ligne. Une simple "
     u"LIGNE VIDE terminait donc le prompt. Le prompt d'origine tenait en un "
     u"paragraphe, le defaut dormait ; la reecriture en trois paragraphes l'a "
     u"reveille. La simulation affichait un extrait tronque a 80 caracteres et "
     u"ne montrait rien. Vu en imprimant le texte complet : 287 caracteres au "
     u"lieu de 1 114 -- on payait pour la premiere phrase.",
     u"Avant toute depense, imprimer le prompt COMPLET tel que l'outil "
     u"l'enverra, et compter les caracteres. Une simulation dit ce qu'on va "
     u"payer, pas ce qu'on va envoyer."),

    (u"Une relecture croisee est un AVIS A VERIFIER, pas un verdict",
     u"22 sept. 2026",
     u"Plan 18, deux tours avec Jimmy. Il a trouve deux vrais defauts que "
     u"j'avais laisses -- le geste nomme (<< shrug >>) et la taille par "
     u"adjectif. Et il a propose deux fois des corrections FAUSSES, du meme "
     u"mecanisme : faire entrer le cycliste par un cote (verifie sur la prise : "
     u"il entre par le bas et ca se lit), et le mettre sur la bande cyclable "
     u"(il est sur l'asphalte ; sa correction supprimait le contraste qui fait "
     u"la chute).",
     u"Lui donner l'IMAGE, pas seulement sa description -- les deux erreurs "
     u"viennent de la. Et verifier chaque correction sur le fichier avant de "
     u"l'appliquer : ce qui se verifie se tranche, ce qui ne se verifie pas "
     u"reste un avis."),

    (u"Une depense refusee par le MONTAGE coute autant qu'une prise ratee",
     u"22 sept. 2026",
     u"Plan 18. monter_avatar.py taille chaque plan a min(clip ; amorce + "
     u"narration + queue). La narration fait 2,77 s : une prise de 7 s serait "
     u"revenue a 4,02 s, et les deux secondes du geste -- la raison meme de la "
     u"reprise -- seraient tombees sans erreur ni avertissement.",
     u"Avant de generer, calculer ce que le MONTAGE gardera. Si le plan raconte "
     u"apres la voix, lui donner sa queue dans _queues.txt, a cote des plans, "
     u"et s'assurer que le generateur lit le MEME fichier."),

    (u"Une reference transporte le VISAGE et la POSITION, pas le lieu",
     u"16 sept. 2026",
     u"Deux fois le meme mecanisme en une journee. cycliste-jaune fabrique "
     u"avec --ref mark-marche est sorti avec le visage de Mark, et il servait "
     u"de maitre a cinq plans. Puis deux-bandes, fabrique avec --ref "
     u"bande-rouge-pieds pour tenir la matiere, a garde les pieds sur le "
     u"rouge malgre un texte qui disait le contraire. Un prompt ne gagne "
     u"jamais contre une reference sur ce qu'elle MONTRE.",
     u"Si le plan change un visage ou une position, ne rien referencer qui "
     u"les porte. Le declarer dans A-TOURNER.txt -- << Visage neuf : oui >>, "
     u"<< Position neuve : oui >> -- et image_plan.py refuse alors. Pour tenir "
     u"le LIEU, referencer un decor vide, ou decrire."),

    (u"Demander une RETOUCHE, pas une composition",
     u"16 sept. 2026",
     u"Trois prompts d'affilee ont echoue a placer quelqu'un en nommant le "
     u"revetement sous ses pieds, et ils echouaient dans des directions "
     u"OPPOSEES : << BOTH ARE ON THE RED STRIP >> a donne le gris, << stands "
     u"on the grey pavement slabs >> a donne le rouge. Le modele ne desobeit "
     u"pas, il COMPOSE. Les plans 18 et 19 ont ete obtenus du premier coup en "
     u"changeant de registre.",
     u"Quand une image voisine porte deja la bonne position : << Take the "
     u"first reference photograph and change ONE thing in it... do not move "
     u"him, do not resize him, do not change what he is standing on >>, puis "
     u"nommer LA seule chose qui change. Et ancrer sur un objet physique -- "
     u"la bordure de granit entre lui et l'asphalte -- plutot que sur le nom "
     u"d'une surface."),

    (u"Une PROPORTION ne convoque rien : on peut la demander",
     u"16 sept. 2026",
     u"J'avais retire << filling two-thirds of the width >> en disant qu'une "
     u"contrainte inutile ne peut que couter. Faux : une proportion n'est pas "
     u"une negation, elle ne nomme aucun acteur. Ignoree elle coute zero ; "
     u"suivie elle a donne le plan 12 du premier coup.",
     u"Demander la proportion quand elle SERT (ici : un gris assez large pour "
     u"que deux pieds y tiennent). Ne pas compter dessus pour un partage "
     u"exact -- cinq mesures disent qu'elle n'est pas obeie au chiffre."),

    (u"Une ICONE normalisee se DESSINE, elle ne se demande pas",
     u"16 sept. 2026",
     u"Deux images perdues a demander l'Ampelmaennchen. Le prompt decrivait "
     u"le chapeau et les deux bras tendus ; le modele a boulonne un panneau "
     u"carre sur le mat. Le nom propre d'une icone convoque l'imagerie qui "
     u"l'entoure.",
     u"Demander l'objet NU (<< the upper round lens is lit and glows an even "
     u"plain red >>), puis incruster le dessin : video/ampelmann.py. Mieux "
     u"encore, --sa-lumiere DECOUPE la figure dans la lampe deja allumee, ce "
     u"qui garde la granulation, la couleur et le coeur surexpose de l'image."),

    (u"MESURER, et ETALONNER la mesure avant de s'en servir",
     u"16 sept. 2026",
     u"Le jaune du blouson : (210,212,52) contre (210,209,81), donc le gag "
     u"tient. Le rouge de la bande : six images a 27-30 % de saturation, deux "
     u"a 38-44 %, donc DEUX a reprendre et pas huit. Mais accorder_tenue.py, "
     u"premiere version, comparait des RGB absolus et declarait << ce n'est "
     u"plus la meme tenue >> entre deux images deja validees : il mesurait "
     u"l'EXPOSITION.",
     u"Une impression ne raccorde rien, un chiffre oui -- a condition de "
     u"l'etalonner sur des cas DEJA ACCEPTES avant de le laisser arbitrer. "
     u"Normaliser sur un neutre present partout (ici le gris des dalles)."),

    (u"RECADRER une prise payee plutot que d'en racheter une",
     u"16 sept. 2026",
     u"Le plan 15 de l'episode 2 sauve par un recadrage serre ; mark-marche "
     u"et cycliste-jaune ramenes au bon cadrage a cout nul. Ce qui n'est pas "
     u"dans l'image ne peut pas y apparaitre -- mais ce qui y est de trop "
     u"peut en sortir.",
     u"Avant de racheter, CALCULER si le recadrage suffit. Au plan 12 il ne "
     u"suffisait pas, et le calcul l'a dit : ramener la frontiere au centre "
     u"demandait de retirer 626 px pour une moitie rouge de 455, alors que le "
     u"pictogramme en mesure 857. Le calcul ferme la question, l'oeil non."),

    (u"La GEOGRAPHIE s'ecrit avant les plans",
     u"16 sept. 2026",
     u"Jacques : << comment ca qu'il se retrouve deja a un feu, alors qu'on le "
     u"voyait marcher sur la piste et qu'il n'y avait pas de feu a "
     u"proximite ? >> J'avais ecrit l'episode comme une SUITE DE PLANS : "
     u"chacun se defend seul, mis bout a bout ils ne decrivent aucun lieu.",
     u"Poser le lieu en tete du decoupage -- une seule rue, ce qu'il y a au "
     u"debut, au milieu, au bout -- et exiger que chaque image la serve. Ce "
     u"qu'on verra a la fin doit etre VISIBLE des le debut, au fond du cadre."),

    (u"Une COURBE s'ecrit comme une courbe, pas comme une suite d'etats",
     u"16 sept. 2026",
     u"Jacques : << il faudrait que le monsieur au manteau jaune devienne un "
     u"peu plus aimable au cours de route >>. La progression du cycliste "
     u"existait pourtant : agace (09), pedagogue (11), calme (13), pince-"
     u"sans-rire (15). Mais chaque prompt decrivait un ETAT SANS REFERENCE AU "
     u"PRECEDENT -- et quatre etats justes ne font pas une progression si "
     u"aucun ne se souvient d'ou il vient. Les plans sont fabriques "
     u"separement : rien ne relie deux prompts sauf ce qu'on y ecrit.",
     u"Ecrire chaque plan en fonction du precedent, et lui faire annoncer sa "
     u"propre place dans la courbe : << this is as hard as he will be : "
     u"everything after this softens >>, << the hardness has gone out of him "
     u"-- and it shows BEFORE he speaks >>. Et dire ce que le visage FAIT, pas "
     u"seulement ce qu'il ressent : la machoire qui se relache se filme, la "
     u"bienveillance non."),

    (u"La CAMERA se verrouille par un etat, pas par trois interdictions",
     u"16 sept. 2026",
     u"Le plus genant de la journee : la regle camera-qui-bouge de CE fichier "
     u"PRESCRIVAIT << Locked-off camera: no zoom, no push-in, no camera "
     u"movement of any kind >>. Trois negations, dans le fichier dont la "
     u"premiere regle explique que ces modeles fabriquent ce qu'on interdit. "
     u"Et la reprise du plan 09 a recadre en cours de plan. La queue disait de "
     u"meme << The framing itself NEVER changes >>.",
     u"<< The camera is locked on a tripod and stays there for the whole shot: "
     u"the same lens, the same height, the same distance. >> Et pour la queue : "
     u"<< The framing holds to the very end: in the last frame he is the same "
     u"size and in the same place in the picture as in the first. >> Relire "
     u"les REMEDES de ses propres regles avec l'oeil des regles voisines : "
     u"celui-ci se contredisait depuis l'episode 1."),

    (u"Les OBJETS aussi doivent raccorder, pas seulement les visages",
     u"16 sept. 2026",
     u"Le velo du cycliste change trois fois : noir avec phare avant dans "
     u"l'image maitresse et au plan 19, gris-argent avec porte-bagages au "
     u"plan 18. Personne n'avait regarde -- on surveillait les visages (les "
     u"deux Annas du 8 sept., le cycliste au visage de Mark), les lieux (le "
     u"decor qui se remeuble) et les vetements (accorder_tenue.py). Les "
     u"objets, jamais. Jacques : << ca ne choquera pas les gens, mais il faut "
     u"toujours verifier pour que les objets soient les memes >>.",
     u"Lister en tete du decoupage LES OBJETS QUI REVIENNENT -- le velo, le "
     u"blouson, le sac, la tasse -- et les verifier un par un sur les images "
     u"avant de tourner. La reference sert a ca : elle transporte un objet "
     u"comme elle transporte un visage, et c'est le seul cas ou cette force "
     u"joue POUR nous. Referencer l'image maitresse de l'objet, pas seulement "
     u"celle du personnage."),

    (u"L'INTENTION s'ecrit avant le prompt, et on fait relire",
     u"16 sept. 2026",
     u"Le plan 12 a brule cinq images parce que je defendais un partage 50/50 "
     u"que je n'avais jamais justifie. La question de Jacques -- << qu'est-ce "
     u"que tu cherches a faire exactement ? >> -- l'a defait en une phrase, et "
     u"a decouvert le vrai defaut : l'image illustrait << Rot fuer Raeder >> "
     u"et rien de << Grau fuer Menschen >>.",
     u"Ecrire l'intention (a quoi sert le plan, ce qui doit etre lisible sans "
     u"le son, ce qui s'ajoutera, ce qui a deja rate), puis le prompt EXACT, "
     u"puis faire relire par un autre modele -- avec les images. Voir "
     u"video/PROCEDURE-episode.md. La relecture du plan 12 a rapporte mieux "
     u"qu'un prompt : elle a montre que garde-negative ne connaissait que le "
     u"vocabulaire de l'episode 2, pas la structure d'une negation."),
]


# Les verbes qui font parler. Un prompt sans aucun d'eux decrit une pose, pas
# une replique -- et c'est la cause documentee des bouches qui bougent mal.
#
# ⚠️ SANS << he >> DEVANT. La premiere version exigeait << he asks >> et ratait
# << and asks again >> du plan 16 : le verbe etait la, la phrase coordonnee
# avait laisse tomber le sujet. Un controle qui accuse un prompt correct se
# fait desarmer au bout de deux fois.
VERBES_PAROLE = re.compile(
    r"(?i)\b(says|asks|answers|replies|greets|explains|tells|names|lists|"
    r"repeats|states|adds|offers|confirms|agrees|reads|speaking)\b")

# Le bloc d'apres-parole : ce qu'il fait pendant qu'il se tait. On le cherche
# dans SON paragraphe -- celui qui commence par << Finally >>.
APRES_PAROLE = re.compile(r"(?i)(blinks?|breathes?|listens?|waits?)")
PARA_FINAL = re.compile(r"(?ms)^Finally\b.*?(?=\n\s*\n|\Z)")
# Le paragraphe de decor de la garde positive : ce qu'il nomme EST dans l'image.
PARA_DECOR = re.compile(r"(?ms)^He is alone in the room\b.*?(?=\n\s*\n|\Z)")

# Les attenuateurs. Au-dela de six dans un prompt, le geste disparait.
ATTENUATEURS = re.compile(
    r"(?i)\b(small|slight(ly)?|gentl[ey]|subtle|barely|hardly|faint(ly)?|"
    r"a little|not broad|nothing broad|minimal|tiny)\b")

# Les negations, au sens du guide : ce que le modele doit se representer pour
# le refuser.
NEGATIONS = re.compile(r"(?i)\b(no|not|never|nobody|nothing|neither|without)\b")

# Les objets que le modele sait fabriquer si on les nomme sans dire ou ils sont.
#
# ⚠️ LE PLURIEL. La premiere version ecrivait \bdocument\b et ratait
# << two documents >> -- c'est-a-dire exactement le prompt qui a fait apparaitre
# la feuille. Un controle qui rate le cas qui l'a fait naitre ne sert a rien.
OBJETS = re.compile(r"(?i)\b(forms?|sheets?|papers?|documents?|leaflets?|"
                    r"cards?|passports?|stamps?|pens?|phones?|folders?)\b")
# Ce qui compte comme << j'ai dit ce que font les mains >>.
#
# ⚠️ << empty >> TOUT SEUL NE VEUT RIEN DIRE. La premiere version l'acceptait
# comme preuve qu'on avait decrit les mains -- et la garde positive contient
# << the room is quiet and empty >> et << an empty noticeboard >>. Le controle
# se declarait donc satisfait par une phrase qui parle du MUR. Le mot doit
# etre attache aux mains.
MAINS_DITES = re.compile(
    r"(?i)(hands?[^.]{0,60}(rest|stay|lie|remain|empty|open)"
    r"|(empty|open)[^.]{0,30}hands?"
    r"|holds? (it|the sheet|the form|it out)"
    r"|in his hands?|between finger)")

MARQUEURS = re.compile(r"(?im)^(first|then|next|after that|finally)\b")


# La phrase de camera verrouillee contient elle-meme les mots << zoom >> et
# << push-in >>, precedes de << no >>. Une regle qui cherche ces mots se declenche
# donc sur la consigne qu'elle est censee proteger : premier faux positif du
# controle, trouve en le lancant. On retire la phrase avant de chercher.
# ⚠️ ELLE NE SERT PLUS QU AUX ANCIENS PROMPTS. La phrase de camera est
#    desormais positive (voir le remede de camera-qui-bouge) et ne contient
#    plus de negation a retirer. On garde le retrait pour les episodes 1 et
#    2, dont les prompts portent encore l ancienne formule.
PHRASE_VERROU = re.compile(r"(?i)Locked-off camera:[^.]*\.")


# Les seules regles qui ont un sens sur un prompt d'IMAGE FIXE.
#
# ⚠️ NE PAS LEUR APPLIQUER TOUT LE JEU. Une image ne parle pas, ne dure pas et
#    n'a pas de queue de plan : << pas-de-verbe-de-parole >> et
#    << fin-sans-intention >> accuseraient CHAQUE prompt d'image, tous corrects.
#    Un controle qui accuse le juste se fait desarmer au bout de deux fois --
#    c'est deja ecrit plus haut a propos de << he asks >>, et ca vaut ici.
#
#    Ce qui reste est ce qui a reellement coute des images : la garde
#    negative, l'icone appelee par son nom, et l'empilement de negations.
POUR_IMAGE = ("garde-negative", "icone-nommee-par-son-nom",
              "negations-en-nombre", "qualificatifs-empiles",
              "taille-par-adjectif", "nom-du-geste", "repere-hors-champ",
              "sol-bord-a-bord", "corps-sans-contact")

# Se tenir sur une surface, et ou l'image coupe. Voir << corps-sans-contact >>.
POSE_SUR = re.compile(r"(?i)\b(stands?|standing|stood) on\b")
LIGNE_DE_COUPE = re.compile(
    r"(?i)(bottom edge of the picture|seen from the (waist|chest|hips?) up"
    r"|cropped? at the (waist|chest|hips?)|shoes?|feet|shadow)")

# Un prompt d'IMAGE ou de MOUVEMENT de decor : ni parole, ni queue de plan.
EST_IMAGE = re.compile(r"PROMPT\s+(?:D'IMAGE|DE\s+MOUVEMENT)", re.I)


def controler(texte, image=False):
    """Rend la liste des (code, gravite, titre, cout, remede, extrait).

    `image=True` restreint le jeu a POUR_IMAGE -- voir la note ci-dessus."""
    trouves = []
    sans_verrou = PHRASE_VERROU.sub(" ", texte)
    for code, gravite, motif, titre, cout, remede in REGLES:
        if image and code not in POUR_IMAGE:
            continue
        if code == "trop-de-temps":
            n = len(MARQUEURS.findall(texte))
            if n > 3:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d temps marques" % n))
            continue
        if code == "pas-de-verbe-de-parole":
            if not VERBES_PAROLE.search(texte):
                trouves.append((code, gravite, titre, cout, remede,
                                u"aucun de : says, asks, answers, greets..."))
            continue
        if code == "fin-sans-intention":
            # ⚠️ PREMIERE VERSION FAUSSE, ET INSTRUCTIVE : elle regardait le
            # dernier tiers du FICHIER. Or deux paragraphes de forme suivent la
            # queue du plan -- le decor et le cadrage -- donc le bloc
            # d'apres-parole n'y est jamais, et huit prompts corrects etaient
            # declares fautifs. On cherche le paragraphe lui-meme.
            para = PARA_FINAL.search(texte)
            if not para:
                trouves.append((code, gravite, titre, cout, remede,
                                u"aucun paragraphe de queue de plan"))
            elif len(APRES_PAROLE.findall(para.group(0))) < 2:
                trouves.append((code, gravite, titre, cout, remede,
                                u"la queue du plan ne dit pas ce qu'il fait"))
            continue
        if code == "qualificatifs-empiles":
            n = len(ATTENUATEURS.findall(texte))
            if n > 6:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d attenuateurs" % n))
            continue
        if code == "objet-qui-se-materialise":
            # Seulement quand les mains sont dans le cadre : un plan tete et
            # epaules n'a pas de mains a decrire.
            # ⚠️ ET ON NE COMPTE PAS LES OBJETS DU DECOR. La garde positive que
            # j'ai ecrite nomme << the date stamp >> -- un objet qui est DANS
            # l'image, donc sans danger. Sans cette exception, la regle se
            # declenchait sur sept prompts dont quatre deja tournes et bons :
            # un controle qui crie tout le temps ne se lit plus.
            utile = PARA_DECOR.sub(" ", texte)
            large = re.search(r"(?i)(medium shot|waist up)", texte)
            objet = OBJETS.search(utile)
            dit_les_mains = MAINS_DITES.search(texte)
            if large and objet and not dit_les_mains:
                trouves.append((code, gravite, titre, cout, remede,
                                u"<< %s >> nomme, et rien sur ce que tiennent "
                                u"les mains" % objet.group(0)))
            continue
        if code == "corps-sans-contact":
            # Le defaut est arrive sur une image, mais la question vaut pour
            # tout prompt qui plante quelqu'un sur une surface : ou coupe-t-on ?
            pose = POSE_SUR.search(texte)
            if pose and not LIGNE_DE_COUPE.search(texte):
                trouves.append((code, gravite, titre, cout, remede,
                                u"<< %s >>, et rien sur l'endroit ou l'image "
                                u"coupe" % pose.group(0)))
            continue
        if code == "negations-en-nombre":
            n = len(NEGATIONS.findall(sans_verrou))
            if n > 10:
                trouves.append((code, gravite, titre, cout, remede,
                                u"%d negations (le guide en demande le moins "
                                u"possible)" % n))
            continue
        ou = sans_verrou if code == "camera-qui-bouge" else texte
        m = re.search(motif, ou)
        if m:
            extrait = ou[max(0, m.start() - 40):m.end() + 40]
            extrait = " ".join(extrait.split())
            trouves.append((code, gravite, titre, cout, remede, extrait))
    return trouves


def dire(chemin, trouves, bavard=True):
    if not trouves:
        if bavard:
            print("  %-14s ok" % os.path.basename(chemin))
        return 0
    fautes = 0
    print("  %s" % os.path.basename(chemin))
    for code, gravite, titre, cout, remede, extrait in trouves:
        marque = "FAUTE" if gravite == "faute" else "doute"
        if gravite == "faute":
            fautes += 1
        print("    [%s] %s -- %s" % (marque, code, titre))
        print("           ... %s ..." % extrait[:110])
        print("           deja paye : %s" % cout)
        print("           a la place : %s" % remede)
    return fautes


def verifier_fichier(chemin, bavard=True):
    # ⚠️ TOUS LES PROMPTS NE SONT PAS DES PROMPTS D'AVATAR, et le controle
    #    l'ignorait. Un prompt d'IMAGE et un prompt de MOUVEMENT de decor
    #    n'ont ni parole ni queue de plan : leur reprocher l'absence de verbe
    #    de parole n'a aucun sens. Le 22 septembre 2026 il l'a fait trois fois
    #    de suite sur le plan 18 puis le plan 04 -- et un controle qu'on
    #    apprend a ignorer ne controle plus rien.
    #
    #    Le type se lit dans le fichier : << PROMPT D'IMAGE >> ou
    #    << PROMPT DE MOUVEMENT >>. Sans en-tete, on suppose l'avatar, qui
    #    reste le cas le plus frequent et le plus cher.
    texte = io.open(chemin, encoding="utf-8").read()
    return dire(chemin, controler(texte, image=EST_IMAGE.search(texte) is not None),
                bavard)


def verifier_scene(scene, bavard=True):
    d = os.path.join(RACINE, "video", "episode-%s" % scene,
                     "_essai-avatar", "prompts")
    fichiers = sorted(glob.glob(os.path.join(d, "plan*.txt")))
    if not fichiers:
        sys.exit("  aucun prompt dans %s" % d)
    return sum(verifier_fichier(f, bavard) for f in fichiers)


def lecons():
    """Tout ce qu'on a appris, a relire AVANT d'ecrire un prompt.

    Demande de Jacques le 16 septembre 2026 : << j'aimerais qu'on passe a
    travers tout, tout ce qu'on a appris avant meme de decrire un nouveau
    prompt >>, et << je veux que cette experience-la continue a se construire >>.

    ⚠️ CE QUI FAIT VIVRE CETTE LISTE. Chaque prise refusee doit produire soit
    une regle de plus ici, soit une phrase qui dit pourquoi elle n'est pas
    mecanisable. Une prise refusee qui ne laisse rien derriere elle sera
    repayee -- c'est deja arrive quatre fois le 16 septembre, sur des lecons
    qui etaient ecrites ailleurs et que personne ne relisait.
    """
    print()
    print("  CE QU'ON A DEJA PAYE -- a relire avant d'ecrire un prompt")
    print("  " + "-" * 66)
    for code, gravite, _motif, titre, cout, remede in REGLES:
        print()
        print("  [%s] %s" % ("refus " if gravite == "faute" else "doute ", code))
        print("     %s" % titre)
        print("     deja paye  : %s" % cout)
        print("     a la place : %s" % remede)
    print()
    print("  %d regles. Une prise refusee doit en laisser une de plus." % len(REGLES))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("fichier", nargs="?")
    p.add_argument("--scene")
    p.add_argument("--avant-episode", action="store_true",
                   dest="avant_episode",
                   help="LA REVUE COMPLETE -- fautes ET acquis. A passer "
                        "avant d'ouvrir un nouvel episode.")
    p.add_argument("--lecons", action="store_true",
                   help="tout ce qu'on a appris, a relire avant d'ecrire")
    a = p.parse_args()
    if a.avant_episode:
        print("=" * 74)
        print("  LA REVUE D'AVANT-EPISODE")
        print("=" * 74)
        print(u"""
  Regle posee par Jacques le 16 septembre 2026 :

      << Il faut construire cette connaissance-la pour qu'on puisse avancer
      avec plus de confiance pour les prochains episodes. Que ce soit ajoute
      a chaque fois qu'on corrige quelque chose qui tient la route, puis
      qu'on revalide l'ensemble avant de recreer un autre episode. >>

  Deux listes, et il faut les deux. Les FAUTES empechent de refaire ; les
  ACQUIS apprennent a faire. Un projet qui ne tient que la premiere
  redecouvre ses solutions a chaque fois, et les paie a chaque fois.
""")
        print("-" * 74)
        print("  CE QUI MARCHE -- %d acquis" % len(ACQUIS))
        print("-" * 74)
        for titre, date, etabli, usage in ACQUIS:
            print(u"\n  \u2713 %s\n    (%s)" % (titre, date))
            print(u"    etabli par : %s" % etabli)
            print(u"    a faire    : %s" % usage)
        print()
        print("-" * 74)
        print("  CE QU'ON A DEJA PAYE -- %d fautes" % len(REGLES))
        print("-" * 74)
        lecons()
        print("=" * 74)
        print(u"""  ET CE QUI N'EST PAS DANS CE FICHIER, PARCE QU'IL NE SAIT PAS LE LIRE :

    - l'INTENTION s'ecrit avant le prompt, et un autre modele la relit,
      avec les images. video/PROCEDURE-episode.md.
    - la GEOGRAPHIE de l'episode s'ecrit avant les plans.
    - --montrer est gratuit : le lire AVANT chaque depense.
    - une prise payee ne s'ecrase jamais a la main ; --refaire l'archive.
""")
        print("=" * 74)
        return

    if a.lecons:
        lecons()
        return
    if a.scene:
        fautes = verifier_scene(a.scene)
    elif a.fichier:
        fautes = verifier_fichier(a.fichier)
    else:
        sys.exit("  Preciser un fichier ou --scene NOM.")
    print()
    if fautes:
        print("  %d faute(s) connue(s). Elles ont deja coute une prise chacune." % fautes)
        sys.exit(1)
    print("  aucune faute connue. (Ce qui ne veut pas dire que le prompt est bon.)")


if __name__ == "__main__":
    main()
