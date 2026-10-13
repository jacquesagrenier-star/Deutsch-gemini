# -*- coding: utf-8 -*-
"""Pose TOUT le russe dans un depot, dans l'ordre du brief, et s'arrete a la
premiere erreur.

    python russe/outils/poser_tout.py [<racine_cible>]

<racine_cible> : le depot a modifier (par defaut, celui qui contient ce
script). Les fichiers russes (russe/...) et les outils sont toujours lus a
cote de ce script : on peut donc poser dans une COPIE jetable du depot
(cp -r, git worktree) sans rien y recopier a la main.

    1. interface      russe/interface.json  -> bloc « ru » de I18N (index.html)
    2. grammaire      russe/grammaire.json  -> grammaire.json, textes.ru
    3. corpus         russe/lots/*.json     -> tests/corpus_langue.py --langue ru pose
    4. examen         russe/examen/t*.json  -> pruefung.json (poser_examen.py)
    5. articles       russe/articles/t_ru.json -> index.html (patch_articles.py)
    6. exercices      russe/exercices/corr_*.json -> exercices.json (poser_exos.py)
    7. scenes         traductions/<scene>.ru.json, russe/scenes-page.json ->
                      construire.py et la page des scenes connaissent ru, puis
                      chaque scene est reconstruite
    8. prononciation  russe/prononciation_ru.py -> tests/prononciation.py, puis
                      prononciation.json (--ecrire)
    9. cablage        cablage_ru.py --ecrire (le code d'index.html, rangs
                      apres le polonais : voir l'hypothese en tete de ce script)

Chaque etape refuse de tourner si le russe est deja la : on ne pose pas
deux fois. Rien n'est committe : c'est au lanceur de relire le diff, puis
de faire tourner tests/verifier.py et tests/syntaxe.js.
"""
import glob
import io
import json
import os
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.dirname(os.path.dirname(ICI))          # le depot de ce script
RUSSE = os.path.join(SOURCE, "russe")
CIBLE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else SOURCE
PY = sys.executable


def etape(n, titre):
    print("\n=== %d. %s" % (n, titre))


def court(a):
    """Un chemin lisible dans le journal : relatif a la cible ou a la source."""
    if a == PY:
        return "python"
    if not os.path.isabs(a):
        return a
    for racine, nom in ((CIBLE, ""), (SOURCE, "<source>/")):
        if os.path.commonpath([a, racine]) == racine:
            return nom + os.path.relpath(a, racine)
    return a


def lancer(args, cwd=CIBLE, attendu=None, tolerer=False):
    """Lance un outil ; s'arrete s'il echoue (ou si sa sortie n'a pas `attendu`).
    tolerer=True : renvoie (code, sortie) au lieu de s'arreter sur un echec."""
    print("  $ " + " ".join(court(a) for a in args))
    p = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       encoding="utf-8")
    sortie = p.stdout.rstrip()
    if sortie:
        print("    " + sortie.replace("\n", "\n    "))
    if tolerer:
        return p.returncode, sortie
    if p.returncode != 0:
        sys.exit("ARRET : %s a echoue (code %d)" % (os.path.basename(args[1]), p.returncode))
    if attendu and not re.search(attendu, sortie):
        sys.exit("ARRET : sortie inattendue de %s (on attendait %r)"
                 % (os.path.basename(args[1]), attendu))
    return sortie


def lire(chemin):
    return io.open(chemin, encoding="utf-8", newline="").read()


def ecrire(chemin, texte):
    io.open(chemin, "w", encoding="utf-8", newline="").write(texte)


def nl_de(texte):
    return "\r\n" if "\r\n" in texte else "\n"


def js_chaine(v):
    if "</script" in v.lower():
        sys.exit("ARRET : « </script » dans un texte, il couperait la page : %r" % v[:60])
    return json.dumps(v, ensure_ascii=False).replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


# ------------------------------------------------------------------- etapes

def interface():
    chemin = os.path.join(CIBLE, "index.html")
    src = lire(chemin)
    nl = nl_de(src)
    a = src.index("const I18N = {")
    b = src.index(nl + "};", a)
    bloc = src[a:b]
    if re.search(r"\n    ru: \{", bloc):
        sys.exit("ARRET : I18N a deja un bloc ru")
    # L'ordre et la liste des cles : ceux du portugais (brief, section 1).
    debut_pt = bloc.index(nl + "    pt: {")
    fin_pt = bloc.index(nl + "    }", debut_pt)
    cles_pt = re.findall(r"^        ([A-Za-z0-9_]+): ", bloc[debut_pt:fin_pt], re.M)
    ru = json.load(io.open(os.path.join(RUSSE, "interface.json"), encoding="utf-8"))
    if set(ru) != set(cles_pt) or len(cles_pt) != len(set(cles_pt)):
        sys.exit("ARRET : interface.json %d cles, pt %d (en trop %s, manquantes %s)"
                 % (len(ru), len(cles_pt), sorted(set(ru) - set(cles_pt))[:5],
                    sorted(set(cles_pt) - set(ru))[:5]))
    if not bloc.endswith(nl + "    }"):
        sys.exit("ARRET : fin de I18N inattendue")
    lignes = ["        %s: %s," % (k, js_chaine(ru[k])) for k in cles_pt]
    ajout = "," + nl + "    ru: {" + nl + nl.join(lignes) + nl + "    }"
    ecrire(chemin, src[:b] + ajout + src[b:])
    print("  I18N : bloc ru, %d cles (ordre du portugais)" % len(lignes))


def grammaire():
    chemin = os.path.join(CIBLE, "grammaire.json")
    brut = lire(chemin)
    g = json.loads(brut)
    if json.dumps(g, ensure_ascii=False, separators=(",", ":")) != brut.rstrip("\n"):
        sys.exit("ARRET : grammaire.json ne se reproduit pas a l'identique")
    t = g["textes"]
    if "ru" in t:
        sys.exit("ARRET : grammaire.json a deja du russe")
    ru = json.load(io.open(os.path.join(RUSSE, "grammaire.json"), encoding="utf-8"))
    if set(ru) != set(t["pt"]):
        sys.exit("ARRET : grammaire russe %d cles, portugais %d" % (len(ru), len(t["pt"])))
    t["ru"] = dict((k, ru[k]) for k in t["pt"])
    fin = brut[len(brut.rstrip("\n")):]
    ecrire(chemin, json.dumps(g, ensure_ascii=False, separators=(",", ":")) + fin)
    print("  grammaire.json : %d textes ru" % len(ru))


def corpus():
    lots = sorted(glob.glob(os.path.join(RUSSE, "lots", "*.json")))
    if not lots:
        sys.exit("ARRET : aucun lot")
    outil = os.path.join(CIBLE, "tests", "corpus_langue.py")
    for lot in lots:
        lancer([PY, outil, "--langue", "ru", "pose", lot], attendu=r"champs poses")
    lancer([PY, outil, "--langue", "ru", "etat"])


def examen():
    fichiers = sorted(glob.glob(os.path.join(RUSSE, "examen", "t*.json")))
    lancer([PY, os.path.join(ICI, "poser_examen.py"), os.path.join(CIBLE, "pruefung.json"),
            "ru"] + fichiers + ["--ecrire"], attendu=r"ru : \d+ champs poses, 0 encore manquants")


def articles():
    chemin = os.path.join(CIBLE, "index.html")
    src = lire(chemin)
    # La langue precedente : la derniere colonne lue par construireExercicesArticles.
    m = re.search(r"lignes\.map\(\(\[phrase, genre, fr, en, dico((?:, \w+)*)\]\)", src)
    if not m:
        sys.exit("ARRET : colonnes des exercices d'articles introuvables")
    colonnes = [c.strip() for c in m.group(1).split(",") if c.strip()]
    if "ru" in colonnes:
        sys.exit("ARRET : les exercices d'articles ont deja le russe")
    prec = colonnes[-1]
    dump = os.path.join(SOURCE, ".claude", "russe", "outils", "articles_dump.jsonl")
    lancer([PY, os.path.join(ICI, "patch_articles.py"), chemin, "ru", prec,
            os.path.join(RUSSE, "articles", "t_ru.json"), dump, "--ecrire"],
           attendu=r"ok : \d+ textes ru")


def exercices():
    lancer([PY, os.path.join(ICI, "poser_exos.py"), CIBLE, os.path.join(RUSSE, "exercices")],
           attendu=r"ru : 40 jeux poses, 0 exercices a faire")


def scenes():
    proto = os.path.join(CIBLE, "visuel", "prototype")
    # 7a. Les traductions des scenes (fichiers neufs, deja versionnes sur la
    #     branche russe ; recopies si la cible ne les a pas).
    sources = sorted(glob.glob(os.path.join(SOURCE, "visuel", "prototype", "traductions", "*.ru.json")))
    if not sources:
        sys.exit("ARRET : aucune traduction de scene .ru.json")
    for s in sources:
        d = os.path.join(proto, "traductions", os.path.basename(s))
        if not os.path.exists(d):
            shutil.copyfile(s, d)
    noms = [os.path.basename(s)[:-len(".ru.json")] for s in sources]

    # 7b. construire.py connait le russe.
    chemin = os.path.join(proto, "construire.py")
    src = lire(chemin)
    nl = nl_de(src)
    if '"traduction_ru"' in src:
        sys.exit("ARRET : construire.py connait deja le russe")
    src, n1 = re.subn(r'(\nLANGUES = \[[^\]]*)\]', lambda m: m.group(1) + ', "ru"]', src, count=1)
    src, n2 = re.subn(r'(CHAMPS_MOT = \{[^}]*?)\}',
                      lambda m: m.group(1) + "," + nl + '              "ru": "traduction_ru"}', src, count=1)
    if (n1, n2) != (1, 1):
        sys.exit("ARRET : construire.py, LANGUES ou CHAMPS_MOT introuvable")
    ecrire(chemin, src)

    # 7c. La page des scenes : langue reconnue, repli, et ses 30 textes.
    chemin = os.path.join(proto, "index.html")
    src = lire(chemin)
    nl = nl_de(src)
    if re.search(r'\bru: \["ru"', src):
        sys.exit("ARRET : la page des scenes connait deja le russe")
    src, n1 = re.subn(r'(return \[[^\]]*)\]\.includes\(l\)', lambda m: m.group(1) + ', "ru"].includes(l)', src, count=1)
    src, n2 = re.subn(r'(const REPLI = \{.*?)\}\[LANGUE\];',
                      lambda m: m.group(1) + ', ru: ["ru", "en", "fr"]}[LANGUE];', src, count=1, flags=re.S)
    if (n1, n2) != (1, 1):
        sys.exit("ARRET : page des scenes, liste des langues ou REPLI introuvable")
    textes = json.load(io.open(os.path.join(RUSSE, "scenes-page.json"), encoding="utf-8"))
    a = src.index("const TEXTES = {")
    b = src.index(nl + "};", a)
    lignes = src[a:b].split(nl)
    vus = set()
    for i, l in enumerate(lignes):
        m = re.match(r"^  (\w+):\s*\{fr: .*\}(,?)$", l)
        if not m:
            continue
        cle = m.group(1)
        if cle not in textes:
            sys.exit("ARRET : scenes-page.json n'a pas « %s »" % cle)
        coeur = l[:-1] if m.group(2) else l
        lignes[i] = coeur[:-1] + ", ru: " + js_chaine(textes[cle]) + "}" + m.group(2)
        vus.add(cle)
    if vus != set(textes):
        sys.exit("ARRET : TEXTES et scenes-page.json different : %s" % sorted(set(textes) ^ vus))
    ecrire(chemin, src[:a] + nl.join(lignes) + src[b:])
    print("  page des scenes : ru reconnu, %d textes" % len(vus))

    # 7d. Chaque scene reconstruite (scene-<nom>.js et .es.js).
    for nom in noms:
        lancer([PY, chemin_construire(), nom], attendu=r"zones -> scene-")


def chemin_construire():
    return os.path.join(CIBLE, "visuel", "prototype", "construire.py")


def prononciation():
    chemin = os.path.join(CIBLE, "tests", "prononciation.py")
    src = lire(chemin)
    nl = nl_de(src)
    if re.search(r"^RU = \{", src, re.M):
        sys.exit("ARRET : tests/prononciation.py a deja RU")
    module = lire(os.path.join(RUSSE, "prononciation_ru.py"))
    a = module.index("# LE RUSSE")
    b = module.index("\n}\n", a) + 3
    bloc = module[a:b].replace("\n", nl)
    src, n1 = re.subn(r'(\nLANGUES = \([^)]*)\)', lambda m: m.group(1) + ', "ru")', src, count=1)
    k = src.index(nl + "GROUPES = [")
    src = src[:k] + nl + bloc + src[k:]
    ancien = ("            if rid in PT:" + nl
              + "                court = dict(court, pt=PT[rid][0])" + nl
              + "                expl = dict(expl, pt=PT[rid][1])" + nl)
    if src.count(ancien) != 1:
        sys.exit("ARRET : fusion PT introuvable dans construire()")
    src = src.replace(ancien, ancien
                      + "            if rid in RU:" + nl
                      + "                court = dict(court, ru=RU[rid][0])" + nl
                      + "                expl = dict(expl, ru=RU[rid][1])" + nl)
    src, n2 = re.subn(r'(for c in \(\s*"traduction",[^)]*?)\) if e\.get\(c\)',
                      lambda m: m.group(1) + ', "traduction_ru") if e.get(c)', src, count=1)
    if (n1, n2) != (1, 1):
        sys.exit("ARRET : tests/prononciation.py, LANGUES ou colonnes des exemples introuvables")
    ecrire(chemin, src)
    code, sortie = lancer([PY, chemin, "--ecrire"], tolerer=True)
    if code == 0 and re.search(r"0 faute", sortie):
        return
    # LES VOIX D'AURORA NE SONT PAS DANS LE DEPOT (.gitignore : audio/mp3/).
    # Dans une copie sans elles (session cloud), le script refuse chaque
    # exemple « sans voix » et n'ecrit rien. Ce controle-la ne depend pas du
    # russe : on ecrit alors prononciation.json par construire() lui-meme, en
    # le disant, et seulement si TOUTES les fautes sont des voix absentes.
    fautes = re.findall(r"FAUTE : (.*)", sortie)
    if (os.path.isdir(os.path.join(CIBLE, "audio", "mp3")) or not fautes
            or not all(f.endswith("sans voix d'Aurora") for f in fautes)):
        sys.exit("ARRET : tests/prononciation.py a echoue")
    import importlib.util
    spec = importlib.util.spec_from_file_location("prononciation_cible", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    d, fautes2 = mod.construire()
    if not all(f.endswith("sans voix d'Aurora") for f in fautes2):
        sys.exit("ARRET : tests/prononciation.py, fautes autres que les voix")
    io.open(os.path.join(CIBLE, "prononciation.json"), "w", encoding="utf-8",
            newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  audio/mp3 absent (hors depot) : %d exemples sans voix ignores ICI ;"
          " prononciation.json ecrit par construire(). A relancer sur le PC :"
          " python tests/prononciation.py --ecrire" % len(fautes))


def cablage():
    lancer([PY, os.path.join(ICI, "cablage_ru.py"), CIBLE, "--ecrire"], attendu=r"^ok : cablage russe pret")


ETAPES = [("interface", interface), ("grammaire", grammaire), ("corpus", corpus),
          ("examen", examen), ("articles", articles), ("exercices", exercices),
          ("scenes", scenes), ("prononciation", prononciation), ("cablage", cablage)]


def main():
    if not os.path.exists(os.path.join(CIBLE, "index.html")):
        sys.exit("pas un depot de l'app : " + CIBLE)
    print("source : %s\ncible  : %s" % (SOURCE, CIBLE))
    for n, (titre, f) in enumerate(ETAPES, 1):
        etape(n, titre)
        f()
    print("\nTOUT EST POSE. A faire maintenant, dans la cible :"
          "\n  python tests/verifier.py && node tests/syntaxe.js"
          "\n  python tests/corpus_langue.py --langue ru etat")


if __name__ == "__main__":
    main()
