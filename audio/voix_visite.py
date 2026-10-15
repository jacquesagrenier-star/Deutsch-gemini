# La voix de la visite guidee (v702) : un clip par page narree et par langue
# d'interface, dans voix-visite/<langue>/<clip>.mp3.
#
# LES TEXTES VIENNENT D'index.html, ET DE NULLE PART AILLEURS. La voix doit dire
# mot pour mot ce que la page affiche : le script relit les cles dec_* de I18N
# et compose chaque clip comme la page compose son ecran (titre, puis texte).
# Une copie des textes ici aurait diverge au premier mot change.
#
# Il ne refait que ce qui a change : voix-visite/textes.json garde l'empreinte
# du texte de chaque clip. Apres une regeneration, monter VOIX_VISITE.revision
# dans index.html, sinon les telephones gardent l'ancien fichier en cache.
#
# Voix Charlotte (choisie a l'aveugle par Jacques le 3 octobre 2026, avec
# « l'application » plutot que « l'app », qu'elle prononcait « lappe »).
# Modele multilingual v2, sauf le persan : seul eleven_v3 l'annonce.
# Puis ffmpeg ramene chaque clip a -16 LUFS, en mono : ElevenLabs sort autour de
# -25 LUFS, nettement plus bas que la voix allemande (voir VOLUME_SYNTHESE).
#
# La cle d'API est lue dans elevenlabs.secret (ignore par git), jamais affichee.
import hashlib, json, pathlib, re, subprocess, sys, tempfile, urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "voix-visite"
VOIX = "XB0fDUnXU5powFXDhCwa"   # Charlotte
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt"]   # celles qui ont une voix
# L'ordre des blocs de I18N, toutes langues : le polonais et le russe (v778,
# v779) ont leurs textes mais pas encore de voix de visite.
BLOCS = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
MODELE = {"fa": "eleven_v3"}
MODELE_DEFAUT = "eleven_multilingual_v2"

# clip -> cles dont il dit le texte, dans l'ordre de l'ecran
CLIPS = {
    "intro":   ["dec_t0_titre", "dec_t0_texte"],
    "t4":      ["dec_t4_titre", "dec_t4_texte"],
    "d1":      ["dec_t4_d1"],
    "d2":      ["dec_t4_d2"],
    "d3":      ["dec_t4_d3"],
    "d4":      ["dec_t4_d4"],
    "d5":      ["dec_t4_d5"],
    "pretour": ["dec_t4_pretour"],
    # v806 : la scene a toucher (etape 5). Les clips t5 et t6 gardent leur nom
    # (la seance et la fin, etapes 6 et 7 depuis) : CLIPS_DE_PAGE dans index.html.
    "scene":   ["dec_ts_titre", "dec_ts_texte"],
    "t5":      ["dec_t5_titre", "dec_t5_texte"],
    "t6":      ["dec_t6_titre", "dec_t6_texte"],
}


def textes_de_l_app():
    html = (RACINE / "index.html").read_text(encoding="utf-8")
    par_langue = {l: {} for l in LANGUES}
    for cle in {c for cles in CLIPS.values() for c in cles}:
        valeurs = re.findall(r'^        ' + re.escape(cle) + r': (".*"),$', html, re.M)
        if len(valeurs) != len(BLOCS):
            sys.exit(f"{cle} : {len(valeurs)} valeurs au lieu de {len(BLOCS)}")
        for l, v in zip(BLOCS, valeurs):
            if l not in par_langue:
                continue
            par_langue[l][cle] = json.loads(v)
    return par_langue


def composer(morceaux):
    # Un titre sans ponctuation finale recoit un point : la voix marque la pause.
    sortie = []
    for m in morceaux:
        m = m.strip()
        if m and m[-1] not in ".!?…؟":
            m += "."
        sortie.append(m)
    return " ".join(sortie)


def generer(texte, langue, cle):
    corps = {"text": texte, "model_id": MODELE.get(langue, MODELE_DEFAUT)}
    if langue in MODELE:
        corps["language_code"] = langue
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOIX}?output_format=mp3_44100_128",
        data=json.dumps(corps).encode("utf-8"),
        headers={"xi-api-key": cle, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def normaliser(brut, cible):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(brut)
        source = f.name
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", source,
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ac", "1",
                    "-ar", "44100", "-b:a", "64k", str(cible)], check=True)
    pathlib.Path(source).unlink()


# LA VISITE ESPAGNOLE (v759) : seuls les clips dont le texte differe ont les
# leurs, dans voix-visite/es/<langue>/ -- les autres sont ceux de l'allemand,
# qui disent le meme texte. Langues de l'interface espagnole : fr et en.
# Doit suivre CLIPS_PROPRES_ES dans index.html.
CLIPS_PROPRES_ES = ["intro", "t4", "d5"]
LANGUES_ES = ["fr", "en"]


def textes_espagnols(textes):
    """Les textes de la visite espagnole : I18N_ESPAGNOL d'abord, l'allemand sinon."""
    html = (RACINE / "index.html").read_text(encoding="utf-8")
    a = "const I18N_ESPAGNOL = "
    i = html.index(a) + len(a)
    j = html.index(';\nif(LANGUE_APPRISE === "es"){', i)
    es = json.loads(html[i:j])
    return {l: dict(textes[l], **es.get(l, {})) for l in LANGUES_ES}


def main():
    # --a-blanc : dit ce qui serait refait, et combien de caracteres, sans
    # rien demander a ElevenLabs.
    a_blanc = "--a-blanc" in sys.argv
    cle = None if a_blanc else (RACINE / "elevenlabs.secret").read_text(encoding="utf-8").strip()
    textes = textes_de_l_app()
    manifeste_f = SORTIE / "textes.json"
    manifeste = json.loads(manifeste_f.read_text(encoding="utf-8")) if manifeste_f.exists() else {}
    taches = [(langue, langue, clip, cles, textes[langue], SORTIE / langue)
              for langue in LANGUES for clip, cles in CLIPS.items()]
    es = textes_espagnols(textes)
    taches += [("es-" + langue, langue, clip, CLIPS[clip], es[langue], SORTIE / "es" / langue)
               for langue in LANGUES_ES for clip in CLIPS_PROPRES_ES]
    caracteres = 0
    for cle_manifeste, langue, clip, cles, t, dossier in taches:
        texte = composer([t[c] for c in cles])
        empreinte = hashlib.sha1(texte.encode("utf-8")).hexdigest()
        cible = dossier / f"{clip}.mp3"
        if cible.exists() and manifeste.get(cle_manifeste, {}).get(clip) == empreinte:
            continue
        caracteres += len(texte)
        if a_blanc:
            print(cle_manifeste, clip, len(texte), "caracteres")
            continue
        dossier.mkdir(parents=True, exist_ok=True)
        normaliser(generer(texte, langue, cle), cible)
        manifeste.setdefault(cle_manifeste, {})[clip] = empreinte
        print(cle_manifeste, clip, "fait")
        manifeste_f.write_text(json.dumps(manifeste, indent=1), encoding="utf-8")
    print(caracteres, "caracteres", "a generer" if a_blanc else "generes")


if __name__ == "__main__":
    main()
