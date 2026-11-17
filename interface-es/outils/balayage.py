# -*- coding: utf-8 -*-
"""Ou un texte existe-t-il en russe (derniere langue d'interface posee) mais pas en espagnol ?

    python interface-es/outils/balayage.py [dossier ...]

JSON : tout objet qui porte « ru » (ou un champ *_ru) sans son pendant espagnol.
JS / HTML : toute ligne qui nomme ru (ru:, _ru, "ru") sans nommer es.
Par defaut : le depot entier hors des langues apprises et des archives. Une ligne
signalee n'est pas forcement un trou (une table de l'espagnol APPRIS, un essai) :
c'est une question.
"""
import io, json, os, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXCLUS = ("espanol/", "anglais/", "japonais/", "portugais/", "russe/", "polonais/", "retours/", "tests/",
          "interface-es/", "ajouts/", "audio/", "fusion-espagnol/", "video/", "export/", ".claude/", "scenes/",
          "etoiles/sources/", "pflege/sources/", "relecture_", "corrections_", "Indexbackup")
RU = re.compile(r'(\bru\s*:|_ru\b|"ru"|\'ru\'|[a-z]Ru\b)')
ES = re.compile(r'(\bes\s*:|_es\b|"es"|\'es\'|[a-z]Es\b)')
dossiers = sys.argv[1:]
fichiers = subprocess.run(["git", "ls-files"] + dossiers, cwd=RACINE, capture_output=True, text=True,
                          encoding="utf-8").stdout.split("\n")


def json_trous(o, ch, out):
    if isinstance(o, dict):
        if "ru" in o and "es" not in o and isinstance(o.get("ru"), (str, list)):
            out.append(ch)
        for k, v in o.items():
            if k.endswith("_ru") and (k[:-3] + "_es") not in o:
                out.append(ch + "/" + k)
            json_trous(v, ch + "/" + k, out)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            json_trous(v, ch + "/" + str(i), out)


total = 0
for f in fichiers:
    if not f or f.startswith(EXCLUS) or not re.search(r"\.(json|js|html)$", f):
        continue
    if re.search(r"scene-.*\.(es|en|pt|ja)\.js$|/traductions/.*\.(ru|tr|uk|fa|ar|pt|pl|en|de)\.json$", f):
        continue
    p = os.path.join(RACINE, f)
    try:
        s = io.open(p, encoding="utf-8").read()
    except Exception:
        continue
    if "ru" not in s:
        continue
    trous = []
    if f.endswith(".json"):
        try:
            json_trous(json.loads(s), "", trous)
        except Exception:
            continue
    else:
        for i, l in enumerate(s.split("\n"), 1):
            if RU.search(l) and not ES.search(l):
                trous.append("ligne %d" % i)
    if trous:
        total += len(trous)
        print("%-60s %5d  ex. %s" % (f, len(trous), trous[0][:60]))
print("total", total)
