# -*- coding: utf-8 -*-
"""LES ETAPES DE L'A2 AU C1, ET LES LIGNES « TU SAIS... » (6 nov. 2026).

Jacques, 5 nov. : « Je me demande si on ne devrait pas ajouter les etapes pour
B1, B2 et C1. Puis je pense qu'il faudrait avoir quelque chose de special qui
arrive lorsqu'on a passe un groupe d'etapes. » ; 6 nov. : « Vas-y pour les
recommandations » (maquette https://claude.ai/artifact/3rpgyL13GfJuUwN3qVaG9Z).

Ce fichier est la SOURCE. Il porte :
  - la structure : groupes, etapes, et ce que chaque etape reprend de l'app
    (themes de vocabulaire, feuilles de conjugaison, scenes, themes illustres,
    series d'exercices, fiches ou tuiles de grammaire, parties d'examen) --
    uniquement des identifiants qui existent deja ;
  - le texte FRANCAIS : le nom de chaque groupe, le titre de chaque etape, et la
    ligne « Tu sais... » de chaque etape (A2-C1), de chaque etape de Premiers pas
    et de l'A1, et de chaque repere.

La ligne « Tu sais... » est un groupe a l'infinitif, a la 2e personne du
singulier (« te presenter », « ton chemin »). Elle doit se lire apres les deux
amorces de l'app : « Tu sais maintenant... » et « Cette semaine, tu as appris
a... ». Elle dit une situation de la vraie vie, jamais un point de grammaire.

Les traductions vivent dans etapes/traductions/<appr>/<langue>.json, une cle par
texte (cles listees par python tests/etapes_construire.py --a-traduire).
Construire : python tests/etapes_construire.py
Controler  : python tests/etapes.py
"""

# Les langues d'interface, par langue apprise (celles de a1-voyage.json).
LANGUES = {
    "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"],
    "es": ["fr", "en", "pt", "ar", "de"],
}

# ---------------------------------------------------------------------------
# Les lignes « Tu sais... » de ce qui existe deja.
# Premiers pas : par rang d'etape (premiers-pas.json n'a pas d'id).
# ---------------------------------------------------------------------------
PREMIERS_PAS = {
    "de": ["saluer et te présenter", "commander et payer au café", "demander ton chemin en ville",
           "acheter un billet de train", "réserver une chambre d'hôtel", "demander un prix et une taille",
           "appeler à l'aide", "faire répéter et dire l'heure"],
    "es": ["saluer et te présenter", "commander et payer au café", "demander ton chemin en ville",
           "acheter un billet de train", "réserver une chambre d'hôtel", "demander un prix et une taille",
           "appeler à l'aide", "faire répéter et dire l'heure"],
}

# A1 : par id d'escale ou d'etape (a1-voyage.json, escales + installe + suite).
A1 = {
    "de": {
        "arriver": "t'installer à l'hôtel",
        "manger": "commander au restaurant",
        "marche": "acheter au marché et à la boulangerie",
        "ville": "trouver ton chemin en ville",
        "train": "prendre le train",
        "achats": "essayer et acheter des vêtements",
        "sante": "dire où tu as mal",
        "imprevus": "signaler une perte ou un vol",
        "poste": "envoyer un colis et laver ton linge",
        "rencontrer": "te présenter et parler de toi",
        "plage": "parler de la météo",
        "visiter": "acheter des billets pour un musée",
        "logement": "chercher un logement",
        "buergeramt": "faire tes démarches à la mairie",
        "famille": "parler de ta famille",
        "maison": "décrire ton logement",
        "cuisine": "parler de ce que tu manges",
        "travail": "dire quel métier tu fais",
        "ecole": "parler de tes études et de ton emploi du temps",
        "loisirs": "parler de tes loisirs",
        "corps": "parler du corps, de la nature et des animaux",
        "societe": "te repérer en ville et parler d'argent",
    },
    "es": {
        "arriver": "t'installer à l'hôtel",
        "manger": "commander au restaurant",
        "marche": "acheter au marché et à la boulangerie",
        "ville": "trouver ton chemin en ville",
        "train": "prendre le train ou le car",
        "achats": "essayer et acheter des vêtements",
        "sante": "dire où tu as mal",
        "imprevus": "signaler une perte ou un vol",
        "poste": "envoyer un colis et laver ton linge",
        "rencontrer": "te présenter et parler de toi",
        "plage": "parler de la météo",
        "visiter": "acheter des billets pour un musée",
        "logement": "chercher un logement et parler aux voisins",
        "buergeramt": "faire tes démarches et prendre rendez-vous",
        "familia": "parler de ta famille",
        "casa": "raconter ta journée à la maison",
        "cocina": "parler de cuisine et de ce que tu manges",
        "trabajo": "parler de ton travail",
        "escuela": "parler de tes études",
        "ocio": "parler de tes loisirs et de tes vêtements",
        "cuerpo": "parler du corps, des animaux et du temps qu'il fait",
        "sociedad": "te repérer en ville, compter et dire l'heure",
    },
}

# Reperes : par id (reperes.json, espanol/datos/reperes.json).
REPERES = {
    "de": {
        "n0-20": "compter jusqu'à 20",
        "n20-100": "compter jusqu'à 100",
        "n100-1000": "compter jusqu'à 1000",
        "jours": "dire les jours de la semaine",
        "couleurs": "nommer les couleurs",
        "mois": "dire les mois de l'année",
        "alphabet": "épeler ton nom",
        "genre-die": "reconnaître un nom féminin à sa terminaison",
        "genre-der": "reconnaître un nom masculin à sa terminaison",
        "genre-das": "reconnaître un nom neutre à sa terminaison",
        "pluriel": "mettre un nom au pluriel",
    },
    "es": {
        "n0-20": "compter jusqu'à 20",
        "n20-100": "compter jusqu'à 100",
        "n100-1000": "compter jusqu'à 1000",
        "jours": "dire les jours de la semaine",
        "couleurs": "nommer les couleurs",
        "mois": "dire les mois de l'année",
        "alphabet": "épeler ton nom",
        "genre-m": "reconnaître un nom masculin à sa terminaison",
        "genre-f": "reconnaître un nom féminin à sa terminaison",
        "pluriel": "mettre un nom au pluriel",
    },
}

# ---------------------------------------------------------------------------
# Les groupes et les etapes de l'A2 au C1.
#   id        unique dans la langue apprise (l'etat de la personne le garde)
#   nom       le nom du groupe (francais), a la premiere personne
#   examen    pour un groupe examen : les examens vises (affiche tel quel)
#   etapes    t (titre), sais (« Tu sais... »), icone, et ce que l'etape reprend :
#             themes (themes.json / temas.json), feuilles (conjugaison.json),
#             scenes (visuel/prototype/scene-<nom>.js), illustres (cles de
#             THEMES_ILLUSTRES), series (cles de exercices.json / ejercicios.json),
#             tuiles (allemand : data-orbid des tuiles de grammaire), fiches
#             (espagnol : id des fiches de grammaire.json), pruefung (examen :
#             partie de pruefung.json, niveau, et les « teil » ou « typ » retenus).
# Chaque feuille de conjugaison sert une fois ; chaque theme A2-C1 une fois.
# Les groupes examen sans contenu (B2 allemand, DELE) n'existent pas ici : ils
# n'apparaitront qu'avec leur contenu (decision du 6 nov., voir DECISIONS.md).
# ---------------------------------------------------------------------------
def E(id, icone, t, sais, **reprend):
    return dict(id=id, icone=icone, t=t, sais=sais, **reprend)

GROUPES = {"de": {}, "es": {}}

GROUPES["de"]["A2"] = [
    {"id": "a2-raconter", "nom": "Raconter ma vie", "etapes": [
        E("a2-journee", "🗓️", "Ma journée d'hier", "raconter ta journée d'hier",
          feuilles=["raconter_journee", "perfekt_haben"], themes=["zeit_kalender_a2", "grundwortschatz_a2"],
          illustres=["journee"], scenes=["schlafzimmer", "kueche"], series=["perfektExercises"]),
        E("a2-weekend", "🎸", "Mon week-end, mes sorties", "raconter ton week-end et tes sorties",
          feuilles=["perfekt_sein"], themes=["freizeit_hobbys_a2", "sport_a2", "musik_kunst_a2"],
          illustres=["loisirs"], scenes=["musik", "sportplatz"], series=["wortstellungV2Exercises"], tuiles=["wortstellung"]),
        E("a2-vacances", "🏖️", "Mes vacances", "raconter tes vacances",
          feuilles=["participes_forts"], themes=["reisen_urlaub_a2", "wetter_a2", "natur_a2", "umwelt_a2"],
          illustres=["meteo"], scenes=["strand", "camping"], series=["praepWoWohinExercises"], tuiles=["praep"]),
        E("a2-enfance", "🧒", "Quand j'étais petit", "dire comment c'était quand tu étais petit",
          feuilles=["war_hatte", "modaux_passe"], themes=["schule_a2", "universitaet_a2", "tiere_a2"],
          illustres=["animales"], scenes=["klassenzimmer", "bauernhof"], series=["wortstellungSubExercises"], tuiles=["konjunktionen"]),
        E("a2-famille", "👨‍👩‍👧", "Ma famille, ce que je ressens", "parler de ta famille et de ce que tu ressens",
          feuilles=["reflechis_passe"], themes=["familie_a2", "gefuehle_charakter_a2", "feste_feiertage_a2"],
          illustres=["familia", "emociones"], scenes=["familie", "geburtstag"], series=["possessivExercises"], tuiles=["possessiv"]),
        E("a2-decrire", "🧥", "Décrire quelqu'un", "décrire quelqu'un",
          feuilles=["werden_devenir"], themes=["kleidung_a2", "koerperteile_a2", "farben_formen_a2"],
          illustres=["descripcion", "ropa", "contrarios"], scenes=["kleidergeschaeft"], series=["adjektiveDeklinationExercises"]),
    ]},
    {"id": "a2-place", "nom": "Me faire ma place", "etapes": [
        E("a2-logement", "🏠", "Trouver un logement", "chercher un appartement et emménager",
          feuilles=["separables"], themes=["wohnen_a2", "moebel_haushalt_a2"],
          illustres=["logement"], scenes=["umzug", "wohnzimmer"], series=["praepReconnaissanceExercises"]),
        E("a2-travail", "💼", "Au travail", "parler de ton travail et de tes horaires",
          feuilles=["separables_places", "sans_ge"], themes=["arbeit_buero_a2", "berufe_a2"],
          illustres=["metiers"], scenes=["buero"], series=["wortstellungNichtExercises"]),
        E("a2-medecin", "🩺", "Chez le médecin", "expliquer au médecin ce que tu as",
          feuilles=["imperatif"], themes=["gesundheit_a2"],
          illustres=["cuerpo"], scenes=["arztpraxis", "apotheke"], series=["kasusReconnaissanceExercises"], tuiles=["kasus"]),
        E("a2-demarches", "🏛️", "Démarches et rendez-vous", "prendre rendez-vous et remplir un formulaire",
          themes=["politik_gesellschaft_a2", "zahlen_mengen_a2"],
          illustres=["demarches"], scenes=["buergeramt", "post"], series=["wennObExercises", "wortstellungFrageExercises"]),
        E("a2-achats", "🛒", "Acheter, échanger, réclamer", "acheter, échanger ou rapporter un article",
          themes=["einkaufen_geld_a2", "essen_trinken_a2", "obst_gemuese_a2", "kueche_kochen_a2"],
          illustres=["courses", "manger"], scenes=["supermarkt", "markt-gemuese-frucht"], series=["derEinExercises"]),
        E("a2-deplacer", "🚇", "Me repérer, me déplacer", "te repérer et te déplacer en ville",
          themes=["verkehr_a2", "stadt_gebaeude_a2", "medien_technologie_a2"],
          illustres=["transportes", "gato"], scenes=["kreuzung", "ubahn", "zug"], series=["positionsverbenExercises"]),
    ]},
    {"id": "a2-examen", "nom": "Réussir mon A2", "examen": "Goethe A2 · telc A2·B1", "etapes": [
        E("a2-ex-ecouter", "🎧", "Écouter", "comprendre de courts messages entendus", pruefung={"partie": "hoeren", "niveau": "A2"}),
        E("a2-ex-lire", "📖", "Lire", "lire une annonce, un horaire, un mode d'emploi", pruefung={"partie": "lesen", "niveau": "A2"}),
        E("a2-ex-ecrire", "✉️", "Écrire", "écrire un message, un courriel ou une lettre simple", pruefung={"partie": "schreiben", "niveau": "A2"}),
        E("a2-ex-parler", "🗣️", "Parler", "parler de toi et poser des questions", pruefung={"partie": "sprechen", "niveau": "A2"}),
    ]},
]

GROUPES["de"]["B1"] = [
    {"id": "b1-travailler", "nom": "Travailler en allemand", "etapes": [
        E("b1-emploi", "📰", "Chercher un emploi", "chercher un emploi et répondre à une annonce",
          feuilles=["k2_poli"], themes=["berufe_b1", "vhs_kapitel9_b1"], illustres=["metiers"], scenes=["buero"]),
        E("b1-entretien", "🤝", "L'entretien d'embauche", "passer un entretien d'embauche",
          feuilles=["k2_formes"], themes=["vhs_kapitel12_b1", "kleidung_b1", "grundwortschatz_b1"], scenes=["buero"],
          series=["weilObwohlExercises"]),
        E("b1-bureau", "🖥️", "Au bureau", "expliquer comment les choses se font au bureau",
          feuilles=["passif_present"], themes=["arbeit_buero_b1"], scenes=["buero", "bibliothek"],
          series=["zuInfinitivExercises"], tuiles=["zuinfinitiv"]),
        E("b1-collegues", "💬", "Collègues et désaccords", "dire poliment que tu n'es pas d'accord",
          feuilles=["verbes_preposition"], themes=["gefuehle_charakter_b1", "vhs_kapitel4_b1"], illustres=["emociones"],
          series=["verbenMitPraepExercises", "partikelnNuanceExercises"], tuiles=["partikeln"]),
        E("b1-argent", "🏦", "Argent, contrats, assurances", "parler d'argent, de contrats et d'assurances",
          feuilles=["lassen"], themes=["einkaufen_geld_b1", "vhs_kapitel2_b1", "vhs_kapitel3_b1"], illustres=["demarches"],
          scenes=["buergeramt", "post"]),
        E("b1-projets", "🎓", "Me former, mes projets", "parler de ta formation et de tes projets",
          feuilles=["futur"], themes=["schule_b1", "universitaet_b1", "vhs_kapitel11_b1"], scenes=["klassenzimmer", "bibliothek"],
          series=["deshalbTrotzdemExercises"]),
    ]},
    {"id": "b1-avis", "nom": "Donner mon avis", "etapes": [
        E("b1-histoire", "📚", "Lire une histoire", "lire et raconter une histoire au passé",
          feuilles=["praet_faible", "praet_fort"], themes=["musik_kunst_b1", "freizeit_hobbys_b1", "sport_b1", "reisen_urlaub_b1", "vhs_kapitel8_b1", "vhs_kapitel10_b1"],
          illustres=["loisirs"], scenes=["museum", "musik"], series=["alsWennExercises", "praeteritumExercises"]),
        E("b1-souvenirs", "🕰️", "Fêtes, repas, souvenirs", "raconter un souvenir, une fête, un repas",
          feuilles=["praet_familles", "praet_mixte", "plusquamperfekt"],
          themes=["familie_b1", "feste_feiertage_b1", "zeit_kalender_b1", "essen_trinken_b1", "kueche_kochen_b1", "obst_gemuese_b1", "vhs_kapitel5_b1"],
          illustres=["familia", "manger"], scenes=["familie", "geburtstag"], series=["blocsConnecteursExercises"]),
        E("b1-sante", "🩺", "Santé et soins", "parler de santé et de soins",
          themes=["gesundheit_b1", "koerperteile_b1", "vhs_kapitel6_b1"], illustres=["cuerpo"], scenes=["arztpraxis", "untersuchung"],
          series=["relativReconNomAkk"], tuiles=["relativ"]),
        E("b1-environnement", "🌱", "L'environnement", "dire ce qu'on devrait faire pour l'environnement",
          feuilles=["k2_modaux"], themes=["umwelt_b1", "natur_b1", "tiere_b1", "wetter_b1", "vhs_kapitel7_b1"],
          illustres=["animales", "meteo"], scenes=["bauernhof", "park"], series=["obwohlTrotzdemExercises", "konjunktiv2Exercises"]),
        E("b1-medias", "📱", "Médias et opinions", "donner ton avis sur les médias",
          themes=["medien_technologie_b1", "farben_formen_b1", "zahlen_mengen_b1"],
          series=["relativReconDativ", "aberSondernExercises"]),
        E("b1-societe", "🏙️", "Ma ville, ma société", "parler de ta ville et de la société",
          themes=["politik_gesellschaft_b1", "stadt_gebaeude_b1", "verkehr_b1", "wohnen_b1", "moebel_haushalt_b1",
                  "vhs_kapitel1_b1", "vhs_kapitel13_b1", "vhs_kapitel14_b1", "vhs_kapitel15_b1", "vhs_kapitel16_b1"],
          illustres=["transportes", "logement"], scenes=["stadtplatz", "kreuzung"], series=["relativGenitivReconnaissanceExercises"]),
    ]},
    {"id": "b1-examen", "nom": "Réussir mon B1", "examen": "DTZ · telc · Goethe B1", "etapes": [
        E("b1-ex-hoeren", "🎧", "Écouter", "comprendre des annonces, des messages et des conversations",
          pruefung={"partie": "hoeren", "niveau": "B1"}),
        E("b1-ex-lesen", "📖", "Lire", "lire une lettre de l'administration ou un article",
          pruefung={"partie": "lesen", "niveau": "B1"}),
        E("b1-ex-schreiben", "✉️", "Écrire", "écrire une lettre formelle",
          pruefung={"partie": "schreiben", "niveau": "B1"}),
        E("b1-ex-sprechen", "🗣️", "Parler de toi", "te présenter et raconter une expérience",
          pruefung={"partie": "sprechen", "niveau": "B1", "teil": ["Teil 2 · Über Erfahrungen sprechen"]}),
        E("b1-ex-planen", "🧩", "Planifier ensemble", "organiser quelque chose avec quelqu'un",
          pruefung={"partie": "sprechen", "niveau": "B1", "teil": ["Teil 3 · Gemeinsam planen"]}),
        E("b1-ex-praesentieren", "📊", "Présenter un thème (Goethe)", "présenter un thème et répondre aux questions",
          pruefung={"partie": "sprechen", "niveau": "B1", "teil": ["Teil 2 · Ein Thema präsentieren", "Teil 3 · Über eine Präsentation sprechen"]}),
    ]},
]

GROUPES["de"]["B2"] = [
    {"id": "b2-egal", "nom": "Discuter d'égal à égal", "etapes": [
        E("b2-aurait", "💭", "Ce qui aurait pu être", "dire ce qui aurait pu se passer",
          feuilles=["k2_passe"], themes=["gefuehle_charakter_b2", "familie_b2", "feste_feiertage_b2"], illustres=["emociones"],
          series=["konjunktiv2VergangenheitExercises"]),
        E("b2-reproche", "😬", "« Tu aurais dû »", "dire ce que quelqu'un aurait dû faire",
          feuilles=["double_infinitif"], themes=["freizeit_hobbys_b2", "sport_b2", "reisen_urlaub_b2"]),
        E("b2-soutenu", "🎩", "Parler soutenu", "parler dans un registre soutenu",
          feuilles=["k2_forts"], themes=["musik_kunst_b2", "schule_b2", "universitaet_b2"], scenes=["museum"],
          series=["adverbienNuanceExercises"], tuiles=["adverbien"]),
        E("b2-debattre", "⚖️", "Débattre", "débattre et défendre ton point de vue",
          feuilles=["verbes_prep_b2"], themes=["politik_gesellschaft_b2", "grundwortschatz_b2"],
          series=["transformationConnecteursExercises", "konjunktionenNuanceExercises"]),
        E("b2-precis", "🔎", "Décrire avec précision", "décrire un objet ou un lieu avec précision",
          feuilles=["participe_adjectif"], themes=["wohnen_b2", "moebel_haushalt_b2", "kleidung_b2", "farben_formen_b2", "stadt_gebaeude_b2"],
          illustres=["descripcion", "contrarios"], series=["partizipExercises"]),
    ]},
    {"id": "b2-actualite", "nom": "Comprendre l'actualité", "etapes": [
        E("b2-article", "📰", "Lire un article", "comprendre un article de journal",
          feuilles=["passif_temps"], themes=["medien_technologie_b2", "zeit_kalender_b2"], series=["passivExercises"]),
        E("b2-regles", "🛠️", "Règles et consignes", "comprendre des règles et des consignes",
          feuilles=["passif_modal"], themes=["arbeit_buero_b2", "berufe_b2", "verkehr_b2"], scenes=["buero"]),
        E("b2-etat", "🔒", "Ouvert ou fermé : l'état", "dire dans quel état est une chose : ouverte, fermée, réparée",
          feuilles=["passif_etat"], themes=["einkaufen_geld_b2", "essen_trinken_b2", "kueche_kochen_b2", "obst_gemuese_b2"],
          illustres=["courses"], scenes=["supermarkt"]),
        E("b2-sanspassif", "🌍", "Dire sans passif", "dire la même chose sans passif",
          feuilles=["passif_ersatz"], themes=["umwelt_b2", "natur_b2", "wetter_b2", "tiere_b2"], scenes=["park"]),
        E("b2-science", "🧬", "Science et santé", "parler de science et de santé",
          feuilles=["werden_emplois"], themes=["gesundheit_b2", "koerperteile_b2", "zahlen_mengen_b2"], illustres=["cuerpo"],
          scenes=["untersuchung"], series=["werdenExercises"]),
    ]},
]

GROUPES["de"]["C1"] = [
    {"id": "c1-idees", "nom": "Défendre mes idées", "etapes": [
        E("c1-rapporter", "🗞️", "« D'après lui… »", "rapporter ce que quelqu'un a dit",
          feuilles=["k1"], themes=["sprache_kommunikation_c1", "bildung_medien_c1", "medien_technologie_c1"],
          series=["konjunktiv1Exercises"]),
        E("c1-ersatz", "🔁", "Quand le Konjunktiv I ne se voit pas", "rapporter des paroles sans ambiguïté",
          feuilles=["k1_ersatz"], themes=["denken_wahrnehmung_c1", "ursache_wirkung_c1"]),
        E("c1-tribunal", "⚖️", "Témoins et tribunal", "rapporter un témoignage, une question, un ordre",
          feuilles=["k1_passe", "k1_questions"], themes=["recht_justiz_c1", "polizei_verfahren_c1", "sicherheit_krisen_c1"]),
        E("c1-supposer", "🤔", "Supposer, conclure", "faire des suppositions et conclure",
          feuilles=["futur2"], themes=["argumentation_c1", "konflikt_verhandlung_c1", "ethik_werte_c1", "glaube_sinn_c1"],
          series=["konnektorenExercises"]),
    ]},
    {"id": "c1-ecrit", "nom": "Maîtriser l'allemand écrit", "etapes": [
        E("c1-administration", "🏢", "L'allemand des administrations", "comprendre l'allemand des administrations",
          feuilles=["passif_passe_modal"],
          themes=["wirtschaft_verwaltung_c1", "versicherung_c1", "dienstleistung_c1", "logistik_versand_c1", "konsum_handel_c1", "einkaufen_geld_c1"],
          illustres=["demarches"], scenes=["buergeramt"]),
        E("c1-participe", "📜", "Le participe étendu", "lire des phrases longues et denses",
          feuilles=["participe_etendu"], themes=["gesellschaft_wandel_c1", "geschichte_erinnerung_c1", "politik_gesellschaft_c1", "alter_abschied_c1"]),
        E("c1-style", "🧱", "Verbe + nom : le style écrit", "écrire dans un style soutenu",
          feuilles=["fvg"], themes=["arbeit_buero_c1", "universitaet_c1", "schule_c1", "erziehung_kindheit_c1", "pflege_betreuung_c1"],
          series=["funktionsverbExercises"]),
        E("c1-arts", "🎭", "Arts, nature, campagne", "parler d'art et de nature avec précision",
          themes=["technik_kunst_c1", "buehne_text_c1", "musik_kunst_c1", "bild_aufnahme_c1", "natur_c1", "umwelt_c1",
                  "landwirtschaft_c1", "garten_pflanzen_c1", "meer_kueste_c1", "tiere_c1", "wetter_c1"]),
        E("c1-quotidien", "🏡", "Le quotidien, en finesse", "parler de la vie de tous les jours avec finesse",
          themes=["gesundheit_c1", "koerperteile_c1", "wohnen_c1", "heimwerken_c1", "handwerk_material_c1", "kueche_kochen_c1",
                  "kleidung_c1", "sport_c1", "reisen_urlaub_c1", "verkehr_c1", "stadt_gebaeude_c1", "familie_c1",
                  "gefuehle_charakter_c1", "lebensfuehrung_c1", "vereinsleben_c1"],
          scenes=["heimwerken"], series=["premierePlaceExercises"]),
    ]},
    {"id": "c1-examen", "nom": "Réussir mon C1", "examen": "Goethe C1 · telc C1", "etapes": [
        E("c1-ex-ecouter", "🎧", "Écouter", "comprendre une conférence ou un débat", pruefung={"partie": "hoeren", "niveau": "C1"}),
        E("c1-ex-lire", "📖", "Lire", "lire un commentaire ou un texte documentaire", pruefung={"partie": "lesen", "niveau": "C1"}),
        E("c1-ex-ecrire", "✍️", "Écrire", "écrire une argumentation", pruefung={"partie": "schreiben", "niveau": "C1"}),
        E("c1-ex-parler", "🎤", "Parler", "faire un exposé et en discuter", pruefung={"partie": "sprechen", "niveau": "C1"}),
    ]},
]

GROUPES["es"]["A2"] = [
    {"id": "a2-raconter", "nom": "Raconter ma vie", "etapes": [
        E("a2-hoy", "🗓️", "Ce que j'ai fait aujourd'hui", "raconter ce que tu as fait aujourd'hui",
          feuilles=["perfecto"], themes=["las_tareas", "la_comunicacion", "los_movimientos"], illustres=["journee"],
          scenes=["schlafzimmer", "kueche"], fiches=["pasados"]),
        E("a2-vacaciones", "🏖️", "Mes vacances", "raconter tes vacances",
          feuilles=["preterito_regular", "preterito_ser_ir"], themes=["el_viaje", "las_vacaciones", "el_hotel", "el_aeropuerto"],
          illustres=["meteo", "transportes"], scenes=["strand", "flughafen", "hotel"], series=["preposicionesViajeExercises"]),
        E("a2-pasado", "😮", "Ce qui s'est passé", "raconter ce qui s'est passé",
          feuilles=["preterito_irregulier"], themes=["los_problemas", "la_seguridad"], scenes=["zug", "hotel"],
          fiches=["preposiciones"], series=["preposicionesExercises"]),
        E("a2-infancia", "🧒", "Quand j'étais petit", "dire comment c'était quand tu étais petit",
          feuilles=["imperfecto", "imperfecto_irregulier"], themes=["las_etapas", "la_familia_extensa", "los_estudios"],
          illustres=["familia"], scenes=["familie", "klassenzimmer"], fiches=["demostrativos-posesivos"], series=["demostrativosExercises"]),
        E("a2-decorado", "🎭", "Le décor et l'action", "raconter une histoire, avec le décor et l'action",
          feuilles=["preterito_ou_imperfecto"],
          themes=["las_emociones", "las_relaciones", "el_aspecto", "la_personalidad", "las_fiestas", "vhs_kapitel1_b1"],
          illustres=["emociones", "descripcion"], scenes=["geburtstag"], fiches=["ser-estar"], series=["serEstarExercises"]),
    ]},
    {"id": "a2-place", "nom": "Me faire ma place", "etapes": [
        E("a2-vivienda", "🏠", "Le logement", "décrire ton logement et ce que tu es en train de faire",
          feuilles=["estar_gerundio"], themes=["la_vivienda", "nom_casa", "las_herramientas", "los_materiales"],
          illustres=["logement"], scenes=["umzug", "wohnzimmer"], fiches=["hay-preguntas"]),
        E("a2-trabajo", "💼", "Le travail, mes projets", "parler de ton travail et de tes projets",
          feuilles=["ir_a"], themes=["la_oficina", "la_tecnologia", "los_medios"], illustres=["metiers"], scenes=["buero"],
          fiches=["perifrasis"], series=["perifrasisExercises"]),
        E("a2-medico", "🩺", "Chez le médecin", "expliquer au médecin ce que tu as",
          feuilles=["imperativo"], themes=["la_salud", "partes_del_cuerpo", "el_bienestar"], illustres=["cuerpo"],
          scenes=["arztpraxis", "apotheke"], fiches=["pronombres"], series=["imperativoExercises"]),
        E("a2-servicios", "🏛️", "Services et démarches", "te débrouiller au guichet et dans les démarches",
          themes=["los_servicios", "orientarse", "el_dinero", "la_cantidad"], illustres=["demarches"],
          scenes=["buergeramt", "post", "kreuzung"], fiches=["por-para"], series=["porParaExercises"]),
        E("a2-compras", "🛍️", "Acheter, cuisiner, sortir", "acheter, cuisiner et sortir",
          themes=["la_cocina_a2", "las_frutas", "las_verduras", "la_moda", "el_cine", "la_musica", "el_arte", "el_deporte",
                  "la_naturaleza", "el_medioambiente"],
          illustres=["courses", "manger", "loisirs"], scenes=["supermarkt", "markt-gemuese-frucht"], series=["gustarExercises"]),
    ]},
]

GROUPES["es"]["B1"] = [
    {"id": "b1-travailler", "nom": "Travailler en espagnol", "etapes": [
        E("b1-empleo", "📰", "Chercher un emploi", "chercher un emploi et demander poliment",
          feuilles=["condicional_politesse"], themes=["el_trabajo_b1", "comunicacion_profesional"], illustres=["metiers"], scenes=["buero"]),
        E("b1-empresa", "🏢", "L'entreprise", "parler de l'entreprise et de ce qui va se passer",
          feuilles=["futuro"], themes=["la_empresa", "las_finanzas", "la_economia", "el_consumo", "la_publicidad"], scenes=["buero"],
          fiches=["futuro-condicional"], series=["futuroExercises"]),
        E("b1-futuro", "🔮", "Mon avenir", "parler de ton avenir",
          feuilles=["futuro_irregulier"], themes=["la_educacion", "la_tecnologia_b1", "las_redes", "la_ciencia", "los_datos"],
          scenes=["klassenzimmer", "bibliothek"]),
        E("b1-haria", "🤷", "Ce que je ferais", "dire ce que tu ferais à la place de quelqu'un",
          feuilles=["condicional"], themes=["la_industria", "la_energia", "la_agricultura", "nom_taller"],
          scenes=["bauernhof", "heimwerken"], series=["condicionalExercises"]),
        E("b1-prohibir", "⛔", "Ne fais pas ça !", "donner un conseil ou une consigne : ne fais pas ça",
          feuilles=["imperativo_negativo"], themes=["la_salud_b1", "la_medicina", "cuerpo_humano", "la_alimentacion", "frutas_verduras_b1"],
          illustres=["cuerpo"], scenes=["arztpraxis"], fiches=["imperativo"]),
    ]},
    {"id": "b1-avis", "nom": "Donner mon avis", "etapes": [
        E("b1-deseo", "🙏", "Je veux que…", "dire ce que tu veux que les autres fassent",
          feuilles=["subjuntivo", "subjuntivo_souhait"], themes=["relaciones_b1", "la_psicologia", "el_voluntariado"],
          illustres=["emociones"], fiches=["subjuntivo"]),
        E("b1-cuando", "🧳", "Quand tu viendras", "parler de ce qui se passera quand…",
          feuilles=["subjuntivo_cuando"], themes=["viajes_b1", "la_movilidad", "la_geografia", "el_urbanismo", "nom_paisaje"],
          illustres=["transportes"], scenes=["zug", "stadtplatz"], series=["verbosConPreposicionExercises"]),
        E("b1-necesario", "🌍", "Il faut que…", "dire ce qu'il faut faire",
          feuilles=["subjuntivo_irregulier"],
          themes=["medioambiente_b1", "la_inmigracion", "la_igualdad", "la_discapacidad", "problemas_sociales"], scenes=["park"]),
        E("b1-historia", "📜", "Raconter l'histoire", "raconter l'histoire au passé",
          feuilles=["pluscuamperfecto"],
          themes=["la_historia", "la_cultura", "la_literatura", "la_religion", "la_arquitectura", "la_astronomia", "el_espectaculo"],
          scenes=["museum"]),
        E("b1-debate", "🗣️", "Débattre de l'actualité", "débattre de l'actualité",
          themes=["la_argumentacion", "la_actualidad", "la_sociedad", "la_politica", "la_justicia", "deporte_b1", "la_gastronomia"],
          fiches=["conectores"]),
    ]},
]

GROUPES["es"]["B2"] = [
    {"id": "b2-egal", "nom": "Discuter d'égal à égal", "etapes": [
        E("b2-matices", "🎚️", "Les nuances", "nuancer ce que tu dis",
          feuilles=["subj_imparfait"], themes=["los_matices", "el_registro", "emociones_b2"], series=["subjuntivoImperfectoExercises"]),
        E("b2-queria", "💭", "Je voulais que tu viennes", "dire ce que tu voulais que les autres fassent",
          feuilles=["subj_imparfait_emplois"], themes=["el_liderazgo", "la_gestion", "negociacion_b2"]),
        E("b2-si", "🤖", "Si j'avais…", "imaginer ce qui se passerait si…",
          feuilles=["si_irreel"], themes=["la_ia", "futuro_trabajo", "la_investigacion"], series=["oracionesSiExercises"]),
        E("b2-sihubiera", "⏪", "Si j'avais su…", "dire ce qui se serait passé si…",
          feuilles=["si_passe", "condicional_compuesto"], themes=["la_memoria", "la_etica", "la_bioetica"], series=["compuestosExercises"]),
    ]},
    {"id": "b2-actualite", "nom": "Comprendre l'actualité", "etapes": [
        E("b2-suponer", "🔍", "Supposer", "faire des suppositions",
          feuilles=["futuro_perfecto"], themes=["la_incertidumbre", "pensamiento_critico", "la_filosofia"]),
        E("b2-prensa", "📰", "Lire la presse", "comprendre un article de presse",
          feuilles=["pasiva"], themes=["el_periodismo", "la_geopolitica", "la_globalizacion", "la_macroeconomia"], series=["pasivaExercises"]),
        E("b2-indirecto", "🎙️", "Rapporter ce qu'on a dit", "rapporter ce que quelqu'un a dit",
          feuilles=["estilo_indirecto"], themes=["el_debate", "la_retorica", "la_critica"]),
        E("b2-mundo", "🏛️", "Penser le monde", "réfléchir aux grandes questions de société",
          themes=["derechos_humanos", "la_democracia", "la_sociologia", "la_antropologia", "la_estetica", "desarrollo_sostenible",
                  "nom_interior", "frutas_verduras_b2", "el_cuerpo_b2"]),
    ]},
]
