# -*- coding: utf-8 -*-
"""Pose l'arabe des textes de l'espagnol HORS corpus (15 oct. 2026).

    python espanol/ar/poser_autres.py controle [nom ...]   # lit les lots, n'ecrit rien
    python espanol/ar/poser_autres.py pose [nom ...]       # ecrit

nom parmi : i18n categories mots-outils grammaire prononciation variantes scenes
(tous par defaut). Les sources sont dans espanol/ar/sources/<nom>.json (faites par
extraire.py), les traductions dans espanol/ar/lots/<nom>.ar.json -- pour les scenes,
tous les lots/scenes-*.ar.json reunis.

Ou va l'arabe :
  i18n           index.html, bloc « "ar" » de I18N_ESPAGNOL, juste apres « "pt" »
  categories     index.html, « ar: » au bout de chaque ligne des deux tables espagnoles
  mots-outils    index.html, const MOTS_OUTILS_ES_AR (rangs 23-25), apres MOTS_OUTILS_ES_PT
  grammaire      espanol/datos/grammaire.json : textes.ar et une cle « ar » apres chaque « pt »
  prononciation  tests/prononciation_es.py, dictionnaire AR ; puis --ecrire refait le JSON
  variantes      espanol/datos/variantes.json : remarque.ar
  scenes         visuel/prototype/espanol/<scene>.json : titre_ar / n_ar juste apres titre_pt / n_pt
                 (insertion dans le texte : dix de ces fichiers ne sont pas au format json.dumps)

Garde-fous : chaque id de la source a sa traduction (et aucune en trop) ; chaque
texte arabe porte de l'arabe (sauf s'il recopie un texte purement espagnol) ; les
{marques} et les balises HTML sont celles du francais. Une faute arrete tout, rien
n'est ecrit.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.environ.get("ESSAI_RACINE") or os.path.dirname(os.path.dirname(ICI))   # essai sur une copie
LOTS = os.environ.get("ESSAI_LOTS") or os.path.join(ICI, "lots")
INDEX = os.path.join(RACINE, "index.html")
NOMS = ["i18n", "categories", "mots-outils", "grammaire", "prononciation", "variantes", "scenes"]
ARABE = re.compile(u"[\u0600-\u06ff]")
MARQUE = re.compile(r"\{[a-zA-Z_0-9]+\}")
BALISE = re.compile(r"</?([a-zA-Z]+)[^>]*>")


def lire(chemin):
    return io.open(chemin, encoding="utf-8", newline="").read()


def ecrire(chemin, texte):
    io.open(chemin, "w", encoding="utf-8", newline="").write(texte)


def sources(nom):
    return json.load(io.open(os.path.join(ICI, "sources", nom + ".json"), encoding="utf-8"))


def lots(nom):
    if nom == "scenes":
        chemins = sorted(glob.glob(os.path.join(LOTS, "scenes-*.ar.json")))
    else:
        chemins = [os.path.join(LOTS, nom + ".ar.json")]
    out = {}
    for c in chemins:
        if not os.path.exists(c):
            raise SystemExit("%s : lot absent (%s)" % (nom, c))
        for k, v in json.load(io.open(c, encoding="utf-8")).items():
            if k in out and out[k] != v:
                raise SystemExit("%s : %s traduit deux fois, differemment" % (nom, k))
            out[k] = v
    return out


def balises(t):
    return sorted(m.group(0).split()[0].rstrip(">").lower() for m in BALISE.finditer(t))


def verifier_texte(nom, id_, fr, pt, ar, fautes, avis):
    if not isinstance(ar, str) or not ar.strip():
        fautes.append("%s %s : vide" % (nom, id_))
        return
    if not ARABE.search(ar) and ar not in (fr, pt):
        fautes.append("%s %s : pas d'arabe : %s" % (nom, id_, ar[:60]))
    if sorted(MARQUE.findall(ar)) != sorted(MARQUE.findall(fr)):
        fautes.append("%s %s : marques %s au lieu de %s" % (nom, id_, MARQUE.findall(ar), MARQUE.findall(fr)))
    if balises(ar) != balises(fr) and balises(ar) != balises(pt):
        avis.append("%s %s : balises %s (fr %s)" % (nom, id_, balises(ar), balises(fr)))
    if "|" in ar:
        avis.append("%s %s : barre verticale dans le texte" % (nom, id_))


def controler(nom):
    src, trad = sources(nom), lots(nom)
    fautes, avis = [], []
    ids = [e["id"] for e in src]
    for k in sorted(set(trad) - set(ids)):
        fautes.append("%s : id inconnu %s" % (nom, k))
    for e in src:
        ar = trad.get(e["id"])
        if ar is None:
            fautes.append("%s : %s non traduit" % (nom, e["id"]))
            continue
        if nom in ("mots-outils", "prononciation"):
            n = 3 if nom == "mots-outils" else 2
            if not isinstance(ar, list) or len(ar) != n:
                fautes.append("%s %s : %d textes attendus" % (nom, e["id"], n))
                continue
            for i in range(n):
                verifier_texte(nom, "%s[%d]" % (e["id"], i), e["fr"][i], e["pt"][i], ar[i], fautes, avis)
        else:
            verifier_texte(nom, e["id"], e["fr"], e["pt"], ar, fautes, avis)
    return src, trad, fautes, avis


# ---------------------------------------------------------------- index.html

def poser_i18n(src, trad, html):
    debut = html.index("const I18N_ESPAGNOL = {")
    if re.search(r'\n    "ar": \{', html[debut:html.index("\n};", debut)]):
        raise SystemExit("i18n : I18N_ESPAGNOL a deja un bloc ar")
    pt = html.index('\n    "pt": {\n', debut)
    fin = html.index("\n    }\n};", pt)
    lignes = ['        %s: %s' % (json.dumps(e["id"]), json.dumps(trad[e["id"]], ensure_ascii=False)) for e in src]
    bloc = '\n    },\n    "ar": {\n' + ",\n".join(lignes) + "\n    }\n};"
    return html[:fin] + bloc + html[fin + len("\n    }\n};"):]


def poser_categories(src, trad, html):
    for e in src:
        table, cle = e["id"].split("|", 1)
        debut = html.index("const %s = LANGUE_APPRISE" % table)
        motif = re.compile(r'^(    %s:\s*\{ fr: ".*?", en: ".*?", pt: ".*?")( \},?)\s*$' % re.escape(json.dumps(cle)), re.M)
        m = motif.search(html, debut)
        if not m:
            raise SystemExit("categories : ligne introuvable pour " + e["id"])
        html = html[:m.start()] + m.group(1) + ", ar: " + json.dumps(trad[e["id"]], ensure_ascii=False) \
            + m.group(2) + html[m.end():]
    return html


def poser_mots_outils(src, trad, html):
    if "const MOTS_OUTILS_ES_AR" in html:
        raise SystemExit("mots-outils : MOTS_OUTILS_ES_AR existe deja")
    table = {}
    for e in src:
        cle, es = e["id"].split("|", 1)
        table.setdefault(cle, {})[es] = trad[e["id"]]
    m = re.search(r"^const MOTS_OUTILS_ES_PT = \{.*?\n\};\n", html, re.S | re.M)
    const = ("// L'ARABE DES MOTS-OUTILS ESPAGNOLS (15 oct. 2026), aux rangs 23-25 de\n"
             "// RANGS_CARTE.funktionswort, comme le portugais aux rangs 20-22.\n"
             "const MOTS_OUTILS_ES_AR = " + json.dumps(table, ensure_ascii=False, indent=2) + ";\n")
    html = html[:m.end()] + const + html[m.end():]
    ancien = ("            if(p){ w[20] = p[0]; w[21] = p[1]; w[22] = p[2]; }\n")
    if html.count(ancien) != 1:
        raise SystemExit("mots-outils : boucle de pose introuvable")
    nouveau = ancien + ("            const a = MOTS_OUTILS_ES_AR[cle][w[0]];\n"
                        "            if(a){ w[23] = a[0]; w[24] = a[1]; w[25] = a[2]; }\n")
    return html.replace(ancien, nouveau)


# ---------------------------------------------------------------- JSON

def json_reproduit(chemin):
    brut = lire(chemin)
    d = json.loads(brut)

    def ser(o):
        t = json.dumps(o, ensure_ascii=False, indent=1) + ("\n" if brut.endswith("\n") else "")
        return t.replace("\n", "\r\n") if "\r\n" in brut else t
    if ser(d) != brut:
        raise SystemExit(chemin + " : ne se reproduit pas a l'identique, rien n'est ecrit")
    return d, ser


def apres_pt(o, ar):
    """Copie de o avec « ar » insere juste apres « pt »."""
    out = {}
    for k, v in o.items():
        if k == "ar":
            continue
        out[k] = v
        if k == "pt":
            out["ar"] = ar
    return out


def poser_grammaire(src, trad):
    chemin = os.path.join(RACINE, "espanol", "datos", "grammaire.json")
    d, ser = json_reproduit(chemin)
    textes = dict(d["textes"])
    textes["ar"] = {e["id"].split("|", 1)[1]: trad[e["id"]] for e in src if e["id"].startswith("textes|")}
    d["textes"] = textes
    par_chemin = {e["id"]: trad[e["id"]] for e in src if e["id"].startswith("fiches/")}
    vus = set()

    def marcher(o, chemin_):
        if isinstance(o, dict):
            if "pt" in o and "fr" in o:
                vus.add(chemin_)
                return apres_pt(o, par_chemin[chemin_])
            return {k: marcher(v, chemin_ + "/" + k) for k, v in o.items()}
        if isinstance(o, list):
            return [marcher(v, chemin_ + "/" + str(i)) for i, v in enumerate(o)]
        return o
    d["fiches"] = [marcher(f, "fiches/" + f["id"]) for f in d["fiches"]]
    if vus != set(par_chemin):
        raise SystemExit("grammaire : chemins non poses %s" % sorted(set(par_chemin) - vus)[:5])
    ecrire(chemin, ser(d))
    print("  grammaire      %d textes + %d dans les fiches" % (len(textes["ar"]), len(vus)))


def poser_variantes(src, trad):
    chemin = os.path.join(RACINE, "espanol", "datos", "variantes.json")
    d, ser = json_reproduit(chemin)
    for e in src:
        cle, mot = e["id"].split("|", 1)
        d[cle][mot]["remarque"] = apres_pt(d[cle][mot]["remarque"], trad[e["id"]])
    ecrire(chemin, ser(d))
    print("  variantes      %d" % len(src))


def poser_prononciation(src, trad):
    chemin = os.path.join(RACINE, "tests", "prononciation_es.py")
    brut = lire(chemin)
    nl = "\r\n" if "\r\n" in brut else "\n"
    debut, fin = "AR = {" + nl, "# AR-FIN" + nl
    i, j = brut.index(debut) + len(debut), brut.index(fin)
    if brut[i:j].strip():
        raise SystemExit("prononciation : AR n'est pas vide")
    lignes = "".join(' %s: (%s,%s      %s),%s' % (json.dumps(e["id"]), json.dumps(trad[e["id"]][0], ensure_ascii=False),
                                               nl, json.dumps(trad[e["id"]][1], ensure_ascii=False), nl) for e in src)
    ecrire(chemin, brut[:i] + lignes + brut[j:])
    r = subprocess.run([sys.executable, chemin, "--ecrire"], capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip())
    if r.returncode:
        raise SystemExit("prononciation_es.py --ecrire a echoue : " + r.stderr)
    print("  prononciation  %d regles" % len(src))


def poser_scenes(src, trad):
    dossier = os.path.join(RACINE, "visuel", "prototype", "espanol")
    par_fichier = {}
    for e in src:
        par_fichier.setdefault(e["id"].split("|", 1)[0], []).append(e)
    total = 0
    for nom, entrees in sorted(par_fichier.items()):
        chemin = os.path.join(dossier, nom + ".json")
        brut = lire(chemin)
        if '"n_ar"' in brut or '"titre_ar"' in brut:
            raise SystemExit("scenes : %s a deja de l'arabe" % nom)
        # (cle, valeur pt) -> files des traductions, dans l'ordre du document
        attente = {}
        for e in entrees:
            cle = "titre_pt" if e["id"].endswith("|titre") else "n_pt"
            attente.setdefault((cle, e["pt"]), []).append(trad[e["id"]])
        motif = re.compile(r'(^[ \t]*)?"(titre_pt|n_pt)": ("(?:[^"\\]|\\.)*")', re.M)
        morceaux, pos, poses = [], 0, 0
        for m in motif.finditer(brut):
            cle, val = m.group(2), json.loads(m.group(3))
            file_ = attente.get((cle, val))
            if not file_:
                raise SystemExit("scenes : %s, %s sans traduction : %s" % (nom, cle, val[:50]))
            ar = json.dumps(file_.pop(0), ensure_ascii=False)
            cle_ar = cle[:-3] + "_ar"
            if m.group(1) is not None:          # la cle commence la ligne
                nl = "\r\n" if "\r\n" in brut else "\n"
                ajout = ',%s%s"%s": %s' % (nl, m.group(1), cle_ar, ar)
            else:                                # plusieurs cles sur la meme ligne
                ajout = ', "%s": %s' % (cle_ar, ar)
            morceaux.append(brut[pos:m.end()] + ajout)
            pos = m.end()
            poses += 1
        reste = [k for k, v in attente.items() if v]
        if reste:
            raise SystemExit("scenes : %s, %d traduction(s) sans place" % (nom, len(reste)))
        nouveau = "".join(morceaux) + brut[pos:]
        json.loads(nouveau)
        ecrire(chemin, nouveau)
        total += poses
    print("  scenes         %d textes dans %d fichiers" % (total, len(par_fichier)))


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("controle", "pose"):
        print(__doc__)
        return
    noms = a[1:] or NOMS
    lu, toutes_fautes = {}, []
    for nom in noms:
        src, trad, fautes, avis = controler(nom)
        lu[nom] = (src, trad)
        for x in avis:
            print("  avis :", x)
        for x in fautes:
            print("  FAUTE :", x)
        toutes_fautes += fautes
        print("  %-14s %d textes, %d faute(s), %d avis" % (nom, len(src), len(fautes), len(avis)))
    if toutes_fautes:
        raise SystemExit("%d faute(s) : rien n'est ecrit" % len(toutes_fautes))
    if a[0] == "controle":
        return
    html = lire(INDEX)
    avant = html
    for nom, f in (("i18n", poser_i18n), ("categories", poser_categories), ("mots-outils", poser_mots_outils)):
        if nom in lu:
            html = f(lu[nom][0], lu[nom][1], html)
            print("  %-14s pose dans index.html" % nom)
    if html != avant:
        ecrire(INDEX, html)
    for nom, f in (("grammaire", poser_grammaire), ("variantes", poser_variantes),
                   ("prononciation", poser_prononciation), ("scenes", poser_scenes)):
        if nom in lu:
            f(*lu[nom])


if __name__ == "__main__":
    main()
