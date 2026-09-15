# -*- coding: utf-8 -*-
"""Classe nos entrees par frequence d'usage, a partir des listes de Leipzig.

    python tests/frequence.py            -- le rapport, sans rien ecrire
    python tests/frequence.py --ecrire   -- ecrit frequence.json

D'OU VIENNENT LES DONNEES, ET CE QUE LA LICENCE OBLIGE
    Leipzig Corpora Collection (Universitat Leipzig), sous CC BY : usage
    commercial permis, PAS de partage a l'identique -- moins contraignant que
    le CC BY-SA de WikDict, que le depot porte deja. L'attribution est
    obligatoire et va au meme endroit que celle de WikDict.

        (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI

    Deux corpus, volontairement :
        deu_mixed-typical_2011  le melange equilibre -- registre proche de
                                celui qu'un apprenant rencontre
        deu_news_2023           la presse recente -- vocabulaire d'aujourd'hui
    Chacun est ramene a une frequence PAR MILLION avant d'etre additionne,
    sinon le plus gros corpus deciderait seul.

    Et un troisieme, d'une AUTRE NATURE (v606) :
        deu_opensubtitles_2018  les sous-titres de 4 610 films et series --
                                de la langue PARLEE, la ou les deux autres
                                sont de la langue ecrite

    Pourquoi il a fallu l'ajouter : mesure sur nos propres mots A1, les deux
    corpus ecrits servaient « Regierung », « Praesident », « Projekt » et
    « Kunde » AVANT « Wasser » et « Hand ». Ce sont des mots frequents dans un
    journal, pas dans une cuisine -- et la seance du jour promet de rendre
    fonctionnel dans la vie reelle.

    ⚠️ SUBTLEX-DE, LA SOURCE QUE LA RECHERCHE CITE, EST INTERDITE ICI. Sa
    licence (CC BY-NC-SA 4.0, verifiee dans le license.txt de son depot OSF)
    dit « noncommercial purposes only ». Wortando est une entreprise. Les
    sous-titres OPUS OpenSubtitles 2018 ne portent pas cette clause ; ils
    demandent l'attribution, qui vit dans la carte « Credits » a cote de
    WikDict et de Leipzig. Ne pas remplacer l'un par l'autre « parce que la
    litterature prefere SUBTLEX » : c'est la licence qui tranche, pas la
    qualite.

    Les archives vivent HORS DU DEPOT (C:/Users/jacqu/.wortando/frequence) :
    100 Mo de donnees brutes n'ont rien a faire dans un depot public, et seul
    le classement derive est versionne.

⚠️ LE PIEGE QUE CE SCRIPT CONTOURNE
    Ces listes comptent des FORMES, pas des lemmes. La frequence de « gehen »
    est portee par « geht », « ging », « gegangen » -- l'infinitif lui-meme est
    rare. Un appariement naif ferait donc descendre tous les verbes et tous les
    adjectifs, et monter tous les noms.

    Deux protections, et la seconde suffirait a elle seule :

    1. On additionne les formes qu'on POSSEDE DEJA : les six personnes du
       present pour un verbe, le pluriel pour un nom, les cinq desinences
       regulieres pour un adjectif. Aucun lemmatiseur, aucune dependance.
    2. ON NE CLASSE QU'A L'INTERIEUR D'UNE CATEGORIE. Un bloc melange les types
       selon une composition fixe (tant de noms, tant de verbes), donc on n'a
       jamais besoin de comparer un verbe a un nom. Le biais restant est
       constant dans une categorie : il s'annule au classement.

⚠️ CE QUI N'EST PAS CLASSABLE
    Les expressions (« Wie geht's ? ») sont des suites de mots : aucune liste
    de frequence ne les contient. Elles sortent du classement et le rapport le
    dit, plutot que de leur donner un rang invente.
"""
import argparse
import io
import json
import os
import re
import sys
import tarfile

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = "C:/Users/jacqu/.wortando/frequence"
CORPUS = ["deu_mixed-typical_2011_300K", "deu_news_2023_300K",
          "deu_opensubtitles_2018"]

# ⚠️ LES CORPUS ECRITS EN MINUSCULES, ET CE QU'ILS CASSENT EN SILENCE.
#
# La liste de sous-titres est integralement repliee en minuscules : « mann »
# y figure, « Mann » non. Or l'allemand met une majuscule a tous ses noms, et
# on additionne CLE PAR CLE. Sans traitement, ce corpus n'apporte donc RIEN
# aux noms -- et le melange retombe silencieusement sur la presse ecrite,
# qu'on venait justement de corriger. Le defaut ne se voit pas : aucun compte
# ne bouge, seul l'ordre des noms reste celui d'avant.
#
# On credite donc en plus chaque cle capitalisee connue des autres corpus de
# la masse rangee sous sa forme repliee.
#
# ⚠️ CE QUE CE REPLI COUTE, MESURE ET NON ESTIME : il fond un nom et son
# homographe minuscule. 13 de nos 462 noms A1 sont dans ce cas -- Arm, Bar,
# Essen, Fest, Gruen, Husten, Laden, Leben, Mal, Morgen, Null, Orange, Weg.
# Pour la plupart le sens est voisin (« das Essen » / « essen »), et la masse
# case-correcte des deux corpus Leipzig vient contrebalancer. Les deux
# vraiment discutables sont « Weg » et « Mal ». C'est une limite connue, pas
# un defaut a corriger a la main : le jour ou une liste de sous-titres
# conservant la casse existera, elle remplacera celle-ci.
MINUSCULES = {"deu_opensubtitles_2018"}
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
# Les desinences de la declinaison faible et forte. « gut » -> gute, guten,
# gutes, guter, gutem. On ne genere pas le comparatif : « besser » n'est pas
# une forme de « gut » au sens ou une liste de frequence l'entendrait.
DESINENCES = ["e", "en", "es", "er", "em"]


def charger_frequences():
    """forme -> frequence par million, additionnee sur les corpus.

    Les corpus qui conservent la casse passent EN PREMIER : c'est leur jeu de
    cles capitalisees qui sert ensuite a recuperer la masse des corpus replies
    en minuscules. Voir MINUSCULES.
    """
    freq = {}
    for nom in sorted(CORPUS, key=lambda n: n in MINUSCULES):
        chemin = os.path.join(SOURCE, nom, nom + "-words.txt")
        if not os.path.exists(chemin):
            arch = os.path.join(SOURCE, nom + ".tar.gz")
            if not os.path.exists(arch):
                sys.exit("  Corpus absent : %s\n  Le telecharger depuis "
                         "https://downloads.wortschatz-leipzig.de/corpora/%s.tar.gz"
                         % (arch, nom))
            with tarfile.open(arch) as t:
                t.extract("%s/%s-words.txt" % (nom, nom), SOURCE)
        brut, total = {}, 0
        with io.open(chemin, encoding="utf-8") as f:
            for ligne in f:
                p = ligne.rstrip("\n").split("\t")
                if len(p) < 3:
                    continue
                try:
                    n = int(p[2])
                except ValueError:
                    continue
                brut[p[1]] = brut.get(p[1], 0) + n
                total += n
        if not total:
            sys.exit("  Corpus vide : " + chemin)
        if nom in MINUSCULES:
            # La masse repliee revient aussi aux cles capitalisees deja
            # connues : sans cette boucle, ce corpus ne dirait rien des noms.
            rendus = 0
            for cle in list(freq):
                if cle[:1].isupper():
                    n = brut.get(cle.lower())
                    if n:
                        freq[cle] += n * 1e6 / total
                        rendus += 1
            print("  %-28s %7d formes, %9d occurrences  (minuscules : %d "
                  "cles capitalisees creditees)" % (nom, len(brut), total, rendus))
        else:
            print("  %-28s %7d formes, %9d occurrences" % (nom, len(brut), total))
        for mot, n in brut.items():
            freq[mot] = freq.get(mot, 0.0) + n * 1e6 / total
    return freq


# ============ LE NOYAU : CE QUI REND FONCTIONNEL, ET QU'ON N'INVENTE PAS ============
#
# La frequence dit ce qui revient souvent. Elle ne dit pas ce dont une personne
# a BESOIN en arrivant. Les deux ne coincident pas : sur nos 860 mots A1, la
# frequence seule servait « Euro », « Mensch », « Uhr », « Seite » et « Spiel »
# avant « Wasser », « Familie », « Hilfe » et « Schule ».
#
# La liste officielle du niveau tranche ca, et elle existe : le Goethe-Institut
# publie une Wortliste pour A1, A2 et B1, batie sur une analyse de BESOINS --
# ce qu'il faut pour se debrouiller -- et non sur un corpus. On ne construit
# donc aucun « noyau maison » : on lit le leur.
#
# ⚠️ AU-DELA DE B1, IL N'Y A PAS DE NOYAU, ET IL NE FAUT PAS EN FABRIQUER UN.
# Le Goethe-Institut ne publie pas de Wortliste pour B2 ni C1 : a ce niveau le
# vocabulaire est considere comme ouvert. Les entrees de ces niveaux recoivent
# donc toutes le meme palier, ce qui revient a les classer par la frequence
# seule -- exactement comme avant. C'est une absence de donnee, pas un oubli.
#
# ⚠️ CES LISTES NE SONT PAS DANS LE DEPOT (examens/ est gitignore : on ne
# redistribue pas des documents du Goethe-Institut, et le depot est public).
# Sans elles le script ne s'arrete pas : il classe par la frequence seule et
# le dit. Un fichier annexe manquant ne doit jamais casser un classement.
NOYAUX = {
    "A1": ["goethe_a1"],
    "A2": ["goethe_a1", "goethe_a2"],
    "B1": ["goethe_a1", "goethe_a2", "goethe_b1", "dtz"],
}


def charger_noyaux():
    """niveau -> ensemble des mots-vedettes officiels, en minuscules."""
    cache, out = {}, {}
    for niveau, listes in NOYAUX.items():
        mots = set()
        for nom in listes:
            if nom not in cache:
                chemin = os.path.join(RACINE, "examens", nom + ".json")
                cache[nom] = set()
                if os.path.isfile(chemin):
                    d = json.load(io.open(chemin, encoding="utf-8"))
                    cache[nom] = {m.strip().lower() for m in d.get("mots", [])}
            mots |= cache[nom]
        if mots:
            out[niveau] = mots
    return out


def dans_noyau(mot, noyau):
    """Le palier ne DEMOTE que ce que la liste sait juger : un mot unique.

    ⚠️ UNE LOCUTION N'EST JAMAIS REPOUSSEE, ET C'EST LE MEME PIEGE QUE f = 0.

    La Wortliste A1 contient bien ses Redewendungen -- « Auf Wiedersehen »,
    « Guten Appetit » -- mais notre extraction n'en garde que les MOTS-VEDETTES
    isoles : une phrase n'y survit pas comme phrase. Une premiere version
    exigeait donc que tous les mots de la locution figurent dans la liste, et
    le resultat etait absurde : « Wie bitte ? » sortait du noyau parce que la
    liste ne contient pas le jeton « bitte? », « Ich bin dabei » parce qu'elle
    porte « sein » et non « bin », « Macht nichts » parce qu'elle porte
    « machen » et non « macht ».

    On aurait pu bricoler un lemmatiseur. Mais punir une locution pour une
    limite de NOTRE extraction, c'est exactement la faute que le plancher
    repare ailleurs : prendre une absence de mesure pour un verdict. Une suite
    de mots garde donc le palier du noyau, et c'est son plancher de frequence
    qui la classe.
    """
    m = (mot or "").strip().strip("?!.,;:").lower()
    if " " in m:
        return True
    return m in noyau


def eclater(f):
    """Les variantes d'une entree telle que nos fichiers l'ecrivent.

    Plusieurs entrees portent une PAIRE separee par une barre oblique --
    « ehrlich/unehrlich », « fern/nah », « bloß / nur ». Cherchees telles
    quelles, elles etaient muettes alors que leurs deux membres sont courants.
    Une barre oblique n'apparait jamais dans une forme allemande : la couper
    est sans risque.
    """
    f = (f or "").strip()
    if not f:
        return []
    if "/" in f:
        return [p.strip() for p in f.split("/") if p.strip()]
    return [f]


def somme(freq, formes):
    """La frequence cumulee des formes trouvees, et combien ont ete trouvees."""
    total, vues, trouvees = 0.0, set(), 0
    for brut in formes:
        for f in eclater(brut):
            if f in vues:
                continue
            vues.add(f)
            v = freq.get(f)
            if v:
                total += v
                trouvees += 1
    return total, trouvees


def note_nom(freq, o):
    s, n = somme(freq, [o.get("mot"), o.get("pluriel")])
    return s, n, False


PRONOMS = {"mich", "dich", "sich", "uns", "euch"}


def formes_verbales(o):
    """Toutes les formes d'un verbe qui tiennent en UN SEUL mot.

    ⚠️ Deux familles cassaient l'appariement, et pour deux raisons opposees.

    LES PRONOMINAUX. « sich erinnern » s'ecrit en deux mots -- infinitif comme
    present (« erinnere mich »). Aucune forme ne pouvait donc etre trouvee. Le
    verbe lui-meme, « erinnern », est parfaitement courant : il suffit de
    retirer le pronom.

    LES SEPARABLES. « anrufen » se dit « rufe an » : deux mots la aussi, mais
    ici on ne PEUT pas retirer la particule -- « rufe » donnerait la frequence
    de « rufen », un autre verbe. La forme d'un seul mot qui existe vraiment
    est le PARTICIPE, « angerufen », qu'on va chercher dans la phrase d'exemple
    du parfait. Sans ca, le rang median des separables etait 1017 contre 436
    pour les autres, et « anrufen » -- verbe d'A1 -- tombait au rang 806.
    """
    brutes = [o.get("infinitif")]
    p = o.get("praesens")
    if isinstance(p, dict):
        brutes.extend(p.values())

    out, separable = [], False
    for f in brutes:
        mots = (f or "").strip().split()
        if len(mots) > 1 and mots[0] == "sich":
            mots = mots[1:]
        if len(mots) > 1 and mots[-1] in PRONOMS:
            mots = mots[:-1]
        if len(mots) == 1:
            out.append(mots[0])
        elif len(mots) == 2:
            separable = True

    if separable:
        # La particule est le dernier mot du present, le participe le seul
        # mot de la phrase du parfait qui commence par elle ET porte un « ge ».
        p1 = ((p or {}).get("ich") or "").split()
        part = p1[-1] if len(p1) > 1 and p1[-1] not in PRONOMS else ""
        if part:
            for mot in re.findall(r"\w+", o.get("perfekt") or "", re.UNICODE):
                b = mot.lower()
                if b.startswith(part) and "ge" in b[len(part):]:
                    out.append(mot)
    return out


def est_separable(o):
    m = ((o.get("praesens") or {}).get("ich") or "").split()
    return len(m) > 1 and m[-1] not in PRONOMS


def note_verbe(freq, o):
    # L'infinitif ET les six personnes du present. C'est ce qui remet les
    # verbes a leur place : « sein » comme forme est rare, « ist » ne l'est pas.
    s, n = somme(freq, formes_verbales(o))
    return s, n, False


def mediane(v):
    v = sorted(v)
    return v[len(v) // 2] if v else 0


def corriger_familles(lignes):
    """Fond deux sous-groupes mesures a des echelles differentes.

    Le participe ne rattrape qu'une partie du retard des verbes separables :
    il couvre le parfait, alors que l'usage courant est au present, ou le
    verbe est coupe en deux (« rufe ... an ») et donc introuvable dans une
    liste de formes. Apres correction le rang median restait 873 pour les
    separables contre 554 pour les autres -- « anrufen », verbe d'A1, au rang
    629.

    ⚠️ C'est exactement le probleme des categories, un cran plus bas : deux
    populations dont la MESURE, non la langue, differe d'un facteur a peu pres
    constant. Et la solution est la meme -- ne comparer que ce qui est
    comparable. On classe chaque famille contre elle-meme, puis on fond les
    deux listes par PERCENTILE. Le 10e percentile des separables se retrouve
    au niveau du 10e percentile des autres, ce qui est vrai par construction
    et n'invente aucune frequence.

    ⚠️ UNE PREMIERE VERSION FONDAIT LES DEUX LISTES PAR PERCENTILE, ET C'ETAIT
    FAUX. Les rangs medians devenaient parfaits (657 contre 656) mais la tete
    du classement devenait absurde : « annehmen » et « anbieten » passaient
    devant « haben » et « koennen ». Fondre par percentile suppose deux
    distributions de MEME FORME ; or le sommet de la frequence allemande est
    tenu par des auxiliaires et des modaux, et aucun verbe separable n'en
    approche. Le percentile corrigeait le milieu en cassant les extremes.

    D'ou un simple FACTEUR MULTIPLICATIF, qui est le modele qu'on vient de
    decrire : ce qui manque a un separable, c'est la masse du present, une
    proportion a peu pres constante de son usage. On l'estime par le rapport
    des medianes, on multiplie, et on classe tout ensemble. La forme de la
    distribution est preservee -- le sommet reste le sommet.

    Renvoie (avant, apres, facteur) pour que le rapport montre le resultat au
    lieu de l'affirmer.
    """
    if not lignes:
        return None
    rang = {id(l): i for i, l in enumerate(sorted(lignes, key=lambda l: -l[2]))}
    avant = (mediane([rang[id(l)] for l in lignes if l[5] == "sep"]),
             mediane([rang[id(l)] for l in lignes if l[5] != "sep"]))
    m_sep = mediane([l[2] for l in lignes if l[5] == "sep" and l[3]])
    m_autre = mediane([l[2] for l in lignes if l[5] != "sep" and l[3]])
    if not m_sep or not m_autre:
        return None
    facteur = m_autre / m_sep
    for l in lignes:
        l[6] = l[2] * facteur if l[5] == "sep" else l[2]
    rang = {id(l): i for i, l in enumerate(sorted(lignes, key=lambda l: -l[6]))}
    apres = (mediane([rang[id(l)] for l in lignes if l[5] == "sep"]),
             mediane([rang[id(l)] for l in lignes if l[5] != "sep"]))
    return (avant, apres, facteur)


def note_simple(freq, o):
    s, n = somme(freq, [(o.get("mot") or "").strip()])
    return s, n, False


# ⚠️ L'ADJECTIF EST LE CAS DIFFICILE, ET IL A FALLU MESURER POUR TRANCHER.
#
#   Compter la forme NUE hisse « zu » au premier rang des adjectifs -- la
#   frequence est celle de la preposition et de la particule, pas celle de
#   « zu » au sens de « ferme ». Meme chose pour « rund » et « weiter ».
#
#   Ne compter que les formes DECLINEES corrige ca (le classement devient neu,
#   gross, weit, deutsch, gut, klein...) mais rend muets 70 adjectifs de plus :
#   les invariables (lila, beige, chic, gratis, fit, extra) n'ont aucune forme
#   declinee, et « hoch » se decline en « hohe », pas en « hoche ».
#
#   D'ou la regle retenue : LES DECLINEES D'ABORD, la forme nue seulement si
#   aucune declinee n'est connue -- et dans ce cas l'entree est SIGNALEE, parce
#   que c'est exactement la ou le classement est fragile.
def note_adjectif(freq, o):
    # eclater() AVANT de decliner : « ehrlich/unehrlich » + « e » donnerait
    # « ehrlich/unehrliche », dont la coupure produirait la forme nue du
    # premier membre -- exactement ce que le repli est cense eviter.
    bases = eclater(o.get("mot"))
    if not bases:
        return 0.0, 0, False
    s, n = somme(freq, [b + d for b in bases for d in DESINENCES])
    if n:
        return s, n, False
    s, n = somme(freq, bases)
    return s, n, bool(n)


def entrees():
    """(categorie, niveau, cle, noteur, objet) pour tout le corpus."""
    out = []
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))
    for t in th["themes"]:
        for m in t.get("mots", []):
            if m.get("mot"):
                out.append(("noms", t.get("niveau"), m["mot"], note_nom, m))
    for fichier, cat, cle, noteur in [
            ("verbe.json", "verbes", "infinitif", note_verbe),
            ("adjectif.json", "adjectifs", "mot", note_adjectif),
            ("adverbe.json", "adverbes", "mot", note_simple),
            ("redewendung.json", "expressions", "mot", note_simple)]:
        chemin = os.path.join(RACINE, fichier)
        if not os.path.exists(chemin):
            continue
        d = json.load(io.open(chemin, encoding="utf-8"))
        for niv in NIVEAUX:
            for o in (d.get(niv) or []) if isinstance(d, dict) else []:
                if o.get(cle):
                    out.append((cat, niv, o[cle], noteur, o))
    # ⚠️ funktionswort.json est range par FAMILLE GRAMMATICALE (konjunktionen,
    # partikeln, praepositionen, zahlen, pronomen, artikelwoerter) et non par
    # niveau CECR. Le parcourir comme les autres le rendait invisible : il
    # n'apparaissait pas du tout dans le rapport, sans erreur.
    #
    # ⚠️ ET LE NIVEAU EXISTE, il est simplement DANS CHAQUE ENTREE. Une premiere
    # version rangeait ces 161 mots sous leur famille au lieu de leur niveau, ce
    # qui a fait croire qu'ils n'avaient pas de niveau du tout -- et failli les
    # faire tous verser en A1, alors que « obwohl », « sodass » et « indem » y
    # sont a juste titre en B1. Le defaut etait dans le lecteur, pas la donnee.
    chemin = os.path.join(RACINE, "funktionswort.json")
    if os.path.exists(chemin):
        d = json.load(io.open(chemin, encoding="utf-8"))
        for famille, liste in (d.items() if isinstance(d, dict) else []):
            if not isinstance(liste, list):
                continue
            for o in liste:
                if o.get("mot"):
                    out.append(("mots-outils", o.get("niveau") or "?",
                                o["mot"], note_simple, o))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true",
                    help="ecrit frequence.json (sinon : rapport seulement)")
    a = ap.parse_args()

    print("\nLES CORPUS")
    freq = charger_frequences()
    print("  %-28s %7d formes distinctes au total\n" % ("reunis", len(freq)))

    noyaux = charger_noyaux()
    if noyaux:
        print("LE NOYAU -- listes officielles du Goethe-Institut")
        for niveau in NIVEAUX:
            if niveau in noyaux:
                print("  %-3s %5d mots-vedettes de reference" % (niveau, len(noyaux[niveau])))
            else:
                print("  %-3s     -- aucune liste publiee : frequence seule" % niveau)
    else:
        print("LE NOYAU -- listes absentes de examens/ : frequence seule "
              "(python tests/listes_examen.py --extraire)")
    print()

    par_cat = {}
    for cat, niv, cle, noteur, o in entrees():
        # La FAMILLE : un sous-groupe dont on sait que la mesure le penalise
        # d'un facteur a peu pres constant. Voir corriger_familles().
        fam = "sep" if (cat == "verbes" and est_separable(o)) else ""
        s, n, r = noteur(freq, o)
        # Le PALIER : 0 dans le noyau officiel du niveau, 1 en dehors. Sans
        # liste pour ce niveau, tout le monde a le meme palier et il ne
        # departage rien.
        ref = noyaux.get(niv)
        palier = 0 if (not ref or dans_noyau(cle, ref)) else 1
        # (mot, niveau, frequence, formes trouvees, repli, famille, cle de tri,
        #  palier)
        par_cat.setdefault(cat, []).append([cle, niv, s, n, r, fam, s, palier])
    ecart = corriger_familles(par_cat.get("verbes") or [])

    # ⚠️ LE PLANCHER DES SUITES DE MOTS, ET POURQUOI f = 0 ETAIT UN MENSONGE.
    #
    # « Es tut mir leid », « Die Rechnung, bitte », « Guten Abend » ne sont
    # dans AUCUNE liste de frequence : ces listes comptent des mots isoles.
    # Elles sortaient donc a 0, c'est-a-dire dernieres de leur categorie --
    # alors que ce sont exactement les phrases qui rendent capable de se
    # debrouiller en trois jours.
    #
    # 0 voulait dire « absent de la liste », et le classement le lisait
    # « rarissime ». On remplace par le mot le PLUS RARE de la suite : c'est
    # lui qui rend la locution difficile, et c'est une mesure, pas un rang
    # invente. Une entree d'un seul mot vraiment absente garde 0 -- son
    # plancher est sa propre valeur.
    for lignes in par_cat.values():
        for l in lignes:
            if l[3]:
                continue
            jetons = [t.strip(".,!?;:").lower() for t in (l[0] or "").split()]
            vals = [freq.get(j) or freq.get(j.capitalize()) or 0.0
                    for j in jetons if j]
            l[6] = min(vals) if vals else 0.0

    print("LA COUVERTURE -- combien de nos mots la liste connait")
    print("  %-13s %6s %9s %9s %8s %s"
          % ("", "total", "trouves", "muets", "%", "replis"))
    print("  " + "-" * 60)
    resultat, muets_par_cat, replis_par_cat = {}, {}, {}
    for cat in ["noms", "verbes", "adjectifs", "adverbes", "mots-outils",
                "expressions"]:
        lignes = par_cat.get(cat)
        if not lignes:
            continue
        muets = [l[0] for l in lignes if l[3] == 0]
        replis = sorted([(l[2], l[0]) for l in lignes if l[4]], reverse=True)
        pct = 100.0 * (len(lignes) - len(muets)) / len(lignes)
        print("  %-13s %6d %9d %9d %7.1f%% %6d"
              % (cat, len(lignes), len(lignes) - len(muets), len(muets), pct,
                 len(replis)))
        muets_par_cat[cat] = muets
        replis_par_cat[cat] = replis
        # LE CLASSEMENT SE FAIT EN DEUX TEMPS (v606) : le PALIER d'abord, la
        # frequence ensuite. Un mot du noyau officiel passe devant un mot hors
        # noyau, meme plus frequent -- c'est tout l'objet du palier : ce qui
        # sert a se debrouiller vient avant ce qui revient souvent.
        #
        # A palier egal, la plus frequente d'abord. Tri sur la CLE l[6] : la
        # frequence pour la plupart des categories, le percentile de famille
        # pour les verbes (voir corriger_familles), le plancher pour les
        # suites de mots. A note egale, l'alphabet -- un ordre arbitraire
        # ASSUME vaut mieux qu'un ordre arbitraire qui se prend pour un
        # classement.
        rangs = []
        for l in sorted(lignes, key=lambda l: (l[7], -l[6], l[0])):
            e = {"m": l[0], "n": l[1], "f": round(l[2], 2)}
            if l[4]:
                e["approx"] = 1   # note obtenue sur la forme nue : fragile
            rangs.append(e)
        resultat[cat] = rangs

    print()
    for cat in ["noms", "verbes", "adjectifs", "adverbes", "mots-outils"]:
        if cat in resultat:
            print("  %-12s tete : %s" % (
                cat, ", ".join(x["m"] for x in resultat[cat][:12])))
    if ecart:
        print("\n  LES VERBES SEPARABLES -- rang median, separables / autres")
        print("     avant correction : %4d / %4d" % ecart[0])
        print("     apres correction : %4d / %4d   (facteur x%.2f)"
              % (ecart[1] + (ecart[2],)))

    print("\n  LES MUETS -- absents de la liste, ranges en queue")
    for cat, muets in muets_par_cat.items():
        if muets:
            print("  %-13s %4d, dont : %s"
                  % (cat, len(muets), ", ".join(sorted(muets)[:7])))
    replis_adj = replis_par_cat.get("adjectifs") or []
    if replis_adj:
        print("\n  LES REPLIS -- notes sur la forme nue faute de declinaison "
              "connue,\n  donc les plus exposes a l'homographie. Les plus hauts "
              "d'abord :")
        print("  " + ", ".join("%s (%.0f)" % (c, s) for s, c in replis_adj[:12]))

    if not a.ecrire:
        print("\n  (rapport seulement -- relancer avec --ecrire pour produire "
              "frequence.json)")
        return

    dest = os.path.join(RACINE, "frequence.json")
    val = {
        "_source": "Leipzig Corpora Collection (CC BY) -- "
                   "(c) Universitat Leipzig / Sachsische Akademie der "
                   "Wissenschaften / InfAI ; OPUS OpenSubtitles 2018 "
                   "(Lison & Tiedemann 2016), d'apres opensubtitles.org",
        "_corpus": CORPUS,
        "_note": "ORDRE = palier puis frequence. Palier : les mots de la "
                 "Wortliste officielle du niveau (Goethe A1/A2/B1) passent "
                 "devant les autres ; B2 et C1 n'ont pas de liste publiee, "
                 "donc pas de palier. Classement PAR CATEGORIE, jamais entre "
                 "categories : les listes comptent des formes et non des "
                 "lemmes, ce qui penalise verbes et adjectifs face aux noms. "
                 "f = frequence par million cumulee sur les formes connues ; "
                 "f = 0 veut dire ABSENT des listes, pas rare -- les suites "
                 "de mots sont classees au plancher de leur mot le plus rare.",
        "categories": resultat
    }
    # COMPACT, et une ligne par categorie. Indente, le meme contenu pesait
    # 490 ko contre 250 : l'app charge ses donnees depuis GitHub a chaque
    # ouverture, et ce fichier est derive -- la source lisible, c'est ce
    # script. Une ligne par categorie garde tout de meme le diff lisible
    # quand un mot change de rang.
    parts = []
    for cle, v in val.items():
        if cle != "categories":
            parts.append(" %s: %s" % (json.dumps(cle), json.dumps(v, ensure_ascii=False)))
    cats = [" %s: %s" % (json.dumps(k), json.dumps(v, ensure_ascii=False,
                                                   separators=(",", ":")))
            for k, v in val["categories"].items()]
    io.open(dest, "w", encoding="utf-8", newline="").write(
        "{\n" + ",\n".join(parts) + ',\n "categories": {\n'
        + ",\n".join(cats) + "\n }\n}\n")
    print("\n  ecrit : frequence.json  (%d ko, %d entrees)"
          % (os.path.getsize(dest) // 1024,
             sum(len(v) for v in val["categories"].values())))


if __name__ == "__main__":
    main()
