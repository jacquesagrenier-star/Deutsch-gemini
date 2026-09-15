# -*- coding: utf-8 -*-
"""Extrait les listes de vocabulaire officielles, et mesure ce que le cours couvre.

    python tests/listes_examen.py --extraire     # PDF -> examens/*.json
    python tests/listes_examen.py --couverture   # confronte le corpus aux listes

LES TROIS LISTES, TELECHARGEES DEPUIS goethe.de

    dtz.pdf         Deutsch-Test fuer Zuwanderer -- l'examen qui clot le cours
                    d'integration, niveau A2-B1
    goethe_b1.pdf   Goethe-Zertifikat B1, environ 2 400 unites lexicales
    goethe_a2.pdf   Goethe-Zertifikat A2

POURQUOI ON PREND L'UNION DES TROIS. Elles decrivent le meme niveau du meme
cadre europeen et se recouvrent largement. Couvrir l'union, c'est couvrir les
trois -- et ca evite d'attacher le produit a une institution ou a un public
particulier. La tuile porte le NIVEAU, pas le nom d'un examen.

L'EXTRACTION EST UNE HEURISTIQUE, ET ELLE DOIT LE RESTER MODESTEMENT. Le PDF
est mis en page sur deux colonnes ; `pdftotext -raw` rend l'ordre de lecture,
ce qui donne une entree par ligne, mais une entree de verbe se poursuit sur la
ligne suivante (« abbiegen, biegt ab, » / « bog ab, ist abgebogen »). On
recolle donc les continuations, puis on ne garde que le MOT-VEDETTE : article
retire, pluriel et conjugaison coupes au premier virgule.

Ce qui en sort n'est pas parole d'evangile. Le chiffre de couverture est un
ORDRE DE GRANDEUR destine a une decision -- « la tuile vaut-elle le coup ? » --
et non une liste a importer telle quelle dans le cours.
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMENS = os.path.join(RACINE, "examens")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import langue as L                                          # noqa: E402

LISTES = ["dtz", "goethe_b1", "goethe_a2"]

# ⚠️ LE A1 EST EXTRAIT MAIS N'ENTRE PAS DANS LISTES, ET C'EST VOULU.
#
# LISTES est l'instrument du TAUX DE COUVERTURE, et ce taux est une
# affirmation publique : la tuile « Preparation A2-B1 » annonce couvrir ces
# listes-la. Ajouter le A1 a l'union deplacerait le chiffre sans que rien
# dans le cours ait change. Le A1 sert a autre chose : definir le NOYAU du
# niveau pour tests/frequence.py, qui le lit dans examens/goethe_a1.json.
LISTE_A1 = "goethe_a1"

ARTICLES = ("der ", "die ", "das ")

# LES COLONNES OU VIVENT LES MOTS-VEDETTES, en points PDF, par fichier.
#
# Les trois PDF n'ont pas la meme mise en page, et c'est ce qui a fait echouer
# la premiere extraction : `pdftotext -raw` rend l'ordre de lecture, donc il
# melange les mots-vedettes aux phrases d'exemple. On sortait 3 208 entrees du
# B1 la ou l'officiel en annonce 2 400 -- 800 formes conjuguees et morceaux de
# mots coupes pris pour du vocabulaire, et un taux de couverture fausse.
#
# pypdf donne la position de chaque bloc de texte. Un mot-vedette est dans la
# colonne de gauche d'une demi-page ; un exemple est a sa droite. Deux
# demi-pages par page, donc deux plages.
COLONNES = {
    "dtz":       ((0, 110), (290, 380)),
    "goethe_b1": ((0, 110), (300, 400)),
    "goethe_a2": ((0, 110), (290, 380)),
}

# Le A2 met le mot ET son exemple dans un seul bloc, separes par une longue
# suite d'espaces. La decoupe sur deux espaces ou plus rattrape ce cas, et ne
# gene pas les deux autres fichiers.
ESPACES = re.compile(r"\s{2,}")

# Une entree de verbe se poursuit sur la ligne suivante (« abbiegen, biegt ab, »
# / « bog ab, ist abgebogen ») : la precedente finit par une virgule.
# Une cesure se poursuit aussi : la precedente finit par un trait d'union.
def recoller(entrees):
    out = []
    for x in entrees:
        if out and (out[-1].endswith(",") or out[-1].endswith("-")):
            out[-1] = out[-1].rstrip("-") + (" " if out[-1].endswith(",") else "") + x
        else:
            out.append(x)
    return out


def blocs_vedettes(pdf, plages):
    """Les blocs de texte situes dans une colonne de mots-vedettes."""
    import pypdf
    lecteur = pypdf.PdfReader(pdf)
    pages = []
    for page in lecteur.pages:
        blocs = []

        def visiteur(txt, cm, tm, police, taille, _b=blocs):
            t = txt.strip()
            if t:
                _b.append((round(tm[4]), round(tm[5]), t))

        page.extract_text(visitor_text=visiteur)
        gardes = [(x, y, t) for x, y, t in blocs
                  if any(a <= x < b for a, b in plages)]
        # De haut en bas, puis de gauche a droite : l'ordre de lecture humain.
        gardes.sort(key=lambda m: (-m[1], m[0]))
        pages.extend(ESPACES.split(t)[0].strip() for _, _, t in gardes)
    return pages


# Lignes de mise en page a jeter : titres, numeros de page, pieds de page.
BRUIT = re.compile(r"^(WORTLISTE|WORTSCHATZ|VS_\d+|GOETHE.*|TELC.*|\d+|[A-Z]|"
                   r"[\d.]+\s*[A-ZÄÖÜ ]*)$")


def nettoyer(entree):
    """Une entree brute -> le mot-vedette seul, ou None si ce n'en est pas un."""
    x = entree.strip()
    if not x or BRUIT.match(x) or "=" in x:
        return None
    # Le mot-vedette s'arrete au premier separateur : virgule (pluriel ou
    # conjugaison), parenthese (« Abgase (Pl.) »), barre oblique (variante).
    tete = re.split(r"[,(/;]", x)[0].strip()
    for a in ARTICLES:
        if tete.lower().startswith(a):
            tete = tete[len(a):].strip()
    tete = tete.strip('"').strip()
    # Un mot-vedette allemand est un seul mot. Deux mots ou plus, c'est une
    # phrase que la mise en page a laissee passer.
    if not tete or " " in tete or len(tete) < 2:
        return None
    if not re.match(r"^[A-Za-zÄÖÜäöüß\-]+$", tete):
        return None
    return tete


# POURQUOI IL N'Y A PAS DE FILTRE DES FORMES FLECHIES, ET C'EST DELIBERE.
#
# Il reste dans les listes une centaine de preterits et de participes echappes
# des lignes de conjugaison (« arbeitete », « gelacht »). Un filtre a ete
# essaye : ne retirer un mot que si son propre infinitif figure deja dans la
# liste, ce qui semblait sur. Il a retire 671 entrees du DTZ, dont « erste » et
# « dritte » -- de vrais mots du niveau.
#
# Le vrai probleme n'etait pas le filtre : c'est qu'on regle une heuristique
# SANS VERITE DE REFERENCE. Chaque passe deplacait le total de plusieurs
# centaines, dans un sens ou dans l'autre, sans qu'on puisse dire laquelle
# etait la meilleure. On s'arrete donc a la mesure geometrique, qui est
# verifiable : les colonnes du PDF sont un fait, pas une supposition.
#
# Le chiffre porte donc une incertitude d'environ 15 %, et il faut la dire en
# meme temps que lui. Elle suffit largement a la seule question posee : le
# cours couvre-t-il les listes officielles ? La reponse -- non, il manque des
# centaines de mots -- ne bouge pas dans cette fourchette.


# ⚠️ LE A1 A UNE AUTRE GEOMETRIE, ET LA MECANIQUE DES COLONNES N'Y MARCHE PAS.
#
# Les trois autres PDF posent le mot-vedette dans une colonne et sa phrase
# d'exemple dans une autre : il suffit de garder la premiere. Le A1 met les
# deux DANS LE MEME BLOC, a x = 143. Il faut donc couper a l'interieur d'une
# ligne, et non entre deux colonnes.
#
# Le signal, et il est solide : une phrase allemande commence par une
# MAJUSCULE. Une ligne qui commence par une minuscule, par un article ou par
# « (sich) » porte donc un mot-vedette ; une ligne qui commence par une
# majuscule sans article est la suite d'exemples de l'entree precedente.
#
# Les cinq premieres pages sont de la prose (couverture, sommaire, Vorwort,
# Themen) et sortiraient « zusammengestellt » comme un mot du niveau.
#
# Ce que ca donne : 822 mots-vedettes pour ~650 annonces dans le Vorwort. Le
# depassement vient surtout des tableaux d Uhrzeit (« dreizehn Uhr siebzehn »
# rend trois jetons). Il est SANS CONSEQUENCE ici, pour la raison dite plus
# bas : cette liste sert a reconnaitre nos mots, pas a certifier un total. Le
# chiffre sert a ORDONNER, pas a compter.
VEDETTE_A1 = [
    re.compile(r"^(?:der|die|das)\s+([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\-]+)"),
    re.compile(r"^\(sich\)\s+([a-zäöüß][A-Za-zÄÖÜäöüß\-]+)"),
    re.compile(r"^([a-zäöüß][A-Za-zÄÖÜäöüß\-]*)(?:\s|,|$)"),
]
BRUIT_A1 = re.compile(r"^(?:VS_\d+|Seite\s*\d+|[A-ZÄÖÜ]|wortliste|"
                      r"Alphabetische|INVeNTAre|WORTLISTE)$", re.I)


# ⚠️ LES PAGES 6 A 8 NE SE LISENT PAS COMME LES AUTRES, ET L'OUBLIER A DONNE
# UN RESULTAT ABSURDE : « vier » entrait dans le noyau, « zwei » et « drei »
# non -- donc la seance servait QUATRE avant DEUX.
#
# Ces trois pages sont la Wortgruppenliste : des tableaux « 1 = eins », ou le
# mot ecrit vit a droite (x = 178 ou 378), hors de la colonne des mots-vedettes.
# Seuls quelques nombres y tombaient par hasard.
#
# On y prend donc TOUT ce qui ressemble a un mot allemand, sans regarder la
# colonne. C'est sans risque, et pour une raison qui vaut d'etre dite : du
# bruit en TROP dans cette liste ne coute rien. Elle ne sert qu'a repondre
# « ce mot du cours est-il dans le noyau ? » -- un intrus comme
# « wortgruppenliste » ne correspond a aucune de nos entrees et ne sera jamais
# consulte. Le seul defaut couteux serait un mot du cours MANQUANT, et c'est
# exactement ce qu'on repare ici.
MOT_ALLEMAND = re.compile(r"^[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\-]+$")
PAGES_GROUPES = range(5, 8)


def extraire_a1(pdf):
    import pypdf
    lecteur = pypdf.PdfReader(pdf)
    vus, mots = set(), []

    def garder(tete):
        tete = (tete or "").strip("-")
        if len(tete) >= 2 and tete not in vus:
            vus.add(tete)
            mots.append(tete)

    for num, page in enumerate(lecteur.pages):
        if num < 5:
            continue                      # couverture, sommaire, Vorwort, Themen
        blocs = []

        def visiteur(txt, cm, tm, police, taille, _b=blocs):
            t = txt.strip()
            if t:
                _b.append((round(tm[4]), round(tm[5]), t))

        page.extract_text(visitor_text=visiteur)
        if num in PAGES_GROUPES:
            for _, _, t in blocs:
                for jeton in re.split(r"[\s\t/]+", t):
                    if MOT_ALLEMAND.match(jeton) and jeton.lower() not in (
                            "der", "die", "das"):
                        garder(jeton)
            continue
        gardes = [(x, y, t) for x, y, t in blocs if 130 <= x <= 160]
        gardes.sort(key=lambda m: (-m[1], m[0]))
        for _, _, ligne in gardes:
            x = ligne.strip()
            if not x or BRUIT_A1.match(x):
                continue
            for rx in VEDETTE_A1:
                m = rx.match(x)
                if not m:
                    continue
                garder(m.group(1))
                break
    return sorted(mots)


def extraire():
    out = {}
    pdf_a1 = os.path.join(EXAMENS, LISTE_A1 + ".pdf")
    if os.path.isfile(pdf_a1):
        mots = extraire_a1(pdf_a1)
        chemin = os.path.join(EXAMENS, LISTE_A1 + ".json")
        with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"source": LISTE_A1, "mots": mots}, f,
                      ensure_ascii=False, indent=1)
            f.write("\n")
        out[LISTE_A1] = mots
        print("  %-12s %5d mots-vedettes  (noyau, hors taux de couverture)"
              % (LISTE_A1, len(mots)))
    else:
        print("  ! absent : %s" % pdf_a1)
    for nom in LISTES:
        pdf = os.path.join(EXAMENS, nom + ".pdf")
        if not os.path.isfile(pdf):
            print("  ! absent : %s" % pdf)
            continue
        brut = recoller(blocs_vedettes(pdf, COLONNES[nom]))
        mots = sorted({m for m in (nettoyer(x) for x in brut) if m})
        chemin = os.path.join(EXAMENS, nom + ".json")
        with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"source": nom, "mots": mots}, f, ensure_ascii=False, indent=1)
            f.write("\n")
        out[nom] = mots
        print("  %-12s %5d mots-vedettes" % (nom, len(mots)))
    return out


def charger():
    out = {}
    for nom in LISTES:
        chemin = os.path.join(EXAMENS, nom + ".json")
        if os.path.isfile(chemin):
            out[nom] = set(json.load(io.open(chemin, encoding="utf-8"))["mots"])
    return out


def corpus():
    """Toutes les formes que le cours ENSEIGNE : entree, pluriel et paire.

    CETTE FONCTION EST LA SEULE SOURCE DU CHIFFRE DE COUVERTURE, et elle vit
    ici plutot que dans paliers_examen.py pour une raison precise : les deux
    modules ont compte differemment pendant un temps, l'un a 2 437 mots
    couverts et l'autre a 2 596, sans que rien ne le signale. Deux comptes du
    meme fait divergent toujours ; il n'en reste donc qu'un.

    Les listes officielles portent la forme lue sur un panneau -- « Senioren »,
    « Kenntnisse » -- et comptent le feminin comme une entree a part --
    « Autorin » a cote de « Autor ». Or la carte de « der Autor » affiche
    « Feminin : die Autorin ». Le mot est enseigne, il est couvert.
    """
    out = set()
    d = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))
    for t in d.get("themes", d):
        for m in t.get("mots", []):
            for cle in ("mot", "pluriel", "feminin", "masculin"):
                f = (m.get(cle) or "").strip()
                if f and f != "—":
                    out.add(f)
    lg = L.Langue("tr")          # la langue cible est sans importance ici
    for cartes in lg.toutes_les_cartes().values():
        for c in cartes:
            mot = (c.get("cle") or "").strip()
            if mot:
                out.add(mot)

    # LES MOTS-OUTILS COMPTENT, et les oublier faussait le chiffre a la
    # baisse. funktionswort.json n'est pas un des cinq JSON de vocabulaire --
    # il est range par classe de mot et Langue.toutes_les_cartes() ne le voit
    # pas -- mais ses 161 entrees SONT des cartes, avec leur cas et leur
    # phrase. Sans cette boucle, « fuer », « weil » et « dieser » passaient
    # pour absents du cours alors qu'ils y sont depuis toujours.
    #
    # Une entree peut porter deux formes separees par une barre --
    # « eben / halt » -- que les listes officielles comptent separement.
    chemin = os.path.join(RACINE, "funktionswort.json")
    if os.path.isfile(chemin):
        for liste in json.load(io.open(chemin, encoding="utf-8")).values():
            for m in liste:
                for f in (m.get("mot") or "").split("/"):
                    f = f.strip()
                    if f:
                        out.add(f)
    return out


def couverture():
    listes = charger()
    if not listes:
        print("Aucune liste extraite. Lancer --extraire d'abord.")
        return 1

    corpus_mots = corpus()
    print("  corpus Wortando : %d formes allemandes enseignees" % len(corpus_mots))
    print()

    union = set()
    for nom, mots in listes.items():
        union |= mots
        dedans = mots & corpus_mots
        print("  %-12s %5d mots   couverts %5d   %5.1f %%"
              % (nom, len(mots), len(dedans), 100.0 * len(dedans) / len(mots)))
    dedans = union & corpus_mots
    print("  %-12s %5d mots   couverts %5d   %5.1f %%"
          % ("UNION", len(union), len(dedans), 100.0 * len(dedans) / len(union)))
    print()

    # RECONCILIATION AVEC paliers_examen.py, qui annonce un autre chiffre.
    #
    # Les deux ne mesurent pas la meme chose, et sans cette ligne l'ecart passe
    # pour un defaut : « couverts » compte les mots qu'une carte enseigne ;
    # « reste a faire » retire en plus les mots-outils deja arbitres et les
    # variantes de casse (« schade » contre « Schade »). Un mot ecarte n'est ni
    # couvert ni a faire -- il n'est simplement plus une question.
    hors = set()
    chemin_e = os.path.join(RACINE, "ajouts", "noyau-00-ecartes.txt")
    if os.path.isfile(chemin_e):
        hors = {l.strip() for l in io.open(chemin_e, encoding="utf-8")
                if l.strip() and not l.startswith("#")}
    minuscules = {m.lower() for m in corpus_mots}
    reste = {m for m in union
             if m not in corpus_mots and m.lower() not in minuscules and m not in hors}
    # UN MOT COUVERT N'EST PAS UN MOT ECARTE, meme s'il figure encore dans le
    # fichier des ecartes. Les deux se sont contredits : 77 mots-outils y
    # etaient listes comme « pas de carte » alors qu'ils en avaient une. Le
    # fichier a ete remis d'accord (tests/nettoyer_ecartes.py), mais le compte
    # ne s'y fie plus -- c'est la donnee qui tranche, pas la liste.
    print("  dont %d ecarte(s) volontairement (mots-outils, bruit d'extraction)"
          % len((union & hors) - corpus_mots))
    print("  reste a faire : %d mot(s)" % len(reste))
    print()

    manquants = sorted(union - corpus_mots)
    chemin = os.path.join(EXAMENS, "manquants.txt")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Mots des listes officielles absents du cours (%d)\n" % len(manquants))
        f.write("# Produit par tests/listes_examen.py --couverture.\n")
        f.write("# L'extraction est une heuristique : quelques entrees sont du\n")
        f.write("# bruit de mise en page, et quelques absences sont des formes\n")
        f.write("# que le cours a sous une autre entree. A lire, pas a importer.\n\n")
        f.write("\n".join(manquants))
        f.write("\n")
    print("  ecrit : examens/manquants.txt  (%d mots)" % len(manquants))
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if "--extraire" in sys.argv:
        extraire()
        return 0
    if "--couverture" in sys.argv:
        return couverture()
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
