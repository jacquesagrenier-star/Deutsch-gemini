# -*- coding: utf-8 -*-
"""Les scenes en anglais : visuel/prototype/scene-<nom>.en.js.

    python anglais/outils/scenes.py            (les 37 scenes gardees)
    python anglais/outils/scenes.py kueche     (une seule)

UNE SCENE, TROIS LANGUES, UNE SEULE GEOMETRIE (decide par Jacques le 27 oct.
2026 : « servir des memes images », l'anglais a Boston). Ce script part de la
scene allemande DEJA CONSTRUITE (scene-<nom>.js, par visuel/prototype/construire.py)
et n'ecrit que le .en.js : il ne touche ni a l'allemand ni a l'espagnol.

Le mot anglais de chaque mot allemand vient de MOTS ci-dessous (une table
commune : un mot n'a qu'une traduction d'une scene a l'autre), sinon de la
traduction anglaise que la zone allemande porte deja (champ « en »). Pluriel,
niveau, theme et sens viennent du corpus anglais (anglais/datos) quand le mot y
est ; sinon la zone garde le sens francais et le niveau de l'allemand, et n'a
pas de theme (pas de carte a reviser).

Les six scenes ecartees le 27 oct. 2026 (trop europeennes pour Boston) :
EXCLUES. Les couches A2-C1 allemandes enseignent l'allemand : l'anglais n'a
que la couche A1 (decouvrir, trouver), comme l'espagnol a ses debuts.
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

EXCLUES = {"kreuzung", "ubahn", "zug", "stadtplatz", "weihnachtsmarkt", "post"}

TITRES = {
    "apotheke": "At the pharmacy", "arztpraxis": "At the doctor's office", "baeckerei": "At the bakery",
    "bauernhof": "On the farm", "bibliothek": "At the library", "buergeramt": "At City Hall",
    "buero": "At the office", "camping": "Camping by the lake", "fahrradwerkstatt": "At the bike shop",
    "familie": "Sunday dinner", "flughafen": "At Logan Airport", "friseur": "At the hair salon",
    "fruehstueck": "Breakfast at the café", "geburtstag": "A birthday party", "heimwerken": "Fixing up the apartment",
    "hotel": "At the hotel", "klassenzimmer": "In the classroom", "kleidergeschaeft": "At the clothing store",
    "kueche": "In the kitchen", "markt-gemuese-frucht": "At the farmers market",
    "markt-gemuese-wurzel": "At the farmers market", "markt-obst-heimisch": "At the farmers market",
    "markt-obst-sued": "At the farmers market", "museum": "At the museum", "musik": "Music at home",
    "park": "On Boston Common", "restaurant": "At the restaurant", "schlafzimmer": "In the bedroom",
    "sportplatz": "On the soccer field", "strand": "At the beach", "supermarkt": "At the supermarket",
    "umzug": "Moving day", "untersuchung": "The checkup", "untersuchung-dos": "The checkup",
    "waschsalon": "At the laundromat", "winter": "A snowy day in Boston", "wohnzimmer": "In the living room",
}

# Le mot anglais (americain) quand la traduction de la zone allemande ne
# convient pas : britannique, double sens, ou deux mots allemands qui
# tomberaient sur le meme mot anglais dans une scene. « gb » : le mot
# britannique quand il differe et que le corpus ne le donne pas deja.
MOTS = {
    "Boden": "floor", "Brust": "chest", "Brötchen": "roll", "Einkaufswagen": "shopping cart|gb=trolley",
    "Fahrrad": "bike", "Flugzeug": "plane", "Frau": "woman", "Mann": "man", "Gemüse": "vegetables",
    "Gesäß": "bottom", "Po": "bottom", "Handfläche": "palm", "Kanne": "pitcher|gb=jug", "Karte": "card",
    "Karton": "cardboard box", "Kasse": "cash register|gb=till", "Kiste": "crate", "Klebeband": "tape",
    "Klingel": "doorbell", "Kugelschreiber": "ballpoint pen", "Kühlschrank": "fridge",
    "Lichterkette": "string lights|gb=fairy lights", "Liege": "exam table|gb=examination couch",
    "Mais": "corn|gb=sweetcorn", "Medikament": "medicine", "Mütze": "winter hat|gb=woolly hat",
    "Netz": "net", "Oma": "grandma", "Opa": "grandpa", "Pfeife": "whistle", "Pflaster": "Band-Aid|gb=plaster",
    "Portemonnaie": "wallet", "Rad": "wheel", "Rote Bete": "beet|gb=beetroot", "Salat": "lettuce",
    "Schalter": "counter", "Theke": "counter", "Schrank": "closet", "Sonnenschirm": "beach umbrella|gb=parasol",
    "Sportplatz": "soccer field|gb=football pitch", "Stand": "stand", "Steckdose": "outlet|gb=socket",
    "Stock": "stick", "Tablette": "pill", "Taschentuch": "tissue", "Telefon": "phone", "Teppich": "carpet",
    "Torte": "layer cake|gb=gateau", "Turnschuh": "sneaker", "Uhr": "clock", "Verband": "bandage",
    "Verkäuferin": "salesperson", "Versichertenkarte": "insurance card", "Waage": "scale|gb=scales",
    "Wasserhahn": "faucet", "Weg": "path", "Zeitschrift": "magazine", "Zettel": "note",
    "Zollstock": "folding ruler", "Ärztin": "doctor", "Studentin": "student", "Teilnehmerin": "participant",
    "Isomatte": "sleeping pad|gb=sleeping mat", "Mülleimer": "trash can|gb=bin", "Aubergine": "eggplant|gb=aubergine",
    "Zucchini": "zucchini|gb=courgette", "Paprika": "bell pepper|gb=pepper", "Handy": "cell phone",
    "Kissen": "cushion", "Mauer": "stone wall", "Schachtel": "box", "Tüte": "paper bag", "Tasche": "bag",
    "Kopfhörer": "headphones", "Erdapfel": "potato", "Schwammerl": "mushroom", "Rüebli": "carrot",
    "Marille": "apricot", "Apfelsine": "orange", "Heidelbeere": "blueberry", "Blaubeere": "blueberry",
    "Mutter": "mother", "Karotte": "carrot", "Laterne": "street lamp|gb=street lamp", "Fußball": "soccer ball|gb=football",
    "Bügeleisen": "iron", "Dose": "can|gb=tin", "Couchtisch": "coffee table", "Pinsel": "paintbrush",
    "Bürste": "brush", "Rezeption": "front desk|gb=reception", "Schaufenster": "store window|gb=shop window",
    "Kreide": "chalk", "Nachttisch": "nightstand|gb=bedside table", "Nacken": "back of the neck",
    "Kniekehle": "back of the knee", "Verkehrszeichen": "road sign", "Waschmittel": "laundry detergent|gb=washing powder",
    "Trikot": "jersey|gb=shirt", "Note": "grade", "Rasen": "lawn", "Wiese": "meadow",
}

# Les noms qui ne se comptent pas : pas de pluriel, si le corpus ne le dit pas.
INDENOMBRABLES = {"bread", "butter", "cheese", "meat", "milk", "rice", "salt", "sugar", "water", "coffee", "tea",
                  "juice", "beer", "wine", "oil", "ham", "flour", "sand", "smoke", "steam", "snow", "grass", "hair",
                  "money", "luggage", "paper", "wood", "fire", "tape", "chalk", "laundry detergent", "washing powder",
                  "spinach", "chard", "celery", "lettuce", "garlic", "corn", "sweetcorn", "broccoli", "asparagus",
                  "rhubarb", "fennel", "kohlrabi", "string lights", "fairy lights", "headphones", "pants", "jeans",
                  "scissors", "pliers", "glasses", "vegetables", "fruit", "medicine", "heating", "furniture"}


def charger_scene(nom):
    t = io.open(os.path.join(PROTO, "scene-%s.js" % nom), encoding="utf-8").read()
    return json.loads(t[t.index("{"):t.rindex("}") + 1])


def corpus():
    """mot americain -> {pluriel, niveau, theme, fr, gb, plgb} ; et le britannique."""
    us = json.load(io.open(os.path.join(RACINE, "anglais", "datos", "themes.json"), encoding="utf-8"))["themes"]
    gb = json.load(io.open(os.path.join(RACINE, "anglais", "datos-gb", "themes.json"), encoding="utf-8"))["themes"]
    idx = {}
    for tu, tg in zip(us, gb):
        for mu, mg in zip(tu["mots"], tg["mots"]):
            idx.setdefault(mu["mot"].lower(), {
                "mot": mu["mot"], "pluriel": None if mu["pluriel"] == "—" else mu["pluriel"],
                "niveau": tu["niveau"], "theme": tu["id"], "fr": mu["traduction"],
                "gb": mg["mot"] if mg["mot"] != mu["mot"] else None,
                "plgb": None if mg["pluriel"] == "—" else mg["pluriel"]})
    return idx


# Les pluriels que la regle de construire.py manque, hors du corpus. None :
# pas de pluriel a montrer.
PLURIELS = {"avocado": "avocados", "calf": "calves", "goldfish": "goldfish", "snowman": "snowmen",
            "back of the neck": None, "back of the knee": None, "underpants": None, "kiwi": "kiwis",
            "shelf": "shelves", "loaf": "loaves", "wolf": "wolves", "tooth": "teeth", "foot": "feet"}


def pluriel(mot):
    if mot in PLURIELS:
        return PLURIELS[mot]
    import construire
    return construire.pluriel(mot)


def anglais_de(point, idx):
    """La zone allemande -> son mot anglais (dict), ou None."""
    brut = MOTS.get(point["mot"])
    if brut is None:
        en = re.sub(r"\(.*?\)", "", point.get("en") or "")
        brut = re.split(r"[,;]", en)[0].strip()
        brut = re.sub(r"^(the|a|an)\s+", "", brut, flags=re.I)
    mot, _, gb = brut.partition("|gb=")
    if not mot:
        return None
    c = idx.get(mot.lower())
    if c:
        return {"mot": c["mot"], "genre": "", "pluriel": c["pluriel"], "niveau": c["niveau"], "theme": c["theme"],
                "fr": point.get("fr") or c["fr"],
                "gb": ({"mot": c["gb"], "pluriel": c["plgb"]} if c["gb"] else
                       ({"mot": gb, "pluriel": None if gb in INDENOMBRABLES else pluriel(gb)} if gb else None))}
    return {"mot": mot, "genre": "", "pluriel": None if mot in INDENOMBRABLES else pluriel(mot),
            "niveau": point.get("niveau") or "A2", "theme": None, "fr": point.get("fr"),
            "gb": {"mot": gb, "pluriel": None if gb in INDENOMBRABLES else pluriel(gb)} if gb else None}


def nettoyer(d):
    return {k: v for k, v in d.items() if v is not None}


def construire_scene(nom, idx):
    de = charger_scene(nom)
    points = []
    for p in de["points"]:
        r = anglais_de(p, idx)
        if not r:
            print("  ⚠ %s : %s sans mot anglais" % (nom, p["mot"]))
            continue
        aussi, vus = [], {r["mot"]}
        for a in p.get("aussi", []):
            ra = anglais_de(a, idx)
            if ra and ra["mot"] not in vus:
                vus.add(ra["mot"])
                aussi.append(nettoyer({k: ra.get(k) for k in ("mot", "genre", "niveau", "theme", "fr", "gb")}))
        q = {k: v for k, v in p.items() if k not in ("tr", "uk", "fa", "pt", "ar", "pl", "ru", "en")}
        q.update(nettoyer(r))
        if not r.get("gb"):
            q.pop("gb", None)
        if not r.get("theme"):
            q.pop("theme", None)
        if not r.get("pluriel"):
            q.pop("pluriel", None)
        q["aussi"] = aussi
        points.append(q)
    scene = dict(de, points=points)
    scene["titre"] = TITRES.get(nom, de.get("titre"))
    scene["exclus"] = sorted({r["mot"] for r in (anglais_de({"mot": m}, idx) for m in de.get("exclus", [])) if r})
    # La couche A1 allemande s'appelle « Noms et articles » : l'anglais n'a
    # pas d'article a apprendre avec le nom.
    a1 = dict(de.get("couches", {}).get("A1", {}), titre="Les noms")
    scene["couches"] = {"A1": a1}
    # Les couches A2-C1 ECRITES pour l'anglais (anglais/scenes/<nom>.json,
    # session A2-C1) ; « _de » y rappelle le fait allemand, on ne le copie pas.
    p_en = os.path.join(RACINE, "anglais", "scenes", nom + ".json")
    if os.path.exists(p_en):
        for niv, couche in json.load(io.open(p_en, encoding="utf-8")).get("couches", {}).items():
            scene["couches"][niv] = dict(couche, qs=[{k: v for k, v in q.items() if not k.startswith("_")}
                                                    for q in couche.get("qs", [])])
    # L'interface de l'anglais est en francais : pas de traductions d'interface.
    scene["traductions"] = {}
    js = ("// GENERE par anglais/outils/scenes.py (depuis scene-%s.js) -- ne pas modifier a la main.\n" % nom
          + "window.SCENE = " + json.dumps(scene, ensure_ascii=False, indent=1) + ";\n")
    io.open(os.path.join(PROTO, "scene-%s.en.js" % nom), "w", encoding="utf-8", newline="\n").write(js)
    return len(points), sum(1 for p in points if p.get("theme"))


def toutes():
    return sorted(n[len("scene-"):-len(".js")] for n in os.listdir(PROTO)
                  if re.match(r"^scene-[a-z-]+\.js$", n) and os.path.exists(
                      os.path.join(PROTO, n[len("scene-"):-len(".js")] + ".points.json")))


def main():
    idx = corpus()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or [n for n in toutes() if n not in EXCLUES]
    total = carte = 0
    for nom in noms:
        if nom in EXCLUES:
            print("  %s : ecartee de l'anglais (27 oct. 2026)" % nom)
            continue
        n, c = construire_scene(nom, idx)
        total += n
        carte += c
        print("  %d zones (%d dans le corpus A1) -> scene-%s.en.js" % (n, c, nom))
    print("%d scenes, %d zones, dont %d avec une carte du corpus." % (len(noms), total, carte))


if __name__ == "__main__":
    main()
