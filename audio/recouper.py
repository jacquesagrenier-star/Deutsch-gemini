# -*- coding: utf-8 -*-
"""Extrait le dernier mot d'une phrase porteuse, sans l'ecouter.

    python audio/recouper.py fichier.mp3 sortie.mp3
    python audio/recouper.py --dossier audio/essai_prononciation --motif "*_5_*"

POURQUOI CE DECOUPAGE EXISTE. `eleven_multilingual_v2` deduit la langue du
texte qu'on lui envoie. Sur un mot court et isole -- « neu », « jung » -- il n'a
presque rien pour la deduire et lit a la francaise. Verifie a l'oreille le
3 septembre 2026 : le meme mot place dans une phrase allemande sort juste. On
genere donc « Man sagt: neu. » et on ne garde que « neu ».

COMMENT ON TROUVE LE MOT SANS L'ENTENDRE. La porteuse se termine par le mot,
precede d'une pause (les deux points) et suivi du silence de fin. ffmpeg sait
reperer ces silences. Le dernier segment de parole EST le mot.

LES TROIS GARDE-FOUS, ET POURQUOI ILS NE SONT PAS DECORATIFS. Je ne peux pas
ecouter ce que je decoupe. Un decoupage rate ne se voit pas : il produit un
fichier parfaitement valide qui dit « man » au lieu de « neu », ou un mot dont
l'attaque est rognee. Les trois controles ci-dessous sont donc la seule chose
qui separe une chaine sure d'une chaine qui abime 500 fichiers en silence.

  1. Il faut AU MOINS DEUX segments de parole. Un seul segment veut dire que
     la detection a echoue -- ou que la voix n'a pas marque la pause -- et on
     ne saurait pas ou couper.
  2. La duree du mot doit rester PLAUSIBLE : entre 0,15 et 1,60 s. En dessous,
     on a attrape une consonne ; au-dessus, on a garde une partie de la
     porteuse.
  3. Quand un ancien fichier existe pour le meme mot, la nouvelle duree doit
     rester dans une fourchette de 0,5x a 2,0x. L'ancien etait mal prononce,
     pas mal decoupe : sa duree est donc une bonne reference. C'est le controle
     le plus utile, parce qu'il est propre a CHAQUE mot.

Un fichier qui echoue a l'un des trois n'est pas ecrit : il est SIGNALE. Mieux
vaut vingt mots a reprendre a la main qu'un seul mot faux qui passe.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MARGE_AVANT = 0.040     # s, pour ne pas rogner l'attaque
MARGE_APRES = 0.060     # s, pour laisser la chute naturelle
FONDU = 0.010           # s, contre le clic de coupe
# LES BORNES DEPENDENT DU NOMBRE DE MOTS, pas d'une constante. Le corpus
# ne contient pas que des mots : « Alles Gute zum Geburtstag » est une
# entree a part entiere et dure legitimement deux secondes. Une borne fixe
# a 1,60 s la refusait, ainsi que dix autres expressions -- non parce que
# la coupe etait mauvaise, mais parce que la regle etait ecrite pour des
# mots isoles.
MIN_MOT = 0.12          # « doch » fait 0,14 s : la borne etait trop haute
MAX_BASE = 0.80         # le socle : attaque, chute, marges
MAX_PAR_SIGNE = 0.11    # ce que coute une lettre de plus, en secondes
SEUIL_SILENCE = "-38dB"
DUREE_SILENCE = 0.10


class Refus(Exception):
    pass


def duree(chemin):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", chemin],
        capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def segments_parole(chemin):
    """Les intervalles de parole, deduits des silences reperes par ffmpeg."""
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", chemin, "-af",
         "silencedetect=noise=%s:d=%s" % (SEUIL_SILENCE, DUREE_SILENCE),
         "-f", "null", "-"],
        capture_output=True, text=True)
    journal = r.stderr
    debuts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", journal)]
    fins = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", journal)]
    total = duree(chemin)

    # La parole occupe ce qui reste entre les silences.
    bornes = sorted([(f, "debut") for f in fins] + [(d, "fin") for d in debuts])
    segments, ouvert = [], 0.0 if not fins or fins[0] > 0.001 else None
    for t, quoi in bornes:
        if quoi == "debut":
            ouvert = t
        elif ouvert is not None:
            if t - ouvert > 0.02:
                segments.append((ouvert, t))
            ouvert = None
    if ouvert is not None and total - ouvert > 0.02:
        segments.append((ouvert, total))
    return segments


def parole_totale(chemin):
    """Du debut du premier son a la fin du dernier -- le silence exclu.

    C'EST CETTE MESURE QU'IL FAUT COMPARER, PAS LA DUREE DU FICHIER. Un mot
    genere seul par ElevenLabs arrive avec environ 0,4 s de silence autour :
    « Bank » fait 0,79 s de fichier pour 0,31 s de parole. Comparer un mot
    recoupe serre a ce total-la, c'est mesurer du silence -- et refuser des
    coupes parfaitement bonnes. C'est l'erreur qui a fait rejeter 26 mots
    sur 40 au premier essai.
    """
    segs = segments_parole(chemin)
    return (segs[-1][1] - segs[0][0]) if segs else 0.0


# ABAISSE DE 0,18 A 0,12 LE 4 SEPTEMBRE 2026, avec le passage a la voix Aurora.
#
# 0,18 s etait juste pour Nadja, qui marquait une pause nette apres « Wort: ».
# Aurora enchaine plus fluidement : sur 105 mots isoles, le plus grand ecart
# tombait entre 0,10 et 0,18 s, et le decoupage refusait TOUT -- 0 reussite sur
# 105. Un seuil regle pour une voix ne vaut pas pour une autre.
#
# Mesure des paliers, sur les enregistrements deja payes des mots refuses :
#   0,18 s -> 0 %   |   0,15 s -> 61 %   |   0,14 s -> 78 %   |   0,12 s -> 92 %
#
# 0,12 retenu apres ECOUTE de six coupes par Jacques -- Adresse, Apotheke,
# Banane, Bank, Bar, Beruf : mot entier, pas de reste de porteuse. C'est la
# seule verification qui vaille, le reste n'est que de l'arithmetique.
#
# Les deux autres garde-fous sont INCHANGES et c'est ce qui rend l'abaissement
# supportable : la pause retenue doit toujours dominer les autres d'un facteur
# 1,5, et la duree du mot doit rester plausible.
ECART_MIN = 0.12        # s, en deca ce n'est pas une pause mais une consonne
ECART_RAPPORT = 1.5     # la vraie pause doit dominer nettement les autres


def bornes(texte):
    """Les durees plausibles, deduites de la LONGUEUR du texte.

    Compter les mots ne suffisait pas : l'allemand soude ses nombres, et
    « neunzehnhundertneunundachtzig » est UN mot de 29 lettres qui dure
    legitimement 2,5 s. La longueur en signes predit la duree bien mieux
    que le nombre d'espaces -- c'est d'ailleurs le meme raisonnement que
    celui de controler.py sur la taille des fichiers.
    """
    n = len(texte or "xxx")
    return MIN_MOT, MAX_BASE + MAX_PAR_SIGNE * n


def recouper(source, destination, reference=None, texte=None):
    """Coupe au PLUS GRAND ECART, pas au dernier segment.

    LA PREMIERE VERSION COMPTAIT LES SEGMENTS, et elle a refuse 24 mots sur
    149 : « Abfall », « Bett », « Brot »... Un mot qui contient une occlusive
    -- p, t, k -- porte un micro-silence a l'interieur, que ffmpeg compte comme
    un silence de plus. Pire, sur « Wort: Bett. » c'est « Wort » LUI-MEME qui
    se fend sur son t final : ecarts 0,103 / 0,378 / 0,121. Le dernier segment
    n'y est plus le mot, mais sa derniere consonne.

    Ce qui distingue vraiment la porteuse du mot, c'est la pause des deux
    points : 0,38 s la ou une occlusion en vaut 0,10. On coupe donc au plus
    grand ecart, et tout ce qui suit est le mot -- ce qui rattrape du meme coup
    les entrees de plusieurs mots (« Danke, gut »), dont la virgule interne
    n'est jamais le plus grand ecart.
    """
    segs = segments_parole(source)
    if len(segs) < 2:
        raise Refus("%d segment(s) de parole -- impossible de situer le mot"
                    % len(segs))

    ecarts = [segs[i + 1][0] - segs[i][1] for i in range(len(segs) - 1)]
    coupe = max(range(len(ecarts)), key=lambda i: ecarts[i])
    plus_grand = ecarts[coupe]
    autres = sorted((e for i, e in enumerate(ecarts) if i != coupe), reverse=True)

    if plus_grand < ECART_MIN:
        raise Refus("plus grand ecart de %.2f s -- aucune pause franche, la "
                    "porteuse et le mot ne se separent pas" % plus_grand)
    if autres and plus_grand < ECART_RAPPORT * autres[0]:
        raise Refus("ecarts %.2f et %.2f s trop proches -- on ne sait pas "
                    "lequel separe la porteuse du mot" % (plus_grand, autres[0]))

    debut, fin = segs[coupe + 1][0], segs[-1][1]
    longueur = fin - debut
    bas, haut = bornes(texte)
    if not (bas <= longueur <= haut):
        raise Refus("segment de %.2f s, hors des bornes %.2f-%.2f pour "
                    "%d signe(s)" % (longueur, bas, haut, len(texte or "xxx")))
    if reference and os.path.exists(reference):
        ref = parole_totale(reference)
        # La borne basse est a 0,45 et non 0,5 : dans la porteuse le mot est
        # dit un peu plus vite que seul, ou il portait un accent d'insistance.
        # Un ecart d'un tiers est donc normal, pas suspect.
        if ref > 0 and not (0.45 * ref <= longueur <= 2.0 * ref):
            raise Refus("%.2f s de parole contre %.2f s dans l'ancien fichier "
                        "(hors 0,45x-2,0x)" % (longueur, ref))

    a = max(0.0, debut - MARGE_AVANT)
    b = fin + MARGE_APRES
    duree_sortie = b - a
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-v", "error", "-y",
         "-ss", "%.3f" % a, "-to", "%.3f" % b, "-i", source,
         "-af", "afade=t=in:st=0:d=%.3f,afade=t=out:st=%.3f:d=%.3f"
                % (FONDU, max(0.0, duree_sortie - 2 * FONDU), 2 * FONDU),
         # LE FORMAT EST IMPOSE, PAS DEVINE. ffmpeg deduit normalement le
         # conteneur de l'extension ; un fichier de travail nomme « .coupe »
         # le laisse sans reponse et il s'arrete. Le dire explicitement rend
         # la fonction sure quel que soit le nom de sortie.
         "-c:a", "libmp3lame", "-b:a", "64k", "-ar", "44100", "-ac", "1",
         "-f", "mp3", destination],
        check=True, capture_output=True)
    return longueur


def main():
    p = argparse.ArgumentParser()
    p.add_argument("source", nargs="?")
    p.add_argument("destination", nargs="?")
    p.add_argument("--dossier")
    p.add_argument("--motif", default="*.mp3")
    a = p.parse_args()

    if a.dossier:
        fichiers = sorted(glob.glob(os.path.join(a.dossier, a.motif)))
        if not fichiers:
            print("  aucun fichier pour %s" % a.motif)
            return 1
        for f in fichiers:
            dest = f.replace(".mp3", "__coupe.mp3")
            try:
                n = recouper(f, dest)
                print("  + %-34s %.2f s" % (os.path.basename(dest), n))
            except Refus as err:
                print("  ! %-34s %s" % (os.path.basename(f), err))
        return 0

    if not a.source or not a.destination:
        print(__doc__)
        return 1
    try:
        n = recouper(a.source, a.destination)
        print("  + %s  %.2f s" % (a.destination, n))
        return 0
    except Refus as err:
        print("  ! %s : %s" % (a.source, err))
        return 1


if __name__ == "__main__":
    sys.exit(main())
