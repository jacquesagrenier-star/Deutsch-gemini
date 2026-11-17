# -*- coding: utf-8 -*-
"""Les briques des sources du vocabulaire des Soins (un fichier par theme : tNN_*.py).

ON CORRIGE ICI, JAMAIS DANS pflege/datos/ : pflege/datos/themes.json est DERIVE,
refait par  python pflege/outils/construire.py (via pflege/sources/<theme>.py et adaptateur.py),
puis controle par  python tests/pflege.py  et  python tests/pflege_vocabulaire.py

Une entree = une carte. Les champs sont ecrits en une ligne, separes par « | », dans
un ORDRE FIXE :

  traductions (9) : fr | en | tr | uk | fa | ar | pt | pl | ru  [| es]
  exemple    (10) : de | fr | en | tr | uk | fa | ar | pt | pl | ru  [| es]

- l'ESPAGNOL (10e langue d'interface, decision de Jacques du 16 nov. : « la traduction pour la
  langue de l'apprenant dans toutes les langues ») s'ajoute EN DERNIER : 10 traductions et 11
  exemples. Tout mot ne depuis le 16 nov. l'a ; les plus anciens le recevront par un lot a part ;

- le francais d'un NOM porte son article (« l'escarre », « la toilette ») : le
  constructeur en tire article_fr, comme dans themes.json ;
- pt = le portugais du Bresil (la langue d'interface `pt` de l'app) ;
- chaque terme est le MOT DU METIER dans la langue cible (« escarre », « pressure
  ulcer », « bası yarası »), pas une traduction mot a mot ;
- un prenom s'ecrit {Elif}, {Jonas}, {Frau Hoffmann}... : il est remplace a la
  construction par la table de personnages.py (les noms peuvent encore changer).

Les constructeurs :

  N(niveau, "die Schulter", "Schultern", trad, ex)  nom ; pluriel "—" = sans pluriel,
                                                     "(Pl.)" = toujours au pluriel
  V(niveau, "lagern", trad, ex, aux="haben", p2="gelagert")   verbe
  A(niveau, "geschwollen", trad, ex)                adjectif (ou paire d'adjectifs)
  X(niveau, "Wie geht es Ihnen?", trad, ex)         expression, phrase, groupe de mots
  P(niveau, "das Bauchweh", "die Abdominalschmerzen",   PAIRE (sorte « paire », 15 nov.) : ce que dit
    trad_patient, trad_service, ex_patient, ex_service)  le PATIENT, puis ce que dit ou ecrit le
                                                     SERVICE ; les deux traductions et les deux
                                                     exemples (10 champs chacun) dans le meme ordre
  R(niveau, "Kopf", ex)                             REPRISE d'un mot du corpus general :
                                                     meme carte, une phrase de soins en
                                                     plus ; precision=trad si le corpus
                                                     ne donne pas le sens du metier

Un verbe (et une reprise de verbe) donne son Perfekt : aux="haben"/"sein" et p2="gelagert", ou
perfekt="hat sich verschlechtert / hat sich gebessert" en entier (paires).

Options communes : chapitre="ch01_aufnahme" (le chapitre de « Ma journee au service »,
pflege/sources/chapitres.py ; sinon chapitres_mots.py, sinon le chapitre du theme), relire=True (une infirmiere doit valider ; ⚕️ de l'annexe A),
note="..." (pour la relectrice, en francais, jamais affichee),
es_trad="..." (une reprise sans precision= dont la fiche du corpus n'a pas d'espagnol),
sens_distinct="..." (le mot existe au corpus dans un AUTRE sens : on en fait une
carte a part, et on dit lequel).
"""

LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
NIVEAUX = ("A2", "B1", "B2")


def _champs(texte, n, quoi, mot):
    parts = [p.strip() for p in texte.split("|")]
    if len(parts) == n + 1:   # l'espagnol en dernier (16 nov.)
        n += 1
    if len(parts) != n:
        raise ValueError("%s : %s attend %d champs, en a %d" % (mot, quoi, n, len(parts)))
    if any(not p for p in parts):
        raise ValueError("%s : %s a un champ vide" % (mot, quoi))
    return parts


def _base(niveau, typ, mot, trad, ex, opts):
    if niveau not in NIVEAUX:
        raise ValueError("%s : niveau %r" % (mot, niveau))
    e = {"niveau": niveau, "type": typ, "mot": mot}
    if trad is not None:
        e["trad"] = _champs(trad, 9, "la traduction", mot)
    e["ex"] = _champs(ex, 10, "l'exemple", mot)
    for k in ("relire", "note", "sens_distinct", "aux", "p2", "perfekt", "feminin", "masculin", "source", "chapitre",
              "es_trad"):
        if opts.get(k):
            e[k] = opts[k]
    if opts.get("precision"):
        e["precision"] = _champs(opts["precision"], 9, "la precision", mot)
    inconnus = set(opts) - {"relire", "note", "sens_distinct", "aux", "p2", "perfekt", "feminin", "masculin", "source", "precision", "typ", "chapitre", "es_trad"}
    if inconnus:
        raise ValueError("%s : options inconnues %s" % (mot, sorted(inconnus)))
    return e


def N(niveau, art_mot, pluriel, trad, ex, **opts):
    art, _, mot = art_mot.partition(" ")
    if art not in ("der", "die", "das"):
        raise ValueError("%s : article manquant" % art_mot)
    e = _base(niveau, "nom", mot, trad, ex, opts)
    if pluriel == "(Pl.)":
        e["genre"], e["pluriel"] = "die (Pl.)", mot
    else:
        e["genre"], e["pluriel"] = art, pluriel
    return e


def V(niveau, mot, trad, ex, **opts):
    return _base(niveau, "verbe", mot, trad, ex, opts)


def A(niveau, mot, trad, ex, **opts):
    return _base(niveau, "adjectif", mot, trad, ex, opts)


def X(niveau, mot, trad, ex, **opts):
    return _base(niveau, "expression", mot, trad, ex, opts)


def P(niveau, patient, service, trad_patient, trad_service, ex_patient, ex_service, **opts):
    """Une paire « dit le patient / dit le service » (pflege/FORMAT-DONNEES.md, § 1 bis).
    Les mots s'ecrivent avec leur article (« das Bauchweh ») : la carte les montre tels quels."""
    e = _base(niveau, "paire", service, trad_service, ex_service, opts)
    e["patient"] = patient
    e["trad_patient"] = _champs(trad_patient, 9, "la traduction du patient", service)
    e["ex_patient"] = _champs(ex_patient, 10, "l'exemple du patient", service)
    return e


def R(niveau, mot, ex, **opts):
    typ = opts.pop("typ", None)
    e = _base(niveau, "reprise", mot, None, ex, opts)
    if typ:
        e["type_corpus"] = typ
    return e
