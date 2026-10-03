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
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar"]   # ordre des blocs de I18N
MODELE = {"fa": "eleven_v3"}
MODELE_DEFAUT = "eleven_multilingual_v2"

# clip -> cles dont il dit le texte, dans l'ordre de l'ecran
CLIPS = {
    "intro":   ["dec_t0_titre", "dec_t0_texte"],
    "t4":      ["dec_t4_titre", "dec_t4_texte"],
    "p1":      ["dec_t4_p1"],
    "p2":      ["dec_t4_p2"],
    "pfin":    ["dec_t4_pfin"],
    "pretour": ["dec_t4_pretour"],
    "t5":      ["dec_t5_titre", "dec_t5_texte"],
    "t6":      ["dec_t6_titre", "dec_t6_texte"],
}


def textes_de_l_app():
    html = (RACINE / "index.html").read_text(encoding="utf-8")
    par_langue = {l: {} for l in LANGUES}
    for cle in {c for cles in CLIPS.values() for c in cles}:
        valeurs = re.findall(r'^        ' + re.escape(cle) + r': (".*"),$', html, re.M)
        if len(valeurs) != len(LANGUES):
            sys.exit(f"{cle} : {len(valeurs)} valeurs au lieu de {len(LANGUES)}")
        for l, v in zip(LANGUES, valeurs):
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


def main():
    cle = (RACINE / "elevenlabs.secret").read_text(encoding="utf-8").strip()
    textes = textes_de_l_app()
    manifeste_f = SORTIE / "textes.json"
    manifeste = json.loads(manifeste_f.read_text(encoding="utf-8")) if manifeste_f.exists() else {}
    caracteres = 0
    for langue in LANGUES:
        (SORTIE / langue).mkdir(parents=True, exist_ok=True)
        for clip, cles in CLIPS.items():
            texte = composer([textes[langue][c] for c in cles])
            empreinte = hashlib.sha1(texte.encode("utf-8")).hexdigest()
            cible = SORTIE / langue / f"{clip}.mp3"
            if cible.exists() and manifeste.get(langue, {}).get(clip) == empreinte:
                continue
            normaliser(generer(texte, langue, cle), cible)
            manifeste.setdefault(langue, {})[clip] = empreinte
            caracteres += len(texte)
            print(langue, clip, "fait")
            manifeste_f.write_text(json.dumps(manifeste, indent=1), encoding="utf-8")
    print(caracteres, "caracteres generes")


if __name__ == "__main__":
    main()
