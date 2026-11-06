"""Les voix de radio du DTZ (Hoeren, Teil 2 et 4) : chercher, puis faire entendre a Jacques.

    python visuel/prototype/dtz/outils/voix_radio.py --chercher
        Liste les voix allemandes de la bibliotheque ElevenLabs (gratuit, aucun credit) et garde les candidates
        dans outils/voix_radio_candidates.json.
    python visuel/prototype/dtz/outils/voix_radio.py --echantillons --pour-de-vrai
        Fait dire LA MEME phrase de radio a chaque candidate (multilingual v2 seulement), anonymisee A, B, C... :
        quelques centaines de credits, dans l'enveloppe accordee par Jacques le 4 nov. 2026 (« Oui, les deux »).
        Les fichiers vont dans outils/echantillons/ (hors depot), la cle du comparatif a cote.

POURQUOI NOTRE PHRASE ET PAS L'EXTRAIT DE LA BIBLIOTHEQUE : l'extrait est souvent en anglais, ou dit autre chose
qu'une annonce. Jacques juge une voix sur ce qu'elle dira dans l'examen, et toutes disent la meme chose, a sonie
egale : la seule difference entendue est la voix (methode du comparatif d'Aurora, 3 sept.).

La cle ElevenLabs est lue comme le fait audio/generer.py (variable ELEVENLABS_API_KEY ou elevenlabs.secret a la
racine du depot principal) ; elle n'est jamais affichee.
"""
import argparse
import io
import json
import os
import sys
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ICI))))
PRINCIPAL = os.path.normpath(os.path.join(DEPOT, "..", "..", ".."))   # le worktree vit dans .claude/worktrees/<nom>
CANDIDATES = os.path.join(ICI, "voix_radio_candidates.json")
ECHANTILLONS = os.path.join(ICI, "echantillons")

PHRASE = ("Das Wetter für Berlin und Brandenburg: Heute Vormittag regnet es noch, am Nachmittag wird es trocken, "
          "bei Temperaturen um zehn Grad. Morgen gibt es viel Sonne, aber nur fünf Grad.")


def cle():
    c = (os.environ.get("ELEVENLABS_API_KEY") or "").strip()
    for racine in (DEPOT, PRINCIPAL):
        if c:
            break
        chemin = os.path.join(racine, "elevenlabs.secret")
        if os.path.exists(chemin):
            c = io.open(chemin, encoding="utf-8").read().strip()
    if not c:
        sys.exit("Cle ElevenLabs absente.")
    return c


def api(chemin, k):
    req = urllib.request.Request("https://api.elevenlabs.io" + chemin, headers={"xi-api-key": k})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def chercher():
    k = cle()
    garde = []
    for genre in ("male", "female"):
        for usage in ("informative_educational", "narrative_story", ""):
            q = {"page_size": "40", "language": "de", "gender": genre, "sort": "usage_character_count_1y"}
            if usage:
                q["use_cases"] = usage
            d = api("/v1/shared-voices?" + urllib.parse.urlencode(q), k)
            for v in d.get("voices", []):
                if any(g["voice_id"] == v["voice_id"] for g in garde):
                    continue
                garde.append({"voice_id": v["voice_id"], "public_owner_id": v.get("public_owner_id"), "nom": v.get("name"),
                              "genre": genre, "age": v.get("age"), "accent": v.get("accent"), "usage": v.get("use_case"),
                              "descriptif": (v.get("description") or "")[:160], "langue": v.get("language"),
                              "utilisations": v.get("cloned_by_count"), "caracteres_1an": v.get("usage_character_count_1y")})
    io.open(CANDIDATES, "w", encoding="utf-8").write(json.dumps(garde, ensure_ascii=False, indent=1))
    for g in garde:
        print("%-6s %-28s %-10s %-14s %s" % (g["genre"], (g["nom"] or "")[:28], g["age"] or "", g["accent"] or "", g["descriptif"][:70]))
    print("\n%d voix gardees dans %s" % (len(garde), os.path.relpath(CANDIDATES, DEPOT)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chercher", action="store_true")
    a = ap.parse_args()
    if a.chercher:
        chercher()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
