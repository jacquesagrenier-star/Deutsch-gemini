# Pose dans pruefung.json les champs d'examen MANQUANTS d'une langue.
#   python poser_examen.py <pruefung.json> <langue> <t1.json> [t2.json ...] [--ecrire]
# Cle d'une traduction : "<section>/<i>[/<j>]|<base>" (base = consigne, trad,
# erkl, frage, options, aufgabe). Refuse : un id qui ne correspond a aucun
# champ manquant, une liste d'options de mauvaise longueur, des chevrons
# francais (sauf en uk/fa/ar/ru, qui les emploient), un caractere de controle, et
# un fichier qui ne se reecrirait pas a l'identique hors champs ajoutes.
import io, json, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
CIBLE, LANGUE, FICHIERS = args[0], args[1], args[2:]
ECRIRE = "--ecrire" in sys.argv
CHEVRONS_PERMIS = LANGUE in ("uk", "fa", "ar", "ru")

trad = {}
for f in FICHIERS:
    for k, v in json.load(io.open(f, encoding="utf-8")).items():
        if k in trad:
            sys.exit("DOUBLON " + k)
        trad[k] = v

brut = io.open(CIBLE, encoding="utf-8", newline="").read()
crlf = "\r\n" in brut
d = json.loads(brut)

def rendu(o):
    s = json.dumps(o, ensure_ascii=False, indent=1)
    return s.replace("\n", "\r\n") if crlf else s

fin = brut[len(brut.rstrip("\r\n")):]
if rendu(d) + fin != brut:
    sys.exit("FORMAT : le fichier ne se reecrit pas a l'identique")

poses, manquants = set(), []

def controle(cle, fr, t):
    if isinstance(fr, list):
        if not isinstance(t, list) or len(t) != len(fr):
            sys.exit("OPTIONS " + cle)
        textes = t
    else:
        if not isinstance(t, str):
            sys.exit("TYPE " + cle)
        textes = [t]
    for s in textes:
        if not s.strip() or any(ord(c) < 32 for c in s) or (not CHEVRONS_PERMIS and ("«" in s or "»" in s)):
            sys.exit("TEXTE %s : %r" % (cle, s))

def poser(path, o):
    sortie = {}
    cles = list(o.keys())
    for i, k in enumerate(cles):
        sortie[k] = o[k]
        if "_" not in k or k.startswith("_"):
            continue
        base = k.rsplit("_", 1)[0]
        if base + "_fr" not in o or (base + "_" + LANGUE) in o:
            continue
        suivantes = [c for c in cles[i + 1:] if "_" in c and c.rsplit("_", 1)[0] == base]
        if suivantes:
            continue
        cle = path + "|" + base
        if cle not in trad:
            manquants.append(cle)
            continue
        controle(cle, o[base + "_fr"], trad[cle])
        sortie[base + "_" + LANGUE] = trad[cle]
        poses.add(cle)
    return sortie

for sec in ["sprechen", "schreiben", "lesen", "hoeren"]:
    for i, o in enumerate(d[sec]):
        p = sec + "/" + str(i)
        if sec == "lesen":
            o["fragen"] = [poser(p + "/" + str(j), q) for j, q in enumerate(o.get("fragen", []))]
        d[sec][i] = poser(p, o)

reste = set(trad) - poses
if reste:
    sys.exit("SANS CHAMP MANQUANT : " + ", ".join(sorted(reste)[:5]))
print("%s : %d champs poses, %d encore manquants" % (LANGUE, len(poses), len(manquants)))
if ECRIRE:
    io.open(CIBLE, "w", encoding="utf-8", newline="").write(rendu(d) + fin)
    print("ecrit")
