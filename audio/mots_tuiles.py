# -*- coding: utf-8 -*-
"""Les mots des TUILES de « Construis la phrase » (forme « ordre » de la
seance), en allemand et dans les deux voix espagnoles : inventaire, cout,
generation en porteuse, normalisation, controle.

    python audio/mots_tuiles.py                                 # rapport, trois voix
    python audio/mots_tuiles.py --langue es --niveaux A1 --a-blanc
    python audio/mots_tuiles.py --langue es --niveaux A1 --payer --plafond 30000
    python audio/mots_tuiles.py --langue es --niveaux A1 --normaliser
    python audio/mots_tuiles.py --langue es --niveaux A1 --controler

NE LE 24 OCT. 2026. Jacques : « desayunamos se dit encore avec le son du
cellulaire ». Chaque tuile touchee dit son mot (v904) ; les fichiers de mots
de tuiles (manifest_es.py, source « tuiles », v919) ne couvraient que Premiers
pas et A1 voyage, et l'allemand n'en avait aucun. Accord de Jacques : « je veux
qu'on les fasse tous. Jusqu'a C1 », espagnol et allemand. Mesure espagnole
d'abord dans audio/couverture_tuiles_es.py.

CE QUE LA TUILE DIT (index.html, item.forme === "ordre") : le mot affiche,
ponctuation collee retiree aux deux bouts (^[¿¡«"(]+ et [.,;:!?»")]+$), EN
MINUSCULES EN ESPAGNOL SEULEMENT -- l'allemand garde sa majuscule, qui
distingue « Essen » de « essen ». Le fichier est sha1(ce texte)[:16], comme
partout : c'est la cle que l'app calcule qui fait foi.

LES PHRASES QUI PEUVENT SE REMETTRE EN ORDRE
  - phraseDeCarte() : l'exemple d'une carte de nom, d'adjectif ou de verbe, de
    3 a 11 mots (mots_max du palier le plus large) ;
  - la feuille de conjugaison : la phrase d'un autre temps du verbe, 3 a 10 ;
  - Premiers pas et A1 voyage : leurs phrases.
ET LES INTRUS (intrusOrdre), qui sont aussi des tuiles qu'on touche :
  - un article voisin de la meme famille (den / dem, el / los), avec la
    majuscule du mot qu'il imite en allemand (« Den » en tete) ;
  - une autre forme du present du verbe vise (hast / habe) ;
  - un mot de plus de 2 lettres d'une AUTRE phrase de carte, jusqu'a 12 mots,
    toute ponctuation retiree.

LE NIVEAU D'UN MOT est le plus bas des phrases ou il paraît : les debutants
d'abord. Les mots deja enregistres (vocabulaire, Premiers pas...) ont deja leur
fichier et ne coutent rien.

LA PORTEUSE, TOUJOURS : un mot seul est lu dans la mauvaise langue (« neu » a
la francaise, 3 sept. ; « a pie » a l'anglaise, 23 oct.). « Wort: <mot>. »
pour Aurora (refaire_mots.py), « Palabra. ... <mot> » pour Lolita et Monica
(refaire_es.py : le point puis les points de suspension imposent la pause que
recouper.py sait trouver). Vitesse 0,80, modele v2 -- jamais Flash.

APRES : --normaliser (sonie, original archive dans audio/mp3_original/), puis
--controler (SATURE, CLIC, TRAINE sur les seuls fichiers de ce lot, avec leur
texte), puis python audio/controler_sons.py, puis python audio/deposer.py. Les
noms sont neufs : AUDIO_REVISION n'a pas a bouger.
"""
import argparse, collections, filecmp, hashlib, io, json, os, re, shutil, sys, time

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                       # noqa : cle, reglages, modeles, Aurora
import manifest                      # noqa : l'allemand
import manifest_es                   # noqa : l'espagnol, deux variantes

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
VITESSE = 0.80
LANGUES = {
    # langue : (voix, dossier sous audio/mp3/, porteuse, minuscule)
    "de":    (generer.VOIX, "", "Wort: %s.", False),
    "es":    ("3EsCRTMlRTbsPyDyDm45", "es-es", "Palabra. ... %s", True),    # Lolita
    "latam": ("yR4AeVlfzs6IiKxIH9gQ", "es-419", "Palabra. ... %s", True),  # Monica
}
FAMILLES = {   # FAMILLES_ARTICLES d'index.html
    "de": [["der", "die", "das", "den", "dem", "des"], ["ein", "eine", "einen", "einem", "einer"],
           ["mein", "meine", "meinen", "meinem", "meiner"], ["kein", "keine", "keinen", "keinem", "keiner"]],
    "es": [["el", "la", "los", "las"], ["un", "una", "unos", "unas"], ["mi", "mis"], ["este", "esta", "estos", "estas"]],
}
CARTE_MAX, FEUILLE_MAX, INTRUS_MAX = 11, 10, 12
# UN FICHIER PAR VOIX (24 oct. 2026) : trois voix generees en parallele
# ecrivaient le meme fichier et s'effacaient l'une l'autre.
REFUS = os.path.join(RACINE, "audio", "tuiles_refus_%s.json")
FILTRE = None          # --app : les mots demandes par l'app d'abord


def identifiant(t):
    return hashlib.sha1(t.encode("utf-8")).hexdigest()[:16]


def dit(m, minuscule):
    """Ce que l'app envoie a direAllemand() quand on touche la tuile."""
    d = re.sub(r'^[¿¡«"(]+|[.,;:!?»")]+$', "", m)
    return d.lower() if minuscule else d


def phrases(langue):
    """(texte, niveau, sorte) : sorte = carte, feuille ou parcours."""
    out = []
    if langue == "de":
        for t, niv, genre, src in manifest.recolter():
            if genre != "phrase":
                continue
            if src in ("nomen", "adjektive", "verben.exemple"):
                out.append((t, niv, "carte"))
            elif src in ("verben.perfekt", "verben.praeteritum", "verben.konjunktiv2"):
                out.append((t, niv, "feuille"))
            elif src in ("premiers_pas", "a1_voyage"):
                out.append((t, niv, "parcours"))
    else:
        for t, src, niv in manifest_es.recolter(langue):
            if src in ("noms", "adjetivos.json", "verbos.json"):
                out.append((t, niv, "carte"))
            elif src == "verbos.temps":
                out.append((t, niv, "feuille"))
            elif src in ("premiers_pas", "a1_voyage"):
                out.append((t, niv, "parcours"))
    return out


def presents(langue):
    """formesPresent() de chaque verbe : (forme, niveau)."""
    chemin = "verbe.json" if langue == "de" else os.path.join("espanol", "datos", "verbos.json")
    d = json.load(io.open(os.path.join(RACINE, chemin), encoding="utf-8"))
    for niv, liste in d.items():
        for v in liste:
            p = v.get("praesens")
            if isinstance(p, dict):
                for f in p.values():
                    for x in str(f or "").split():
                        yield x, niv


def mots(langue):
    """{mot dit: niveau le plus bas}."""
    _, _, _, minus = LANGUES[langue]
    rang = lambda n: NIVEAUX.index(n) if n in NIVEAUX else 9
    vus = {}

    def prendre(m, niv):
        if not m or not any(c.isalnum() for c in m):
            return
        if m not in vus or rang(niv) < rang(vus[m]):
            vus[m] = niv

    for t, niv, sorte in phrases(langue):
        n = len(t.split())
        if n < 3 and sorte != "parcours":
            continue
        if n < 2:
            continue
        borne = {"carte": CARTE_MAX, "feuille": FEUILLE_MAX, "parcours": 999}[sorte]
        if n <= borne:
            for m in t.split():
                prendre(dit(m, minus), niv)
        # Les intrus pris dans les autres phrases de carte (phraseDeCarte(it, 12)).
        if sorte == "carte" and n <= INTRUS_MAX:
            for m in t.split():
                propre = re.sub(r"[.,!?;:¿¡]+", "", m)
                if len(propre) > 2:
                    prendre(dit(propre, minus), niv)
    fam = FAMILLES["de" if langue == "de" else "es"]
    for f in fam:
        for a in f:
            prendre(dit(a, minus), "A1")
            if langue == "de":
                prendre(a[0].upper() + a[1:], "A1")
    for f, niv in presents(langue):
        prendre(dit(f, minus), niv)
    return vus


def chemins(langue, ident):
    dossier = LANGUES[langue][1]
    return (os.path.join(RACINE, "audio", "mp3", dossier, ident + ".mp3"),
            os.path.join(RACINE, "audio", "mp3_original", dossier, ident + ".mp3"))


def brut(langue, ident):
    return os.path.join(RACINE, "audio", "bruts_tuiles", langue, ident + ".mp3")


def de_ce_script(langue, niveaux):
    """Les mots dont CE script a fait le fichier (sa prise brute existe). Les
    autres -- vocabulaire, Premiers pas -- ont leur propre chaine : les
    renormaliser empilerait une generation d'encodage (le piege du 9 oct.)."""
    return [m for m, _ in lot(langue, niveaux, tout=True)
            if os.path.exists(brut(langue, identifiant(m)))
            and any(os.path.exists(c) for c in chemins(langue, identifiant(m)))]


def fait(langue, m):
    """Un mot est fait quand il a son fichier servi OU sa coupe archivee (en
    attente de normalisation : on ne la repaie pas)."""
    return any(os.path.exists(c) for c in chemins(langue, identifiant(m)))


def lot(langue, niveaux, tout=False):
    """Les mots de ces niveaux ; sans tout=True, seulement ceux sans fichier."""
    out = []
    for m, niv in mots(langue).items():
        if niv not in niveaux:
            continue
        if FILTRE is not None and not tout and m not in FILTRE:
            continue
        if tout or not os.path.exists(chemins(langue, identifiant(m))[0]):
            out.append((m, niv))
    out.sort(key=lambda x: (NIVEAUX.index(x[1]), x[0].lower()))
    return out


def lire_refus(langue):
    if os.path.exists(REFUS % langue):
        return json.load(io.open(REFUS % langue, encoding="utf-8"))
    return {}


def ecrire_refus(r, langue):
    with io.open(REFUS % langue, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)


def rapport():
    for langue in ("es", "latam", "de"):
        porteuse = LANGUES[langue][2]
        tous = mots(langue)
        print("%-6s %d mots de tuiles distincts" % (langue, len(tous)))
        cumul = 0
        for n in NIVEAUX:
            l = [m for m, niv in tous.items() if niv == n]
            if not l:
                continue
            manque = [m for m in l if not os.path.exists(chemins(langue, identifiant(m))[0])]
            cout = sum(len(porteuse % m) for m in manque)
            cumul += cout
            print("   %-3s %6d mots, %6d sans fichier  ~%7d credits  (cumul %7d)"
                  % (n, len(l), len(manque), cout, cumul))


def payer(langue, niveaux, plafond, max_n, autre_porteuse="", vitesse=VITESSE):
    voix, dossier, porteuse, _ = LANGUES[langue]
    from recouper import recouper, Refus
    refus = lire_refus(langue)
    cle_refus = lambda m: "%s|%s" % (langue, m)
    if autre_porteuse:
        # LA REPRISE DES REFUS : seulement eux, dans une autre porteuse, avec
        # leur propre prise brute (l'ancienne, mal decoupee, ne doit pas servir).
        porteuse = autre_porteuse
        a_faire = [(m, n) for m, n in lot(langue, niveaux, tout=True) if cle_refus(m) in refus]
        for m, _ in a_faire:
            del refus[cle_refus(m)]
    else:
        a_faire = [(m, n) for m, n in lot(langue, niveaux)
                   if cle_refus(m) not in refus and not fait(langue, m)]
    suffixe = "" if not autre_porteuse else "__" + "".join(c if c.isalnum() else "_" for c in autre_porteuse)
    if vitesse != VITESSE:
        suffixe += "__v%d" % round(vitesse * 100)
    if max_n:
        a_faire = a_faire[:max_n]
    cout = sum(len(porteuse % m) for m, _ in a_faire)
    print("%s : %d mots a produire, ~%d credits (plafond %d)" % (langue, len(a_faire), cout, plafond))
    if not a_faire:
        return
    bruts = os.path.join(RACINE, "audio", "bruts_tuiles", langue)
    os.makedirs(bruts, exist_ok=True)
    os.makedirs(os.path.join(RACINE, "audio", "mp3", dossier), exist_ok=True)
    os.makedirs(os.path.join(RACINE, "audio", "mp3_original", dossier), exist_ok=True)
    cle = generer.cle_api()
    modele = generer.MODELES["v2"][0]          # v2 TOUJOURS (Jacques, 12 oct.)
    reglages = dict(generer.REGLAGES, speed=vitesse)
    depense = poses = rates = 0
    debut = time.time()
    try:
        for i, (m, niv) in enumerate(a_faire, 1):
            texte = porteuse % m
            ident = identifiant(m)
            prise = brut(langue, ident)[:-4] + suffixe + ".mp3"
            if not os.path.exists(prise):
                if depense + len(texte) > plafond:
                    print("plafond atteint (%d credits). Relancer reprend la suite." % depense)
                    break
                try:
                    son = appeler(voix, texte, reglages, modele, cle)
                except generer.TexteBloque:
                    refus[cle_refus(m)] = {"mot": m, "niveau": niv, "raison": "refuse par ElevenLabs"}
                    rates += 1
                    continue
                open(prise + ".part", "wb").write(son)
                os.replace(prise + ".part", prise)
                depense += len(texte)
            # LA COUPE VA DANS L'ARCHIVE, JAMAIS DANS audio/mp3/ (24 oct. 2026).
            # audio/mp3/ est le dossier depose : une coupe non normalisee qui
            # y attend partirait en ligne au premier deposer.py d'une autre
            # session, et Hosting la sert « immutable, un an ». --normaliser
            # fait le fichier servi depuis l'archive.
            servi, cible = chemins(langue, ident)
            try:
                recouper(prise, cible + ".part", texte=m)
                os.replace(cible + ".part", cible)
                if autre_porteuse and os.path.exists(servi):
                    os.remove(servi)        # une reprise : l'ancien est a refaire
                poses += 1
            except Refus as err:
                refus[cle_refus(m)] = {"mot": m, "niveau": niv, "raison": str(err)}
                rates += 1
                if os.path.exists(cible + ".part"):
                    os.remove(cible + ".part")
            if i % 100 == 0:
                ecoule = time.time() - debut
                print("  %5d/%d  %7d credits  %d refus  reste ~%d min" % (
                    i, len(a_faire), depense, rates, int((len(a_faire) - i) * ecoule / i / 60)), flush=True)
                ecrire_refus(refus, langue)
    except KeyboardInterrupt:
        print("interrompu -- ce qui est fait est garde.")
    finally:
        ecrire_refus(refus, langue)
    print("%s : %d poses, %d refus, %d credits depenses" % (langue, poses, rates, depense))


def appeler(voix, texte, reglages, modele, cle):
    import urllib.error, urllib.request
    url = "https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=%s" % (voix, generer.FORMAT)
    corps = json.dumps({"text": texte, "model_id": modele, "voice_settings": reglages,
                        "seed": generer.SEED}).encode("utf-8")
    for essai in range(6):
        req = urllib.request.Request(url, data=corps, method="POST", headers={
            "xi-api-key": cle, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:200]
            if e.code in (429, 500, 502, 503, 504) and essai < 5:
                time.sleep(2 ** essai)
                continue
            if e.code == 403 and ("violate" in detail or "blocked" in detail):
                raise generer.TexteBloque(detail)
            # Le quota epuise se dit en 401 « quota_exceeded » : on s'arrete,
            # on ne rate pas mille mots un par un.
            raise RuntimeError("HTTP %d : %s" % (e.code, detail))
        except urllib.error.URLError:
            if essai < 5:
                time.sleep(2 ** essai)
                continue
            raise
    raise RuntimeError("echec apres 6 essais")


def normaliser(langue, niveaux, travailleurs=7):
    """Comme generer_es.normaliser(), restreint aux fichiers de ce lot :
    l'original archive d'abord, puis la sonie. Reprenable."""
    from concurrent.futures import ThreadPoolExecutor
    import normaliser as N
    N.FF = N.ffmpeg()
    os.makedirs(os.path.join(RACINE, "audio", "mp3_original", LANGUES[langue][1]), exist_ok=True)

    def a_faire(m):
        # Trois cas : la coupe archivee sans fichier servi (le circuit
        # normal) ; un fichier servi sans archive ou identique a elle (les
        # lots A1-A2 du 24 oct., ecrits avant ce circuit).
        cible, src = chemins(langue, identifiant(m))
        if not os.path.exists(cible):
            return os.path.exists(src)
        return not os.path.exists(src) or filecmp.cmp(cible, src, shallow=False)

    liste = [m for m in de_ce_script(langue, niveaux) if a_faire(m)]
    print("%s : %d a normaliser" % (langue, len(liste)), flush=True)

    def un(m):
        cible, src = chemins(langue, identifiant(m))
        try:
            if not os.path.exists(src):
                shutil.copy2(cible, src)
            tmp = cible + ".norm.mp3"
            ok = N.normaliser(src, tmp, intermediaire=tmp + ".t1.mp3")
            if ok:
                for essai in range(6):     # OneDrive verrouille parfois un fichier
                    try:
                        os.replace(tmp, cible)
                        return True
                    except PermissionError:
                        time.sleep(1 + essai)
            if os.path.exists(tmp):
                os.remove(tmp)
            return False
        except OSError:
            return False

    with ThreadPoolExecutor(max_workers=travailleurs) as ex:
        res = list(ex.map(un, liste))
    print("%s : %d normalises, %d rates" % (langue, sum(res), len(res) - sum(res)))


def controler(langue, niveaux, sortie=""):
    """Les mesures de controler_sons.py, sur les fichiers de ce lot, avec leur
    texte (TRAINE se juge au nombre de lettres). Les originaux identiques au
    fichier servi n'ont pas ete normalises : signales aussi."""
    from concurrent.futures import ThreadPoolExecutor
    import controler_sons as C
    liste = de_ce_script(langue, niveaux)

    def un(m):
        cible, src = chemins(langue, identifiant(m))
        if not os.path.exists(cible):
            return m, ["NON_NORMALISE"], None
        x = C.mesurer(cible)
        d = ["ILLISIBLE"] if x is None else C.defauts(x, m)
        if not os.path.exists(src) or filecmp.cmp(cible, src, shallow=False):
            d.append("NON_NORMALISE")
        return m, d, x
    with ThreadPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(un, liste))
    nb = collections.Counter(x for _, d, _ in res for x in d)
    graves = [(m, d, x) for m, d, x in res if set(d) & {"SATURE", "CLIC", "TRAINE", "ILLISIBLE", "NON_NORMALISE"}]
    print("%s : %d fichiers controles   %s" % (langue, len(res), "  ".join("%s %d" % kv for kv in sorted(nb.items())) or "rien"))
    for m, d, x in graves[:40]:
        print("   %-22s %-26s %s" % (m, ",".join(d), x))
    if sortie:
        json.dump([{"mot": m, "id": identifiant(m), "defauts": d, "mesure": x} for m, d, x in graves],
                  io.open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return graves


def recopier(niveaux, faire=False):
    """GRATUIT, allemand seulement. L'app garde la casse de la tuile : « Auch »
    en tete de phrase n'a pas de fichier, « auch » en a un (24 oct. 2026 : 243
    mots). Meme son, autre cle : on copie le fichier servi ET son original
    archive sous la cle demandee, sans un credit."""
    faits = 0
    for m, niv in lot("de", niveaux):
        for autre in (m.lower(), m[:1].upper() + m[1:], m[:1].lower() + m[1:]):
            if autre == m:
                continue
            mp3, orig = chemins("de", identifiant(autre))
            if os.path.exists(mp3) and os.path.exists(orig):
                cible, cible_orig = chemins("de", identifiant(m))
                if faire:
                    shutil.copy2(orig, cible_orig)
                    shutil.copy2(mp3, cible)
                faits += 1
                break
    print("de %s : %d mots %s depuis l'autre casse" % (",".join(niveaux), faits, "recopies" if faire else "a recopier"))


def restreindre_a(chemin_json, langue):
    """Les mots que audio/couverture_app.py a vus demandes PAR L'APP (seance.tuile
    et feuille.tuile) : ils passent avant les intrus du present."""
    d = json.load(io.open(chemin_json, encoding="utf-8"))
    r = d[{"de": "de", "es": "es-es", "latam": "es-419"}[langue]]
    return set(r["seance.tuile"]["sans_fichier"]) | set(r["feuille.tuile"]["sans_fichier"])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--langue", choices=sorted(LANGUES))
    p.add_argument("--niveaux", default="A1")
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--payer", action="store_true")
    p.add_argument("--plafond", type=int, default=0, help="credits au plus pour cette execution (obligatoire avec --payer)")
    p.add_argument("--max", type=int, default=0)
    p.add_argument("--normaliser", action="store_true")
    p.add_argument("--controler", action="store_true")
    p.add_argument("--json", default="")
    p.add_argument("--liste", action="store_true")
    p.add_argument("--recopier", action="store_true", help="allemand : copier l'autre casse (gratuit)")
    p.add_argument("--faire", action="store_true", help="avec --recopier : copier pour de bon")
    p.add_argument("--reprendre-refus", default="", metavar="PORTEUSE",
                   help="refaire les refus dans cette porteuse (ex. \"Wort. ... %%s\")")
    p.add_argument("--vitesse", type=float, default=VITESSE)
    p.add_argument("--marquer", default="", metavar="JSON",
                   help="mettre aux refus les mots que --controler --json a signales (pour --reprendre-refus)")
    p.add_argument("--app", default="", help="JSON de couverture_app.py : seulement les mots qu'il liste")
    a = p.parse_args()
    global FILTRE
    if a.app and a.langue:
        FILTRE = restreindre_a(a.app, a.langue)
    if not a.langue:
        rapport()
        return
    niveaux = [n.strip() for n in a.niveaux.split(",")]
    if a.marquer:
        r = lire_refus(a.langue)
        for g in json.load(io.open(a.marquer, encoding="utf-8")):
            r["%s|%s" % (a.langue, g["mot"])] = {"mot": g["mot"], "niveau": "?", "raison": ",".join(g["defauts"])}
        ecrire_refus(r, a.langue)
        print("%s : %d refus" % (a.langue, len(r)))
    elif a.recopier:
        recopier(niveaux, a.faire)
    elif a.payer:
        if a.plafond <= 0:
            sys.exit("--plafond obligatoire : le solde se consulte avant chaque lot.")
        payer(a.langue, niveaux, a.plafond, a.max, a.reprendre_refus, a.vitesse)
    elif a.normaliser:
        normaliser(a.langue, niveaux)
    elif a.controler:
        sys.exit(1 if controler(a.langue, niveaux, a.json) else 0)
    else:
        l = lot(a.langue, niveaux)
        porteuse = LANGUES[a.langue][2]
        print("%s %s : %d mots sans fichier, ~%d credits" % (
            a.langue, ",".join(niveaux), len(l), sum(len(porteuse % m) for m, _ in l)))
        if a.liste:
            for m, n in l:
                print("   %-3s %s" % (n, m))


if __name__ == "__main__":
    main()
