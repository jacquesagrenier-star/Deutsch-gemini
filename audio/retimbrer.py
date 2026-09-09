# -*- coding: utf-8 -*-
"""Change la VOIX d'une piste sans toucher a son minutage (Speech-to-Speech).

    python audio/retimbrer.py --video "C:/.../clip.mp4"
    python audio/retimbrer.py --video ... --sortie essais/plan16-aurora.mp4

POURQUOI CE SCRIPT EXISTE
    Seedance fabrique l'image et le son dans la meme passe : sa bouche est
    faite sur SA voix. Toute la journee du 9 septembre 2026 on a essaye de lui
    faire suivre la notre -- sync.so d'abord, la voix en reference ensuite --
    et il n'y arrive qu'a peu pres : attaque decalee de 0,35 s, et articulation
    etiree de 0,60 s sur la replique la plus longue.

    L'autre sens ne peut pas rater. On prend la piste que Seedance a generee,
    celle sur laquelle sa bouche a ete construite, et on n'en change QUE LE
    TIMBRE. Meme onde, memes attaques, memes pauses, autre voix. Le decalage
    est mecaniquement impossible : c'est le meme son.

CE QU'IL FAUT ECOUTER, ET C'EST TOUT LE RISQUE
    Le Speech-to-Speech conserve la prononciation de la source. Si Seedance
    bafouille << ihrere Hilfe >>, Aurora bafouillera << ihrere Hilfe >> avec un
    joli timbre. Pour une application qui ENSEIGNE l'allemand, une prononciation
    approximative n'est pas un defaut de rendu : c'est la lecon qui devient
    fausse.

    Ce script ne juge donc rien. Il fabrique le clip a ecouter.
"""
import argparse
import io
import json
import os
import subprocess
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
sys.path.insert(0, os.path.join(RACINE, "video"))
import generer as G                                         # noqa: E402
import montage as M                                         # noqa: E402

API = "https://api.elevenlabs.io/v1/speech-to-speech/%s?output_format=mp3_44100_192"

# ⚠️ LE MODELE DOIT ETRE LE MULTILINGUE. Premier essai du 9 septembre 2026 fait
# avec eleven_english_sts_v2 -- le modele ANGLAIS -- sur de l'allemand. Jacques :
# « la voix est differente, c'est moins clair, moins comprehensible ». Un modele
# de conversion entraine sur une autre langue rend les phonemes qu'il connait,
# pas ceux qu'il entend.
MODELE = "eleven_multilingual_sts_v2"

# La conversion garde le minutage quel que soit le reglage ; ce qui se joue ici,
# c'est la nettete. stability haute = moins d'invention, similarity haute = plus
# proche de la voix cible. Pour une application qui enseigne la prononciation,
# on veut de la tenue, pas de l'expressivite.
REGLAGES = {"stability": 0.75, "similarity_boost": 0.9, "style": 0.0,
            "use_speaker_boost": True}


def multipart(champs, fichiers):
    import uuid
    b = "----wortando" + uuid.uuid4().hex
    out = []
    for k, v in champs.items():
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                    % (b, k, v)).encode("utf-8"))
    for k, chemin in fichiers.items():
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"; "
                    "filename=\"%s\"\r\nContent-Type: audio/mpeg\r\n\r\n"
                    % (b, k, os.path.basename(chemin))).encode("utf-8"))
        out.append(open(chemin, "rb").read())
        out.append(b"\r\n")
    out.append(("--%s--\r\n" % b).encode("utf-8"))
    return b"".join(out), "multipart/form-data; boundary=" + b


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--video", required=True, help="le clip Seedance, avec son son")
    p.add_argument("--plan", type=int,
                   help="le numero du plan : la voix du locuteur est prise "
                        "dans la scene. SANS LUI on retimbre avec Aurora, qui "
                        "est la voix de l'Erzaehler -- et Mark parlerait avec "
                        "une voix de femme. C'est arrive le 9 septembre 2026.")
    p.add_argument("--scene", default="01-ankunft-berlin")
    p.add_argument("--voix", help="ou bien un voice_id explicite")
    p.add_argument("--modele", default=MODELE,
                   help="eleven_multilingual_sts_v2 par defaut ; le modele "
                        "anglais massacre l'allemand.")
    p.add_argument("--debruiter", action="store_true",
                   help="retirer le fond sonore du hall. Un debruiteur mange "
                        "souvent les consonnes : a n'activer que si le fond "
                        "s'entend vraiment.")
    p.add_argument("--sortie", help="le mp4 a ecrire")
    a = p.parse_args()

    if not os.path.exists(a.video):
        sys.exit("  Introuvable : %s" % a.video)

    voix, qui = a.voix, "voice_id fourni"
    if a.plan:
        d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                              encoding="utf-8"))
        p_ = next((x for x in d["plans"] if x["n"] == a.plan), None)
        if not p_:
            sys.exit("  Le plan %d n'existe pas dans %s." % (a.plan, a.scene))
        loc = d["locuteurs"].get(p_["locuteur"], {})
        if not loc.get("voice_id"):
            sys.exit("  Pas de voice_id pour %s." % p_["locuteur"])
        voix, qui = loc["voice_id"], "%s (%s)" % (loc.get("nom", p_["locuteur"]),
                                                  loc.get("voix", ""))
    if not voix:
        sys.exit("  Preciser --plan (recommande) ou --voix.")
    print("  voix : %s   modele : %s" % (qui, a.modele))
    F = M.ffmpeg()
    tmp = os.path.join(RACINE, "essais", "retimbrage")
    os.makedirs(tmp, exist_ok=True)
    base = os.path.splitext(os.path.basename(a.video))[0][:40]

    # 1. Extraire la piste de Seedance, telle quelle.
    src = os.path.join(tmp, base + "-seedance.mp3")
    subprocess.run([F, "-y", "-v", "error", "-i", a.video, "-map", "0:a",
                    "-ar", "44100", "-ac", "1", "-b:a", "128k", src], check=True)
    d0, d1, tot = M.parole(F, src, seuil=0.10)
    print("  piste de Seedance : %.2f s, parole de %.2f a %.2f s" % (tot, d0, d1))

    # 2. La retimbrer chez ElevenLabs.
    corps, typ = multipart({"model_id": a.modele,
                            "remove_background_noise": "true" if a.debruiter else "false",
                            "voice_settings": json.dumps(REGLAGES)},
                           {"audio": src})
    req = urllib.request.Request(API % voix, data=corps, method="POST",
                                 headers={"xi-api-key": G.cle_api(),
                                          "Content-Type": typ,
                                          "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            son = r.read()
    except urllib.error.HTTPError as e:
        sys.exit("  ElevenLabs a refuse (%s) :\n%s"
                 % (e.code, e.read().decode("utf-8", "replace")[:600]))
    neuf = os.path.join(tmp, base + "-retimbre.mp3")
    open(neuf, "wb").write(son)
    e0, e1, etot = M.parole(F, neuf, seuil=0.10)
    print("  piste retimbree   : %.2f s, parole de %.2f a %.2f s" % (etot, e0, e1))
    print("  ecart d'attaque   : %+.2f s        ecart de fin : %+.2f s"
          % (e0 - d0, e1 - d1))
    if abs(e0 - d0) > 0.12 or abs(e1 - d1) > 0.15:
        print("  ⚠️ le minutage a bouge -- la promesse du procede est justement")
        print("     qu'il ne bouge pas. A regarder avant d'en faire une chaine.")

    # 3. Reposer sur l'image, a la place exacte.
    out = a.sortie or os.path.join(tmp, base + "-retimbre.mp4")
    subprocess.run([F, "-y", "-v", "error", "-i", a.video, "-i", neuf,
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", out], check=True)
    print("  ->  %s" % os.path.relpath(out, RACINE))
    print("  A ECOUTER : l'allemand est-il assez propre pour etre enseigne ?")


if __name__ == "__main__":
    main()
