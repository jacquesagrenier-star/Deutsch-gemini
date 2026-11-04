# -*- coding: utf-8 -*-
"""Les demarches, theme illustre de la vague 3 (4 nov. 2026, decision du chef pendant l'absence de Jacques : « servir
l'allemand et le DTZ »). L'administration et la vie pratique : le Buergeramt, prendre rendez-vous, s'inscrire, le
formulaire, les documents, la banque, l'assurance maladie, le medecin de famille ; on y lit aussi un formulaire, un avis,
des heures d'ouverture et une confirmation de rendez-vous, dessines en HTML par la page (aucun texte dans les images).

    python visuel/demarches/demarches.py --json             # demarches.json seul, gratuit
    python visuel/demarches/demarches.py --montrer          # les prompts seuls, gratuit
    python visuel/demarches/demarches.py --essai            # la planche d'essai (6 images, 0,90 $) -- ACCORD DE JACQUES
    python visuel/demarches/demarches.py pass konto         # celles-la seulement (0,15 $ chacune)
    python visuel/demarches/demarches.py --refaire pass     # l'ancienne passe en <nom>-rate<k>.png

L'ANGLE (regle 2 des themes : pas de scene refaite). La scene « Im Buergeramt » enseigne les OBJETS du bureau (le
tampon, l'ecran, le classeur). Le theme enseigne la DEMARCHE : ou l'on va, ce qu'on y fait, ce qu'on apporte, le
formulaire qu'on remplit, l'avis qu'on lit, la phrase polie du guichet (Sie / usted).

LES DEUX MONDES. Les images sont les memes, sans texte ; les phrases sont ecrites pour chaque langue.
  - en allemand, Mark Garnier a Berlin-Pankow, Gartenstrasse 12 (decision de Jacques du 3 nov. : le nom et l'adresse
    des documents du DTZ ; les textes du DTZ y mettent aussi la Hausverwaltung Kern et la Praxis Dr. Yilmaz) ;
  - en espagnol, le Mark de la serie « Mark en Madrid » (mexicain) : l'empadronamiento, la cita, el banco, la consulta.
Mark a 25 ans en novembre 2026 (la presentation de l'oral du DTZ) : ne le 14 mars 2001. Ni compagne ni enfant : ledig.
Sa mere est allemande (personnages.json), mais elle est devenue canadienne avant sa naissance : avec la regle d'avant
2024, elle a perdu la nationalite allemande et ne l'a pas transmise. Mark n'est PAS allemand, il a besoin d'un titre
de sejour et peut suivre un cours d'integration (decision de Jacques du 4 nov., decisions/DECISIONS.md). Le permis de
sejour figure pour l'instant en avis (« Was braucht man fuer die Aufenthaltserlaubnis? ») ; en espagnol, Mark est
mexicain a Madrid : le permiso de residencia vaut pour lui aussi.

LES PHRASES SONT FABRIQUEES par la page (demarches.html) a partir de ces tables, jamais ecrites une a une : chaque
demarche a ses morceaux (le verbe du corpus, l'objet, le lieu) et ses traductions-gabarits ({L} = le lieu). Un leurre
n'est jamais une reponse possible : chaque demarche dit ou ELLE PEUT AUSSI se faire (« aussi ») et quels verbes lui
iraient aussi (« aussi_v ») ; chaque image de document dit les documents clairement faux pour elle (« faux »).

Images : fal, nano-banana-pro, 0,15 $ l'image. Mark ne se regenere jamais : retouche de son image de l'episode 2 (la
tenue « administration », chemise bleu clair) ; le Buergeramt reprend le maitre de l'episode 2 (murs vert menthe, plinthe
vert fonce, carrelage creme fendu). Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/demarches/img/.
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "demarches", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
EP2 = PRINCIPAL + "/video/episode-02-beim-buergeramt/01-images/"
REFERENCES = {"Mark": EP2 + "mark-moyen.png", "Buergeramt": EP2 + "buergeramt_wartezimmer.png"}

# ---------------------------------------------------------------------------------------------------------------
# LES LIEUX. dat : la reponse de « Wo? » (Wo? + datif, la contraction im = in dem) ; nom : le lieu dans une phrase
# (« Am Samstag ist die Bank geschlossen. ») ; carte : le nom en tete d'un avis. mot / genre : la forme du corpus (le
# mot que la question fait avancer). trad : {langue: [le nom avec l'article, « a » + le lieu, feminin ?]}.
LIEUX = {
    "de": {
        "buergeramt":   {"mot": "Bürgeramt", "genre": "das", "nom": "das Bürgeramt", "dat": "im Bürgeramt", "carte": "Bürgeramt Pankow",
                         "trad": {"fr": ["le bureau des citoyens", "au bureau des citoyens", False], "en": ["the citizens' office", "at the citizens' office"],
                                  "pt": ["o posto de atendimento ao cidadão", "no posto de atendimento ao cidadão", False]}},
        "bank":         {"mot": "Bank", "genre": "die", "nom": "die Bank", "dat": "bei der Bank", "carte": "Bank · Filiale Pankow",
                         "trad": {"fr": ["la banque", "à la banque", True], "en": ["the bank", "at the bank"], "pt": ["o banco", "no banco", False]}},
        "krankenkasse": {"mot": "Krankenkasse", "genre": "die", "nom": "die Krankenkasse", "dat": "bei der Krankenkasse", "carte": "Krankenkasse · Geschäftsstelle Pankow",
                         "trad": {"fr": ["la caisse d'assurance maladie", "à la caisse d'assurance maladie", True], "en": ["the health insurance office", "at the health insurance office"],
                                  "pt": ["a caixa do seguro de saúde", "na caixa do seguro de saúde", True]}},
        "praxis":       {"mot": "Praxis", "genre": "die", "nom": "die Praxis", "dat": "in der Praxis", "carte": "Praxis Dr. Yilmaz · Allgemeinmedizin",
                         "trad": {"fr": ["le cabinet médical", "au cabinet médical", False], "en": ["the doctor's practice", "at the doctor's practice"],
                                  "pt": ["o consultório", "no consultório", False]}},
    },
    "es": {
        "oficina":  {"mot": "oficina", "genre": "la", "nom": "la oficina", "dat": "en la oficina", "carte": "Oficina de Atención a la Ciudadanía · Centro",
                     "trad": {"fr": ["le bureau de la mairie", "au bureau de la mairie", False], "en": ["the town hall office", "at the town hall office"],
                              "pt": ["a repartição da prefeitura", "na repartição da prefeitura", True], "de": ["das Bürgeramt", "im Bürgeramt"]}},
        "banco":    {"mot": "banco", "genre": "el", "nom": "el banco", "dat": "en el banco", "carte": "Banco · Sucursal Malasaña",
                     "trad": {"fr": ["la banque", "à la banque", True], "en": ["the bank", "at the bank"], "pt": ["o banco", "no banco", False], "de": ["die Bank", "bei der Bank"]}},
        "consulta": {"mot": "consulta", "genre": "la", "nom": "la consulta", "dat": "en la consulta", "carte": "Centro de Salud · Consulta de medicina de familia",
                     "trad": {"fr": ["le cabinet médical", "au cabinet médical", False], "en": ["the doctor's practice", "at the doctor's practice"],
                              "pt": ["o consultório", "no consultório", False], "de": ["die Praxis", "in der Praxis"]}},
    },
}

# LES HEURES D'OUVERTURE (inventees, vraisemblables) : jour (1 = lundi ... 6 = samedi) -> plages [debut, fin[
HORAIRES = {
    "de": {"buergeramt": {1: [[8, 15]], 2: [[11, 18]], 3: [[8, 13]], 4: [[11, 18]], 5: [[8, 13]]},
           "bank": {1: [[9, 16]], 2: [[9, 16]], 3: [[9, 13]], 4: [[9, 18]], 5: [[9, 14]]},
           "krankenkasse": {1: [[8, 17]], 2: [[8, 17]], 3: [[8, 17]], 4: [[8, 18]], 5: [[8, 13]]},
           "praxis": {1: [[8, 12], [15, 18]], 2: [[8, 12], [15, 18]], 3: [[8, 12]], 4: [[8, 12], [15, 19]], 5: [[8, 12]]}},
    "es": {"oficina": {1: [[9, 14]], 2: [[9, 14]], 3: [[9, 14]], 4: [[9, 14], [16, 19]], 5: [[9, 14]]},
           "banco": {1: [[8, 14]], 2: [[8, 14]], 3: [[8, 14]], 4: [[8, 14]], 5: [[8, 14]]},
           "consulta": {1: [[8, 15]], 2: [[8, 15], [16, 20]], 3: [[8, 15]], 4: [[8, 15], [16, 20]], 5: [[8, 15]]}},
}
JOURS = {"de": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
         "es": ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"],
         "fr": ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"],
         "en": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
         "pt": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]}
# offen / geschlossen, abierto / cerrado : les adjectifs de l'avis (es : [masculin, feminin], accord avec le lieu)
OUVERT = {"de": {"offen": "offen", "geschlossen": "geschlossen"},
          "es": {"abierto": ["abierto", "abierta"], "cerrado": ["cerrado", "cerrada"]}}
OUVERT_TRAD = {"fr": {"o": ["ouvert", "ouverte"], "f": ["fermé", "fermée"]}, "en": {"o": ["open", "open"], "f": ["closed", "closed"]},
               "pt": {"o": ["aberto", "aberta"], "f": ["fechado", "fechada"]}, "de": {"o": ["offen", "offen"], "f": ["geschlossen", "geschlossen"]}}

# ---------------------------------------------------------------------------------------------------------------
# LES DOCUMENTS. Une image par document (img : None pour ceux qui ne vivent que dans un avis). acc : apres « braucht
# man » / « hace falta » ; trad : [le nom avec l'article] ; faux : les documents CLAIREMENT faux pour l'image -- les
# seuls leurres d'une question sur l'image (deux cartes avec photo se ressemblent : jamais l'une pour l'autre).
DOCS = {
    "de": {
        "pass":               {"mot": "Pass", "genre": "der", "acc": "den Pass", "img": "pass",
                               "trad": {"fr": "le passeport", "en": "the passport", "pt": "o passaporte"}},
        "formular":           {"mot": "Formular", "genre": "das", "acc": "das Formular", "img": "formular",
                               "trad": {"fr": "le formulaire", "en": "the form", "pt": "o formulário"}},
        "meldebescheinigung": {"mot": "Meldebescheinigung", "genre": "die", "acc": "die Meldebescheinigung", "img": "bescheinigung",
                               "trad": {"fr": "l'attestation de domicile", "en": "the registration certificate", "pt": "o comprovante de residência"}},
        "versichertenkarte":  {"mot": "Versichertenkarte", "genre": "die", "acc": "die Versichertenkarte", "img": "versichertenkarte",
                               "trad": {"fr": "la carte d'assurance maladie", "en": "the health insurance card", "pt": "a carteirinha do seguro de saúde"}},
        "arbeitsvertrag":     {"mot": "Arbeitsvertrag", "genre": "der", "acc": "den Arbeitsvertrag", "img": "arbeitsvertrag",
                               "trad": {"fr": "le contrat de travail", "en": "the employment contract", "pt": "o contrato de trabalho"}},
        "mietvertrag":        {"mot": "Mietvertrag", "genre": "der", "acc": "den Mietvertrag", "img": "mietvertrag",
                               "trad": {"fr": "le bail", "en": "the tenancy agreement", "pt": "o contrato de aluguel"}},
        "foto":               {"mot": "Foto", "genre": "das", "acc": "ein Foto", "img": "foto",
                               "trad": {"fr": "une photo", "en": "a photo", "pt": "uma foto"}},
        "karte":              {"mot": "Karte", "genre": "die", "acc": "die Karte", "img": "karte",
                               "trad": {"fr": "la carte bancaire", "en": "the bank card", "pt": "o cartão do banco"}},
        "bestaetigung":       {"mot": "Bestätigung", "genre": "die", "acc": "die Bestätigung vom Vermieter", "img": None,
                               "trad": {"fr": "l'attestation du propriétaire", "en": "the landlord's confirmation", "pt": "a declaração do proprietário"}},
    },
    "es": {
        "pasaporte":   {"mot": "pasaporte", "genre": "el", "acc": "el pasaporte", "img": "pass",
                        "trad": {"fr": "le passeport", "en": "the passport", "pt": "o passaporte", "de": "der Pass"}},
        "formulario":  {"mot": "formulario", "genre": "el", "acc": "el formulario", "img": "formular",
                        "trad": {"fr": "le formulaire", "en": "the form", "pt": "o formulário", "de": "das Formular"}},
        "certificado": {"mot": "certificado de empadronamiento", "genre": "el", "acc": "el certificado de empadronamiento", "img": "bescheinigung",
                        "trad": {"fr": "l'attestation de domicile", "en": "the registration certificate", "pt": "o comprovante de residência", "de": "die Meldebescheinigung"}},
        "tarjeta_sanitaria": {"mot": "tarjeta sanitaria", "genre": "la", "acc": "la tarjeta sanitaria", "img": "versichertenkarte",
                        "trad": {"fr": "la carte d'assurance maladie", "en": "the health card", "pt": "o cartão de saúde", "de": "die Versichertenkarte"}},
        "contrato":    {"mot": "contrato", "genre": "el", "acc": "el contrato de trabajo", "img": "arbeitsvertrag", "affiche": "contrato de trabajo",
                        "trad": {"fr": "le contrat de travail", "en": "the employment contract", "pt": "o contrato de trabalho", "de": "der Arbeitsvertrag"}},
        "contrato_alquiler": {"mot": "contrato", "genre": "el", "acc": "el contrato de alquiler", "img": "mietvertrag", "affiche": "contrato de alquiler",
                        "trad": {"fr": "le bail", "en": "the tenancy agreement", "pt": "o contrato de aluguel", "de": "der Mietvertrag"}},
        "foto":        {"mot": "foto", "genre": "la", "acc": "una foto", "img": "foto",
                        "trad": {"fr": "une photo", "en": "a photo", "pt": "uma foto", "de": "ein Foto"}},
        "tarjeta":     {"mot": "tarjeta", "genre": "la", "acc": "la tarjeta", "img": "karte",
                        "trad": {"fr": "la carte bancaire", "en": "the bank card", "pt": "o cartão do banco", "de": "die Bankkarte"}},
    },
}
# les images de documents et ce qui est clairement faux pour chacune (les cles des documents, langue par langue)
FAUX_IMG = {
    "pass":              {"de": ["formular", "meldebescheinigung", "arbeitsvertrag", "mietvertrag", "foto", "karte", "versichertenkarte"],
                          "es": ["formulario", "certificado", "contrato", "contrato_alquiler", "foto", "tarjeta", "tarjeta_sanitaria"]},
    "formular":          {"de": ["pass", "versichertenkarte", "foto", "karte"], "es": ["pasaporte", "tarjeta_sanitaria", "foto", "tarjeta"]},
    "bescheinigung":     {"de": ["pass", "versichertenkarte", "foto", "karte"], "es": ["pasaporte", "tarjeta_sanitaria", "foto", "tarjeta"]},
    "versichertenkarte": {"de": ["pass", "formular", "meldebescheinigung", "arbeitsvertrag", "mietvertrag", "foto"],
                          "es": ["pasaporte", "formulario", "certificado", "contrato", "contrato_alquiler", "foto"]},
    "arbeitsvertrag":    {"de": ["pass", "versichertenkarte", "foto", "karte"], "es": ["pasaporte", "tarjeta_sanitaria", "foto", "tarjeta"]},
    "mietvertrag":       {"de": ["pass", "versichertenkarte", "foto", "karte"], "es": ["pasaporte", "tarjeta_sanitaria", "foto", "tarjeta"]},
    "foto":              {"de": ["formular", "meldebescheinigung", "arbeitsvertrag", "mietvertrag", "karte", "versichertenkarte"],
                          "es": ["formulario", "certificado", "contrato", "contrato_alquiler", "tarjeta", "tarjeta_sanitaria"]},
    "karte":             {"de": ["pass", "formular", "meldebescheinigung", "arbeitsvertrag", "mietvertrag", "foto"],
                          "es": ["pasaporte", "formulario", "certificado", "contrato", "contrato_alquiler", "foto"]},
}

# ---------------------------------------------------------------------------------------------------------------
# LES DEMARCHES de Mark. v : l'infinitif du corpus (la page prend sa conjugaison, praesens er_sie_es, et sa forme
# polie : sie_Sie en allemand, le subjonctif « usted » en espagnol) ; obj : apres le verbe ; lieu : la cle d'un lieu
# (None : pas de lieu dans la phrase) ; aussi : les autres lieux ou elle peut se faire (jamais un leurre de « Wo? ») ;
# aussi_v : les autres verbes qui iraient avec cet objet (jamais un leurre) ; img : l'image d'action (None : pas
# d'image) ; sie : l'objet dans la phrase polie (None : pas de phrase polie) ; t : les traductions de la phrase de Mark,
# {L} = le lieu ; ts : celles de la phrase polie.
DEMARCHES = {
    "de": [
        {"id": "nummer", "v": "ziehen", "aussi_v": ["zeigen", "mitbringen", "abholen", "abgeben"], "obj": "eine Nummer", "lieu": "buergeramt", "aussi": ["krankenkasse", "bank"], "img": "nummer", "sie": "eine Nummer",
         "t": {"fr": "Mark prend un numéro{L}.", "en": "Mark takes a number{L}.", "pt": "Mark tira uma senha{L}."},
         "ts": {"fr": "Prenez un numéro, s'il vous plaît.", "en": "Please take a number.", "pt": "Tire uma senha, por favor."}},
        {"id": "formular", "v": "ausfüllen", "aussi_v": ["unterschreiben", "mitbringen", "abgeben", "zeigen", "abholen"], "obj": "das Formular", "lieu": "buergeramt", "aussi": ["*"], "img": "ausfuellen", "sie": "das Formular",
         "t": {"fr": "Mark remplit le formulaire{L}.", "en": "Mark fills in the form{L}.", "pt": "Mark preenche o formulário{L}."},
         "ts": {"fr": "Remplissez le formulaire, s'il vous plaît.", "en": "Please fill in the form.", "pt": "Preencha o formulário, por favor."}},
        {"id": "anmelden", "v": "anmelden", "aussi_v": ["zeigen", "abgeben", "bezahlen"], "obj": "seine Wohnung", "lieu": "buergeramt", "aussi": [], "img": None, "sie": "Ihre Wohnung",
         "t": {"fr": "Mark déclare son appartement{L}.", "en": "Mark registers his flat{L}.", "pt": "Mark registra o seu apartamento{L}."},
         "ts": {"fr": "Déclarez votre appartement, s'il vous plaît.", "en": "Please register your flat.", "pt": "Registre o seu apartamento, por favor."}},
        {"id": "zeigen_pass", "v": "zeigen", "aussi_v": ["mitbringen", "abholen", "abgeben", "unterschreiben"], "obj": "seinen Pass", "lieu": "buergeramt", "aussi": ["bank"], "img": "pass_zeigen", "sie": "Ihren Pass",
         "t": {"fr": "Mark montre son passeport{L}.", "en": "Mark shows his passport{L}.", "pt": "Mark mostra o seu passaporte{L}."},
         "ts": {"fr": "Montrez votre passeport, s'il vous plaît.", "en": "Please show your passport.", "pt": "Mostre o seu passaporte, por favor."}},
        {"id": "abholen", "v": "abholen", "aussi_v": ["zeigen", "mitbringen", "abgeben", "unterschreiben", "bezahlen"], "obj": "seine Meldebescheinigung", "lieu": "buergeramt", "aussi": [], "img": "abholen", "sie": "Ihre Meldebescheinigung",
         "t": {"fr": "Mark va chercher son attestation de domicile{L}.", "en": "Mark collects his registration certificate{L}.", "pt": "Mark busca o seu comprovante de residência{L}."},
         "ts": {"fr": "Venez chercher votre attestation de domicile, s'il vous plaît.", "en": "Please collect your registration certificate.", "pt": "Busque o seu comprovante de residência, por favor."}},
        {"id": "bezahlen", "v": "bezahlen", "aussi_v": [], "obj": "die Gebühr", "lieu": "buergeramt", "aussi": ["*"], "img": None, "sie": "die Gebühr",
         "t": {"fr": "Mark paie les frais{L}.", "en": "Mark pays the fee{L}.", "pt": "Mark paga a taxa{L}."},
         "ts": {"fr": "Payez les frais, s'il vous plaît.", "en": "Please pay the fee.", "pt": "Pague a taxa, por favor."}},
        {"id": "konto", "v": "eröffnen", "aussi_v": [], "obj": "ein Konto", "lieu": "bank", "aussi": [], "img": "konto", "sie": None,
         "t": {"fr": "Mark ouvre un compte{L}.", "en": "Mark opens an account{L}.", "pt": "Mark abre uma conta{L}."}},
        {"id": "geld", "v": "abheben", "aussi_v": ["abholen", "mitbringen", "abgeben", "bezahlen", "ziehen"], "obj": "Geld", "lieu": "bank", "aussi": [], "img": "geld", "sie": None,
         "t": {"fr": "Mark retire de l'argent{L}.", "en": "Mark withdraws money{L}.", "pt": "Mark saca dinheiro{L}."}},
        {"id": "foto", "v": "abgeben", "aussi_v": ["mitbringen", "zeigen", "abholen"], "obj": "ein Foto", "lieu": "krankenkasse", "aussi": ["buergeramt"], "img": None, "sie": "ein Foto",
         "t": {"fr": "Mark remet une photo{L}.", "en": "Mark hands in a photo{L}.", "pt": "Mark entrega uma foto{L}."},
         "ts": {"fr": "Remettez une photo, s'il vous plaît.", "en": "Please hand in a photo.", "pt": "Entregue uma foto, por favor."}},
        {"id": "termin", "v": "vereinbaren", "aussi_v": ["anmelden"], "obj": "einen Termin", "lieu": "praxis", "aussi": ["*"], "img": "telefon", "sie": "einen Termin",
         "t": {"fr": "Mark prend rendez-vous{L}.", "en": "Mark makes an appointment{L}.", "pt": "Mark marca uma consulta{L}."},
         "ts": {"fr": "Prenez rendez-vous, s'il vous plaît.", "en": "Please make an appointment.", "pt": "Marque um horário, por favor."}},
        {"id": "zeigen_karte", "v": "zeigen", "aussi_v": ["mitbringen", "abholen", "abgeben", "unterschreiben"], "obj": "seine Versichertenkarte", "lieu": "praxis", "aussi": ["krankenkasse"], "img": "karte_zeigen", "sie": "Ihre Versichertenkarte",
         "t": {"fr": "Mark montre sa carte d'assurance maladie{L}.", "en": "Mark shows his health insurance card{L}.", "pt": "Mark mostra a sua carteirinha do seguro de saúde{L}."},
         "ts": {"fr": "Montrez votre carte d'assurance maladie, s'il vous plaît.", "en": "Please show your health insurance card.", "pt": "Mostre a sua carteirinha do seguro de saúde, por favor."}},
        {"id": "warten", "v": "warten", "aussi_v": [], "obj": "", "lieu": "praxis", "aussi": ["*"], "img": "warten", "sie": "im Wartezimmer",
         "t": {"fr": "Mark attend{L}.", "en": "Mark is waiting{L}.", "pt": "Mark espera{L}."},
         "ts": {"fr": "Attendez dans la salle d'attente, s'il vous plaît.", "en": "Please wait in the waiting room.", "pt": "Espere na sala de espera, por favor."}},
        {"id": "unterschreiben", "v": "unterschreiben", "aussi_v": ["zeigen", "mitbringen", "abholen", "abgeben"], "obj": "den Arbeitsvertrag", "lieu": None, "aussi": [], "img": "unterschreiben", "sie": "hier",
         "t": {"fr": "Mark signe le contrat de travail.", "en": "Mark signs the employment contract.", "pt": "Mark assina o contrato de trabalho."},
         "ts": {"fr": "Signez ici, s'il vous plaît.", "en": "Please sign here.", "pt": "Assine aqui, por favor."}},
        {"id": "mitbringen", "v": "mitbringen", "aussi_v": ["unterschreiben", "zeigen", "abholen", "abgeben"], "obj": "seinen Arbeitsvertrag", "lieu": None, "aussi": [], "img": None, "sie": "Ihren Arbeitsvertrag",
         "t": {"fr": "Mark apporte son contrat de travail.", "en": "Mark brings his employment contract.", "pt": "Mark traz o seu contrato de trabalho."},
         "ts": {"fr": "Apportez votre contrat de travail, s'il vous plaît.", "en": "Please bring your employment contract.", "pt": "Traga o seu contrato de trabalho, por favor."}},
    ],
    "es": [
        {"id": "nummer", "v": "sacar", "aussi_v": ["pedir", "recoger", "enseñar"], "obj": "un número", "lieu": "oficina", "aussi": ["banco", "consulta"], "img": "nummer", "sie": "un número",
         "t": {"fr": "Mark prend un numéro{L}.", "en": "Mark takes a number{L}.", "pt": "Mark tira uma senha{L}.", "de": "Mark zieht {L} eine Nummer."},
         "ts": {"fr": "Prenez un numéro, s'il vous plaît.", "en": "Please take a number.", "pt": "Tire uma senha, por favor.", "de": "Ziehen Sie bitte eine Nummer."}},
        {"id": "formular", "v": "rellenar", "aussi_v": ["firmar", "pedir", "recoger", "traer", "enseñar", "sacar", "abrir"], "obj": "el formulario", "lieu": "oficina", "aussi": ["*"], "img": "ausfuellen", "sie": "el formulario",
         "t": {"fr": "Mark remplit le formulaire{L}.", "en": "Mark fills in the form{L}.", "pt": "Mark preenche o formulário{L}.", "de": "Mark füllt {L} das Formular aus."},
         "ts": {"fr": "Remplissez le formulaire, s'il vous plaît.", "en": "Please fill in the form.", "pt": "Preencha o formulário, por favor.", "de": "Füllen Sie bitte das Formular aus."}},
        {"id": "certificado", "v": "pedir", "aussi_v": ["sacar", "recoger", "enseñar", "traer", "firmar"], "obj": "un certificado de empadronamiento", "lieu": "oficina", "aussi": [], "img": None, "sie": None,
         "t": {"fr": "Mark demande une attestation de domicile{L}.", "en": "Mark asks for a registration certificate{L}.", "pt": "Mark pede um comprovante de residência{L}.", "de": "Mark beantragt {L} eine Meldebescheinigung."}},
        {"id": "zeigen_pass", "v": "enseñar", "aussi_v": ["traer", "recoger", "pedir", "sacar", "abrir", "firmar"], "obj": "su pasaporte", "lieu": "oficina", "aussi": ["banco"], "img": "pass_zeigen", "sie": "su pasaporte",
         "t": {"fr": "Mark montre son passeport{L}.", "en": "Mark shows his passport{L}.", "pt": "Mark mostra o seu passaporte{L}.", "de": "Mark zeigt {L} seinen Pass."},
         "ts": {"fr": "Montrez votre passeport, s'il vous plaît.", "en": "Please show your passport.", "pt": "Mostre o seu passaporte, por favor.", "de": "Zeigen Sie bitte Ihren Pass."}},
        {"id": "abholen", "v": "recoger", "aussi_v": ["pedir", "sacar", "enseñar", "traer", "firmar"], "obj": "su certificado", "lieu": "oficina", "aussi": [], "img": "abholen", "sie": "su certificado",
         "t": {"fr": "Mark va chercher son attestation{L}.", "en": "Mark collects his certificate{L}.", "pt": "Mark busca o seu comprovante{L}.", "de": "Mark holt {L} seine Bescheinigung ab."},
         "ts": {"fr": "Venez chercher votre attestation, s'il vous plaît.", "en": "Please collect your certificate.", "pt": "Busque o seu comprovante, por favor.", "de": "Holen Sie bitte Ihre Bescheinigung ab."}},
        {"id": "konto", "v": "abrir", "aussi_v": [], "obj": "una cuenta", "lieu": "banco", "aussi": [], "img": "konto", "sie": None,
         "t": {"fr": "Mark ouvre un compte{L}.", "en": "Mark opens an account{L}.", "pt": "Mark abre uma conta{L}.", "de": "Mark eröffnet {L} ein Konto."}},
        {"id": "geld", "v": "sacar", "aussi_v": ["pedir", "recoger", "traer", "enseñar"], "obj": "dinero", "lieu": "banco", "aussi": [], "img": "geld", "sie": None,
         "t": {"fr": "Mark retire de l'argent{L}.", "en": "Mark withdraws money{L}.", "pt": "Mark saca dinheiro{L}.", "de": "Mark hebt {L} Geld ab."}},
        {"id": "termin", "v": "pedir", "aussi_v": ["sacar"], "obj": "cita", "lieu": "consulta", "aussi": ["*"], "img": "telefon", "sie": "cita",
         "t": {"fr": "Mark prend rendez-vous{L}.", "en": "Mark makes an appointment{L}.", "pt": "Mark marca uma consulta{L}.", "de": "Mark vereinbart {L} einen Termin."},
         "ts": {"fr": "Prenez rendez-vous, s'il vous plaît.", "en": "Please make an appointment.", "pt": "Marque um horário, por favor.", "de": "Vereinbaren Sie bitte einen Termin."}},
        {"id": "zeigen_karte", "v": "enseñar", "aussi_v": ["traer", "recoger", "pedir", "sacar", "firmar"], "obj": "su tarjeta sanitaria", "lieu": "consulta", "aussi": [], "img": "karte_zeigen", "sie": "su tarjeta sanitaria",
         "t": {"fr": "Mark montre sa carte d'assurance maladie{L}.", "en": "Mark shows his health card{L}.", "pt": "Mark mostra o seu cartão de saúde{L}.", "de": "Mark zeigt {L} seine Versichertenkarte."},
         "ts": {"fr": "Montrez votre carte d'assurance maladie, s'il vous plaît.", "en": "Please show your health card.", "pt": "Mostre o seu cartão de saúde, por favor.", "de": "Zeigen Sie bitte Ihre Versichertenkarte."}},
        {"id": "warten", "v": "esperar", "aussi_v": [], "obj": "", "lieu": "consulta", "aussi": ["*"], "img": "warten", "sie": "aquí",
         "t": {"fr": "Mark attend{L}.", "en": "Mark is waiting{L}.", "pt": "Mark espera{L}.", "de": "Mark wartet {L}."},
         "ts": {"fr": "Attendez ici, s'il vous plaît.", "en": "Please wait here.", "pt": "Espere aqui, por favor.", "de": "Warten Sie bitte hier."}},
        {"id": "unterschreiben", "v": "firmar", "aussi_v": ["traer", "enseñar", "recoger", "pedir", "sacar"], "obj": "el contrato de trabajo", "lieu": None, "aussi": [], "img": "unterschreiben", "sie": "aquí",
         "t": {"fr": "Mark signe le contrat de travail.", "en": "Mark signs the employment contract.", "pt": "Mark assina o contrato de trabalho.", "de": "Mark unterschreibt den Arbeitsvertrag."},
         "ts": {"fr": "Signez ici, s'il vous plaît.", "en": "Please sign here.", "pt": "Assine aqui, por favor.", "de": "Unterschreiben Sie bitte hier."}},
        {"id": "mitbringen", "v": "traer", "aussi_v": ["firmar", "enseñar", "recoger", "pedir", "sacar"], "obj": "su contrato de trabajo", "lieu": None, "aussi": [], "img": None, "sie": "su contrato de trabajo",
         "t": {"fr": "Mark apporte son contrat de travail.", "en": "Mark brings his employment contract.", "pt": "Mark traz o seu contrato de trabalho.", "de": "Mark bringt seinen Arbeitsvertrag mit."},
         "ts": {"fr": "Apportez votre contrat de travail, s'il vous plaît.", "en": "Please bring your employment contract.", "pt": "Traga o seu contrato de trabalho, por favor.", "de": "Bringen Sie bitte Ihren Arbeitsvertrag mit."}},
    ],
}

# ---------------------------------------------------------------------------------------------------------------
# LE FORMULAIRE DE MARK. Chaque case : label (affiche), mot / genre (le mot du corpus que la case fait travailler),
# v (la valeur, la meme partout), faux (des valeurs fausses pour Mark, pour « vrai ou faux »), vf (False : pas de
# « vrai ou faux » sur cette case), t : {langue: [le label avec l'article pour une phrase, le label court, la valeur
# traduite (None = la meme)]}.
CHAMPS = {
    "de": {
        "familienname": {"label": "Familienname", "mot": "Familienname", "genre": "der", "v": "Garnier", "faux": ["Garnet", "Gardner"],
                         "t": {"fr": ["le nom de famille", "Nom de famille", None], "en": ["surname", "Surname", None], "pt": ["o sobrenome", "Sobrenome", None]}},
        "vorname":      {"label": "Vorname", "mot": "Vorname", "genre": "der", "v": "Mark", "faux": ["Marc", "Max"],
                         "t": {"fr": ["le prénom", "Prénom", None], "en": ["first name", "First name", None], "pt": ["o nome", "Nome", None]}},
        "geburtsdatum": {"label": "Geburtsdatum", "mot": "Geburtsdatum", "genre": "das", "v": "14.03.2001", "faux": ["14.08.2001", "13.04.2001"], "satz": "der 14.03.2001",
                         "t": {"fr": ["la date de naissance", "Date de naissance", "14/03/2001"], "en": ["date of birth", "Date of birth", "14/03/2001"], "pt": ["a data de nascimento", "Data de nascimento", "14/03/2001"]}},
        "geburtsort":   {"label": "Geburtsort", "mot": "Geburtsort", "genre": "der", "v": "Montréal", "faux": ["Berlin", "Toronto"],
                         "t": {"fr": ["le lieu de naissance", "Lieu de naissance", None], "en": ["place of birth", "Place of birth", None], "pt": ["o local de nascimento", "Local de nascimento", None]}},
        "staat":        {"label": "Staatsangehörigkeit", "mot": "Staatsangehörigkeit", "genre": "die", "v": "kanadisch", "faux": ["französisch", "amerikanisch"],
                         "t": {"fr": ["la nationalité", "Nationalité", "canadienne"], "en": ["nationality", "Nationality", "Canadian"], "pt": ["a nacionalidade", "Nacionalidade", "canadense"]},
                         "tf": {"französisch": ["française", "French", "francesa"], "amerikanisch": ["américaine", "American", "americana"]}},
        "familienstand": {"label": "Familienstand", "mot": "Familienstand", "genre": "der", "v": "ledig", "faux": ["verheiratet", "geschieden"], "adj": True,
                         "t": {"fr": ["la situation familiale", "Situation familiale", "célibataire"], "en": ["marital status", "Marital status", "single"], "pt": ["o estado civil", "Estado civil", "solteiro"]},
                         "tf": {"verheiratet": ["marié", "married", "casado"], "geschieden": ["divorcé", "divorced", "divorciado"]}},
        "adresse":      {"label": "Adresse", "mot": "Adresse", "genre": "die", "v": "Gartenstraße 12", "faux": ["Gartenstraße 21", "Gartenweg 12"],
                         "t": {"fr": ["l'adresse", "Adresse", None], "en": ["address", "Address", None], "pt": ["o endereço", "Endereço", None]}},
        "plz":          {"label": "Postleitzahl", "mot": "Postleitzahl", "genre": "die", "v": "13187", "faux": ["13178", "10187"],
                         "t": {"fr": ["le code postal", "Code postal", None], "en": ["postcode", "Postcode", None], "pt": ["o CEP", "CEP", None]}},
        "ort":          {"label": "Ort", "mot": "Ort", "genre": "der", "v": "Berlin", "faux": ["Hamburg", "Montréal"], "vf": False,
                         "t": {"fr": ["la ville", "Ville", None], "en": ["town", "Town", None], "pt": ["a cidade", "Cidade", None]}},
        "telefon":      {"label": "Telefonnummer", "mot": "Telefonnummer", "genre": "die", "v": "0176 23 81 45 09", "faux": ["0176 23 18 45 09", "030 23 81 45 09"],
                         "t": {"fr": ["le numéro de téléphone", "Numéro de téléphone", None], "en": ["phone number", "Phone number", None], "pt": ["o número de telefone", "Telefone", None]}},
        "beruf":        {"label": "Beruf", "mot": "Beruf", "genre": "der", "v": "Praktikant", "faux": ["Lehrer", "Arzt"],
                         "t": {"fr": ["la profession", "Profession", "stagiaire"], "en": ["occupation", "Occupation", "intern"], "pt": ["a profissão", "Profissão", "estagiário"]},
                         "tf": {"Lehrer": ["professeur", "teacher", "professor"], "Arzt": ["médecin", "doctor", "médico"]}},
        "datum":        {"label": "Datum", "mot": "Datum", "genre": "das", "v": "10.11.2026", "faux": ["01.11.2026", "10.12.2026"], "vf": False,
                         "t": {"fr": ["la date", "Date", "10/11/2026"], "en": ["date", "Date", "10/11/2026"], "pt": ["a data", "Data", "10/11/2026"]}},
        "unterschrift": {"label": "Unterschrift", "mot": "Unterschrift", "genre": "die", "v": "✍", "faux": [], "vf": False, "signature": True,
                         "t": {"fr": ["la signature", "Signature", None], "en": ["signature", "Signature", None], "pt": ["a assinatura", "Assinatura", None]}},
    },
    "es": {
        "nombre":      {"label": "Nombre", "mot": "nombre", "genre": "el", "v": "Mark", "faux": ["Marco", "Max"],
                        "t": {"fr": ["le prénom", "Prénom", None], "en": ["first name", "First name", None], "pt": ["o nome", "Nome", None], "de": ["der Vorname", "Vorname", None]}},
        "apellidos":   {"label": "Apellidos", "mot": "apellido", "genre": "el", "v": "Garnier", "faux": ["García", "Gardner"], "satz": "Garnier",
                        "t": {"fr": ["le nom de famille", "Nom de famille", None], "en": ["surname", "Surname", None], "pt": ["o sobrenome", "Sobrenome", None], "de": ["der Familienname", "Familienname", None]}},
        "nacimiento":  {"label": "Fecha de nacimiento", "mot": "fecha de nacimiento", "genre": "la", "v": "14/03/2001", "faux": ["14/08/2001", "13/04/2001"],
                        "t": {"fr": ["la date de naissance", "Date de naissance", None], "en": ["date of birth", "Date of birth", None], "pt": ["a data de nascimento", "Data de nascimento", None], "de": ["das Geburtsdatum", "Geburtsdatum", "14.03.2001"]}},
        "lugar":       {"label": "Lugar de nacimiento", "mot": "lugar de nacimiento", "genre": "el", "v": "Ciudad de México", "faux": ["Madrid", "Guadalajara"],
                        "t": {"fr": ["le lieu de naissance", "Lieu de naissance", "Mexico"], "en": ["place of birth", "Place of birth", "Mexico City"], "pt": ["o local de nascimento", "Local de nascimento", "Cidade do México"], "de": ["der Geburtsort", "Geburtsort", "Mexiko-Stadt"]},
                        "tf": {"Madrid": ["Madrid", "Madrid", "Madri", "Madrid"], "Guadalajara": ["Guadalajara", "Guadalajara", "Guadalajara", "Guadalajara"]}},
        "nacionalidad": {"label": "Nacionalidad", "mot": "nacionalidad", "genre": "la", "v": "mexicana", "faux": ["española", "colombiana"],
                        "t": {"fr": ["la nationalité", "Nationalité", "mexicaine"], "en": ["nationality", "Nationality", "Mexican"], "pt": ["a nacionalidade", "Nacionalidade", "mexicana"], "de": ["die Staatsangehörigkeit", "Staatsangehörigkeit", "mexikanisch"]},
                        "tf": {"española": ["espagnole", "Spanish", "espanhola", "spanisch"], "colombiana": ["colombienne", "Colombian", "colombiana", "kolumbianisch"]}},
        "estado":      {"label": "Estado civil", "mot": "estado civil", "genre": "el", "v": "soltero", "faux": ["casado", "divorciado"], "adj": "soltero",
                        "t": {"fr": ["la situation familiale", "Situation familiale", "célibataire"], "en": ["marital status", "Marital status", "single"], "pt": ["o estado civil", "Estado civil", "solteiro"], "de": ["der Familienstand", "Familienstand", "ledig"]},
                        "tf": {"casado": ["marié", "married", "casado", "verheiratet"], "divorciado": ["divorcé", "divorced", "divorciado", "geschieden"]}},
        "direccion":   {"label": "Dirección", "mot": "dirección", "genre": "la", "v": "calle de la Luna 12, 2.º B", "faux": ["calle de la Luna 21, 2.º B", "calle del Sol 12, 2.º B"],
                        "t": {"fr": ["l'adresse", "Adresse", None], "en": ["address", "Address", None], "pt": ["o endereço", "Endereço", None], "de": ["die Adresse", "Adresse", None]}},
        "cp":          {"label": "Código postal", "mot": "código postal", "genre": "el", "v": "28004", "faux": ["28040", "28014"],
                        "t": {"fr": ["le code postal", "Code postal", None], "en": ["postcode", "Postcode", None], "pt": ["o CEP", "CEP", None], "de": ["die Postleitzahl", "Postleitzahl", None]}},
        "municipio":   {"label": "Municipio", "mot": None, "genre": None, "v": "Madrid", "faux": [], "vf": False,
                        "t": {"fr": ["la commune", "Commune", None], "en": ["town", "Town", None], "pt": ["o município", "Município", None], "de": ["der Ort", "Ort", None]}},
        "telefono":    {"label": "Teléfono", "mot": "teléfono", "genre": "el", "v": "612 48 30 17", "faux": ["612 48 03 17", "621 48 30 17"],
                        "t": {"fr": ["le téléphone", "Téléphone", None], "en": ["phone number", "Phone number", None], "pt": ["o telefone", "Telefone", None], "de": ["die Telefonnummer", "Telefonnummer", None]}},
        "fecha":       {"label": "Fecha", "mot": "fecha", "genre": "la", "v": "10/11/2026", "faux": ["01/11/2026", "10/12/2026"], "vf": False,
                        "t": {"fr": ["la date", "Date", None], "en": ["date", "Date", None], "pt": ["a data", "Data", None], "de": ["das Datum", "Datum", "10.11.2026"]}},
        "firma":       {"label": "Firma", "mot": "firma", "genre": "la", "v": "✍", "faux": [], "vf": False, "signature": True,
                        "t": {"fr": ["la signature", "Signature", None], "en": ["signature", "Signature", None], "pt": ["a assinatura", "Assinatura", None], "de": ["die Unterschrift", "Unterschrift", None]}},
    },
}
# Les formulaires : le titre, le lieu, les cases dans l'ordre (celles d'un vrai formulaire de ce lieu)
FORMULAIRES = {
    "de": [{"id": "anmeldung", "titre": "Anmeldung einer Wohnung", "lieu": "buergeramt",
            "champs": ["familienname", "vorname", "geburtsdatum", "geburtsort", "staat", "familienstand", "adresse", "plz", "ort", "datum", "unterschrift"]},
           {"id": "konto", "titre": "Antrag auf Kontoeröffnung", "lieu": "bank",
            "champs": ["familienname", "vorname", "geburtsdatum", "staat", "adresse", "plz", "ort", "telefon", "beruf", "datum", "unterschrift"]},
           {"id": "patient", "titre": "Patientenbogen", "lieu": "praxis",
            "champs": ["familienname", "vorname", "geburtsdatum", "adresse", "plz", "ort", "telefon", "beruf", "datum", "unterschrift"]}],
    "es": [{"id": "padron", "titre": "Hoja de empadronamiento", "lieu": "oficina",
            "champs": ["nombre", "apellidos", "nacimiento", "lugar", "nacionalidad", "estado", "direccion", "cp", "municipio", "fecha", "firma"]},
           {"id": "cuenta", "titre": "Solicitud de apertura de cuenta", "lieu": "banco",
            "champs": ["nombre", "apellidos", "nacimiento", "nacionalidad", "direccion", "cp", "municipio", "telefono", "fecha", "firma"]},
           {"id": "paciente", "titre": "Ficha del paciente", "lieu": "consulta",
            "champs": ["nombre", "apellidos", "nacimiento", "direccion", "cp", "telefono", "fecha", "firma"]}],
}

# ---------------------------------------------------------------------------------------------------------------
# LES AVIS « BITTE BRINGEN SIE MIT » : pour chaque demarche, les documents a apporter (ce qu'on demande vraiment :
# l'Anmeldung demande le passeport, le formulaire et l'attestation du proprietaire -- la Wohnungsgeberbestaetigung ;
# la banque, le passeport et l'attestation de domicile ; la carte d'assurance, une photo et le contrat de travail).
# pour : « Fuer die Anmeldung » ; t : la meme chose, traduite.
AVIS = {
    "de": [{"id": "anmeldung", "lieu": "buergeramt", "titre": "Anmeldung einer Wohnung", "pour": "Für die Anmeldung", "docs": ["pass", "formular", "bestaetigung"],
            "t": {"fr": "Pour déclarer son domicile", "en": "To register your address", "pt": "Para registrar o endereço"}},
           {"id": "konto", "lieu": "bank", "titre": "Ein Konto eröffnen", "pour": "Für ein Konto", "docs": ["pass", "meldebescheinigung"],
            "t": {"fr": "Pour ouvrir un compte", "en": "To open an account", "pt": "Para abrir uma conta"}},
           {"id": "karte", "lieu": "krankenkasse", "titre": "Ihre Versichertenkarte", "pour": "Für die Versichertenkarte", "docs": ["foto", "arbeitsvertrag"],
            "t": {"fr": "Pour la carte d'assurance maladie", "en": "For the health insurance card", "pt": "Para a carteirinha do seguro de saúde"}},
           {"id": "arzt", "lieu": "praxis", "titre": "Ihr erster Termin", "pour": "Für den ersten Termin", "docs": ["versichertenkarte"],
            "t": {"fr": "Pour le premier rendez-vous", "en": "For the first appointment", "pt": "Para a primeira consulta"}},
           {"id": "aufenthalt", "lieu": None, "carte": "Ausländerbehörde · Merkblatt", "titre": "Aufenthaltserlaubnis", "pour": "Für die Aufenthaltserlaubnis",
            "docs": ["pass", "foto", "arbeitsvertrag", "meldebescheinigung"],
            "t": {"fr": "Pour le permis de séjour", "en": "For the residence permit", "pt": "Para a autorização de residência"}}],
    "es": [{"id": "padron", "lieu": "oficina", "titre": "Empadronamiento", "pour": "Para empadronarse", "docs": ["pasaporte", "formulario", "contrato_alquiler"],
            "t": {"fr": "Pour déclarer son domicile", "en": "To register your address", "pt": "Para registrar o endereço", "de": "Für die Anmeldung"}},
           {"id": "cuenta", "lieu": "banco", "titre": "Abrir una cuenta", "pour": "Para abrir una cuenta", "docs": ["pasaporte", "certificado"],
            "t": {"fr": "Pour ouvrir un compte", "en": "To open an account", "pt": "Para abrir uma conta", "de": "Für ein Konto"}},
           {"id": "sanitaria", "lieu": "consulta", "titre": "Tarjeta sanitaria", "pour": "Para la tarjeta sanitaria", "docs": ["pasaporte", "certificado"],
            "t": {"fr": "Pour la carte d'assurance maladie", "en": "For the health card", "pt": "Para o cartão de saúde", "de": "Für die Versichertenkarte"}},
           {"id": "medico", "lieu": "consulta", "titre": "Su primera cita", "pour": "Para la primera cita", "docs": ["tarjeta_sanitaria"],
            "t": {"fr": "Pour le premier rendez-vous", "en": "For the first appointment", "pt": "Para a primeira consulta", "de": "Für den ersten Termin"}},
           {"id": "residencia", "lieu": None, "carte": "Oficina de Extranjería · Información", "titre": "Permiso de residencia", "pour": "Para el permiso de residencia",
            "docs": ["pasaporte", "foto", "contrato", "certificado"],
            "t": {"fr": "Pour le permis de séjour", "en": "For the residence permit", "pt": "Para a autorização de residência", "de": "Für die Aufenthaltserlaubnis"}}],
}
# le mot « Termin » / « cita » (la confirmation de rendez-vous), et ses heures possibles : la page tire un jour
# OUVERT du lieu et une heure dans ses plages (un rendez-vous ne tombe jamais un jour de fermeture)
TERMIN = {"de": {"mot": "Termin", "genre": "der", "salles": ["Raum 1.04", "Raum 2.14", "Raum 3.07"]},
          "es": {"mot": "cita", "genre": "la", "salles": ["Puesto 4", "Puesto 7", "Puesto 12"]}}

# ---------------------------------------------------------------------------------------------------------------
# LES MOTS ABSENTS DU CORPUS, a ajouter PAR PAIRES (allemand et espagnol), prepares dans ajouts/demarches.json et
# espanol/ajouts/demarches.json, PAS appliques : en attendant, l'app les tient « hors jeu ». Leur traduction ici,
# pour la page (la ligne sous le mot).
AJOUTS_TRAD = {
    "de": {"Geburtsdatum": {"fr": "date de naissance", "en": "date of birth", "tr": "doğum tarihi", "uk": "дата народження", "fa": "تاریخ تولد", "ar": "تاريخ الميلاد",
                            "pt": "data de nascimento", "pl": "data urodzenia", "ru": "дата рождения"},
           "Geburtsort": {"fr": "lieu de naissance", "en": "place of birth", "tr": "doğum yeri", "uk": "місце народження", "fa": "محل تولد", "ar": "مكان الميلاد",
                          "pt": "local de nascimento", "pl": "miejsce urodzenia", "ru": "место рождения"},
           "Telefonnummer": {"fr": "numéro de téléphone", "en": "phone number", "tr": "telefon numarası", "uk": "номер телефону", "fa": "شماره تلفن", "ar": "رقم الهاتف",
                             "pt": "número de telefone", "pl": "numer telefonu", "ru": "номер телефона"},
           "Meldebescheinigung": {"fr": "attestation de domicile", "en": "registration certificate", "tr": "ikamet belgesi", "uk": "довідка про реєстрацію", "fa": "گواهی ثبت محل سکونت",
                                  "ar": "شهادة تسجيل السكن", "pt": "comprovante de residência", "pl": "zaświadczenie o zameldowaniu", "ru": "справка о регистрации"},
           "Aufenthaltserlaubnis": {"fr": "permis de séjour", "en": "residence permit", "tr": "oturma izni", "uk": "дозвіл на проживання", "fa": "اجازهٔ اقامت", "ar": "تصريح الإقامة",
                                    "pt": "autorização de residência", "pl": "zezwolenie na pobyt", "ru": "вид на жительство"}},
    "es": {"fecha de nacimiento": {"fr": "date de naissance", "en": "date of birth", "pt": "data de nascimento", "ar": "تاريخ الميلاد", "de": "Geburtsdatum"},
           "lugar de nacimiento": {"fr": "lieu de naissance", "en": "place of birth", "pt": "local de nascimento", "ar": "مكان الميلاد", "de": "Geburtsort"},
           "código postal": {"fr": "code postal", "en": "postcode", "pt": "CEP", "ar": "الرمز البريدي", "de": "Postleitzahl"},
           "estado civil": {"fr": "situation familiale", "en": "marital status", "pt": "estado civil", "ar": "الحالة الاجتماعية", "de": "Familienstand"},
           "certificado de empadronamiento": {"fr": "attestation de domicile", "en": "registration certificate", "pt": "comprovante de residência", "ar": "شهادة تسجيل السكن", "de": "Meldebescheinigung"},
           "permiso de residencia": {"fr": "permis de séjour", "en": "residence permit", "pt": "autorização de residência", "ar": "تصريح الإقامة", "de": "Aufenthaltserlaubnis"}},
}
LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}

# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES (4:3, aucun texte lisible). source : une reference (Mark de l'episode 2, le Buergeramt de l'episode 2),
# jamais une description seule de Mark. ESSAI : la planche d'essai (6 images, 0,90 $), a montrer a Jacques avant le reste.
MARK = ("The same man as in the first reference picture: exactly the same face, the same curly dark brown hair, the same age, "
        "the same build and the same clothes -- a light blue button-down shirt with the sleeves rolled to the forearm, navy "
        "trousers, a brown leather belt. He is friendly and relaxed, a slight smile. ")
LIEU_AMT = ("The place is the same old Berlin municipal office as in the second reference picture: pale mint-green walls with a darker "
            "green dado rail, cream floor tiles, high ceiling, fluorescent tubes. ")
PHOTO = (" A photorealistic photograph, natural light, natural colours, 4:3 landscape format. ABSOLUTELY NO readable text, "
         "no letters, no numbers, no logos, no signs, no captions, no watermark anywhere in the picture: every paper, screen and "
         "card is blank or blurred. Hands: five fingers each, natural. ")
IMAGES = {
    # LES DOCUMENTS, en gros plan, sur un bureau de bois clair
    "pass":              {"prompt": "Close-up of a closed dark navy blue passport booklet lying on a light wooden desk next to a pen. The cover has only a small embossed golden emblem, no words. Soft daylight."},
    "formular":          {"prompt": "Close-up of a blank official form on a light wooden desk: a printed sheet with empty rectangular boxes in rows, small empty checkboxes and a signature line, all blank, nothing written; a ballpoint pen lies across it. Seen from above at a slight angle."},
    "bescheinigung":     {"prompt": "Close-up of a single official certificate sheet on a light wooden desk: a few blurred grey lines of text that cannot be read, and one round blue official ink stamp near the bottom, with a signature scribble. Seen from above at a slight angle."},
    "versichertenkarte": {"prompt": "Close-up of a green plastic health insurance card with a small portrait photo of a young man on the left and a gold chip, lying on a doctor's reception counter, next to a small potted plant. No writing on the card."},
    "arbeitsvertrag":    {"prompt": "Close-up of a multi-page employment contract stapled at the corner on an office desk, two signature lines at the bottom, a fountain pen and a cup of coffee beside it; the text is out of focus and cannot be read."},
    "mietvertrag":       {"prompt": "Close-up of a stapled rental contract lying on a wooden table with a ring of two apartment keys placed on top of it; the text is out of focus and cannot be read."},
    "foto":              {"prompt": "Close-up of a strip of four identical small biometric passport photos of a young man with curly dark brown hair (the man of the reference), neutral expression, plain light grey background, lying on a light wooden desk next to scissors.", "source": "Mark"},
    "karte":             {"prompt": "Close-up of a hand holding a plain dark blue bank card with a gold chip in front of a card payment terminal on a counter; the card and the terminal screen show no writing."},
    # LES DEMARCHES DE MARK (retouches de son image de l'episode 2)
    "nummer":            {"source": "Mark+Buergeramt", "prompt": "He stands in the waiting hall and pulls a small paper waiting ticket from a grey ticket machine on a stand; the ticket is blank. A row of black linked chairs and the noticeboards behind him, out of focus. Seen from the side, from the waist up."},
    "ausfuellen":        {"source": "Mark+Buergeramt", "prompt": "He stands at a high standing desk by the wall of the waiting hall and fills in a paper form with a pen, concentrating, his passport lying open beside the form. The form shows only blank boxes. Seen at three quarters, from the waist up."},
    "pass_zeigen":       {"source": "Mark+Buergeramt", "prompt": "He stands at a wooden service counter and hands his closed navy passport across it to a female clerk in her fifties in a dark cardigan, who reaches out to take it. Seen from the side, both from the waist up."},
    "abholen":           {"source": "Mark+Buergeramt", "prompt": "At a wooden service counter a female clerk in her fifties in a dark cardigan hands him a single printed sheet with a round blue stamp; he takes it with a pleased smile. Seen from the side, both from the waist up. The sheet cannot be read."},
    "konto":             {"source": "Mark", "prompt": "In a bright modern bank branch he sits at an advisor's desk opposite a female bank advisor in her thirties in a blazer; she shows him a blank document on a tablet and a bank card lies on the desk between them. Seen at three quarters, from the waist up."},
    "geld":              {"source": "Mark", "prompt": "He stands at a cash machine in the wall of a bank on a street and takes banknotes out of the slot, his bank card in the other hand. The screen is blank and bright. Seen from the side, from the waist up."},
    "telefon":           {"source": "Mark", "prompt": "In his small, bright Berlin apartment he sits at a kitchen table and talks on his mobile phone, writing an appointment into a paper pocket diary with blank pages. Seen at three quarters, from the waist up."},
    "karte_zeigen":      {"source": "Mark", "prompt": "At the reception counter of a doctor's practice (white counter, a medical assistant in a white top behind it) he hands over a green plastic health insurance card. Seen from the side, from the waist up."},
    "warten":            {"source": "Mark", "prompt": "He sits on a chair in the waiting room of a doctor's practice, with white walls, a plant and a few magazines on a low table, waiting patiently with his jacket on his knees. Two other patients sit further away. Seen from the front, the whole room in the picture."},
    "unterschreiben":    {"source": "Mark", "prompt": "In a bright office he sits at a desk and signs the last page of a contract with a pen, a woman in her forties (his future boss) smiling on the other side of the desk. The paper cannot be read. Seen at three quarters, from the waist up."},
}
ESSAI = ["nummer", "ausfuellen", "konto", "pass", "versichertenkarte", "bescheinigung"]


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


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


def glose(e, langue, l):
    return e.get("traduction" if l == "fr" else "traduction_" + l)


def mots_du_theme(langue):
    """Les mots que le theme fait travailler, a la forme du corpus, et leur traduction (le corpus, sinon AJOUTS_TRAD)."""
    noms = corpus_noms(langue)
    verbes = corpus_liste("verbe.json" if langue == "de" else "espanol/datos/verbos.json", "infinitif")
    adjs = corpus_liste("adjectif.json" if langue == "de" else "espanol/datos/adjetivos.json", "mot")
    mots, absents = [], []
    def ajouter(mot, genre=None, cat=None):
        k = (mot, genre, cat)
        if k in [(m["mot"], m.get("genre"), m.get("cat")) for m in mots]:
            return
        if cat == "verbe":
            e = verbes.get(mot)
        elif cat == "adjectif":
            e = adjs.get(mot)
        else:
            e = noms.get((mot, genre))
        if e:
            g = {l: glose(e, langue, l) for l in LANGUES[langue]}
        elif mot in AJOUTS_TRAD[langue]:
            g = AJOUTS_TRAD[langue][mot]; absents.append(mot)
        else:
            sys.exit("  %s (%s) absent du corpus %s et des ajouts" % (mot, genre or cat, langue))
        manque = [l for l, v in g.items() if not v]
        if manque:
            sys.exit("  %s (%s) : pas de traduction en %s" % (mot, langue, ", ".join(manque)))
        w = {"mot": mot, "g": g}
        if genre: w["genre"] = genre
        if cat: w["cat"] = cat
        mots.append(w)
    for l in LIEUX[langue].values():
        ajouter(l["mot"], l["genre"])
    for d in DOCS[langue].values():
        ajouter(d["mot"], d["genre"])
    for d in DEMARCHES[langue]:
        ajouter(d["v"], cat="verbe")
    for c in CHAMPS[langue].values():
        if c["mot"]:
            ajouter(c["mot"], c["genre"])
        if c.get("adj"):
            ajouter(c["v"] if c["adj"] is True else c["adj"], cat="adjectif")
    for k in OUVERT[langue]:
        ajouter(k, cat="adjectif")
    ajouter(TERMIN[langue]["mot"], TERMIN[langue]["genre"])
    return mots, sorted(set(absents))


def conjugaisons(langue):
    """praesens er_sie_es et la forme polie de chaque verbe, prises au corpus (verbe.json, verbos.json)."""
    verbes = corpus_liste("verbe.json" if langue == "de" else "espanol/datos/verbos.json", "infinitif")
    out = {}
    for d in DEMARCHES[langue]:
        e = verbes[d["v"]]
        p = e["praesens"]
        if langue == "de":
            out[d["v"]] = {"er": p["er_sie_es"], "ich": p["ich"], "du": p["du"], "sie": p["sie_Sie"]}
        else:
            out[d["v"]] = {"er": p["er_sie_es"], "ich": p["ich"], "du": p["du"], "usted": e["subjuntivo"][2]}
    return out


def verifier():
    for langue in ("de", "es"):
        for d in DEMARCHES[langue]:
            if d["lieu"] and d["lieu"] not in LIEUX[langue]:
                sys.exit("  lieu inconnu : %s" % d["id"])
            if d["img"] and d["img"] not in IMAGES:
                sys.exit("  image inconnue : %s" % d["img"])
            need = ["fr", "en", "pt"] + (["de"] if langue == "es" else [])
            for cle in ("t",) + (("ts",) if d.get("sie") else ()):
                manque = [l for l in need if l not in d[cle]]
                if manque:
                    sys.exit("  %s %s : traduction %s absente (%s)" % (langue, d["id"], cle, manque))
        for a in AVIS[langue]:
            for k in a["docs"]:
                if k not in DOCS[langue]:
                    sys.exit("  avis %s : document inconnu %s" % (a["id"], k))
        for f in FORMULAIRES[langue]:
            for c in f["champs"]:
                if c not in CHAMPS[langue]:
                    sys.exit("  formulaire %s : case inconnue %s" % (f["id"], c))
        for i, fx in FAUX_IMG.items():
            for k in fx[langue]:
                if k not in DOCS[langue]:
                    sys.exit("  faux de %s : %s inconnu" % (i, k))
        imgs = {d["img"] for d in DOCS[langue].values() if d["img"]}
        if imgs - set(FAUX_IMG):
            sys.exit("  image de document sans faux : %s" % (imgs - set(FAUX_IMG)))


def ecrire_json():
    verifier()
    d = {"lieux": LIEUX, "horaires": HORAIRES, "jours": JOURS, "ouvert": OUVERT, "ouvertTrad": OUVERT_TRAD, "docs": DOCS, "fauxImg": FAUX_IMG,
         "demarches": DEMARCHES, "champs": CHAMPS, "formulaires": FORMULAIRES, "avis": AVIS, "termin": TERMIN, "mots": {}, "absents": {}, "conj": {}}
    for langue in ("de", "es"):
        d["mots"][langue], d["absents"][langue] = mots_du_theme(langue)
        d["conj"][langue] = conjugaisons(langue)
    d["images"] = {i: {"existe": os.path.exists(os.path.join(RACINE, "visuel", "prototype", "demarches", i + ".webp"))} for i in IMAGES}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    for chemin in (os.path.join(RACINE, "visuel", "prototype", "demarches", "demarches.json"),):
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    for langue in ("de", "es"):
        print("  %s : %d mots, dont %d absents du corpus (%s)" % (langue, len(d["mots"][langue]), len(d["absents"][langue]), ", ".join(d["absents"][langue])))
    return d


def images():
    out = {}
    for i, im in IMAGES.items():
        src = im.get("source")
        photo = PHOTO
        if not src:
            # un document seul : « Hands: five fingers » fait venir des mains (l'attestation de la planche d'essai,
            # 4 nov. : deux mains inconnues en manches sombres). On demande au contraire l'objet seul.
            photo = PHOTO.replace("Hands: five fingers each, natural. ", "No people and no hands in the picture: the object alone. ")
            assert photo != PHOTO
        prompt = (MARK if src and "Mark" in src else "") + (LIEU_AMT if src and "Buergeramt" in src else "") + im["prompt"] + photo
        out[i] = (src, prompt)
    return out


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
            corps["image_urls"] = [O.deposer(REFERENCES[s], "image/png", cle)[0] for s in source.split("+")]
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
