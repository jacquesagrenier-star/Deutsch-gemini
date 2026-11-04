# -*- coding: utf-8 -*-
"""Faire les courses, theme illustre (vague 3, 4 nov. 2026). LES IMAGES SONT FACTUREES : 0,15 $ l'image, chez fal --
RIEN NE SE LANCE SANS L'ACCORD DE JACQUES, donne dans la session du theme.

    python visuel/courses/courses.py --json        # courses.json et gloses.json seuls, gratuit
    python visuel/courses/courses.py --montrer     # les prompts seuls, gratuit
    python visuel/courses/courses.py --planche     # la planche d'essai (6 images, 0,90 $)
    python visuel/courses/courses.py               # les images qui manquent (0,15 $ chacune)
    python visuel/courses/courses.py kasse-karte   # celle-la seulement
    python visuel/courses/courses.py --refaire kasse-karte   # l'ancienne passe en <nom>-rate<n>.png

L'ANGLE (regle 2 des themes : pas de scene refaite ; et pas de doublon avec « Manger et gouter ») : manger a deja
les contenants (kilo, botella, vaso, taza, trozo, lata, docena, loncha, litro), la liste de courses en grammes et en
kilos, la commande et l'addition AU CAFE. Ici, L'ACHAT DANS LES MAGASINS :
  - ou acheter quoi (Wo kauft man Brot? / ¿Dónde se compra el pan?) et aller au magasin : zur / zum, in der / im,
    auf dem Markt, am Kiosk ; al / a la, en el / en la ;
  - le dialogue au comptoir, le client et la vendeuse (Was darf es sein? Sonst noch etwas? Brauchen Sie eine Tüte?
    / ¿Qué desea? ¿Algo más? ¿Quiere una bolsa?) ;
  - les prix lus et entendus (les pieges : neunundvierzig / vierundneunzig, siebzehn / siebzig ; sesenta / setenta),
    le verbe qui s'accorde (kostet / kosten, cuesta / cuestan), comparer (teurer, mas caro, mas cara), la monnaie ;
  - le prospectus des offres : les emballages qui manquaient (eine Packung, ein Glas, eine Tube, eine Tuete / un
    paquete, un bote, un tubo, una bolsa) et l'article de la commande (Ich haette gern einen Kuchen / Quisiera una tarta).
Les magasins : les SCENES de l'app quand elles existent (baeckerei, supermarkt, apotheke, markt-*), reprises telles
quelles -- le meme monde, gratuit ; quatre magasins neufs (Metzgerei, Kiosk, Drogerie, Buchhandlung), au meme format
(9:16) et dans le meme style ; leurs cartes sont dans video/LIEUX.md.
Les prix, les etiquettes, le prospectus : dessines dans la page (fal ecrit mal).
Toutes les phrases de la page sont FABRIQUEES depuis courses.json : une image ne dit que ce qu'elle montre.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/courses/img/.
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
SORTIE = os.path.join(PROTO, "courses")

EDIT, T2I, PRIX = "fal-ai/nano-banana-pro/edit", "fal-ai/nano-banana-pro", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "courses", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png"}

# ---------- LES MAGASINS ----------
# de : le mot du corpus, « wo » (Wo? datif) et « zu » (Wohin?), avec les LEURRES de chacun -- jamais une forme qui
# pourrait aussi etre juste (« in die Baeckerei » est juste pour Wohin : on n'offre que zur / zum / zu / in) ; « im
# Markt » ou « im Kiosk » peuvent se dire : jamais proposes. es : « en » (donde) et « a » (adonde). None : le magasin
# n'existe pas dans cette langue (la Drogerie, tres allemande ; en Colombie « droguería » veut dire pharmacie).
# img : l'image du magasin (une scene de l'app, ou courses/<id> quand elle sera faite).
MAGASINS = [
    {"id": "baeckerei", "img": "baeckerei.webp",
     "de": {"mot": "Bäckerei", "genre": "die", "wo": "in der", "woL": ["in die", "zur", "im"], "zu": "zur", "zuL": ["zum", "zu", "in"]},
     "es": {"mot": "panadería", "genre": "la", "en": "en la", "enL": ["a la", "en el", "al"], "a": "a la", "aL": ["al", "en la", "a el"]},
     "tr": {"fr": ["la boulangerie", "à la boulangerie"], "en": ["the bakery", "at the bakery", "to the bakery"], "pt": ["a padaria", "na padaria", "à padaria"]}},
    {"id": "metzgerei", "img": "courses/metzgerei.webp",
     "de": {"mot": "Metzgerei", "genre": "die", "wo": "in der", "woL": ["in die", "zur", "im"], "zu": "zur", "zuL": ["zum", "zu", "in"]},
     "es": {"mot": "carnicería", "genre": "la", "en": "en la", "enL": ["a la", "en el", "al"], "a": "a la", "aL": ["al", "en la", "a el"]},
     "tr": {"fr": ["la boucherie", "à la boucherie"], "en": ["the butcher's", "at the butcher's", "to the butcher's"], "pt": ["o açougue", "no açougue", "ao açougue"]}},
    {"id": "supermarkt", "img": "supermarkt.webp",
     "de": {"mot": "Supermarkt", "genre": "der", "wo": "im", "woL": ["in der", "in den", "zum"], "zu": "zum", "zuL": ["zur", "zu", "in"]},
     "es": {"mot": "supermercado", "genre": "el", "en": "en el", "enL": ["en la", "al", "a la"], "a": "al", "aL": ["a el", "a la", "en el"]},
     "tr": {"fr": ["le supermarché", "au supermarché"], "en": ["the supermarket", "at the supermarket", "to the supermarket"], "pt": ["o supermercado", "no supermercado", "ao supermercado"]}},
    {"id": "markt", "img": "markt-obst-heimisch.webp",
     "de": {"mot": "Markt", "genre": "der", "wo": "auf dem", "woL": ["auf den", "auf der", "zum"], "zu": "zum", "zuL": ["zur", "zu", "in"]},
     "es": {"mot": "mercado", "genre": "el", "en": "en el", "enL": ["en la", "al", "a la"], "a": "al", "aL": ["a el", "a la", "en el"]},
     "tr": {"fr": ["le marché", "au marché"], "en": ["the market", "at the market", "to the market"], "pt": ["a feira", "na feira", "à feira"]}},
    {"id": "apotheke", "img": "apotheke.webp",
     "de": {"mot": "Apotheke", "genre": "die", "wo": "in der", "woL": ["in die", "zur", "im"], "zu": "zur", "zuL": ["zum", "zu", "in"]},
     "es": {"mot": "farmacia", "genre": "la", "en": "en la", "enL": ["a la", "en el", "al"], "a": "a la", "aL": ["al", "en la", "a el"]},
     "tr": {"fr": ["la pharmacie", "à la pharmacie"], "en": ["the pharmacy", "at the pharmacy", "to the pharmacy"], "pt": ["a farmácia", "na farmácia", "à farmácia"]}},
    {"id": "kiosk", "img": "courses/kiosk.webp",
     "de": {"mot": "Kiosk", "genre": "der", "wo": "am", "woL": ["an der", "an den", "zum"], "zu": "zum", "zuL": ["zur", "zu", "in"]},
     "es": {"mot": "quiosco", "genre": "el", "en": "en el", "enL": ["en la", "al", "a la"], "a": "al", "aL": ["a el", "a la", "en el"]},
     "tr": {"fr": ["le kiosque", "au kiosque"], "en": ["the kiosk", "at the kiosk", "to the kiosk"], "pt": ["a banca", "na banca", "à banca"]}},
    {"id": "drogerie", "img": "courses/drogerie.webp",
     "de": {"mot": "Drogerie", "genre": "die", "wo": "in der", "woL": ["in die", "zur", "im"], "zu": "zur", "zuL": ["zum", "zu", "in"]},
     "es": None,
     "tr": {"fr": ["la droguerie", "à la droguerie"], "en": ["the drugstore", "at the drugstore", "to the drugstore"], "pt": ["a drogaria", "na drogaria", "à drogaria"]}},
    {"id": "buchhandlung", "img": "courses/buchhandlung.webp",
     "de": {"mot": "Buchhandlung", "genre": "die", "wo": "in der", "woL": ["in die", "zur", "im"], "zu": "zur", "zuL": ["zum", "zu", "in"]},
     "es": {"mot": "librería", "genre": "la", "en": "en la", "enL": ["a la", "en el", "al"], "a": "a la", "aL": ["al", "en la", "a el"]},
     "tr": {"fr": ["la librairie", "à la librairie"], "en": ["the bookshop", "at the bookshop", "to the bookshop"], "pt": ["a livraria", "na livraria", "à livraria"]}},
]

# ---------- CE QU'ON Y ACHETE ----------
# « vend » : TOUS les magasins ou on l'achete aussi -- aucun ne sert de leurre (le pain se vend aussi au supermarche ;
# le dentifrice a la pharmacie). de : la forme apres « Wo kauft man » et « braucht » ; es : avec article (la question :
# « ¿Dónde se compra el pan? », s'accorde au pluriel) et sans (« necesita pan »).
PRODUITS = [
    {"id": "brot", "vend": ["baeckerei", "supermarkt", "markt"], "de": "Brot", "es": {"art": "el pan", "nu": "pan", "pl": False},
     "tr": {"fr": ["du pain", "de pain"], "en": "bread", "pt": "pão", "de": "Brot"}},
    {"id": "kuchen", "vend": ["baeckerei", "supermarkt"], "de": "Kuchen", "es": {"art": "la tarta", "nu": "una tarta", "pl": False},
     "tr": {"fr": ["du gâteau", "d'un gâteau"], "en": "cake", "pt": "bolo", "de": "Kuchen"}},
    {"id": "fleisch", "vend": ["metzgerei", "supermarkt", "markt"], "de": "Fleisch", "es": {"art": "la carne", "nu": "carne", "pl": False},
     "tr": {"fr": ["de la viande", "de viande"], "en": "meat", "pt": "carne", "de": "Fleisch"}},
    {"id": "wurst", "vend": ["metzgerei", "supermarkt", "markt"], "de": "Wurst", "es": {"art": "el jamón", "nu": "jamón", "pl": False},
     "tr": {"fr": ["de la charcuterie", "de charcuterie"], "en": "cold meat", "pt": "frios", "de": "Wurst"}},
    {"id": "medikamente", "vend": ["apotheke"], "de": "Medikamente", "es": {"art": "los medicamentos", "nu": "medicamentos", "pl": True},
     "tr": {"fr": ["des médicaments", "de médicaments"], "en": "medicine", "pt": "remédios", "de": "Medikamente"}},
    {"id": "tabletten", "vend": ["apotheke"], "de": "Tabletten", "es": {"art": "las pastillas", "nu": "pastillas", "pl": True},
     "tr": {"fr": ["des comprimés", "de comprimés"], "en": "tablets", "pt": "comprimidos", "de": "Tabletten"}},
    {"id": "zeitung", "vend": ["kiosk", "supermarkt", "buchhandlung"], "de": "eine Zeitung", "es": {"art": "el periódico", "nu": "un periódico", "pl": False},
     "tr": {"fr": ["un journal", "d'un journal"], "en": "a newspaper", "pt": "um jornal", "de": "eine Zeitung"}},
    {"id": "buch", "vend": ["buchhandlung", "supermarkt", "kiosk"], "de": "ein Buch", "es": {"art": "el libro", "nu": "un libro", "pl": False},
     "tr": {"fr": ["un livre", "d'un livre"], "en": "a book", "pt": "um livro", "de": "ein Buch"}},
    {"id": "zahnpasta", "vend": ["drogerie", "supermarkt", "apotheke"], "de": "Zahnpasta", "es": {"art": "la pasta de dientes", "nu": "pasta de dientes", "pl": False},
     "tr": {"fr": ["du dentifrice", "de dentifrice"], "en": "toothpaste", "pt": "pasta de dente", "de": "Zahnpasta"}},
    {"id": "seife", "vend": ["drogerie", "supermarkt", "apotheke"], "de": "Seife", "es": {"art": "el jabón", "nu": "jabón", "pl": False},
     "tr": {"fr": ["du savon", "de savon"], "en": "soap", "pt": "sabonete", "de": "Seife"}},
    {"id": "obst", "vend": ["markt", "supermarkt"], "de": "Obst", "es": {"art": "la fruta", "nu": "fruta", "pl": False},
     "tr": {"fr": ["des fruits", "de fruits"], "en": "fruit", "pt": "frutas", "de": "Obst"}},
    {"id": "gemuese", "vend": ["markt", "supermarkt"], "de": "Gemüse", "es": {"art": "la verdura", "nu": "verdura", "pl": False},
     "tr": {"fr": ["des légumes", "de légumes"], "en": "vegetables", "pt": "legumes", "de": "Gemüse"}},
]

# ---------- LE COMPTOIR : les repliques ----------
# r : qui parle (K le client, V la vendeuse ou le vendeur) ; mot : le mot que la replique enseigne (au corpus), sinon
# la question vise le role ; dit : la lecture en lettres d'une replique a chiffres (regle du 28 oct.).
# tr : la traduction de la replique DE CETTE LANGUE (es et de ne disent pas toujours la meme chose).
LIGNES = {
    "V1": {"r": "V", "de": "Guten Tag! Was darf es sein?", "es": "Buenos días. ¿Qué desea?",
           "tr": {"de": {"fr": "Bonjour ! Qu'est-ce que ce sera ?", "en": "Hello! What would you like?", "pt": "Bom dia! O que deseja?"},
                  "es": {"fr": "Bonjour. Vous désirez ?", "en": "Good morning. What would you like?", "pt": "Bom dia. O que deseja?", "de": "Guten Tag. Was darf es sein?"}}},
    "K1": {"r": "K", "de": "Ich hätte gern sechs Brötchen, bitte.", "es": "Quisiera seis panecillos, por favor.", "mot": {"de": ["Brötchen", "das"]},
           "tr": {"de": {"fr": "Je voudrais six petits pains, s'il vous plaît.", "en": "I'd like six bread rolls, please.", "pt": "Eu queria seis pãezinhos, por favor."},
                  "es": {"fr": "Je voudrais six petits pains, s'il vous plaît.", "en": "I'd like six bread rolls, please.", "pt": "Eu queria seis pãezinhos, por favor.", "de": "Ich hätte gern sechs Brötchen, bitte."}}},
    "V2": {"r": "V", "de": "Sonst noch etwas?", "es": "¿Algo más?",
           "tr": {"de": {"fr": "Autre chose ?", "en": "Anything else?", "pt": "Mais alguma coisa?"},
                  "es": {"fr": "Autre chose ?", "en": "Anything else?", "pt": "Mais alguma coisa?", "de": "Sonst noch etwas?"}}},
    "K2": {"r": "K", "de": "Nein, danke. Das ist alles.", "es": "No, gracias. Eso es todo.",
           "tr": {"de": {"fr": "Non, merci. C'est tout.", "en": "No, thank you. That's all.", "pt": "Não, obrigado. É só isso."},
                  "es": {"fr": "Non, merci. C'est tout.", "en": "No, thank you. That's all.", "pt": "Não, obrigado. É só isso.", "de": "Nein, danke. Das ist alles."}}},
    "V3": {"r": "V", "de": "Brauchen Sie eine Tüte?", "es": "¿Quiere una bolsa?", "mot": {"de": ["Tüte", "die"], "es": ["bolsa", "la"]},
           "tr": {"de": {"fr": "Vous avez besoin d'un sac ?", "en": "Do you need a bag?", "pt": "Precisa de uma sacola?"},
                  "es": {"fr": "Vous voulez un sac ?", "en": "Would you like a bag?", "pt": "Quer uma sacola?", "de": "Möchten Sie eine Tüte?"}}},
    "K3": {"r": "K", "de": "Nein, danke. Ich habe eine Tasche.", "es": "No, gracias. Ya tengo una.", "mot": {"de": ["Tasche", "die"]},
           "tr": {"de": {"fr": "Non, merci. J'ai un sac.", "en": "No, thanks. I have a bag.", "pt": "Não, obrigado. Eu tenho uma bolsa."},
                  "es": {"fr": "Non, merci. J'en ai déjà un.", "en": "No, thanks. I already have one.", "pt": "Não, obrigado. Já tenho uma.", "de": "Nein, danke. Ich habe schon eine."}}},
    "V4": {"r": "V", "de": "Zahlen Sie bar oder mit Karte?", "es": "¿Paga en efectivo o con tarjeta?", "mot": {"de": ["zahlen", "verbe"], "es": ["efectivo", "el"]},
           "tr": {"de": {"fr": "Vous payez en espèces ou par carte ?", "en": "Are you paying cash or by card?", "pt": "Vai pagar em dinheiro ou com cartão?"},
                  "es": {"fr": "Vous payez en espèces ou par carte ?", "en": "Are you paying cash or by card?", "pt": "Vai pagar em dinheiro ou com cartão?", "de": "Zahlen Sie bar oder mit Karte?"}}},
    "K4": {"r": "K", "de": "Mit Karte, bitte.", "es": "Con tarjeta, por favor.", "mot": {"de": ["Karte", "die"], "es": ["tarjeta", "la"]},
           "tr": {"de": {"fr": "Par carte, s'il vous plaît.", "en": "By card, please.", "pt": "Com cartão, por favor."},
                  "es": {"fr": "Par carte, s'il vous plaît.", "en": "By card, please.", "pt": "Com cartão, por favor.", "de": "Mit Karte, bitte."}}},
    "V5": {"r": "V", "de": "Das macht 4,20 €.", "es": "Son 4,20 €.", "dit": {"de": "Das macht vier Euro zwanzig.", "es": "Son cuatro euros con veinte."},
           "tr": {"de": {"fr": "Ça fait 4,20 €.", "en": "That's €4.20.", "pt": "São 4,20 €."},
                  "es": {"fr": "Ça fait 4,20 €.", "en": "That's €4.20.", "pt": "São 4,20 €.", "de": "Das macht 4,20 €."}}},
    "K5": {"r": "K", "de": "Hier sind fünf Euro.", "es": "Aquí tiene cinco euros.", "mot": {"de": ["Euro", "der"], "es": ["euro", "el"]},
           "tr": {"de": {"fr": "Voici cinq euros.", "en": "Here's five euros.", "pt": "Aqui estão cinco euros."},
                  "es": {"fr": "Voici cinq euros.", "en": "Here's five euros.", "pt": "Aqui estão cinco euros.", "de": "Hier sind fünf Euro."}}},
    "K6": {"r": "K", "de": "Was kosten die Äpfel?", "es": "¿Cuánto cuestan las manzanas?", "mot": {"de": ["kosten", "verbe"], "es": ["costar", "verbe"]},
           "tr": {"de": {"fr": "Combien coûtent les pommes ?", "en": "How much are the apples?", "pt": "Quanto custam as maçãs?"},
                  "es": {"fr": "Combien coûtent les pommes ?", "en": "How much are the apples?", "pt": "Quanto custam as maçãs?", "de": "Was kosten die Äpfel?"}}},
    "V7": {"r": "V", "de": "Das Kilo kostet 2,90 €.", "es": "El kilo cuesta 2,90 €.", "mot": {"de": ["Kilo", "das"], "es": ["kilo", "el"]},
           "dit": {"de": "Das Kilo kostet zwei Euro neunzig.", "es": "El kilo cuesta dos euros con noventa."},
           "tr": {"de": {"fr": "Le kilo coûte 2,90 €.", "en": "They're €2.90 a kilo.", "pt": "O quilo custa 2,90 €."},
                  "es": {"fr": "Le kilo coûte 2,90 €.", "en": "They're €2.90 a kilo.", "pt": "O quilo custa 2,90 €.", "de": "Das Kilo kostet 2,90 €."}}},
    "K8": {"r": "K", "de": "Kann ich mit Karte bezahlen?", "es": "¿Puedo pagar con tarjeta?", "mot": {"de": ["bezahlen", "verbe"], "es": ["pagar", "verbe"]},
           "tr": {"de": {"fr": "Je peux payer par carte ?", "en": "Can I pay by card?", "pt": "Posso pagar com cartão?"},
                  "es": {"fr": "Je peux payer par carte ?", "en": "Can I pay by card?", "pt": "Posso pagar com cartão?", "de": "Kann ich mit Karte bezahlen?"}}},
    "V8": {"r": "V", "de": "Ja, natürlich.", "es": "Sí, claro.",
           "tr": {"de": {"fr": "Oui, bien sûr.", "en": "Yes, of course.", "pt": "Sim, claro."},
                  "es": {"fr": "Oui, bien sûr.", "en": "Yes, of course.", "pt": "Sim, claro.", "de": "Ja, natürlich."}}},
    "K9": {"r": "K", "de": "Wo finde ich den Reis?", "es": "¿Dónde está el arroz?", "mot": {"de": ["Reis", "der"], "es": ["arroz", "el"]},
           "tr": {"de": {"fr": "Où est-ce que je trouve le riz ?", "en": "Where can I find the rice?", "pt": "Onde encontro o arroz?"},
                  "es": {"fr": "Où est le riz ?", "en": "Where's the rice?", "pt": "Onde fica o arroz?", "de": "Wo ist der Reis?"}}},
    "V9": {"r": "V", "de": "Im Regal dort hinten, neben den Nudeln.", "es": "Allí al fondo, al lado de la pasta.", "mot": {"de": ["Regal", "das"]},
           "tr": {"de": {"fr": "Sur l'étagère du fond, à côté des pâtes.", "en": "On the shelf at the back, next to the pasta.", "pt": "Na prateleira lá no fundo, ao lado do macarrão."},
                  "es": {"fr": "Là-bas, au fond, à côté des pâtes.", "en": "Over there at the back, next to the pasta.", "pt": "Lá no fundo, ao lado do macarrão.", "de": "Dort hinten, neben den Nudeln."}}},
    "V10": {"r": "V", "de": "Hier ist Ihr Kassenbon.", "es": "Aquí tiene su recibo.", "mot": {"de": ["Kassenbon", "der"], "es": ["recibo", "el"]},
            "tr": {"de": {"fr": "Voici votre ticket de caisse.", "en": "Here's your receipt.", "pt": "Aqui está o seu recibo."},
                   "es": {"fr": "Voici votre ticket.", "en": "Here's your receipt.", "pt": "Aqui está o seu recibo.", "de": "Hier ist Ihr Kassenbon."}}},
    "K10": {"r": "K", "de": "Danke schön. Auf Wiedersehen!", "es": "Gracias. ¡Adiós!",
            "tr": {"de": {"fr": "Merci beaucoup. Au revoir !", "en": "Thank you. Goodbye!", "pt": "Muito obrigado. Até logo!"},
                   "es": {"fr": "Merci. Au revoir !", "en": "Thanks. Goodbye!", "pt": "Obrigado. Tchau!", "de": "Danke. Tschüss!"}}},
    "V11": {"r": "V", "de": "Es sind 220 Gramm. Darf es etwas mehr sein?", "es": "Son 220 gramos. ¿Está bien así?", "mot": {"de": ["Gramm", "das"], "es": ["gramo", "el"]},
            "dit": {"de": "Es sind zweihundertzwanzig Gramm. Darf es etwas mehr sein?", "es": "Son doscientos veinte gramos. ¿Está bien así?"},
            "tr": {"de": {"fr": "Ça fait 220 grammes. Un peu plus, ça vous va ?", "en": "It's 220 grams. Is a little more all right?", "pt": "São 220 gramas. Pode ser um pouco mais?"},
                   "es": {"fr": "Ça fait 220 grammes. Ça vous va comme ça ?", "en": "It's 220 grams. Is that all right?", "pt": "São 220 gramas. Está bom assim?", "de": "Es sind 220 Gramm. Ist das so in Ordnung?"}}},
    "K11": {"r": "K", "de": "Ja, das ist in Ordnung.", "es": "Sí, está bien.",
            "tr": {"de": {"fr": "Oui, ça va.", "en": "Yes, that's fine.", "pt": "Sim, tudo bem."},
                   "es": {"fr": "Oui, c'est bien.", "en": "Yes, that's fine.", "pt": "Sim, está bom.", "de": "Ja, das ist gut so."}}},
    "K12": {"r": "K", "de": "Ist der Käse im Angebot?", "es": "¿El queso está en oferta?", "mot": {"de": ["Angebot", "das"], "es": ["oferta", "la"]},
            "tr": {"de": {"fr": "Le fromage est en promotion ?", "en": "Is the cheese on special offer?", "pt": "O queijo está em promoção?"},
                   "es": {"fr": "Le fromage est en promotion ?", "en": "Is the cheese on special offer?", "pt": "O queijo está em promoção?", "de": "Ist der Käse im Angebot?"}}},
    "V12": {"r": "V", "de": "Ja, diese Woche kostet er nur 1,99 €.", "es": "Sí, esta semana cuesta solo 1,99 €.",
            "dit": {"de": "Ja, diese Woche kostet er nur einen Euro neunundneunzig.", "es": "Sí, esta semana cuesta solo un euro con noventa y nueve."},
            "tr": {"de": {"fr": "Oui, cette semaine, il ne coûte que 1,99 €.", "en": "Yes, this week it's only €1.99.", "pt": "Sim, esta semana custa só 1,99 €."},
                   "es": {"fr": "Oui, cette semaine, il ne coûte que 1,99 €.", "en": "Yes, this week it's only €1.99.", "pt": "Sim, esta semana custa só 1,99 €.", "de": "Ja, diese Woche kostet er nur 1,99 €."}}},
    "K13": {"r": "K", "de": "Das ist mir zu teuer.", "es": "Es demasiado caro para mí.", "mot": {"de": ["teuer", "adjectif"], "es": ["caro", "adjectif"]},
            "tr": {"de": {"fr": "C'est trop cher pour moi.", "en": "That's too expensive for me.", "pt": "Está caro demais para mim."},
                   "es": {"fr": "C'est trop cher pour moi.", "en": "It's too expensive for me.", "pt": "É caro demais para mim.", "de": "Das ist mir zu teuer."}}},
    "V13": {"r": "V", "de": "Heute sind die Erdbeeren billig.", "es": "Hoy las fresas están baratas.", "mot": {"de": ["billig", "adjectif"], "es": ["barato", "adjectif"]},
            "tr": {"de": {"fr": "Aujourd'hui, les fraises ne sont pas chères.", "en": "The strawberries are cheap today.", "pt": "Hoje os morangos estão baratos."},
                   "es": {"fr": "Aujourd'hui, les fraises ne sont pas chères.", "en": "The strawberries are cheap today.", "pt": "Hoje os morangos estão baratos.", "de": "Heute sind die Erdbeeren billig."}}},
    "K14": {"r": "K", "de": "Haben Sie Vollkornbrot?", "es": "¿Tiene pan integral?", "mot": {"de": ["Brot", "das"], "es": ["pan", "el"]},
            "tr": {"de": {"fr": "Vous avez du pain complet ?", "en": "Do you have wholemeal bread?", "pt": "Tem pão integral?"},
                   "es": {"fr": "Vous avez du pain complet ?", "en": "Do you have wholemeal bread?", "pt": "Tem pão integral?", "de": "Haben Sie Vollkornbrot?"}}},
    "V14": {"r": "V", "de": "Nein, leider ist keins mehr da.", "es": "No, lo siento, ya no queda.",
            "tr": {"de": {"fr": "Non, désolée, il n'y en a plus.", "en": "No, sorry, there's none left.", "pt": "Não, infelizmente acabou."},
                   "es": {"fr": "Non, désolée, il n'y en a plus.", "en": "No, sorry, there's none left.", "pt": "Não, sinto muito, acabou.", "de": "Nein, leider ist keins mehr da."}}},
    "V15": {"r": "V", "de": "Der Nächste, bitte!", "es": "¡El siguiente, por favor!",
            "tr": {"de": {"fr": "Au suivant, s'il vous plaît !", "en": "Next, please!", "pt": "O próximo, por favor!"},
                   "es": {"fr": "Au suivant, s'il vous plaît !", "en": "Next, please!", "pt": "O próximo, por favor!", "de": "Der Nächste, bitte!"}}},
}
# LES PAIRES question -> reponse, et pour chacune les reponses qui pourraient AUSSI convenir (jamais en leurre) :
# « Sonst noch etwas? — Ich hätte gern sechs Brötchen. » est possible ; « Zahlen Sie bar...? — Hier sind fünf Euro. »
# aussi ; « Kann ich mit Karte bezahlen? — Nein, leider... » aussi.
PAIRES = [
    {"q": "V1", "r": "K1", "aussi": []},
    {"q": "V2", "r": "K2", "aussi": ["K1", "K5"]},
    {"q": "V3", "r": "K3", "aussi": ["K2", "K11", "K4"]},
    {"q": "V4", "r": "K4", "aussi": ["K5", "K11"]},
    {"q": "V5", "r": "K5", "aussi": ["K4", "K11"]},
    {"q": "K6", "r": "V7", "aussi": []},
    {"q": "K8", "r": "V8", "aussi": ["V14"]},
    {"q": "K9", "r": "V9", "aussi": ["V14"]},
    {"q": "V10", "r": "K10", "aussi": ["K11"]},
    {"q": "V11", "r": "K11", "aussi": ["K2", "K4", "K5"]},
    {"q": "K12", "r": "V12", "aussi": ["V8", "V14"]},
]
ROLES = {"de": {"K": {"m": ["Kunde", "der"], "f": ["Kundin", "die"]}, "V": {"m": ["Verkäufer", "der"], "f": ["Verkäuferin", "die"]}},
         "es": {"K": {"m": ["cliente", "el"], "f": ["clienta", "la"]}, "V": {"m": ["dependiente", "el"], "f": ["dependienta", "la"]}}}
TRAD_ROLES = {"fr": {"K": {"m": "le client", "f": "la cliente"}, "V": {"m": "le vendeur", "f": "la vendeuse"}},
              "en": {"K": {"m": "the customer", "f": "the customer"}, "V": {"m": "the shop assistant", "f": "the shop assistant"}},
              "pt": {"K": {"m": "o cliente", "f": "a cliente"}, "V": {"m": "o vendedor", "f": "a vendedora"}},
              "de": {"K": {"m": "der Kunde", "f": "die Kundin"}, "V": {"m": "der Verkäufer", "f": "die Verkäuferin"}}}

# ---------- LES ARTICLES ET LEURS PRIX ----------
# pour les prix, la comparaison et l'accord du verbe : de / es avec l'article, pl, le mot du corpus ; prix : [min, max]
# en centimes ; tr : fr [avec article, genre f?, pl?], en, pt [avec article, f?]
ARTICLES = [
    {"id": "butter", "de": ["die Butter", False, "Butter", "die"], "es": ["la mantequilla", False, "mantequilla", "la"], "prix": [129, 279],
     "tr": {"fr": ["le beurre", False], "en": "the butter", "pt": ["a manteiga", True]}},
    {"id": "kaese", "de": ["der Käse", False, "Käse", "der"], "es": ["el queso", False, "queso", "el"], "prix": [249, 649],
     "tr": {"fr": ["le fromage", False], "en": "the cheese", "pt": ["o queijo", False]}},
    {"id": "brot", "de": ["das Brot", False, "Brot", "das"], "es": ["el pan", False, "pan", "el"], "prix": [189, 429],
     "tr": {"fr": ["le pain", False], "en": "the bread", "pt": ["o pão", False]}},
    {"id": "milch", "de": ["die Milch", False, "Milch", "die"], "es": ["la leche", False, "leche", "la"], "prix": [89, 179],
     "tr": {"fr": ["le lait", False], "en": "the milk", "pt": ["o leite", False]}},
    {"id": "kaffee", "de": ["der Kaffee", False, "Kaffee", "der"], "es": ["el café", False, "café", "el"], "prix": [399, 949],
     "tr": {"fr": ["le café", False], "en": "the coffee", "pt": ["o café", False]}},
    {"id": "aepfel", "de": ["die Äpfel", True, "Apfel", "der"], "es": ["las manzanas", True, "manzana", "la"], "prix": [149, 349],
     "tr": {"fr": ["les pommes", True], "en": "the apples", "pt": ["as maçãs", True]}},
    {"id": "tomaten", "de": ["die Tomaten", True, "Tomate", "die"], "es": ["los tomates", True, "tomate", "el"], "prix": [129, 329],
     "tr": {"fr": ["les tomates", True], "en": "the tomatoes", "pt": ["os tomates", False]}},
    {"id": "eier", "de": ["die Eier", True, "Ei", "das"], "es": ["los huevos", True, "huevo", "el"], "prix": [169, 349],
     "tr": {"fr": ["les œufs", False], "en": "the eggs", "pt": ["os ovos", False]}},
    {"id": "kuchen", "de": ["der Kuchen", False, "Kuchen", "der"], "es": ["la tarta", False, "tarta", "la"], "prix": [299, 1490],
     "tr": {"fr": ["le gâteau", False], "en": "the cake", "pt": ["o bolo", False]}},
    {"id": "zeitung", "de": ["die Zeitung", False, "Zeitung", "die"], "es": ["el periódico", False, "periódico", "el"], "prix": [150, 380],
     "tr": {"fr": ["le journal", False], "en": "the newspaper", "pt": ["o jornal", False]}},
    {"id": "buch", "de": ["das Buch", False, "Buch", "das"], "es": ["el libro", False, "libro", "el"], "prix": [899, 2490],
     "tr": {"fr": ["le livre", False], "en": "the book", "pt": ["o livro", False]}},
    {"id": "schokolade", "de": ["die Schokolade", False, "Schokolade", "die"], "es": ["el chocolate", False, "chocolate", "el"], "prix": [89, 299],
     "tr": {"fr": ["le chocolat", False], "en": "the chocolate", "pt": ["o chocolate", False]}},
    {"id": "reis", "de": ["der Reis", False, "Reis", "der"], "es": ["el arroz", False, "arroz", "el"], "prix": [99, 279],
     "tr": {"fr": ["le riz", False], "en": "the rice", "pt": ["o arroz", False]}},
    {"id": "erdbeeren", "de": ["die Erdbeeren", True, "Erdbeere", "die"], "es": ["las fresas", True, "fresa", "la"], "prix": [199, 499],
     "tr": {"fr": ["les fraises", True], "en": "the strawberries", "pt": ["os morangos", False]}},
]
# le francais au feminin pluriel (« les pommes sont plus chères ») : [genre f, pl] ; ARTICLES.tr.fr = [nom, f]
# ---------- LA COMMANDE : l'article qui va dans le trou ----------
# de : « Ich hätte gern ___ Kuchen. » (l'accusatif : einen / eine / ein) ; es : « Quisiera ___ tarta. » (un / una).
# mot : le nom qui decide de l'article (le contenant, pas le contenu : eine Flasche Wasser).
COMMANDE = {
    "de": [("ein", "Brot", "Brot", "das", "brot"), ("einen", "Kuchen", "Kuchen", "der", "kuchen"), ("eine", "Zeitung", "Zeitung", "die", "zeitung"),
           ("ein", "Buch", "Buch", "das", "buch"), ("einen", "Kaffee", "Kaffee", "der", "kaffee"),
           ("eine", "Tüte", "Tüte", "die", "tuete"), ("eine", "Flasche Wasser", "Flasche", "die", "wasser"), ("eine", "Packung Nudeln", "Packung", "die", "nudeln"),
           ("ein", "Glas Marmelade", "Glas", "das", "marmelade"), ("eine", "Dose Tomaten", "Dose", "die", "tomatendose"), ("eine", "Tube Zahnpasta", "Tube", "die", "zahnpasta"),
           ("ein", "Kilo Äpfel", "Kilo", "das", "kiloaepfel"), ("einen", "Apfel", "Apfel", "der", "apfel")],
    "es": [("una", "tarta", "tarta", "la", "kuchen"), ("un", "periódico", "periódico", "el", "zeitung"), ("un", "libro", "libro", "el", "buch"),
           ("un", "café", "café", "el", "kaffee"), ("una", "bolsa", "bolsa", "la", "tuete"), ("una", "botella de agua", "botella", "la", "wasser"),
           ("un", "paquete de pasta", "paquete", "el", "nudeln"), ("un", "bote de mermelada", "bote", "el", "marmelade"), ("una", "lata de tomate", "lata", "la", "tomatendose"),
           ("un", "tubo de pasta de dientes", "tubo", "el", "zahnpasta"), ("un", "kilo de manzanas", "kilo", "el", "kiloaepfel"),
           ("una", "manzana", "manzana", "la", "apfel"), ("un", "chocolate", "chocolate", "el", "schoko")],
}
TRAD_COMMANDE = {
    "brot": {"fr": "un pain", "en": "a loaf of bread", "pt": "um pão", "de": "ein Brot"},
    "kuchen": {"fr": "un gâteau", "en": "a cake", "pt": "um bolo", "de": "einen Kuchen"},
    "zeitung": {"fr": "un journal", "en": "a newspaper", "pt": "um jornal", "de": "eine Zeitung"},
    "buch": {"fr": "un livre", "en": "a book", "pt": "um livro", "de": "ein Buch"},
    "brezel": {"fr": "un bretzel", "en": "a pretzel", "pt": "um pretzel", "de": "eine Brezel"},
    "kaffee": {"fr": "un café", "en": "a coffee", "pt": "um café", "de": "einen Kaffee"},
    "tuete": {"fr": "un sac", "en": "a bag", "pt": "uma sacola", "de": "eine Tüte"},
    "wasser": {"fr": "une bouteille d'eau", "en": "a bottle of water", "pt": "uma garrafa de água", "de": "eine Flasche Wasser"},
    "nudeln": {"fr": "un paquet de pâtes", "en": "a packet of pasta", "pt": "um pacote de macarrão", "de": "eine Packung Nudeln"},
    "marmelade": {"fr": "un pot de confiture", "en": "a jar of jam", "pt": "um pote de geleia", "de": "ein Glas Marmelade"},
    "tomatendose": {"fr": "une boîte de tomates", "en": "a tin of tomatoes", "pt": "uma lata de tomate", "de": "eine Dose Tomaten"},
    "zahnpasta": {"fr": "un tube de dentifrice", "en": "a tube of toothpaste", "pt": "um tubo de pasta de dente", "de": "eine Tube Zahnpasta"},
    "kiloaepfel": {"fr": "un kilo de pommes", "en": "a kilo of apples", "pt": "um quilo de maçãs", "de": "ein Kilo Äpfel"},
    "stueckkaese": {"fr": "un morceau de fromage", "en": "a piece of cheese", "pt": "um pedaço de queijo", "de": "ein Stück Käse"},
    "apfel": {"fr": "une pomme", "en": "an apple", "pt": "uma maçã", "de": "einen Apfel"},
    "schoko": {"fr": "un chocolat chaud", "en": "a hot chocolate", "pt": "um chocolate quente", "de": "eine heiße Schokolade"},
}
# ---------- LE PROSPECTUS : les offres de la semaine, par emballage ----------
# img : une nature morte (manger/ les a deja pour la bouteille, la boite et le litre ; courses/ pour les autres, a faire)
EMBALLAGES = [
    {"id": "nudeln", "img": "courses/packung-nudeln.webp", "prix": [79, 189],
     "de": {"np": "eine Packung Nudeln", "mot": ["Packung", "die"], "ligne": "Nudeln", "emb": "Packung"},
     "es": {"np": "un paquete de pasta", "mot": ["paquete", "el"], "ligne": "Pasta", "emb": "paquete"}},
    {"id": "marmelade", "img": "courses/glas-marmelade.webp", "prix": [149, 329],
     "de": {"np": "ein Glas Marmelade", "mot": ["Glas", "das"], "ligne": "Marmelade", "emb": "Glas"},
     "es": {"np": "un bote de mermelada", "mot": ["bote", "el"], "ligne": "Mermelada", "emb": "bote"}},
    {"id": "zahnpasta", "img": "courses/tube-zahnpasta.webp", "prix": [99, 289],
     "de": {"np": "eine Tube Zahnpasta", "mot": ["Tube", "die"], "ligne": "Zahnpasta", "emb": "Tube"},
     "es": {"np": "un tubo de pasta de dientes", "mot": ["tubo", "el"], "ligne": "Pasta de dientes", "emb": "tubo"}},
    {"id": "chips", "img": "courses/tuete-chips.webp", "prix": [119, 259],
     "de": {"np": "eine Tüte Chips", "mot": ["Tüte", "die"], "ligne": "Chips", "emb": "Tüte"},
     "es": {"np": "una bolsa de patatas fritas", "mot": ["bolsa", "la"], "ligne": "Patatas fritas", "emb": "bolsa"}},
    {"id": "wasser", "img": "manger/qte-botella-agua.webp", "prix": [39, 99],
     "de": {"np": "eine Flasche Wasser", "mot": ["Flasche", "die"], "ligne": "Mineralwasser", "emb": "Flasche"},
     "es": {"np": "una botella de agua", "mot": ["botella", "la"], "ligne": "Agua mineral", "emb": "botella"}},
    {"id": "tomatendose", "img": "manger/qte-lata-tomate.webp", "prix": [59, 139],
     "de": {"np": "eine Dose Tomaten", "mot": ["Dose", "die"], "ligne": "Tomaten", "emb": "Dose"},
     "es": {"np": "una lata de tomate", "mot": ["lata", "la"], "ligne": "Tomate", "emb": "lata"}},
    {"id": "milch", "img": "manger/qte-litro-leche.webp", "prix": [89, 159],
     "de": {"np": "ein Liter Milch", "mot": ["Liter", "der"], "ligne": "Milch", "emb": "Liter"},
     "es": {"np": "un litro de leche", "mot": ["litro", "el"], "ligne": "Leche", "emb": "litro"}},
]
TRAD_EMB = {"nudeln": {"fr": "un paquet de pâtes", "en": "a packet of pasta", "pt": "um pacote de macarrão", "de": "eine Packung Nudeln"},
            "marmelade": {"fr": "un pot de confiture", "en": "a jar of jam", "pt": "um pote de geleia", "de": "ein Glas Marmelade"},
            "zahnpasta": {"fr": "un tube de dentifrice", "en": "a tube of toothpaste", "pt": "um tubo de pasta de dente", "de": "eine Tube Zahnpasta"},
            "chips": {"fr": "un paquet de chips", "en": "a bag of crisps", "pt": "um pacote de batatas fritas", "de": "eine Tüte Chips"},
            "wasser": {"fr": "une bouteille d'eau", "en": "a bottle of water", "pt": "uma garrafa de água", "de": "eine Flasche Wasser"},
            "tomatendose": {"fr": "une boîte de tomates", "en": "a tin of tomatoes", "pt": "uma lata de tomate", "de": "eine Dose Tomaten"},
            "milch": {"fr": "un litre de lait", "en": "a litre of milk", "pt": "um litro de leite", "de": "ein Liter Milch"}}

# ---------- LES MOMENTS (images a faire) : vrai ou faux, et ou sommes-nous ----------
# lieu : le magasin ; qui : le client (Mark ou Anna) ; v : le sexe de qui vend ; fait : ce que l'image montre, phrase
# vraie (de, es, tr) ; mot : le mot que la phrase enseigne.
MOMENTS = [
    {"id": "baeckerei-bestellen", "lieu": "baeckerei", "qui": "Mark", "v": "f",
     "fait": {"de": "Mark bestellt Brötchen.", "es": "Mark pide panecillos.", "fr": "Mark commande des petits pains.", "en": "Mark is ordering bread rolls.", "pt": "Mark pede pãezinhos."},
     "mot": {"de": ["Brötchen", "das"], "es": ["pan", "el"]},
     "scene": "Mark, the man of the first reference picture, with exactly his face, hair and clothes, stands in front of the glass counter of the bakery of the last reference picture and points at the bread rolls in the wicker basket; behind the counter, the baker of the last reference picture (the smiling woman with the white cap and the white blouse) listens and reaches for the rolls with steel tongs."},
    {"id": "baeckerei-tuete", "lieu": "baeckerei", "qui": "Mark", "v": "f",
     "fait": {"de": "Die Verkäuferin gibt Mark eine Tüte.", "es": "La dependienta le da una bolsa a Mark.", "fr": "La vendeuse donne un sac à Mark.", "en": "The shop assistant is giving Mark a bag.", "pt": "A vendedora dá uma sacola ao Mark."},
     "mot": {"de": ["Tüte", "die"], "es": ["bolsa", "la"]},
     "scene": "In the same bakery, at the same counter, the baker with the white cap hands Mark a brown paper bag full of bread rolls across the counter; Mark takes it with a smile."},
    {"id": "baeckerei-bar", "lieu": "baeckerei", "qui": "Mark", "v": "f",
     "fait": {"de": "Mark bezahlt bar.", "es": "Mark paga en efectivo.", "fr": "Mark paie en espèces.", "en": "Mark is paying cash.", "pt": "Mark paga em dinheiro."},
     "mot": {"de": ["bezahlen", "verbe"], "es": ["efectivo", "el"]},
     "scene": "In the same bakery, at the same counter, Mark gives the baker a five-euro note; the baker, with the white cap, holds out a few coins of change in her open hand. No card, no card terminal in anybody's hand."},
    {"id": "metzgerei-wiegen", "lieu": "metzgerei", "qui": "Anna", "v": "m",
     "fait": {"de": "Der Verkäufer wiegt den Schinken.", "es": "El dependiente pesa el jamón.", "fr": "Le vendeur pèse le jambon.", "en": "The shop assistant is weighing the ham.", "pt": "O vendedor pesa o presunto."},
     "mot": {"de": ["Gramm", "das"], "es": ["gramo", "el"]},
     "scene": "Anna, the woman of the first reference picture, with exactly her face, hair and clothes, stands in front of the glass counter of the butcher's shop of the last reference picture; the butcher of the last reference picture, behind the counter, puts a few slices of ham on paper on the scale and shows them to her; the display of the scale shows no digits."},
    {"id": "markt-fragen", "lieu": "markt", "qui": "Anna", "v": "m",
     "fait": {"de": "Anna fragt nach dem Preis der Äpfel.", "es": "Anna pregunta el precio de las manzanas.", "fr": "Anna demande le prix des pommes.", "en": "Anna is asking the price of the apples.", "pt": "Anna pergunta o preço das maçãs."},
     "mot": {"de": ["kosten", "verbe"], "es": ["costar", "verbe"]},
     "scene": "At the fruit stand of the market of the last reference picture (the same green awning, the same wooden crates), Anna, the woman of the first reference picture, points at the crate of red apples (plain unmarked skins, no stickers) and asks; behind the crates, a friendly fruit seller, a man of about sixty with a short grey beard and a dark green apron, holds an empty paper bag and answers her. No price signs, no writing."},
    {"id": "kasse-karte", "lieu": "supermarkt", "qui": "Mark", "v": "f",
     "fait": {"de": "Mark bezahlt mit Karte.", "es": "Mark paga con tarjeta.", "fr": "Mark paie par carte.", "en": "Mark is paying by card.", "pt": "Mark paga com cartão."},
     "mot": {"de": ["Karte", "die"], "es": ["tarjeta", "la"]},
     "scene": "At the checkout of the supermarket of the last reference picture (the same grey floor, the same light, and behind the checkout the same shelves full of colourful goods as in the reference picture: bottles of orange and red juice, red and green tins, brown paper bags of coffee, bars of chocolate -- every package in plain colours with no writing, never white blank boxes), Mark, the man of the first reference picture, holds a bank card against the small card terminal; the cashier, a woman of about fifty with dark hair in a bun and a dark blue work polo shirt, stands behind the till and smiles; his groceries lie on the belt: a plain white carton of milk with no print, a loaf of bread and three apples with plain unmarked skins, no stickers. No cash anywhere; the screen of the terminal shows no digits."},
    {"id": "kasse-bon", "lieu": "supermarkt", "qui": "Mark", "v": "f",
     "fait": {"de": "Mark bekommt den Kassenbon.", "es": "Mark recibe el recibo.", "fr": "Mark reçoit le ticket de caisse.", "en": "Mark is getting the receipt.", "pt": "Mark recebe o recibo."},
     "mot": {"de": ["Kassenbon", "der"], "es": ["recibo", "el"]},
     "scene": "At the same checkout, the same cashier with the dark blue polo shirt hands Mark a long white paper receipt; Mark takes it, his groceries already in a cloth bag over his shoulder. Behind them, the same shelves of colourful goods as in the reference picture, in plain colours with no writing, never white blank boxes. The receipt shows no readable writing."},
    {"id": "regal-suchen", "lieu": "supermarkt", "qui": "Mark", "v": "m",
     "fait": {"de": "Mark sucht den Reis.", "es": "Mark busca el arroz.", "fr": "Mark cherche le riz.", "en": "Mark is looking for the rice.", "pt": "Mark procura o arroz."},
     "mot": {"de": ["Reis", "der"], "es": ["arroz", "el"]},
     "scene": "In an aisle of the same supermarket, Mark, with a red shopping basket on his arm, asks a young shop employee in a dark blue work polo shirt; the employee points to the shelf at the back of the aisle. Shelves with packets of rice and pasta in plain bright colours (yellow, red, blue, brown paper), never white blank boxes, no labels, no writing."},
]
PLANCHE = ["metzgerei", "tube-zahnpasta", "glas-marmelade", "baeckerei-bestellen", "kasse-karte", "markt-fragen"]

# les natures mortes et les magasins a faire
NATURES = {
    "packung-nudeln": "A packet of dry spaghetti in a plain transparent plastic wrapping with a plain yellow band, lying on the table.",
    "glas-marmelade": "A glass jar of red strawberry jam with a plain white metal screw lid and no label, a spoon beside it.",
    "tube-zahnpasta": "A tube of toothpaste, plain white with a single light blue stripe, lying flat next to a blue toothbrush.",
    "tuete-chips": "A closed bag of potato crisps, a plain shiny orange bag with a picture of a few crisps, and a few crisps beside it.",
}
LIEUX = {
    "metzgerei": "A small traditional German butcher's shop in a Berlin neighbourhood: a long glass counter running from the front of the shop to the back along the right-hand wall, with sausages, ham, cuts of meat and a few salads on white trays; behind it, the butcher, a cheerful man of about forty-five with short brown hair, in a white coat and a white apron; a scale on top of the counter; white tiled walls, a few hanging cured sausages, a window with daylight on the left, a worn tiled floor.",
    "kiosk": "A small Berlin corner kiosk (Spaetkauf) seen from inside the shop: shelves of newspapers and magazines on the left, their covers colourful photographs and plain colours with no readable writing, never white blank covers, a fridge of drinks at the back, sweets and a counter with a till on the right; behind the counter, the kiosk owner, a man of about fifty with a grey moustache and a dark green cardigan; daylight from the glass door.",
    "drogerie": "A bright German drugstore (Drogerie): long white shelves with toothpaste, soap, shampoo bottles, creams and nappies in plain colours, a checkout counter with a saleswoman of about thirty with a dark ponytail and a white polo shirt at the front right, a grey floor.",
    "buchhandlung": "A small, warm neighbourhood bookshop in Berlin: wooden bookshelves full of books on the walls, a table of books in the middle, a counter with a till on the right; behind it, the bookseller, a woman of about sixty with short grey hair and round glasses, in a dark red cardigan; a big window with daylight on the left, a wooden floor.",
}


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def es_se_compra(p):
    return "¿Dónde se compra" + ("n " if p["es"]["pl"] else " ") + p["es"]["art"] + "?"


def decouverte(langue):
    """La phrase de chaque magasin : « In der Bäckerei kauft man Brot. », « En la panadería se compra pan. »."""
    L = "de" if langue == "de" else "es"
    out = {}
    for m in MAGASINS:
        if not m[L]:
            continue
        prods = [p for p in PRODUITS if p["vend"][0] == m["id"]] or [p for p in PRODUITS if m["id"] in p["vend"]]
        if m["id"] == "supermarkt":
            t = "Im Supermarkt kauft man fast alles." if L == "de" else "En el supermercado se compra casi de todo."
        elif L == "de":
            t = m["de"]["wo"].capitalize() + " " + m["de"]["mot"] + " kauft man " + " und ".join(p["de"] for p in prods[:2]) + "."
        else:
            p = prods[0]["es"]
            t = m["es"]["en"].capitalize() + " " + m["es"]["mot"] + " se compra" + ("n " if p["pl"] else " ") + p["nu"] + "."
        out["mag-" + m["id"]] = {"texte": t, "son": identifiant(t)}
    for k, l in LIGNES.items():
        t = l[L]
        out["ligne-" + k] = {"texte": t, "son": identifiant(t)}
    return out


def ecrire_json():
    def pret(chemin):
        return os.path.exists(os.path.join(PROTO, chemin))
    d = {"magasins": [dict(m, pret=pret(m["img"])) for m in MAGASINS], "produits": PRODUITS, "lignes": LIGNES, "paires": PAIRES,
         "roles": ROLES, "tradRoles": TRAD_ROLES, "articles": ARTICLES, "commande": COMMANDE, "tradCommande": TRAD_COMMANDE,
         "emballages": [dict(e, pret=pret(e["img"])) for e in EMBALLAGES], "tradEmb": TRAD_EMB,
         "moments": [dict({k: v for k, v in m.items() if k != "scene"}, img="courses/" + m["id"] + ".webp", pret=pret("courses/" + m["id"] + ".webp")) for m in MOMENTS],
         "latam": {"patatas": "papas"},
         "decouverte": {"de": decouverte("de"), "es": decouverte("es")}}
    os.makedirs(SORTIE, exist_ok=True)
    io.open(os.path.join(SORTIE, "courses.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def mots_du_theme():
    """Les mots que la page enseigne, a la forme du corpus : (mot, genre ou cat). La page les recalcule (motsDuTheme)."""
    out = {"es": [], "de": []}
    for L in ("es", "de"):
        for m in MAGASINS:
            if m[L]:
                out[L].append((m[L]["mot"], m[L]["genre"]))
        for r in ROLES[L].values():
            for g in r.values():
                out[L].append(tuple(g))
        for l in LIGNES.values():
            if l.get("mot", {}).get(L):
                out[L].append(tuple(l["mot"][L]))
        for a in ARTICLES:
            out[L].append((a[L][2], a[L][3]))
        for c in COMMANDE[L]:
            out[L].append((c[2], c[3]))
        for e in EMBALLAGES:
            out[L].append(tuple(e[L]["mot"]))
        for m in MOMENTS:
            out[L].append(tuple(m["mot"][L]))
        out[L] += [("teuer", "adjectif"), ("billig", "adjectif"), ("kosten", "verbe"), ("bezahlen", "verbe"), ("Euro", "der")] if L == "de" else \
                  [("caro", "adjectif"), ("barato", "adjectif"), ("costar", "verbe"), ("pagar", "verbe"), ("euro", "el")]
        out[L] = list(dict.fromkeys(out[L]))
    return out


def ecrire_gloses():
    """La traduction des mots du theme tiree du CORPUS (relu), pour les langues ou la page ne traduit pas la phrase
    entiere (ar, tr, uk, fa, pl, ru). Les mots absents du corpus sont listes. DERIVE : le refaire."""
    def lire(p):
        return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))
    LDE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
           "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}
    plats = lambda p: [e for v in lire(p).values() if isinstance(v, list) for e in v if isinstance(e, dict)]
    noms = lambda p: [m for t in lire(p)["themes"] for m in t["mots"]]
    sources = {"de": (plats("adjectif.json"), plats("verbe.json"), noms("themes.json"), LDE),
               "es": (plats("espanol/datos/adjetivos.json"), plats("espanol/datos/verbos.json"), noms("espanol/datos/temas.json"), LES)}
    out, manque = {"de": {}, "es": {}}, {"de": [], "es": []}
    voulus = mots_du_theme()
    for L, (adjs, verbes, ns, champs) in sources.items():
        for mot, g in voulus[L]:
            if g == "adjectif":
                cand, cle = [e for e in adjs if e.get("mot") == mot], mot
            elif g == "verbe":
                cand, cle = [e for e in verbes if (e.get("infinitif") or e.get("mot")) == mot], mot
            else:
                cand, cle = [m for m in ns if m.get("mot") == mot and m.get("genre") == g], g + " " + mot
            if not cand:
                manque[L].append(cle)
                continue
            out[L][cle] = {l: cand[0][c] for l, c in champs.items() if cand[0].get(c)}
    io.open(os.path.join(SORTIE, "gloses.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return manque


def images():
    """{nom: (personnes, prompt, format, decor)} -- decor : l'image (scene de l'app ou image deja faite) qui donne le lieu."""
    NATURE = ("A photorealistic still-life photograph on a light wooden table, plain light grey studio background, soft even "
              "light, seen slightly from above, the object centred and entirely visible, nothing else on the table. "
              "Absolutely no text, no letters, no numbers, no brand, no logos anywhere. ")
    LIEU = ("A photorealistic photograph, in exactly the same photographic style as the reference picture of the bakery (the same "
            "camera height, the same natural light, the same colours, a vertical picture), of the inside of another small shop of "
            "the same Berlin neighbourhood. Natural colours. Absolutely no text, no letters, no prices, no signs, no logos anywhere. ")
    MOMENT = ("A photorealistic photograph, the same photographic style as the reference pictures. The place is the shop of the "
              "last reference picture: the same counter, shelves, walls, floor and light, seen from a closer, horizontal point of "
              "view. The people of the reference pictures keep exactly their faces, hair and clothes; everybody's face and "
              "gesture are easy to read. Absolutely no text, no letters, no prices, no logos anywhere. ")
    out = {}
    for n, quoi in LIEUX.items():
        out[n] = ([], LIEU + quoi, "9:16", "baeckerei")
    for n, quoi in NATURES.items():
        out[n] = ([], NATURE + quoi, "4:3", None)
    for m in MOMENTS:
        decor = {"baeckerei": "baeckerei", "supermarkt": "supermarkt", "markt": "markt-obst-heimisch", "metzgerei": "metzgerei"}[m["lieu"]]
        out[m["id"]] = ([m["qui"]], MOMENT + m["scene"], "4:3", decor)
    return out


def chemin_decor(decor):
    """Une scene de l'app (visuel/prototype/<decor>.webp, convertie en png) ou une image deja faite du theme."""
    png = os.path.join(DOSSIER, decor + ".png")
    if os.path.exists(png):
        return png
    webp = os.path.join(PROTO, decor + ".webp")
    if os.path.exists(webp):
        from PIL import Image
        os.makedirs(DOSSIER, exist_ok=True)
        Image.open(webp).convert("RGB").save(os.path.join(DOSSIER, "decor-" + decor + ".png"))
        return os.path.join(DOSSIER, "decor-" + decor + ".png")
    return None


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    tout = images()
    noms_ = [a for a in sys.argv[1:] if not a.startswith("--")] or (PLANCHE if "--planche" in sys.argv else list(tout))
    inconnus = [n for n in noms_ if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    ecrire_json()
    manque = ecrire_gloses()
    for L in manque:
        if manque[L]:
            print("  absents du corpus (%s) : %s" % (L, ", ".join(manque[L])))
    if "--json" in sys.argv:
        return
    if refaire and not montrer:
        for n in noms_:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms_ if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if montrer:
        for n in a_faire:
            print("\n  %s %s decor=%s\n  %s" % (n, tout[n][0], tout[n][3], tout[n][1]))
        return
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    os.makedirs(DOSSIER, exist_ok=True)
    depots = {}

    def deposer(chemin):
        if chemin not in depots:
            depots[chemin] = O.deposer(chemin, "image/png", cle)[0]
        return depots[chemin]
    for nom_ in a_faire:
        gens, prompt, fmt, decor = tout[nom_]
        refs = [deposer(SOURCES[g]) for g in gens]
        if decor:
            png = chemin_decor(decor)
            if not png:
                print("  ATTENTE", nom_, ": le decor", decor, "n'est pas encore fait")
                continue
            refs.append(deposer(png))
        print("\n  %s\n  %s" % (nom_, prompt))
        modele = EDIT if refs else T2I
        corps = {"prompt": prompt, "aspect_ratio": fmt, "resolution": "2K", "output_format": "png", "num_images": 1}
        if refs:
            corps["image_urls"] = refs
        soum = O._json("https://queue.fal.run/" + modele, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom_, err)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom_, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom_ + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom_, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom_ + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "sources": [SOURCES[g] for g in gens] + ([decor] if decor else []), "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
