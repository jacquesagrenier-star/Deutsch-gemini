# -*- coding: utf-8 -*-
"""Passe les plans d'une scene au lip-sync de sync.so.

    python video/lipsync.py --scene 01-ankunft-berlin              # a blanc
    python video/lipsync.py --scene 01-ankunft-berlin --pour-de-vrai

A BLANC PAR DEFAUT, comme scene_audio.py : chaque seconde envoyee est
facturee, et un lancement par megarde se paie.

IL REPREND OU IL S'ETAIT ARRETE, ET C'EST LE POINT IMPORTANT
    Chaque generation soumise recoit un identifiant, note aussitot dans
    etat.json. Une relance ne resoumet donc jamais un plan deja envoye : elle
    va reprendre son identifiant et redemander ou il en est.

    Sans ca, une coupure reseau au onzieme plan sur douze couterait douze
    generations de plus a la reprise -- on paierait deux fois un travail deja
    fait, et sans le savoir.

CE QUE FAIT LE LIP-SYNC, ET CE QU'IL NE FAIT PAS
    Il REPEINT LES LEVRES pour qu'elles suivent l'audio fourni. Le reste de
    l'image est celui du clip source, y compris LA MACHOIRE, le menton et les
    joues. C'est pour cela que la piste sonore de nos clips est jetee des le
    rapatriement : ce que le personnage semblait articuler n'a aucune
    importance.

    Mais ce qu'il semblait articuler AVEC LA MACHOIRE, si. Verifie le
    8 septembre 2026 sur le plan 5 : une bouche qui s'ouvre en plein silence,
    a l'image pres, dans le clip d'origine comme dans le synchronise, et
    identique sous lipsync-2 et lipsync-2-pro. Aucun modele ne peut la
    refermer -- ce n'est pas dans les levres.

    D'ou la regle du tournage, dans scenes/production.py (bloc BOUCHE) : le
    personnage parle au debut du plan, puis ferme la bouche et ne la rouvre
    plus. La machoire bouge ou l'oreille entend une voix.
"""
import argparse
import io
import json
import mimetypes
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.sync.so/v2/generate"

# Le meme retard de voix que montage.py : l'audio cale ici doit tomber la ou
# le montage l'aurait pose, sinon la bouche suit une piste et l'oreille une
# autre. Une seule valeur, importee, plutot que deux qui derivent.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import montage as M                                         # noqa: E402
AMORCE = M.AMORCE

# LE DEBUT DE LA FENETRE DE PAROLE ECRITE DANS LE PROMPT. production.bouche
# arrondit l'amorce du montage a 0,5 s pour la dire au modele ; c'est donc 0,5
# que la machoire a RECU.
#
# ⚠️ CE N'EST PAS CELLE QU'ELLE REND (mesure du 10 septembre 2026).
#
# Six prises tournees avec la voix en reference, mesurees par
# video/mesurer_decalage.py : la machoire demarre de +0,11 a +1,96 s APRES la
# voix qu'on a donnee. Jamais avant, pas une fois -- donc au montage le son
# arrive toujours EN AVANCE sur l'image, le cote que l'UIT-R BT.1359-1 tolere
# le moins (45 ms, contre 125 ms pour un son en retard).
#
# Et l'ecart n'est pas une constante : 1,85 s d'etendue sur six prises. Il n'y
# a donc rien a compenser d'un chiffre fixe. La seule valeur juste est la
# fenetre MESUREE de la prise, que rapatrier.py ecrit dans
# 02-prises/_parole.json depuis le 9 septembre -- et que ce script ignorait.
#
# FENETRE ne sert donc plus que de REPLI, pour les prises tournees avant que
# la mesure existe. Le calage y reste une supposition, et il le dit.
FENETRE = 0.5

# On preferera toujours mettre le son en RETARD sur l'image plutot qu'en
# avance : les seuils de l'UIT ne sont pas symetriques. Voir mesurer_decalage.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mesurer_decalage as MD                               # noqa: E402
TOLERANCE_RETARD = -MD.ITU_DETECTABLE[1]     # 0,125 s


def fenetres_machoire(base):
    """Ou la machoire parle VRAIMENT, plan par plan, pour la prise retenue.

    Deux fichiers se rejoignent ici, et aucun des deux ne suffit seul :
      03-final/_retenues.txt  dit QUELLE prise est dans 03-final
      02-prises/_parole.json  dit ou sa machoire parle

    Une prise absente du second est une prise d'avant la mesure : sa piste a
    ete coupee a l'archivage et sa machoire n'est plus observable. On ne
    devine pas -- on retombe sur FENETRE et on le signale.
    """
    prises = {}
    ret = os.path.join(base, "03-final", "_retenues.txt")
    if os.path.exists(ret):
        for ligne in io.open(ret, encoding="utf-8"):
            m = re.match(r"\s*\d{4}-\d\d-\d\d \d\d:\d\d\s+plan(\d+)\s+(\S+\.mp4)",
                         ligne)
            if m:
                prises[int(m.group(1))] = m.group(2)   # la derniere ligne gagne
    pj = os.path.join(base, "02-prises", "_parole.json")
    mesures = (json.load(io.open(pj, encoding="utf-8"))
               if os.path.exists(pj) else {})
    out = {}
    for n, prise in prises.items():
        b = (mesures.get(prise) or {}).get("bouche")
        if b and len(b) == 2 and b[1] > b[0]:
            out[n] = (float(b[0]), float(b[1]), prise)
    return out


def placer_voix(s_aud, amorce_forcee, fenetre):
    """(retard a appliquer a la voix, ligne de diagnostic).

    LA REGLE, ET D'OU ELLE VIENT
        On cale l'ATTAQUE, pas le milieu. Quand la machoire parle plus
        longtemps que la voix, le jeu va d'abord au DEBUT -- jusqu'a 125 ms,
        la ou l'UIT laisse passer un son en retard. Une machoire qui s'ouvre
        un dixieme avant la voix se lit comme une inspiration ; une voix qui
        part avant la machoire, elle, est le defaut que l'oreille attrape a
        45 ms.

        Le reste du jeu tombe a la fin, et c'est la bouche qui traine --
        « la bouche d'Anna continue a bouger apres qu'elle a arrete de
        parler ». Ce defaut-la ne se cale pas, il se CONFORME
        (audio/conformer.py) ou se retourne. Le diagnostic le chiffre plutot
        que de le repartir en silence.

        Quand la machoire parle MOINS longtemps que la voix, il n'y a plus de
        jeu : on aligne les attaques, ce qui met l'ecart entier a la fin et
        garde l'attaque juste.
    """
    tete, queue, fichier = M.parole(M.ffmpeg(), s_aud)
    parlee = queue - tete
    if amorce_forcee is not None:
        return amorce_forcee, tete, parlee, "amorce imposee : %.2f s" % amorce_forcee
    if fenetre:
        s0, s1, prise = fenetre
        jeu = (s1 - s0) - parlee
        debut_voix = s0 + max(0.0, min(jeu, TOLERANCE_RETARD))
        # Convention de mesurer_decalage : positif = son en avance sur l'image.
        ecart = s0 - debut_voix
        traine = s1 - (debut_voix + parlee)
        diag = ("machoire mesuree %.2f-%.2f (%s) -> %s"
                % (s0, s1, prise, MD.verdict(ecart)))
        if traine > 0.08:
            diag += " ; bouche qui traine %.2f s -- a conformer" % traine
        elif traine < -0.08:
            # L'inverse, et il est tout aussi visible : la bouche se referme
            # pendant que la voix parle encore. conformer.py sait aussi
            # comprimer -- c'est le meme geste, dans l'autre sens.
            diag += (" ; bouche fermee %.2f s avant la fin de la voix"
                     " -- a conformer" % -traine)
        return debut_voix - tete, tete, parlee, diag
    # REPLI : la machoire n'a pas ete mesuree. On centre la voix dans la
    # fenetre DEMANDEE, comme avant le 10 septembre -- en sachant maintenant
    # que le modele ne l'honore pas, et en le disant.
    ecart = max(0.0, fichier - parlee)
    if ecart > 0.05:
        am = FENETRE + ecart / 2.0 - tete
    else:
        am = AMORCE
    return am, tete, parlee, ("machoire NON MESUREE (prise d'avant le 9 sept.)"
                              " : calage suppose sur la fenetre demandee")

# SYNC FACTURE A L'IMAGE, PAS A LA SECONDE. Leur page de tarifs affiche un
# prix a la seconde calcule sur 25 im/s ; nos clips Seedance sont a 24, donc
# la seconde nous coute 4 % de moins que l'affiche. Releve sur sync.so/pricing
# le 8 septembre 2026, tarif des forfaits Hobbyist et Creator (Growth -5 %,
# Scale -20 %).
PAR_IMAGE = {"lipsync-1.9.0": 0.001, "lipsync-2": 0.002,
             "lipsync-2-pro": 0.00333, "sync-3": 0.00534, "react-1": 0.00667}
TARIF = PAR_IMAGE


def _sonde(chemin):
    import imageio_ffmpeg
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner",
                           "-i", chemin], capture_output=True, text=True,
                          errors="replace").stderr


def duree_clip(chemin):
    m = re.search(r"Duration: \d+:(\d+):([\d.]+)", _sonde(chemin))
    return int(m.group(1)) * 60 + float(m.group(2)) if m else 0.0


def images_par_seconde(chemin):
    m = re.search(r"([\d.]+) fps", _sonde(chemin))
    return float(m.group(1)) if m else None


def calibrer(voix, clip, sortie, amorce):
    """Ecrit une piste aussi longue que le clip : amorce de silence, la voix,
    puis du silence jusqu'au bout.

    POURQUOI, ET CE QUE CA A COUTE DE L'APPRENDRE
        Le 8 septembre 2026, premier envoi du plan 5 : clip de 4,04 s, voix de
        2,27 s, sync a renvoye 2,25 s. Il COUPE la video a la longueur de
        l'audio. Envoyes tels quels, les douze plans auraient perdu leur
        respiration -- ce silence avant et apres la replique qui fait qu'un
        plan ne commence pas sur la premiere syllabe.

        On aurait pu chercher un sync_mode dans leur API. Mais un parametre
        mal nomme y passe sans erreur, comme speed chez ElevenLabs, et on ne
        l'apprendrait qu'en regardant le resultat. Caler l'audio nous-memes ne
        depend de rien : la duree est la bonne parce que nous l'avons faite.

        C'est meme meilleur : pendant le silence, sync sait que la bouche doit
        etre fermee. Avec une piste tronquee, il n'en savait rien.

    L'AMORCE TOMBE QUAND LA VOIX NE TIENT PAS
        Le plan 13 dure 7,04 s et la replique d'Anna 7,08. Avec l'amorce, la
        piste faisait 7,43 s, coupee a 7,04 : quatre dixiemes de sa phrase
        partaient a la poubelle -- et le lip-sync s'est fait sur la version
        amputee. montage.py a toujours su ca (amorce = 0 quand ca ne rentre
        pas) ; ce script ne le savait pas encore, et rien ne s'en est plaint.
        C'est l'appelant qui decide maintenant, avec le meme calcul.
    """
    import imageio_ffmpeg
    ms = int(round(amorce * 1000))
    r = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner",
                        "-nostats", "-loglevel", "error", "-y", "-i", voix,
                        "-af", "adelay=%d:all=1,apad" % ms,
                        "-t", "%.3f" % duree_clip(clip),
                        "-ar", "44100", "-ac", "1", sortie],
                       capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        sys.exit("  calage audio echoue :\n%s" % r.stderr[-500:])
    return sortie


def raccourcir(clip, sortie, fin):
    """Coupe le clip a `fin` secondes, sans reencoder.

    POURQUOI AVANT L'ENVOI ET PAS APRES
        Sync facture a l'image. Envoyer la queue de silence, c'est payer pour
        synchroniser des images qu'on jettera au montage -- 35 % du metrage de
        l'episode 1. Couper d'abord coute zero et enleve la ligne de la
        facture.

        L'idee vient d'un conseil de Gemini le 8 septembre 2026. Elle differe
        de celle de ChatGPT le meme jour -- generer un clip plus court chez
        Seedance -- qui ne marche pas ici : le modele ne descend pas sous 4 s
        et nos repliques font 1,5 a 2,7 s.

        A NE FAIRE QU'UNE FOIS LE MONTAGE DECIDE. Un clip raccourci ne se
        rallonge pas, et la version aeree ne serait plus possible.
    """
    import imageio_ffmpeg
    r = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner",
                        "-nostats", "-loglevel", "error", "-y", "-i", clip,
                        "-t", "%.3f" % fin, "-c", "copy", "-an", sortie],
                       capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        sys.exit("  raccourcissement echoue :\n%s" % r.stderr[-500:])
    return sortie


def cle():
    chemin = os.path.join(RACINE, "sync.secret")
    c = (os.environ.get("SYNC_API_KEY") or "").strip()
    if not c and os.path.exists(chemin):
        c = io.open(chemin, encoding="utf-8").read().strip()
    if not c or len(c.split()) > 1 or len(c) < 20:
        sys.exit("  Cle absente ou mal formee. Colle-la seule sur une ligne dans\n"
                 "  sync.secret, a la racine du projet.")
    return c


def multipart(champs, fichiers):
    """Encode un corps multipart. urllib ne sait pas le faire, et ajouter une
    dependance pour trois lignes ne vaut pas le coup."""
    b = "----wortando" + uuid.uuid4().hex
    out = []
    for k, v in champs.items():
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                    % (b, k, v)).encode("utf-8"))
    for k, chemin in fichiers.items():
        nom = os.path.basename(chemin)
        typ = mimetypes.guess_type(nom)[0] or "application/octet-stream"
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"; filename=\"%s\"\r\n"
                    "Content-Type: %s\r\n\r\n" % (b, k, nom, typ)).encode("utf-8"))
        out.append(open(chemin, "rb").read())
        out.append(b"\r\n")
    out.append(("--%s--\r\n" % b).encode("utf-8"))
    return b"".join(out), "multipart/form-data; boundary=" + b


# Cloudflare renvoie 403 « error code: 1010 » sur la signature par defaut
# d'urllib -- « Python-urllib/3.x ». Ce n'est pas la cle qui est refusee, c'est
# le client : un agent ordinaire suffit a passer, et rien n'est soumis tant
# qu'on ne passe pas, donc l'echec ne coute rien.
AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
         "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def appel(url, cle_api, corps=None, typ=None, methode="GET"):
    req = urllib.request.Request(url, data=corps, method=methode,
                                 headers={"x-api-key": cle_api,
                                          "User-Agent": AGENT,
                                          "Accept": "application/json"})
    if typ:
        req.add_header("Content-Type", typ)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        raise RuntimeError("HTTP %d — %s" % (e.code, detail))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--modele", default="lipsync-2", choices=sorted(TARIF))
    ap.add_argument("--plans", help="n'en faire que ceux-la : 5 ou 5,6,8. "
                                    "A defaut, tous les plans parlants.")
    ap.add_argument("--amorce", type=float, default=None, metavar="SECONDES",
                    help="retard de la voix, au lieu des %.2f s de "
                         "montage.py. Sert quand la fenetre de parole du "
                         "clip ne tombe pas au debut." % AMORCE)
    ap.add_argument("--queue", type=float, default=None, metavar="SECONDES",
                    help="couper le clip SECONDES apres la fin de la replique "
                         "AVANT de l'envoyer -- meme valeur que montage.py")
    ap.add_argument("--essai", action="store_true",
                    help="ecrire dans _essais/<modele>-planNN.mp4 sans toucher "
                         "a etat.json ni au plan retenu -- pour comparer deux "
                         "modeles sur le meme plan avant d'engager les douze")
    ap.add_argument("--pour-de-vrai", action="store_true")
    a = ap.parse_args()

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    plans = [p for p in d["plans"] if p["type"] == "replique"]

    # UN PLAN D'ABORD, LES ONZE AUTRES ENSUITE. Le lip-sync se juge a l'oeil,
    # sur un visage, pas sur une facture : douze plans envoyes d'un coup se
    # paient avant qu'on sache si le modele tient sur des gros plans.
    if a.plans:
        voulus = {int(x) for x in a.plans.replace(" ", "").split(",") if x}
        inconnus = voulus - {p["n"] for p in plans}
        if inconnus:
            sys.exit("  Ces plans ne parlent pas, ou n'existent pas : %s"
                     % ", ".join(str(x) for x in sorted(inconnus)))
        plans = [p for p in plans if p["n"] in voulus]

    # L'arborescence de l'episode : les clips muets retenus sont dans
    # 03-final/, les plans synchronises vont a cote dans 04-lipsync/. On ne
    # remplace jamais un clip d'origine -- une prise Artlist ne se refait pas
    # a l'identique, et un lip-sync rate ne doit rien pouvoir ecraser.
    base = os.path.join(RACINE, "video", "episode-" + a.scene)
    src = os.path.join(base, "03-final")
    aud = os.path.join(RACINE, "audio", "scenes", a.scene)
    dst = os.path.join(RACINE, "video", "episode-" + a.scene, "04-lipsync")
    os.makedirs(dst, exist_ok=True)

    courts = os.path.join(RACINE, "video", "episode-" + a.scene,
                          "04-lipsync", "_clips-coupes")
    travail = []
    for p in plans:
        v = os.path.join(src, "plan%02d.mp4" % p["n"])
        s = os.path.join(aud, "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(v):
            sys.exit("  video manquante : 03-final/%s" % os.path.basename(v))
        if not os.path.exists(s):
            sys.exit("  audio manquant : %s" % os.path.basename(s))
        if a.queue is not None:
            fin = min(duree_clip(v), AMORCE + duree_clip(s) + a.queue)
            if fin < duree_clip(v) - 0.02:
                os.makedirs(courts, exist_ok=True)
                v = raccourcir(v, os.path.join(
                    courts, "plan%02d.mp4" % p["n"]), fin)
        travail.append((p, v, s))

    # On mesure les clips au lieu de croire le champ "duree" de la scene :
    # c'est le fichier envoye qui est facture, pas le plan prevu.
    ips = images_par_seconde(travail[0][1]) or 24.0
    total = sum(duree_clip(v) for _, v, _ in travail)
    images = int(round(total * ips))
    print("  %s — %d plans a synchroniser sur %d"
          % (d["situation"], len(travail), len(d["plans"])))
    fenetres = fenetres_machoire(base)
    for p, v, s_aud in travail:
        print("    plan%02d  %-5s %5.2f s  %s"
              % (p["n"], p["locuteur"], duree_clip(v), p.get("de", "")[:44]))
        # LE VERDICT AVANT LA DEPENSE. Le calage se decidait au moment de
        # l'envoi, donc apres avoir paye : on ne savait qu'un plan partait
        # decale qu'en regardant le resultat. Il est calcule ici, dans l'essai
        # a blanc, ou il ne coute rien et ou il peut encore faire renoncer.
        _, _, _, diag = placer_voix(s_aud, a.amorce, fenetres.get(p["n"]))
        print("            %s" % diag)
    print("  %.1f s a %.0f im/s = %d images" % (total, ips, images))
    print("  modele %s : %.5f $/image, soit environ %.2f $"
          % (a.modele, TARIF[a.modele], images * TARIF[a.modele]))
    if not a.pour_de_vrai:
        print("\n  Essai a blanc. Relancer avec --pour-de-vrai pour depenser.")
        return

    k = cle()
    cales = os.path.join(dst, "_audio-cale")
    os.makedirs(cales, exist_ok=True)
    # UN ESSAI NE S'INSTALLE PAS. Il ecrit a part et ne note rien : on compare
    # donc deux modeles sur le meme plan sans que le montage ramasse l'un ou
    # l'autre au passage, et sans qu'une relance croie le travail deja fait.
    if a.essai:
        dst = os.path.join(dst, "_essais")
        os.makedirs(dst, exist_ok=True)
    etat_f = os.path.join(dst, "etat.json")
    etat = ({} if a.essai else
            json.load(io.open(etat_f, encoding="utf-8"))
            if os.path.exists(etat_f) else {})

    def sauver():
        if a.essai:
            return
        io.open(etat_f, "w", encoding="utf-8", newline="").write(
            json.dumps(etat, ensure_ascii=False, indent=2) + "\n")

    # UN PLAN A LA FOIS. Le plan gratuit de sync.so n'autorise qu'une
    # generation simultanee : envoyer les douze d'un coup fait echouer la
    # deuxieme sur un 429, et les dix suivantes avec elle. On soumet donc,
    # on attend, on rapatrie, puis on passe au suivant.
    for p, v, s_aud in travail:
        n = str(p["n"])
        if etat.get(n, {}).get("fichier"):
            # ⚠️ « DEJA FAIT » NE VEUT RIEN DIRE SI LE CLIP SOURCE A CHANGE.
            #
            # Le 9 septembre 2026, le plan 05 a ete retourne : 03-final a recu
            # une nouvelle prise, mais etat.json disait encore COMPLETED et
            # 04-lipsync gardait l'ancienne. Une relance aurait saute le plan
            # en silence, et le montage aurait repris la vieille version --
            # apres 200 credits de re-tournage payes pour rien.
            #
            # On compare donc les dates : une source plus recente que le
            # resultat rend le travail perime. On ne l'efface pas tout seul,
            # une generation payee ne se jette pas sans qu'on le dise.
            fait = os.path.join(dst, etat[n]["fichier"])
            if os.path.exists(fait) and os.path.getmtime(v) > os.path.getmtime(fait):
                print("  plan%02d  PERIME : le clip de 03-final est plus recent"
                      " que le plan synchronise." % p["n"])
                print("           Pour le refaire : retirer l'entree \"%s\" de"
                      " 04-lipsync/etat.json" % n)
                print("           et supprimer 04-lipsync/%s" % etat[n]["fichier"])
                continue
            print("  plan%02d  deja fait" % p["n"])
            continue

        if not etat.get(n, {}).get("id"):
            # Meme calcul que montage.py : l'amorce saute des que la
            # replique ne tient plus dans le clip, sinon on lui coupe
            # la fin -- et le lip-sync se ferait sur la phrase amputee.
            #
            # ⚠️ L'AMORCE SE CALCULE SUR LA PAROLE, PAS SUR LE FICHIER.
            #
            # Le clip a ete tourne avec une consigne : bouche fermee jusqu'a
            # 0,5 s, parole ensuite pendant la duree du mp3. Cette duree
            # comptait le silence des deux bouts -- 0,29 s de trop par plan en
            # moyenne, 2,33 s sur le plan 13. La machoire de Seedance parle
            # donc plus longtemps que la voix, et poser la voix au ras du
            # debut laisse tout l'ecart s'accumuler A LA FIN, la ou Jacques
            # l'a vu : « la bouche continue un petit peu ».
            #
            # On ne peut pas retimer une machoire deja tournee. On peut la
            # CENTRER : la parole est placee au milieu de la fenetre que le
            # modele a recue, ce qui coupe l'ecart en deux et le partage entre
            # le debut et la fin. Une machoire qui demarre un dixieme trop tot
            # se lit comme une inspiration ; une machoire qui continue apres
            # le dernier mot se lit comme un defaut.
            #
            # Quand le clip aura ete tourne avec la fenetre corrigee (voir
            # production.duree_voix), l'ecart sera nul et ce calcul rendra
            # simplement l'amorce d'origine.
            # LE REPERE EST 0,5 s, PAS L'AMORCE. C'est le chiffre ecrit dans
            # le prompt (production.bouche : « from 0.5 to X seconds:
            # speaking »), donc celui que la machoire a recu. L'amorce du
            # montage, elle, vaut 0,35 -- deux nombres differents pour deux
            # choses differentes, et les confondre decale la voix du mauvais
            # cote. La fenetre de la machoire est donc [0,5 ; 0,5 + fichier].
            am, tete, parlee, diag = placer_voix(s_aud, a.amorce,
                                                 fenetres.get(p["n"]))
            if duree_clip(s_aud) + max(am, 0.0) > duree_clip(v):
                am = 0.0
                print("  (amorce retiree, la replique remplit le plan)")
            elif am < 0:
                am = 0.0
            print("  plan%02d  la parole tombe a %.2f s (amorce %.2f) -- %s"
                  % (p["n"], am + tete, am, diag))
            cale = calibrer(s_aud, v, os.path.join(cales, "%02d.wav" % p["n"]),
                            am)
            corps, typ = multipart({"model": a.modele}, {"video": v, "audio": cale})
            print("  plan%02d envoi..." % p["n"], end="", flush=True)
            r = appel(API, k, corps, typ, "POST")
            etat[n] = {"id": r.get("id"), "statut": r.get("status")}
            sauver()   # AVANT tout le reste : un identifiant perdu est une generation payee deux fois
            print(" %s" % (r.get("id") or "?")[:8], end="", flush=True)

        debut = time.time()
        while time.time() - debut < 900:
            time.sleep(10)
            r = appel(API + "/" + etat[n]["id"], k)
            st = r.get("status")
            etat[n]["statut"] = st
            sauver()
            if st == "COMPLETED" and r.get("outputUrl"):
                f = os.path.join(dst, ("%s-plan%02d.mp4" % (a.modele, p["n"]))
                                 if a.essai else "plan%02d.mp4" % p["n"])
                dl = urllib.request.Request(r["outputUrl"], headers={"User-Agent": AGENT})
                with urllib.request.urlopen(dl, timeout=300) as w:
                    open(f, "wb").write(w.read())
                etat[n]["fichier"] = os.path.basename(f)
                sauver()
                print("  ->  %d Ko" % (os.path.getsize(f) // 1024))
                break
            if st in ("FAILED", "REJECTED"):
                etat[n]["erreur"] = r.get("error") or st
                sauver()
                print("  ->  ECHEC : %s" % etat[n]["erreur"])
                break
        else:
            print("  ->  toujours en cours apres 15 min, on passe")

    faits = [x for x in etat.values() if x.get("fichier")]
    print("\n  %d/%d plans synchronises dans video/episode-%s/04-lipsync/"
          % (len(faits), len(travail), a.scene))
    if len(faits) == len(travail):
        print("  montage.py les prend tout seul : il regarde 04-lipsync avant 03-final.")
    for n, x in sorted(etat.items(), key=lambda y: int(y[0])):
        if not x.get("fichier"):
            print("     plan%02s : %s" % (n, x.get("erreur") or x.get("statut")))


if __name__ == "__main__":
    main()
