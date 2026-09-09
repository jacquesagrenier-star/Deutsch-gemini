# -*- coding: utf-8 -*-
"""Assemble l'episode : les 19 plans dans l'ordre, chacun avec sa replique.

    python video/montage.py --scene 01-ankunft-berlin

CE QU'IL FAIT, ET CE QU'IL NE FAIT PAS
    Il colle bout a bout les clips de 03-final/ dans l'ordre du scenario et
    pose sur chacun sa piste ElevenLabs. Il ne fait NI lip-sync NI
    sous-titres : le lip-sync se fait avant, plan par plan, chez sync.so, et
    les sous-titres sont affiches par l'application, pas incrustes.

    C'est donc un montage de travail -- celui qui permet de voir l'episode
    pour la premiere fois et de juger le rythme.

LE SILENCE AVANT ET APRES CHAQUE REPLIQUE
    Les clips durent 4 a 7 secondes, les repliques 1,5 a 7. L'ecart n'est pas
    du gaspillage : un plan ne peut pas commencer sur la premiere syllabe ni
    finir sur la derniere. On pose donc la voix avec un retard (AMORCE), et
    ce qui reste apres elle est la respiration du plan.

    Si la replique est plus longue que le clip -- ca arrive, plan 13 -- on
    part a zero et on laisse deborder : mieux vaut une fin serree qu'une
    phrase coupee.

LA QUEUE SE COUPE ICI, APRES LE LIP-SYNC
    --queue coupe chaque plan parlant un temps donne apres la fin de sa
    replique, et il le fait MAINTENANT QUE LE PLAN EST SYNCHRONISE. On peut
    donc rejouer le montage a 0,2 s, a 0,6 s, a 1 s, et regarder.

    L'autre ordre -- couper d'abord, synchroniser ensuite -- economise 0,89 $
    chez sync.so sur l'episode, puisqu'on ne paie pas les images jetees. Mais
    un clip raccourci ne se rallonge plus : rendre son air a un plan
    obligerait a repayer toute la synchro. Le rythme d'une scene ne se decide
    pas avant de l'avoir vue.

    lipsync.py --queue existe toujours pour le jour ou le montage est fige.

ON NE REENCODE LA VIDEO QU'UNE FOIS
    Chaque plan est mux avec son audio sans toucher au flux video (-c:v copy).
    Le seul reencodage a lieu au collage final, et il est inevitable : les
    clips viennent tous du meme modele avec les memes reglages, mais concat
    exige un flux continu.
"""
import argparse
import array
import io
import json
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Le retard de la voix sur le debut du plan. Assez pour qu'on voie le
# personnage avant qu'il parle, assez peu pour que le plan ne traine pas.
AMORCE = 0.35


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def duree(ff, chemin):
    r = subprocess.run([ff, "-hide_banner", "-i", chemin],
                       capture_output=True, text=True, errors="replace")
    m = re.search(r"Duration: \d+:(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 60 + float(m.group(2)) if m else None


def parole(ff_, mp3):
    """(debut, fin, duree du fichier) -- ou la VOIX porte, en secondes.

    POURQUOI ON NE SE FIE PLUS A LA DUREE DU FICHIER (9 septembre 2026)
        Jacques, sur le plan 05 synchronise : « la bouche continue un petit
        peu, elle n'est pas synchro ». Mesure : la machoire est en retard de
        208 ms sur la voix a la fin de la phrase, et bouge encore 0,62 s apres
        le dernier mot.

        La cause n'etait ni Seedance ni sync.so. La feuille de tournage
        demandait de parler pendant LA DUREE DU FICHIER mp3 -- or un mp3 ne
        parle pas tout du long. Mesure sur les dix-neuf repliques : 0,10 s de
        silence en tete, 0,19 s en queue, soit 0,29 s de machoire de trop par
        plan. La machoire parlait donc plus longtemps que la voix, et l'ecart
        grandissait jusqu'au dernier mot.

        Le plan 13 est l'exemple extreme : fichier de 7,04 s, voix qui
        s'arrete a 4,71 s, puis du silence numerique pur (niveau 2 sur 18 912,
        verifie a quatre seuils). Son clip a ete genere a NEUF secondes pour
        une replique de 4,6 s.

        Toute duree tiree d'une replique passe donc par ici.

    LE SEUIL
        4 % du maximum, sur des fenetres de 10 ms. Sur nos fichiers le choix
        ne change rien -- de 1 % a 10 %, le plan 13 donne 4,71 / 4,64 s. Une
        voix ElevenLabs sur fond numerique n'a pas de zone grise.
    """
    r = subprocess.run([ff_, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", mp3, "-map", "0:a", "-ac", "1", "-ar", "24000",
                        "-f", "s16le", "-"], capture_output=True)
    n = len(r.stdout) // 2
    if n < 240:
        return 0.0, 0.0, 0.0
    ech = array.array("h")
    ech.frombytes(r.stdout[:n * 2])
    par = 240                                          # 10 ms
    env = [sum(abs(v) for v in ech[i * par:(i + 1) * par]) / float(par)
           for i in range(n // par)]
    haut = max(env) if env else 0.0
    if haut <= 0:
        return 0.0, n / 24000.0, n / 24000.0
    seuil = haut * 0.04
    ou = [i for i, v in enumerate(env) if v > seuil]
    if not ou:
        return 0.0, n / 24000.0, n / 24000.0
    return ou[0] / 100.0, (ou[-1] + 1) / 100.0, n / 24000.0


def ff(cmd, quoi):
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        sys.exit("  echec sur %s :\n%s" % (quoi, r.stderr[-700:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--queue", type=float, default=None, metavar="SECONDES",
                    help="couper chaque plan parlant SECONDES apres la fin de "
                         "la replique, synchronise ou non. Se rejoue autant "
                         "de fois qu'on veut. Sans lui, le plan va au bout.")
    a = ap.parse_args()

    F = ffmpeg()
    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    dv = os.path.join(RACINE, "video", "episode-" + a.scene)
    da = os.path.join(RACINE, "audio", "scenes", a.scene)
    tmp = os.path.join(dv, "_montage")
    os.makedirs(tmp, exist_ok=True)

    morceaux = []
    synchro = 0
    perimes = []
    print("  plan   clip    voix   %s" % "assemblage")
    for p in d["plans"]:
        # LE PLAN SYNCHRONISE PASSE AVANT L'ORIGINAL. lipsync.py ecrit dans
        # 04-lipsync sans jamais toucher a 03-final : on peut donc remonter
        # l'episode avant, pendant et apres la synchro, et il prend a chaque
        # fois ce qui existe de mieux. Un plan absent de 04-lipsync -- les
        # decors, qui n'ont pas de visage -- retombe sur son clip d'origine.
        #
        # ⚠️ ENCORE FAUT-IL QUE LA SYNCHRO SOIT CELLE DE LA PRISE EN PLACE.
        # Le 9 septembre 2026, douze plans ont ete retournes : 03-final a recu
        # les nouvelles prises, et 04-lipsync gardait la synchro des anciennes,
        # au meme nom, sans une ligne pour le dire. Le montage aurait repris
        # les vieux plans en silence -- apres 2 400 credits de re-tournage.
        #
        # lipsync.py porte deja cette garde depuis le matin ; le montage, non,
        # et c'est lui qu'on lance en premier pour regarder. On compare donc
        # les dates ici aussi : une source plus recente que sa synchro rend
        # celle-ci perimee, et le plan retombe sur 03-final -- ou l'on voit
        # bouger des levres au hasard, ce qui SE VOIT, au lieu de revoir sans
        # le savoir la prise qu'on vient de remplacer.
        origine = os.path.join(dv, "03-final", "plan%02d.mp4" % p["n"])
        v = os.path.join(dv, "04-lipsync", "plan%02d.mp4" % p["n"])
        synchronise = os.path.exists(v)
        perime = (synchronise and os.path.exists(origine)
                  and os.path.getmtime(origine) > os.path.getmtime(v))
        if perime:
            synchronise = False
            perimes.append(p["n"])
        if synchronise:
            synchro += 1
        else:
            v = origine
        s = os.path.join(da, "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(v):
            sys.exit("  Plan %02d : clip manquant (%s)" % (p["n"], os.path.basename(v)))
        if not os.path.exists(s):
            sys.exit("  Plan %02d : replique manquante (%s)" % (p["n"], os.path.basename(s)))

        dv_, da_ = duree(F, v), duree(F, s)
        out = os.path.join(tmp, "plan%02d.mp4" % p["n"])

        # COUPER PLUTOT QU'ETIRER. Le 8 septembre, cherchant a supprimer le
        # silence ou la bouche du clip s'agite pour rien, on a mesure ce qu'il
        # faudrait pour le combler avec la voix : un ralenti de 0,40 a 0,64
        # fois selon les plans -- 55 a 150 % plus long. Une diction d'endormi,
        # et ElevenLabs v3 ignore de toute facon le reglage de vitesse.
        #
        # La queue, elle, ne coute rien : on garde l'amorce, la replique, et
        # le temps demande apres elle. Ce qu'on perd est la respiration du
        # plan ; ce qu'on gagne est de ne plus montrer une machoire qui parle
        # sur du silence. C'est un choix de rythme, donc il se regarde.
        #
        # ON COUPE APRES LE LIP-SYNC, ET C'EST UN CHOIX PAYANT (9 sept. 2026)
        #     Ce bloc refusait de toucher a un plan venu de 04-lipsync : il
        #     avait deja ete raccourci par lipsync.py avant l'envoi, pour ne
        #     pas payer sync.so sur des images qu'on jette.
        #
        #     Jacques : synchroniser le clip ENTIER coute 0,89 $ de plus sur
        #     l'episode, et laisse le rythme reglable jusqu'au bout. Un clip
        #     raccourci avant l'envoi, lui, ne se rallonge plus -- pour
        #     rendre l'air a un plan il faut repayer la synchro complete.
        #     Quatre-vingt-neuf cents contre un aller-retour : il a raison.
        #
        #     La coupe vit donc ici, ou elle se refait autant de fois qu'on
        #     veut. lipsync.py --queue reste possible, mais c'est le geste de
        #     la fin, quand le montage ne bougera plus.
        #
        # LA CIBLE EST ABSOLUE, PAS RELATIVE -- c'est ce qui rend la coupe
        # rejouable. On vise AMORCE + replique + queue, mesure depuis le debut
        # du plan. Si le fichier est deja plus court (lipsync.py est passe
        # avec une queue plus serree), on ne peut pas le rallonger : on le dit
        # au lieu de couper une deuxieme fois.
        #
        # -c:v copy NE COUPE PAS A LA MILLISECONDE. Il garde des paquets
        # entiers, donc l'image tombe ou elle peut (2,83 s) pendant que
        # l'audio, lui, est coupe net (2,73 s). L'ecart de 0,10 s par plan
        # revenait par la fenetre apres qu'on l'ait chasse par la porte.
        #
        # La duree du plan est donc CELLE DU FICHIER, mesuree, et l'audio se
        # cale dessus. Jamais l'inverse. L'image coupee et la piste sonore
        # entrent separement dans le mux qui suit, et c'est -t fin qui les
        # ramene a la meme longueur.
        fin, image, trop_court = dv_, v, ""
        if a.queue is not None and p["type"] == "replique":
            vise = AMORCE + da_ + a.queue
            if vise < dv_ - 0.02:
                coupe = os.path.join(tmp, "_coupe%02d.mp4" % p["n"])
                ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y",
                    "-i", v, "-t", "%.3f" % vise, "-c:v", "copy", "-an", coupe],
                   "coupe du plan %02d" % p["n"])
                image, fin = coupe, duree(F, coupe)
            elif dv_ < vise - 0.02:
                trop_court = ("  <- %.2f s seulement, la queue demandee en "
                              "voudrait %.2f" % (dv_, vise))

        # APAD N'EST PAS UN DETAIL DE CONFORT, C'EST CE QUI TIENT LE MONTAGE.
        #
        # Une replique de 2,4 s dans un plan de 5 s laissait une piste audio
        # PLUS COURTE QUE L'IMAGE. Le demultiplexeur concat assemble les deux
        # flux separement : chaque trou d'audio remonte tout ce qui suit. Sur
        # l'episode 1, le decalage atteignait +4,7 s au comptoir et +9,9 s a
        # la fin -- la voix d'Anna arrivait avant que Mark ne soit devant elle.
        #
        # Repere par Jacques le 8 septembre : « la discussion arrive plusieurs
        # secondes avant que Marc arrive au comptoir ». Le defaut etait dans
        # TOUS les montages de la journee, et rien ne l'avait signale : ffmpeg
        # ne s'en plaint pas, les durees totales sont justes, et le tableau a
        # l'ecran montrait des plans parfaitement normaux.
        #
        # On complete donc chaque piste par du silence jusqu'a la derniere
        # image du plan. Image et son font exactement la meme longueur, et le
        # collage ne peut plus deriver.
        if synchronise:
            # LE PLAN SYNCHRONISE PORTE DEJA SA VOIX, ET AU BON ENDROIT.
            # lipsync.py lui a envoye une piste calee sur la duree du clip,
            # amorce comprise : c'est exactement celle que le montage aurait
            # posee. La reposer par-dessus ferait un doublon decale.
            #
            # L'IMAGE VIENT DU FICHIER COUPE, LA VOIX DU FICHIER ENTIER. Si on
            # prenait les deux dans le coupe, on n'aurait rien : la coupe se
            # fait en -c:v copy -an, elle jette le son. La piste synchronisee
            # est donc relue depuis l'original et ramenee a `fin` par -t.
            amorce, note = AMORCE, "  sync"
            entree = ["-i", image, "-i", v, "-map", "0:v", "-map", "1:a"]
        else:
            # La voix tient-elle avec l'amorce ? Sinon on la colle au debut.
            amorce = AMORCE if (da_ + AMORCE) <= dv_ else 0.0
            note = "" if amorce else "  <- voix au ras, la replique remplit le plan"
            entree = ["-i", image, "-itsoffset", "%.3f" % amorce, "-i", s,
                      "-map", "0:v", "-map", "1:a"]
        note += trop_court
        if p["n"] in perimes:
            note += "  <- synchro PERIMEE, on montre le clip brut"
        ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y"]
           + entree
           + ["-af", "apad", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
              "-ar", "44100", "-t", "%.3f" % fin, out],
           "plan %02d" % p["n"])
        morceaux.append(out)
        if fin < dv_ - 0.02:
            note += "  coupe a %.2f s (-%.2f)" % (fin, dv_ - fin)
        print("  %02d    %5.2f  %5.2f   +%.2f%s"
              % (p["n"], dv_, da_, amorce, note))

    # LE CONTROLE QUI AURAIT ATTRAPE LA DERIVE. Un segment dont le son est
    # plus court que l'image decale tout ce qui suit, et rien d'autre ne le
    # dit. On le verifie donc a chaque montage, sur chaque segment.
    boiteux = []
    for m in morceaux:
        r = subprocess.run([F, "-hide_banner", "-i", m, "-map", "0:a",
                            "-c", "copy", "-f", "null", "-"],
                           capture_output=True, text=True, errors="replace")
        t = re.search(r"time=\d+:(\d+):([\d.]+)", r.stderr)
        son = int(t.group(1)) * 60 + float(t.group(2)) if t else 0.0
        img = duree(F, m)
        if abs(img - son) > 0.05:
            boiteux.append((os.path.basename(m), img, son))
    if boiteux:
        print("\n  DERIVE : ces segments n'ont pas la meme duree d'image et de")
        print("  son. Le collage fera remonter tout ce qui les suit.")
        for nom, img, son in boiteux:
            print("    %s  image %.2f  son %.2f  (%+.2f)" % (nom, img, son, img - son))
        sys.exit("  Montage abandonne.")

    liste = os.path.join(tmp, "_liste.txt")
    io.open(liste, "w", encoding="utf-8", newline="").write(
        "".join("file '%s'\n" % os.path.basename(m) for m in morceaux))

    final = os.path.join(dv, "EPISODE-%s.mp4" % a.scene.split("-")[0])
    ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", liste,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
        final], "collage final")

    print("\n  %s" % os.path.relpath(final, RACINE))
    print("  %.1f secondes, %d plans" % (duree(F, final), len(morceaux)))
    print("  image et son de meme duree sur les %d segments." % len(morceaux))
    if perimes:
        print("  SYNCHRO PERIMEE sur %d plan(s) : %s"
              % (len(perimes), ", ".join("%02d" % n for n in perimes)))
        print("  Leur clip de 03-final est plus recent que 04-lipsync : ce"
              " montage montre")
        print("  les prises neuves SANS synchro. Refaire la synchro de ces"
              " plans avant de")
        print("  juger les levres -- le rythme, lui, se juge des maintenant.")
    parlants = sum(1 for p in d["plans"] if p["type"] == "replique")
    if synchro < parlants:
        print("  %d/%d plans parlants passes au lip-sync -- les autres bougent"
              " encore les levres au hasard." % (synchro, parlants))


if __name__ == "__main__":
    main()
