# -*- coding: utf-8 -*-
"""Le travail et la recherche d'emploi, theme illustre de la vague 4 (5 nov. 2026, Jacques : « On devrait peut-etre
lancer quatre nouveaux themes », puis « go »). Un sujet central du DTZ et de l'A2-B1 : l'annonce, le CV et la lettre,
l'entretien, le contrat, le premier jour, les collegues et la cheffe, se declarer malade.

    python visuel/travail/travail.py --json             # travail.json seul, gratuit
    python visuel/travail/travail.py --montrer          # les prompts seuls, gratuit
    python visuel/travail/travail.py --essai            # la planche d'essai (6 images, 0,90 $) -- ACCORD DE JACQUES
    python visuel/travail/travail.py gespraech krank    # celles-la seulement (0,15 $ chacune)
    python visuel/travail/travail.py --refaire krank    # l'ancienne passe en <nom>-rate<k>.png

L'ANGLE (regle 2 des themes : pas de scene refaite). La scene « Im Buero » enseigne les OBJETS du bureau ; le theme
enseigne le PARCOURS : lire une annonce, ecrire sa lettre, repondre en entretien, lire son contrat, faire connaissance,
appeler pour dire qu'on est malade. Les papiers (annonces, CV, lettre, contrat, appel) sont dessines en HTML par la
page : aucune image n'a de texte.

LES DEUX MONDES (les memes images, des phrases ecrites pour chaque langue), comme « Les demarches » :
  - en allemand, Mark Garnier a Berlin (Gartenstrasse 12, 13187 Berlin), 25 ans, ne le 14 mars 2001 a Montreal ; il
    fait un stage dans un bureau (l'oral du DTZ : « Im Moment mache ich ein Praktikum in einem Buero ») et cherche un
    poste. Il n'est PAS allemand (decision du 4 nov.) : c'est sans incidence ici, un titre de sejour autorise le travail.
    Sa future cheffe est la femme de l'image « unterschreiben » des demarches (blonde, la quarantaine, veste beige) :
    Frau Schneider, du service client de Sonnenweg Reisen. Ses collegues : Jonas et Lisa.
  - en espagnol, le Mark de « Mark en Madrid » (mexicain, ne a Mexico, comme dans « Les demarches ») ; la meme cheffe
    est la senora Navarro de Viajes Solano, ses collegues Jorge et Lucia.
Ni Anna ni sa famille : le travail de Mark n'est pas le leur.

LES PHRASES SONT FABRIQUEES ICI, depuis ces tables, et la page ne fait que les tirer : chaque question porte le mot
qu'elle fait travailler (a la forme du corpus), son enonce, sa reponse, une reserve de leurres CLAIREMENT faux (jamais
une reponse possible : « proches » pour les qualites, « compat » pour l'entretien), la phrase juste et sa traduction.
Le script verifie ce qu'il fabrique : aucun leurre egal a la reponse, chaque mot du theme vise par au moins deux
sortes, au moins 100 questions differentes par langue.

Images : fal, nano-banana-pro, 0,15 $ l'image. Mark ne se regenere jamais : retouche de son image de l'episode 2 ; la
cheffe et le bureau viennent de l'image « unterschreiben » des demarches (meme femme, meme piece) ; la chambre de Mark
de « La journee » (mark-1), son salon (mark-6), sa cuisine des demarches (telefon). Originaux hors du depot et de
OneDrive : C:/Users/jacqu/.wortando/travail/img/.
"""
import hashlib, io, json, os, re, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "travail", "img")
W = os.path.join(os.path.expanduser("~"), ".wortando")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
REFERENCES = {"Mark": PRINCIPAL + "/video/episode-02-beim-buergeramt/01-images/mark-moyen.png",
              "Bureau": W + "/demarches/img/unterschreiben.png",          # la cheffe et son bureau
              "Cuisine": W + "/demarches/img/telefon.png",                # la cuisine de Mark (demarches)
              "Salon": W + "/journee/img/mark-6.png",                     # le salon de Mark, son petit bureau
              "Chambre": W + "/journee/img/mark-1.png",                   # la chambre de Mark
              "Equipe": DOSSIER + "/kollegen.png"}                         # les deux collegues, une fois faits
LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}
TL = {"es": ["fr", "en", "pt", "de"], "de": ["fr", "en", "pt"]}        # les langues des phrases traduites en entier


# ---------------------------------------------------------------------------------------------------------------
# LES GENS. n : dans une phrase de la langue apprise (sujet) ; t : la meme personne dans les traductions.
GENS = {
    "de": {"mark":  {"n": "Mark", "g": "m"},
           "chef":  {"n": "Frau Schneider", "g": "f", "t": {"fr": "Mme Schneider", "en": "Ms Schneider", "pt": "a Sra. Schneider"}},
           "m":     {"n": "Jonas", "g": "m"},
           "f":     {"n": "Lisa", "g": "f"}},
    "es": {"mark":  {"n": "Mark", "g": "m"},
           "chef":  {"n": "la señora Navarro", "g": "f", "t": {"fr": "Mme Navarro", "en": "Ms Navarro", "pt": "a Sra. Navarro", "de": "Frau Navarro"}},
           "m":     {"n": "Jorge", "g": "m"},
           "f":     {"n": "Lucía", "g": "f"}},
}
FIRME = {"de": "Sonnenweg Reisen", "es": "Viajes Solano"}


def gens(langue, k, l=None):
    p = GENS[langue][k]
    return p["n"] if l is None else (p.get("t", {}).get(l) or p["n"])


def cap(s):
    return s[:1].upper() + s[1:]


def accord(s, g):
    """« ponctuel{=|le} » -> ponctuel / ponctuelle ; « {=he|she} » -> he / she."""
    return re.sub(r"\{=([^|}]*)\|([^}]*)\}", lambda m: m.group(1) if g == "m" else m.group(2), s)


def euros(x, l):
    ent = float(x).is_integer()
    if l == "en":
        return "€" + ("{:,.0f}".format(x) if ent else "{:,.2f}".format(x))
    s = "{:,.0f}".format(x) if ent else "{:,.2f}".format(x)
    s = s.replace(",", "§").replace(".", ",").replace("§", "\u202f" if l == "fr" else ".")
    return s + " €"


def lohn(x, par, l):
    e = euros(x, l)
    return {"de": {"monat": e + " im Monat", "stunde": e + " pro Stunde"},
            "es": {"monat": e + " al mes", "stunde": e + " la hora"},
            "fr": {"monat": e + " par mois", "stunde": e + " de l'heure"},
            "en": {"monat": e + " a month", "stunde": e + " an hour"},
            "pt": {"monat": e + " por mês", "stunde": e + " por hora"}}[l][par]


# ---------------------------------------------------------------------------------------------------------------
# LES CONTACTS DES ANNONCES : g, nom ; leurs formes selon la langue et la place dans la phrase.
def contact(c, l, cas="n"):
    f, nom = c["g"] == "f", c["nom"]
    if l == "de":
        return {"n": ("Frau " if f else "Herr ") + nom, "akk": ("Frau " if f else "Herrn ") + nom,
                "brief": ("Sehr geehrte Frau " if f else "Sehr geehrter Herr ") + nom + ",",
                "faux": ("Sehr geehrter Frau " if f else "Sehr geehrte Herr ") + nom + ","}[cas]
    if l == "es":
        return {"n": ("la señora " if f else "el señor ") + nom, "akk": ("a la señora " if f else "al señor ") + nom,
                "brief": ("Estimada señora " if f else "Estimado señor ") + nom + ":",
                "faux": ("Estimado señora " if f else "Estimada señor ") + nom + ":"}[cas]
    return {"fr": ("Mme " if f else "M. ") + nom, "en": ("Ms " if f else "Mr ") + nom,
            "pt": ("a Sra. " if f else "o Sr. ") + nom}[l]


# LE DEBUT : ab = dans l'annonce (« ab dem 1. Dezember ») ; am = dans une reponse (« Ich kann am 1. Dezember anfangen »)
BEGINN = {
    "sofort": {"de": ["ab sofort", "sofort"], "es": ["incorporación inmediata", "de inmediato"],
               "fr": ["dès maintenant", "tout de suite"], "en": ["immediately", "right away"], "pt": ["imediatamente", "imediatamente"]},
    "1dez":   {"de": ["ab dem 1. Dezember", "am 1. Dezember"], "es": ["a partir del 1 de diciembre", "el 1 de diciembre"],
               "fr": ["à partir du 1er décembre", "le 1er décembre"], "en": ["from 1 December", "on 1 December"], "pt": ["a partir de 1º de dezembro", "em 1º de dezembro"]},
    "1jan":   {"de": ["ab dem 1. Januar", "am 1. Januar"], "es": ["a partir del 1 de enero", "el 1 de enero"],
               "fr": ["à partir du 1er janvier", "le 1er janvier"], "en": ["from 1 January", "on 1 January"], "pt": ["a partir de 1º de janeiro", "em 1º de janeiro"]},
    "15jan":  {"de": ["ab dem 15. Januar", "am 15. Januar"], "es": ["a partir del 15 de enero", "el 15 de enero"],
               "fr": ["à partir du 15 janvier", "le 15 janvier"], "en": ["from 15 January", "on 15 January"], "pt": ["a partir de 15 de janeiro", "em 15 de janeiro"]},
}

# LE TEMPS DE TRAVAIL. mot / genre : le mot du corpus vise (None : aucun) ; satz : la phrase « Die Stelle ist in Vollzeit. »
UMFANG = {
    "de": {"vollzeit": {"mot": "Vollzeit", "genre": "die", "wort": "Vollzeit", "satz": "Die Stelle ist in Vollzeit."},
           "teilzeit": {"mot": "Teilzeit", "genre": "die", "wort": "Teilzeit", "satz": "Die Stelle ist in Teilzeit."},
           "minijob":  {"mot": "Minijob", "genre": "der", "wort": "Minijob", "satz": "Die Stelle ist ein Minijob."}},
    "es": {"vollzeit": {"mot": "jornada completa", "genre": "la", "wort": "jornada completa", "satz": "Es un puesto de jornada completa."},
           "teilzeit": {"mot": "media jornada", "genre": "la", "wort": "media jornada", "satz": "Es un puesto de media jornada."},
           "minijob":  {"mot": "trabajo", "genre": "el", "wort": "por horas", "satz": "Es un trabajo por horas."}},
}
UMFANG_T = {"vollzeit": {"fr": "Le poste est à temps plein.", "en": "The job is full-time.", "pt": "A vaga é de tempo integral.", "de": "Die Stelle ist in Vollzeit."},
            "teilzeit": {"fr": "Le poste est à temps partiel.", "en": "The job is part-time.", "pt": "A vaga é de meio período.", "de": "Die Stelle ist in Teilzeit."},
            "minijob":  {"fr": "Le poste est un mini-job, quelques heures par semaine.", "en": "The job is a mini-job, a few hours a week.", "pt": "A vaga é um minijob, poucas horas por semana.", "de": "Die Stelle ist ein Minijob."}}
UMFANG_T_ES = {"vollzeit": {"fr": "C'est un poste à temps plein.", "en": "It's a full-time job.", "pt": "É uma vaga de tempo integral.", "de": "Es ist eine Stelle in Vollzeit."},
               "teilzeit": {"fr": "C'est un poste à mi-temps.", "en": "It's a part-time job (half days).", "pt": "É uma vaga de meio período.", "de": "Es ist eine Stelle in Teilzeit (halbtags)."},
               "minijob":  {"fr": "C'est un travail payé à l'heure, quelques heures par semaine.", "en": "It's a job paid by the hour, a few hours a week.", "pt": "É um trabalho por hora, poucas horas por semana.", "de": "Es ist ein Job auf Stundenbasis, ein paar Stunden pro Woche."}}
UMFANG_MOT_T = {"vollzeit": {"fr": "temps plein", "en": "full-time", "pt": "tempo integral", "de": "Vollzeit"},
                "teilzeit": {"fr": "temps partiel", "en": "part-time", "pt": "meio período", "de": "Teilzeit"},
                "minijob":  {"fr": "mini-job (quelques heures)", "en": "mini-job (a few hours)", "pt": "minijob (poucas horas)", "de": "Minijob"}}

# ---------------------------------------------------------------------------------------------------------------
# LES QUALITES (ce que les annonces demandent, ce qu'on dit de soi en entretien). def : ce que fait la personne, {P} =
# la personne ; proches : les qualites que cette description pourrait AUSSI dire (jamais un leurre).
QUALITES = {
    "de": {
        "pünktlich":     {"def": "{P} kommt nie zu spät.", "proches": ["zuverlässig"],
                          "t": {"fr": ["ponctuel{=|le}", "{P} n'arrive jamais en retard."], "en": ["punctual", "{P} is never late."], "pt": ["pontual", "{P} nunca se atrasa."]}},
        "zuverlässig":   {"def": "{P} macht immer, was {=er|sie} verspricht.", "proches": ["pünktlich", "fleißig"],
                          "t": {"fr": ["fiable", "{P} fait toujours ce qu'{=il|elle} promet."], "en": ["reliable", "{P} always does what {=he|she} promises."], "pt": ["confiável", "{P} sempre faz o que promete."]}},
        "freundlich":    {"def": "{P} lächelt und grüßt die Kunden immer.", "proches": ["teamfähig"],
                          "t": {"fr": ["aimable", "{P} sourit et salue toujours les clients."], "en": ["friendly", "{P} always smiles and greets the customers."], "pt": ["simpátic{=o|a}", "{P} sempre sorri e cumprimenta os clientes."]}},
        "flexibel":      {"def": "{P} kann auch am Wochenende arbeiten.", "proches": [],
                          "t": {"fr": ["flexible", "{P} peut aussi travailler le week-end."], "en": ["flexible", "{P} can also work at weekends."], "pt": ["flexível", "{P} também pode trabalhar no fim de semana."]}},
        "fleißig":       {"def": "{P} arbeitet viel und macht nur kurze Pausen.", "proches": ["zuverlässig"],
                          "t": {"fr": ["travailleu{=r|se}", "{P} travaille beaucoup et ne fait que de courtes pauses."], "en": ["hard-working", "{P} works a lot and only takes short breaks."], "pt": ["esforçad{=o|a}", "{P} trabalha muito e só faz pausas curtas."]}},
        "selbstständig": {"def": "{P} arbeitet gut allein, ohne Hilfe.", "proches": [],
                          "t": {"fr": ["autonome", "{P} travaille bien seul{=|e}, sans aide."], "en": ["independent", "{P} works well alone, without help."], "pt": ["independente", "{P} trabalha bem sozinh{=o|a}, sem ajuda."]}},
        "ordentlich":    {"def": "{P} räumt den Schreibtisch jeden Abend auf.", "proches": [],
                          "t": {"fr": ["ordonné{=|e}", "{P} range son bureau chaque soir."], "en": ["tidy", "{P} tidies {=his|her} desk every evening."], "pt": ["organizad{=o|a}", "{P} arruma a mesa toda noite."]}},
        "teamfähig":     {"def": "{P} arbeitet gern mit den Kollegen zusammen.", "proches": ["freundlich"],
                          "t": {"fr": ["!a l'esprit d'équipe", "{P} aime travailler avec ses collègues."], "en": ["a team player", "{P} likes working with colleagues."], "pt": ["!trabalha bem em equipe", "{P} gosta de trabalhar com os colegas."]}},
    },
    "es": {
        "puntual":       {"def": "{P} nunca llega tarde.", "proches": ["responsable"],
                          "t": {"fr": ["ponctuel{=|le}", "{P} n'arrive jamais en retard."], "en": ["punctual", "{P} is never late."], "pt": ["pontual", "{P} nunca se atrasa."], "de": ["pünktlich", "{P} kommt nie zu spät."]}},
        "responsable":   {"def": "{P} siempre cumple lo que promete.", "proches": ["puntual", "trabajador"],
                          "t": {"fr": ["responsable", "{P} tient toujours ses promesses."], "en": ["responsible", "{P} always keeps {=his|her} promises."], "pt": ["responsável", "{P} sempre cumpre o que promete."], "de": ["zuverlässig", "{P} hält immer, was {=er|sie} verspricht."]}},
        "amable":        {"def": "{P} siempre sonríe y saluda a los clientes.", "proches": [],
                          "t": {"fr": ["aimable", "{P} sourit et salue toujours les clients."], "en": ["friendly", "{P} always smiles and greets the customers."], "pt": ["simpátic{=o|a}", "{P} sempre sorri e cumprimenta os clientes."], "de": ["freundlich", "{P} lächelt und grüßt die Kunden immer."]}},
        "flexible":      {"def": "{P} también puede trabajar los fines de semana.", "proches": [],
                          "t": {"fr": ["flexible", "{P} peut aussi travailler le week-end."], "en": ["flexible", "{P} can also work at weekends."], "pt": ["flexível", "{P} também pode trabalhar no fim de semana."], "de": ["flexibel", "{P} kann auch am Wochenende arbeiten."]}},
        "trabajador":    {"def": "{P} trabaja mucho y hace pocas pausas.", "proches": ["responsable"], "f": "trabajadora",
                          "t": {"fr": ["travailleu{=r|se}", "{P} travaille beaucoup et fait peu de pauses."], "en": ["hard-working", "{P} works a lot and takes few breaks."], "pt": ["esforçad{=o|a}", "{P} trabalha muito e faz poucas pausas."], "de": ["fleißig", "{P} arbeitet viel und macht wenige Pausen."]}},
        "ordenado":      {"def": "{P} recoge su mesa todas las tardes.", "proches": [], "f": "ordenada",
                          "t": {"fr": ["ordonné{=|e}", "{P} range son bureau chaque soir."], "en": ["tidy", "{P} tidies {=his|her} desk every evening."], "pt": ["organizad{=o|a}", "{P} arruma a mesa todo fim de tarde."], "de": ["ordentlich", "{P} räumt jeden Abend den Schreibtisch auf."]}},
        "independiente": {"def": "{P} trabaja bien sol{=o|a}, sin ayuda.", "proches": [],
                          "t": {"fr": ["autonome", "{P} travaille bien seul{=|e}, sans aide."], "en": ["independent", "{P} works well alone, without help."], "pt": ["independente", "{P} trabalha bem sozinh{=o|a}, sem ajuda."], "de": ["selbstständig", "{P} arbeitet gut allein, ohne Hilfe."]}},
    },
}
MARK_QUALITES = {"de": ["pünktlich", "zuverlässig", "freundlich", "flexibel"], "es": ["puntual", "responsable", "amable", "flexible"]}


def adj(langue, a, g):
    return QUALITES[langue][a].get("f", a) if (g == "f" and langue == "es") else a


# ---------------------------------------------------------------------------------------------------------------
# LES ANNONCES. stelle : le poste affiche ; mot / genre : le metier du corpus que le poste fait travailler ; ou : le lieu
# de travail (« Der neue Kellner arbeitet in einem Cafe. ») ; erwartet : les qualites demandees ; kontakt : a qui ecrire ;
# brief : qui ecrit la lettre (Mark ecrit pour les postes qu'il vise ; les autres lettres sont d'autres candidats).
ANNONCES = {
    "de": [
        {"id": "sonnenweg", "firma": "Sonnenweg Reisen GmbH", "stelle": "Mitarbeiter im Kundenservice", "mot": "Mitarbeiter", "genre": "der",
         "neu": "Der neue Mitarbeiter", "ou": "in einem Reisebüro", "umfang": "vollzeit", "stunden": 40, "lohn": [3000, "monat"], "beginn": "1dez",
         "erwartet": ["freundlich", "zuverlässig"], "plus": "Sie sprechen Französisch und Englisch.", "bietet": "28 Tage Urlaub, ein nettes Team",
         "kontakt": {"g": "f", "nom": "Schneider"}, "mail": "jobs@sonnenweg-reisen.de", "brief": "Mark",
         "t": {"fr": ["employé au service client", "Le nouvel employé travaille dans une agence de voyages."], "en": ["customer service assistant", "The new assistant works in a travel agency."], "pt": ["atendente", "O novo atendente trabalha em uma agência de viagens."]}},
        {"id": "hotel", "firma": "Hotel am Park", "stelle": "Rezeptionist", "mot": "Rezeptionist", "genre": "der",
         "neu": "Der neue Rezeptionist", "ou": "in einem Hotel", "umfang": "teilzeit", "stunden": 25, "lohn": [15, "stunde"], "beginn": "15jan",
         "erwartet": ["freundlich", "flexibel"], "plus": "Sie sprechen gut Englisch.", "bietet": "Arbeit im Zentrum von Berlin",
         "kontakt": {"g": "m", "nom": "Lange"}, "mail": "personal@hotel-am-park.de", "brief": "Mark",
         "t": {"fr": ["réceptionniste", "Le nouveau réceptionniste travaille dans un hôtel."], "en": ["receptionist", "The new receptionist works in a hotel."], "pt": ["recepcionista", "O novo recepcionista trabalha em um hotel."]}},
        {"id": "cafe", "firma": "Café Kranich", "stelle": "Kellner", "mot": "Kellner", "genre": "der",
         "neu": "Der neue Kellner", "ou": "in einem Café", "umfang": "minijob", "stunden": 8, "lohn": [14.5, "stunde"], "beginn": "sofort",
         "erwartet": ["pünktlich", "freundlich"], "plus": "Arbeit am Samstag und am Sonntag.", "bietet": "ein junges Team",
         "kontakt": {"g": "f", "nom": "Krause"}, "mail": "hallo@cafe-kranich.de", "brief": "Mark",
         "t": {"fr": ["serveur", "Le nouveau serveur travaille dans un café."], "en": ["waiter", "The new waiter works in a café."], "pt": ["garçom", "O novo garçom trabalha em um café."]}},
        {"id": "restaurant", "firma": "Restaurant Linde", "stelle": "Koch", "mot": "Koch", "genre": "der",
         "neu": "Der neue Koch", "ou": "in einem Restaurant", "umfang": "vollzeit", "stunden": 40, "lohn": [2600, "monat"], "beginn": "1jan",
         "erwartet": ["teamfähig", "selbstständig"], "plus": "Sie haben eine Ausbildung als Koch.", "bietet": "ein Essen pro Tag",
         "kontakt": {"g": "m", "nom": "Wolf"}, "mail": "kueche@restaurant-linde.de", "brief": "Ali Demir",
         "t": {"fr": ["cuisinier", "Le nouveau cuisinier travaille dans un restaurant."], "en": ["cook", "The new cook works in a restaurant."], "pt": ["cozinheiro", "O novo cozinheiro trabalha em um restaurante."]}},
        {"id": "baeckerei", "firma": "Bäckerei Sommer", "stelle": "Verkäufer", "mot": "Verkäufer", "genre": "der",
         "neu": "Der neue Verkäufer", "ou": "in einer Bäckerei", "umfang": "teilzeit", "stunden": 20, "lohn": [14.5, "stunde"], "beginn": "sofort",
         "erwartet": ["pünktlich", "ordentlich"], "plus": "Arbeit am Morgen, von 6 bis 10 Uhr.", "bietet": "frisches Brot für das Team",
         "kontakt": {"g": "f", "nom": "Sommer"}, "mail": "info@baeckerei-sommer.de", "brief": "Sofia Rossi",
         "t": {"fr": ["vendeur", "Le nouveau vendeur travaille dans une boulangerie."], "en": ["sales assistant", "The new sales assistant works in a bakery."], "pt": ["vendedor", "O novo vendedor trabalha em uma padaria."]}},
        {"id": "apotheke", "firma": "Apotheke am Markt", "stelle": "Fahrer", "mot": "Fahrer", "genre": "der",
         "neu": "Der neue Fahrer", "ou": "für eine Apotheke", "umfang": "minijob", "stunden": 6, "lohn": [15, "stunde"], "beginn": "1dez",
         "erwartet": ["zuverlässig", "pünktlich"], "plus": "Sie bringen Medikamente zu unseren Kunden.", "bietet": "ein Auto der Apotheke",
         "kontakt": {"g": "m", "nom": "Brandt"}, "mail": "apotheke-am-markt@mail.de", "brief": "Piotr Nowak",
         "t": {"fr": ["chauffeur", "Le nouveau chauffeur travaille pour une pharmacie."], "en": ["driver", "The new driver works for a pharmacy."], "pt": ["motorista", "O novo motorista trabalha para uma farmácia."]}},
    ],
    "es": [
        {"id": "sonnenweg", "firma": "Viajes Solano", "stelle": "Agente de atención al cliente", "mot": "cliente", "genre": "el",
         "neu": "El nuevo agente de atención al cliente", "ou": "en una agencia de viajes", "umfang": "vollzeit", "stunden": 40, "lohn": [1700, "monat"], "beginn": "1dez",
         "erwartet": ["amable", "responsable"], "plus": "Hablas inglés y francés.", "bietet": "30 días de vacaciones, un buen equipo",
         "kontakt": {"g": "f", "nom": "Navarro"}, "mail": "empleo@viajessolano.es", "brief": "Mark",
         "t": {"fr": ["agent du service client", "Le nouvel agent du service client travaille dans une agence de voyages."], "en": ["customer service agent", "The new customer service agent works in a travel agency."], "pt": ["atendente", "O novo atendente trabalha em uma agência de viagens."], "de": ["Mitarbeiter im Kundenservice", "Der neue Mitarbeiter im Kundenservice arbeitet in einem Reisebüro."]}},
        {"id": "hotel", "firma": "Hotel Retiro", "stelle": "Recepcionista", "mot": "recepcionista", "genre": "el",
         "neu": "El nuevo recepcionista", "ou": "en un hotel", "umfang": "teilzeit", "stunden": 20, "lohn": [850, "monat"], "beginn": "15jan",
         "erwartet": ["amable", "flexible"], "plus": "Hablas bien inglés.", "bietet": "trabajo en el centro de Madrid",
         "kontakt": {"g": "m", "nom": "Gil"}, "mail": "personal@hotelretiro.es", "brief": "Mark",
         "t": {"fr": ["réceptionniste", "Le nouveau réceptionniste travaille dans un hôtel."], "en": ["receptionist", "The new receptionist works in a hotel."], "pt": ["recepcionista", "O novo recepcionista trabalha em um hotel."], "de": ["Rezeptionist", "Der neue Rezeptionist arbeitet in einem Hotel."]}},
        {"id": "cafe", "firma": "Cafetería Luna", "stelle": "Camarero/a", "mot": "camarero", "genre": "el",
         "neu": "El nuevo camarero", "ou": "en una cafetería", "umfang": "minijob", "stunden": 10, "lohn": [10, "stunde"], "beginn": "sofort",
         "erwartet": ["puntual", "amable"], "plus": "Trabajo los sábados y los domingos.", "bietet": "un equipo joven",
         "kontakt": {"g": "f", "nom": "López"}, "mail": "hola@cafeterialuna.es", "brief": "Mark",
         "t": {"fr": ["serveur", "Le nouveau serveur travaille dans un café."], "en": ["waiter", "The new waiter works in a café."], "pt": ["garçom", "O novo garçom trabalha em um café."], "de": ["Kellner", "Der neue Kellner arbeitet in einem Café."]}},
        {"id": "restaurant", "firma": "Restaurante El Olivo", "stelle": "Cocinero/a", "mot": "cocinero", "genre": "el",
         "neu": "El nuevo cocinero", "ou": "en un restaurante", "umfang": "vollzeit", "stunden": 40, "lohn": [1600, "monat"], "beginn": "1jan",
         "erwartet": ["trabajador", "independiente"], "plus": "Tienes experiencia en cocina.", "bietet": "una comida al día",
         "kontakt": {"g": "m", "nom": "Ruiz"}, "mail": "cocina@elolivo.es", "brief": "Andrés Romero",
         "t": {"fr": ["cuisinier", "Le nouveau cuisinier travaille dans un restaurant."], "en": ["cook", "The new cook works in a restaurant."], "pt": ["cozinheiro", "O novo cozinheiro trabalha em um restaurante."], "de": ["Koch", "Der neue Koch arbeitet in einem Restaurant."]}},
        {"id": "baeckerei", "firma": "Panadería Sol", "stelle": "Dependiente/a", "mot": "dependiente", "genre": "el",
         "neu": "El nuevo dependiente", "ou": "en una panadería", "umfang": "teilzeit", "stunden": 20, "lohn": [800, "monat"], "beginn": "sofort",
         "erwartet": ["puntual", "ordenado"], "plus": "Trabajo por la mañana, de 7 a 11.", "bietet": "pan del día para el equipo",
         "kontakt": {"g": "f", "nom": "Vega"}, "mail": "info@panaderiasol.es", "brief": "Carla Ortiz",
         "t": {"fr": ["vendeur", "Le nouveau vendeur travaille dans une boulangerie."], "en": ["sales assistant", "The new sales assistant works in a bakery."], "pt": ["vendedor", "O novo vendedor trabalha em uma padaria."], "de": ["Verkäufer", "Der neue Verkäufer arbeitet in einer Bäckerei."]}},
        {"id": "apotheke", "firma": "Farmacia Plaza", "stelle": "Conductor/a", "mot": "conductor", "genre": "el",
         "neu": "El nuevo conductor", "ou": "para una farmacia", "umfang": "minijob", "stunden": 8, "lohn": [11, "stunde"], "beginn": "1dez",
         "erwartet": ["responsable", "puntual"], "plus": "Llevas medicamentos a nuestros clientes.", "bietet": "un coche de la farmacia",
         "kontakt": {"g": "m", "nom": "Sanz"}, "mail": "farmaciaplaza@correo.es", "brief": "Pedro Gómez",
         "t": {"fr": ["chauffeur", "Le nouveau chauffeur travaille pour une pharmacie."], "en": ["driver", "The new driver works for a pharmacy."], "pt": ["motorista", "O novo motorista trabalha para uma farmácia."], "de": ["Fahrer", "Der neue Fahrer arbeitet für eine Apotheke."]}},
    ],
}

# ---------------------------------------------------------------------------------------------------------------
# LE CV DE MARK. Chaque rubrique : titre affiche, mot vise (None : le CV lui-meme), lignes.
CV = {
    "de": {"titre": "Lebenslauf", "mot": ["Lebenslauf", "der"], "rubriques": [
        {"titre": "Persönliche Daten", "mot": None, "lignes": ["Mark Garnier", "geboren am 14.03.2001 in Montréal", "Gartenstraße 12, 13187 Berlin", "Telefon: 0176 23 81 45 09"]},
        {"titre": "Berufserfahrung", "mot": ["Praktikum", "das"], "lignes": ["seit 03/2026: Praktikum in einem Büro, Berlin", "2023–2025: Kundenservice (Teilzeit), Reisebüro, Montréal"]},
        {"titre": "Ausbildung", "mot": ["Ausbildung", "die"], "lignes": ["2019–2023: Studium Tourismus (Bachelor), Montréal"]},
        # 6 nov. 2026 (decision de Jacques, la coherence des personnages) : Mark arrive a Berlin et APPREND l'allemand --
        # jamais « fliessend ». Il parle trois langues (« Ich spreche Französisch, Deutsch und Englisch », l'entretien) :
        # l'espagnol (« Grundkenntnisse ») quitte le CV, qui le disait au meme niveau que l'allemand.
        {"titre": "Sprachkenntnisse", "mot": ["Sprachkenntnisse", "die (Pl.)"], "lignes": ["Französisch: Muttersprache", "Deutsch: Grundkenntnisse (Deutschkurs)", "Englisch: sehr gut"]},
        {"titre": "Hobbys", "mot": ["Hobby", "das"], "lignes": ["Fußball, Laufen, Kochen"]}],
        "t": {"fr": ["Données personnelles", "Expérience professionnelle", "Formation", "Langues", "Loisirs"],
              "en": ["Personal details", "Work experience", "Education", "Languages", "Hobbies"],
              "pt": ["Dados pessoais", "Experiência profissional", "Formação", "Idiomas", "Hobbies"]}},
    "es": {"titre": "Currículum vítae", "mot": ["currículum", "el"], "rubriques": [
        {"titre": "Datos personales", "mot": None, "lignes": ["Mark Garnier", "Nacido el 14/03/2001 en Ciudad de México", "Calle de la Luna 12, 2.º B, 28004 Madrid", "Teléfono: 612 48 30 17"]},
        {"titre": "Experiencia laboral", "mot": ["experiencia", "la"], "lignes": ["Desde 03/2026: becario en una oficina, Madrid", "2023–2025: atención al cliente (media jornada), agencia de viajes, Ciudad de México"]},
        {"titre": "Formación", "mot": ["formación", "la"], "lignes": ["2019–2023: Grado en Turismo, Ciudad de México"]},
        {"titre": "Idiomas", "mot": ["idioma", "el"], "lignes": ["Español: lengua materna", "Inglés: muy bien", "Francés: nivel intermedio"]},
        {"titre": "Aficiones", "mot": None, "lignes": ["Fútbol, correr, cocinar"]}],
        "t": {"fr": ["Données personnelles", "Expérience professionnelle", "Formation", "Langues", "Loisirs"],
              "en": ["Personal details", "Work experience", "Education", "Languages", "Hobbies"],
              "pt": ["Dados pessoais", "Experiência profissional", "Formação", "Idiomas", "Hobbies"],
              "de": ["Persönliche Daten", "Berufserfahrung", "Ausbildung", "Sprachkenntnisse", "Hobbys"]}},
}
# les langues du CV, pour les « vrai ou faux » : [langue dans la phrase, niveau dans la phrase, traductions]
SPRACHEN = {
    "de": [["Französisch", "Mark spricht Französisch als Muttersprache.", {"fr": "Le français est la langue maternelle de Mark.", "en": "French is Mark's mother tongue.", "pt": "O francês é a língua materna do Mark."}],
           ["Deutsch", "Mark spricht ein bisschen Deutsch und lernt es.", {"fr": "Mark parle un peu allemand et l'apprend.", "en": "Mark speaks a little German and is learning it.", "pt": "Mark fala um pouco de alemão e está aprendendo."}],
           ["Englisch", "Mark spricht sehr gut Englisch.", {"fr": "Mark parle très bien anglais.", "en": "Mark speaks very good English.", "pt": "Mark fala inglês muito bem."}]],
    "es": [["español", "La lengua materna de Mark es el español.", {"fr": "La langue maternelle de Mark est l'espagnol.", "en": "Mark's mother tongue is Spanish.", "pt": "A língua materna do Mark é o espanhol.", "de": "Marks Muttersprache ist Spanisch."}],
           ["inglés", "Mark habla muy bien inglés.", {"fr": "Mark parle très bien anglais.", "en": "Mark speaks very good English.", "pt": "Mark fala inglês muito bem.", "de": "Mark spricht sehr gut Englisch."}],
           ["francés", "Mark tiene un nivel intermedio de francés.", {"fr": "Mark a un niveau intermédiaire en français.", "en": "Mark has intermediate French.", "pt": "Mark tem nível intermediário de francês.", "de": "Mark spricht mittelgut Französisch."}]],
}
# la phrase fausse : une autre langue a la meme place (« Mark spricht fliessend Spanisch. »)
SPRACHE_T = {"de": {"Französisch": "Französisch", "Deutsch": "Deutsch", "Englisch": "Englisch"},
             "es": {"español": "español", "inglés": "inglés", "francés": "francés"}}

# ---------------------------------------------------------------------------------------------------------------
# LA LETTRE. Les lignes, avec leurs morceaux a trou : (cle, texte juste, leurres, mot vise, consigne)
def lettre(langue, a):
    k = a["kontakt"]
    beg = BEGINN[a["beginn"]][langue][1]
    q = [adj(langue, x, "m") for x in a["erwartet"]]
    if langue == "de":
        stelle = a["stelle"]
        lignes = ["Bewerbung als " + stelle, contact(k, "de", "brief"),
                  "ich habe Ihre Anzeige gelesen und bewerbe mich um die Stelle als " + stelle + ".",
                  "Ich bin " + q[0] + " und " + q[1] + ". Ich kann " + beg + " anfangen.",
                  "Über eine Einladung zu einem Vorstellungsgespräch freue ich mich.",
                  "Mit freundlichen Grüßen", a["brief"] if a["brief"] != "Mark" else "Mark Garnier"]
        trous = [
            ("anrede", 1, contact(k, "de", "brief"), [contact(k, "de", "faux"), ("Hallo Frau " if k["g"] == "f" else "Hallo Herr ") + k["nom"] + ","], ["Anschreiben", "das"], "c_lettreDebut"),
            ("gruss", 5, "Mit freundlichen Grüßen", ["Tschüss", "Bis bald", "Hallo"], ["Gruß", "der"], "c_lettreFin"),
            ("um", 2, "um", ["auf", "mit", "an"], ["sich bewerben", "verbe"], "c_lettreMot"),
            ("als", 2, "als", ["wie", "von"], ["Stelle", "die"], "c_lettreMot"),
            ("bewerbe", 2, "bewerbe", ["stelle", "melde", "lerne"], ["Bewerbung", "die"], "c_lettreMot"),
        ]
        betreff = "Betreff"
    else:
        stelle = a["stelle"].split("/")[0].lower()
        lignes = ["Solicitud del puesto de " + stelle, contact(k, "es", "brief"),
                  "He leído su oferta y me gustaría solicitar el puesto de " + stelle + ".",
                  "Soy " + q[0] + " y " + q[1] + ". Puedo empezar " + beg + ".",
                  "Quedo a su disposición para una entrevista.",
                  "Un cordial saludo,", a["brief"] if a["brief"] != "Mark" else "Mark Garnier"]
        trous = [
            ("anrede", 1, contact(k, "es", "brief"), [contact(k, "es", "faux"), ("¡Hola, señora " if k["g"] == "f" else "¡Hola, señor ") + k["nom"] + "!"], ["carta de presentación", "la"], "c_lettreDebut"),
            ("gruss", 5, "Un cordial saludo,", ["¡Chao!", "¡Hasta luego!", "¡Hola!"], ["saludo", "el"], "c_lettreFin"),
            ("de", 2, "de", ["a", "en", "con"], ["puesto", "el"], "c_lettreMot"),
            ("solicitar", 2, "solicitar", ["firmar", "comer", "llamar"], ["solicitar", "verbe"], "c_lettreMot"),
        ]
        betreff = "Asunto"
    return lignes, trous, betreff


# ---------------------------------------------------------------------------------------------------------------
# L'ENTRETIEN. Pour les deux postes que vise Mark (sonnenweg, hotel). q : la question du recruteur ; r : la reponse de
# Mark, fabriquee depuis son CV et l'annonce ({a} {b} : deux de ses qualites ; {am} : le debut ; {umf} : le temps de
# travail) ; compat : les autres reponses qui pourraient aussi convenir (jamais un leurre) ; mot : le mot vise.
ENTRETIEN = {
    "de": [
        {"id": "ueber", "q": "Erzählen Sie bitte etwas über sich.", "r": "Ich heiße Mark Garnier, ich bin 25 Jahre alt und komme aus Kanada.", "compat": ["sprachen", "erfahrung", "staerken", "warum"], "mot": ["Vorstellungsgespräch", "das"],
         "t": {"fr": ["Parlez-moi un peu de vous.", "Je m'appelle Mark Garnier, j'ai 25 ans et je viens du Canada."], "en": ["Please tell me a little about yourself.", "My name is Mark Garnier, I'm 25 and I'm from Canada."], "pt": ["Fale um pouco sobre você.", "Eu me chamo Mark Garnier, tenho 25 anos e sou do Canadá."]}},
        {"id": "sprachen", "q": "Welche Sprachen sprechen Sie?", "r": "Ich spreche Französisch, Deutsch und Englisch.", "compat": ["ueber", "staerken", "warum"], "mot": ["Sprache", "die"],
         "t": {"fr": ["Quelles langues parlez-vous ?", "Je parle français, allemand et anglais."], "en": ["Which languages do you speak?", "I speak French, German and English."], "pt": ["Que idiomas o senhor fala?", "Falo francês, alemão e inglês."]}},
        {"id": "erfahrung", "q": "Haben Sie schon Berufserfahrung?", "r": "Ja, ich habe zwei Jahre im Kundenservice gearbeitet.", "compat": ["ueber", "staerken", "warum"], "mot": ["arbeiten", "verbe"],
         "t": {"fr": ["Avez-vous déjà de l'expérience professionnelle ?", "Oui, j'ai travaillé deux ans au service client."], "en": ["Do you have any work experience?", "Yes, I worked in customer service for two years."], "pt": ["O senhor já tem experiência profissional?", "Sim, trabalhei dois anos no atendimento ao cliente."]}},
        {"id": "staerken", "q": "Was sind Ihre Stärken?", "r": "Ich bin {a} und {b}.", "compat": ["ueber", "sprachen", "erfahrung", "warum"], "mot": ["Stärke", "die"],
         "t": {"fr": ["Quels sont vos points forts ?", "Je suis {a} et {b}."], "en": ["What are your strengths?", "I'm {a} and {b}."], "pt": ["Quais são os seus pontos fortes?", "Sou {a} e {b}."]}},
        {"id": "beginn", "q": "Wann können Sie anfangen?", "r": "Ich kann {am} anfangen.", "compat": [], "mot": ["anfangen", "verbe"],
         "t": {"fr": ["Quand pouvez-vous commencer ?", "Je peux commencer {am}."], "en": ["When can you start?", "I can start {am}."], "pt": ["Quando o senhor pode começar?", "Posso começar {am}."]}},
        {"id": "umfang", "q": "Möchten Sie in Vollzeit oder in Teilzeit arbeiten?", "r": "Ich möchte gern in {umf} arbeiten.", "compat": [], "mot": None,
         "t": {"fr": ["Voulez-vous travailler à temps plein ou à temps partiel ?", "J'aimerais travailler à {umf}."], "en": ["Would you like to work full-time or part-time?", "I'd like to work {umf}."], "pt": ["O senhor quer trabalhar em tempo integral ou meio período?", "Eu gostaria de trabalhar em {umf}."]}},
        {"id": "fragen", "q": "Haben Sie noch Fragen?", "r": "Ja: Wie viele Tage Urlaub habe ich im Jahr?", "compat": [], "mot": ["Urlaub", "der"],
         "t": {"fr": ["Avez-vous encore des questions ?", "Oui : combien de jours de congé ai-je par an ?"], "en": ["Do you have any questions?", "Yes: how many days of holiday do I get a year?"], "pt": ["O senhor tem mais alguma pergunta?", "Sim: quantos dias de férias eu tenho por ano?"]}},
        {"id": "warum", "q": "Warum möchten Sie bei uns arbeiten?", "r": "Ich arbeite gern mit Menschen, und ich spreche drei Sprachen.", "compat": ["ueber", "sprachen", "staerken", "erfahrung"], "mot": ["Vorstellungsgespräch", "das"],
         "t": {"fr": ["Pourquoi voulez-vous travailler chez nous ?", "J'aime travailler avec les gens, et je parle trois langues."], "en": ["Why do you want to work for us?", "I like working with people, and I speak three languages."], "pt": ["Por que o senhor quer trabalhar conosco?", "Gosto de trabalhar com pessoas e falo três idiomas."]}},
    ],
    "es": [
        {"id": "ueber", "q": "Hábleme un poco de usted.", "r": "Me llamo Mark Garnier, tengo 25 años y soy de México.", "compat": ["sprachen", "erfahrung", "staerken", "warum"], "mot": ["entrevista", "la"],
         "t": {"fr": ["Parlez-moi un peu de vous.", "Je m'appelle Mark Garnier, j'ai 25 ans et je suis du Mexique."], "en": ["Tell me a little about yourself.", "My name is Mark Garnier, I'm 25 and I'm from Mexico."], "pt": ["Fale um pouco sobre você.", "Eu me chamo Mark Garnier, tenho 25 anos e sou do México."], "de": ["Erzählen Sie bitte etwas über sich.", "Ich heiße Mark Garnier, ich bin 25 Jahre alt und komme aus Mexiko."]}},
        {"id": "sprachen", "q": "¿Qué idiomas habla?", "r": "Hablo español, inglés y francés.", "compat": ["ueber", "staerken", "warum"], "mot": ["idioma", "el"],
         "t": {"fr": ["Quelles langues parlez-vous ?", "Je parle espagnol, anglais et français."], "en": ["Which languages do you speak?", "I speak Spanish, English and French."], "pt": ["Que idiomas o senhor fala?", "Falo espanhol, inglês e francês."], "de": ["Welche Sprachen sprechen Sie?", "Ich spreche Spanisch, Englisch und Französisch."]}},
        {"id": "erfahrung", "q": "¿Tiene experiencia?", "r": "Sí, he trabajado dos años en atención al cliente.", "compat": ["ueber", "staerken", "warum"], "mot": ["experiencia", "la"],
         "t": {"fr": ["Avez-vous de l'expérience ?", "Oui, j'ai travaillé deux ans au service client."], "en": ["Do you have any experience?", "Yes, I have worked in customer service for two years."], "pt": ["O senhor tem experiência?", "Sim, trabalhei dois anos no atendimento ao cliente."], "de": ["Haben Sie Erfahrung?", "Ja, ich habe zwei Jahre im Kundenservice gearbeitet."]}},
        {"id": "staerken", "q": "¿Cuáles son sus puntos fuertes?", "r": "Soy {a} y {b}.", "compat": ["ueber", "sprachen", "erfahrung", "warum"], "mot": None,
         "t": {"fr": ["Quels sont vos points forts ?", "Je suis {a} et {b}."], "en": ["What are your strengths?", "I'm {a} and {b}."], "pt": ["Quais são os seus pontos fortes?", "Sou {a} e {b}."], "de": ["Was sind Ihre Stärken?", "Ich bin {a} und {b}."]}},
        {"id": "beginn", "q": "¿Cuándo puede empezar?", "r": "Puedo empezar {am}.", "compat": [], "mot": ["empezar", "verbe"],
         "t": {"fr": ["Quand pouvez-vous commencer ?", "Je peux commencer {am}."], "en": ["When can you start?", "I can start {am}."], "pt": ["Quando o senhor pode começar?", "Posso começar {am}."], "de": ["Wann können Sie anfangen?", "Ich kann {am} anfangen."]}},
        {"id": "umfang", "q": "¿Prefiere jornada completa o media jornada?", "r": "Prefiero {umf}.", "compat": [], "mot": None,
         "t": {"fr": ["Préférez-vous un temps plein ou un mi-temps ?", "Je préfère {umf}."], "en": ["Do you prefer full-time or part-time?", "I prefer {umf}."], "pt": ["O senhor prefere tempo integral ou meio período?", "Prefiro {umf}."], "de": ["Möchten Sie lieber in Vollzeit oder in Teilzeit arbeiten?", "Ich möchte lieber in {umf} arbeiten."]}},
        {"id": "fragen", "q": "¿Tiene alguna pregunta?", "r": "Sí: ¿cuántos días de vacaciones tengo al año?", "compat": [], "mot": ["vacaciones", "las"],
         "t": {"fr": ["Avez-vous une question ?", "Oui : combien de jours de congé ai-je par an ?"], "en": ["Do you have any questions?", "Yes: how many days of holiday do I get a year?"], "pt": ["O senhor tem alguma pergunta?", "Sim: quantos dias de férias eu tenho por ano?"], "de": ["Haben Sie noch Fragen?", "Ja: Wie viele Tage Urlaub habe ich im Jahr?"]}},
        {"id": "warum", "q": "¿Por qué quiere trabajar con nosotros?", "r": "Me gusta trabajar con la gente y hablo tres idiomas.", "compat": ["ueber", "sprachen", "staerken", "erfahrung"], "mot": ["entrevista", "la"],
         "t": {"fr": ["Pourquoi voulez-vous travailler chez nous ?", "J'aime travailler avec les gens, et je parle trois langues."], "en": ["Why do you want to work for us?", "I like working with people, and I speak three languages."], "pt": ["Por que o senhor quer trabalhar conosco?", "Gosto de trabalhar com pessoas e falo três idiomas."], "de": ["Warum möchten Sie bei uns arbeiten?", "Ich arbeite gern mit Menschen, und ich spreche drei Sprachen."]}},
    ],
}
# le temps de travail dans la reponse : « in Vollzeit » / « la jornada completa » ; et traduit
UMF_REP = {"de": {"vollzeit": "Vollzeit", "teilzeit": "Teilzeit"}, "es": {"vollzeit": "la jornada completa", "teilzeit": "la media jornada"},
           "fr": {"vollzeit": "temps plein", "teilzeit": "temps partiel"}, "en": {"vollzeit": "full-time", "teilzeit": "part-time"},
           "pt": {"vollzeit": "tempo integral", "teilzeit": "meio período"}}
UMF_REP_FR_ES = {"vollzeit": "un temps plein", "teilzeit": "un mi-temps"}
UMF_REP_DE_ES = {"vollzeit": "Vollzeit", "teilzeit": "Teilzeit"}

# ---------------------------------------------------------------------------------------------------------------
# LE CONTRAT DE MARK (le poste sonnenweg). Chaque case : label, valeur, faux, la question, la phrase, le mot vise.
CONTRAT = {
    "de": {"titre": "Arbeitsvertrag", "mot": ["Arbeitsvertrag", "der"], "parties": ["Sonnenweg Reisen GmbH, Berlin (Arbeitgeber)", "Mark Garnier (Arbeitnehmer)"], "cases": [
        {"id": "beginn", "label": "Beginn", "v": "1. Dezember 2026", "faux": ["1. November 2026", "1. Januar 2027"], "mot": ["Beginn", "der"],
         "q": "Wann fängt Mark an?", "r": "am 1. Dezember", "rf": ["am 1. November", "am 1. Januar"], "ph": "Mark fängt am 1. Dezember an.", "vf": "Mark fängt {r} an.",
         "t": {"fr": "Mark commence le 1er décembre.", "en": "Mark starts on 1 December.", "pt": "Mark começa em 1º de dezembro."}},
        {"id": "probezeit", "label": "Probezeit", "v": "6 Monate", "faux": ["3 Monate", "12 Monate"], "mot": ["Probezeit", "die"],
         "q": "Wie lange dauert die Probezeit?", "r": "6 Monate", "rf": ["3 Monate", "12 Monate"], "ph": "Die Probezeit dauert 6 Monate.", "vf": "Die Probezeit dauert {r}.",
         "t": {"fr": "La période d'essai dure 6 mois.", "en": "The probation period lasts 6 months.", "pt": "O período de experiência dura 6 meses."}},
        {"id": "arbeitszeit", "label": "Arbeitszeit", "v": "40 Stunden pro Woche", "faux": ["20 Stunden pro Woche", "30 Stunden pro Woche"], "mot": ["Arbeitszeit", "die"],
         "q": "Wie viele Stunden pro Woche arbeitet Mark?", "r": "40 Stunden", "rf": ["20 Stunden", "30 Stunden"], "ph": "Mark arbeitet 40 Stunden pro Woche.", "vf": "Mark arbeitet {r} pro Woche.",
         "t": {"fr": "Mark travaille 40 heures par semaine.", "en": "Mark works 40 hours a week.", "pt": "Mark trabalha 40 horas por semana."}},
        {"id": "gehalt", "label": "Gehalt", "v": "3.000 € brutto im Monat", "faux": ["2.500 € brutto im Monat", "3.500 € brutto im Monat"], "mot": ["Gehalt", "das"],
         "q": "Wie viel verdient Mark?", "r": "3.000 € brutto im Monat", "rf": ["2.500 € brutto im Monat", "3.500 € brutto im Monat"], "ph": "Mark verdient 3.000 € brutto im Monat.", "vf": "Mark verdient {r}.",
         "t": {"fr": "Mark gagne 3\u202f000 € brut par mois.", "en": "Mark earns €3,000 gross a month.", "pt": "Mark ganha 3.000 € brutos por mês."}},
        {"id": "urlaub", "label": "Urlaub", "v": "28 Tage im Jahr", "faux": ["20 Tage im Jahr", "30 Tage im Jahr"], "mot": ["Urlaub", "der"],
         "q": "Wie viele Tage Urlaub hat Mark?", "r": "28 Tage im Jahr", "rf": ["20 Tage im Jahr", "30 Tage im Jahr"], "ph": "Mark hat 28 Tage Urlaub im Jahr.", "vf": "Mark hat {r} Urlaub.",
         "t": {"fr": "Mark a 28 jours de congé par an.", "en": "Mark has 28 days of holiday a year.", "pt": "Mark tem 28 dias de férias por ano."}}]},
    "es": {"titre": "Contrato de trabajo", "mot": ["contrato", "el"], "parties": ["Viajes Solano S.L., Madrid (empresa)", "Mark Garnier (trabajador)"], "cases": [
        {"id": "beginn", "label": "Fecha de inicio", "v": "1 de diciembre de 2026", "faux": ["1 de noviembre de 2026", "1 de enero de 2027"], "mot": ["empezar", "verbe"],
         "q": "¿Cuándo empieza Mark?", "r": "el 1 de diciembre", "rf": ["el 1 de noviembre", "el 1 de enero"], "ph": "Mark empieza el 1 de diciembre.", "vf": "Mark empieza {r}.",
         "t": {"fr": "Mark commence le 1er décembre.", "en": "Mark starts on 1 December.", "pt": "Mark começa em 1º de dezembro.", "de": "Mark fängt am 1. Dezember an."}},
        {"id": "probezeit", "label": "Período de prueba", "v": "2 meses", "faux": ["6 meses", "1 año"], "mot": ["período de prueba", "el"],
         "q": "¿Cuánto dura el período de prueba?", "r": "2 meses", "rf": ["6 meses", "1 año"], "ph": "El período de prueba dura 2 meses.", "vf": "El período de prueba dura {r}.",
         "t": {"fr": "La période d'essai dure 2 mois.", "en": "The probation period lasts 2 months.", "pt": "O período de experiência dura 2 meses.", "de": "Die Probezeit dauert 2 Monate."}},
        {"id": "arbeitszeit", "label": "Jornada", "v": "completa, 40 horas semanales", "faux": ["media, 20 horas semanales", "30 horas semanales"], "mot": ["jornada completa", "la"],
         "q": "¿Cuántas horas a la semana trabaja Mark?", "r": "40 horas", "rf": ["20 horas", "30 horas"], "ph": "Mark trabaja 40 horas a la semana.", "vf": "Mark trabaja {r} a la semana.",
         "t": {"fr": "Mark travaille 40 heures par semaine.", "en": "Mark works 40 hours a week.", "pt": "Mark trabalha 40 horas por semana.", "de": "Mark arbeitet 40 Stunden pro Woche."}},
        {"id": "gehalt", "label": "Sueldo", "v": "1.700 € brutos al mes", "faux": ["1.200 € brutos al mes", "2.100 € brutos al mes"], "mot": ["sueldo", "el"],
         "q": "¿Cuánto gana Mark?", "r": "1.700 € brutos al mes", "rf": ["1.200 € brutos al mes", "2.100 € brutos al mes"], "ph": "Mark gana 1.700 € brutos al mes.", "vf": "Mark gana {r}.",
         "t": {"fr": "Mark gagne 1\u202f700 € brut par mois.", "en": "Mark earns €1,700 gross a month.", "pt": "Mark ganha 1.700 € brutos por mês.", "de": "Mark verdient 1.700 € brutto im Monat."}},
        {"id": "urlaub", "label": "Vacaciones", "v": "30 días al año", "faux": ["15 días al año", "22 días al año"], "mot": ["vacaciones", "las"],
         "q": "¿Cuántos días de vacaciones tiene Mark?", "r": "30 días al año", "rf": ["15 días al año", "22 días al año"], "ph": "Mark tiene 30 días de vacaciones al año.", "vf": "Mark tiene {r} de vacaciones.",
         "t": {"fr": "Mark a 30 jours de congé par an.", "en": "Mark has 30 days of holiday a year.", "pt": "Mark tem 30 dias de férias por ano.", "de": "Mark hat 30 Tage Urlaub im Jahr."}}]},
}
# la phrase vraie/fausse « Mark hat 30 Tage im Jahr Urlaub. » a besoin de « 30 Tage » sans « im Jahr » : on garde la valeur telle quelle

# ---------------------------------------------------------------------------------------------------------------
# LES ACTIONS (les images). s : qui fait (cle de GENS) ; v : l'infinitif du corpus ; obj : apres le verbe ; pre : avant
# le verbe (« le » de « Lucia le ensena ») ; img : l'image (None : pas d'image) ; aussi_v : les verbes qui iraient
# aussi avec cet objet (jamais un leurre) ; verbe : False quand l'objet seul ne choisit pas le verbe ; t : traductions.
ACTIONS = {
    "de": [
        {"id": "suchen", "s": "mark", "v": "suchen", "obj": "eine Stelle", "img": "suchen", "aussi_v": ["anfangen"],
         "t": {"fr": "Mark cherche un emploi.", "en": "Mark is looking for a job.", "pt": "Mark procura um emprego."}},
        {"id": "schreiben", "s": "mark", "v": "schreiben", "obj": "seine Bewerbung", "img": "bewerbung", "aussi_v": ["schicken", "unterschreiben", "zeigen", "suchen", "vorstellen"],
         "t": {"fr": "Mark écrit sa candidature.", "en": "Mark writes his application.", "pt": "Mark escreve a sua candidatura."}},
        {"id": "schicken", "s": "mark", "v": "schicken", "obj": "seinen Lebenslauf", "img": None, "aussi_v": ["schreiben", "zeigen", "unterschreiben", "suchen", "vorstellen"],
         "t": {"fr": "Mark envoie son CV.", "en": "Mark sends his CV.", "pt": "Mark envia o seu currículo."}},
        {"id": "bewerben", "s": "mark", "v": "sich bewerben", "obj": "um die Stelle", "img": None, "aussi_v": [], "verbe": False,
         "t": {"fr": "Mark pose sa candidature pour le poste.", "en": "Mark applies for the job.", "pt": "Mark se candidata à vaga."}},
        {"id": "vorstellen_sich", "s": "mark", "v": "sich vorstellen", "obj": "bei Frau Schneider", "img": "gespraech", "aussi_v": [], "verbe": False,
         "t": {"fr": "Mark passe un entretien chez Mme Schneider.", "en": "Mark has an interview with Ms Schneider.", "pt": "Mark faz uma entrevista com a Sra. Schneider."}},
        {"id": "unterschreiben", "s": "mark", "v": "unterschreiben", "obj": "den Arbeitsvertrag", "img": "unterschreiben", "aussi_v": ["zeigen", "schicken", "schreiben", "suchen", "vorstellen"],
         "t": {"fr": "Mark signe le contrat de travail.", "en": "Mark signs the employment contract.", "pt": "Mark assina o contrato de trabalho."}},
        {"id": "anfangen", "s": "mark", "v": "anfangen", "obj": "am Montag", "img": None, "aussi_v": [], "verbe": False,
         "t": {"fr": "Mark commence lundi.", "en": "Mark starts on Monday.", "pt": "Mark começa na segunda-feira."}},
        {"id": "begruessen", "s": "chef", "v": "begrüßen", "obj": "Mark", "img": "begruessen", "aussi_v": [], "verbe": False,
         "t": {"fr": "Mme Schneider accueille Mark.", "en": "Ms Schneider welcomes Mark.", "pt": "A Sra. Schneider recebe o Mark."}},
        {"id": "vorstellen", "s": "chef", "v": "vorstellen", "obj": "Mark die Kollegen", "img": "kollegen", "aussi_v": ["zeigen"],
         "t": {"fr": "Mme Schneider présente ses collègues à Mark.", "en": "Ms Schneider introduces Mark to his colleagues.", "pt": "A Sra. Schneider apresenta os colegas ao Mark."}},
        {"id": "kennenlernen", "s": "mark", "v": "kennenlernen", "obj": "seine Kollegen", "img": None, "aussi_v": ["begrüßen", "anrufen", "suchen", "zeigen", "vorstellen"],
         "t": {"fr": "Mark fait la connaissance de ses collègues.", "en": "Mark meets his colleagues.", "pt": "Mark conhece os colegas."}},
        {"id": "zeigen", "s": "f", "v": "zeigen", "obj": "Mark seinen Schreibtisch", "img": "arbeitsplatz", "aussi_v": [],
         "t": {"fr": "Lisa montre son bureau à Mark.", "en": "Lisa shows Mark his desk.", "pt": "A Lisa mostra a mesa ao Mark."}},
        {"id": "arbeiten", "s": "mark", "v": "arbeiten", "obj": "im Kundenservice", "img": "arbeiten", "aussi_v": ["anrufen"],
         "t": {"fr": "Mark travaille au service client.", "en": "Mark works in customer service.", "pt": "Mark trabalha no atendimento ao cliente."}},
        {"id": "essen", "s": "mark", "v": "essen", "obj": "mit den Kollegen in der Kantine", "img": "kantine", "aussi_v": ["arbeiten"],
         "t": {"fr": "Mark mange avec ses collègues à la cantine.", "en": "Mark eats with his colleagues in the canteen.", "pt": "Mark come com os colegas no refeitório."}},
        {"id": "krankmelden", "s": "mark", "v": "krankmelden", "obj": "heute", "img": "krank", "aussi_v": [], "verbe": False,
         "t": {"fr": "Mark se déclare malade aujourd'hui.", "en": "Mark calls in sick today.", "pt": "Mark avisa que está doente hoje."}},
        {"id": "anrufen", "s": "mark", "v": "anrufen", "obj": "seine Chefin", "img": "krank", "aussi_v": ["begrüßen", "kennenlernen", "zeigen", "suchen", "vorstellen"],
         "t": {"fr": "Mark appelle sa cheffe.", "en": "Mark calls his boss.", "pt": "Mark liga para a chefe."}},
        {"id": "verdienen", "s": "mark", "v": "verdienen", "obj": "3.000 Euro im Monat", "img": None, "aussi_v": ["schicken"],
         "t": {"fr": "Mark gagne 3\u202f000 euros par mois.", "en": "Mark earns 3,000 euros a month.", "pt": "Mark ganha 3.000 euros por mês."}},
    ],
    "es": [
        {"id": "suchen", "s": "mark", "v": "buscar", "obj": "trabajo", "img": "suchen", "aussi_v": ["tener", "solicitar", "empezar"],
         "t": {"fr": "Mark cherche du travail.", "en": "Mark is looking for work.", "pt": "Mark procura trabalho.", "de": "Mark sucht Arbeit."}},
        {"id": "schreiben", "s": "mark", "v": "escribir", "obj": "su carta de presentación", "img": "bewerbung", "aussi_v": ["enviar", "firmar", "enseñar", "buscar", "presentar", "tener"],
         "t": {"fr": "Mark écrit sa lettre de motivation.", "en": "Mark writes his cover letter.", "pt": "Mark escreve a sua carta de apresentação.", "de": "Mark schreibt sein Anschreiben."}},
        {"id": "schicken", "s": "mark", "v": "enviar", "obj": "su currículum", "img": None, "aussi_v": ["escribir", "enseñar", "firmar", "buscar", "presentar", "tener"],
         "t": {"fr": "Mark envoie son CV.", "en": "Mark sends his CV.", "pt": "Mark envia o seu currículo.", "de": "Mark schickt seinen Lebenslauf."}},
        {"id": "bewerben", "s": "mark", "v": "solicitar", "obj": "el puesto", "img": None, "aussi_v": ["buscar", "tener", "ganar", "conocer", "empezar"],
         "t": {"fr": "Mark pose sa candidature pour le poste.", "en": "Mark applies for the job.", "pt": "Mark se candidata à vaga.", "de": "Mark bewirbt sich um die Stelle."}},
        {"id": "vorstellen_sich", "s": "mark", "v": "tener", "obj": "una entrevista con la señora Navarro", "img": "gespraech", "aussi_v": ["solicitar", "buscar", "empezar"],
         "t": {"fr": "Mark a un entretien avec Mme Navarro.", "en": "Mark has an interview with Ms Navarro.", "pt": "Mark tem uma entrevista com a Sra. Navarro.", "de": "Mark hat ein Vorstellungsgespräch bei Frau Navarro."}},
        {"id": "unterschreiben", "s": "mark", "v": "firmar", "obj": "el contrato", "img": "unterschreiben", "aussi_v": ["enseñar", "enviar", "escribir", "buscar", "tener", "conocer"],
         "t": {"fr": "Mark signe le contrat.", "en": "Mark signs the contract.", "pt": "Mark assina o contrato.", "de": "Mark unterschreibt den Vertrag."}},
        {"id": "anfangen", "s": "mark", "v": "empezar", "obj": "el lunes", "img": None, "aussi_v": [], "verbe": False,
         "t": {"fr": "Mark commence lundi.", "en": "Mark starts on Monday.", "pt": "Mark começa na segunda-feira.", "de": "Mark fängt am Montag an."}},
        {"id": "begruessen", "s": "chef", "v": "saludar", "obj": "a Mark", "img": "begruessen", "aussi_v": [], "verbe": False,
         "t": {"fr": "Mme Navarro accueille Mark.", "en": "Ms Navarro welcomes Mark.", "pt": "A Sra. Navarro recebe o Mark.", "de": "Frau Navarro begrüßt Mark."}},
        {"id": "vorstellen", "s": "chef", "v": "presentar", "obj": "a Mark a sus compañeros", "img": "kollegen", "aussi_v": ["saludar", "enseñar"],
         "t": {"fr": "Mme Navarro présente Mark à ses collègues.", "en": "Ms Navarro introduces Mark to her team.", "pt": "A Sra. Navarro apresenta o Mark aos colegas.", "de": "Frau Navarro stellt Mark die Kollegen vor."}},
        {"id": "kennenlernen", "s": "mark", "v": "conocer", "obj": "a sus compañeros", "img": None, "aussi_v": ["saludar", "llamar", "buscar", "presentar", "enseñar", "escribir", "tener", "ayudar"],
         "t": {"fr": "Mark fait la connaissance de ses collègues.", "en": "Mark meets his colleagues.", "pt": "Mark conhece os colegas.", "de": "Mark lernt seine Kollegen kennen."}},
        {"id": "zeigen", "s": "f", "v": "enseñar", "pre": "le", "obj": "su escritorio a Mark", "img": "arbeitsplatz", "aussi_v": ["presentar"],
         "t": {"fr": "Lucía montre son bureau à Mark.", "en": "Lucía shows Mark his desk.", "pt": "A Lucía mostra a mesa ao Mark.", "de": "Lucía zeigt Mark seinen Schreibtisch."}},
        {"id": "arbeiten", "s": "mark", "v": "trabajar", "obj": "en atención al cliente", "img": "arbeiten", "aussi_v": [],
         "t": {"fr": "Mark travaille au service client.", "en": "Mark works in customer service.", "pt": "Mark trabalha no atendimento ao cliente.", "de": "Mark arbeitet im Kundenservice."}},
        {"id": "essen", "s": "mark", "v": "comer", "obj": "con sus compañeros en el comedor", "img": "kantine", "aussi_v": ["trabajar"],
         "t": {"fr": "Mark mange avec ses collègues à la cantine.", "en": "Mark eats with his colleagues in the canteen.", "pt": "Mark come com os colegas no refeitório.", "de": "Mark isst mit den Kollegen in der Kantine."}},
        {"id": "anrufen", "s": "mark", "v": "llamar", "obj": "a su jefa", "img": "krank", "aussi_v": ["saludar", "conocer", "buscar", "escribir", "presentar", "enseñar", "enviar", "ayudar"],
         "t": {"fr": "Mark appelle sa cheffe.", "en": "Mark calls his boss.", "pt": "Mark liga para a chefe.", "de": "Mark ruft seine Chefin an."}},
        {"id": "verdienen", "s": "mark", "v": "ganar", "obj": "1.700 euros al mes", "img": None, "aussi_v": ["enviar", "tener"],
         "t": {"fr": "Mark gagne 1\u202f700 euros par mois.", "en": "Mark earns 1,700 euros a month.", "pt": "Mark ganha 1.700 euros por mês.", "de": "Mark verdient 1.700 Euro im Monat."}},
    ],
}
PRONOMS_REFLEXIFS = ("sich", "mich", "dich", "uns", "euch", "mir", "dir")
# deux images qui se ressemblent : la phrase de l'une n'est jamais un leurre de l'autre (la cheffe et Mark a la meme
# table ; la cheffe qui accueille Mark, la cheffe qui lui presente l'equipe)
IMG_PROCHES = [("gespraech", "unterschreiben"), ("begruessen", "kollegen"), ("arbeitsplatz", "arbeiten")]

# ---------------------------------------------------------------------------------------------------------------
# SIE OU DU, USTED OU TU : la cheffe vouvoie en entretien ; entre collegues, on se tutoie. v : l'infinitif ; sie / du :
# la question, ___ a la place du verbe ; t : leurs traductions.
REGISTRE = {
    "de": [
        {"v": "können", "sie": "___ Sie am Montag anfangen?", "du": "___ du mir kurz helfen?",
         "t": {"fr": ["Pouvez-vous commencer lundi ?", "Tu peux m'aider une minute ?"], "en": ["Can you start on Monday?", "Can you help me for a minute?"], "pt": ["O senhor pode começar na segunda?", "Você pode me ajudar um minutinho?"]}},
        {"v": "haben", "sie": "___ Sie Erfahrung im Kundenservice?", "du": "___ du heute Mittag Zeit?",
         "t": {"fr": ["Avez-vous de l'expérience au service client ?", "Tu as le temps ce midi ?"], "en": ["Do you have experience in customer service?", "Have you got time at lunchtime today?"], "pt": ["O senhor tem experiência em atendimento?", "Você tem tempo hoje na hora do almoço?"]}},
        {"v": "sprechen", "sie": "___ Sie auch Englisch?", "du": "___ du auch Französisch?",
         "t": {"fr": ["Parlez-vous aussi anglais ?", "Tu parles aussi français ?"], "en": ["Do you speak English too?", "Do you speak French too?"], "pt": ["O senhor também fala inglês?", "Você também fala francês?"]}},
        {"v": "kommen", "sie": "Woher ___ Sie?", "du": "Woher ___ du?",
         "t": {"fr": ["D'où venez-vous ?", "Tu viens d'où ?"], "en": ["Where are you from?", "Where are you from?"], "pt": ["De onde o senhor é?", "De onde você é?"]}},
        {"v": "arbeiten", "sie": "___ Sie gern im Team?", "du": "Seit wann ___ du hier?", "dir": "de",
         "t": {"fr": ["Aimez-vous travailler en équipe ?", "Tu travailles ici depuis quand ?"], "en": ["Do you like working in a team?", "How long have you been working here?"], "pt": ["O senhor gosta de trabalhar em equipe?", "Desde quando você trabalha aqui?"]}},
        {"v": "trinken", "sie": "___ Sie einen Kaffee?", "du": "___ du auch einen Kaffee?",
         "t": {"fr": ["Vous prenez un café ?", "Tu prends un café, toi aussi ?"], "en": ["Would you like a coffee?", "Do you want a coffee too?"], "pt": ["O senhor toma um café?", "Você também toma um café?"]}},
        {"v": "sein", "sie": "___ Sie Herr Garnier?", "du": "___ du der Neue?", "dir": "vers",
         "t": {"fr": ["Vous êtes M. Garnier ?", "C'est toi, le nouveau ?"], "en": ["Are you Mr Garnier?", "Are you the new guy?"], "pt": ["O senhor é o Sr. Garnier?", "Você é o novato?"]}},
        {"v": "essen", "sie": None, "du": "___ du heute mit uns in der Kantine?", "dir": "vers",
         "t": {"fr": [None, "Tu manges avec nous à la cantine aujourd'hui ?"], "en": [None, "Are you eating with us in the canteen today?"], "pt": [None, "Você vai almoçar com a gente no refeitório hoje?"]}},
    ],
    "es": [
        {"v": "poder", "sie": "¿___ usted empezar el lunes?", "du": "¿Me ___ ayudar un momento?",
         "t": {"fr": ["Pouvez-vous commencer lundi ?", "Tu peux m'aider une minute ?"], "en": ["Can you start on Monday?", "Can you help me for a minute?"], "pt": ["O senhor pode começar na segunda?", "Você pode me ajudar um minutinho?"], "de": ["Können Sie am Montag anfangen?", "Kannst du mir kurz helfen?"]}},
        {"v": "tener", "sie": "¿___ usted experiencia en atención al cliente?", "du": "¿___ tiempo para comer hoy?",
         "t": {"fr": ["Avez-vous de l'expérience au service client ?", "Tu as le temps de déjeuner aujourd'hui ?"], "en": ["Do you have experience in customer service?", "Have you got time for lunch today?"], "pt": ["O senhor tem experiência em atendimento?", "Você tem tempo para almoçar hoje?"], "de": ["Haben Sie Erfahrung im Kundenservice?", "Hast du heute Zeit zum Mittagessen?"]}},
        {"v": "hablar", "sie": "¿___ usted inglés?", "du": "¿___ francés también?",
         "t": {"fr": ["Parlez-vous anglais ?", "Tu parles aussi français ?"], "en": ["Do you speak English?", "Do you speak French too?"], "pt": ["O senhor fala inglês?", "Você também fala francês?"], "de": ["Sprechen Sie Englisch?", "Sprichst du auch Französisch?"]}},
        {"v": "ser", "sie": "¿De dónde ___ usted?", "du": "¿De dónde ___?",
         "t": {"fr": ["D'où êtes-vous ?", "Tu es d'où ?"], "en": ["Where are you from?", "Where are you from?"], "pt": ["De onde o senhor é?", "De onde você é?"], "de": ["Woher kommen Sie?", "Woher kommst du?"]}},
        {"v": "trabajar", "sie": "¿___ usted bien en equipo?", "du": "¿Desde cuándo ___ aquí?", "dir": "de",
         "t": {"fr": ["Travaillez-vous bien en équipe ?", "Tu travailles ici depuis quand ?"], "en": ["Do you work well in a team?", "How long have you been working here?"], "pt": ["O senhor trabalha bem em equipe?", "Desde quando você trabalha aqui?"], "de": ["Arbeiten Sie gut im Team?", "Seit wann arbeitest du hier?"]}},
        {"v": "querer", "sie": "¿___ usted un café?", "du": "¿___ un café?",
         "t": {"fr": ["Voulez-vous un café ?", "Tu veux un café ?"], "en": ["Would you like a coffee?", "Do you want a coffee?"], "pt": ["O senhor quer um café?", "Você quer um café?"], "de": ["Möchten Sie einen Kaffee?", "Möchtest du einen Kaffee?"]}},
        {"v": "comer", "sie": None, "du": "¿___ con nosotros hoy?", "dir": "vers",
         "t": {"fr": [None, "Tu manges avec nous aujourd'hui ?"], "en": [None, "Are you having lunch with us today?"], "pt": [None, "Você almoça com a gente hoje?"], "de": [None, "Isst du heute mit uns?"]}},
    ],
}
# qui parle a qui : le Sie / usted, la cheffe a Mark ; le du / tu, un collegue a Mark ou Mark a un collegue
REGISTRE_GENS = {"sie": [("chef", "mark")], "du": [("m", "mark"), ("f", "mark"), ("mark", "m"), ("mark", "f")]}
FRAGT = {"de": "{A} fragt {B}:", "es": "{A} pregunta a {B}:"}

# ---------------------------------------------------------------------------------------------------------------
# L'APPEL : se declarer malade. Le symptome (le mot du corpus, et la forme dans la phrase), puis les lignes, une a
# trou : (qui parle, texte avec ___, la reponse, les leurres, le mot vise).
SYMPTOMES = {
    "de": [["Fieber", "das", "Fieber"], ["Halsschmerzen", "die", "Halsschmerzen"], ["Kopfschmerzen", "die", "Kopfschmerzen"], ["Grippe", "die", "eine Grippe"], ["Erkältung", "die", "eine Erkältung"]],
    "es": [["fiebre", "la", "fiebre"], ["gripe", "la", "gripe"], ["tos", "la", "tos"], ["resfriado", "el", "un resfriado"]],
}
SYMPTOMES_T = {"Fieber": {"fr": "de la fièvre", "en": "a temperature", "pt": "febre"}, "Halsschmerzen": {"fr": "mal à la gorge", "en": "a sore throat", "pt": "dor de garganta"},
               "Kopfschmerzen": {"fr": "mal à la tête", "en": "a headache", "pt": "dor de cabeça"}, "Grippe": {"fr": "la grippe", "en": "flu", "pt": "gripe"},
               "Erkältung": {"fr": "un rhume", "en": "a cold", "pt": "um resfriado"},
               "fiebre": {"fr": "de la fièvre", "en": "a temperature", "pt": "febre", "de": "Fieber"}, "gripe": {"fr": "la grippe", "en": "flu", "pt": "gripe", "de": "eine Grippe"},
               "tos": {"fr": "de la toux", "en": "a cough", "pt": "tosse", "de": "Husten"}, "resfriado": {"fr": "un rhume", "en": "a cold", "pt": "um resfriado", "de": "eine Erkältung"}}


def appel(langue, sym):
    """Les lignes de l'appel ; chaque ligne : [qui, texte, trou ou None]. trou : [reponse, leurres, mot, consigne]."""
    s = sym[2]
    # le symptome est LU (ligne 2) : les trous viennent apres, et chaque appel a son symptome, donc ses questions
    if langue == "de":
        return [
            ["chef", "Sonnenweg Reisen, Schneider, guten Morgen.", None],
            ["mark", "Guten Morgen, Frau Schneider. Hier ist Mark Garnier.", None],
            ["mark", "Ich habe seit gestern " + s + ".", None],
            ["mark", "Es tut mir leid, ich bin ___.", ["krank", ["pünktlich", "fleißig", "teamfähig"], ["krank", "adjectif"]]],
            ["mark", "Ich kann heute nicht zur ___ kommen.", ["Arbeit", ["Bewerbung", "Probezeit", "Stelle"], ["Arbeit", "die"]]],
            ["chef", "Oh, das tut mir leid. Gehen Sie bitte zum ___.", ["Arzt", ["Chef", "Kollegen", "Kunden"], ["Arzt", "der"]]],
            ["chef", "Und schicken Sie mir bitte die ___.", ["Krankmeldung", ["Stellenanzeige", "Bewerbung", "Probezeit"], ["Krankmeldung", "die"]]],
            ["chef", "Gute ___, Herr Garnier!", ["Besserung", ["Reise", "Arbeit", "Nacht"], ["Besserung", "die"]]],
            ["mark", "Danke schön. Auf Wiederhören!", None],
        ]
    return [
        ["chef", "Viajes Solano, buenos días.", None],
        ["mark", "Buenos días, señora Navarro. Soy Mark Garnier.", None],
        ["mark", "Desde ayer tengo " + s + ".", None],
        ["mark", "Lo siento, estoy ___.", ["enfermo", ["contento", "puntual", "trabajador"], ["enfermo", "adjectif"]]],
        ["mark", "Hoy no puedo ir a ___.", ["trabajar", ["firmar", "solicitar", "buscar"], ["trabajar", "verbe"]]],
        ["chef", "Vaya al ___, por favor.", ["médico", ["jefe", "compañero", "cliente"], ["médico", "el"]]],
        ["chef", "Y mándeme la ___ médica, por favor.", ["baja", ["oferta", "carta", "entrevista"], ["baja", "la"]]],
        ["chef", "¡Que se mejore, Mark!", None],
        ["mark", "Gracias. ¡Hasta luego!", None],
    ]


# la traduction de la ligne a trou, une fois completee
def appel_t(langue, i, sym):
    T = {3: {"fr": "Je suis désolé, je suis malade.", "en": "I'm sorry, I'm ill.", "pt": "Sinto muito, estou doente.", "de": "Es tut mir leid, ich bin krank."},
         4: {"fr": "Je ne peux pas venir au travail aujourd'hui.", "en": "I can't come to work today.", "pt": "Não posso ir trabalhar hoje.", "de": "Ich kann heute nicht zur Arbeit kommen."},
         5: {"fr": "Oh, je suis désolée. Allez chez le médecin, s'il vous plaît.", "en": "Oh, I'm sorry. Please go to the doctor.", "pt": "Ah, sinto muito. Vá ao médico, por favor.", "de": "Oh, das tut mir leid. Gehen Sie bitte zum Arzt."},
         6: {"fr": "Et envoyez-moi l'arrêt de travail, s'il vous plaît.", "en": "And please send me the sick note.", "pt": "E me mande o atestado médico, por favor.", "de": "Und schicken Sie mir bitte die Krankmeldung."},
         7: {"fr": "Bon rétablissement, monsieur Garnier !", "en": "Get well soon, Mr Garnier!", "pt": "Melhoras, Sr. Garnier!", "de": "Gute Besserung, Herr Garnier!"}}
    if langue == "es":
        T[4] = {"fr": "Aujourd'hui, je ne peux pas aller travailler.", "en": "I can't go to work today.", "pt": "Hoje não posso ir trabalhar.", "de": "Heute kann ich nicht zur Arbeit gehen."}
        T[7] = {"fr": "Bon rétablissement, Mark !", "en": "Get well soon, Mark!", "pt": "Melhoras, Mark!", "de": "Gute Besserung, Mark!"}
    return T.get(i)


# ---------------------------------------------------------------------------------------------------------------
# QUI EST QUI : la description d'une personne, le mot du role ; leurres : les autres roles (jamais un role vrai aussi).
ROLES = {
    "de": [
        {"qui": "chef", "img": "begruessen", "d": ["Frau Schneider leitet das Team im Kundenservice. Sie ist Marks ___.", "Frau Schneider ist die Chefin von Mark, Jonas und Lisa. Sie ist die ___."], "r": "Chefin", "l": ["Chef", "Kollegin", "Kollege"], "mot": ["Chefin", "die"],
         "t": {"fr": "Mme Schneider est la cheffe de Mark.", "en": "Ms Schneider is Mark's boss.", "pt": "A Sra. Schneider é a chefe do Mark."}},
        {"qui": "m", "img": "kollegen", "d": ["Jonas arbeitet mit Mark im Team. Er ist Marks ___.", "Jonas und Mark arbeiten zusammen. Jonas ist ein ___ von Mark."], "r": "Kollege", "l": ["Kollegin", "Chefin", "Chef"], "mot": ["Kollege", "der"],
         "t": {"fr": "Jonas est un collègue de Mark.", "en": "Jonas is Mark's colleague.", "pt": "Jonas é colega do Mark."}},
        {"qui": "f", "img": "kollegen", "d": ["Lisa arbeitet mit Mark im Team. Sie ist Marks ___.", "Lisa und Mark arbeiten zusammen. Lisa ist eine ___ von Mark."], "r": "Kollegin", "l": ["Kollege", "Chefin", "Chef"], "mot": ["Kollegin", "die"],
         "t": {"fr": "Lisa est une collègue de Mark.", "en": "Lisa is Mark's colleague.", "pt": "Lisa é colega do Mark."}},
        {"qui": "mark", "img": "arbeiten", "d": ["Mark arbeitet seit Dezember bei Sonnenweg Reisen. Er ist ein neuer ___.", "Die Firma hat einen neuen ___: Mark."], "r": "Mitarbeiter", "l": ["Chefin", "Arbeitgeber", "Kunde"], "mot": ["Mitarbeiter", "der"],
         "t": {"fr": "Mark est un nouvel employé.", "en": "Mark is a new employee.", "pt": "Mark é um novo funcionário."}},
        {"qui": "firma", "img": None, "d": ["Sonnenweg Reisen bezahlt Marks Gehalt. Die Firma ist Marks ___.", "Mark arbeitet für Sonnenweg Reisen: Das ist sein ___."], "r": "Arbeitgeber", "l": ["Kollege", "Mitarbeiter", "Kunde"], "mot": ["Arbeitgeber", "der"],
         "t": {"fr": "Sonnenweg Reisen est l'employeur de Mark.", "en": "Sonnenweg Reisen is Mark's employer.", "pt": "A Sonnenweg Reisen é a empregadora do Mark."}},
        {"qui": "kunde", "img": "arbeiten", "d": ["Mark hilft am Telefon einem Mann, der eine Reise buchen möchte. Der Mann ist ein ___.", "Mark spricht am Telefon mit einer Frau, die eine Reise sucht. Sie ist eine ___."], "r": ["Kunde", "Kundin"], "l": ["Kollege", "Chef", "Mitarbeiter"], "mot": [["Kunde", "der"], ["Kundin", "die"]],
         "t": {"fr": ["L'homme est un client.", "La femme est une cliente."], "en": ["The man is a customer.", "The woman is a customer."], "pt": ["O homem é um cliente.", "A mulher é uma cliente."]}},
    ],
    "es": [
        {"qui": "chef", "img": "begruessen", "d": ["La señora Navarro dirige el equipo de atención al cliente. Es la ___ de Mark.", "La señora Navarro es la ___ de Mark, Jorge y Lucía."], "r": "jefa", "l": ["jefe", "compañera", "compañero"], "mot": ["jefa", "la"],
         "t": {"fr": "Mme Navarro est la cheffe de Mark.", "en": "Ms Navarro is Mark's boss.", "pt": "A Sra. Navarro é a chefe do Mark.", "de": "Frau Navarro ist Marks Chefin."}},
        {"qui": "m", "img": "kollegen", "d": ["Jorge trabaja con Mark en el mismo equipo. Es su ___.", "Jorge y Mark trabajan juntos. Jorge es un ___ de Mark."], "r": "compañero", "l": ["compañera", "jefa", "jefe"], "mot": ["compañero", "el"],
         "t": {"fr": "Jorge est un collègue de Mark.", "en": "Jorge is Mark's colleague.", "pt": "Jorge é colega do Mark.", "de": "Jorge ist ein Kollege von Mark."}},
        {"qui": "f", "img": "kollegen", "d": ["Lucía trabaja con Mark en el mismo equipo. Es su ___.", "Lucía y Mark trabajan juntos. Lucía es una ___ de Mark."], "r": "compañera", "l": ["compañero", "jefa", "jefe"], "mot": ["compañera", "la"],
         "t": {"fr": "Lucía est une collègue de Mark.", "en": "Lucía is Mark's colleague.", "pt": "Lucía é colega do Mark.", "de": "Lucía ist eine Kollegin von Mark."}},
        {"qui": "firma", "img": None, "d": ["Mark trabaja para Viajes Solano. Viajes Solano es su ___.", "Viajes Solano paga el sueldo de Mark: es su ___."], "r": "empresa", "l": ["jefa", "compañero", "cliente"], "mot": ["empresa", "la"],
         "t": {"fr": "Viajes Solano est l'entreprise de Mark.", "en": "Viajes Solano is Mark's company.", "pt": "A Viajes Solano é a empresa do Mark.", "de": "Viajes Solano ist Marks Firma."}},
        {"qui": "kunde", "img": "arbeiten", "d": ["Mark ayuda por teléfono a un señor que quiere reservar un viaje. El señor es un ___.", "Mark habla por teléfono con un señor que busca un viaje. Es un ___ de Viajes Solano."], "r": "cliente", "l": ["compañero", "jefe", "empresa"], "mot": ["cliente", "el"],
         "t": {"fr": "Le monsieur est un client.", "en": "The man is a customer.", "pt": "O senhor é um cliente.", "de": "Der Mann ist ein Kunde."}},
    ],
}

# ---------------------------------------------------------------------------------------------------------------
# SER OU ESTAR (l'espagnol seulement) : une qualite (ser), un etat du moment ou un lieu (estar).
ESTAR = {  # l'etat du moment : [adjectif du corpus, forme f, image, traductions [m, f]]
    "enfermo":  ["enferma", "krank", {"fr": ["malade", "malade"], "en": ["ill", "ill"], "pt": ["doente", "doente"], "de": ["krank", "krank"]}, "hoy"],
    "nervioso": ["nerviosa", None, {"fr": ["nerveux", "nerveuse"], "en": ["nervous", "nervous"], "pt": ["nervoso", "nervosa"], "de": ["nervös", "nervös"]}, "antes de la entrevista"],
    "contento": ["contenta", None, {"fr": ["content", "contente"], "en": ["happy", "happy"], "pt": ["contente", "contente"], "de": ["zufrieden", "zufrieden"]}, "con su nuevo trabajo"],
    "cansado":  ["cansada", None, {"fr": ["fatigué", "fatiguée"], "en": ["tired", "tired"], "pt": ["cansado", "cansada"], "de": ["müde", "müde"]}, "después de ocho horas de trabajo"],
}
ESTAR_T = {"hoy": {"fr": " aujourd'hui", "en": " today", "pt": " hoje", "de": " heute"},
           "antes de la entrevista": {"fr": " avant l'entretien", "en": " before the interview", "pt": " antes da entrevista", "de": " vor dem Vorstellungsgespräch"},
           "con su nuevo trabajo": {"fr": " de son nouveau travail", "en": " with {=his|her} new job", "pt": " com o novo trabalho", "de": " mit der neuen Arbeit"},
           "después de ocho horas de trabajo": {"fr": " après huit heures de travail", "en": " after eight hours of work", "pt": " depois de oito horas de trabalho", "de": " nach acht Stunden Arbeit"}}
LIEUX_ESTAR = [["La oficina de Viajes Solano ___ en Madrid.", "está", ["oficina", "la"], {"fr": "Le bureau de Viajes Solano est à Madrid.", "en": "The Viajes Solano office is in Madrid.", "pt": "O escritório da Viajes Solano fica em Madri.", "de": "Das Büro von Viajes Solano ist in Madrid."}],
               ["La mesa de Mark ___ al lado de la ventana.", "está", ["escritorio", "el"], {"fr": "Le bureau de Mark est à côté de la fenêtre.", "en": "Mark's desk is next to the window.", "pt": "A mesa do Mark fica ao lado da janela.", "de": "Marks Schreibtisch steht neben dem Fenster."}],
               ["Viajes Solano ___ una empresa de viajes.", "es", ["empresa", "la"], {"fr": "Viajes Solano est une entreprise de voyages.", "en": "Viajes Solano is a travel company.", "pt": "A Viajes Solano é uma empresa de viagens.", "de": "Viajes Solano ist ein Reiseunternehmen."}],
               ["La señora Navarro ___ la jefa de Mark.", "es", ["jefa", "la"], {"fr": "Mme Navarro est la cheffe de Mark.", "en": "Ms Navarro is Mark's boss.", "pt": "A Sra. Navarro é a chefe do Mark.", "de": "Frau Navarro ist Marks Chefin."}],
               ["Jorge ___ el compañero de Mark.", "es", ["compañero", "el"], {"fr": "Jorge est le collègue de Mark.", "en": "Jorge is Mark's colleague.", "pt": "Jorge é o colega do Mark.", "de": "Jorge ist Marks Kollege."}]]

# ---------------------------------------------------------------------------------------------------------------
# LES DOCUMENTS (images sans texte) et ce qui est clairement faux pour chacun
DOCS = {
    "de": {"zeitung": ["Stellenanzeige", "die", {"fr": "l'offre d'emploi", "en": "the job advert", "pt": "o anúncio de emprego"}],
           "lebenslauf": ["Lebenslauf", "der", {"fr": "le CV", "en": "the CV", "pt": "o currículo"}],
           "anschreiben": ["Anschreiben", "das", {"fr": "la lettre de motivation", "en": "the cover letter", "pt": "a carta de apresentação"}],
           "arbeitsvertrag": ["Arbeitsvertrag", "der", {"fr": "le contrat de travail", "en": "the employment contract", "pt": "o contrato de trabalho"}]},
    "es": {"zeitung": ["oferta de empleo", "la", {"fr": "l'offre d'emploi", "en": "the job advert", "pt": "o anúncio de emprego", "de": "die Stellenanzeige"}],
           "lebenslauf": ["currículum", "el", {"fr": "le CV", "en": "the CV", "pt": "o currículo", "de": "der Lebenslauf"}],
           "anschreiben": ["carta de presentación", "la", {"fr": "la lettre de motivation", "en": "the cover letter", "pt": "a carta de apresentação", "de": "das Anschreiben"}],
           "arbeitsvertrag": ["contrato", "el", {"fr": "le contrat de travail", "en": "the employment contract", "pt": "o contrato de trabalho", "de": "der Arbeitsvertrag"}]},
}

# ---------------------------------------------------------------------------------------------------------------
# LES MOTS ABSENTS DU CORPUS, a ajouter PAR PAIRES (allemand et espagnol) avec l'accord de Jacques. En attendant, l'app
# les tient « hors jeu ». Leur traduction ici, pour la ligne sous le mot.
AJOUTS_TRAD = {
    "de": {"Stellenanzeige": {"fr": "offre d'emploi", "en": "job advert", "tr": "iş ilanı", "uk": "оголошення про вакансію", "fa": "آگهی استخدام", "ar": "إعلان وظيفة", "pt": "anúncio de emprego", "pl": "ogłoszenie o pracę", "ru": "объявление о вакансии"},
           "Minijob": {"fr": "mini-job (petit emploi)", "en": "mini-job", "tr": "mini iş", "uk": "мініджоб (підробіток)", "fa": "مینی‌جاب (کار کوتاه‌مدت)", "ar": "عمل صغير (ميني جوب)", "pt": "minijob (bico)", "pl": "minijob (praca dorywcza)", "ru": "миниджоб (подработка)"},
           "Arbeitszeit": {"fr": "temps de travail", "en": "working hours", "tr": "çalışma süresi", "uk": "робочий час", "fa": "ساعت کاری", "ar": "ساعات العمل", "pt": "jornada de trabalho", "pl": "czas pracy", "ru": "рабочее время"},
           "Krankmeldung": {"fr": "arrêt maladie", "en": "sick note", "tr": "hastalık bildirimi", "uk": "лікарняний", "fa": "گواهی بیماری", "ar": "إشعار المرض", "pt": "atestado médico", "pl": "zwolnienie lekarskie", "ru": "больничный"},
           "teamfähig": {"fr": "qui a l'esprit d'équipe", "en": "a good team player", "tr": "takım çalışmasına yatkın", "uk": "командний", "fa": "اهل کار گروهی", "ar": "قادر على العمل ضمن فريق", "pt": "bom de equipe", "pl": "umiejący pracować w zespole", "ru": "умеющий работать в команде"}},
    "es": {"currículum": {"fr": "CV", "en": "CV", "pt": "currículo", "ar": "السيرة الذاتية", "de": "Lebenslauf"},
           "carta de presentación": {"fr": "lettre de motivation", "en": "cover letter", "pt": "carta de apresentação", "ar": "رسالة تقديم", "de": "Anschreiben"},
           "oferta de empleo": {"fr": "offre d'emploi", "en": "job offer", "pt": "oferta de emprego", "ar": "عرض عمل", "de": "Stellenangebot"},
           "jornada completa": {"fr": "temps plein", "en": "full-time", "pt": "tempo integral", "ar": "دوام كامل", "de": "Vollzeit"},
           "media jornada": {"fr": "mi-temps", "en": "part-time (half days)", "pt": "meio período", "ar": "نصف دوام", "de": "Teilzeit (halbtags)"},
           "período de prueba": {"fr": "période d'essai", "en": "probation period", "pt": "período de experiência", "ar": "فترة التجربة", "de": "Probezeit"},
           "jefa": {"fr": "cheffe, patronne", "en": "boss (woman)", "pt": "chefe (mulher)", "ar": "مديرة", "de": "Chefin"},
           "compañera": {"fr": "collègue (femme)", "en": "colleague (woman)", "pt": "colega (mulher)", "ar": "زميلة", "de": "Kollegin"},
           "baja": {"fr": "arrêt maladie", "en": "sick leave", "pt": "licença médica", "ar": "إجازة مرضية", "de": "Krankschreibung"}},
}

# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES (4:3, aucun texte). source : les references (Mark, la cheffe et son bureau, ses pieces). src : une image
# deja publiee, reprise telle quelle (rien a payer). ESSAI : la planche d'essai (6 images, 0,90 $).
MARK = ("The young man is the same man as in the first reference picture: exactly the same face, the same curly dark brown "
        "hair, the same age and build. ")
TENUE = "He wears a light blue button-down shirt under an unstructured dark navy jacket, no tie, navy trousers. "
CHEFFE = ("The woman is exactly the same woman as in the second reference picture: the same face, the same shoulder-length "
          "blonde hair, the same age (her forties), the same beige tweed blazer over a white blouse. ")
BUREAU = ("The place is the same bright office as in the second reference picture: white walls, tall white windows, light "
          "wooden furniture. ")
EQUIPE = ("The two colleagues: a man in his early thirties with short brown hair, a short brown beard and black-framed glasses, "
          "in a dark green sweater; and a woman in her late twenties with long black hair in a ponytail, in a mustard-yellow "
          "cardigan over a white top. ")
PHOTO = (" A photorealistic photograph, natural light, natural colours, 4:3 landscape format. ABSOLUTELY NO readable text, "
         "no letters, no numbers, no logos, no signs, no captions, no watermark anywhere in the picture: every paper, screen and "
         "badge is blank or blurred, computer screens are turned away from the camera. Hands: five fingers each, natural. ")
IMAGES = {
    "suchen":      {"source": "Mark+Cuisine", "prompt": MARK + "He sits at the light wooden kitchen table of the second reference picture (the same small bright kitchen), in a plain grey knit sweater, a mug of coffee beside him; he reads the job advertisement pages of a printed newspaper spread out on the table and circles one small advert with a pen, concentrated. The newspaper print is blurred and cannot be read. Seen at three quarters, from the waist up."},
    "bewerbung":   {"source": "Mark+Salon", "prompt": MARK + "He sits at the small desk by the big window of the living room of the second reference picture (the same room), in a plain grey knit sweater, his laptop open with the screen turned away from the camera; he holds a printed one-page CV with a small passport photo of himself in the top corner and checks it, a pen in his other hand. The text on the paper is blurred and cannot be read. Seen at three quarters, from the waist up."},
    "gespraech":   {"source": "Mark+Bureau", "prompt": MARK + CHEFFE + BUREAU + "A job interview: he sits at the light wooden table opposite her; " + TENUE + "She holds his printed CV (blurred, unreadable) and listens with a friendly smile while he answers, gesturing slightly with one open hand, a little nervous but confident. A glass of water on the table. Seen from the side, both from the waist up."},
    "begruessen":  {"source": "Mark+Bureau", "prompt": MARK + CHEFFE + "His first day at work: in the bright entrance area of the same company (white walls, tall white windows, light wooden floor, a coat rack and a green plant), she welcomes him with a warm handshake and a big smile; " + TENUE + "A small backpack on his shoulder, happy and a bit shy. Seen from the side, both from the knees up."},
    "kollegen":    {"source": "Mark+Bureau", "prompt": MARK + CHEFFE + EQUIPE + "In a bright open-plan office of the same company (tall white windows, light wooden desks with computer screens turned away), she introduces him to his two new colleagues, who stand by their desks; " + TENUE + "The woman colleague shakes his hand with a smile, the bearded man waves hello. All four are smiling. Seen from the front at three quarters, all four from the waist up, nobody else in the room."},
    "krank":       {"source": "Mark+Chambre", "prompt": MARK + "Early morning in the simple bedroom of the second reference picture (white walls, wooden bed, white curtains): he is ill, pale with a red nose and tired eyes, sitting up in bed under the duvet in a plain grey T-shirt; he holds his mobile phone to his ear and talks with an apologetic face. On the bedside table: a box of tissues, a glass of water and a thermometer. Seen from the side, from the waist up."},
    "arbeitsplatz": {"source": "Mark+Equipe", "prompt": MARK + "The woman with the long black ponytail and the mustard-yellow cardigan of the second reference picture (the same woman) shows him his new desk in the same bright open-plan office: a light wooden desk with a computer (screen turned away from the camera), a telephone headset, a notebook and a small green plant. She points at the desk with a smile, he looks pleased. " + TENUE + "Seen at three quarters, both from the waist up."},
    "arbeiten":    {"source": "Mark+Equipe", "prompt": MARK + "He sits at his desk in the same bright open-plan office as in the second reference picture, wearing a telephone headset with a small microphone, talking to a customer with a friendly smile and typing on a keyboard; the computer screen is turned away from the camera. " + TENUE.replace("He wears", "He wears, jacket off,").replace("under an unstructured dark navy jacket, no tie", "with the sleeves rolled up") + "Behind him, slightly out of focus, the bearded colleague with glasses works at his own desk. Seen at three quarters, from the waist up."},
    "kantine":     {"source": "Mark+Equipe", "prompt": MARK + "Lunch break in the bright company canteen (long light wooden tables, big windows): he eats with the two colleagues of the second reference picture (the man with the short beard and glasses in the dark green sweater, the woman with the long black ponytail in the mustard-yellow cardigan); trays with plates of pasta and salad, glasses of water; they talk and laugh. He wears a light blue button-down shirt, jacket off. Seen from the front at three quarters, the three from the waist up."},
    "lebenslauf":  {"source": "Mark", "prompt": "Close-up of a printed one-page CV lying on a light wooden desk: a small passport-style photo of the young man of the reference picture (curly dark brown hair, friendly face) in the top right corner, a few short blurred headings and blocks of blurred grey lines that cannot be read; a ballpoint pen beside it. Seen from above at a slight angle."},
    "anschreiben": {"prompt": "Close-up of a printed one-page formal letter lying half out of an open white envelope on a light wooden desk: a blurred address block at the top, three blurred paragraphs and a handwritten signature in blue ink at the bottom; nothing can be read. Seen from above at a slight angle."},
    "zeitung":     {"prompt": "Close-up of the job advertisement page of a printed newspaper lying on a table: many small rectangular adverts in columns with thin frames, all the print blurred and unreadable, one small advert circled with a red pen, the edge of a coffee cup in a corner. Seen from above."},
    "unterschreiben": {"src": "demarches/unterschreiben.webp"},
    "arbeitsvertrag": {"src": "demarches/arbeitsvertrag.webp"},
}
ESSAI = ["suchen", "bewerbung", "gespraech", "begruessen", "kollegen", "krank"]


def img_src(i):
    return IMAGES[i].get("src") or "travail/" + i + ".webp"


# ---------------------------------------------------------------------------------------------------------------
# LE CORPUS
def corpus_noms(langue):
    f = "themes.json" if langue == "de" else "espanol/datos/temas.json"
    out = {}
    for t in json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))["themes"]:
        for m in t["mots"]:
            out.setdefault((m["mot"], m.get("genre")), m)
    return out


def corpus_liste(fichier, cle):
    out = {}
    for niv, l in json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8")).items():
        if isinstance(l, list):
            for e in l:
                out.setdefault(e.get(cle) or e.get("mot"), e)
    return out


class Corpus:
    def __init__(self, langue):
        self.langue = langue
        self.noms = corpus_noms(langue)
        self.verbes = corpus_liste("verbe.json" if langue == "de" else "espanol/datos/verbos.json", "infinitif")
        self.adjs = corpus_liste("adjectif.json" if langue == "de" else "espanol/datos/adjetivos.json", "mot")

    def entree(self, mot, genre=None, cat=None):
        if cat == "verbe":
            return self.verbes.get(mot)
        if cat == "adjectif":
            return self.adjs.get(mot)
        return self.noms.get((mot, genre))

    def glose(self, mot, genre=None, cat=None):
        e = self.entree(mot, genre, cat)
        if e:
            return {l: e.get("traduction" if l == "fr" else "traduction_" + l) for l in LANGUES[self.langue]}
        if mot in AJOUTS_TRAD[self.langue]:
            return dict(AJOUTS_TRAD[self.langue][mot])
        return None

    def er(self, v):
        """La forme de la 3e personne, en trois morceaux : [verbe, pronom reflechi, particule] (« meldet », « sich », « krank »)."""
        e = self.verbes[v]
        f = e["praesens"]["er_sie_es"].split()
        if self.langue == "es":
            return [e["praesens"]["er_sie_es"], "", ""]
        verbe, reste = f[0], f[1:]
        pron = ""
        if reste and reste[0] in PRONOMS_REFLEXIFS:
            pron, reste = reste[0], reste[1:]
        if not pron and (e.get("reflexiv") or v.startswith("sich ")):
            pron = "sich"
        return [verbe, pron, " ".join(reste)]


def w(mot, genre=None, cat=None):
    d = {"mot": mot}
    if cat:
        d["cat"] = cat
    elif genre:
        d["genre"] = genre
    return d


def wl(paire):
    """[mot, genre] ou [mot, "verbe"|"adjectif"] -> le mot vise."""
    if paire is None:
        return None
    m, g = paire
    return w(m, cat=g) if g in ("verbe", "adjectif") else w(m, g)


def espaces(s):
    return re.sub(r" ([.,!?:])", r"\1", re.sub(r"\s+", " ", s)).strip()


# ---------------------------------------------------------------------------------------------------------------
# LA FABRIQUE DES QUESTIONS. Chaque question : s (sorte), c (consigne), av (le papier ou l'image montre avant), e (enonce,
# ___ = le trou), r (reponse), l (reserve de leurres), n (combien en montrer), ph (la phrase juste, dite apres), t (sa
# traduction par langue), w (le mot vise), d (le mot a redire), tc (traductions des choix, pour « tu as choisi »).
def fabriquer(langue):
    C = Corpus(langue)
    ES = langue == "es"
    tls = TL[langue]
    Q = []

    deja = set()

    def ajouter(**q):
        q.setdefault("n", 3)
        q["l"] = [x for x in dict.fromkeys(q["l"]) if x != q["r"]]
        cle = (q["s"], q["e"], json.dumps(q["av"], ensure_ascii=False), q["r"])
        if cle in deja:
            return                                         # la meme question, fabriquee deux fois : une seule
        deja.add(cle)
        Q.append(q)
        if q["s"] in ("quoi", "serEstar", "ordre"):
            # vrai ou faux : la meme phrase, juste ou avec une autre (l'action d'une autre image ; ser au lieu d'estar)
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            juste = q["ph"]
            faux = q["l"][0] if q["s"] in ("quoi", "ordre") else q["e"].replace("___", q["l"][0])
            for e_, r_ in ((juste, V), (faux, F)):
                c2 = ("vraifaux", e_, json.dumps(q["av"], ensure_ascii=False), r_)
                if c2 not in deja:
                    deja.add(c2)
                    Q.append(dict(q, s="vraifaux", c="c_vraifauxPhrase", e=e_, r=r_, l=[F if r_ == V else V], n=1, vf=True, liste=False,
                                  req=q["s"] == "quoi"))      # req : sans son image, la question n'a pas de sens

    def tr(d, **v):
        out = {}
        for l in tls:
            s = d.get(l) if isinstance(d, dict) else None
            if s is None:
                continue
            for k, x in v.items():
                s = s.replace("{" + k + "}", x[l] if isinstance(x, dict) else x)
            out[l] = s
        return out

    ads = ANNONCES[langue]
    U = UMFANG[langue]
    # 1. LES ANNONCES : le temps de travail (la case cachee), puis les cases lues
    for a in ads:
        u = U[a["umfang"]]
        ajouter(s="umfang", c="c_umfang", av=["annonce", a["id"], "umfang", "cache"], e=("¿Jornada completa, media jornada o por horas?" if ES else "Vollzeit, Teilzeit oder Minijob?"),
                r=u["wort"], l=[U[k]["wort"] for k in U if k != a["umfang"]], n=2, ph=u["satz"], t={l: (UMFANG_T_ES if ES else UMFANG_T)[a["umfang"]][l] for l in tls},
                w=w(u["mot"], u["genre"]), d=u["wort"])
        # les heures
        h = lambda n: ("%d horas" if ES else "%d Stunden") % n
        autres_h = sorted({x["stunden"] for x in ads if x["stunden"] != a["stunden"]} | {a["stunden"] + 10, max(4, a["stunden"] - 10)} - {a["stunden"]})
        ajouter(s="annonce", c="c_annonce", av=["annonce", a["id"], "stunden"], e=("¿Cuántas horas a la semana se trabaja?" if ES else "Wie viele Stunden pro Woche arbeitet man?"),
                r=h(a["stunden"]), l=[h(x) for x in autres_h], ph=("Se trabajan %d horas a la semana." if ES else "Man arbeitet %d Stunden pro Woche.") % a["stunden"],
                t=tr({"fr": "On travaille %d heures par semaine." % a["stunden"], "en": "You work %d hours a week." % a["stunden"], "pt": "Trabalha-se %d horas por semana." % a["stunden"], "de": "Man arbeitet %d Stunden pro Woche." % a["stunden"]}),
                w=w("hora", "la") if ES else w("Arbeitszeit", "die"), d=("hora" if ES else "die Arbeitszeit"))
        # le salaire : le mois (Gehalt / sueldo), l'heure (Lohn / ganar)
        x, par = a["lohn"]
        autres_l = [lohn(y[0], y[1], langue) for y in {tuple(b["lohn"]) for b in ads if b["lohn"][1] == par and b["lohn"] != a["lohn"]}]
        autres_l += [lohn(x + (500 if par == "monat" else 2), par, langue), lohn(x - (500 if par == "monat" else 2), par, langue)]
        r = lohn(x, par, langue)
        ajouter(s="annonce", c="c_annonce", av=["annonce", a["id"], "lohn"], e=("¿Cuánto se gana?" if ES else "Wie viel verdient man?"), r=r, l=autres_l,
                ph=("Se gana " + r + "." if ES else "Man verdient " + r + "."),
                t={l: {"fr": "On gagne ", "en": "You earn ", "pt": "Ganha-se ", "de": "Man verdient "}[l] + lohn(x, par, "de" if l == "de" else l) + "." for l in tls},
                w=(w("sueldo", "el") if par == "monat" else w("ganar", cat="verbe")) if ES else (w("Gehalt", "das") if par == "monat" else w("Lohn", "der")),
                d=(("el sueldo" if par == "monat" else "ganar") if ES else ("das Gehalt" if par == "monat" else "der Lohn")))
        # le debut
        b = BEGINN[a["beginn"]]
        ajouter(s="annonce", c="c_annonce", av=["annonce", a["id"], "beginn"], e=("¿Cuándo se empieza a trabajar?" if ES else "Wann fängt man an?"),
                r=b[langue][1], l=[BEGINN[k][langue][1] for k in BEGINN if k != a["beginn"]],
                ph=("Se empieza a trabajar " + b["es"][1] + "." if ES else "Man fängt " + b["de"][1] + " an."),
                t={l: {"fr": "On commence " + b["fr"][1] + ".", "en": "You start " + b["en"][1] + ".", "pt": "O trabalho começa " + b["pt"][1] + ".", "de": "Man fängt " + b["de"][1] + " an."}[l] for l in tls},
                w=w("empezar", cat="verbe") if ES else w("anfangen", cat="verbe"), d=("empezar" if ES else "anfangen"))
        # a qui ecrire
        k = a["kontakt"]
        ajouter(s="annonce", c="c_annonce", av=["annonce", a["id"], "kontakt"], e=("¿A quién se envía el currículum?" if ES else "An wen schickt man die Bewerbung?"),
                r=contact(k, langue, "akk"), l=[contact(o["kontakt"], langue, "akk") for o in ads if o["id"] != a["id"]],
                ph=("Se envía el currículum " + contact(k, "es", "akk") + "." if ES else "Man schickt die Bewerbung an " + contact(k, "de", "akk") + "."),
                t={l: ({"fr": "On envoie le CV à ", "en": "You send your CV to ", "pt": "O currículo vai para ", "de": "Man schickt den Lebenslauf an "} if ES else
                       {"fr": "On envoie la candidature à ", "en": "You send the application to ", "pt": "A candidatura vai para "})[l]
                       + (contact(k, "de", "akk") if l == "de" else contact(k, l)) + "." for l in tls},
                w=w("currículum", "el") if ES else w("Bewerbung", "die"), d=("el currículum" if ES else "die Bewerbung"))
        # ce que l'annonce demande
        for q in a["erwartet"]:
            hors = [x for x in QUALITES[langue] if x not in a["erwartet"]]
            ajouter(s="annonce", c="c_annonce", av=["annonce", a["id"], "erwartet"], e=("¿Cómo hay que ser, según la oferta?" if ES else "Was steht in der Anzeige? Man soll … sein."),
                    r=q, l=hors, ph=("Hay que ser " + q + "." if ES else "Man soll " + q + " sein."),
                    t={l: {"fr": "Il faut être " + accord(QUALITES[langue][q]["t"]["fr"][0], "m") + ".", "en": "You need to be " + QUALITES[langue][q]["t"]["en"][0] + ".",
                           "pt": "É preciso ser " + accord(QUALITES[langue][q]["t"]["pt"][0], "m") + ".", "de": "Man soll " + QUALITES[langue][q]["t"].get("de", [""])[0] + " sein."}[l]
                       if not QUALITES[langue][q]["t"][l][0].startswith("!") else {"fr": "Il faut avoir l'esprit d'équipe.", "pt": "É preciso saber trabalhar em equipe."}[l] for l in tls},
                    w=w(q, cat="adjectif"), d=q, groupe=a["id"])
        # ou travaille le nouveau
        ajouter(s="annonce", c="c_annonce", av=["annonce", a["id"], "firma"], e=("¿Dónde trabaja " + a["neu"].replace("El ", "el ") + "?" if ES else "Wo arbeitet " + a["neu"].replace("Der ", "der ") + "?"),
                r=a["ou"], l=[o["ou"] for o in ads if o["id"] != a["id"]], ph=a["neu"] + (" trabaja " if ES else " arbeitet ") + a["ou"] + ".",
                t={l: a["t"][l][1] for l in tls}, w=w(a["mot"], a["genre"]), d=a["genre"] + " " + a["mot"])
    # vrai ou faux sur les annonces : la phrase d'une case avec la valeur d'une autre annonce
    for q in [q for q in Q if q["s"] == "annonce" and q["av"][2] in ("stunden", "lohn", "beginn", "kontakt", "firma")]:
        for faux in q["l"][:2]:
            phf = q["ph"].replace(q["r"], faux, 1)
            if phf == q["ph"]:
                continue
            ajouter(s="vraifaux", c="c_vraifauxAnnonce", av=q["av"], e=phf, r=("Falso" if ES else "Falsch"), l=[("Verdadero" if ES else "Richtig")], n=1, ph=q["ph"], t=q["t"], w=q["w"], d=q["d"], vf=True)
        ajouter(s="vraifaux", c="c_vraifauxAnnonce", av=q["av"], e=q["ph"], r=("Verdadero" if ES else "Richtig"), l=[("Falso" if ES else "Falsch")], n=1, ph=q["ph"], t=q["t"], w=q["w"], d=q["d"], vf=True)
    for a in ads:
        u = U[a["umfang"]]
        for k in U:
            ajouter(s="vraifaux", c="c_vraifauxAnnonce", av=["annonce", a["id"], "umfang", "cache"], e=U[k]["satz"], r=(("Verdadero" if ES else "Richtig") if k == a["umfang"] else ("Falso" if ES else "Falsch")),
                    l=[("Falso" if ES else "Falsch") if k == a["umfang"] else ("Verdadero" if ES else "Richtig")], n=1, ph=u["satz"], t={l: (UMFANG_T_ES if ES else UMFANG_T)[a["umfang"]][l] for l in tls},
                    w=w(u["mot"], u["genre"]), d=u["wort"], vf=True)

    # 2. LES QUALITES : ce que fait la personne -> la qualite
    QU = QUALITES[langue]
    for qk, qv in QU.items():
        for p in ("mark", "m", "f", "chef"):
            g = GENS[langue][p]["g"]
            P = gens(langue, p)
            e = cap(accord(qv["def"].replace("{P}", P), g))
            rep = adj(langue, qk, g)
            leurres = [adj(langue, x, g) for x in QU if x != qk and x not in qv["proches"] and qk not in QU[x]["proches"]]
            ph = cap(P) + (" es " if ES else " ist ") + rep + "."
            t = {}
            for l in tls:
                Pl = cap(gens(langue, p, l))
                vb = {"fr": " est ", "en": " is ", "pt": " é ", "de": " ist "}[l]; at = accord(qv["t"][l][0], g)
                t[l] = accord(qv["t"][l][1].replace("{P}", Pl), g) + " " + Pl + ((" " + at[1:]) if at.startswith("!") else vb + at) + "."
            ajouter(s="qualite", c="c_qualite", av=None, e=e + " " + (cap(P) + " es ___." if ES else cap(P) + " ist ___."), r=rep, l=leurres, ph=e + " " + ph, t=t,
                    w=w(qk, cat="adjectif"), d=rep)
            # vrai ou faux : la meme description, la bonne qualite ou une qualite clairement fausse
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            ajouter(s="vraifaux", c="c_vraifauxQualite", av=None, e=e + " " + ph, r=V, l=[F], n=1, ph=e + " " + ph, t=t, w=w(qk, cat="adjectif"), d=rep, vf=True)
            fx = leurres[(len(qk) + len(P)) % len(leurres)]
            ajouter(s="vraifaux", c="c_vraifauxQualite", av=None, e=e + " " + cap(P) + (" es " if ES else " ist ") + fx + ".", r=F, l=[V], n=1, ph=e + " " + ph, t=t, w=w(qk, cat="adjectif"), d=rep, vf=True)

    # 3. L'ENTRETIEN : la question du recruteur -> la reponse de Mark
    ENT = ENTRETIEN[langue]
    for aid in ("sonnenweg", "hotel"):
        a = next(x for x in ads if x["id"] == aid)
        k = a["kontakt"]
        rec = contact(k, langue, "n")
        b = BEGINN[a["beginn"]]
        mq = MARK_QUALITES[langue]
        paires = [(x, y) for x in mq for y in mq if x != y]
        for e in ENT:
            variantes = paires if "{a}" in e["r"] else [None]
            for pr in variantes:
                def rem(s, l):
                    if pr:
                        s = s.replace("{a}", pr[0] if l == langue else accord(QU[pr[0]]["t"][l][0], "m")).replace("{b}", pr[1] if l == langue else accord(QU[pr[1]]["t"][l][0], "m"))
                    s = s.replace("{am}", b[l][1] if l in b else "")
                    if l == "fr" and ES:
                        s = s.replace("{umf}", UMF_REP_FR_ES[a["umfang"]])
                    elif l == "de" and ES:
                        s = s.replace("{umf}", UMF_REP_DE_ES[a["umfang"]])
                    else:
                        s = s.replace("{umf}", UMF_REP[l][a["umfang"]] if a["umfang"] in UMF_REP[l] else "")
                    return s
                if "{umf}" in e["r"] and a["umfang"] not in UMF_REP[langue]:
                    continue
                rep = rem(e["r"], langue)
                autres = [x for x in ENT if x["id"] != e["id"] and x["id"] not in e["compat"] and e["id"] not in x["compat"]]
                leurres = []
                for x in autres:
                    if "{a}" in x["r"]:
                        x2 = x["r"].replace("{a}", mq[0]).replace("{b}", mq[1])
                    else:
                        x2 = x["r"]
                    leurres.append(rem(x2, langue))
                mot = wl(e["mot"]) if e["mot"] else (w(pr[0], cat="adjectif") if pr else wl(["Vollzeit", "die"] if not ES else ["jornada completa", "la"]))
                if e["id"] == "umfang":
                    u = U[a["umfang"]]
                    mot = w(u["mot"], u["genre"])
                t = {l: "« " + e["t"][l][0] + " » — « " + rem(e["t"][l][1], l) + " »" if l == "fr" else "“" + e["t"][l][0] + "” — “" + rem(e["t"][l][1], l) + "”" if l == "en"
                     else "„" + e["t"][l][0] + "“ — „" + rem(e["t"][l][1], l) + "“" if l == "de" else "“" + e["t"][l][0] + "” — “" + rem(e["t"][l][1], l) + "”" for l in tls}
                qui = cap(rec)
                dd = mot["mot"] if mot.get("cat") else (mot.get("genre", "") + " " + mot["mot"]).strip()
                av = ["img", "gespraech"] if aid == "sonnenweg" else None
                enq = (qui + " pregunta: «" + e["q"] + "»" if ES else qui + " fragt: „" + e["q"] + "“")
                ajouter(s="entretien", c="c_entretien", av=av, e=enq, r=rep, l=leurres, ph=rep, t=t, w=mot, d=dd, liste=True)
                # vrai ou faux : la reponse convient-elle a la question ? (une seule fois par question, pas par paire)
                if pr is None or pr == paires[0]:
                    V, F = ("Sí", "No") if ES else ("Ja", "Nein")
                    rep2 = (" Mark: «" if ES else " Mark: „")
                    fin = ("»" if ES else "“")
                    ajouter(s="vraifaux", c="c_vraifauxEntretien", av=av, e=enq + rep2 + rep + fin, r=V, l=[F], n=1, ph=rep, t=t, w=mot, d=dd, vf=True)
                    ajouter(s="vraifaux", c="c_vraifauxEntretien", av=av, e=enq + rep2 + leurres[len(e["id"]) % len(leurres)] + fin, r=F, l=[V], n=1, ph=rep, t=t, w=mot, d=dd, vf=True)

    # 4. LA LETTRE : un morceau a trou
    for a in ads:
        lignes, trous, betreff = lettre(langue, a)
        k_f = a["kontakt"]["g"] == "f"
        for (cle, i, rep, leurres, mot, cons) in trous:
            ligne = lignes[i]
            if cle in ("anrede", "gruss"):
                trou = "___"
            else:
                motif = {"um": " um die", "als": " als ", "bewerbe": "bewerbe mich", "de": "puesto de ", "solicitar": "solicitar el"}[cle]
                trou = ligne.replace(motif, motif.replace(rep, "___"), 1)
            tl = {}
            f, kn = k_f, a["kontakt"]["nom"]
            for l in tls:
                if cle == "anrede":
                    tl[l] = {"fr": "Madame," if f else "Monsieur,", "en": ("Dear Ms " if f else "Dear Mr ") + kn + ",", "pt": ("Prezada Sra. " if f else "Prezado Sr. ") + kn + ",",
                             "de": ("Sehr geehrte Frau " if f else "Sehr geehrter Herr ") + kn + ","}[l]
                elif cle == "gruss":
                    tl[l] = {"fr": "Veuillez agréer mes salutations distinguées.", "en": "Kind regards,", "pt": "Atenciosamente,", "de": "Mit freundlichen Grüßen"}[l]
                else:
                    tl[l] = {"fr": "Je pose ma candidature pour le poste de " + a["t"]["fr"][0] + ".", "en": "I am applying for the job of " + a["t"]["en"][0] + ".",
                             "pt": "Estou me candidatando à vaga de " + a["t"]["pt"][0] + ".", "de": "Ich bewerbe mich um die Stelle als " + a["t"].get("de", [""])[0] + "."}[l]
            dd = mot[0] if mot[1] in ("verbe", "adjectif") else mot[1] + " " + mot[0]
            ajouter(s="lettre", c=cons, av=["lettre", a["id"], i, trou], e=("" if cle in ("anrede", "gruss") else trou), r=rep, l=leurres, n=min(3, len(leurres)), ph=ligne, t=tl, w=wl(mot), d=dd, liste=cle in ("anrede", "gruss"))
            # vrai ou faux : la ligne avec la bonne forme, ou avec un leurre
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            fx = leurres[(len(a["id"]) + i) % len(leurres)]
            fausse = trou.replace("___", fx)
            ajouter(s="vraifaux", c="c_vraifauxLettre", av=["lettre", a["id"], i, ligne], e=ligne, r=V, l=[F], n=1, ph=ligne, t=tl, w=wl(mot), d=dd, vf=True)
            ajouter(s="vraifaux", c="c_vraifauxLettre", av=["lettre", a["id"], i, fausse], e=fausse, r=F, l=[V], n=1, ph=ligne, t=tl, w=wl(mot), d=dd, vf=True)

    # 5. LE CV : la rubrique d'une ligne
    cv = CV[langue]
    rub = cv["rubriques"]
    for ri, r in enumerate(rub):
        for li, ligne in enumerate(r["lignes"]):
            mot = wl(r["mot"]) if r["mot"] else wl(cv["mot"])
            dd = mot["mot"] if mot.get("cat") else mot["genre"] + " " + mot["mot"]
            tt = {l: r["titre"] + (" = " if l != "de" else " → ") + cv["t"][l][ri] for l in tls}
            ajouter(s="cv", c="c_cv", av=["cv", ri, li, "cache"], e=("¿En qué apartado está esta línea?" if ES else "Unter welcher Überschrift steht diese Zeile?"), r=r["titre"],
                    l=[x["titre"] for x in rub if x is not r], ph=r["titre"] + ": " + ligne, t=tt, w=mot, d=dd)
            # vrai ou faux : « „Fussball, Laufen, Kochen“ steht unter „Hobbys“. »
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            autre = rub[(ri + li + 1) % len(rub)] if rub[(ri + li + 1) % len(rub)] is not r else rub[(ri + 2) % len(rub)]
            dit = lambda t_: ("«" + ligne + "» está en el apartado «" + t_ + "»." if ES else "„" + ligne + "“ steht unter „" + t_ + "“.")
            ajouter(s="vraifaux", c="c_vraifauxCv", av=["cv", ri, li, "cache"], e=dit(r["titre"]), r=V, l=[F], n=1, ph=r["titre"] + ": " + ligne, t=tt, w=mot, d=dd, vf=True)
            ajouter(s="vraifaux", c="c_vraifauxCv", av=["cv", ri, li, "cache"], e=dit(autre["titre"]), r=F, l=[V], n=1, ph=r["titre"] + ": " + ligne, t=tt, w=mot, d=dd, vf=True)
    # vrai ou faux sur les langues du CV
    SP = SPRACHEN[langue]
    for i, (sp, phrase, t) in enumerate(SP):
        mot = wl(["idioma", "el"]) if ES else wl(["Sprachkenntnisse", "die (Pl.)"])
        ajouter(s="vraifaux", c="c_vraifauxCv", av=["cv", 3, i], e=phrase, r=("Verdadero" if ES else "Richtig"), l=[("Falso" if ES else "Falsch")], n=1, ph=phrase, t={l: t[l] for l in tls}, w=mot, d=mot["mot"], vf=True)
        for j, (sp2, _, _) in enumerate(SP):
            if j != i:
                f = phrase.replace(sp, sp2)
                if f != phrase and f not in [p for (_, p, _) in SP]:
                    ajouter(s="vraifaux", c="c_vraifauxCv", av=["cv", 3, i], e=f, r=("Falso" if ES else "Falsch"), l=[("Verdadero" if ES else "Richtig")], n=1, ph=phrase, t={l: t[l] for l in tls}, w=mot, d=mot["mot"], vf=True)

    # 6. LE CONTRAT : la question d'une case ; le nom d'une case cachee ; vrai ou faux
    ct = CONTRAT[langue]
    for c in ct["cases"]:
        mot = wl(c["mot"])
        dd = mot["mot"] if mot.get("cat") else mot["genre"] + " " + mot["mot"]
        tt = {l: c["t"][l] for l in tls}
        ajouter(s="contrat", c="c_contrat", av=["contrat", c["id"], None], e=c["q"], r=c["r"], l=c["rf"], n=2, ph=c["ph"], t=tt, w=mot, d=dd)
        ajouter(s="contrat", c="c_contratLabel", av=["contrat", None, c["id"]], e="___: " + c["v"], r=c["label"], l=[x["label"] for x in ct["cases"] if x is not c], ph=c["label"] + ": " + c["v"], t=tt, w=mot, d=dd)
        for v, juste in [(c["r"], True)] + [(f, False) for f in c["rf"]]:
            ajouter(s="vraifaux", c="c_vraifauxContrat", av=["contrat", c["id"], None], e=c["vf"].replace("{r}", v), r=(("Verdadero" if ES else "Richtig") if juste else ("Falso" if ES else "Falsch")),
                    l=[("Falso" if ES else "Falsch") if juste else ("Verdadero" if ES else "Richtig")], n=1, ph=c["ph"], t=tt, w=mot, d=dd, vf=True)

    # 7. LES ACTIONS : l'image -> la phrase ; l'objet -> le verbe ; (de) la place du petit mot
    ACT = ACTIONS[langue]
    def phrase(x, avec_obj=True):
        v, pron, part = C.er(x["v"])
        S = cap(gens(langue, x["s"]))
        if ES:
            return espaces(S + " " + (x.get("pre", "") + " ") + v + " " + (x["obj"] if avec_obj else "") + ".")
        return espaces(S + " " + v + " " + pron + " " + (x["obj"] if avec_obj else "") + " " + part + ".")
    def proches(i, j):
        return {i, j} in [set(p) for p in IMG_PROCHES]
    for x in ACT:
        x["ph"] = phrase(x)                                # la phrase de la decouverte
        tt = {l: x["t"][l] for l in tls}
        if x["img"]:
            autres = [y for y in ACT if y["img"] and y["img"] != x["img"] and y["v"] != x["v"] and not proches(x["img"], y["img"])]
            ajouter(s="quoi", c="c_quoi", av=["img", x["img"]], e=("¿Qué pasa en la foto?" if ES else "Was passiert auf dem Bild?"), r=phrase(x), l=[phrase(y) for y in autres], n=2,
                    ph=phrase(x), t=tt, w=w(x["v"], cat="verbe"), d=x["v"], liste=True)
        if x.get("verbe", True) and x["obj"]:
            libres = [y["v"] for y in ACT if y["v"] != x["v"] and y["v"] not in x["aussi_v"] and y.get("verbe", True)]
            enonce = ((x.get("pre", "") + " ___ ").lstrip() + x["obj"]) if ES else (x["obj"] + " ___")
            av = ["img", x["img"]] if x["img"] else None
            ajouter(s="verbe", c="c_verbe", av=av, e=enonce, r=x["v"], l=libres, ph=phrase(x), t=tt, w=w(x["v"], cat="verbe"), d=x["v"])
            # vrai ou faux : la phrase avec son verbe, ou avec un verbe qui ne va pas avec l'objet
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            y = next(z for z in ACT if z["v"] == libres[len(x["id"]) % len(libres)])
            ajouter(s="vraifaux", c="c_vraifauxPhrase", av=av, e=phrase(x), r=V, l=[F], n=1, ph=phrase(x), t=tt, w=w(x["v"], cat="verbe"), d=x["v"], vf=True)
            ajouter(s="vraifaux", c="c_vraifauxPhrase", av=av, e=phrase(dict(x, v=y["v"])), r=F, l=[V], n=1, ph=phrase(x), t=tt, w=w(x["v"], cat="verbe"), d=x["v"], vf=True)
        if not ES:
            v, pron, part = C.er(x["v"])
            S = cap(gens(langue, x["s"]))
            if part or x["v"] in ("sich bewerben", "unterschreiben"):
                juste = phrase(x)
                if part:
                    faux = [espaces(S + " " + part + v + " " + pron + " " + x["obj"] + "."), espaces(S + " " + v + " " + part + " " + pron + " " + x["obj"] + ".")]
                    if pron:
                        faux.append(espaces(S + " " + v + " " + x["obj"] + " " + part + " " + pron + "."))
                elif x["v"] == "sich bewerben":
                    faux = [espaces(S + " wirbt sich " + x["obj"] + " be."), espaces(S + " bewirbt " + x["obj"] + " sich.")]
                else:
                    faux = [espaces(S + " schreibt " + x["obj"] + " unter."), espaces(S + " unter schreibt " + x["obj"] + ".")]
                ajouter(s="ordre", c="c_ordre", av=["img", x["img"]] if x["img"] else None, e="Welcher Satz ist richtig?", r=juste, l=faux, n=2, ph=juste,
                        t={l: x["t"][l] for l in tls}, w=w(x["v"], cat="verbe"), d=x["v"], liste=True)

    # 8. SIE OU DU / USTED OU TU
    for it in REGISTRE[langue]:
        e = C.verbes[it["v"]]["praesens"]
        formes = {"sie": e["sie_Sie"] if not ES else e["er_sie_es"], "du": e["du"], "er": e["er_sie_es"] if not ES else e["ich"]}
        for reg in ("sie", "du"):
            if not it[reg]:
                continue
            for (A, B) in REGISTRE_GENS[reg]:
                if reg == "du" and it.get("dir") == "vers" and B != "mark":
                    continue                               # « Bist du der Neue? » : un collegue le demande a Mark, pas l'inverse
                if reg == "du" and it.get("dir") == "de" and A != "mark":
                    continue                               # « Seit wann arbeitest du hier? » : Mark, le nouveau, le demande
                rep = formes[reg]
                txt = it[reg]
                debut = txt.startswith("___") or txt.startswith("¿___")
                aff = lambda f: (cap(f) if debut else f)
                juste = txt.replace("___", aff(rep))
                ti = 0 if reg == "sie" else 1
                tt = {l: it["t"][l][ti] for l in tls if it["t"][l][ti]}
                pA, pB = cap(gens(langue, A)), gens(langue, B)
                if ES and B != "mark":
                    pB = pB
                intro = FRAGT[langue].replace("{A}", pA).replace("{B}", pB)
                vis = "chef" if reg == "sie" else (A if A != "mark" else B)
                mot = {"de": {"chef": ["Chefin", "die"], "m": ["Kollege", "der"], "f": ["Kollegin", "die"]},
                       "es": {"chef": ["jefa", "la"], "m": ["compañero", "el"], "f": ["compañera", "la"]}}[langue][vis]
                ajouter(s="registre", c="c_registre", av=None, e=intro + " " + ("«" + txt + "»" if ES else "„" + txt + "“"), r=aff(rep),
                        l=[aff(formes[k]) for k in formes if formes[k] != rep], n=2, ph=juste, t=tt, w=wl(mot), d=mot[1] + " " + mot[0], cle=reg)

    # 9. L'APPEL : une ligne a trou
    for sym in SYMPTOMES[langue]:
        lignes = appel(langue, sym)
        for i, (qui, txt, trou) in enumerate(lignes):
            if not trou:
                continue
            rep, leurres, mot = trou[0], trou[1], trou[2]
            t = appel_t(langue, i, sym)
            tt = {l: t[l] for l in tls if t and l in t}
            dd = mot[0] if mot[1] in ("verbe", "adjectif") else mot[1] + " " + mot[0]
            ajouter(s="telefon", c="c_telefon", av=["appel", sym[0], i, txt], e=txt, r=rep, l=leurres, ph=txt.replace("___", rep), t=tt, w=wl(mot), d=dd)
            # vrai ou faux : la ligne completee juste, ou avec un leurre (« Ich habe Urlaub. »)
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            fausse = txt.replace("___", leurres[len(sym[0]) % len(leurres)])
            ajouter(s="vraifaux", c="c_vraifauxAppel", av=["appel", sym[0], i, txt.replace("___", rep)], e=txt.replace("___", rep), r=V, l=[F], n=1, ph=txt.replace("___", rep), t=tt, w=wl(mot), d=dd, vf=True)
            ajouter(s="vraifaux", c="c_vraifauxAppel", av=["appel", sym[0], i, fausse], e=fausse, r=F, l=[V], n=1, ph=txt.replace("___", rep), t=tt, w=wl(mot), d=dd, vf=True)

    # 10. QUI EST QUI
    for ro in ROLES[langue]:
        reps = ro["r"] if isinstance(ro["r"], list) else [ro["r"]] * len(ro["d"])
        mots = ro["mot"] if isinstance(ro["mot"][0], list) else [ro["mot"]] * len(ro["d"])
        for i, dsc in enumerate(ro["d"]):
            t = {l: (ro["t"][l][i] if isinstance(ro["t"][l], list) else ro["t"][l]) for l in tls}
            av = ["img", ro["img"]] if ro["img"] else None
            leurres = [x for x in ro["l"] if x not in reps]
            ajouter(s="qui", c="c_qui", av=av, e=dsc, r=reps[i], l=leurres, n=3, ph=dsc.replace("___", reps[i]), t=t, w=wl(mots[i]), d=mots[i][1] + " " + mots[i][0])
            V, F = ("Verdadero", "Falso") if ES else ("Richtig", "Falsch")
            ajouter(s="vraifaux", c="c_vraifauxQui", av=av, e=dsc.replace("___", reps[i]), r=V, l=[F], n=1, ph=dsc.replace("___", reps[i]), t=t, w=wl(mots[i]), d=mots[i][1] + " " + mots[i][0], vf=True)
            ajouter(s="vraifaux", c="c_vraifauxQui", av=av, e=dsc.replace("___", leurres[i % len(leurres)]), r=F, l=[V], n=1, ph=dsc.replace("___", reps[i]), t=t, w=wl(mots[i]), d=mots[i][1] + " " + mots[i][0], vf=True)

    # 11. SER OU ESTAR (es)
    if ES:
        for qk in QU:
            for p in ("mark", "m", "f"):
                g = GENS[langue][p]["g"]
                P = cap(gens(langue, p))
                a_ = adj(langue, qk, g)
                tt = {l: cap(gens(langue, p, l)) + {"fr": " est ", "en": " is ", "pt": " é ", "de": " ist "}[l] + accord(QU[qk]["t"][l][0], g) + "." for l in tls}
                ajouter(s="serEstar", c="c_serEstar", av=None, e=P + " ___ " + a_ + ".", r="es", l=["está"], n=1, ph=P + " es " + a_ + ".", t=tt, w=w(qk, cat="adjectif"), d=a_)
        for ek, (f, img, ttr, quand) in ESTAR.items():
            for p in ("mark", "m", "f"):
                g = GENS[langue][p]["g"]
                P = cap(gens(langue, p))
                a_ = ek if g == "m" else f
                tt = {l: cap(gens(langue, p, l)) + {"fr": " est ", "en": " is ", "pt": " está ", "de": " ist "}[l] + ttr[l][0 if g == "m" else 1] + accord(ESTAR_T[quand][l], g) + "." for l in tls}
                ajouter(s="serEstar", c="c_serEstar", av=["img", img] if (img and p == "mark") else None, e=P + " ___ " + a_ + " " + quand + ".", r="está", l=["es"], n=1,
                        ph=P + " está " + a_ + " " + quand + ".", t=tt, w=w(ek, cat="adjectif"), d=a_)
        for (e, rep, mot, tt) in LIEUX_ESTAR:
            ajouter(s="serEstar", c="c_serEstar", av=None, e=e, r=rep, l=["es" if rep == "está" else "está"], n=1, ph=e.replace("___", rep), t={l: tt[l] for l in tls}, w=wl(mot), d=mot[1] + " " + mot[0])

    # 12. LES DOCUMENTS : l'image -> le nom ; le nom entendu -> l'image ; et le papier dessine -> le nom (sans image)
    dk = DOCS[langue]
    papiers = {"zeitung": [["annonce", a["id"], None, "anon"] for a in ads[:3]], "lebenslauf": [["cv", -1, -1, "anon"]], "anschreiben": [["lettre", "sonnenweg", -1, None], ["lettre", "cafe", -1, None]],
               "arbeitsvertrag": [["contrat", None, None, "anon"]]}
    for k, (m, g, t) in dk.items():
        aff = g + " " + m
        for av in papiers[k]:
            ajouter(s="document", c="c_papier", av=av, e=("¿Qué es este papel?" if ES else "Was für ein Papier ist das?"), r=aff, l=[dk[x][1] + " " + dk[x][0] for x in dk if x != k], n=3,
                    ph=("Es " + aff + "." if ES else "Das ist " + aff + "."), t={l: {"fr": "C'est ", "en": "This is ", "pt": "É ", "de": "Das ist "}[l] + t[l] + "." for l in tls}, w=w(m, g), d=aff)
    for k, (m, g, t) in dk.items():
        aff = g + " " + m
        ajouter(s="document", c="c_document", av=["img", k], e=("¿Qué es esto?" if ES else "Was ist das?"), r=aff, l=[dk[x][1] + " " + dk[x][0] for x in dk if x != k], n=3,
                ph=("Es " + aff + "." if ES else "Das ist " + aff + "."), t={l: {"fr": "C'est ", "en": "This is ", "pt": "É ", "de": "Das ist "}[l] + t[l] + "." for l in tls}, w=w(m, g), d=aff)
        ajouter(s="entendre", c="c_entendre", av=None, e="", r=k, l=[x for x in dk if x != k], n=2, ph=("Es " + aff + "." if ES else "Das ist " + aff + "."),
                t={l: {"fr": "C'est ", "en": "This is ", "pt": "É ", "de": "Das ist "}[l] + t[l] + "." for l in tls}, w=w(m, g), d=aff, images=True)
    return Q, C


# ---------------------------------------------------------------------------------------------------------------
def annonce_affiche(langue, a):
    """Les lignes de l'annonce, dans l'ordre d'une vraie annonce : [cle, libelle, valeur]."""
    U = UMFANG[langue]
    x, par = a["lohn"]
    b = BEGINN[a["beginn"]][langue][0]
    if langue == "de":
        return {"titre": a["stelle"] + " (m/w/d)", "firma": a["firma"], "intro": "Wir suchen " + ("ab sofort" if a["beginn"] == "sofort" else b) + ":",
                "lignes": [["umfang", "Arbeitszeit", U[a["umfang"]]["wort"]], ["stunden", "Stunden", "%d Stunden pro Woche" % a["stunden"]],
                           ["lohn", "Lohn" if par == "stunde" else "Gehalt", lohn(x, par, "de").replace(" im Monat", " brutto im Monat")],
                           ["beginn", "Beginn", b], ["erwartet", "Sie sind", ", ".join(a["erwartet"])], ["plus", "", a["plus"]], ["bietet", "Wir bieten", a["bietet"]],
                           ["kontakt", "Bewerbung an", contact(a["kontakt"], "de", "n") + ", " + a["mail"]]]}
    return {"titre": a["stelle"], "firma": a["firma"], "intro": "Buscamos:",
            "lignes": [["umfang", "Jornada", U[a["umfang"]]["wort"]], ["stunden", "Horas", "%d horas a la semana" % a["stunden"]],
                       ["lohn", "Sueldo", lohn(x, par, "es").replace(" al mes", " brutos al mes")], ["beginn", "Inicio", b],
                       ["erwartet", "Eres", " y ".join(a["erwartet"])], ["plus", "", a["plus"]], ["bietet", "Ofrecemos", a["bietet"]],
                       ["kontakt", "Envía tu currículum a", contact(a["kontakt"], "es", "n") + ", " + a["mail"]]]}


def ecrire_json():
    d = {"gens": GENS, "firme": FIRME, "annonces": {}, "cv": CV, "contrat": CONTRAT, "lettres": {}, "appels": {}, "images": {i: img_src(i) for i in IMAGES},
         "docs": DOCS, "actions": ACTIONS, "questions": {}, "mots": {}, "absents": {}, "tc": {}}
    rapport = []
    for langue in ("de", "es"):
        Q, C = fabriquer(langue)
        d["annonces"][langue] = {a["id"]: annonce_affiche(langue, a) for a in ANNONCES[langue]}
        d["lettres"][langue] = {}
        for a in ANNONCES[langue]:
            lignes, _, betreff = lettre(langue, a)
            d["lettres"][langue][a["id"]] = {"lignes": lignes, "betreff": betreff, "expediteur": a["brief"] if a["brief"] != "Mark" else "Mark Garnier"}
        d["appels"][langue] = {s[0]: [[qui, txt.replace("___", tr_[0]) if tr_ else txt] for (qui, txt, tr_) in appel(langue, s)] for s in SYMPTOMES[langue]}
        # les mots vises, a la forme du corpus, et leur traduction (le corpus, sinon les ajouts)
        mots, absents, vus = [], [], set()
        for q in Q:
            k = (q["w"]["mot"], q["w"].get("genre"), q["w"].get("cat"))
            if k in vus:
                continue
            vus.add(k)
            g = C.glose(*k)
            if g is None:
                sys.exit("  %s %s : absent du corpus et des ajouts" % (langue, k))
            manque = [l for l, v in g.items() if not v]
            if manque:
                sys.exit("  %s %s : pas de traduction en %s" % (langue, k, ", ".join(manque)))
            if not C.entree(*k):
                absents.append(k[0])
            m = dict(q["w"]); m["g"] = g
            mots.append(m)
        d["mots"][langue] = mots
        d["absents"][langue] = sorted(set(absents))
        # les traductions des choix (« Tu as choisi : ... ») : les mots du corpus, par la glose
        tc = {}
        for q in Q:
            for o in [q["r"]] + q["l"]:
                if o in tc:
                    continue
                for cle in ((o, None, "adjectif"), (o, None, "verbe")) + tuple((o.split(" ", 1)[1], o.split(" ", 1)[0], None) for _ in [0] if " " in o):
                    g = C.glose(*cle)
                    if g:
                        tc[o] = g
                        break
        d["tc"][langue] = tc
        # le controle : chaque question bien formee, chaque mot vise par deux sortes au moins, la reserve
        sortes = {}
        for q in Q:
            assert q["r"] not in q["l"], q
            assert len(q["l"]) >= (1 if q.get("vf") or q["s"] == "serEstar" else 1), ("pas de leurre", q)
            k = (q["w"]["mot"], q["w"].get("genre"), q["w"].get("cat"))
            sortes.setdefault(k, set()).add(q["s"])
        seuls = [k[0] for k, s in sortes.items() if len(s) < 2]
        diff = len({(q["s"], q["e"], json.dumps(q["av"], ensure_ascii=False), q["r"]) for q in Q})
        par = {}
        for q in Q:
            par[q["s"]] = par.get(q["s"], 0) + 1
        rapport.append("  %s : %d questions (%d differentes), %d mots dont %d absents du corpus (%s) ; par sorte %s%s" % (
            langue, len(Q), diff, len(mots), len(d["absents"][langue]), ", ".join(d["absents"][langue]), json.dumps(par, ensure_ascii=False),
            ("\n    mots vises par une seule sorte : " + ", ".join(seuls)) if seuls else ""))
        d["questions"][langue] = Q
    d["images_existent"] = {i: os.path.exists(os.path.join(RACINE, "visuel", "prototype", img_src(i))) for i in IMAGES}
    texte = json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "\n"
    chemin = os.path.join(RACINE, "visuel", "prototype", "travail", "travail.json")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    print("\n".join(rapport))
    print("  -> %s (%d ko)" % (os.path.relpath(chemin, RACINE), len(texte.encode("utf-8")) // 1024))
    return d


def images():
    out = {}
    for i, im in IMAGES.items():
        if im.get("src"):
            continue
        src = im.get("source")
        photo = PHOTO
        if not src or src == "Mark":
            photo = PHOTO.replace("Hands: five fingers each, natural. ", "No people and no hands in the picture: the object alone. ")
        out[i] = (src, im["prompt"] + photo)
    return out


def reference_png(chemin):
    """fal veut une image : un webp est converti en png a cote (dans le dossier des originaux)."""
    if chemin.lower().endswith(".png"):
        return chemin
    from PIL import Image
    sortie = os.path.join(DOSSIER, "ref-" + os.path.splitext(os.path.basename(chemin))[0] + ".png")
    Image.open(chemin).convert("RGB").save(sortie)
    return sortie


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    ecrire_json()
    if "--json" in sys.argv:
        return
    tout = images()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or (ESSAI if "--essai" in sys.argv else list(tout))
    inconnus = [n for n in noms if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    os.makedirs(DOSSIER, exist_ok=True)
    if refaire and not montrer:
        for n in noms:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if montrer:
        for nom in a_faire:
            print("\n  %s%s\n  %s" % (nom, " (retouche de %s)" % tout[nom][0] if tout[nom][0] else "", tout[nom][1]))
        return
    manque = [s for n in a_faire for s in (tout[n][0] or "").split("+") if s and not os.path.exists(REFERENCES[s])]
    if manque:
        sys.exit("  references absentes : " + ", ".join(sorted(set(manque))) + " (« Equipe » = kollegen.png : la faire d'abord)")
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for nom in a_faire:
        source, prompt = tout[nom]
        print("\n  %s%s\n  %s" % (nom, " (retouche de %s)" % source if source else "", prompt))
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = TEXTE
        if source:
            corps["image_urls"] = [O.deposer(reference_png(REFERENCES[s]), "image/png", cle)[0] for s in source.split("+")]
            modele = EDIT
        soum = O._json("https://queue.fal.run/" + modele, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom, err)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "source": source, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
