# -*- coding: utf-8 -*-
"""Le pont entre les sources du vocabulaire (tNN_*.py, compactes, ecrites a la main) et le FORMAT
que l'app charge (pflege/FORMAT-DONNEES.md, § 1 : un fichier pflege/sources/<theme>.py avec THEME et
MOTS, que pflege/outils/construire.py transforme en pflege/datos/themes.json).

On ecrit et on corrige dans tNN_*.py ; pflege/sources/<theme>.py ne fait qu'appeler theme_soins().

Conversions :
  - N, V, A, X -> le dictionnaire du § 1 (sorte nom | verbe | adjectif | expression), trad = {langue:
    (traduction, exemple)} pour les 9 langues ; « die (Pl.) » -> genre « die », pluriel = le mot ;
  - V -> perfekt « hat gelagert » (aux + p2, « hat sich … » pour un verbe pronominal) ou perfekt= donne ;
  - R (reprise du corpus general) -> l'entree complete avec "corpus": True : genre, pluriel, article_fr
    et traductions pris a la fiche du corpus (precision= si le corpus ne donne pas le sens du metier),
    la phrase d'exemple de soins de la source ; adverbe du corpus -> sorte « adjectif » ;
  - {Personnage} -> le nom de la langue (personnages.py) ;
  - LECTURES {ecrit: dit} -> "lecture" sur l'entree dont l'exemple a des chiffres ; "lecture_mot" si le
    mot lui-meme en a ;
  - relire=True -> "relire" : la note (note=) ou « ⚕️ a valider ».
"""
import importlib.util
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(ICI)), "outils"))
import corpus  # noqa: E402
from commun import LANGUES as ORDRE_SOURCE  # noqa: E402  fr en tr uk fa ar pt pl ru
from personnages import PERSONNAGES, LANGUES_EX  # noqa: E402

LANGUES_APP = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
SORTE = {"nom": "nom", "verbe": "verbe", "adjectif": "adjectif", "adverbe": "adjectif",
         "expression": "expression", "mot-outil": "expression"}
ARTICLES_FR = ("le ", "la ", "les ", "l'", "l’")

# Une icone au trait par theme (viewBox 24, comme les themes du corpus).
ICONES = {
    "koerper": '<svg viewBox="0 0 24 24"><circle cx="12" cy="4.5" r="2.2"/><path d="M8 21l1.5-8M16 21l-1.5-8M7 9.5l5-1.5 5 1.5M9.5 13h5l-.5-5h-4z"/></svg>',
    "grundpflege": '<svg viewBox="0 0 24 24"><path d="M3 18v-6h18v6M3 15h18M6 12V9a2 2 0 0 1 2-2h3v5"/><path d="M3 18v2M21 18v2"/></svg>',
    "medikamente": '<svg viewBox="0 0 24 24"><rect x="3" y="9" width="12" height="6" rx="3" transform="rotate(-35 9 12)"/><path d="M7.5 9.5l3.5 5"/><circle cx="17.5" cy="16.5" r="3.5"/></svg>',
    "hygiene": '<svg viewBox="0 0 24 24"><path d="M12 3s5 6 5 10a5 5 0 0 1-10 0c0-4 5-10 5-10z"/><path d="M10 14a2 2 0 0 0 2 2"/></svg>',
    "ernaehrung": '<svg viewBox="0 0 24 24"><path d="M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10"/><path d="M15 3h4l-1 8h-2zM17 11v10"/></svg>',
    "notfaelle": '<svg viewBox="0 0 24 24"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/></svg>',
    "team": '<svg viewBox="0 0 24 24"><circle cx="8" cy="8" r="3"/><circle cx="16.5" cy="9" r="2.5"/><path d="M2.5 20a5.5 5.5 0 0 1 11 0M13.5 20a4 4 0 0 1 8 0"/></svg>',
    "dokumentation": '<svg viewBox="0 0 24 24"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M8.5 10h7M8.5 14h7M8.5 18h4"/></svg>',
    "angehoerige": '<svg viewBox="0 0 24 24"><path d="M12 20s-7-4.3-7-9.6A4 4 0 0 1 12 7.6a4 4 0 0 1 7 2.8C19 15.7 12 20 12 20z"/><path d="M9 12.5c1 1.2 2 1.7 3 1.7s2-.5 3-1.7"/></svg>',
    "szenen": '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 15l5-4 4 3 3-2 6 4"/><circle cx="16" cy="9" r="1.5"/></svg>',
}


def charger(nom_module):
    chemin = os.path.join(ICI, nom_module + ".py")
    spec = importlib.util.spec_from_file_location("vocabulaire_" + nom_module, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def noms(texte, langue):
    def rep(mo):
        n = mo.group(1)
        if n not in PERSONNAGES:
            raise ValueError("personnage inconnu {%s} dans : %s" % (n, texte))
        forme = PERSONNAGES[n][langue]
        avant = texte[:mo.start()]
        # en tete de phrase : la majuscule (« a senhora Weber » -> « A senhora Weber »)
        if not avant.strip() or re.search(r"[.!?:]\s*$|[«„“\"]\s*$", avant):
            forme = forme[:1].upper() + forme[1:]
        return forme
    return re.sub(r"\{([^{}]+)\}", rep, texte)


def _article(fr):
    for a in ARTICLES_FR:
        if fr.startswith(a):
            return ("l'" if a in ("l'", "l’") else a), fr[len(a):]
    return "", fr


def _trad(traductions, exemples):
    """traductions : {langue: texte} ; exemples : liste source (de, fr, en, ...)."""
    ex = dict(zip(LANGUES_EX, exemples))
    return {l: (traductions[l], noms(ex[l], l)) for l in LANGUES_APP}


def source_reprise(e):
    hits = corpus.chercher(e["mot"], e.get("type_corpus"))
    if e.get("source"):
        hits = [h for h in hits if h["ou"] == e["source"]]
    if not hits:
        raise ValueError("reprise %r : absent du corpus" % e["mot"])
    hors_vhs = [h for h in hits if not str(h["ou"]).startswith("vhs_")]
    return (hors_vhs or hits)[0]


# Le Perfekt des verbes REPRIS du corpus (verbe.json n'en donne qu'une phrase) ; un verbe neuf le
# porte dans sa source (aux= et p2=, ou perfekt=).
PERFEKT_CORPUS = {
    "wehtun": "hat wehgetan", "husten": "hat gehustet", "ausstrahlen": "hat ausgestrahlt",
    "schwitzen": "hat geschwitzt", "weinen": "hat geweint", "trösten": "hat getröstet",
    "sterben": "ist gestorben", "beruhigen": "hat beruhigt", "zuhören": "hat zugehört",
    "waschen": "hat gewaschen", "sich waschen": "hat sich gewaschen", "duschen": "hat geduscht",
    "anziehen": "hat angezogen", "ausziehen": "hat ausgezogen", "rasieren": "hat rasiert",
    "aufstehen": "ist aufgestanden", "lagern": "hat gelagert", "messen": "hat gemessen",
    "wiegen": "hat gewogen", "einnehmen": "hat eingenommen", "essen": "hat gegessen",
    "trinken": "hat getrunken", "bluten": "hat geblutet", "atmen": "hat geatmet",
    "stürzen": "ist gestürzt", "aufschreiben": "hat aufgeschrieben", "unterschreiben": "hat unterschrieben",
    "dokumentieren": "hat dokumentiert", "eintragen": "hat eingetragen", "sich krankmelden": "hat sich krankgemeldet",
    "krankmelden": "hat sich krankgemeldet", "abzeichnen": "hat abgezeichnet", "verbinden": "hat verbunden",
    "behandeln": "hat behandelt", "versorgen": "hat versorgt", "begleiten": "hat begleitet",
    "betreuen": "hat betreut", "beobachten": "hat beobachtet", "kontrollieren": "hat kontrolliert",
    "überwachen": "hat überwacht", "informieren": "hat informiert", "melden": "hat gemeldet",
    "hinfallen": "ist hingefallen", "fallen": "ist gefallen", "putzen": "hat geputzt",
    "helfen": "hat geholfen", "untersuchen": "hat untersucht", "spritzen": "hat gespritzt",
    "desinfizieren": "hat desinfiziert", "wechseln": "hat gewechselt", "absetzen": "hat abgesetzt",
    "verabreichen": "hat verabreicht", "schlucken": "hat geschluckt", "vertrauen": "hat vertraut",
    "sich verletzen": "hat sich verletzt", "verletzen": "hat verletzt", "vorbeugen": "hat vorgebeugt",
    "anrufen": "hat angerufen", "tauschen": "hat getauscht", "übernehmen": "hat übernommen",
    "operieren": "hat operiert", "röntgen": "hat geröntgt", "massieren": "hat massiert",
    "einspringen": "ist eingesprungen", "übergeben": "hat übergeben", "protokollieren": "hat protokolliert",
    "mitteilen": "hat mitgeteilt", "benachrichtigen": "hat benachrichtigt", "sich ernähren": "hat sich ernährt",
    "abnehmen": "hat abgenommen", "zunehmen": "hat zugenommen", "sich erholen": "hat sich erholt",
    "sich ausruhen": "hat sich ausgeruht", "ausruhen": "hat sich ausgeruht", "sich hinlegen": "hat sich hingelegt",
    "sich setzen": "hat sich gesetzt", "sich bewegen": "hat sich bewegt", "bewegen": "hat bewegt",
}


def _perfekt(e):
    if e.get("perfekt"):
        return e["perfekt"]
    if e["type"] == "reprise":
        k = e["mot"]
        if k in PERFEKT_CORPUS:
            return PERFEKT_CORPUS[k]
        raise ValueError("reprise du verbe %r : Perfekt inconnu (perfekt= ou PERFEKT_CORPUS)" % k)
    if e.get("p2"):
        aux = {"haben": "hat", "sein": "ist"}[e.get("aux", "haben")]
        sich = "sich " if e["mot"].startswith("sich ") else ""
        return "%s %s%s" % (aux, sich, e["p2"])
    return ""


def convertir(e, lectures):
    typ = e["type"]
    d = {"niveau": e["niveau"]}
    if typ == "reprise":
        h = source_reprise(e)
        f = h["fiche"] or {}
        sorte = SORTE[h["type"]]
        d.update({"sorte": sorte, "mot": h["mot"]})
        if sorte == "nom":
            g = f.get("genre", "")
            d.update({"genre": "die" if g == "die (Pl.)" else g, "pluriel": f.get("pluriel") or "—",
                      "article_fr": f.get("article_fr") or ""})
        if e.get("precision"):
            tr = dict(zip(ORDRE_SOURCE, e["precision"]))
            if sorte == "nom":
                art, tr["fr"] = _article(tr["fr"])
                d["article_fr"] = art or d.get("article_fr", "")
        else:
            tr = {l: f.get("traduction" if l == "fr" else "traduction_" + l) for l in LANGUES_APP}
            if sorte == "nom" and not d.get("article_fr"):
                art, tr["fr"] = _article(tr["fr"] or "")
                d["article_fr"] = art
        d["corpus"] = True
        d["source_corpus"] = "%s %s" % (h["fichier"], h["ou"])
    else:
        sorte = {"nom": "nom", "verbe": "verbe", "adjectif": "adjectif", "expression": "expression"}[typ]
        d.update({"sorte": sorte, "mot": e["mot"]})
        tr = dict(zip(ORDRE_SOURCE, e["trad"]))
        if sorte == "nom":
            art, tr["fr"] = _article(tr["fr"])
            g = e["genre"]
            d.update({"genre": "die" if g == "die (Pl.)" else g, "pluriel": e["pluriel"], "article_fr": art})
            if e.get("feminin"):
                d["feminin"] = e["feminin"]
            if e.get("masculin"):
                d["masculin"] = e["masculin"]
        d["corpus"] = False
        if e.get("sens_distinct"):
            d["sens_distinct"] = e["sens_distinct"]
    if sorte == "verbe":
        d["perfekt"] = _perfekt(e)
    exemple_de = noms(e["ex"][0], "de")
    d["exemple"] = exemple_de
    d["trad"] = _trad(tr, e["ex"])
    if exemple_de in lectures:
        d["lecture"] = lectures[exemple_de]
    if d["mot"] in lectures:
        d["lecture_mot"] = lectures[d["mot"]]
    d["relire"] = ("⚕️ " + e["note"]) if (e.get("relire") and e.get("note")) else ("⚕️ à valider" if e.get("relire") else "")
    return d


def _lectures(m):
    return {noms(k, "de"): noms(v, "de") for k, v in getattr(m, "LECTURES", {}).items()}


def theme_soins(nom_module):
    """(THEME, MOTS) au format de pflege/FORMAT-DONNEES.md, § 1, pour pflege/sources/<theme>.py."""
    m = charger(nom_module)
    T = m.THEME
    titre = dict(zip(ORDRE_SOURCE, [x.strip() for x in T["titre"].split("|")]))
    fr = titre["fr"][:1].upper() + titre["fr"][1:]
    theme = {
        "base": "soins_" + T["cle"],
        "nom_theme": T["nom_theme"],
        "nom_theme_fr": fr,
        "nom_theme_trad": {l: (titre[l][:1].upper() + titre[l][1:]) for l in LANGUES_APP},
        "svg": ICONES[T["cle"]],
    }
    lect = _lectures(m)
    return theme, [convertir(e, lect) for e in m.MOTS]


def mots_ajoutes(nom_module, deja):
    """Les entrees de nom_module absentes de « deja » (une liste MOTS existante), a mettre A LA FIN."""
    m = charger(nom_module)
    vus = set()
    for x in deja:
        vus.add(corpus.cle(x["mot"] if isinstance(x, dict) else x[2], garder_sich=True))
    lect = _lectures(m)
    out = []
    for e in m.MOTS:
        d = convertir(e, lect)
        if corpus.cle(d["mot"], garder_sich=True) not in vus:
            out.append(d)
    return out
