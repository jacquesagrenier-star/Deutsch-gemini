# -*- coding: utf-8 -*-
"""Inventaire mesure de ce qui est encore allemand dans index.html.

Chaque ligne du tableau produit = un motif grep, le nombre de LIGNES
d'index.html qui le contiennent, et les premiers numeros de ligne. Les motifs
sont ecrits pour etre relances tels quels avec `grep -c` (syntaxe ERE).

    python japonais/moteur/inventaire.py            # tableau Markdown
    python japonais/moteur/inventaire.py --json     # meme chose en JSON

Classement (voir CONCEPTION.md, section 1) :
  a  deja parametre par LANGUE_ENSEIGNEE / urlDonnees / ASSETS_BASE
  b  propre a l'allemand : une autre langue doit le DESACTIVER (capacite)
  c  mecanisme general ecrit en dur pour l'allemand : a GENERALISER

Bibliotheque standard seulement. Ne modifie rien.
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (classe, sujet, motif ERE, commentaire)
MOTIFS = [
    # ---- a : deja parametre -------------------------------------------------
    ("a", "Table de la langue enseignee", r"LANGUE_ENSEIGNEE", "code, nom, voix, donnees, audio"),
    ("a", "Adresse des donnees", r"urlDonnees\(", "12 fetch + la definition + 1 commentaire"),
    ("a", "Ressources de la marque", r"ASSETS_BASE", "logo, videos : pas de la langue"),
    ("a", "Prefixe de progression", r"prefixeLangue\(", "vide pour l'allemand, voulu"),
    ("a", "Cle de progression par theme", r"progressKey\(", ""),
    ("a", "Cle de progression globale", r"directionScopedKey\(", "serie, objectif, XP"),
    ("a", "Jeux d'exercices sortis", r"exercices\.json", "v392, goulot startExerciseSet"),
    ("a", "Ecrans de grammaire sortis", r"grammaire\.json", "v393"),
    ("a", "Base audio", r"AUDIO_BASE", "= LANGUE_ENSEIGNEE.audio"),
    # ---- b : propre a l'allemand ---------------------------------------------
    ("b", "Tuiles d'accueil allemandes", r'class="orb orb-de"', "15 tuiles, cachees par CSS en direction en"),
    ("b", "Panneaux de tuile", r'if\(id === "[a-z0-9]+"\)\{', "orbPanelData() : 17 panneaux"),
    ("b", "Exercices allemands (start...Uebung/Exercise)", r"^function start[A-Za-z]*(Uebung|Exercise|Exercises)\(", ""),
    ("b", "Ecrans d'explication (open...Info)", r"^function open[A-Za-z]*Info\(", "16 ecrans"),
    ("b", "Cas grammaticaux", r"Akkusativ|Dativ|Genitiv|Nominativ", "lignes, I18N compris"),
    ("b", "Articles der/die/das", r"\"der\"|'der'|der/die/das|=== \"die\"|=== \"das\"", ""),
    ("b", "Quiz d'article", r"startQuizArticle|startDerEinUebung", ""),
    ("b", "Couleur de l'article (decouverte)", r"couleur de l'article|trois couleurs d'article|La couleur dit l'article", ""),
    ("b", "Konjunktiv II", r"[Kk]onjunktiv", ""),
    ("b", "Temps allemands (Praesens/Perfekt/Praeteritum)", r"praesens|perfekt|praeteritum", "champs de verbe.json"),
    ("b", "Rection / verbes a cas", r"rektion|kasusverben|kasusVerb", ""),
    ("b", "Verbes separables / zu-Infinitiv", r"zuinf_separable|zuInfinitiv|zuinfinitiv", ""),
    ("b", "Examens (pruefung, Goethe, telc, DTZ)", r"[Pp]ruefung|Goethe|telc|\bdtz\b|DTZ", ""),
    ("b", "Chapitres VHS (manuel de cours allemand)", r"vhs|VHS", "acces par compte"),
    ("b", "Declinaison de l'adjectif", r"adjektiveDeklination|Deklination", ""),
    ("b", "Ordre des mots allemand", r"[Ww]ortstellung|tekamolo|Tekamolo", ""),
    # ---- c : general mais ecrit en dur ---------------------------------------
    ("c", "Niveaux CECR en dur", r'\["A1", "A2"|\["A2", "B1"', "tableaux litteraux"),
    ("c", "Constantes de niveaux", r"NIVEAUX_CECR|NIVEAUX_VOCAB|\bLEVELS\b", ""),
    ("c", "Lettres de niveau regexp", r"a1\|a2\|b1\|b2\|c1", "suffixes d'id de theme"),
    ("c", "Mode de carte (flashcardMode ===)", r"flashcardMode *=== *['\"]", "une branche par forme de carte"),
    ("c", "Rangs de tuple lus dans loadFlashcard (card[N])", r"card\[[0-9]+\]", ""),
    ("c", "Rangs de tuple, tout le fichier (w/word/card/e/c[N])", r"\b(w|word|mot|entry|e|card|c)\[[0-9]+\]", ""),
    ("c", "Champs de traduction par langue (traduction_xx)", r"traduction_(en|tr|uk|fa|ar)", "une colonne par langue d'interface"),
    ("c", "Voix allemande nommee", r"findGermanVoice\(", "= pickVoice(LANGUE_ENSEIGNEE.code)"),
    ("c", "Lecture de la langue enseignee", r"direAllemand\(", "15 appels, nom allemand"),
    ("c", "Empreinte audio sans marque de langue", r"sha1Hex\(|empreinteAudio\(", "sha1(texte) seul"),
    ("c", "Direction FR<->DE de la carte", r"frontIsFrench", ""),
    ("c", "Direction anglaise (module en)", r"=== *['\"]en['\"]", "dir === 'en' et voisins"),
    ("c", "Progression allemande forcee", r"withGermanProgress", ""),
    ("c", "Cle de mot = position (CLES_STABLES)", r"CLES_STABLES|cleMot\(", "seuls les verbes ont une cle stable"),
    ("c", "Frequence (frequence.json)", r"[Ff]requence", "rang par chaine de caracteres"),
    ("c", "Nom unique d'un mot de carte", r"motDeLaCarte\(", "w[0] ou w.infinitif ou w.mot"),
    ("c", "Mot 'allemand' dans le code et l'I18N", r"allemand|Allemand", "lignes, I18N compris"),
]


def compter(lignes, motif):
    rx = re.compile(motif)
    nums = [i + 1 for i, l in enumerate(lignes) if rx.search(l)]
    return nums


def main():
    chemin = os.path.join(RACINE, "index.html")
    with open(chemin, encoding="utf-8", newline="") as f:
        lignes = f.read().replace("\r\n", "\n").split("\n")
    res = []
    for classe, sujet, motif, note in MOTIFS:
        nums = compter(lignes, motif)
        res.append({"classe": classe, "sujet": sujet, "motif": motif,
                    "lignes": len(nums), "premieres": nums[:4], "note": note})
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return
    print("index.html : %d lignes\n" % len(lignes))
    print("| cl. | sujet | lignes | premieres lignes | motif (grep -cE) | note |")
    print("|---|---|---:|---|---|---|")
    for r in res:
        print("| %s | %s | %d | %s | `%s` | %s |" % (
            r["classe"], r["sujet"], r["lignes"],
            ", ".join(str(n) for n in r["premieres"]),
            r["motif"].replace("|", "\\|"), r["note"]))


if __name__ == "__main__":
    main()
