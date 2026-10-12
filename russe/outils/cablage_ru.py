# -*- coding: utf-8 -*-
"""Cable le russe dans le CODE de l'app, comme cablage_ar.py l'a fait pour l'arabe.

    python russe/outils/cablage_ru.py <racine_du_depot> [--ecrire]

Sans --ecrire, rien n'est ecrit : on verifie seulement que chaque
remplacement trouve exactement ce qu'il attend.

HYPOTHESE DE RANGS (brief du 12 oct. 2026) -- A RELIRE AVANT DE LANCER
    Le russe s'integre APRES l'arabe ET le polonais. Dans les tuples de cartes,
    chaque langue occupe un bloc de rangs a la suite de la precedente :
      - cartes a deux champs (nomen, adjektive : traduction, exemple) :
          pl = ar + 2, ru = ar + 4 ;
      - cartes a trois champs (funktionswort, expression : traduction,
        exemple, categorie) :
          pl = ar + 3, ru = ar + 6.
    Le script ne recopie pas ces nombres : il les DEDUIT de RANGS_CARTE.
      - Si « pl » y est deja (cas normal, apres la fusion du polonais), le
        russe prend le bloc suivant celui du polonais.
      - Si « pl » n'y est pas (copie d'essai, ou polonais pas encore fusionne),
        le russe prend quand meme le bloc ar + 4 / ar + 6, et les tuples recoivent
        des cases vides "" a la place du polonais (commentees « reserve au
        polonais ») : les rangs restent justes, et le polonais n'aura qu'a
        remplacer ces cases au lieu de decaler le russe.
    Partout ailleurs (tables de langues, recherche, examen...), « ru » se
    place apres la derniere langue presente, quelle qu'elle soit.

CE QUE CE SCRIPT NE FAIT PAS (poser_tout.py s'en charge, dans l'ordre) :
    le bloc I18N ru (interface.json), grammaire.json, le corpus, l'examen,
    les exercices d'articles (patch_articles.py), exercices.json, les scenes,
    la prononciation.

DRAPEAU : le brief demande de NE PAS mettre de drapeau national. DRAPEAU vaut
« 🌐 » en attendant le choix de Jacques (autre proposition : les lettres
« RU ») ; une seule constante a changer ci-dessous.
"""
import io
import json
import os
import re
import sys

DRAPEAU = "🌐"
NOM_NATIF = "Русский"

# Les libelles des categories (adverbes, expressions), comme cablage_ar.py.
CATS = {
 "Zeit": "Zeit \\u2014 время",
 "Ort/Richtung": "Ort/Richtung \\u2014 место, направление",
 "H\\u00e4ufigkeit": "H\\u00e4ufigkeit \\u2014 частота",
 "Art und Weise": "Art und Weise \\u2014 образ действия",
 "Grad/Menge": "Grad/Menge \\u2014 степень, количество",
 "Grund/Folge": "Grund/Folge \\u2014 причина, следствие",
 "Verbindung/Logik": "Verbindung/Logik \\u2014 логическая связь",
 "Frageadverbien": "Frageadverbien \\u2014 вопросительные слова",
 "Nuance/Ton": "Nuance/Ton \\u2014 отношение говорящего",
 "Begrüßung/Small Talk": "Begrüßung \\u2014 приветствие, светская беседа",
 "Meinung/Zustimmung": "Meinung \\u2014 выразить мнение",
 "Gefühle/Reaktionen": "Gefühle \\u2014 чувства, реакции",
 "Alltag/Organisation": "Alltag \\u2014 повседневная жизнь",
 "Diskussion/Nuance": "Diskussion \\u2014 дискуссия, нюансы",
 "Feste Verbindungen": "Feste Verbindungen \\u2014 глагол + существительное",
}


class Fichier:
    def __init__(self, chemin):
        self.chemin = chemin
        self.src = io.open(chemin, encoding="utf-8", newline="").read()
        self.nl = "\r\n" if "\r\n" in self.src else "\n"

    def r(self, avant, apres, n=1):
        c = self.src.count(avant)
        if c != n:
            sys.exit("%s : ATTENDU %d, TROUVE %d : %r"
                     % (os.path.basename(self.chemin), n, c, avant[:100]))
        self.src = self.src.replace(avant, apres)

    def sub(self, motif, rempl, n=1, flags=0):
        nouveau, c = re.subn(motif, rempl, self.src, flags=flags)
        if c != n:
            sys.exit("%s : ATTENDU %d, TROUVE %d : %s"
                     % (os.path.basename(self.chemin), n, c, motif[:100]))
        self.src = nouveau

    def ecrire(self):
        io.open(self.chemin, "w", encoding="utf-8", newline="").write(self.src)


def deja(f, motif):
    if re.search(motif, f.src):
        sys.exit("le russe est DEJA cable (%s) : rien n'a ete touche" % motif)


def ajoute_cle(f, nom, valeur):
    """const NOM = { ... }; sur une ligne : ajoute ru en dernier."""
    f.sub(r"(const %s = \{[^\n]*?) \};" % re.escape(nom),
          lambda m: m.group(1) + ", ru: " + valeur + " };")


# ---------------------------------------------------------------- index.html

def rangs_carte(f):
    """Ajoute ru a RANGS_CARTE et renvoie {type: {champ: rang ru}}."""
    a = f.src.index("const RANGS_CARTE = {")
    b = f.src.index(f.nl + "};", a)
    lignes = f.src[a:b].split(f.nl)
    ru, courant = {}, None
    for i, l in enumerate(lignes):
        mt = re.match(r"\s+(\w+):\s+\{ traduction", l)
        if mt:
            courant = mt.group(1)
        largeur = 3 if courant in ("funktionswort", "expression") else 2

        def une_table(m):
            d = dict((k, int(v)) for k, v in re.findall(r"(\w\w):\s*(\d+)", m.group(3)))
            if "ru" in d:
                sys.exit("RANGS_CARTE : ru deja la")
            if "ar" not in d:
                sys.exit("RANGS_CARTE : pas d'arabe, l'hypothese de rangs ne tient pas")
            if "pl" in d:
                if d["pl"] != d["ar"] + largeur:
                    sys.exit("RANGS_CARTE : pl=%d, attendu ar+%d=%d"
                             % (d["pl"], largeur, d["ar"] + largeur))
                rang = d["pl"] + largeur
            else:
                rang = d["ar"] + 2 * largeur
            ru.setdefault(courant, {})[m.group(1)] = rang
            return "%s:%s{ %s, ru:%d }" % (m.group(1), m.group(2), m.group(3), rang)

        lignes[i] = re.sub(r"(traduction|exemple|categorie):(\s+)\{ ([^{}]*?) \}", une_table, l)
    f.src = f.src[:a] + f.nl.join(lignes) + f.src[b:]
    attendu = {"nomen": 2, "adjektive": 2, "funktionswort": 3, "expression": 3}
    for t, n in attendu.items():
        if len(ru.get(t, {})) != n:
            sys.exit("RANGS_CARTE : %s incomplet (%s)" % (t, ru.get(t)))
    return ru


def tuple_carte(f, fonction, debut_ru, largeur, var, cat):
    """Ajoute les rangs russes a la fin du tuple produit par <fonction>.

    debut_ru : rang de traduction_ru (RANGS_CARTE). Les cases entre la
    derniere langue et le russe (le polonais, s'il n'est pas encore la)
    sont remplies de "" et commentees."""
    a = f.src.index("async function %s(" % fonction)
    b = f.src.index(f.nl + "async function ", a + 10)
    corps = f.src[a:b]
    lignes = corps.split(f.nl)
    k = max(i for i, l in enumerate(lignes) if re.search(r"// rangs? \d+", l))
    derniere = lignes[k]
    code, commentaire = derniere.split("//", 1)
    if code.rstrip().endswith(","):
        sys.exit("%s : la derniere ligne de rang a deja une virgule" % fonction)
    rangs = [int(x) for x in re.findall(r"\d+", commentaire.split("(")[0])]
    dernier = max(rangs)
    indent = re.match(r"\s*", derniere).group(0)
    col = len(code)
    def ligne(c, com):
        return (indent + c).ljust(col) + "// " + com
    nouvelles = [code.rstrip() + ",".ljust(col - len(code.rstrip())) + "//" + commentaire]
    trou = debut_ru - (dernier + 1)
    if trou not in (0, largeur):
        sys.exit("%s : dernier rang %d, russe attendu a %d -- trou de %d, ni 0 ni %d"
                 % (fonction, dernier, debut_ru, trou, largeur))
    if trou:
        nouvelles.append(ligne(", ".join(['""'] * trou) + ",",
                               "rangs %d a %d : reserves au polonais (pas encore cable)"
                               % (dernier + 1, dernier + trou)))
    t, e = debut_ru, debut_ru + 1
    if largeur == 2:
        nouvelles.append(ligne('%s.traduction_ru || "",' % var, "rang %d (russe)" % t))
        nouvelles.append(ligne('%s.exemple_ru || ""' % var, "rang %d" % e))
    else:
        nouvelles.append(ligne('%s.traduction_ru || "", %s.exemple_ru || "",' % (var, var),
                               "rangs %d et %d (russe)" % (t, e)))
        nouvelles.append(ligne(cat + ' || ""', "rang %d" % (e + 1)))
    lignes[k:k + 1] = nouvelles
    f.src = f.src[:a] + f.nl.join(lignes) + f.src[b:]


def index_html(f):
    nl = f.nl
    deja(f, r'selectUiLangChoice\(\'ru\'\)')

    # 1. Les deux choisisseurs de langue : un bouton apres le dernier.
    motif = re.compile(r'( *)<button class="setup-choice"( id="setupChoiceLang\w+")? '
                       r'onclick="selectUiLangChoice\(\'(\w+)\'\)">' + nl
                       + r'(.*?)</button>' + nl, re.S)
    boutons = list(motif.finditer(f.src))
    groupes, prec = [], None
    for m in boutons:
        if prec is not None and m.start() == prec.end():
            groupes[-1].append(m)
        else:
            groupes.append([m])
        prec = m
    if len(groupes) != 2:
        sys.exit("choisisseurs de langue : %d groupes, 2 attendus" % len(groupes))
    for g in reversed(groupes):
        m = g[-1]
        ind = m.group(1)
        ident = ' id="setupChoiceLangRu"' if m.group(2) else ""
        bouton = (ind + '<button class="setup-choice"%s onclick="selectUiLangChoice(\'ru\')">' % ident + nl
                  + ind + '    <span class="setup-choice-flag">%s</span>' % DRAPEAU + nl
                  + ind + '    <span>%s</span>' % NOM_NATIF + nl
                  + ind + '</button>' + nl)
        f.src = f.src[:m.end()] + bouton + f.src[m.end():]

    # 2. Langues d'interface (l'espagnol garde fr / en).
    f.sub(r'(const UI_LANGS = LANGUE_APPRISE === "es" \? \["fr", "en"\] : \[[^\]]*)\];',
          lambda m: m.group(1) + ', "ru"];')

    # 3. Tables d'une ligne.
    ajoute_cle(f, "SUFFIXE_LANGUE", '"_ru"')
    ajoute_cle(f, "DRAPEAUX_LANGUE", '"%s"' % DRAPEAU)
    ajoute_cle(f, "SUFFIXE_CHAMEAU", '"Ru"')
    ajoute_cle(f, "NOM_LANGUE_NATIF", '"%s"' % NOM_NATIF)
    ajoute_cle(f, "LOCALES_ABO", '"ru-RU"')
    ajoute_cle(f, "NOMS_LANGUE", '"russe"')
    ajoute_cle(f, "VOICE_PREFEREES", "[]")
    ajoute_cle(f, "LANGUE_TAG", '"ru-RU"')

    # 4. Repli ru -> en -> fr (table sur plusieurs lignes).
    a = f.src.index("const REPLI_LANGUE = {")
    b = f.src.index(" };", a)
    f.src = (f.src[:b] + "," + nl
             + "                       // Le russe : meme repli que les autres langues." + nl
             + '                       ru: ["ru", "en", "fr"]' + f.src[b:])

    # 5. Rangs des cartes, puis les tuples qui les remplissent.
    ru = rangs_carte(f)
    tuple_carte(f, "loadAdjektiveJson", ru["adjektive"]["traduction"], 2, "w", None)
    tuple_carte(f, "loadThemesJson", ru["nomen"]["traduction"], 2, "w", None)
    tuple_carte(f, "loadFunktionswoerterJson", ru["funktionswort"]["traduction"], 3, "w", "w.kategorie_ru")
    tuple_carte(f, "loadRedewendungenJson", ru["expression"]["traduction"], 3, "r", "cat.ru")
    tuple_carte(f, "loadAdverbienJson", ru["expression"]["traduction"], 3, "a", "cat.ru")

    # 6. Chargeur des verbes : les champs _ru apres la derniere langue.
    for champ in ("traduction", "exemple", "praeteritum", "perfekt", "konjunktiv2"):
        f.sub(r'(%s_fa: v\.%s_fa \|\| "",(?: %s_\w\w: v\.%s_\w\w \|\| "",)*)'
              % ((champ,) * 4),
              lambda m, c=champ: m.group(1) + ' %s_ru: v.%s_ru || "",' % (c, c))

    # 7. Recherche.
    f.sub(r"(de: w\[0\], fr: w\[3\], en: w\[4\][^\n]*?)(, alt: w\[8\])",
          lambda m: m.group(1) + ", ru: w[%d]" % ru["nomen"]["traduction"] + m.group(2))
    f.sub(r"(de: v\.infinitif, fr: v\.traduction, en: v\.traduction_en[^\n]*?)(\r?\n)",
          lambda m: m.group(1) + ", ru: v.traduction_ru" + m.group(2), 3)
    f.sub(r"(de: a\[0\], fr: a\[1\], en: a\[5\][^\n]*?)(\r?\n)",
          lambda m: m.group(1) + ", ru: a[%d]" % ru["adjektive"]["traduction"] + m.group(2), 2)
    def cfg(m):
        nombres = m.group(2)
        rang = ru["funktionswort" if nombres.startswith(", 9,") else "expression"]["traduction"]
        return m.group(1) + nombres + ", %d]" % rang
    f.sub(r"(\[\w+Theme, 'search_kind_\w+', 'search_src_\w+', '\w+')((?:, \d+)+)\]", cfg, 6)
    m = re.search(r"fa: w\[cfg\[6\]\](?:, \w\w: w\[cfg\[(\d+)\]\])*", f.src)
    k = int(m.group(1)) if m.group(1) else 6
    f.r(m.group(0), m.group(0) + ", ru: w[cfg[%d]]" % (k + 1))

    # 8. Ecoute, phrases a construire, examen.
    f.sub(r"(const rangs = \(w, r\) => \(\{[^\n]*?) \}\);",
          lambda m: m.group(1) + ", ru: w[r.ru] });")
    f.sub(r"(fa: v\.exemple_fa(?:, \w\w: v\.exemple_\w\w)*) \}",
          lambda m: m.group(1) + ", ru: v.exemple_ru }", 2)
    f.sub(r"(explanation_fa: ph\.de(?:, explanation_\w\w: ph\.de)*)",
          lambda m: m.group(1) + ", explanation_ru: ph.de")
    for base in ("correct", "options"):
        f.sub(r"(%sFa: (\w+),(?: %s\w\w: \2,)*)" % (base, base),
              lambda m, b=base: m.group(1) + " %sRu: %s," % (b, m.group(2)), 3)
    f.sub(r"(const LANGUES_PRUEFUNG = \[[^\]]*)\];", lambda m: m.group(1) + ', "ru"];')

    # 9. Libelles des categories (adverbes, expressions allemandes).
    lignes = f.src.split(nl)
    vus = {}
    for i, l in enumerate(lignes):
        m = re.match(r'^    "([^"]+)":\s*\{ fr: ', l)
        if m and m.group(1) in CATS:
            if " ru: " in l:
                sys.exit("deja ru : " + m.group(1))
            coeur = l.rstrip()
            fin = "," if coeur.endswith("},") else ""
            coeur = coeur[:-2] if fin else coeur[:-1]
            lignes[i] = coeur.rstrip() + ', ru: "' + CATS[m.group(1)] + '" }' + fin
            vus[m.group(1)] = vus.get(m.group(1), 0) + 1
    if set(CATS) - set(vus) or any(n != 1 for n in vus.values()):
        sys.exit("categories : manquantes %s, en double %s"
                 % (set(CATS) - set(vus), [k for k, n in vus.items() if n != 1]))
    f.src = nl.join(lignes)
    return ru


# --------------------------------------------------------------- les outils

def outils(racine):
    """Les scripts de tests/ qui tiennent une liste de langues d'exercices."""
    sortie = []
    f = Fichier(os.path.join(racine, "tests", "lot_exos.py"))
    if '"ru"' not in f.src.split("CHAMEAU = {", 1)[1].split("}", 1)[0]:
        f.sub(r'(CHAMEAU = \{[^}]*?)\}', lambda m: m.group(1) + ', "ru": "Ru"}')
    sortie.append(f)
    f = Fichier(os.path.join(racine, "tests", "trous_langue.py"))
    f.sub(r'(LANGUES = \[[^\]]*)\]', lambda m: m.group(1) + ', "ru"]')
    f.sub(r'("en": "optionsEn"\})', '"ru": "optionsRu", \\1')
    f.sub(r'("en": "correctEn"\})', '"ru": "correctRu", \\1')
    sortie.append(f)
    return sortie


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    racine = os.path.abspath(args[0])
    f = Fichier(os.path.join(racine, "index.html"))
    ru = index_html(f)
    autres = outils(racine)
    print("ok : cablage russe pret (rangs %s)" % json.dumps(ru, sort_keys=True))
    if "--ecrire" in sys.argv:
        for x in [f] + autres:
            x.ecrire()
        print("ecrit")


if __name__ == "__main__":
    main()
