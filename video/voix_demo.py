# -*- coding: utf-8 -*-
"""LA VOIX DE LA DEMO -- une phrase par plan, posee sur le montage muet.

    python video/voix_demo.py --langue en
    python video/voix_demo.py --langue en --voix "Microsoft Zira Desktop"

⚠️ UNE PHRASE PAR PLAN, ET LA PHRASE NE DEBORDE PAS. Chaque ligne est calee sur
le DEBUT de son plan, mesure sur les morceaux que montage_demo.py vient de
rendre -- pas sur les durees ecrites dans PLANS, qui sont des consignes, pas
des faits (un clip plus court que demande raccourcit son plan). Si une phrase
depasse son plan, le script le DIT : c'est au texte de raccourcir, jamais au
plan de s'etirer pour l'accueillir.

⚠️ LA VOIX D'ICI EST GRATUITE ET LOCALE (SAPI, la synthese de Windows). Elle
sert a entendre le RYTHME : est-ce que la phrase tient, est-ce qu'elle tombe au
bon moment, est-ce qu'il manque un silence. Elle ne sert pas a livrer --
ElevenLabs viendra quand le texte sera arrete, et une seule fois par langue.
Payer une voix pour un montage qui bouge encore, c'est payer deux fois.

⚠️ ET ON N'ECRIT AUCUN CHIFFRE DANS LA NARRATION. Trente cartes, sept cents
carreaux, quatre-vingt-treize pour cent : chacun est une valeur qui bouge ou
qui depend d'un reglage, et chacun se paierait six fois en reenregistrement.
Les chiffres sont a l'image, ou ils sont toujours justes.
"""
import argparse
import hashlib
import io as _io
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Une phrase par plan, dans l'ordre de PLANS (montage_demo.py). None = le plan
# se passe de voix -- la carte-titre, par exemple : le nom se lit, il ne
# s'annonce pas.
NARRATION = {
    "en": [
        "Every card refines a painting. On the last one, it's yours.",
        "Each day, a session waits. You pick the level; the app picks the words.",
        "You answer. Hard words come back sooner.",
        "And when you can't look, you listen.",
        "A word you don't have is already in the app. And it becomes a card.",
        "Something missing? Tell us.",
        None,
    ],
    "fr": [
        "Chaque carte affine un tableau du monde germanophone. À la dernière, il est à toi.",
        "Chaque jour, une séance t'attend. Tu choisis le niveau et combien de cartes ; l'app choisit lesquelles.",
        "Tu réponds. Ce qui résiste revient plus souvent, ce qui est acquis s'espace.",
        "Et quand tu ne peux pas regarder, tu écoutes. Dans l'autobus, en marchant.",
        "Un mot te manque ? Il est déjà dans l'app, et il devient une carte.",
        "Et s'il manque quelque chose, tu nous le dis. D'ici.",
        None,
    ],
}

VOIX_DEFAUT = {"en": "Microsoft Zira Desktop", "fr": None}

# Les voix d'ElevenLabs, par leur identifiant. Trois candidates anglaises sur
# la MEME phrase, ecoutees cote a cote : c'est la methode qui a choisi la voix
# de Mark le 7 septembre, et c'est la seule qui tranche quelque chose.
VOIX_ELEVEN = {
    "rachel": "21m00Tcm4TlvDq8ikWAM",
    "bella": "EXAVITQu4vr4xnSDxMaL",
    "adam": "pNInz6obpgDQGcFmaJgB",
    "aurora": "8HePnvwzEdJ614CQMPqF",   # la voix allemande de l'app
}
MODELE_ELEVEN = "eleven_multilingual_v2"

# ⚠️ LE SOURIRE SE REGLE, IL NE SE DEMANDE PAS. Demande de Jacques : << plus
# detendu, plus souriant >>. Sous eleven_multilingual_v2, il n'y a pas de
# balise de jeu -- v2 les PRONONCERAIT. Ce qui detend la diction, ce sont deux
# curseurs : la stabilite qui descend (la voix varie au lieu de reciter) et le
# style qui monte (elle s'autorise l'intonation). A 0,75/0,00 -- le reglage du
# corpus du cours -- la lecture est nette et plate : c'est ce qu'il faut pour
# 25 298 mots de vocabulaire, et l'inverse de ce qu'il faut pour une narration.
# ⚠️ NE PAS DESCENDRE LA STABILITE PLUS BAS QUE ~0,30 : au-dela la voix
# commence a changer de couleur d'une phrase a l'autre, et six phrases montees
# bout a bout ne sonnent plus comme la meme personne.
TONS = {
    "neutre":   {"stability": 0.75, "similarity_boost": 0.75,
                 "style": 0.00, "use_speaker_boost": True},
    "souriant": {"stability": 0.35, "similarity_boost": 0.75,
                 "style": 0.55, "use_speaker_boost": True},
}


def cle_eleven():
    cle = (os.environ.get("ELEVENLABS_API_KEY") or "").strip()
    if not cle:
        chemin = RACINE / "elevenlabs.secret"
        if chemin.exists():
            cle = _io.open(chemin, encoding="utf-8").read().strip()
    return cle or None


def dire_eleven(texte, voix_id, cle, cible, ton="souriant"):
    """Une phrase chez ElevenLabs, et JAMAIS DEUX FOIS LA MEME.

    ⚠️ LE CACHE EST LA POUR L'ARGENT, PAS POUR LA VITESSE. Le montage se refait
    dix fois par soiree ; sans empreinte, chaque relance repaierait les six
    phrases. Le nom du fichier porte l'empreinte de (voix + texte) : changer un
    mot regenere cette ligne-la, et elle seule."""
    # ⚠️ LE TON ENTRE DANS L'EMPREINTE. Sans lui, changer de reglage ressort le
    # fichier d'avant : on croit avoir change la voix, on a change un argument.
    reglages = TONS.get(ton, TONS["souriant"])
    empreinte = hashlib.sha1(
        (voix_id + "|" + ton + "|" + json.dumps(reglages, sort_keys=True) + "|" + texte)
        .encode("utf-8")).hexdigest()[:12]
    garde = cible.with_name(cible.stem + "-" + empreinte + ".mp3")
    if garde.exists() and garde.stat().st_size > 2000:
        return garde
    url = ("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_128"
           % voix_id)
    charge = json.dumps({"text": texte, "model_id": MODELE_ELEVEN,
                         "voice_settings": reglages}).encode("utf-8")
    req = urllib.request.Request(url, data=charge, method="POST", headers={
        "xi-api-key": cle, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            garde.write_bytes(r.read())
    except urllib.error.HTTPError as e:
        sys.exit("ElevenLabs a refuse (HTTP %d) : %s"
                 % (e.code, e.read().decode("utf-8", "replace")[:200]))
    return garde


def ffmpeg(args):
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + args)
    if r.returncode != 0:
        sys.exit("ffmpeg a echoue : " + " ".join(args[:6]))


def duree(fichier):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(fichier)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def dire(texte, voix, vitesse, cible):
    """Fabrique un WAV avec la synthese de Windows.

    ⚠️ LE TEXTE PASSE PAR UN FICHIER, JAMAIS PAR LA LIGNE DE COMMANDE. Une
    apostrophe ou un accent dans un argument PowerShell se fait manger ou
    casser selon l'encodage de la console -- et la phrase arrive tronquee sans
    que rien ne le signale."""
    dit = cible.with_suffix(".txt")
    dit.write_text(texte, encoding="utf-8")
    script = (
        "Add-Type -AssemblyName System.Speech; "
        "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        + (("$s.SelectVoice('%s'); " % voix) if voix else "")
        + "$s.Rate = %d; " % vitesse
        + "$s.SetOutputToWaveFile('%s'); " % str(cible).replace("\\", "\\\\")
        + "$t = [IO.File]::ReadAllText('%s', [Text.Encoding]::UTF8); " % str(dit).replace("\\", "\\\\")
        + "$s.Speak($t); $s.Dispose()"
    )
    subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", script],
                   check=False, capture_output=True)
    dit.unlink(missing_ok=True)
    return cible.exists() and cible.stat().st_size > 1000


def main():
    a = argparse.ArgumentParser(description="Pose la narration sur le montage muet.")
    a.add_argument("--langue", default="en")
    a.add_argument("--appareil", default="iphone67")
    a.add_argument("--voix", default=None)
    a.add_argument("--moteur", default="eleven", choices=["eleven", "sapi"],
                   help="eleven : ElevenLabs (payant, pour livrer). "
                        "sapi : la synthese de Windows (gratuite, pour juger le rythme)")
    # Bella : choisie par Jacques le 20 septembre 2026, apres ecoute des trois
    # candidates sur la meme phrase.
    a.add_argument("--ton", default="souriant", choices=sorted(TONS),
                   help="souriant : detendu, intonation libre. neutre : la diction "
                        "nette et plate du corpus du cours")
    a.add_argument("--voix-eleven", default="bella",
                   help="nom court (rachel, bella, adam, aurora) ou identifiant")
    a.add_argument("--vitesse", type=int, default=0, help="SAPI : -10 (lent) a 10 (rapide)")
    a.add_argument("--film", default=None, help="le montage muet a sonoriser")
    a.add_argument("--sortie", default=None)
    args = a.parse_args()

    lignes = NARRATION.get(args.langue)
    if not lignes:
        sys.exit("Pas de narration ecrite pour : " + args.langue)

    base = RACINE / "video" / "demo" / args.langue
    travail = base / args.appareil / "_montage"
    if not travail.exists():
        sys.exit("Monter d'abord le film muet :\n"
                 "  python video/montage_demo.py --langue %s --immobile --transition coupe" % args.langue)

    # Les morceaux, dans l'ordre : ce sont eux qui donnent les vrais decalages.
    morceaux = sorted(p for p in travail.glob("*.mp4") if "-pont" not in p.name)
    film = Path(args.film) if args.film else base / ("wortando-demo-v12-%s.mp4" % args.langue)
    if not film.exists():
        candidats = sorted(base.glob("wortando-demo-*%s.mp4" % args.langue),
                           key=lambda f: f.stat().st_mtime)
        if not candidats:
            sys.exit("Aucun montage muet trouve dans " + str(base))
        film = candidats[-1]

    voix = args.voix or VOIX_DEFAUT.get(args.langue)
    voix_id = VOIX_ELEVEN.get(args.voix_eleven, args.voix_eleven)
    cle = None
    if args.moteur == "eleven":
        cle = cle_eleven()
        if not cle:
            sys.exit("Pas de cle ElevenLabs. Pour juger le rythme sans payer : --moteur sapi")
    sons = base / ("_voix-" + (args.voix_eleven + "-" + args.ton
                               if args.moteur == "eleven" else "sapi"))
    sons.mkdir(exist_ok=True)

    entrees, filtres, etiquettes = ["-i", str(film)], [], []
    debut = 0.0
    depassements = []
    for i, morceau in enumerate(morceaux):
        d = duree(morceau)
        texte = lignes[i] if i < len(lignes) else None
        if texte:
            if args.moteur == "eleven":
                piste = dire_eleven(texte, voix_id, cle, sons / ("%02d" % i), args.ton)
            else:
                piste = sons / ("%02d.wav" % i)
                if not dire(texte, voix, args.vitesse, piste):
                    sys.exit("La synthese n'a rien produit pour le plan %d" % i)
            parle = duree(piste)
            # ⚠️ UN SOUFFLE AVANT DE PARLER : la voix qui demarre sur la coupe
            # se colle au plan precedent et on entend une phrase coupee en
            # deux. 0,25 s suffit a ce que l'oreille change de plan avec l'oeil.
            depart = debut + 0.25
            if parle > d - 0.15:
                depassements.append((i, round(parle, 2), round(d, 2), texte))
            entrees += ["-i", str(piste)]
            filtres.append("[%d:a]adelay=%d|%d[v%d]" % (len(etiquettes) + 1,
                                                        int(depart * 1000), int(depart * 1000), i))
            etiquettes.append("[v%d]" % i)
        debut += d

    if not etiquettes:
        sys.exit("Aucune phrase a poser.")

    melange = "".join(etiquettes) + "amix=inputs=%d:normalize=0[voix]" % len(etiquettes)
    sortie = Path(args.sortie) if args.sortie else base / ("wortando-demo-voix-%s.mp4" % args.langue)
    ffmpeg(entrees + ["-filter_complex", ";".join(filtres + [melange]),
                      "-map", "0:v", "-map", "[voix]",
                      "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", str(sortie)])

    print("%s  (%d phrases)" % (sortie, len(etiquettes)))
    for i, parle, plan, texte in depassements:
        print("  DEBORDE  plan %d : %.2f s de voix pour %.2f s d'image" % (i, parle, plan))
        print("           %s" % texte)
    if depassements:
        print("  -> raccourcir le TEXTE, pas etirer le plan : un plan etire pour")
        print("     accueillir une phrase est un plan qui traine a l'image.")


if __name__ == "__main__":
    main()
