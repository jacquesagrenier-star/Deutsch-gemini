# -*- coding: utf-8 -*-
"""Pose l'ALLEMAND des textes de l'espagnol HORS corpus (1er nov. 2026).

    python espanol/de/poser_autres.py controle [nom ...]   # lit les lots, n'ecrit rien
    python espanol/de/poser_autres.py pose [nom ...]       # ecrit

Les sources sont dans espanol/de/sources/<nom>.json (faites par extraire.py),
les traductions dans espanol/de/lots/<nom>.de.json -- pour les noms marques *,
tous les lots/<nom>-*.de.json reunis (un gros fichier se rend en morceaux).

Ou va l'allemand :
  i18n *         index.html, bloc « de: » de I18N (par tests/fusion_langue.py, qui relit)
  surcharge-es   index.html, bloc « "de" » de I18N_ESPAGNOL, juste apres « "ar" »
  categories     index.html, « de: » au bout de chaque ligne des deux tables espagnoles
  mots-outils    index.html, const MOTS_OUTILS_ES_DE (rangs 32-34), apres MOTS_OUTILS_ES_AR
  vignettes      index.html, ligne « de: [...] » de SCENES_COURTS
  page-scenes    visuel/prototype/index.html, « de: » au bout de chaque ligne de TEXTES
  grammaire      espanol/datos/grammaire.json : textes.de et une cle « de » apres chaque « ar »
  prononciation  tests/prononciation_es.py, dictionnaire DE ; puis --ecrire refait le JSON
  variantes      espanol/datos/variantes.json : remarque.de
  peintres       espanol/mosaique/peintres.json : « de » apres « pt »
  scenes *       visuel/prototype/espanol/<scene>.json : titre_de / n_de juste apres
                 titre_ar / n_ar ; alt_de et consigne_de en tete du fichier
  premiers-pas, a1-voyage, reperes, conjugaison *
                 espanol/datos/<nom>.json : « de » apres « ar » dans chaque objet de langue

Garde-fous : chaque id de la source a sa traduction (et aucune en trop) ; aucun
texte ne recopie le francais ou l'anglais (sauf s'il n'est fait que d'espagnol) ;
les {marques} et les balises HTML sont celles du francais. Une faute arrete
tout, rien n'est ecrit. Chaque fichier JSON doit se reproduire a l'octet pres
avant d'etre ecrit.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.environ.get("ESSAI_RACINE") or os.path.dirname(os.path.dirname(ICI))   # essai sur une copie
LOTS = os.environ.get("ESSAI_LOTS") or os.path.join(ICI, "lots")
INDEX = os.path.join(RACINE, "index.html")
PAGE_SCENES = os.path.join(RACINE, "visuel", "prototype", "index.html")
OBJETS = ["premiers-pas", "a1-voyage", "reperes", "conjugaison"]
NOMS = ["i18n", "surcharge-es", "categories", "mots-outils", "vignettes", "page-scenes", "grammaire",
        "prononciation", "variantes", "peintres", "scenes"] + OBJETS
EN_MORCEAUX = {"i18n", "scenes"} | set(OBJETS)
MARQUE = re.compile(r"\{[a-zA-Z_0-9]+\}")
BALISE = re.compile(r"</?([a-zA-Z]+)[^>]*>")
sys.path.insert(0, ICI)
from poser import doute_allemand   # noqa: E402


def lire(chemin):
    return io.open(chemin, encoding="utf-8", newline="").read()


def ecrire(chemin, texte):
    io.open(chemin, "w", encoding="utf-8", newline="").write(texte)


def sources(nom):
    return json.load(io.open(os.path.join(ICI, "sources", nom + ".json"), encoding="utf-8"))


def lots(nom):
    chemins = [os.path.join(LOTS, nom + ".de.json")]
    if nom in EN_MORCEAUX:
        chemins = sorted(glob.glob(os.path.join(LOTS, nom + "-*.de.json"))) + \
            [c for c in chemins if os.path.exists(c)]
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


def verifier_texte(nom, id_, fr, en, de, fautes, avis):
    if not isinstance(de, str) or not de.strip():
        if fr.strip():
            fautes.append("%s %s : vide" % (nom, id_))
        return
    # Un texte identique en francais et en anglais n'est fait que d'exemples
    # (« lo · la · le · se », « Con tener — tener ganas ») : il se recopie.
    # Pareil pour une liste d'exemples espagnols recopiee du francais.
    espagnol_seul = de in (fr, en) and re.search(r"[ñáíóú¿¡]|(?<!\w)(?:el|la|los|las|un|una|este|ese|mi|lo|le|se)(?!\w)", de) \
        and not re.search(r"(?<!\w)(?:et|est|les|des|du|pour|avec|dans)(?!\w)", de)
    d = None if (de == fr and fr == en) or espagnol_seul else doute_allemand(re.sub(r"<[^>]+>", " ", de), re.sub(r"<[^>]+>", " ", fr), re.sub(r"<[^>]+>", " ", en))
    if d:
        # Un mot court identique au francais (« Info », « Menu ») est permis.
        (fautes if d == "identique au francais ou a l'anglais" else avis).append("%s %s : %s : %s" % (nom, id_, d, de[:70]))
    if sorted(MARQUE.findall(de)) != sorted(MARQUE.findall(fr)):
        fautes.append("%s %s : marques %s au lieu de %s" % (nom, id_, MARQUE.findall(de), MARQUE.findall(fr)))
    if balises(de) != balises(fr) and balises(de) != balises(en):
        avis.append("%s %s : balises %s (fr %s)" % (nom, id_, balises(de), balises(fr)))
    if "|" in de and "|" not in fr:
        avis.append("%s %s : barre verticale dans le texte" % (nom, id_))


def controler(nom):
    src, trad = sources(nom), lots(nom)
    fautes, avis = [], []
    ids = [e["id"] for e in src]
    for k in sorted(set(trad) - set(ids)):
        fautes.append("%s : id inconnu %s" % (nom, k))
    for e in src:
        de = trad.get(e["id"])
        if de is None:
            fautes.append("%s : %s non traduit" % (nom, e["id"]))
            continue
        if nom in ("mots-outils", "prononciation"):
            n = 3 if nom == "mots-outils" else 2
            if not isinstance(de, list) or len(de) != n:
                fautes.append("%s %s : %d textes attendus" % (nom, e["id"], n))
                continue
            for i in range(n):
                verifier_texte(nom, "%s[%d]" % (e["id"], i), e["fr"][i], e["en"][i], de[i], fautes, avis)
        else:
            verifier_texte(nom, e["id"], e["fr"], e["en"], de, fautes, avis)
    return src, trad, fautes, avis


# ---------------------------------------------------------------- index.html

def poser_i18n(src, trad, html):
    """Le bloc « de: » de I18N, juste avant sa fermeture (apres ru).

    ⚠️ PAS PAR tests/fusion_langue.py : il cherche « \\n    de: { » dans TOUT le
    fichier pour savoir si le bloc existe, et « de: { A1: [...] » (les series
    d'exercices allemandes) lui repond -- il y a verse les 1 600 cles. On borne
    donc la recherche au dictionnaire I18N, et i18n_dump.js relit apres."""
    deb = html.index("const I18N = {")
    fin = html.index("\n};", deb)
    if re.search(r"\n    de: \{", html[deb:fin]):
        raise SystemExit("i18n : I18N a deja un bloc de")
    avant = html[:fin].rstrip()
    if not avant.endswith(","):
        avant += ","
    lignes = "".join('\n        %s: %s,' % (e["id"], json.dumps(trad[e["id"]], ensure_ascii=False)) for e in src)
    return avant + "\n    de: {" + lignes.rstrip(",") + "\n    }" + html[fin:]


def relire_i18n(src, trad):
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js"), "de"], capture_output=True, cwd=RACINE)
    if r.returncode:
        raise SystemExit("i18n : node ne relit pas le bloc I18N :\n" + r.stderr.decode("utf-8", "replace")[:800])
    relu = json.loads(r.stdout.decode("utf-8")).get("de", {})
    ecarts = [e["id"] for e in src if relu.get(e["id"]) != trad[e["id"]]]
    if ecarts or len(relu) != len(src):
        raise SystemExit("i18n : %d ecart(s) a la relecture (%s), %d cles relues" % (len(ecarts), ecarts[:5], len(relu)))
    print("  i18n           %d cles, relues par node a l'identique" % len(relu))


def poser_i18n_es(src, trad, html):
    debut = html.index("const I18N_ESPAGNOL = {")
    if re.search(r'\n    "de": \{', html[debut:html.index("\n};", debut)]):
        raise SystemExit("surcharge-es : I18N_ESPAGNOL a deja un bloc de")
    ar = html.index('\n    "ar": {', debut)
    fin = html.index("\n    },", ar)
    lignes = ['        %s: %s' % (json.dumps(e["id"]), json.dumps(trad[e["id"]], ensure_ascii=False)) for e in src]
    bloc = '\n    },\n    "de": {\n' + ",\n".join(lignes)
    return html[:fin] + bloc + html[fin:]


def poser_categories(src, trad, html):
    for e in src:
        table, cle = e["id"].split("|", 1)
        debut = html.index("const %s = LANGUE_APPRISE" % table)
        motif = re.compile(r'^(    %s:\s*\{ fr: ".*?", en: ".*?", pt: ".*?", ar: ".*?")( \},?)\s*$'
                           % re.escape(json.dumps(cle)), re.M)
        m = motif.search(html, debut)
        if not m:
            raise SystemExit("categories : ligne introuvable pour " + e["id"])
        html = html[:m.start()] + m.group(1) + ", de: " + json.dumps(trad[e["id"]], ensure_ascii=False) \
            + m.group(2) + html[m.end():]
    return html


def poser_mots_outils(src, trad, html):
    if "const MOTS_OUTILS_ES_DE" in html:
        raise SystemExit("mots-outils : MOTS_OUTILS_ES_DE existe deja")
    table = {}
    for e in src:
        cle, es = e["id"].split("|", 1)
        table.setdefault(cle, {})[es] = trad[e["id"]]
    m = re.search(r"^const MOTS_OUTILS_ES_AR = \{.*?\n\};\n", html, re.S | re.M)
    const = ("// L'ALLEMAND DES MOTS-OUTILS ESPAGNOLS (1er nov. 2026), aux rangs 32-34 de\n"
             "// RANGS_CARTE.funktionswort (le polonais et le russe tiennent 26-31).\n"
             "const MOTS_OUTILS_ES_DE = " + json.dumps(table, ensure_ascii=False, indent=2) + ";\n")
    html = html[:m.end()] + const + html[m.end():]
    ancien = ("            if(a){ w[23] = a[0]; w[24] = a[1]; w[25] = a[2]; }\n")
    if html.count(ancien) != 1:
        raise SystemExit("mots-outils : boucle de pose introuvable")
    nouveau = ancien + ("            const d = MOTS_OUTILS_ES_DE[cle][w[0]];\n"
                        "            if(d){ w[32] = d[0]; w[33] = d[1]; w[34] = d[2]; }\n")
    return html.replace(ancien, nouveau)


def poser_scenes_courts(src, trad, html):
    m = re.search(r"^(    ru: \[.*\])\n\};\nconst SCENES_ORDRE_COURT", html, re.M)
    if not m:
        raise SystemExit("vignettes : ligne ru de SCENES_COURTS introuvable")
    ligne = "    de: " + json.dumps([trad[e["id"]] for e in src], ensure_ascii=False).replace('", "', '", "')
    return html[:m.end(1)] + ",\n" + ligne + html[m.end(1):]


def poser_page_scenes(src, trad):
    s = lire(PAGE_SCENES)
    d = s.index("const TEXTES = {")
    f = s.index("\n};", d)
    corps = s[d:f]
    for e in src:
        motif = re.compile(r'^(  %s:\s*\{.*?)\}(,?)(\r?)$' % re.escape(e["id"]), re.M)
        m = motif.search(corps)
        if not m:
            raise SystemExit("page-scenes : ligne introuvable pour " + e["id"])
        corps = corps[:m.start()] + m.group(1) + ", de: " + json.dumps(trad[e["id"]], ensure_ascii=False) \
            + "}" + m.group(2) + m.group(3) + corps[m.end():]
    ecrire(PAGE_SCENES, s[:d] + corps + s[f:])
    print("  page-scenes    %d textes" % len(src))


# ---------------------------------------------------------------- JSON

def json_reproduit(chemin):
    brut = lire(chemin)
    d = json.loads(brut)
    for indent in (1, 2):
        def ser(o, indent=indent):
            t = json.dumps(o, ensure_ascii=False, indent=indent) + ("\n" if brut.endswith("\n") else "")
            return t.replace("\n", "\r\n") if "\r\n" in brut else t
        if ser(d) == brut:
            return d, ser
    raise SystemExit(chemin + " : ne se reproduit pas a l'identique, rien n'est ecrit")


def apres(o, cle, de):
    """Copie de o avec « de » insere juste apres « cle »."""
    out = {}
    for k, v in o.items():
        if k == "de":
            continue
        out[k] = v
        if k == cle:
            out["de"] = de
    if "de" not in out:
        out["de"] = de
    return out


def poser_grammaire(src, trad):
    chemin = os.path.join(RACINE, "espanol", "datos", "grammaire.json")
    d, ser = json_reproduit(chemin)
    textes = dict(d["textes"])
    textes["de"] = {e["id"].split("|", 1)[1]: trad[e["id"]] for e in src if e["id"].startswith("textes|")}
    d["textes"] = textes
    par_chemin = {e["id"]: trad[e["id"]] for e in src if e["id"].startswith("fiches/")}
    vus = set()

    def marcher(o, chemin_):
        if isinstance(o, dict):
            if "ar" in o and "fr" in o:
                vus.add(chemin_)
                return apres(o, "ar", par_chemin[chemin_])
            return {k: marcher(v, chemin_ + "/" + k) for k, v in o.items()}
        if isinstance(o, list):
            return [marcher(v, chemin_ + "/" + str(i)) for i, v in enumerate(o)]
        return o
    d["fiches"] = [marcher(f, "fiches/" + f["id"]) for f in d["fiches"]]
    if vus != set(par_chemin):
        raise SystemExit("grammaire : chemins non poses %s" % sorted(set(par_chemin) - vus)[:5])
    ecrire(chemin, ser(d))
    print("  grammaire      %d textes + %d dans les fiches" % (len(textes["de"]), len(vus)))


def poser_objets(nom, src, trad):
    chemin = os.path.join(RACINE, "espanol", "datos", nom + ".json")
    d, ser = json_reproduit(chemin)
    par_chemin = {e["id"]: trad[e["id"]] for e in src}
    vus = set()

    def marcher(o, chemin_):
        if isinstance(o, dict):
            if isinstance(o.get("fr"), str) and "ar" in o:
                vus.add(chemin_)
                return apres(o, "ar", par_chemin[chemin_])
            return {k: (v if k.startswith("_") else marcher(v, chemin_ + "/" + k)) for k, v in o.items()}
        if isinstance(o, list):
            return [marcher(v, chemin_ + "/" + str(i)) for i, v in enumerate(o)]
        return o
    d = marcher(d, "")
    if vus != set(par_chemin):
        raise SystemExit("%s : chemins non poses %s" % (nom, sorted(set(par_chemin) ^ vus)[:5]))
    ecrire(chemin, ser(d))
    print("  %-14s %d textes" % (nom, len(vus)))


def poser_variantes(src, trad):
    chemin = os.path.join(RACINE, "espanol", "datos", "variantes.json")
    d, ser = json_reproduit(chemin)
    for e in src:
        cle, mot = e["id"].split("|", 1)
        d[cle][mot]["remarque"] = apres(d[cle][mot]["remarque"], "ar", trad[e["id"]])
    ecrire(chemin, ser(d))
    print("  variantes      %d" % len(src))


def poser_peintres(src, trad):
    chemin = os.path.join(RACINE, "espanol", "mosaique", "peintres.json")
    d, ser = json_reproduit(chemin)
    for e in src:
        p = d["peintres"][e["id"]]
        d["peintres"][e["id"]] = apres(p, "ar" if "ar" in p else "pt", trad[e["id"]])
    ecrire(chemin, ser(d))
    print("  peintres       %d" % len(src))


def poser_prononciation(src, trad):
    chemin = os.path.join(RACINE, "tests", "prononciation_es.py")
    brut = lire(chemin)
    nl = "\r\n" if "\r\n" in brut else "\n"
    debut, fin = "DE = {" + nl, "# DE-FIN" + nl
    i, j = brut.index(debut) + len(debut), brut.index(fin)
    if brut[i:j].strip():
        raise SystemExit("prononciation : DE n'est pas vide")
    lignes = "".join(' %s: (%s,%s      %s),%s' % (json.dumps(e["id"]), json.dumps(trad[e["id"]][0], ensure_ascii=False),
                                               nl, json.dumps(trad[e["id"]][1], ensure_ascii=False), nl) for e in src)
    ecrire(chemin, brut[:i] + lignes + brut[j:])
    r = subprocess.run([sys.executable, chemin, "--ecrire"], capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip())
    if r.returncode:
        raise SystemExit("prononciation_es.py --ecrire a echoue : " + r.stderr + r.stdout[-1500:])
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
        nl = "\r\n" if "\r\n" in brut else "\n"
        if '"n_de"' in brut or '"titre_de"' in brut or '"alt_de"' in brut:
            raise SystemExit("scenes : %s a deja de l'allemand" % nom)
        # Chaque texte arabe, dans l'ordre du document (l'ordre des cles de
        # json.loads), avec l'id que lui a donne extraire.py : l'allemand se
        # pose juste apres lui. alt et consigne vont en tete du fichier.
        champs = {}
        for e in entrees:
            parties = e["id"].split("|")
            if len(parties) == 2:
                champs[parties[1]] = trad[e["id"]]
        d = json.loads(brut)
        ordre = []   # (cle_ar, texte_ar, traduction allemande)
        vus = set()

        def ajouter(cle_ar, texte_ar, id_):
            if id_ not in trad:
                raise SystemExit("scenes : %s sans traduction (%s)" % (id_, cle_ar))
            vus.add(id_)
            ordre.append((cle_ar, texte_ar, trad[id_]))
        for niv, c in d.get("couches", {}).items():
            for k, v in c.items():
                if k == "titre_ar":
                    ajouter(k, v, "%s|%s|titre" % (nom, niv))
                elif k == "qs":
                    for i, q in enumerate(v):
                        for k2, v2 in q.items():
                            if k2 == "n_ar":
                                ajouter(k2, v2, "%s|%s|%d" % (nom, niv, i))
                            elif k2 == "sens_ar":
                                ajouter(k2, v2, "%s|%s|%d|sens" % (nom, niv, i))
                            elif k2 == "latam" and isinstance(v2, dict) and v2.get("n_ar"):
                                ajouter("n_ar", v2["n_ar"], "%s|%s|%d|latam" % (nom, niv, i))
        attendus = {e["id"] for e in entrees if len(e["id"].split("|")) > 2}
        if vus != attendus:
            raise SystemExit("scenes : %s, ids sans place : %s" % (nom, sorted(attendus ^ vus)[:5]))
        motif = re.compile(r'(^[ \t]*)?"(titre_ar|n_ar|sens_ar)": ("(?:[^"\\]|\\.)*")', re.M)
        morceaux, pos, k = [], 0, 0
        for m in motif.finditer(brut):
            cle, val = m.group(2), json.loads(m.group(3))
            if k >= len(ordre) or ordre[k][:2] != (cle, val):
                raise SystemExit("scenes : %s, ordre inattendu au %d-ieme texte arabe" % (nom, k))
            de = json.dumps(ordre[k][2], ensure_ascii=False)
            cle_de = cle[:-3] + "_de"
            if m.group(1) is not None:
                ajout = ',%s%s"%s": %s' % (nl, m.group(1), cle_de, de)
            else:
                ajout = ', "%s": %s' % (cle_de, de)
            morceaux.append(brut[pos:m.end()] + ajout)
            pos = m.end()
            k += 1
        if k != len(ordre):
            raise SystemExit("scenes : %s, %d texte(s) sans place" % (nom, len(ordre) - k))
        nouveau = "".join(morceaux) + brut[pos:]
        # alt_de et consigne_de : en tete, juste apres l'accolade ouvrante.
        if champs:
            mm = re.match(r'\{(\r?\n)([ \t]*)', nouveau)
            if not mm:
                raise SystemExit("scenes : %s ne commence pas par une accolade sur sa ligne" % nom)
            tete = "".join('"%s_de": %s,%s%s' % (c, json.dumps(champs[c], ensure_ascii=False), mm.group(1), mm.group(2))
                           for c in ("alt", "consigne") if c in champs)
            nouveau = nouveau[:mm.end()] + tete + nouveau[mm.end():]
        json.loads(nouveau)
        ecrire(chemin, nouveau)
        total += k + len(champs)
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
    html = lire(INDEX).replace("\r\n", "\n")   # git (autocrlf) range le fichier en LF
    avant = html
    for nom, f in (("i18n", poser_i18n), ("surcharge-es", poser_i18n_es),("categories", poser_categories),
                   ("mots-outils", poser_mots_outils), ("vignettes", poser_scenes_courts)):
        if nom in lu:
            html = f(lu[nom][0], lu[nom][1], html)
            print("  %-14s pose dans index.html" % nom)
    if html != avant:
        ecrire(INDEX, html)
    if "i18n" in lu:
        relire_i18n(*lu["i18n"])
    for nom, f in (("page-scenes", poser_page_scenes), ("grammaire", poser_grammaire),
                   ("variantes", poser_variantes), ("peintres", poser_peintres),
                   ("prononciation", poser_prononciation), ("scenes", poser_scenes)):
        if nom in lu:
            f(*lu[nom])
    for nom in OBJETS:
        if nom in lu:
            poser_objets(nom, *lu[nom])


if __name__ == "__main__":
    main()
