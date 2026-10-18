# -*- coding: utf-8 -*-
"""Inventorie tout l'allemand que l'application prononce, et le chiffre.

    python audio/manifest.py              # rapport seul, n'ecrit rien
    python audio/manifest.py --ecrire     # ecrit aussi audio/manifest.json

CE QUI EST INVENTORIE
    Tout texte ALLEMAND que l'app peut dire a voix haute : les mots eux-memes,
    leurs phrases d'exemple, et -- facile a oublier -- les trois autres temps de
    chaque verbe plus l'imperatif, qui ont chacun leur bouton haut-parleur sur
    la carte. Cet oubli-la avait fausse la premiere estimation de 30 %.

    Les traductions (francais, anglais, turc) ne sont PAS inventoriees : elles
    restent a la synthese du navigateur. Ce sont les langues que l'utilisateur
    connait deja ; la voix y etiquette, elle n'enseigne pas.

    ⚠️ CE QUI COMPTE, C'EST CE QUE L'APP ENVOIE A direAllemand(), PAS CE QUE
    LES JSON CONTIENNENT. Quatre groupes ont manque ici jusqu'au 12 octobre
    2026 (1 087 textes), chacun ajoute a l'app apres la v407 sans que ce
    fichier soit mis au courant : les degres des adjectifs (une chaine
    construite a la volee), les verbes et adjectifs des chapitres VHS (une
    autre cle de themes.json), les verbes de position (en dur dans
    index.html), les personnes des scenes (un prefixe ajoute a la volee).
    tests/voix_couverture.py rejoue les formules de l'app et compare a ce
    manifeste : le lancer apres tout ajout qui parle.

L'IDENTIFIANT
    id = sha1(texte)[:16]. Nommer par le texte lui-meme plutot que par une cle
    de donnees a trois consequences, toutes voulues :
      - l'app recalcule l'identifiant a l'execution depuis le texte de la carte,
        donc rien a ajouter dans les JSON et aucun index a tenir a jour ;
      - les doublons disparaissent d'office (5,6 % du corpus) ;
      - ajouter un mot, c'est ajouter un fichier.
    Contrepartie assumee : corriger une coquille dans une phrase change son
    identifiant. L'ancien fichier devient orphelin, le nouveau manque, et le
    repli speechSynthesis couvre le trou jusqu'a la prochaine generation.
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]


def charger(nom):
    with io.open(os.path.join(RACINE, nom), encoding="utf-8") as f:
        return json.load(f)


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def recolter():
    """Renvoie la liste des occurrences : (texte, niveau, genre, source)."""
    out = []

    def prendre(texte, niveau, genre, source):
        if texte and texte.strip():
            out.append((texte.strip(), niveau or "A1", genre, source))

    for theme in charger("themes.json")["themes"]:
        niv = theme.get("niveau")
        for m in theme["mots"]:
            mot = (m.get("mot") or "").strip()
            genre = (m.get("genre") or "").strip()
            # Un nom se prononce sous DEUX formes, et il faut les deux fichiers :
            #   "Mann"      -- la dictee, qui dit justement de ne pas ecrire
            #                  l'article (voir dictation_hint) ;
            #   "der Mann"  -- la carte et le mode Ecoute, qui le prononcent
            #                  avec son article parce que c'est ainsi qu'on
            #                  retient le genre.
            # N'en generer qu'une renvoyait l'autre a la voix du telephone,
            # pour le type de carte le plus utilise de l'application.
            prendre(mot, niv, "mot", "nomen")
            if genre and genre != mot:
                prendre(genre + " " + mot, niv, "mot", "nomen.article")
            # LE PLURIEL AUSSI, depuis la v403 : la carte porte un second
            # haut-parleur a cote de la forme du pluriel (demande de Kirsty).
            # Sans cette ligne il n'a aucun fichier et sort a la voix du
            # telephone, juste sous un mot qui, lui, sort en voix enregistree --
            # l'ecart s'entend d'autant mieux que les deux se suivent.
            # "die" en toutes lettres parce que c'est ce que la carte affiche
            # ET ce que speakPlural() envoie : l'identifiant etant sha1(texte),
            # les deux doivent etre la MEME chaine, au caractere pres.
            pluriel = (m.get("pluriel") or "").strip()
            if pluriel and pluriel not in ("—", "-"):
                prendre("die " + pluriel, niv, "mot", "nomen.pluriel")
            prendre(m.get("exemple"), niv, "phrase", "nomen")
        # LES CHAPITRES VHS (audit du 12 octobre 2026). Un theme vhs_kapitelN_b1
        # porte, a cote de ses mots, ses propres `verben` et `adjektive`, que
        # l'app passe tels quels aux cartes Verbes et Adjectifs (modes
        # vhskapitelverben / vhskapiteladjektive). Ce manifeste ne lisait que
        # theme["mots"] : 347 phrases de verbes et 19 d'adjectifs n'avaient
        # jamais ete generees -- les autres doublaient verbe.json par chance.
        # Memes formes que pour verbe.json ci-dessous, puisque c'est le meme
        # rendu de carte qui les prononce.
        for v in theme.get("verben") or []:
            prendre(v.get("infinitif"), niv, "mot", "kapitel.verben")
            for cle in ("exemple", "perfekt", "praeteritum", "konjunktiv2"):
                prendre(v.get(cle), niv, "phrase", "kapitel.verben." + cle)
            imp = v.get("imperativ")
            if isinstance(imp, dict):
                formes = [imp.get("du"), imp.get("ihr"), imp.get("sie_Sie")]
                prendre(" ".join(x for x in formes if x), niv, "phrase",
                        "kapitel.verben.imperativ")
        for a in theme.get("adjektive") or []:
            prendre(a.get("mot"), niv, "mot", "kapitel.adjektive")
            prendre(a.get("exemple"), niv, "phrase", "kapitel.adjektive")

    verbes = charger("verbe.json")
    for niv in verbes:
        for v in verbes[niv]:
            prendre(v.get("infinitif"), niv, "mot", "verben")
            # Les quatre temps ont chacun leur bouton sur la carte, plus
            # l'imperatif : c'est la moitie du corpus des verbes.
            for cle in ("exemple", "perfekt", "praeteritum", "konjunktiv2"):
                prendre(v.get(cle), niv, "phrase", "verben." + cle)
            imp = v.get("imperativ")
            if isinstance(imp, dict):
                formes = [imp.get("du"), imp.get("ihr"), imp.get("sie_Sie")]
                prendre(" ".join(x for x in formes if x), niv, "phrase",
                        "verben.imperativ")

    for fichier, cle_mot, source in (("adjectif.json", "mot", "adjektive"),
                                     ("adverbe.json", "mot", "adverbien"),
                                     ("redewendung.json", "mot", "redewendungen")):
        d = charger(fichier)
        for niv in d:
            for x in d[niv]:
                prendre(x.get(cle_mot), niv, "mot", source)
                prendre(x.get("exemple"), niv, "phrase", source)
                # LES DEGRES DE L'ADJECTIF (v677, audit du 12 octobre 2026).
                # La carte affiche « besser · am besten » sous le mot, au meme
                # emplacement que le pluriel d'un nom, avec le meme bouton
                # d'ecoute -- et la chaine automatique du verso les dit aussi.
                # Ce qu'elle envoie est UNE SEULE chaine, construite a la
                # volee : reglerAudioPluriel(germanWord + ", " + card[15] +
                # ", " + card[16]). Comme pour « die » + pluriel : meme chaine
                # ici, au caractere pres, sinon l'identifiant ne concorde pas.
                # Rien pour un adjectif sans comparatif OU sans superlatif
                # (lila, tot) : la carte n'affiche alors pas la ligne.
                if source == "adjektive" and x.get("comparatif") and x.get("superlatif"):
                    prendre(x["mot"] + ", " + x["comparatif"] + ", " + x["superlatif"],
                            niv, "phrase", "adjektive.degres")

    d = charger("funktionswort.json")
    for section in d:
        for x in d[section]:
            niv = x.get("niveau")
            prendre(x.get("mot"), niv, "mot", "funktionswort." + section)
            prendre(x.get("exemple"), niv, "phrase", "funktionswort." + section)

    # L'EPREUVE D'ECOUTE DE L'EXAMEN. Elle etait absente de ce manifeste, et
    # personne ne l'avait vu : ses 120 passages passaient donc par la voix de
    # synthese du telephone -- la seule epreuve ou le son EST la competence
    # evaluee, entrainee sur une voix qui n'existe pas.
    #
    # Le champ s'appelle `audio` et non `exemple` : c'est un passage lu a voix
    # haute, jamais affiche a l'ecran. Le niveau vient de l'entree elle-meme.
    for x in charger("pruefung.json")["hoeren"]:
        prendre(x.get("audio"), x.get("niveau"), "phrase", "pruefung.hoeren")

    # LES TROIS AUTRES EPREUVES. Elles n'avaient aucun son du tout -- pas meme
    # celui du telephone : rien dans l'application ne les prononcait. Ce qu'on
    # ajoute ici est exactement ce que le bouton « entendre la phrase » joue,
    # une fois l'exercice repondu (voir phraseAllemandeDeLExercice).
    #
    #   sprechen  : la question de l'examinateur PUIS la reponse modele. Une
    #               epreuve d'expression orale sans modele entendu manquait sa
    #               competence de la meme facon que Hoeren manquait la sienne.
    #   schreiben : la lettre remise dans l'ordre.
    #   lesen     : le texte SEUL. La question qui l'accompagne est redigee
    #               dans la langue de l'usager et n'a rien a faire ici.
    pruefung = charger("pruefung.json")
    for x in pruefung["sprechen"]:
        blocs = x.get("chunks") or []
        if blocs:
            prendre((x.get("frage") or "") + " " + " ".join(blocs),
                    x.get("niveau"), "phrase", "pruefung.sprechen")
    for x in pruefung["schreiben"]:
        blocs = x.get("chunks") or []
        if blocs:
            prendre(" ".join(blocs), x.get("niveau"), "phrase",
                    "pruefung.schreiben")
    for x in pruefung["lesen"]:
        prendre(x.get("text"), x.get("niveau"), "phrase", "pruefung.lesen")

    # LES 1 682 EXERCICES DE GRAMMAIRE. Un exercice se termine sur une phrase
    # allemande JUSTE, et jusqu'a la v480 on pouvait la lire sans jamais
    # l'entendre -- « dem Mann » ne s'apprend pas seulement a l'oeil.
    #
    # ⚠️ CE BLOC DOIT RENDRE EXACTEMENT CE QUE RENVOIE
    # phraseAllemandeDeLExercice() DANS index.html, AU CARACTERE PRES.
    # L'identifiant etant sha1(texte), un espace de difference produit un
    # fichier orphelin ici et un fichier manquant la-bas -- sans aucune erreur
    # nulle part. Les trois cas, dans le meme ordre que le code JS :
    #   - des blocs a remettre en ordre -> les blocs joints par un espace ;
    #   - un blanc dans l'enonce -> l'enonce avec la bonne forme dedans,
    #     capitalisee si le blanc ouvre la phrase ;
    #   - tout le reste -> RIEN. Un enonce de type « Quel cas ? » est redige
    #     dans la langue de l'usager et n'a pas de bouton dans l'app non plus.
    #
    # Le niveau : ces exercices n'en portent aucun, et il ne sert ici qu'a
    # decider de l'ORDRE de generation. B1 est le milieu honnete d'un ensemble
    # qui va de A2 a B2.
    for nom, liste in charger("exercices.json")["jeux"].items():
        for x in liste:
            # audioDe d'abord, comme phraseAllemandeDeLExercice() : la phrase
            # juste, ecrite a la main quand la reconstruction lirait l'indice
            # (« vor Wo (Dativ) Haus », 104 exercices, corriges le 9 oct. 2026).
            if x.get("audioDe"):
                prendre(str(x["audioDe"]).strip(), "B1", "phrase", "exercices." + nom)
                continue
            blocs = x.get("chunks") or []
            if blocs:
                prendre(" ".join(blocs), "B1", "phrase", "exercices." + nom)
                continue
            enonce = x.get("question") or ""
            if "___" not in enonce:
                continue
            bon = x.get("correct") or (x.get("answers") or [""])[0]
            if not bon:
                continue
            bon = str(bon)
            if enonce.index("___") == 0:
                bon = bon[0].upper() + bon[1:]
            prendre(enonce.replace("___", bon, 1), "B1", "phrase",
                    "exercices." + nom)

    # LES EXERCICES D'ARTICLES NE SONT PAS DANS exercices.json : ils sont
    # FABRIQUES PAR LE CODE, dans index.html. Ce manifeste ne les voyait donc
    # pas, aucun mp3 n'a jamais ete genere pour eux, et l'app retombait sur la
    # voix de synthese du telephone. Signale par Jacques le 9 septembre 2026 :
    # « c'est pas ta voix Aurora, c'est ta voix du iPhone ». 146 phrases
    # manquaient sur 152.
    #
    # On les demande au code lui-meme (node evalue index.html) plutot que de
    # les recopier ici : une donnee recopiee derive, celle-ci est lue a la
    # source a chaque passage. Meme procede que tests/i18n_dump.js.
    for phrase in phrases_des_articles():
        prendre(phrase, "B1", "phrase", "exercices.articles")

    # LES VERBES DE POSITION (« legen ou liegen ? ») sont dans le meme cas :
    # huit verbes en dur dans index.html (positionsverbenTheme), pas dans
    # verbe.json. Dix-sept de leurs phrases doublaient verbe.json par chance,
    # les sept autres sortaient a la voix du telephone (audit du 12 octobre
    # 2026). Meme procede : lus a la source par tests/phrases_positionsverben.js.
    # Le niveau : A2, celui des prepositions mixtes que ce jeu exerce. Le
    # script rend l'infinitif (un mot) puis ses trois phrases : l'espace les
    # distingue.
    for texte in phrases_des_positionsverben():
        prendre(texte, "A2", "phrase" if " " in texte else "mot",
                "positionsverben")

    # LES SCENES ILLUSTREES (9 oct. 2026). Chaque question A2-C1 se conclut sur
    # une phrase allemande que la scene PRONONCE (champ phrase, lu par dire()
    # dans visuel/prototype/index.html, au caractere pres). Jacques : « on n'a
    # pas les phrases avec la voix d'Aurora ». Le niveau est celui de la couche.
    import glob
    for f in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "*.points.json"))):
        nom = os.path.basename(f)[:-len(".points.json")]
        with io.open(f, encoding="utf-8") as fh:
            scene = json.load(fh)
        for niv, couche in (scene.get("couches") or {}).items():
            for q in couche.get("qs") or []:
                prendre(q.get("phrase"), niv, "phrase", "scene." + nom)
        # LES PERSONNES (audit du 12 octobre 2026). En A1 « decouvrir », toucher
        # Anna ou Mark fait dire son prenom AVANT le mot : dire((p.personne ?
        # p.personne + ". " : "") + p.genre + " " + p.mot) -> « Anna. die Frau ».
        # Le mot seul (« die Frau ») est deja la par nomen.article ; la forme
        # avec le prenom est construite a la volee et n'etait nulle part. On la
        # lit dans scene-<nom>.js, le fichier que l'app charge : c'est lui qui
        # porte le genre, que points.json n'a pas (construire.py l'ajoute).
        for p in points_de_la_scene(nom):
            if p.get("personne") and p.get("genre") and p.get("mot"):
                prendre(p["personne"] + ". " + p["genre"] + " " + p["mot"],
                        "A1", "phrase", "scene.personne")

    # PREMIERS PAS (v837, 16 oct. 2026) : premiers-pas.json. Jacques : « toutes
    # les lectures avec la voix d'Aurora, pas la voix du telephone ». Ce que
    # l'app dit, au caractere pres : la forme de chaque ligne du tableau
    # (pp_tableau), l'expression et l'exemple de chaque flashcard (la carte
    # d'expression lit card[0] et card[3]), chaque phrase (direPhrase).
    for etape in charger("premiers-pas.json")["etapes"]:
        for l in etape["tableau"]["l"]:
            prendre(l[0], "A1", "phrase" if " " in l[0].strip() else "mot", "premiers_pas")
        for c in etape["cartes"]:
            prendre(c[0], "A1", "phrase" if " " in c[0].strip() else "mot", "premiers_pas")
            if len(c) > 2 and isinstance(c[2], str):
                prendre(c[2], "A1", "phrase", "premiers_pas")
        for p in etape["phrases"]:
            prendre(p["p"], "A1", "phrase", "premiers_pas")

    # A1 VOYAGE (v862-v864, 18 oct. 2026) : a1-voyage.json. Ce que l'app dit, au
    # caractere pres : les lignes des tableaux (escales ET suite), l'exemple de
    # chaque phrase toute faite et son moule rempli par chaque variante -- comme
    # la carte av_bloc : avant + variante + apres, coupe au premier « … » --, et
    # chaque replique des dialogues (« eux » comme « moi »).
    for t in a1_voyage_textes(charger("a1-voyage.json")):
        prendre(t, "A1", "phrase" if " " in t.strip() else "mot", "a1_voyage")

    return out


def contracter(avant, mot, espagnol):
    """« a el » -> « al », « de el » -> « del » : le miroir de contracterA1V()
    dans index.html (v866). Sans lui, le fichier de voix ne correspond plus au
    texte que l'app dit."""
    if espagnol and re.match(r"(?i)el ", mot):
        if re.search(r"(?i)(^|\s)a $", avant):
            return avant[:-2] + "al ", mot[3:]
        if re.search(r"(?i)(^|\s)de $", avant):
            return avant[:-3] + "del ", mot[3:]
    return avant, mot


def a1_voyage_textes(d, latam=False, espagnol=False):
    """Les textes allemands (ou espagnols) que l'A1 voyage fait entendre."""
    out = []
    lieux = d.get("escales", []) + d.get("installe", []) + d.get("suite", [])
    for e in lieux:
        for l in (e.get("tableau") or {}).get("l", []):
            out.append(l[0])
        for b in e.get("blocs", []):
            if latam and isinstance(b.get("la"), dict):
                b = dict(b, **b["la"])
            morceaux = (b.get("p") or "").split("…")
            avant, apres = morceaux[0], "…".join(morceaux[1:])
            if b.get("ex"):
                out.append(b["ex"])
            for v in b.get("v", []):
                a, m = contracter(avant, v, espagnol)
                out.append(a + m + apres)
        for l in (e.get("dialogue") or {}).get("l", []):
            out.append(l["la"] if latam and l.get("la") else l["p"])
    return out


def points_de_la_scene(nom):
    """Les points de scene-<nom>.js, tels que l'app les charge.

    Le fichier est du JavaScript genere (`window.SCENE = {...};`) ; on en lit
    l'objet JSON. Une scene sans fichier construit n'a pas de points : elle
    n'est pas encore dans l'app, donc rien a prononcer.
    """
    f = os.path.join(RACINE, "visuel", "prototype", "scene-" + nom + ".js")
    if not os.path.exists(f):
        return []
    with io.open(f, encoding="utf-8") as fh:
        src = fh.read()
    src = src[src.index("{"):].rstrip().rstrip(";")
    return json.loads(src).get("points") or []


def phrases_des_articles():
    """Les phrases allemandes des exercices d'articles, lues dans index.html.

    ⚠️ ARRET SI NODE ECHOUE. Un manifeste amput. de 146 phrases se
    regenererait sans un mot et laisserait ces exercices muets une seconde
    fois -- exactement le defaut qu'on repare ici.
    """
    return textes_lus_dans_index("phrases_articles.js",
                                 "les exercices d'articles")


def phrases_des_positionsverben():
    """L'infinitif et les trois phrases de chaque verbe de position, lus dans
    index.html par tests/phrases_positionsverben.js. Meme arret que ci-dessus."""
    return textes_lus_dans_index("phrases_positionsverben.js",
                                 "les verbes de position")


def textes_lus_dans_index(nom_script, quoi):
    """Fait evaluer index.html par node (tests/<nom_script>) et rend un texte
    par ligne. S'arrete si le script manque, echoue ou ne rend rien : un
    manifeste ampute se regenererait sans un mot."""
    script = os.path.join(RACINE, "tests", nom_script)
    if not os.path.exists(script):
        sys.exit("  tests/%s manquant : %s seraient omis du manifeste."
                 % (nom_script, quoi))
    r = subprocess.run(["node", script], capture_output=True, text=True,
                       encoding="utf-8")
    if r.returncode != 0:
        sys.exit("  tests/%s a echoue :\n%s" % (nom_script, r.stderr or ""))
    lignes = [l for l in (r.stdout or "").split("\n") if l.strip()]
    if not lignes:
        sys.exit("  tests/%s n'a rien rendu." % nom_script)
    return lignes


def dedoublonner(occurrences):
    """Un texte identique n'est genere qu'une fois. Il garde le niveau le plus
    bas ou il apparait : c'est celui qui decide de l'ordre de generation, et on
    veut qu'un mot vu en A1 soit produit avec le lot A1."""
    par_texte = {}
    for texte, niveau, genre, source in occurrences:
        e = par_texte.get(texte)
        if e is None:
            par_texte[texte] = {"id": identifiant(texte), "texte": texte,
                                "niveau": niveau, "genre": genre,
                                "sources": [source], "occurrences": 1}
        else:
            e["occurrences"] += 1
            if source not in e["sources"]:
                e["sources"].append(source)
            if NIVEAUX.index(niveau) < NIVEAUX.index(e["niveau"]):
                e["niveau"] = niveau
    entrees = list(par_texte.values())
    entrees.sort(key=lambda e: (NIVEAUX.index(e["niveau"]),
                                0 if e["genre"] == "mot" else 1, e["texte"]))
    return entrees


def rapport(occurrences, entrees):
    brut = sum(len(t) for t, _, _, _ in occurrences)
    net = sum(len(e["texte"]) for e in entrees)
    par_niveau = collections.OrderedDict((n, collections.Counter()) for n in NIVEAUX)
    for e in entrees:
        c = par_niveau[e["niveau"]]
        c[e["genre"] + "_n"] += 1
        c[e["genre"] + "_c"] += len(e["texte"])

    print("%-4s %8s %10s %9s %10s %12s %13s" %
          ("", "mots", "car.", "phrases", "car.", "total car.", "cumul"))
    cumul = 0
    for n in NIVEAUX:
        c = par_niveau[n]
        tot = c["mot_c"] + c["phrase_c"]
        cumul += tot
        print("%-4s %8d %10d %9d %10d %12d %13d" %
              (n, c["mot_n"], c["mot_c"], c["phrase_n"], c["phrase_c"], tot, cumul))

    print()
    print("  occurrences      : %6d  ->  %7d caracteres" % (len(occurrences), brut))
    print("  textes uniques   : %6d  ->  %7d caracteres" % (len(entrees), net))
    print("  economise        : %6d  ->  %7d caracteres (%.1f %%)" %
          (len(occurrences) - len(entrees), brut - net, 100.0 * (brut - net) / brut))
    print()
    # Un credit = un caractere en Multilingual v2, un demi en Flash.
    for nom, taux in (("Multilingual v2", 1.0), ("Flash", 0.5)):
        credits = int(net * taux)
        print("  %-16s %7d credits  ->  %.1f mois de Creator (121 000/mois)"
              % (nom, credits, credits / 121000.0))
    a12 = sum(par_niveau[n]["mot_c"] + par_niveau[n]["phrase_c"] for n in ("A1", "A2"))
    print()
    print("  A1 + A2 seuls    : %6d caracteres -- %s dans un mois de Creator"
          % (a12, "tiennent" if a12 <= 121000 else "NE TIENNENT PAS"))


def main():
    occurrences = recolter()
    entrees = dedoublonner(occurrences)
    rapport(occurrences, entrees)

    if "--ecrire" in sys.argv:
        chemin = os.path.join(RACINE, "audio", "manifest.json")
        with io.open(chemin, "w", encoding="utf-8", newline="") as f:
            f.write(json.dumps(entrees, ensure_ascii=False, indent=1))
        print("\n  ecrit : audio/manifest.json (%d entrees)" % len(entrees))
    else:
        print("\n  (rapport seul -- relancer avec --ecrire pour produire le manifeste)")


if __name__ == "__main__":
    main()
