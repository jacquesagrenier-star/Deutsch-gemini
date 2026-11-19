# -*- coding: utf-8 -*-
"""Ce que partagent les generateurs des themes illustres des Soins (pflege/outils/themes_soins/<cle>.py).

UN GENERATEUR fabrique, depuis ses donnees, la BANQUE de questions d'un theme et toutes ses phrases allemandes, puis
ecrit visuel/prototype/soins-theme-<cle>/donnees.json, que lit la page (visuel/prototype/themes/soins.js). Les phrases
ne sont jamais ecrites a la main : elles sortent de gabarits remplis par les donnees (personnes, parties du corps,
valeurs...). Le francais de chaque phrase sort des memes gabarits ; les huit autres langues d'interface (en es pt tr
uk pl ru ar fa) viennent de pflege/sources/themes_soins/<cle>/<langue>.json, traduits et relus a part :
  {"textes": {cle: traduction}, "phrases": {phrase allemande: traduction}, "mots": {mot affiche: traduction}}
Une entree qui manque y est ajoutee VIDE a chaque passage (le traducteur la remplit), et le rapport la compte : la
page n'est publiee qu'a zero manque. Les mots prennent leur traduction dans le corpus des Soins
(pflege/datos/themes.json) ; l'espagnol, que ce corpus n'a pas encore, vient du fichier de la langue (cle « mots »).

Regle 4 du contrat (pflege/FORMAT-DONNEES.md) : aucun chiffre dans un texte allemand dit a voix haute. Le generateur
s'arrete sur un chiffre dans une phrase, une reponse ou un mot dit.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
LANGUES = ["fr", "en", "es", "pt", "tr", "uk", "pl", "ru", "ar", "fa"]
TRADUITES = [l for l in LANGUES if l != "fr"]          # les langues des fichiers de traduction


def lire_json(chemin):
    return json.load(io.open(chemin, encoding="utf-8"))


def ecrire_json(chemin, d, indent=1):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=indent) + "\n")


def corpus_soins():
    """{mot affiche (« die Hüfte », « stechend »): entree du corpus, avec « theme » (l'id du theme de soins)}.
    Un mot present deux fois (« die Atemnot » : un nom du corps ET une paire patient / service) garde sa premiere
    entree ici ; la paire se trouve aussi sous « paire:<mot> »."""
    idx = {}
    for t in lire_json(os.path.join(RACINE, "pflege", "datos", "themes.json"))["themes"]:
        for m in t["mots"]:
            cle = ((m.get("genre") + " ") if m.get("genre") else "") + m["mot"]
            idx.setdefault(cle, dict(m, theme=t["id"]))
            if m.get("sorte") == "paire":
                idx.setdefault("paire:" + cle, dict(m, theme=t["id"]))
    return idx


def corpus_general():
    """Le corpus general (themes.json a la racine) : un mot courant (die Brille, der Koffer) qu'il connait, avec sa
    traduction dans les dix langues ; l'app le trouve dans ses cartes ordinaires (pas de theme de soins)."""
    idx = {}
    for t in lire_json(os.path.join(RACINE, "themes.json"))["themes"]:
        for m in t["mots"]:
            cle = ((m.get("genre") + " ") if m.get("genre") else "") + m["mot"]
            idx.setdefault(cle, dict(m, theme=None, sorte="nom" if m.get("genre") else m.get("sorte", "nom")))
    return idx


CAT = {"nom": None, "adjectif": "adjectif", "verbe": "verbe", "adverbe": "adverbe", "expression": None, "paire": None}


def mot_du_corpus(corpus, affiche, dit=None):
    """Un mot du theme, a la forme du corpus, avec sa traduction dans les langues du corpus (l'espagnol a part)."""
    if affiche.startswith("verbe:"):
        inf = affiche.split(":", 1)[1]
        v = next((e for n in lire_json(os.path.join(RACINE, "verbe.json")).values() for e in n if e["infinitif"] == inf), None)
        if not v:
            sys.exit("verbe absent de verbe.json : " + inf)
        glose = {l: v.get("traduction" if l == "fr" else "traduction_" + l) for l in LANGUES if v.get("traduction" if l == "fr" else "traduction_" + l)}
        out = {"mot": inf, "genre": None, "cat": "verbe", "theme": None, "affiche": inf, "glose": glose}
        if dit:
            out["dit"] = dit
        return out
    if affiche not in corpus:
        global _GENERAL
        if _GENERAL is None:
            _GENERAL = corpus_general()
        if affiche not in _GENERAL:
            sys.exit("mot absent des corpus (Soins et general) : %s (le demander a la session vocabulaire)" % affiche)
        m = _GENERAL[affiche]
    else:
        m = corpus[affiche]
    affiche = affiche.split(":", 1)[-1]
    glose = {"fr": ((m.get("article_fr") or "") + m.get("traduction", "")).strip()}
    for l in LANGUES[1:]:
        if m.get("traduction_" + l):
            glose[l] = m["traduction_" + l]
    out = {"mot": m["mot"], "genre": m.get("genre") or None, "cat": CAT.get(m.get("sorte")), "theme": m["theme"],
           "affiche": affiche, "glose": glose}
    if dit:
        out["dit"] = dit
    return out


_GENERAL = None
CHIFFRE = re.compile(r"\d")


def sans_chiffre(texte, ou):
    if texte and CHIFFRE.search(texte):
        sys.exit("un chiffre dans l'allemand dit (regle 4) -- %s : %s" % (ou, texte))


class Theme:
    """Rassemble les mots, les questions, les phrases (avec leur francais) et les textes d'un theme, puis les ecrit."""

    def __init__(self, cle):
        self.cle = cle
        self.corpus = corpus_soins()
        self.mots, self.rang = [], {}
        self.questions = []
        self.phrases_fr = {}          # phrase allemande -> francais
        self.textes_fr = {}           # cle -> francais
        self.gloses_fr = {}           # texte allemand d'un choix -> francais (le mot choisi, apres une erreur)
        self.gloses_partout = {}      # ... la meme dans toutes les langues (un chiffre)
        self.phrases_faites = {}      # phrase allemande -> {langue: traduction} deja faite (les dialogues)
        self.decouverte = []
        self.images = {}

    # --- les mots
    def mot(self, affiche, dit=None):
        """affiche : « die Hüfte » ; « paire:die Atemnot » prend l'entree « paire » d'un mot present deux fois."""
        if affiche not in self.rang:
            self.rang[affiche] = len(self.mots)
            self.mots.append(mot_du_corpus(self.corpus, affiche, dit))
        return self.rang[affiche]

    # --- les phrases et leur francais
    def phrase(self, de, fr, trad=None):
        """trad : les traductions deja faites (une replique de dialogue, traduite et relue avec lui) : rien a traduire."""
        sans_chiffre(de, "phrase")
        if trad:
            self.phrases_faites[de] = dict(trad)
        if de in self.phrases_fr and self.phrases_fr[de] != fr:
            sys.exit("une phrase, deux francais : %s (%s / %s)" % (de, self.phrases_fr[de], fr))
        self.phrases_fr[de] = fr
        return de

    def texte(self, cle, fr):
        self.textes_fr[cle] = fr

    def glose(self, de, fr, partout=False):
        """La traduction d'un choix (le mot choisi, apres une erreur) ; partout : la meme dans toutes les langues (un nombre)."""
        self.gloses_fr[de] = fr
        if partout:
            self.gloses_partout[de] = fr

    def image(self, nom, alt, **extra):
        self.images[nom] = dict(alt=alt, **extra)

    # --- une question de la banque
    def question(self, sorte, mot, consigne, bonne, phrase, choix=None, images=None, visuel=None, enonce=None,
                 ecoute=None, dit=None, centre=False, ordre_fixe=False, bonne_texte=None, aide=None):
        """aide : la cle d'un texte (T.texte) qui explique la faute, montre apres la reponse."""
        for t in [phrase, bonne if images is None else None, ecoute, dit] + (choix or []):
            sans_chiffre(t, "%s/%s" % (self.cle, sorte))
        if choix is not None:
            if bonne not in choix or len(set(choix)) != len(choix) or len(choix) < 2:
                sys.exit("choix faux ou en double -- %s : %s / %s" % (sorte, bonne, choix))
        if images is not None and (bonne not in images or len(set(images)) != len(images)):
            sys.exit("images fausses ou en double -- %s : %s / %s" % (sorte, bonne, images))
        if phrase not in self.phrases_fr:
            sys.exit("phrase sans francais -- %s : %s" % (sorte, phrase))
        q = {"id": "%s%d" % (sorte[:3], len(self.questions)), "sorte": sorte, "mot": mot, "consigne": consigne,
             "bonne": bonne, "phrase": phrase}
        for k, v in (("choix", choix), ("images", images), ("visuel", visuel), ("enonce", enonce), ("ecoute", ecoute),
                     ("dit", dit), ("bonneTexte", bonne_texte), ("aide", aide)):
            if v is not None:
                q[k] = v
        if centre:
            q["centre"] = True
        if ordre_fixe:
            q["ordreFixe"] = True
        if any(self._meme(q, x) for x in self.questions):
            return None
        self.questions.append(q)
        return q

    @staticmethod
    def _meme(a, b):
        cles = ("sorte", "mot", "bonne", "phrase", "enonce", "visuel", "ecoute")
        return all(a.get(k) == b.get(k) for k in cles) and sorted(a.get("choix") or a.get("images") or []) == sorted(b.get("choix") or b.get("images") or [])

    # --- l'ecriture
    def ecrire(self, extra=None):
        src = os.path.join(RACINE, "pflege", "sources", "themes_soins", self.cle)
        manques = {}
        phrases = {p: {"fr": fr} for p, fr in self.phrases_fr.items()}
        textes = {k: {"fr": fr} for k, fr in self.textes_fr.items()}
        gloses = {g: {"fr": fr} for g, fr in self.gloses_fr.items()}
        for l in TRADUITES:
            chemin = os.path.join(src, l + ".json")
            tr = lire_json(chemin) if os.path.exists(chemin) else {}
            a_traduire = {k: v for k, v in self.gloses_fr.items() if k not in self.gloses_partout}
            a_faire = {k: v for k, v in self.phrases_fr.items() if not self.phrases_faites.get(k, {}).get(l)}
            for groupe, attendu in (("textes", self.textes_fr), ("phrases", a_faire), ("gloses", a_traduire),
                                    ("mots", {m["affiche"]: m["glose"]["fr"] for m in self.mots if l not in m["glose"]})):
                g = tr.setdefault(groupe, {})
                for k in attendu:
                    g.setdefault(k, "")
                # une entree qui ne sert plus est retiree (une phrase changee laisse sa traduction perimee)
                for k in [k for k in g if k not in attendu]:
                    del g[k]
            # le francais a cote, pour le traducteur
            tr["_francais"] = {"textes": self.textes_fr, "phrases": a_faire, "gloses": a_traduire}
            # reecrit seulement si quelque chose a change : plusieurs traducteurs travaillent en meme temps, chacun
            # sur sa langue, et chacun relance ce generateur
            avant = lire_json(chemin) if os.path.exists(chemin) else None
            if tr != avant:
                ecrire_json(chemin, tr)
            n = 0
            for k, v in tr["textes"].items():
                if v: textes[k][l] = v
                else: n += 1
            for k, v in tr["phrases"].items():
                if v: phrases[k][l] = v
                else: n += 1
            for k, d in self.phrases_faites.items():
                if d.get(l):
                    phrases[k][l] = d[l]
            for k, v in tr["gloses"].items():
                if v: gloses[k][l] = v
                else: n += 1
            for k, v in self.gloses_partout.items():
                gloses[k][l] = v
            for m in self.mots:
                v = tr["mots"].get(m["affiche"])
                if l not in m["glose"]:
                    if v: m["glose"][l] = v
                    else: n += 1
            manques[l] = n
        sortie = {"_lisez_moi": "DERIVE de pflege/outils/themes_soins/%s.py (et des traductions de pflege/sources/themes_soins/%s/) : "
                                "ne pas corriger a la main." % (self.cle, self.cle),
                  "cle": self.cle, "textes": textes, "mots": self.mots, "questions": self.questions,
                  "phrases": phrases, "gloses": gloses, "images": self.images, "decouverte": self.decouverte}
        sortie.update(extra or {})
        ecrire_json(os.path.join(RACINE, "visuel", "prototype", "soins-theme-" + self.cle, "donnees.json"), sortie, indent=None)
        # le rapport
        par_sorte = {}
        for q in self.questions:
            par_sorte[q["sorte"]] = par_sorte.get(q["sorte"], 0) + 1
        sortes_du_mot = {}
        for q in self.questions:
            sortes_du_mot.setdefault(q["mot"], set()).add(q["sorte"])
        seuls = [self.mots[i]["affiche"] for i, s in sortes_du_mot.items() if len(s) < 2]
        sans_q = [m["affiche"] for i, m in enumerate(self.mots) if i not in sortes_du_mot]
        print("soins-theme-%s : %d mots, %d questions (%s), %d phrases, %d images"
              % (self.cle, len(self.mots), len(self.questions), ", ".join("%s %d" % kv for kv in sorted(par_sorte.items())),
                 len(self.phrases_fr), len(self.images)))
        print("  traductions manquantes : " + ", ".join("%s %d" % (l, manques[l]) for l in TRADUITES))
        if seuls:
            print("  ⚠ mots a une seule sorte : " + ", ".join(seuls))
        if sans_q:
            print("  ⚠ mots sans question : " + ", ".join(sans_q))
        if len(self.questions) < 100:
            print("  ⚠ moins de 100 questions")
        return manques
