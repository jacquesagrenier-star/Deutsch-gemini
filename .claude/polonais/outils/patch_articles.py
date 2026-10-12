# Ajoute une langue aux exercices d'articles codes en dur dans index.html.
#   python patch_articles.py <index.html> <langue> <precedente> <t.json> <dump.jsonl> [--ecrire]
# <precedente> : la derniere langue deja posee (pt, puis uk...). La nouvelle
# se place juste apres elle : un 6e element dans les explications, une
# colonne de plus en fin de ligne des tableaux. Le genre et la famille de
# l'indice viennent de GENRES[langue].
import io, json, re, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
CIBLE, L, PREC, TFILE, DUMPFILE = args
U, P = L.upper(), PREC.upper()
T = json.load(io.open(TFILE, encoding="utf-8"))
DUMP = [json.loads(l) for l in io.open(DUMPFILE, encoding="utf-8") if l.strip()]
GENRES = {
 "uk": ('{ m:"чоловічий", f:"жіночий", n:"середній", pl:"множина" }',
        '{ def:"означений", indef:"неозначений", neg:"заперечний" }'),
 "ar": ('{ m:"مذكر", f:"مؤنث", n:"محايد", pl:"جمع" }',
        '{ def:"معرفة", indef:"نكرة", neg:"نفي" }'),
 "pl": ('{ m:"rodzaj męski", f:"rodzaj żeński", n:"rodzaj nijaki", pl:"liczba mnoga" }',
        '{ def:"określony", indef:"nieokreślony", neg:"przeczący" }'),
}
src = io.open(CIBLE, encoding="utf-8", newline="").read()
NL = "\r\n" if "\r\n" in src else "\n"
utilises = set()

def js(s):
    return json.dumps(s, ensure_ascii=False)

def une(avant, apres, n=1):
    global src
    c = src.count(avant)
    if c != n:
        sys.exit("ATTENDU %d, TROUVE %d : %r" % (n, c, avant[:90]))
    src = src.replace(avant, apres)

def bloc(texte, debut):
    a = texte.index(debut)
    return a, texte.index("};" if debut.endswith("{") else "];", a)

# 1. Genre et famille.
m = re.search(r"const ARTICLE_FAMILLE_%s = [^\n]*\n" % P, src)
une(m.group(0), m.group(0) + "const ARTICLE_GENRE_%s = %s;%s" % (U, GENRES[L][0], NL)
    + "const ARTICLE_FAMILLE_%s = %s;%s" % (U, GENRES[L][1], NL))

# 2. Explications et declencheurs : un element de plus en fin de tableau.
def element(debut_bloc, prefixe, motif):
    global src
    a, b = bloc(src, debut_bloc)
    corps, morceaux, pos, n = src[a:b], [], 0, None
    for m in re.finditer(motif, corps):
        cle = prefixe + m.group(1)
        if cle not in T:
            sys.exit("MANQUE " + cle)
        fin = corps.index('"]', m.end())
        nb = corps[m.end():fin + 1].count('",') + 1
        n = nb if n is None else n
        if nb != n:
            sys.exit("LONGUEUR %s : %d / %d" % (cle, nb, n))
        morceaux += [corps[pos:fin + 1], "," + NL + "                   " + js(T[cle])]
        pos = fin + 1
        utilises.add(cle)
    morceaux.append(corps[pos:])
    src = src[:a] + "".join(morceaux) + src[b:]
    return n            # index du nouvel element

i_expl = element("const ARTICLE_EXPLICATIONS = {", "E|", r'"((?:def|indef|neg)\.(?:nom|akk|dat|gen)\.(?:m|f|n|pl))":')
i_decl = element("const ARTICLE_DECLENCHEURS = {", "D|", r'\n    (sujet|objet|verbe|preposition|possession):')

# 3. Lignes des tableaux.
ALLEMAND = {d[0]: d[3] for d in DUMP if len(d) > 3}
def lignes(nom, prefixe):
    global src
    a, b = bloc(src, "const " + nom + " = [")
    corps = src[a:b].split(NL)
    i = 0
    for k, ligne in enumerate(corps):
        if not ligne.startswith('    ["'):
            continue
        cle = prefixe + str(i)
        if json.loads(ligne.strip().rstrip(","))[0] != ALLEMAND[cle]:
            sys.exit("DECALAGE " + cle)
        fin = ligne.rstrip().endswith(",")
        coeur = ligne.rstrip().rstrip(",")
        corps[k] = coeur[:-1] + ", " + js(T[cle]) + "]" + ("," if fin else "")
        utilises.add(cle)
        i += 1
    src = src[:a] + NL.join(corps) + src[b:]

for nom in sorted({d[0].split("|")[1] for d in DUMP if d[0].startswith("R|")}):
    lignes(nom, "R|" + nom + "|")
lignes("ARTICLES_MIX", "M|")

# 4. Le code qui lit ces tableaux.
# La liste des colonnes finit par <precedente> ; d'autres langues peuvent
# s'etre glissees entre fa et elle (pt, uk, ar...).
for deb in ("lignes.map(([phrase, genre, ", "lignes.map(([phrase, cas, famille, genre, decl, "):
    m = re.search(re.escape(deb) + r"[^\]]*\b%s\]" % PREC, src)
    if not m:
        sys.exit("COLONNES : " + deb)
    une(m.group(0), m.group(0)[:-1] + ", %s]" % L)
une('translation_%s: %s || "",' % (PREC, PREC), 'translation_%s: %s || "", translation_%s: %s || "",' % (PREC, PREC, L, L), 2)
h = '            hint_%s: "(" + ARTICLE_GENRE_%s[genre] + " \\u00b7 " + ARTICLE_FAMILLE_%s[famille] + " \\u00b7 " + casNom + ")",' % (PREC, P, P)
une(h + NL, h + NL + h.replace("hint_" + PREC, "hint_" + L).replace("_" + P + "[", "_" + U + "[") + NL)
m = re.search(r'hint_%s: d\[(\d)\] \|\| "",' % PREC, src)
une(m.group(0), m.group(0) + ' hint_%s: d[%d] || "",' % (L, i_decl))
m = re.search(r'explanation_%s: expl\[(\d)\] \|\| "",' % PREC, src)
une(m.group(0), m.group(0) + ' explanation_%s: expl[%d] || "",' % (L, i_expl))
m = re.search(r'            explanation_%s: expl\[(\d)\] \? ARTICLE_CAS_NOM\[cas\] \+ " \\u2014 " \+ expl\[\d\] : "",' % PREC, src)
une(m.group(0) + NL, m.group(0) + NL + '            explanation_%s: expl[%d] ? ARTICLE_CAS_NOM[cas] + " \\u2014 " + expl[%d] : "",' % (L, i_expl, i_expl) + NL)

reste = set(T) - utilises
if reste:
    sys.exit("NON POSE : " + ", ".join(sorted(reste)[:5]))
print("ok : %d textes %s (explications index %d, declencheurs index %d)" % (len(utilises), L, i_expl, i_decl))
if "--ecrire" in sys.argv:
    io.open(CIBLE, "w", encoding="utf-8", newline="").write(src)
    print("ecrit")
