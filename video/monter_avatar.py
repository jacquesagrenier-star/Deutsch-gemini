# -*- coding: utf-8 -*-
"""Monter l'episode avec les prises AVATAR, pour le regarder.

    python video/monter_avatar.py
    python video/monter_avatar.py --queue 0.9 --amorce 0.35

POURQUOI PAS montage.py
    montage.py choisit ses clips dans 04-lipsync puis 03-final, et calcule
    ses coupes a partir de audio/scenes/<scene>/NN-<locuteur>.mp3.
    ⚠️ Or cette numerotation-la a derive : audio/scenes/13-anna.mp3 fait
    1,23 s alors que la replique du plan 13 en fait 4,57 -- la feuille
    A-REFAIRE-AUDIO.txt a redecoupe les longues repliques et les numeros ont
    cesse de se correspondre. Tant que ce noeud n'est pas demele, un montage
    qui s'appuie dessus coupe au mauvais endroit sans le dire.

    Celui-ci ne s'appuie que sur ce qu'on a verifie aujourd'hui : les pistes
    de _a-televerser, dont on sait qu'elles viennent du montage lui-meme, et
    dont importer_prise.py a confirme la correspondance par correlation.

CE QU'IL ASSEMBLE
    les 12 plans parlants  -> _essai-avatar/retours/planNN-omnihuman.mp4,
                              coupes a amorce + replique + queue
    les 7 plans de decor   -> 03-final/planNN.mp4 pour l'image,
                              PLUS audio/scenes/<scene>/NN-erzaehler.mp3
                              pour la NARRATION (01, 02, 03, 04, 07, 18, 19)

⚠️ LES CLIPS DE DECOR N'ONT AUCUNE PISTE SONORE, ET LEUR VOIX VIT AILLEURS.
   Premiere version : j'y ai mis du silence, et l'episode entier a perdu sa
   narration -- sept plans sur dix-neuf. Jacques, en le regardant : « il
   manque la narration », et « il manque un plan lorsqu'il repond qu'il vient
   de Montreal ». Le plan 07 EXISTE, c'est le narrateur entre la question
   d'Anna et la reponse de Mark ; muet, il se lit comme un trou.
   Un plan silencieux au montage ne signale rien : il passe pour une
   respiration voulue.

⚠️ TOUT EST RAMENE AU MEME FORMAT AVANT CONCATENATION. Les prises avatar
   sortent en 1088x1920 a 25 im/s, les plans de decor en 720x1280 a 24. Un
   concat de formats differents echoue, ou pire : il passe et le lecteur
   saute a chaque raccord.
"""
import argparse
import glob
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

# ============ DEUX MONTAGES PAR EPISODE (v579) ============
#
# Le montage COURS prend son temps : il ouvre sur la narration, installe le
# decor, et les sept plans d'Erzaehler portent le gros du vocabulaire.
#
# Le montage VITRINE ouvre sur la chute. Mesure sur l'episode 1 : Mark ne parle
# pas avant 20,65 s, soit 28 % de l'episode -- vingt secondes de patience
# demandees a quelqu'un qui en accorde une. Ce n'est pas un defaut du montage
# cours, c'est un autre metier.
#
# ⚠️ ET LA VITRINE NE COUTE RIEN : elle ne reutilise que des plans deja tournes
# et deja synchronises. Aucun credit, aucune prise neuve.
ORDRE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# L'enjeu d'abord (« je demenage a Berlin »), la pointe d'Anna sur le Buergeramt
# au milieu -- qui amorce l'episode 2 -- et les voeux a la fin. Sept plans, tous
# parlants, tous chronologiques.
VITRINE = [8, 9, 10, 11, 12, 13, 17]

# ⚠️ CETTE LISTE EST CELLE DE L'EPISODE 1, ET ELLE NE VAUT QUE POUR LUI.
# Gardee comme repli quand la scene ne dit rien. Sur l'episode 2 elle se
# trompait sur TROIS plans : elle tenait 6 et 12 pour des repliques (ce sont
# des decors) et 7 pour un decor (c'est le fonctionnaire qui parle). Le
# montage serait alle chercher une prise d'avatar pour un decor, et une
# narration « 07-erzaehler.mp3 » qui n'existe pas -- la scene y range un
# « 07-beamter.mp3 ».
PARLANTS_EP1 = {5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}


def parlants_de_la_scene(scene):
    """Qui parle a l'image, d'apres la SCENE et non d'apres une constante.

    Le champ `type` de chaque plan le dit deja -- « replique » ou « decor ».
    Une liste ecrite a la main devient fausse au deuxieme episode, et rien ne
    le signale : le montage cherche simplement un fichier au mauvais endroit.
    """
    f = os.path.join(RACINE, "scenes", scene + ".json")
    if not os.path.exists(f):
        return set(PARLANTS_EP1)
    d = json.load(io.open(f, encoding="utf-8"))
    return {p["n"] for p in d["plans"] if p.get("type") == "replique"}


L, H, IPS = 1080, 1920, 25


def a_du_son(F, src):
    r = subprocess.run([F, "-hide_banner", "-i", src],
                       capture_output=True, text=True, errors="ignore")
    return "Audio:" in r.stderr


def normaliser(F, src, dst, debut=None, duree=None):
    """⚠️ TOUT SEGMENT SORT AVEC UNE PISTE SONORE, MEME MUETTE.

    Les plans de decor de 03-final n'ont AUCUNE piste audio. Sans cette
    precaution, leurs segments sortaient en video seule, et le concat
    demuxer -- qui exige le meme nombre de flux partout -- laissait tomber
    le son de TOUT l'episode, sans une ligne d'avertissement. Le montage
    s'ouvrait normalement et il etait muet d'un bout a l'autre.
    """
    muet = not a_du_son(F, src)
    cmd = [F, "-y", "-v", "error"]
    if debut is not None:
        cmd += ["-ss", "%.3f" % debut]
    if duree is not None:
        cmd += ["-t", "%.3f" % duree]
    cmd += ["-i", src]
    if muet:
        cmd += ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
    cmd += ["-map", "0:v:0", "-map", "1:a:0" if muet else "0:a:0",
            "-vf", "scale=%d:%d:force_original_aspect_ratio=decrease,"
                   "pad=%d:%d:-1:-1:color=black,fps=%d" % (L, H, L, H, IPS),
            "-c:v", "libx264", "-crf", "18", "-preset", "medium",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
            "-shortest", dst]
    subprocess.run(cmd, check=True)


def narrer(F, src, voix, dst, duree, amorce):
    """L'image du decor, la narration posee dessus apres une courte amorce."""
    subprocess.run(
        [F, "-y", "-v", "error", "-i", src, "-i", voix,
         "-filter_complex",
         "[0:v]scale=%d:%d:force_original_aspect_ratio=decrease,"
         "pad=%d:%d:-1:-1:color=black,fps=%d[v];"
         "[1:a]adelay=%d:all=1,apad,aresample=44100[a]"
         % (L, H, L, H, IPS, int(round(amorce * 1000))),
         "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-ar", "44100", "-ac", "2", "-t", "%.3f" % duree, dst], check=True)


def carton(F, image, piste, dst, debut, duree):
    """Un plan qui n'existe pas encore : son image de depart, sa vraie voix.

    ⚠️ POURQUOI PAS DU NOIR. Un carton noir dit << il manque quelque chose >>
    et rien d'autre. L'image de depart du plan, elle, dit QUI parle, dans quel
    cadrage, et a quelle distance -- donc le montage a blanc repond deja a la
    question du rythme et de l'alternance, qui est la raison d'etre de
    l'exercice.

    ⚠️ ET ELLE EST VOLONTAIREMENT DESATUREE ET ASSOMBRIE. Une image fixe en
    couleur au milieu de plans animes se prend pour une prise ratee ; grise,
    elle se lit comme ce qu'elle est : une place gardee. C'est la meme raison
    qui fait qu'un decor muet passe pour une respiration voulue -- un manque
    qui ne se signale pas devient une intention.
    """
    # ⚠️ MEME FORMAT QUE TOUS LES AUTRES SEGMENTS, AU HERTZ PRES. Le concat
    # demuxer exige des flux identiques ; un carton en 1088x1920 a 48 kHz au
    # milieu de segments en 1080x1920 a 44,1 kHz, et c'est tout le montage qui
    # saute au raccord -- ou qui perd son son sans rien dire. Voir normaliser().
    subprocess.run(
        [F, "-y", "-v", "error", "-loop", "1", "-i", image,
         "-ss", "%.3f" % debut, "-i", piste,
         "-filter_complex",
         "[0:v]scale=%d:%d:force_original_aspect_ratio=decrease,"
         "pad=%d:%d:-1:-1:color=black,hue=s=0.15,eq=brightness=-0.12,"
         "fps=%d[v];[1:a]apad,aresample=44100[a]" % (L, H, L, H, IPS),
         "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-ar", "44100", "-ac", "2", "-t", "%.3f" % duree, dst], check=True)


def image_du_plan(tel, n):
    """L'image de panier du plan, quel que soit le personnage qu'elle porte."""
    for f in sorted(glob.glob(os.path.join(tel, "plan%02d-*.jpg" % n))):
        return f
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--amorce", type=float, default=0.35)
    ap.add_argument("--queue", type=float, default=0.90)
    ap.add_argument("--sortie")
    ap.add_argument("--vitrine", action="store_true",
                    help="le montage court qui ouvre sur la chute")
    ap.add_argument("--ordre", help="liste de plans, ex. 8,9,10,11")
    # ⚠️ UNE FEUILLE PAR MONTAGE, sinon la vitrine ecrase les instants du cours
    # et les sous-titres du cours placent chaque mot au mauvais endroit.
    ap.add_argument("--feuille")
    # ⚠️ UN PLAN DE TETE DECALE TOUT CE QUI SUIT. Prependre trois secondes de
    # carte a la main, c'est laisser la feuille dire que Mark parle a 0,00 s
    # alors qu'il parle a 3,00 -- et les sous-titres suivent la feuille, donc
    # chaque mot se surlignerait trois secondes trop tot. Le montage est le seul
    # a savoir ou commence chaque plan : c'est lui qui pose la tete.
    ap.add_argument("--tete", help="un clip a poser devant, ex. le plan de carte")
    ap.add_argument("--a-blanc", dest="a_blanc", action="store_true",
                    help="garder la place des plans manquants : leur image "
                         "de depart, fixe et grise, avec leur vraie voix")
    a = ap.parse_args()

    if a.ordre:
        ordre = [int(x) for x in a.ordre.replace(" ", "").split(",") if x]
    elif a.vitrine:
        ordre = VITRINE
    else:
        ordre = ORDRE

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    tel = os.path.join(ep, "_a-televerser")
    # ⚠️ DEUX ENDROITS SELON L'EPISODE, ET C'EST UNE DERIVE A NE PAS
    # ARBITRER EN SILENCE. L'episode 1 range ses prises retenues dans
    # _essai-avatar/retours ; l'episode 2 travaille directement dans
    # _essai-avatar. Choisir l'un des deux sans le dire ferait un montage
    # vide, et un montage vide se lit comme << il n'y a rien a monter >>.
    ret = os.path.join(ep, "_essai-avatar", "retours")
    if not os.path.isdir(ret):
        ret = os.path.join(ep, "_essai-avatar")
    tmp = os.path.join(ep, "_montage-avatar")
    os.makedirs(tmp, exist_ok=True)

    morceaux, manquants, total, feuille = [], [], 0.0, []
    print("  plan  source            duree   ce qu'on garde")
    print("  " + "-" * 62)

    if a.tete:
        if not os.path.exists(a.tete):
            sys.exit("  Plan de tete introuvable : %s" % a.tete)
        dt = os.path.join(tmp, "_tete.mp4")
        normaliser(F, a.tete, dt)
        morceaux.append(dt)
        # `total` porte le decalage : la feuille s'ecrit ensuite toute seule
        # avec les bons instants, et les sous-titres la lisent.
        total = M.duree(F, dt)
        print("  --    tete            %6.2f s   %s" % (total, os.path.basename(a.tete)))
    a_blanc = []
    PARLANTS = parlants_de_la_scene(a.scene)
    for n in ordre:
        dst = os.path.join(tmp, "plan%02d.mp4" % n)
        if n in PARLANTS:
            src = os.path.join(ret, "plan%02d-omnihuman.mp4" % n)
            piste = os.path.join(tel, "plan%02d-pleine.mp3" % n)
            if not os.path.exists(src) and a.a_blanc and os.path.exists(piste):
                # Le plan n'existe pas encore : on garde sa PLACE et sa VOIX.
                img = image_du_plan(tel, n)
                if img:
                    tete, queue, _ = M.parole(F, piste)
                    debut = max(0.0, tete - a.amorce)
                    duree = (queue - debut) + a.queue
                    duree = min(duree, M.duree(F, piste) - debut)
                    carton(F, img, piste, dst, debut, duree)
                    a_blanc.append(n)
                    print("  %02d    A BLANC         %6.2f s   image fixe + voix"
                          % (n, duree))
                    feuille.append({"n": n, "debut": round(total, 3),
                                    "duree": round(duree, 3), "type": "a-blanc"})
                    morceaux.append(dst)
                    total += duree
                    continue
            if not os.path.exists(src):
                manquants.append(n)
                print("  %02d    MANQUANT -- la prise avatar n'est pas la" % n)
                continue
            tete, queue, _ = M.parole(F, piste)
            debut = max(0.0, tete - a.amorce)
            duree = (queue - debut) + a.queue
            duree = min(duree, M.duree(F, src) - debut)
            normaliser(F, src, dst, debut, duree)
            print("  %02d    avatar          %6.2f s   %.2f -> %.2f"
                  % (n, duree, debut, debut + duree))
        else:
            src = os.path.join(ep, "03-final", "plan%02d.mp4" % n)
            if not os.path.exists(src):
                manquants.append(n)
                print("  %02d    MANQUANT -- %s" % (n, os.path.basename(src)))
                continue
            voix = os.path.join(RACINE, "audio", "scenes", a.scene,
                                "%02d-erzaehler.mp3" % n)
            if not os.path.exists(voix):
                duree = M.duree(F, src)
                normaliser(F, src, dst)
                print("  %02d    decor           %6.2f s   ⚠️ sans narration"
                      % (n, duree))
            else:
                dv = M.duree(F, voix)
                duree = min(M.duree(F, src), a.amorce + dv + a.queue)
                narrer(F, src, voix, dst, duree, a.amorce)
                print("  %02d    decor + voix    %6.2f s   narration %.2f s"
                      % (n, duree, dv))
        # ⚠️ LE MONTAGE EST LE SEUL A SAVOIR OU COMMENCE CHAQUE PLAN.
        # Recalculer ces instants ailleurs, avec « les memes regles », c'est
        # se garantir qu'ils divergeront le jour ou l'une des deux change.
        # Il ecrit donc la feuille, et les sous-titres la lisent.
        feuille.append({"n": n, "debut": round(total, 3),
                        "duree": round(duree, 3),
                        "type": "replique" if n in PARLANTS else "narration"})
        morceaux.append(dst)
        total += duree

    if not morceaux:
        sys.exit("  Rien a monter.")

    liste = os.path.join(tmp, "_liste.txt")
    io.open(liste, "w", encoding="utf-8", newline="\n").write(
        "".join("file '%s'\n" % m.replace("\\", "/") for m in morceaux))
    # ⚠️ LE NUMERO VIENT DE LA SCENE, PAS D'UNE CONSTANTE. Le montage de
    # l'episode 2 sortait sous le nom « EPISODE-01-avatar.mp4 », dans le
    # dossier du 2. Un fichier mal nomme est la premiere marche vers une
    # mesure fausse -- deja paye deux fois sur ce projet.
    num = a.scene.split("-")[0] if a.scene and a.scene[:2].isdigit() else "01"
    defaut = ("EPISODE-%s-vitrine.mp4" % num if (a.vitrine or a.ordre)
              else "EPISODE-%s-avatar.mp4" % num)
    dst = a.sortie or os.path.join(ep, defaut)
    subprocess.run([F, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", liste, "-c", "copy", dst], check=True)

    fdef = "_plans-vitrine.json" if (a.vitrine or a.ordre) else "_plans.json"
    fjson = a.feuille or os.path.join(tmp, fdef)
    io.open(fjson, "w", encoding="utf-8", newline="").write(
        json.dumps(feuille, ensure_ascii=False, indent=1) + "\n")

    print("\n  %s" % os.path.relpath(dst, RACINE))
    print("  %d plans, %.2f s   (feuille : %s)"
          % (len(morceaux), M.duree(F, dst), os.path.relpath(fjson, RACINE)))
    if manquants:
        print("  ⚠️ MANQUE : %s" % ", ".join("%02d" % n for n in manquants))


if __name__ == "__main__":
    main()
