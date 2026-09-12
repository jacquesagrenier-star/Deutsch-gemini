# -*- coding: utf-8 -*-
"""Sous-titres allemands mot a mot, avec la traduction en dessous.

    python video/sous_titres.py                       (fabrique le .ass)
    python video/sous_titres.py --incruster           (et le grave dans la video)
    python video/sous_titres.py --langue fr           (fr, en, tr, fa, uk)

CE QU'ON FABRIQUE
    Deux lignes gravees dans l'image : l'allemand, dont chaque mot s'allume
    au moment ou il est dit, et la traduction en dessous, fixe.

⚠️ LE CALAGE MOT A MOT EST UNE ESTIMATION, ET IL FAUT LE DIRE.
    ElevenLabs sait rendre des reperes par caractere -- mais seulement en
    REGENERANT l'audio, et le son de ces videos est fige : la bouche a ete
    fabriquee dessus. Il faut donc aligner l'existant.

    Methode, en deux temps :
      1. on repartit la duree de parole au prorata du POIDS de chaque mot
         (ses voyelles, plus une part fixe par mot -- les consonnes prennent
         du temps aussi), avec un supplement apres une virgule ou un point ;
      2. on fait GLISSER chaque frontiere vers le creux d'energie le plus
         proche, dans une fenetre de +/- 120 ms. Quand un blanc existe entre
         deux mots, la frontiere s'y pose ; quand les mots s'enchainent, elle
         reste ou le prorata l'avait mise.

    ⚠️ Ca ne vaut pas un aligneur force. Sur des repliques de 1,5 a 4,6 s
    ca tient a l'oeil ; sur une longue phrase l'erreur s'accumule. Le seul
    juge est le regard de quelqu'un qui lit en meme temps qu'il ecoute.

⚠️ ET LA LIGNE DE TEMPS EST CELLE DU MONTAGE, PAS DES CLIPS.
    Les instants viennent de _montage-avatar/_plans.json, ecrit par
    monter_avatar.py. Les recalculer ici « avec les memes regles » serait se
    garantir qu'ils divergeront le jour ou l'une des deux change.
"""
import argparse
import io
import json
import os
import struct
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

SR = 16000
FENETRE = 0.120        # de combien une frontiere peut glisser
VOYELLES = "aeiouyäöüáéèêàâîïôûùAEIOUYÄÖÜ"
PART_FIXE = 1.2        # ce que "pese" un mot avant meme ses voyelles
PAUSE = {",": 1.4, ";": 1.6, ":": 1.6, ".": 2.0, "!": 2.0, "?": 2.0}


def poids(mot):
    p = PART_FIXE + sum(1 for c in mot if c in VOYELLES)
    for signe, sup in PAUSE.items():
        if mot.endswith(signe):
            p += sup
    return p


def enveloppe(F, chemin):
    r = subprocess.run([F, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", chemin, "-map", "0:a", "-ac", "1", "-ar", str(SR),
                        "-f", "s16le", "-"], capture_output=True)
    x = struct.unpack("<%dh" % (len(r.stdout) // 2), r.stdout)
    pas = int(SR * 0.01)
    return [sum(abs(v) for v in x[i:i + pas]) / pas
            for i in range(0, len(x) - pas, pas)]


def caler(bornes, env, tete, queue):
    """Faire glisser chaque frontiere vers le creux d'energie le plus proche."""
    cales = [bornes[0]]
    for b in bornes[1:-1]:
        i = int(b * 100)
        lo, hi = int((b - FENETRE) * 100), int((b + FENETRE) * 100)
        lo, hi = max(int(tete * 100) + 1, lo), min(len(env) - 1, hi)
        if hi > lo:
            j = min(range(lo, hi + 1), key=lambda k: env[k])
            # ⚠️ On ne glisse que si le creux est REELLEMENT un creux : sinon
            # on deplace la frontiere au hasard du bruit de fond.
            if env[j] < 0.6 * env[i] if i < len(env) else False:
                b = j / 100.0
        cales.append(b)
    cales.append(bornes[-1])
    return cales


def decouper(F, piste, texte):
    """[(mot, debut, fin)] sur la duree de parole mesuree de la piste."""
    mots = texte.split()
    tete, queue, _ = M.parole(F, piste)
    total = sum(poids(m) for m in mots)
    bornes, t = [tete], tete
    for m in mots:
        t += (queue - tete) * poids(m) / total
        bornes.append(t)
    bornes = caler(bornes, enveloppe(F, piste), tete, queue)
    return [(m, bornes[i], bornes[i + 1]) for i, m in enumerate(mots)]


def echapper(s):
    return s.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


# ⚠️ WrapStyle 1, et les trois valeurs veulent dire trois choses.
#   2 : AUCUN retour a la ligne automatique -- le texte deborde de l'ecran
#       sans un avertissement. C'est ce que j'avais mis d'abord.
#   0 : coupe en EQUILIBRANT les lignes. Elargir les marges n'y change
#       rien, il coupe au milieu quelle que soit la place disponible --
#       d'ou le « tu n'as pas elargi le texte » de Jacques alors que les
#       marges etaient passees de 100 a 45 px.
#   1 : remplit la ligne du haut et ne passe a la suivante qu'une fois la
#       place epuisee. C'est le seul qui utilise vraiment la largeur.
#
# ⚠️ LA PHRASE EST EN BLANC, ET LA COULEUR EST POSEE MOT PAR MOT.
# Voir phrase_mot_a_mot() : le tag \k du karaoke a ete abandonne parce qu'il
# garde colores les mots deja dits. Le style ne porte donc plus la couleur de
# surbrillance -- elle est ecrite dans chaque ligne, sur le seul mot du
# moment.
ENTETE = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 1
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: DE,Arial,54,&H00FFFFFF,&H00FFFFFF,&H00101418,&H00000000,-1,0,0,0,100,100,0,0,1,4,2,2,45,45,215,1
Style: FR,Arial,40,&H00E8D8C8,&H00E8D8C8,&H00101418,&H00000000,0,1,0,0,100,100,0,0,1,3,2,2,45,45,120,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


# ⚠️ POURQUOI PAS LE TAG \k DU KARAOKE.
# \k est le mecanisme standard, et il fait exactement ce que Jacques n'a pas
# voulu : un mot dit GARDE sa couleur, donc la phrase se remplit de gauche a
# droite et l'oeil voit une barre de progression, pas un mot. « C'est la
# phrase complete a partir du debut en progressant. »
#
# Pour n'allumer QUE le mot en cours, il faut une ligne par mot : la phrase
# entiere s'affiche a chaque fois, et seul le mot du moment change de
# couleur. Plus verbeux dans le fichier, exact a l'ecran.
# ⚠️ SIX CHIFFRES, PAS HUIT. Un tag \c en ligne attend &Hbbggrr& -- la
# couleur seule, sans l'alpha. Les huit chiffres (&Haabbggrr&) sont la forme
# des STYLES, dans l'en-tete. Premiere version : &H0000D7FF& dans un \c ;
# libass a laisse tomber la balise sans un mot, et les sous-titres sont
# restes uniformement blancs. Une balise mal formee ne se plaint jamais.
SURBRILLANCE = "&H00D7FF&"        # ambre vif, en &Hbbggrr (RGB 255,215,0)
REPOS = "&HFFFFFF&"               # blanc


def phrase_mot_a_mot(mots, decalage, debut, fin):
    """Une ligne par mot : la phrase entiere, le mot du moment en couleur."""
    out = []
    d0 = mots[0][1] + decalage
    if d0 > debut + 0.05:
        # avant le premier mot : la phrase est la, entierement au repos
        out.append("Dialogue: 0,%s,%s,DE,,0,0,0,,%s"
                   % (tc(debut), tc(d0),
                      " ".join(echapper(m) for m, _, _ in mots)))
    for i, (m, d, f) in enumerate(mots):
        d, f = d + decalage, f + decalage
        if i == len(mots) - 1:
            f = max(f, fin)          # le dernier mot reste jusqu'a la coupe
        texte = " ".join(
            ("{\\c%s}%s{\\c%s}" % (SURBRILLANCE, echapper(x), REPOS))
            if j == i else echapper(x)
            for j, (x, _, _) in enumerate(mots))
        out.append("Dialogue: 0,%s,%s,DE,,0,0,0,,%s"
                   % (tc(max(debut, d)), tc(f), texte))
    return out


def tc(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return "%d:%02d:%05.2f" % (h, m, s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--langue", default="fr")
    ap.add_argument("--incruster", action="store_true")
    ap.add_argument("--clip")
    ap.add_argument("--sortie")
    a = ap.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    tel = os.path.join(ep, "_a-televerser")
    feuille = os.path.join(ep, "_montage-avatar", "_plans.json")
    if not os.path.exists(feuille):
        sys.exit("  Pas de feuille de montage. Lancer monter_avatar.py d'abord.")
    plans = {p["n"]: p for p in json.load(io.open(feuille, encoding="utf-8"))}
    scene = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                              encoding="utf-8"))

    lignes = []
    for p in scene["plans"]:
        n = p["n"]
        if n not in plans:
            continue
        info = plans[n]
        de, tr = p.get("de", ""), p.get(a.langue, "")
        if not de:
            continue
        if info["type"] == "replique":
            piste = os.path.join(tel, "plan%02d-pleine.mp3" % n)
            if not os.path.exists(piste):
                continue
            mots = decouper(F, piste, de)
            # ⚠️ Le clip est coupe a `amorce` avant le premier mot : la piste
            # et le montage n'ont pas la meme origine. On recale sur le
            # premier mot, que monter_avatar place a `amorce` du debut.
            decalage = info["debut"] + 0.35 - mots[0][1]
            debut = info["debut"]
            fin = info["debut"] + info["duree"]
            lignes += phrase_mot_a_mot(mots, decalage, debut, fin)
        else:
            # ⚠️ LA NARRATION AUSSI SE SURLIGNE MOT A MOT.
            # Premiere version : elle se lisait d'un bloc, « parce qu'elle
            # n'en a pas besoin ». C'est l'inverse -- c'est elle qui porte le
            # plus de texte, donc celle ou l'apprenant a le plus besoin de
            # savoir ou en est la voix. Jacques : « au debut de la video on ne
            # voit pas la surbrillance sur les mots ».
            voix = os.path.join(RACINE, "audio", "scenes", a.scene,
                                "%02d-erzaehler.mp3" % n)
            debut = info["debut"]
            fin = info["debut"] + info["duree"]
            if os.path.exists(voix):
                mots = decouper(F, voix, de)
                # narrer() retarde la voix de 0,35 s dans le segment : les
                # instants du mp3 se lisent donc a partir de debut + 0,35.
                lignes += phrase_mot_a_mot(mots, info["debut"] + 0.35,
                                           debut, fin)
            else:
                lignes.append("Dialogue: 0,%s,%s,DE,,0,0,0,,%s"
                              % (tc(debut), tc(fin), echapper(de)))
        if tr:
            lignes.append("Dialogue: 0,%s,%s,FR,,0,0,0,,%s"
                          % (tc(debut), tc(fin), echapper(tr)))

    dst = os.path.join(ep, "EPISODE-01-avatar.%s.ass" % a.langue)
    io.open(dst, "w", encoding="utf-8-sig", newline="\r\n").write(
        ENTETE + "\n".join(lignes) + "\n")
    print("  %s   %d lignes" % (os.path.relpath(dst, RACINE), len(lignes)))

    if not a.incruster:
        print("  Relancer avec --incruster pour les graver dans la video.")
        return

    clip = a.clip or os.path.join(ep, "EPISODE-01-avatar-sonorise.mp4")
    if not os.path.exists(clip):
        sys.exit("  Video introuvable : %s" % clip)
    sortie = a.sortie or os.path.splitext(clip)[0] + "-st.mp4"
    # ⚠️ Le filtre subtitles veut un chemin a la mode POSIX, et les deux-points
    # du lecteur Windows doivent etre echappes -- sinon ffmpeg les lit comme
    # des separateurs d'options et se plaint d'un fichier introuvable.
    chemin = dst.replace("\\", "/").replace(":", "\\:")
    subprocess.run([F, "-y", "-v", "error", "-i", clip,
                    "-vf", "subtitles='%s'" % chemin,
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", sortie], check=True)
    print("  %s" % os.path.relpath(sortie, RACINE))


if __name__ == "__main__":
    main()
