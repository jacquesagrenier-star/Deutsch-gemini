# -*- coding: utf-8 -*-
"""Ouvre les pages d'examen (DTZ, telc, telc-pflege) a l'espagnol, langue d'interface de l'allemand.

    python interface-es/outils/cablage_telc_es.py [--ecrire]

Le dictionnaire visuel/prototype/telc/langues/es.json -> es.js est pose a part
(node visuel/prototype/telc/outils/langues.js construire es). La langue ne s'ouvre
dans l'app (LANGUES_PAGES_TELC d'index.html) que quand `node tests/telc_langues.js`
ne trouve plus aucun manque. Demande du chef (15 nov. 2026, signale par pflege-examen) :
dtz/commun.js n'acceptait pas lang=es.
"""
import io, os, sys
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RACINE, "visuel", "prototype")
L7 = '["tr", "uk", "fa", "ar", "pt", "pl", "ru"]'
L9 = '["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]'
CAS = [
    ("dtz/commun.js", 'const LANGUE = (l => ' + L9, 'const LANGUE = (l => ' + L9[:-1] + ', "es"]', 1),
    ("telc/telc.html", 'if (' + L7 + '.includes(l))', 'if (' + L7[:-1] + ', "es"].includes(l))', 1),
    ("telc/oral.html", 'if (' + L7 + '.includes(l))', 'if (' + L7[:-1] + ', "es"].includes(l))', 1),
    ("telc/oral.html", 'const LANG = (l => ' + L9, 'const LANG = (l => ' + L9[:-1] + ', "es"]', 1),
    ("telc-pflege/telc.html", 'if (' + L7 + '.includes(l))', 'if (' + L7[:-1] + ', "es"].includes(l))', 1),
    ("telc/telc-commun.js", 'uk: ["«", "»"], ru: ["«", "»"], fa: ["«", "»"], ar: ["«", "»"] })',
     'uk: ["«", "»"], ru: ["«", "»"], fa: ["«", "»"], ar: ["«", "»"], es: ["«", "»"] })', 1),
    ("telc/telc-commun.js", 'pl: "pl-PL", ru: "ru-RU" })', 'pl: "pl-PL", ru: "ru-RU", es: "es-MX" })', 1),
    ("telc/outils/langues.js", 'const LANGUES = ' + L7 + ';', 'const LANGUES = ' + L7[:-1] + ', "es"];', 1),
]
fichiers = {}
for rel, avant, apres, n in CAS:
    p = os.path.join(P, rel)
    s = fichiers.get(p) or io.open(p, encoding="utf-8", newline="").read()
    c = s.count(avant)
    if c != n:
        sys.exit("%s : ATTENDU %d, TROUVE %d : %r" % (rel, n, c, avant[:80]))
    fichiers[p] = s.replace(avant, apres)
print("ok : %d remplacements dans %d fichiers" % (len(CAS), len(fichiers)))
if "--ecrire" in sys.argv:
    for p, s in fichiers.items():
        io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("ecrit")
