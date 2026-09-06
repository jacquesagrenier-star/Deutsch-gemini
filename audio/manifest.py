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

    return out


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
