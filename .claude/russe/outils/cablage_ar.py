# Cable l'arabe dans index.html, comme le portugais l'a ete en v765.
#   python cablage.py <index.html> [--ecrire]
# Chaque remplacement doit trouver EXACTEMENT le nombre attendu d'occurrences.
import io, re, sys

CIBLE = sys.argv[1]
src = io.open(CIBLE, encoding="utf-8", newline="").read()
NL = "\r\n" if "\r\n" in src else "\n"

def r(avant, apres, n=1):
    global src
    c = src.count(avant)
    if c != n:
        sys.exit("ATTENDU %d, TROUVE %d : %r" % (n, c, avant[:100]))
    src = src.replace(avant, apres)

# 1. Suffixe chameau.
r('const SUFFIXE_CHAMEAU = { fr: "", en: "En", tr: "Tr", uk: "Uk", fa: "Fa", pt: "Pt" };',
  'const SUFFIXE_CHAMEAU = { fr: "", en: "En", tr: "Tr", uk: "Uk", fa: "Fa", pt: "Pt", ar: "Ar" };')

# 2. Rangs des cartes : l'arabe en FIN de tuple, apres le portugais.
r('{ fr:3, en:4, tr:12, uk:15, fa:17, pt:19 }, exemple: { fr:6, en:7, tr:13, uk:16, fa:18, pt:20 } }',
  '{ fr:3, en:4, tr:12, uk:15, fa:17, pt:19, ar:21 }, exemple: { fr:6, en:7, tr:13, uk:16, fa:18, pt:20, ar:22 } }')
r('{ fr:1, en:5, tr:7,  uk:11, fa:13, pt:17 }, exemple: { fr:4, en:6, tr:8,  uk:12, fa:14, pt:18 } }',
  '{ fr:1, en:5, tr:7,  uk:11, fa:13, pt:17, ar:19 }, exemple: { fr:4, en:6, tr:8,  uk:12, fa:14, pt:18, ar:20 } }')
r('{ fr:1, en:5, tr:9,  uk:14, fa:17, pt:20 }, exemple: { fr:4, en:6, tr:10, uk:15, fa:18, pt:21 },',
  '{ fr:1, en:5, tr:9,  uk:14, fa:17, pt:20, ar:23 }, exemple: { fr:4, en:6, tr:10, uk:15, fa:18, pt:21, ar:24 },')
r('categorie:  { fr:2, en:7, tr:11, uk:16, fa:19, pt:22 } },',
  'categorie:  { fr:2, en:7, tr:11, uk:16, fa:19, pt:22, ar:25 } },')
r('{ fr:1, en:5, tr:10, uk:15, fa:18, pt:21 }, exemple: { fr:4, en:6, tr:11, uk:16, fa:19, pt:22 },',
  '{ fr:1, en:5, tr:10, uk:15, fa:18, pt:21, ar:24 }, exemple: { fr:4, en:6, tr:11, uk:16, fa:19, pt:22, ar:25 },')
r('categorie:  { fr:2, en:7, tr:12, uk:17, fa:20, pt:23 } }',
  'categorie:  { fr:2, en:7, tr:12, uk:17, fa:20, pt:23, ar:26 } }')

# 3. Chargeur des verbes : les champs _ar apres les _pt.
for champ in ("traduction", "exemple", "praeteritum", "perfekt", "konjunktiv2"):
    r('%s_pt: v.%s_pt || "",' % (champ, champ),
      '%s_pt: v.%s_pt || "", %s_ar: v.%s_ar || "",' % (champ, champ, champ, champ))

# 4. Tuples des cartes.
r('                    w.traduction_pt || "",   // rang 17 (v765, portugais du Bresil)' + NL +
  '                    w.exemple_pt || ""       // rang 18' + NL,
  '                    w.traduction_pt || "",   // rang 17 (v765, portugais du Bresil)' + NL +
  '                    w.exemple_pt || "",      // rang 18' + NL +
  '                    w.traduction_ar || "",   // rang 19 (arabe)' + NL +
  '                    w.exemple_ar || ""       // rang 20' + NL)
r('                w.traduction_pt || "", w.exemple_pt || "",  // rangs 20 et 21 (v765)' + NL +
  '                w.kategorie_pt || ""                        // rang 22' + NL,
  '                w.traduction_pt || "", w.exemple_pt || "",  // rangs 20 et 21 (v765)' + NL +
  '                w.kategorie_pt || "",                       // rang 22' + NL +
  '                w.traduction_ar || "", w.exemple_ar || "",  // rangs 23 et 24 (arabe)' + NL +
  '                w.kategorie_ar || ""                        // rang 25' + NL)
for v in ("r", "a"):
    r('                    %s.traduction_pt || "", %s.exemple_pt || "",  // rangs 21 et 22 (v765)' % (v, v) + NL +
      '                    cat.pt || ""                                // rang 23' + NL,
      '                    %s.traduction_pt || "", %s.exemple_pt || "",  // rangs 21 et 22 (v765)' % (v, v) + NL +
      '                    cat.pt || "",                               // rang 23' + NL +
      '                    %s.traduction_ar || "", %s.exemple_ar || "",  // rangs 24 et 25 (arabe)' % (v, v) + NL +
      '                    cat.ar || ""                                // rang 26' + NL)
r('                    w.traduction_pt || "",   // rang 19 (v765, portugais du Bresil)' + NL +
  '                    w.exemple_pt || ""       // rang 20' + NL,
  '                    w.traduction_pt || "",   // rang 19 (v765, portugais du Bresil)' + NL +
  '                    w.exemple_pt || "",      // rang 20' + NL +
  '                    w.traduction_ar || "",   // rang 21 (arabe)' + NL +
  '                    w.exemple_ar || ""       // rang 22' + NL)

# 5. Recherche.
r('fa: w[17], pt: w[19], alt: w[8]', 'fa: w[17], pt: w[19], ar: w[21], alt: w[8]')
r('fa: v.traduction_fa, pt: v.traduction_pt' + NL,
  'fa: v.traduction_fa, pt: v.traduction_pt, ar: v.traduction_ar' + NL, 3)
r('fa: a[13], pt: a[17]' + NL, 'fa: a[13], pt: a[17], ar: a[19]' + NL, 2)
for a, b in (("9, 14, 17, 20]", "9, 14, 17, 20, 23]"), ("10, 15, 18, 21]", "10, 15, 18, 21, 24]")):
    n = src.count(a)
    if n not in (4, 2):
        sys.exit("cfg recherche : %s x%d" % (a, n))
    src = src.replace(a, b)
r('fa: w[cfg[6]], pt: w[cfg[7]]', 'fa: w[cfg[6]], pt: w[cfg[7]], ar: w[cfg[8]]')

# 6. Voix, phrases a construire, ecoute.
r('const VOICE_PREFEREES = { en: ["moira"], de: [], fr: [], tr: [], uk: [], fa: [], pt: [] };',
  'const VOICE_PREFEREES = { en: ["moira"], de: [], fr: [], tr: [], uk: [], fa: [], pt: [], ar: [] };')
r('fa: w[r.fa], pt: w[r.pt] });', 'fa: w[r.fa], pt: w[r.pt], ar: w[r.ar] });')
r('fa: v.exemple_fa, pt: v.exemple_pt }', 'fa: v.exemple_fa, pt: v.exemple_pt, ar: v.exemple_ar }', 2)
r('explanation_fa: ph.de, explanation_pt: ph.de', 'explanation_fa: ph.de, explanation_pt: ph.de, explanation_ar: ph.de')

# 7. Libelles des categories (adverbes, expressions allemandes).
CATS = {
 "Zeit": "Zeit \\u2014 زمان", "Ort/Richtung": "Ort/Richtung \\u2014 مكان، اتجاه",
 "H\\u00e4ufigkeit": "H\\u00e4ufigkeit \\u2014 تكرار", "Art und Weise": "Art und Weise \\u2014 كيفية",
 "Grad/Menge": "Grad/Menge \\u2014 درجة، كمية", "Grund/Folge": "Grund/Folge \\u2014 سبب، نتيجة",
 "Verbindung/Logik": "Verbindung/Logik \\u2014 ربط منطقي", "Frageadverbien": "Frageadverbien \\u2014 أدوات استفهام",
 "Nuance/Ton": "Nuance/Ton \\u2014 موقف المتكلّم",
 "Begrüßung/Small Talk": "Begrüßung \\u2014 تحية، دردشة", "Meinung/Zustimmung": "Meinung \\u2014 إبداء الرأي",
 "Gefühle/Reaktionen": "Gefühle \\u2014 مشاعر، ردود فعل", "Alltag/Organisation": "Alltag \\u2014 الحياة اليومية",
 "Diskussion/Nuance": "Diskussion \\u2014 نقاش، تدقيق", "Feste Verbindungen": "Feste Verbindungen \\u2014 فعل + اسم",
}
lignes = src.split(NL)
vus = set()
for i, l in enumerate(lignes):
    m = re.match(r'^    "([^"]+)":\s*\{ fr: ', l)
    if m and m.group(1) in CATS:
        if ' ar: ' in l:
            sys.exit("deja ar : " + m.group(1))
        coeur = l.rstrip()
        fin = "," if coeur.endswith("},") else ""
        coeur = coeur[:-2] if fin else coeur[:-1]
        lignes[i] = coeur.rstrip() + ', ar: "' + CATS[m.group(1)] + '" }' + fin
        vus.add(m.group(1))
if set(CATS) - vus:
    sys.exit("categories manquantes : %s" % (set(CATS) - vus))
src = NL.join(lignes)

print("ok : cablage arabe pret")
if "--ecrire" in sys.argv:
    io.open(CIBLE, "w", encoding="utf-8", newline="").write(src)
    print("ecrit")
