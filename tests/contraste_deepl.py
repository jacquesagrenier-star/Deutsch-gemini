# -*- coding: utf-8 -*-
"""Contraste le turc du corpus avec DeepL, par TRADUCTION INVERSE.

    python tests/contraste_deepl.py --estimer                 # combien ca coute
    python tests/contraste_deepl.py --essai 40                # calibrer d'abord
    python tests/contraste_deepl.py --categories adverbes     # une categorie
    python tests/contraste_deepl.py --rapport                 # relire sans appeler

CE QU'IL FAIT, ET POURQUOI DANS CE SENS-LA.

On prend le TURC du corpus, on le fait retraduire EN ALLEMAND par DeepL, et on
compare avec l'allemand d'origine. La ou ca diverge franchement, il y a un
probleme de sens.

Le sens de la traduction n'est pas un detail. DeepL ne voit jamais l'allemand
d'origine : il ne peut donc pas l'inventer. C'est precisement la faute commise
le 2 septembre, ou un relecteur a signale trois phrases turques comme infideles
EN CITANT des phrases allemandes absentes du corpus, et ou ces trois signalements
ont ete appliques sans verification -- rendant infideles trois traductions qui
etaient justes. Un moteur de traduction ne peut pas commettre cette erreur-la.

CE QU'IL NE FAIT PAS, ET IL FAUT LE REDIRE.

DeepL ne JUGE pas, il traduit. S'il rend « ändern » par « degistirmek » quand la
carte dit « degisiklik yapmak », ca ne prouve rien : les deux sont corrects, il
en a choisi un. Le rapport ne contient donc que les ecarts FRANCS, et il ne
contient pas de verdict -- comme collisions.md, c'est une liste a regarder.

Il ignore aussi tout ce qui a compte dans cette relecture : le niveau CECR, le
registre, et le fait qu'un mot soit deja pris par une autre carte. Ces
questions-la restent pour les relecteurs, et c'est la qu'ils sont bons.

    etape 1a  --suspects      les champs perdus            (relecture_tr.py)
    etape 1b  --collisions    les reponses en double       (relecture_tr.py)
    etape 1c  ce script       les ecarts de SENS           (DeepL)
    etape 2   la relecture croisee : naturel, registre, faux amis

LA CLE D'API. Dans `deepl.secret` a la racine, une ligne, rien d'autre. Le
fichier est deja couvert par `*.secret` dans .gitignore. Une cle gratuite finit
par « :fx » et le script bascule alors tout seul sur api-free.deepl.com.

LE BUDGET, MESURE. Le corpus turc entier fait 345 921 caracteres a envoyer,
repartis ainsi :

    noms         132 536        adverbes      17 262
    verbes       138 132        expressions   27 056
    adjectifs     32 141

Il tient donc dans un seul mois de l'offre API gratuite (500 000 caracteres).
`--estimer` rechiffre avant chaque envoi, `--categories` et `--niveaux`
decoupent si le forfait est plus serre, et surtout TOUT EST MIS EN CACHE : une
phrase deja retraduite n'est jamais repayee. Le cache vit dans
relecture_tr/cache-deepl.json et se garde d'un mois sur l'autre.

LES SEUILS, ET COMMENT ILS ONT ETE FIXES. Pas au jugement : sur des cas connus,
dont les trois phrases rendues infideles le 2 septembre. La premiere version
prenait le meilleur des deux mesures et les laissait passer toutes les trois.
Voir similarite(). Un contraste qui ne rattrape pas les erreurs qu'on sait
avoir commises n'est pas calibre, il est decoratif.
"""
import io
import json
import os
import sys
import time
import unicodedata
import difflib

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import relecture_tr as R                                  # noqa: E402

SORTIE = os.path.join(RACINE, "relecture_tr")
CACHE = os.path.join(SORTIE, "cache-deepl.json")
CLE = os.path.join(RACINE, "deepl.secret")

# Seuils de similarite en dessous desquels on signale. Ils sont volontairement
# BAS : on ne cherche pas la traduction differente, on cherche le contresens.
# A calibrer sur un lot d'essai avant de faire confiance au resultat -- le turc
# n'est pas la paire la plus forte de DeepL.
SEUIL_MOT = 0.45
SEUIL_PHRASE = 0.55

LOT = 50          # DeepL accepte 50 textes par requete


# --------------------------------------------------------------- comparaison

def _plier(t):
    """Minuscules, tremas deplies, ponctuation retiree.

    On compare du SENS, pas de l'orthographe : « Fuer Fragen stehe ich zur
    Verfuegung » et « Für Fragen stehe ich zur Verfügung » sont la meme phrase.
    """
    t = (t or "").lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        t = t.replace(a, b)
    t = "".join(c for c in unicodedata.normalize("NFKD", t)
                if not unicodedata.combining(c))
    return " ".join("".join(c if c.isalnum() else " " for c in t).split())


def similarite(a, b, est_mot):
    """DEUX MESURES, ET PAS LA MEME SELON CE QU'ON COMPARE.

    Sur un MOT, on prend le meilleur des deux : difflib rattrape la
    morphologie (« aendern » contre « ändern » une fois les tremas deplies,
    « Arbeit » dans « Arbeitsplatz »), la ou le recouvrement de mots ne voit
    que deux chaines differentes.

    Sur une PHRASE, on ne garde que le recouvrement de mots, et c'est la
    calibration qui l'a impose. Prendre le maximum laissait passer exactement
    ce qu'on cherche : deux phrases qui partagent leur sujet et dont tout le
    predicat differe. « Mein Betreuer begleitet die Kinder auf dem Ausflug »
    contre « Mein Betreuer gibt mir wertvolles Feedback » sortait a 0,46 par
    les caracteres -- au-dessus du seuil -- alors que le recouvrement de mots
    le met a 0,25. Ces trois phrases-la sont precisement celles qui ont ete
    rendues infideles le 2 septembre : un contraste qui ne les rattrape pas
    ne sert a rien.

    Le recouvrement reste insensible a l'ordre des mots, ce qui est
    indispensable : l'allemand deplace son verbe, et une phrase juste ne doit
    pas etre signalee pour ca.
    """
    a, b = _plier(a), _plier(b)
    if not a or not b:
        return 0.0
    ma, mb = set(a.split()), set(b.split())
    mot = len(ma & mb) / float(max(len(ma), len(mb)))
    if not est_mot:
        return mot
    return max(difflib.SequenceMatcher(None, a, b).ratio(), mot)


# ------------------------------------------------------------------ le corpus

def a_verifier(categories, niveaux):
    """Rend la liste des (carte, champ, texte turc, texte allemand attendu)."""
    out = []
    for nom in categories:
        for c in R.CATEGORIES[nom]():
            if c.get("niveau") not in niveaux:
                continue
            tr, de = (c.get("turc") or "").strip(), (c.get("allemand") or "").strip()
            # L'article ne se traduit pas tout seul : on compare le nom nu.
            for art in ("der ", "die ", "das "):
                if de.startswith(art):
                    de = de[len(art):]
            if tr and de:
                out.append((nom, c, "traduction_tr", tr, de, True))
            phrases = c.get("phrases")
            if phrases:
                for p in phrases:
                    if (p.get("tr") or "").strip() and (p.get("de") or "").strip():
                        out.append((nom, c, p["champ"] + "_tr",
                                    p["tr"].strip(), p["de"].strip(), False))
            else:
                if (c.get("phrase_tr") or "").strip() and (c.get("phrase_de") or "").strip():
                    out.append((nom, c, "exemple_tr", c["phrase_tr"].strip(),
                                c["phrase_de"].strip(), False))
    return out


# -------------------------------------------------------------------- DeepL

def lire_cle():
    if not os.path.isfile(CLE):
        return None
    return io.open(CLE, encoding="utf-8").read().strip()


def charger_cache():
    if os.path.isfile(CACHE):
        try:
            return json.load(io.open(CACHE, encoding="utf-8"))
        except ValueError:
            pass
    return {}


def ecrire_cache(cache):
    with io.open(CACHE, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cache, f, ensure_ascii=False, indent=0, sort_keys=True)
        f.write("\n")


def traduire(textes, cle):
    """Turc -> allemand, par paquets de 50. Rend une liste de meme longueur."""
    import urllib.request
    import urllib.parse
    hote = "api-free.deepl.com" if cle.endswith(":fx") else "api.deepl.com"
    url = "https://%s/v2/translate" % hote
    out = []
    for i in range(0, len(textes), LOT):
        paquet = textes[i:i + LOT]
        donnees = [("text", t) for t in paquet]
        donnees += [("source_lang", "TR"), ("target_lang", "DE")]
        corps = urllib.parse.urlencode(donnees).encode("utf-8")
        req = urllib.request.Request(url, data=corps, headers={
            "Authorization": "DeepL-Auth-Key " + cle,
            "Content-Type": "application/x-www-form-urlencoded",
        })
        with urllib.request.urlopen(req, timeout=60) as r:
            rep = json.loads(r.read().decode("utf-8"))
        out.extend(t["text"] for t in rep.get("translations", []))
        if i + LOT < len(textes):
            time.sleep(0.4)      # on ne bouscule pas l'API
    return out


# ------------------------------------------------------------------- rapport

def ecrire_rapport(trouvailles, examines, caracteres, depuis_cache):
    chemin = os.path.join(SORTIE, "divergences-deepl.md")
    par_categorie = {}
    for t in trouvailles:
        par_categorie.setdefault(t["categorie"], []).append(t)

    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Ecarts de sens releves par traduction inverse (DeepL)\n\n")
        f.write("Produit par `python tests/contraste_deepl.py`. ")
        f.write("**Aucune correction appliquee.**\n\n")
        f.write("Le turc du corpus a ete retraduit EN ALLEMAND, puis compare a ")
        f.write("l'allemand d'origine. DeepL ne voit jamais cet allemand : il ")
        f.write("ne peut donc pas l'inventer, contrairement a un relecteur.\n\n")
        f.write("**Ce n'est pas une liste d'erreurs.** DeepL traduit, il ne ")
        f.write("juge pas : une reponse differente de la notre est souvent un ")
        f.write("simple synonyme. Seuls les ecarts francs sont ici, et chacun ")
        f.write("demande a etre regarde, pas applique.\n\n")
        f.write("Seuils : %.2f sur un mot, %.2f sur une phrase. "
                % (SEUIL_MOT, SEUIL_PHRASE))
        f.write("%d champs examines, %d signales (%.1f %%). "
                % (examines, len(trouvailles),
                   100.0 * len(trouvailles) / examines if examines else 0))
        f.write("%d caracteres envoyes, %d repris du cache.\n"
                % (caracteres, depuis_cache))
        for nom in sorted(par_categorie):
            lot = sorted(par_categorie[nom], key=lambda t: t["similarite"])
            f.write("\n## %s (%d)\n\n" % (nom, len(lot)))
            for t in lot:
                f.write("- **%s** [%s] — champ `%s` — proximite %.2f\n"
                        % (t["allemand"], t["niveau"], t["champ"], t["similarite"]))
                f.write("  - turc     : %s\n" % t["turc"])
                f.write("  - retour   : %s\n" % t["retour"])
                f.write("  - attendu  : %s\n" % t["attendu"])
    print("  ecrit : relecture_tr/divergences-deepl.md  (%d signalement(s) sur "
          "%d champs)" % (len(trouvailles), examines))


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    args = sys.argv[1:]
    categories = list(R.CATEGORIES)
    niveaux = list(R.NIVEAUX)
    essai = None
    for i, a in enumerate(args):
        if a == "--categories" and i + 1 < len(args):
            categories = [c.strip() for c in args[i + 1].split(",")]
        elif a == "--niveaux" and i + 1 < len(args):
            niveaux = [n.strip().upper() for n in args[i + 1].split(",")]
        elif a == "--essai" and i + 1 < len(args):
            essai = int(args[i + 1])

    inconnues = [c for c in categories if c not in R.CATEGORIES]
    if inconnues:
        print("Categorie inconnue : %s" % ", ".join(inconnues))
        return 1

    travail = a_verifier(categories, niveaux)
    if essai:
        travail = travail[:essai]

    cache = charger_cache()
    manquants = [t[3] for t in travail if t[3] not in cache]
    manquants = list(dict.fromkeys(manquants))          # dedoublonne, ordre garde
    cout = sum(len(t) for t in manquants)

    if "--estimer" in args:
        print("  %d champs a verifier, %d textes absents du cache"
              % (len(travail), len(manquants)))
        print("  %d caracteres a envoyer (l'offre gratuite en donne 500 000/mois)"
              % cout)
        return 0

    if "--rapport" not in args and manquants:
        cle = lire_cle()
        if not cle:
            print("  ! aucune cle dans deepl.secret -- rien n'a ete envoye.")
            print("    Mettre la cle d'API DeepL dans ce fichier, une ligne.")
            return 1
        print("  %d textes a traduire, %d caracteres..." % (len(manquants), cout))
        try:
            rendus = traduire(manquants, cle)
        except Exception as e:
            print("  ! DeepL a refuse : %s" % e)
            print("    Le cache deja constitue est conserve.")
            return 1
        for src, dst in zip(manquants, rendus):
            cache[src] = dst
        ecrire_cache(cache)

    trouvailles = []
    examines = 0
    for nom, c, champ, tr, de, est_mot in travail:
        retour = cache.get(tr)
        if retour is None:
            continue
        examines += 1
        s = similarite(retour, de, est_mot)
        if s < (SEUIL_MOT if est_mot else SEUIL_PHRASE):
            trouvailles.append({
                "categorie": nom, "niveau": c.get("niveau"),
                "allemand": c.get("allemand"), "champ": champ,
                "turc": tr, "retour": retour, "attendu": de,
                "similarite": s,
            })

    ecrire_rapport(trouvailles, examines, cout, len(travail) - len(manquants))
    return 0


if __name__ == "__main__":
    sys.exit(main())
