# -*- coding: utf-8 -*-
"""Les scenes en portugais (du Portugal) : visuel/prototype/scene-<nom>.pt.js.

    python portugais/outils/scenes.py            (toutes les scenes)
    python portugais/outils/scenes.py kueche     (une seule)

UNE SCENE, PLUSIEURS LANGUES, UNE SEULE GEOMETRIE (comme l'espagnol et
l'anglais) : ce script part de la scene allemande DEJA CONSTRUITE
(scene-<nom>.js, par visuel/prototype/construire.py) et n'ecrit que le .pt.js.
Il ne touche ni a l'allemand, ni a l'espagnol, ni a l'anglais. A relancer apres
tout construire.py <scene>.

Le mot portugais de CHAQUE mot allemand des scenes vient de MOTS ci-dessous
(une table commune : un mot n'a qu'une traduction d'une scene a l'autre), avec
son article. Un mot allemand ajoute a une scene sans sa ligne ici arrete le
script : c'est ce qui fait evoluer les langues ensemble, comme pour l'espagnol.
Pluriel, niveau, theme et sens viennent du corpus portugais (portugais/datos)
quand le mot y est ; sinon la zone garde le sens francais et le niveau de
l'allemand, et n'a pas de theme (pas de carte a reviser).

L'action se situe a LISBONNE (proposition du 29 oct. 2026, a trancher par
Jacques). Aucune scene n'est ecartee pour l'instant : le tram jaune de la
Kreuzung et de la Stadtplatz est meme tres lisboete. Voir ETAT-DES-LIEUX.md pour
celles dont l'image trahit l'Allemagne (Zug, Weihnachtsmarkt, Post).

Comme l'anglais, seule la couche A1 (« Noms et articles » : decouvrir, trouver) :
les couches A2-C1 allemandes enseignent l'allemand.
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

EXCLUES = set()

TITRES = {
    "apotheke": "Na farmácia", "arztpraxis": "No consultório", "baeckerei": "Na padaria",
    "bauernhof": "Na quinta", "bibliothek": "Na biblioteca", "buergeramt": "Na Loja do Cidadão",
    "buero": "No escritório", "camping": "Campismo junto ao lago", "fahrradwerkstatt": "Na oficina de bicicletas",
    "familie": "O almoço de domingo", "flughafen": "No aeroporto de Lisboa", "friseur": "No cabeleireiro",
    "fruehstueck": "O pequeno-almoço na pastelaria", "geburtstag": "Uma festa de anos", "heimwerken": "Arranjos em casa",
    "hotel": "No hotel", "klassenzimmer": "Na sala de aula", "kleidergeschaeft": "Na loja de roupa",
    "kreuzung": "No cruzamento", "kueche": "Na cozinha", "markt-gemuese-frucht": "No mercado",
    "markt-gemuese-wurzel": "No mercado", "markt-obst-heimisch": "No mercado", "markt-obst-sued": "No mercado",
    "museum": "No museu", "musik": "Música em casa", "park": "No jardim", "post": "Nos correios",
    "restaurant": "No restaurante", "schlafzimmer": "No quarto", "sportplatz": "No campo de jogos",
    "stadtplatz": "Na praça", "strand": "Na praia", "supermarkt": "No supermercado", "ubahn": "No metro",
    "umzug": "A mudança de casa", "untersuchung": "A consulta", "untersuchung-dos": "A consulta",
    "waschsalon": "Na lavandaria", "weihnachtsmarkt": "No mercado de Natal", "winter": "Um dia de neve",
    "wohnzimmer": "Na sala", "zug": "No comboio",
}

# Le mot portugais de chaque mot allemand, avec son article (o, a, os, as).
# « |pl=... » : un pluriel que la regle ne trouve pas (hors du corpus).
MOTS = {
    "Ampel": "o semáforo", "Ananas": "o ananás|pl=ananases", "Anzug": "o fato", "Apfel": "a maçã",
    "Apfelsine": "a laranja", "Apotheke": "a farmácia", "Aprikose": "o alperce", "Arm": "o braço",
    "Artischocke": "a alcachofra", "Aubergine": "a beringela", "Aufzug": "o elevador", "Auge": "o olho",
    "Augenbraue": "a sobrancelha", "Auto": "o carro", "Avocado": "o abacate", "Baby": "o bebé",
    "Backofen": "o forno", "Bahnsteig": "o cais", "Ball": "a bola", "Banane": "a banana", "Bank": "o banco",
    "Bart": "a barba", "Bauch": "a barriga", "Bauchnabel": "o umbigo", "Baum": "a árvore", "Bein": "a perna",
    "Berg": "a montanha", "Besen": "a vassoura", "Bett": "a cama", "Bier": "a cerveja", "Bild": "o quadro",
    "Bildschirm": "o ecrã", "Birne": "a pera", "Blaubeere": "o mirtilo", "Bleistift": "o lápis",
    "Blume": "a flor", "Blumenkohl": "a couve-flor|pl=couves-flor", "Bluse": "a blusa", "Boden": "o chão",
    "Bohne": "o feijão-verde|pl=feijões-verdes", "Bohrmaschine": "o berbequim", "Boot": "o barco",
    "Brezel": "o pretzel", "Brief": "a carta", "Briefkasten": "a caixa do correio|pl=caixas do correio",
    "Briefmarke": "o selo", "Brille": "os óculos", "Brokkoli": "os brócolos", "Brombeere": "a amora",
    "Brot": "o pão", "Bruder": "o irmão", "Brunnen": "o chafariz", "Brust": "o peito",
    "Brötchen": "o papo-seco|pl=papos-secos", "Brücke": "a ponte", "Buch": "o livro", "Bus": "o autocarro",
    "Butter": "a manteiga", "Bäckerei": "a padaria", "Bügeleisen": "o ferro de engomar",
    "Bürgersteig": "o passeio", "Bürste": "a escova", "Café": "a pastelaria", "Computer": "o computador",
    "Couchtisch": "a mesa de centro", "Cousin": "o primo", "Dach": "o telhado", "Dampf": "o vapor",
    "Decke": "o cobertor", "Deckel": "a tampa", "Denkmal": "o monumento", "Dorf": "a aldeia", "Dose": "a lata",
    "Drucker": "a impressora", "Ei": "o ovo", "Eimer": "o balde", "Einkaufswagen": "o carrinho",
    "Eis": "o gelado", "Ellbogen": "o cotovelo", "Erbse": "a ervilha", "Erdapfel": "a batata",
    "Erdbeere": "o morango", "Fahrgast": "o passageiro", "Fahrkarte": "o bilhete", "Fahrrad": "a bicicleta",
    "Fahrradständer": "o suporte de bicicletas", "Farbe": "a tinta", "Feige": "o figo", "Feld": "o campo",
    "Fenchel": "o funcho", "Fenster": "a janela", "Fernseher": "a televisão", "Ferse": "o calcanhar",
    "Feuer": "o fogo", "Finger": "o dedo", "Fisch": "o peixe", "Flasche": "a garrafa", "Fleisch": "a carne",
    "Flugzeug": "o avião", "Fluss": "o rio", "Formular": "o formulário", "Foto": "a fotografia",
    "Frau": "a mulher", "Freund": "o amigo", "Fuß": "o pé", "Fußball": "a bola de futebol",
    "Fußgänger": "o peão|pl=peões", "Gabel": "o garfo", "Gast": "o convidado", "Gebäude": "o edifício",
    "Gehsteig": "o passeio", "Geige": "o violino", "Geld": "o dinheiro", "Gemälde": "a pintura",
    "Gemüse": "os legumes", "Gepäck": "a bagagem", "Gepäckablage": "o porta-bagagens|pl=porta-bagagens",
    "Geschenk": "o presente", "Gesicht": "a cara", "Gesäß": "as nádegas", "Gitarre": "a guitarra", "Glas": "o copo",
    "Gitarrenkoffer": "o estojo da guitarra|pl=estojos da guitarra", "Globus": "o globo",
    "Glühbirne": "a lâmpada", "Goldfisch": "o peixinho-dourado", "Granatapfel": "a romã",
    "Grapefruit": "a toranja", "Gras": "a erva", "Großmutter": "a avó", "Großvater": "o avô",
    "Gurke": "o pepino", "Gürtel": "o cinto", "Haar": "o cabelo", "Haken": "o gancho", "Hals": "o pescoço",
    "Haltestelle": "a paragem", "Hammer": "o martelo", "Hand": "a mão", "Handfläche": "a palma da mão",
    "Handgelenk": "o pulso", "Handschuh": "a luva", "Handtuch": "a toalha", "Handy": "o telemóvel",
    "Haus": "a casa", "Heft": "o caderno", "Heidelbeere": "o mirtilo", "Heizkörper": "o radiador",
    "Heizung": "o aquecimento", "Helm": "o capacete", "Hemd": "a camisa", "Himbeere": "a framboesa",
    "Himmel": "o céu", "Hocker": "o banquinho", "Holz": "a madeira", "Hose": "as calças", "Huhn": "a galinha",
    "Hund": "o cão", "Hut": "o chapéu", "Insel": "a ilha", "Isomatte": "a esteira", "Jacke": "o casaco",
    "Jeans": "as calças de ganga", "Johannisbeere": "a groselha", "Junge": "o rapaz", "Kabel": "o cabo",
    "Kaffee": "o café", "Kaffeemaschine": "a máquina de café", "Kalender": "o calendário",
    "Kamera": "a máquina fotográfica|pl=máquinas fotográficas", "Kanne": "o jarro", "Karotte": "a cenoura",
    "Karte": "o cartão", "Kartoffel": "a batata", "Karton": "a caixa de cartão", "Kasse": "a caixa",
    "Katze": "o gato", "Kellner": "o empregado de mesa", "Kellnerin": "a empregada de mesa", "Kerze": "a vela",
    "Kette": "a corrente", "Kind": "a criança", "Kinn": "o queixo", "Kiosk": "o quiosque", "Kirche": "a igreja",
    "Kirsche": "a cereja", "Kissen": "a almofada", "Kiste": "o caixote", "Kiwi": "o kiwi", "Klavier": "o piano",
    "Klebeband": "a fita-cola|pl=fitas-colas", "Kleid": "o vestido", "Klingel": "a campainha",
    "Knie": "o joelho", "Kniekehle": "a curva do joelho", "Knoblauch": "o alho", "Knochen": "o osso",
    "Knopf": "o botão", "Knöchel": "o tornozelo", "Koffer": "a mala de viagem", "Kohl": "a couve",
    "Kohlrabi": "a couve-rábano|pl=couves-rábano", "Kokosnuss": "o coco", "Kopf": "a cabeça",
    "Kopfhörer": "os auscultadores", "Korb": "o cesto", "Krawatte": "a gravata", "Kreide": "o giz",
    "Kreuzung": "o cruzamento", "Kuchen": "o bolo", "Kugelschreiber": "a esferográfica", "Kuh": "a vaca",
    "Kunde": "o cliente", "Käse": "o queijo", "Körper": "o corpo", "Kühlschrank": "o frigorífico",
    "Kürbis": "a abóbora", "Ladegerät": "o carregador", "Lampe": "o candeeiro", "Lampenschirm": "o abajur",
    "Landkarte": "o mapa", "Laptop": "o portátil|pl=portáteis", "Laster": "o camião", "Laterne": "o candeeiro de rua",
    "Lauch": "o alho-francês|pl=alhos-franceses", "Lautsprecher": "a coluna", "Lehrer": "o professor",
    "Leiter": "o escadote", "Leuchtturm": "o farol", "Lichterkette": "o cordão de luzes",
    "Lieferwagen": "a carrinha", "Liege": "a marquesa", "Limette": "a lima", "Lippe": "o lábio",
    "Lkw": "o camião", "Luftballon": "o balão", "Lunge": "o pulmão", "Löffel": "a colher", "Mais": "o milho",
    "Mandarine": "a tangerina", "Mango": "a manga", "Mangold": "a acelga", "Mann": "o homem",
    "Mannschaft": "a equipa", "Mantel": "o sobretudo", "Marille": "o alperce", "Markise": "o toldo",
    "Mauer": "o muro", "Maus": "o rato", "Medikament": "o medicamento", "Meer": "o mar", "Mehl": "a farinha",
    "Melone": "o melão", "Messer": "a faca", "Milch": "o leite", "Mond": "a lua", "Motorrad": "a mota",
    "Mund": "a boca", "Muschel": "a concha", "Mutter": "a mãe", "Mädchen": "a menina",
    "Mülleimer": "o caixote do lixo|pl=caixotes do lixo", "Münze": "a moeda", "Mütze": "o gorro",
    "Nachbar": "o vizinho", "Nachttisch": "a mesa de cabeceira", "Nacken": "a nuca", "Nagel": "a unha",
    "Nase": "o nariz", "Netz": "a rede", "Note": "a nota", "Nuss": "a noz", "Oberschenkel": "a coxa",
    "Obst": "a fruta", "Ofen": "o forno", "Ohr": "a orelha", "Oma": "a avó", "Onkel": "o tio", "Opa": "o avô",
    "Orange": "a laranja", "Ordner": "a pasta", "Paket": "a encomenda", "Papaya": "a papaia",
    "Papier": "o papel", "Paprika": "o pimento", "Parkplatz": "o estacionamento", "Parkuhr": "o parquímetro",
    "Pass": "o passaporte", "Patient": "o paciente", "Pfanne": "a frigideira", "Pfeffer": "a pimenta",
    "Pfeife": "o apito", "Pferd": "o cavalo", "Pfirsich": "o pêssego", "Pflanze": "a planta",
    "Pflaster": "o penso rápido|pl=pensos rápidos", "Pflaume": "a ameixa", "Pilot": "o piloto",
    "Pilz": "o cogumelo", "Pinsel": "o pincel", "Pizza": "a pizza", "Plakat": "o cartaz", "Platz": "a praça",
    "Po": "as nádegas", "Portemonnaie": "a carteira", "Post": "os correios", "Poster": "o póster",
    "Prospekt": "o folheto", "Pullover": "a camisola", "Puppe": "a boneca", "Rad": "a roda",
    "Radfahrer": "o ciclista", "Radieschen": "o rabanete", "Radweg": "a ciclovia", "Rasen": "a relva",
    "Rauch": "o fumo", "Regal": "a estante", "Regenschirm": "o guarda-chuva", "Reis": "o arroz",
    "Rezept": "a receita", "Rezeption": "a receção", "Rhabarber": "o ruibarbo", "Rippe": "a costela",
    "Rock": "a saia", "Rosenkohl": "a couve-de-bruxelas|pl=couves-de-bruxelas", "Rote Bete": "a beterraba",
    "Rucksack": "a mochila", "Rücken": "as costas", "Rüebli": "a cenoura", "Saft": "o sumo", "Salat": "a alface",
    "Salz": "o sal", "Sand": "a areia", "Sandale": "a sandália", "Schachtel": "a caixinha", "Schaf": "a ovelha",
    "Schal": "o cachecol", "Schalter": "o guiché", "Schaufel": "a pá", "Schaufenster": "a montra",
    "Schere": "a tesoura", "Schild": "a placa", "Schinken": "o presunto", "Schirm": "o guarda-chuva",
    "Schlüssel": "a chave", "Schnee": "a neve", "Schneemann": "o boneco de neve", "Schrank": "o armário",
    "Schreibtisch": "a secretária", "Schuh": "o sapato", "Schulter": "o ombro", "Schulterblatt": "a omoplata",
    "Schwammerl": "o cogumelo", "Schwein": "o porco", "Schwester": "a irmã", "Schürze": "o avental",
    "See": "o lago", "Seife": "o sabonete", "Sellerie": "o aipo", "Serviette": "o guardanapo",
    "Sitz": "o assento", "Skulptur": "a escultura", "Socke": "a meia", "Sofa": "o sofá", "Sonne": "o sol",
    "Sonnenschirm": "o guarda-sol|pl=guarda-sóis", "Spargel": "o espargo", "Speisekarte": "a ementa",
    "Spiegel": "o espelho", "Spieler": "o jogador", "Spielzeug": "o brinquedo", "Spinat": "o espinafre",
    "Sportplatz": "o campo de jogos|pl=campos de jogos", "Sporttasche": "o saco de desporto",
    "Spritze": "a seringa", "Spüle": "o lava-loiça", "Spülmaschine": "a máquina da loiça",
    "Stachelbeere": "a groselha-espinhosa|pl=groselhas-espinhosas", "Stand": "a banca",
    "Steckdose": "a tomada", "Stehlampe": "o candeeiro de pé", "Stein": "a pedra", "Stempel": "o carimbo",
    "Stern": "a estrela", "Stethoskop": "o estetoscópio", "Stiefel": "a bota", "Stift": "a caneta",
    "Stirn": "a testa", "Stock": "a bengala", "Strand": "a praia", "Straße": "a rua", "Straßenbahn": "o elétrico",
    "Student": "o estudante", "Studentin": "a estudante", "Stuhl": "a cadeira", "Suppe": "a sopa",
    "Süßkartoffel": "a batata-doce|pl=batatas-doces", "T-Shirt": "a t-shirt", "Tablette": "o comprimido",
    "Tafel": "o quadro de giz|pl=quadros de giz", "Tasche": "a mala", "Taschentuch": "o lenço", "Tasse": "a chávena",
    "Tastatur": "o teclado", "Taxi": "o táxi", "Tee": "o chá", "Teilnehmer": "o participante",
    "Teilnehmerin": "a participante", "Telefon": "o telefone", "Teller": "o prato", "Teppich": "o tapete",
    "Theke": "o balcão", "Ticket": "o bilhete", "Tisch": "a mesa", "Tochter": "a filha", "Tomate": "o tomate",
    "Topf": "o tacho", "Torte": "o bolo de aniversário", "Tram": "o elétrico", "Traube": "a uva",
    "Treppe": "a escada", "Trikot": "a camisola", "Trommel": "o tambor", "Turm": "a torre",
    "Turnschuh": "os ténis", "Tür": "a porta", "Tüte": "o saco", "U-Bahn": "o metro", "Uhr": "o relógio",
    "Umkleidekabine": "o provador", "Umschlag": "o envelope", "Unterhose": "as cuecas", "Vater": "o pai",
    "Verband": "a ligadura", "Verkehrszeichen": "o sinal de trânsito|pl=sinais de trânsito",
    "Verkäuferin": "a empregada", "Versichertenkarte": "o cartão de utente|pl=cartões de utente",
    "Vitamin": "a vitamina", "Vogel": "o pássaro", "Vorhang": "a cortina", "Waage": "a balança",
    "Wade": "a barriga da perna|pl=barrigas da perna", "Wald": "a floresta", "Wand": "a parede",
    "Wange": "a bochecha", "Wartehäuschen": "o abrigo", "Waschmaschine": "a máquina de lavar",
    "Waschmittel": "o detergente", "Wasser": "a água", "Wasserhahn": "a torneira", "Wassermelone": "a melancia",
    "Wecker": "o despertador", "Weg": "o caminho", "Wein": "o vinho", "Welle": "a onda", "Werkzeug": "a ferramenta",
    "Wiese": "o prado", "Wirbelsäule": "a coluna vertebral|pl=colunas vertebrais", "Wolke": "a nuvem",
    "Zahn": "o dente", "Zange": "o alicate", "Zebrastreifen": "a passadeira", "Zehe": "o dedo do pé|pl=dedos do pé",
    "Zeitschrift": "a revista", "Zeitung": "o jornal", "Zelt": "a tenda", "Zettel": "o papelinho",
    "Zitrone": "o limão", "Zollstock": "o metro articulado|pl=metros articulados", "Zucchini": "a curgete",
    "Zucker": "o açúcar", "Zug": "o comboio", "Zwiebel": "a cebola", "Ärztin": "a médica", "Öl": "o azeite",
}


LIEUX = [("Berlin", "Lisbonne"), ("à Hambourg", "à Porto"), ("Hambourg", "Porto"),
         ("cours d'espagnol", "cours de portugais"), ("cours d'allemand", "cours de portugais")]


def charger_scene(nom):
    t = io.open(os.path.join(PROTO, "scene-%s.js" % nom), encoding="utf-8").read()
    return json.loads(t[t.index("{"):t.rindex("}") + 1])


def corpus():
    """mot -> {genre, pluriel, niveau, theme, fr}, du corpus portugais."""
    idx = {}
    for t in json.load(io.open(os.path.join(RACINE, "portugais", "datos", "themes.json"), encoding="utf-8"))["themes"]:
        for m in t["mots"]:
            idx.setdefault(m["mot"], {"genre": m["genre"], "pluriel": None if m["pluriel"] == "—" else m["pluriel"],
                                      "niveau": t["niveau"], "theme": t["id"], "fr": m["traduction"]})
    return idx


def portugais_de(point, idx):
    """La zone allemande -> son mot portugais (dict). Arrete tout si le mot
    allemand n'a pas sa ligne dans MOTS."""
    brut = MOTS.get(point["mot"])
    if brut is None:
        sys.exit("⚠ « %s » (scene) n'a pas de mot portugais dans MOTS : ajoute-le." % point["mot"])
    tete, _, pl = brut.partition("|pl=")
    art, _, mot = tete.partition(" ")
    c = idx.get(mot)
    if c:
        return {"mot": mot, "genre": c["genre"] or art, "pluriel": c["pluriel"], "niveau": c["niveau"],
                "theme": c["theme"], "fr": point.get("fr") or c["fr"]}
    import construire
    pluriel = None if art in ("os", "as") else (pl or construire.pluriel(mot))
    return {"mot": mot, "genre": art, "pluriel": pluriel, "niveau": point.get("niveau") or "A2", "theme": None,
            "fr": point.get("fr")}


def avec_article(r):
    """Le pluriel de la scene porte son article, comme l'espagnol (los relojes) :
    os pratos, as mesas."""
    if r.get("pluriel") and r.get("genre") in ("o", "a"):
        r["pluriel"] = ("os " if r["genre"] == "o" else "as ") + r["pluriel"]
    return r


def nettoyer(d):
    return {k: v for k, v in d.items() if v is not None}


def construire_scene(nom, idx):
    de = charger_scene(nom)
    points = []
    for p in de["points"]:
        r = avec_article(portugais_de(p, idx))
        aussi, vus = [], {r["mot"]}
        for a in p.get("aussi", []):
            ra = portugais_de(a, idx)
            if ra["mot"] not in vus:
                vus.add(ra["mot"])
                aussi.append(nettoyer({k: ra.get(k) for k in ("mot", "genre", "niveau", "theme", "fr")}))
        q = {k: v for k, v in p.items() if k not in ("tr", "uk", "fa", "pt", "ar", "pl", "ru", "en")}
        q.update(nettoyer(r))
        for k in ("theme", "pluriel"):
            if not r.get(k):
                q.pop(k, None)
        q["aussi"] = aussi
        points.append(q)
    # Deux mots allemands DIFFERENTS sur le meme mot portugais : la question
    # « trouve le ... » aurait deux bonnes reponses. (Deux chaises dans une
    # image, deux zones « Stuhl », c'est normal.)
    source = {}
    for p, d in zip(points, de["points"]):
        source.setdefault(p["mot"], set()).add(d["mot"])
    doublons = sorted(m + " (" + "/".join(sorted(v)) + ")" for m, v in source.items() if len(v) > 1)
    if doublons:
        print("  ⚠ %s : un mot portugais pour deux mots allemands : %s" % (nom, ", ".join(doublons)))
    scene = dict(de, points=points)
    scene["titre"] = TITRES.get(nom, de.get("titre"))
    # La consigne et le texte de l'image (en francais) nomment la ville de
    # l'allemand : l'action du portugais se passe a Lisbonne.
    for cle in ("consigne", "alt"):
        if isinstance(scene.get(cle), str):
            t = scene[cle]
            for a, b in LIEUX:
                t = t.replace(a, b)
            scene[cle] = t
    scene["exclus"] = sorted({portugais_de({"mot": m}, idx)["mot"] for m in de.get("exclus", [])})
    scene["couches"] = {"A1": dict(de.get("couches", {}).get("A1", {}), titre="Noms et articles")}
    # Les couches A2-C1 ECRITES pour le portugais (portugais/scenes/<nom>.json,
    # session « Portugais A2-C1 ») ; les cles « _... » (« _de » rappelle le fait
    # allemand) ne sont pas copiees.
    p_pt = os.path.join(RACINE, "portugais", "scenes", nom + ".json")
    if os.path.exists(p_pt):
        for niv, couche in json.load(io.open(p_pt, encoding="utf-8")).get("couches", {}).items():
            scene["couches"][niv] = dict(couche, qs=[{k: v for k, v in q.items() if not k.startswith("_")}
                                                    for q in couche.get("qs", [])])
    # L'interface du portugais est en francais : pas de traductions d'interface.
    scene["traductions"] = {}
    js = ("// GENERE par portugais/outils/scenes.py (depuis scene-%s.js) -- ne pas modifier a la main.\n" % nom
          + "window.SCENE = " + json.dumps(scene, ensure_ascii=False, indent=1) + ";\n")
    io.open(os.path.join(PROTO, "scene-%s.pt.js" % nom), "w", encoding="utf-8", newline="\n").write(js)
    return len(points), sum(1 for p in points if p.get("theme"))


def toutes():
    return sorted(n[len("scene-"):-len(".js")] for n in os.listdir(PROTO)
                  if re.match(r"^scene-[a-z-]+\.js$", n) and os.path.exists(
                      os.path.join(PROTO, n[len("scene-"):-len(".js")] + ".points.json")))


def main():
    idx = corpus()
    noms = [a for a in sys.argv[1:] if not a.startswith("--") and not a.endswith(".py")] or [n for n in toutes() if n not in EXCLUES]
    total = carte = 0
    for nom in noms:
        n, c = construire_scene(nom, idx)
        total += n
        carte += c
        print("  %d zones (%d dans le corpus A1) -> scene-%s.pt.js" % (n, c, nom))
    print("%d scenes, %d zones, dont %d avec une carte du corpus." % (len(noms), total, carte))


if __name__ == "__main__":
    main()
