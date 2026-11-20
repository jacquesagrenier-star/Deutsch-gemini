# -*- coding: utf-8 -*-
"""LA BONNE REPONSE N'EST PAS TOUJOURS LA PREMIERE TUILE (defaut D9 de la revue A a Z, 19 nov. 2026).

Les series a tuiles affichent `options` DANS L'ORDRE DU FICHIER (renderOptionTuiles(), les cartes « gram » de la
seance, le hors ligne). Douze series allemandes et six espagnoles avaient la bonne reponse en premiere tuile a
100 % : on apprenait a toucher la premiere. Le remede retenu par le chef d'orchestre : REORDONNER LES OPTIONS DANS
LES DONNEES, de facon deterministe -- pas de melange a l'affichage, pour que le parcours de reference reste stable.

    python tests/ordre_options.py                 la mesure, serie par serie (aucune ecriture)
    python tests/ordre_options.py --ecrire        reordonne les series desequilibrees des fichiers JSON
    python tests/ordre_options.py --ecrire <f>    un seul fichier

La bonne reponse est designee PAR SON TEXTE (`answers`, `correct`, `correctEn`…), jamais par un indice : deplacer
une option ne demande donc aucune autre mise a jour. Les variantes de langue (`optionsEn`, `optionsTr`…) suivent
la meme permutation.

Deux cas, par serie dont une place depasse SEUIL :
  - toutes les questions offrent LE MEME JEU d'options (als / wenn ; weil / obwohl) : un ORDRE FIXE, celui que le
    fichier emploie le plus -- comme les series ecrites dans la page (ALS_WENN_OPTIONS). La place ne dit alors
    plus rien : elle est le mot. Seulement si les reponses elles-memes sont equilibrees (aucune au-dessus du seuil) ;
  - sinon, une PLACE EQUILIBREE : les places sont distribuees par petits paquets dans l'ordre du fichier (chaque
    place une fois par paquet ; deux fois pour deux options, pour ne pas alterner 0-1-0-1), l'ordre de chaque paquet
    venant d'une empreinte du nom de la serie. Les series se jouent par blocs de dix dans l'ordre du fichier : chaque
    bloc est equilibre, et jamais plus de deux fois de suite la meme place. Les leurres gardent leur ordre relatif.

Une serie deja equilibree n'est pas touchee : relancer le script ne change rien (il est idempotent).

LES DONNEES DERIVEES. L'anglais et le portugais melangent deja par question (random.Random(question)) ; leurs
generateurs appellent equilibrer() avant d'ecrire, pour les petites series ou le hasard penche. Le japonais est
derive sur sa branche : son generateur doit faire de meme (sinon tests/verifier.py le dira).

tests/verifier.py appelle controle() : aucune serie d'au moins MIN_CONTROLE questions ou la bonne reponse tient
la meme place dans plus de SEUIL des questions."""
import collections, hashlib, io, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIERS = ["exercices.json", "espanol/datos/ejercicios.json", "anglais/datos/exercices.json",
            "portugais/datos/exercices.json", "portugais/datos-br/exercices.json", "japonais/datos/exercices.json"]
SEUIL = 0.60
MIN_CONTROLE = 6


def _t(o):
    return str(o).strip().lower()


def _suffixes(ex):
    """Les cles d'options de la question : '' pour `options`, 'En' pour `optionsEn`…"""
    return [k[len("options"):] for k in ex if k.startswith("options") and isinstance(ex[k], list) and ex[k]]


def place(ex, suffixe=""):
    """L'indice de la bonne reponse dans options<suffixe>, ou None."""
    opts = [_t(o) for o in ex.get("options" + suffixe) or []]
    bonnes = [_t(a) for a in (ex.get("answers") or [])]
    for cle in ("correct" + suffixe, "correct"):
        if isinstance(ex.get(cle), str):
            bonnes.append(_t(ex[cle]))
    for i, o in enumerate(opts):
        if o in bonnes:
            return i
    return None


def a_options(ex):
    return isinstance(ex, dict) and isinstance(ex.get("options"), list) and len(ex["options"]) >= 2


def mesure(questions):
    """(part de la place la plus frequente, compteur des places, nombre de questions mesurees)."""
    c = collections.Counter()
    for ex in questions:
        if a_options(ex):
            p = place(ex)
            if p is not None:
                c[p] += 1
    n = sum(c.values())
    return ((max(c.values()) / n) if n else 0.0, c, n)


def _empreinte(*morceaux):
    return int(hashlib.sha1("|".join(str(m) for m in morceaux).encode("utf-8")).hexdigest(), 16)


def _ordre_fixe(questions):
    """L'ordre commun des options si toutes les questions offrent le meme jeu ET que les reponses sont equilibrees."""
    qs = [ex for ex in questions if a_options(ex)]
    jeux = {frozenset(_t(o) for o in ex["options"]) for ex in qs}
    if len(jeux) != 1 or any(len(set(_t(o) for o in ex["options"])) != len(ex["options"]) for ex in qs):
        return None
    ordres = collections.Counter(tuple(_t(o) for o in ex["options"]) for ex in qs)
    # le plus employe ; a egalite, le premier rencontre dans le fichier
    meilleur = max(ordres.values())
    ordre = next(tuple(_t(o) for o in ex["options"]) for ex in qs if ordres[tuple(_t(o) for o in ex["options"])] == meilleur)
    c = collections.Counter()
    for ex in qs:
        p = place(ex)
        if p is None:
            return None
        c[ordre.index(_t(ex["options"][p]))] += 1
    if max(c.values()) / sum(c.values()) > SEUIL:
        return None
    return ordre


def _cibles(nom, questions):
    """La place visee de la bonne reponse, question par question, dans l'ordre du fichier."""
    sacs, tours, derniers, out = {}, collections.Counter(), {}, []
    for ex in questions:
        if not a_options(ex) or place(ex) is None:
            out.append(None); continue
        n = len(ex["options"])
        if not sacs.get(n):
            tours[n] += 1
            base = list(range(n)) * (2 if n == 2 else 1)
            sac = sorted(range(len(base)), key=lambda i: _empreinte(nom, n, tours[n], i))
            sac = [base[i] for i in sac]
            # jamais plus de deux fois de suite la meme place, d'un paquet au suivant
            d = derniers.get(n, [])
            if len(d) >= 2 and d[-1] == d[-2] == sac[0]:
                j = next((k for k, v in enumerate(sac) if v != sac[0]), None)
                if j is not None:
                    sac[0], sac[j] = sac[j], sac[0]
            elif n > 2 and d and d[-1] == sac[0]:
                sac.append(sac.pop(0))
            sacs[n] = sac
        cible = sacs[n].pop(0)
        derniers.setdefault(n, []).append(cible)
        out.append(cible)
    return out


def _deplacer(liste, de, vers):
    reste = [o for i, o in enumerate(liste) if i != de]
    vers = min(vers, len(reste))
    return reste[:vers] + [liste[de]] + reste[vers:]


def _reordonner(ex, cible=None, ordre=None):
    """Pose la bonne reponse a `cible`, ou range les options selon `ordre`. Rend True si quelque chose a bouge."""
    bouge = False
    p0 = place(ex)
    for suf in _suffixes(ex):
        cle = "options" + suf
        avant = ex[cle]
        p = place(ex, suf)
        if ordre is not None:
            textes = [_t(o) for o in avant]
            if sorted(textes) == sorted(ordre):
                apres = sorted(avant, key=lambda o: ordre.index(_t(o)))
            elif len(avant) == len(ordre) and p == p0:
                # des options traduites, alignees sur `options` : la meme permutation
                perm = sorted(range(len(ordre)), key=lambda i: ordre.index(_t(ex["options"][i])))
                apres = [avant[i] for i in perm]
            elif p is not None:
                apres = _deplacer(avant, p, ordre.index(_t(ex["options"][p0])))
            else:
                continue
        else:
            if p is None:
                continue
            apres = _deplacer(avant, p, cible)
        if apres != avant:
            ex[cle] = apres
            bouge = True
    return bouge


def equilibrer(jeux, forcer=False):
    """Reordonne, en place, les series de `jeux` ({nom: [questions]}) dont une place depasse SEUIL.
    Rend [(nom, questions reordonnees, 'fixe' | 'equilibre', part avant, part apres)]."""
    faits = []
    for nom, questions in jeux.items():
        if not isinstance(questions, list):
            continue
        avant, _, n = mesure(questions)
        if n < 2 or (avant <= SEUIL and not forcer):
            continue
        ordre = _ordre_fixe(questions)
        cibles = None if ordre else _cibles(nom, questions)
        k = 0
        for i, ex in enumerate(questions):
            if not a_options(ex) or place(ex) is None:
                continue
            if _reordonner(ex, cible=None if ordre else cibles[i], ordre=ordre):
                k += 1
        apres, _, _ = mesure(questions)
        faits.append((nom, k, "fixe" if ordre else "equilibre", avant, apres))
    return faits


def controle(jeux, fichier=""):
    """Les series (d'au moins MIN_CONTROLE questions a options) ou une place depasse SEUIL : [message]."""
    pbs = []
    for nom, questions in jeux.items():
        if not isinstance(questions, list):
            continue
        part, c, n = mesure(questions)
        if n >= MIN_CONTROLE and part > SEUIL:
            top = c.most_common(1)[0][0]
            pbs.append("%s : %s : la bonne reponse est la tuile %d dans %d %% des %d questions -- python tests/ordre_options.py --ecrire"
                       % (fichier, nom, top + 1, round(100 * part), n))
    return pbs


def _lire(chemin):
    brut = io.open(chemin, "rb").read()
    texte = brut.decode("utf-8")
    return texte, json.loads(texte)


def _rendre(donnees, modele):
    """Le meme format que `modele` (le texte d'origine) : compact ou indente d'un cran, fin de ligne, CRLF."""
    compact = modele.lstrip().startswith('{"')
    s = json.dumps(donnees, ensure_ascii=False, separators=(",", ":")) if compact else json.dumps(donnees, ensure_ascii=False, indent=1)
    if modele.endswith("\n"):
        s += "\n"
    if "\r\n" in modele:
        s = s.replace("\n", "\r\n")
    return s


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ecrire = "--ecrire" in sys.argv
    fichiers = args or FICHIERS
    total_s = total_q = 0
    for f in fichiers:
        chemin = os.path.join(RACINE, f)
        if not os.path.exists(chemin):
            print("%s : absent" % f); continue
        texte, d = _lire(chemin)
        jeux = d.get("jeux") or {}
        ns = sum(1 for q in jeux.values() if isinstance(q, list) and mesure(q)[2])
        nq = sum(mesure(q)[2] for q in jeux.values() if isinstance(q, list))
        if not ecrire:
            pbs = [(nom, mesure(q)) for nom, q in jeux.items() if isinstance(q, list)]
            hauts = [(m[0], nom, m[1], m[2]) for nom, m in pbs if m[2] >= 2 and m[0] > SEUIL]
            print("%s : %d series a tuiles, %d questions ; %d serie(s) au-dessus de %d %%" % (f, ns, nq, len(hauts), round(100 * SEUIL)))
            for part, nom, c, n in sorted(hauts, reverse=True):
                print("   %3.0f %%  %-44s %4d questions, places %s" % (100 * part, nom, n, dict(sorted(c.items()))))
            continue
        if _rendre(d, texte) != texte:
            print("%s : le format du fichier n'est pas reconnu, RIEN N'EST ECRIT" % f); continue
        faits = equilibrer(jeux)
        if not faits:
            print("%s : rien a reordonner" % f); continue
        io.open(chemin, "w", encoding="utf-8", newline="").write(_rendre(d, texte))
        print("%s : %d serie(s), %d question(s) reordonnees" % (f, len(faits), sum(x[1] for x in faits)))
        for nom, k, sorte, avant, apres in faits:
            print("   %-44s %4d questions  %-9s  %3.0f %% -> %3.0f %%" % (nom, k, sorte, 100 * avant, 100 * apres))
        total_s += len(faits); total_q += sum(x[1] for x in faits)
    if ecrire:
        print("TOTAL : %d serie(s), %d question(s) reordonnees" % (total_s, total_q))


if __name__ == "__main__":
    main()
