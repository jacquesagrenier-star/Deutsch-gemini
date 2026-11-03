# -*- coding: utf-8 -*-
"""Le branchement du theme « Les loisirs » dans index.html (3 nov. 2026), IDEMPOTENT : relance sans effet.

    python visuel/loisirs/brancher.py

1. la tuile, apres la derniere tuile de theme ; 2. la derniere ligne de THEMES_ILLUSTRES ; 3. loi_tuile dans les onze blocs
I18N (a cote de gato_tuile) ; 4. ouvrirThemeLoisirs() ; 5. une ligne dans le panneau Adverbes (de et es : la
frequence) et dans celui des verbes espagnols, a cote de « Les verbes comme gustar ».
A relancer apres un rebase qui aurait perdu une piece (et compter les </div> des tuiles : la fusion du chat en a perdu un).
"""
import io, os, sys
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(RACINE, "index.html")
s = io.open(CH, encoding="utf-8", newline="").read()
nl = "\r\n" if "\r\n" in s else "\n"
avant = s

def apres(ancre, ajout, deja):
    global s
    if deja in s:
        return
    if s.count(ancre) != 1:
        sys.exit("ancre introuvable ou multiple : %r" % ancre[:80])
    s = s.replace(ancre, ancre + ajout)

# 1. la tuile : APRES LA DERNIERE tuile de theme illustre (l'ordre de Tout le contenu suit celui des publications ;
#    la fin d'une tuile est la premiere ligne « </div> » a 8 espaces qui suit son ouverture)
TUILE = nl.join([
    "",
    "        <!-- Les loisirs (3 nov. 2026, vague 2) : quinze activites photographiees avec des personnes connues ; me gusta /",
    "             gern, jugar ou tocar / spielen, machen, fahren, la frequence (un calendrier de quatre semaines) et proposer",
    "             une sortie. visuel/prototype/loisirs.html. es et de. -->",
    '        <div class="orb hidden" data-orbid="loisirs" id="tuileLoisirs" onclick="ouvrirThemeIllustre(' + "'loisirs'" + ')" role="button" tabindex="0">',
    '            <div class="orb-icon"><svg viewBox="0 0 24 24"><circle cx="8" cy="15" r="5"/><path d="M8 10v10M3 15h10"/><path d="M15 4v10.5"/><circle cx="13" cy="15" r="2"/><path d="M15 4l5 1.5v3L15 7"/></svg></div>',
    '            <div><strong data-i18n="loi_tuile">Les loisirs</strong></div>',
    "        </div>"])
if 'id="tuileLoisirs"' not in s:
    debut = s.rindex('onclick="ouvrirThemeIllustre(' + "'")
    fin = s.index(nl + "        </div>", debut) + len(nl + "        </div>")
    s = s[:fin] + TUILE + s[fin:]

# 2. THEMES_ILLUSTRES : la derniere ligne de la table
if 'loisirs: {page: "loisirs.html"' not in s:
    t = s.index("const THEMES_ILLUSTRES = {")
    f = s.index("}};", t)
    s = s[:f] + "}," + nl + '                          loisirs: {page: "loisirs.html", titre: "loi_tuile", tuile: "tuileLoisirs"}};' + s[f + 3:]

# 3. les onze blocs I18N
TITRES = [("Où est le chat ?", "Les loisirs"), ("Where's the cat?", "Free time"), ("Kedi nerede?", "Boş zaman"),
          ("Де кіт?", "Дозвілля"), ("گربه کجاست؟", "اوقات فراغت"), ("أين القطّ؟", "أوقات الفراغ"),
          ("Onde está o gato?", "Lazer"), ("Gdzie jest kot?", "Czas wolny"), ("Где кот?", "Досуг"),
          ("Wo ist die Katze?", "Freizeit"), ("¿Dónde está el gato?", "El tiempo libre")]
for gato, loi in TITRES:
    ancre = '        gato_tuile: "%s",' % gato
    if s.count(ancre) != 1:
        sys.exit("bloc I18N introuvable : %s" % gato)
    i = s.index(ancre) + len(ancre)
    ligne = nl + '        loi_tuile: "%s",' % loi
    if not s[i:i + len(ligne)] == ligne:
        s = s[:i] + ligne + s[i:]

# 4. la fonction d'ouverture (les lignes de panneau)
apres('function ouvrirThemeGato(){ ouvrirThemeIllustre("gato"); }', nl
      + "// les lignes « Les loisirs » des panneaux Adverbes (de, es) et Verbes (es, a cote de gustar)" + nl
      + 'function ouvrirThemeLoisirs(){ ouvrirThemeIllustre("loisirs"); }', "function ouvrirThemeLoisirs")

# 5. les panneaux
ADV = '                { icon:"casque", title:t("op_nomen_o5_t"), desc:tf("op_nomen_o5_d", { n: DICTEE_NOMS }), action:"startDicteeAdverbes", section:"pratique" }'
apres(ADV, nl.join([
    "",
    "            // 3 nov. 2026 : le theme illustre « Les loisirs », la frequence en images (un calendrier de quatre semaines)",
    "            ].concat(LANGUE_APPRISE === \"es\" || LANGUE_APPRISE === \"de\" ? [",
    "                { icon:\"exercice\", title:t(\"loi_tuile\"), desc:LANGUE_APPRISE === \"es\" ? \"siempre · a menudo · a veces · nunca\" : \"immer · oft · manchmal · nie · gern\", action:\"ouvrirThemeLoisirs\", section:\"pratique\" }",
    "            ] : [])"]).replace(nl + "            ].concat", nl + "            ].concat", 1), 'desc:LANGUE_APPRISE === "es" ? "siempre · a menudo')
# le crochet fermant d'origine du panneau Adverbes est maintenant en trop : « ] : [])\n            ]\n        };»
s = s.replace('            ] : [])' + nl + '            ]' + nl + '        };', '            ] : [])' + nl + '        };', 1)
GUSTAR = '                { icon:"exercice", title:t("op_es_gustar_t"), desc:t("op_es_gustar_d"), action:"startGustarUebung", section:"pratique" }'
apres(GUSTAR, "," + nl + "                // 3 nov. 2026 : le theme illustre « Les loisirs » (me gusta + infinitif, en images)" + nl
      + '                { icon:"exercice", title:t("loi_tuile"), desc:"me gusta bailar · ¿Quieres jugar al tenis?", action:"ouvrirThemeLoisirs", section:"pratique" }',
      'desc:"me gusta bailar · ¿Quieres jugar al tenis?"')

if s != avant:
    io.open(CH, "w", encoding="utf-8", newline="").write(s)
    print("  index.html branche")
else:
    print("  rien a faire : deja branche")
