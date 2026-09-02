# -*- coding: utf-8 -*-
"""Configuration d'une langue d'interface, et lecture du corpus dans cette langue.

TOUT CE QUI DEPEND DE LA LANGUE EST ICI, ET NULLE PART AILLEURS. Les trois
outils de relecture -- relecture_langue.py, patch_langue.py, contraste_deepl.py --
importent ce module et ne connaissent plus le turc.

POURQUOI CE MODULE EXISTE. La chaine a ete ecrite pour le turc, avec le suffixe
`_tr` en dur a une trentaine d'endroits. Au moment d'ajouter l'ukrainien, le
reflexe est de copier les trois fichiers et de remplacer `tr` par `uk` : on se
retrouve alors avec six fichiers, et chaque correction est a faire deux fois.
La journee du 2 septembre a produit une dizaine de corrections dans ces outils
-- le garde-fou du saut de ligne final, les occurrences multiples d'un mot, les
champs de temps des verbes, les paires de genre, les collisions acceptees. Six
fichiers auraient voulu dire dix corrections en double, et une divergence
silencieuse des la premiere oubliee.

AJOUTER UNE LANGUE = UNE LIGNE DANS `LANGUES`. Rien d'autre, tant que les JSON
suivent la convention `traduction_<code>` / `exemple_<code>`.
"""
import io
import json
import os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# code : (nom lisible, code source DeepL)
#
# Le code sert de SUFFIXE dans les JSON (`traduction_tr`, `exemple_uk`...), de
# nom de dossier (`relecture_uk/`, `corrections_uk/`) et de langue source pour
# la traduction inverse. Les trois suivent, il n'y a rien a synchroniser.
LANGUES = {
    "tr": ("turc", "TR"),
    "uk": ("ukrainien", "UK"),
    "ru": ("russe", "RU"),
    "pl": ("polonais", "PL"),
    "ro": ("roumain", "RO"),
    "ar": ("arabe", "AR"),
}

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]

# Les quatre temps d'une carte de verbe. Le libelle est montre au relecteur ;
# le champ sert a nommer la colonne dans un signalement (`perfekt_uk`).
TEMPS_VERBE = [
    ("exemple", "Präsens"),
    ("perfekt", "Perfekt"),
    ("praeteritum", "Präteritum"),
    ("konjunktiv2", "Konjunktiv II"),
]

# Quel fichier porte quelle categorie, et sous quelle cle le mot allemand s'y
# trouve. C'est la seule table qui connaisse la forme des cinq JSON.
FICHIERS = {
    "noms":        ("themes.json",      "mot"),
    "verbes":      ("verbe.json",       "infinitif"),
    "adjectifs":   ("adjectif.json",    "mot"),
    "adverbes":    ("adverbe.json",     "mot"),
    "expressions": ("redewendung.json", "mot"),
}

VERS_CATEGORIE = {f: c for c, (f, _) in FICHIERS.items()}


class Langue(object):
    def __init__(self, code):
        if code not in LANGUES:
            raise ValueError("langue inconnue : %s (connues : %s)"
                             % (code, ", ".join(sorted(LANGUES))))
        self.code = code
        self.nom, self.deepl = LANGUES[code]

    # -- les noms de champs et de dossiers ---------------------------------
    def champ(self, base):
        """`traduction` -> `traduction_uk`."""
        return "%s_%s" % (base, self.code)

    @property
    def sortie(self):
        return os.path.join(RACINE, "relecture_%s" % self.code)

    @property
    def corrections(self):
        return os.path.join(RACINE, "corrections_%s" % self.code)

    # -- la lecture du corpus ----------------------------------------------
    def _charger(self, nom):
        return json.load(io.open(os.path.join(RACINE, nom), encoding="utf-8"))

    def cartes_noms(self):
        d = self._charger("themes.json")
        out = []
        for t in d.get("themes", d):
            for m in t.get("mots", []):
                out.append({
                    "cle": m.get("mot"),
                    "niveau": t.get("niveau"),
                    "theme": t.get("nom_theme"),
                    "allemand": ((m.get("genre") or "") + " " + (m.get("mot") or "")).strip(),
                    "sens_fr": m.get("traduction"),
                    "cible": m.get(self.champ("traduction")),
                    "phrase_de": m.get("exemple"),
                    "phrase_fr": m.get("exemple_fr"),
                    "phrase_cible": m.get(self.champ("exemple")),
                })
        return out

    def cartes_simples(self, fichier):
        d = self._charger(fichier)
        out = []
        for niveau in NIVEAUX:
            for m in d.get(niveau, []):
                out.append({
                    "cle": m.get("mot"),
                    "niveau": niveau,
                    "allemand": m.get("mot"),
                    "sens_fr": m.get("traduction"),
                    "cible": m.get(self.champ("traduction")),
                    "phrase_de": m.get("exemple"),
                    "phrase_fr": m.get("exemple_fr"),
                    "phrase_cible": m.get(self.champ("exemple")),
                })
        return out

    def cartes_verbes(self):
        """Un verbe porte quatre temps, chacun avec sa phrase.

        On les soumet tous : c'est la que se cachent les erreurs de temps et
        d'aspect, qu'aucune langue ne rend comme l'allemand.
        """
        d = self._charger("verbe.json")
        out = []
        for niveau in NIVEAUX:
            for v in d.get(niveau, []):
                phrases = []
                for champ, libelle in TEMPS_VERBE:
                    if not v.get(champ):
                        continue
                    phrases.append({
                        "temps": libelle,
                        "champ": champ,
                        "de": v.get(champ),
                        "fr": v.get(champ + "_fr"),
                        "cible": v.get(self.champ(champ)),
                    })
                out.append({
                    "cle": v.get("infinitif"),
                    "niveau": niveau,
                    "allemand": v.get("infinitif"),
                    "sens_fr": v.get("traduction"),
                    "cible": v.get(self.champ("traduction")),
                    "phrases": phrases,
                })
        return out

    def categories(self):
        return {
            "noms": self.cartes_noms,
            "verbes": self.cartes_verbes,
            "adjectifs": lambda: self.cartes_simples("adjectif.json"),
            "adverbes": lambda: self.cartes_simples("adverbe.json"),
            "expressions": lambda: self.cartes_simples("redewendung.json"),
        }

    def toutes_les_cartes(self):
        return {nom: fn() for nom, fn in self.categories().items()}


def depuis_arguments(args, defaut="tr"):
    """`--langue uk` dans la ligne de commande, sinon le defaut.

    Le defaut reste le turc : c'est la seule langue deja traitee, et une
    commande tapee de memoire ne doit pas se tromper de corpus en silence.
    """
    for i, a in enumerate(args):
        if a == "--langue" and i + 1 < len(args):
            return Langue(args[i + 1].strip().lower())
    return Langue(defaut)
