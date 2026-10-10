# -*- coding: utf-8 -*-
"""Fabrique les fichiers audio ESPAGNOLS, une voix par variante.

    python audio/generer_es.py --variante es    --niveaux A1,A2 --a-blanc
    python audio/generer_es.py --variante latam --niveaux A1,A2 --plafond 110000
    python audio/generer_es.py --variante es    --normaliser

LES DEUX VOIX (choisies par Jacques le 10 oct. 2026, accent mesure par
audio/accent_es.py) :
    es    Lolita  3EsCRTMlRTbsPyDyDm45  -> audio/mp3/es-es/
    latam Monica  yR4AeVlfzs6IiKxIH9gQ  -> audio/mp3/es-419/
Un dossier par voix : les deux disent presque les memes textes, donc portent
presque les memes identifiants (sha1 du texte). Dans le meme dossier, l'une
ecraserait l'autre. audio/mp3/ est le dossier depose sur Firebase Hosting :
les fichiers y sont servis a https://deutschai-b6fbb.web.app/es-es/<id>.mp3.

CE QUI EST REPRIS DE L'ALLEMAND, tel quel (voir generer.py, refaire_mots.py) :
  - les reglages (stabilite 0,75, graine fixe, mp3 64 kbit/s) ;
  - LES MOTS SEULS DANS UNE PORTEUSE. Le modele devine la langue d'apres le
    texte ; sur un mot isole il se trompe (« neu » lu a la francaise, 3 sept.
    2026). Remede : « Palabra: <mot>. » a vitesse 0,80, puis on garde ce qui
    suit la plus grande pause (recouper.py). Seulement les textes SANS espace :
    « la casa » ou une phrase portent deja leur contexte.
  - la normalisation de sonie (normaliser.py), apres coup, original archive.

REPRENABLE : rien n'est tenu en memoire. Un fichier present est un fichier fait ;
relancer fait le reste. Les refus du decoupage sont notes dans
audio/es_refus_<dossier>.json : ces mots-la restent a la voix du telephone.
"""
import argparse, io, json, os, shutil, sys, time, urllib.error, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                      # noqa : cle, format, reglages, modeles
import manifest_es                  # noqa : l'inventaire espagnol
from recouper import recouper, Refus  # noqa

VOIX = {
    "es":    ("3EsCRTMlRTbsPyDyDm45", "es-es"),    # Lolita
    "latam": ("yR4AeVlfzs6IiKxIH9gQ", "es-419"),   # Monica
}
PORTEUSE = "Palabra: %s."
VITESSE_PORTEUSE = 0.80


def appeler(voix, texte, reglages, modele, cle):
    url = "https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=%s" % (voix, generer.FORMAT)
    corps = json.dumps({"text": texte, "model_id": modele, "voice_settings": reglages,
                        "seed": generer.SEED}).encode("utf-8")
    for essai in range(5):
        req = urllib.request.Request(url, data=corps, method="POST", headers={
            "xi-api-key": cle, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:200]
            if e.code in (429, 500, 502, 503, 504) and essai < 4:
                time.sleep(2 ** essai)
                continue
            if e.code == 403 and "violate" in detail:
                raise generer.TexteBloque(detail)
            raise RuntimeError("HTTP %d : %s" % (e.code, detail))
    raise RuntimeError("echec apres 5 essais")


def normaliser(dossier, travailleurs=7):
    """La sonie de chaque fichier, original archive dans audio/mp3_original/.

    EN PARALLELE (10 oct. 2026) : quatre passes ffmpeg par fichier, un a la
    fois, faisaient 26 fichiers par minute -- trois heures et demie par voix.
    ffmpeg tourne hors de Python : des fils suffisent, un par coeur.

    REPRENABLE MEME APRES UNE INTERRUPTION EN PLEIN FICHIER. Un fichier est a
    faire si son archive manque, OU si l'archive est encore IDENTIQUE au
    fichier : la copie a eu lieu, pas la normalisation. Le critere « archive
    presente = fait » tout seul aurait laisse ces fichiers-la a jamais crus.
    """
    import filecmp
    from concurrent.futures import ThreadPoolExecutor
    import normaliser as N
    N.FF = N.ffmpeg()
    mp3 = os.path.join(RACINE, "audio", "mp3", dossier)
    archive = os.path.join(N.SOURCE, dossier)
    os.makedirs(archive, exist_ok=True)
    for f in os.listdir(mp3):                      # restes d'une interruption
        if f.endswith((".norm.mp3", ".t1.mp3", ".part")):
            os.remove(os.path.join(mp3, f))

    def a_faire(f):
        src = os.path.join(archive, f)
        return not os.path.exists(src) or filecmp.cmp(os.path.join(mp3, f), src, shallow=False)

    liste = [f for f in sorted(os.listdir(mp3)) if f.endswith(".mp3") and a_faire(f)]
    print("a normaliser : %d" % len(liste), flush=True)

    def remplacer(tmp, cible):
        # ONEDRIVE VERROUILLE PARFOIS UN FICHIER pendant qu'il le synchronise
        # (WinError 5, le 10 oct. 2026, au 2 500e fichier de Lolita). On
        # reessaie ; s'il resiste, on le laisse : son archive est restee
        # identique, la passe suivante le reprendra.
        for essai in range(6):
            try:
                os.replace(tmp, cible)
                return True
            except PermissionError:
                time.sleep(1 + essai)
        return False

    def un(f):
        try:
            cible, src = os.path.join(mp3, f), os.path.join(archive, f)
            if not os.path.exists(src):
                shutil.copy2(cible, src)
            tmp = cible + ".norm.mp3"
            ok = N.normaliser(src, tmp, intermediaire=tmp + ".t1.mp3")
            if ok and remplacer(tmp, cible):
                return True
            if os.path.exists(tmp):
                os.remove(tmp)
            return False
        except OSError:
            return False

    faits = rates = 0
    with ThreadPoolExecutor(max_workers=travailleurs) as ex:
        for i, ok in enumerate(ex.map(un, liste), 1):
            faits += ok
            rates += not ok
            if i % 500 == 0:
                print("  %d/%d" % (i, len(liste)), flush=True)
    print("normalises : %d   rates : %d" % (faits, rates))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variante", choices=sorted(VOIX), required=True)
    p.add_argument("--niveaux", default="A1,A2")
    p.add_argument("--modele", default="v2", choices=sorted(generer.MODELES))
    p.add_argument("--plafond", type=int, default=110000, help="credits au plus pour cette execution")
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--normaliser", action="store_true")
    # LA REPRISE DES REFUS (10 oct. 2026). 18 mots chez Lolita, 45 chez Monica :
    # les deux enchainent « Palabra: » et le mot avec ~0,12 s de pause, trop peu
    # pour que recouper.py sache ou couper. Un POINT impose une vraie pause.
    p.add_argument("--reprendre-refus", action="store_true",
                   help="ne refaire que les refus, avec la porteuse de --porteuse")
    p.add_argument("--porteuse", default=PORTEUSE)
    a = p.parse_args()

    voix, dossier = VOIX[a.variante]
    if a.normaliser:
        normaliser(dossier)
        return
    sortie = os.path.join(RACINE, "audio", "mp3", dossier)
    bruts = os.path.join(RACINE, "audio", "bruts_es", dossier)
    niveaux = [n.strip() for n in a.niveaux.split(",")]
    modele, taux = generer.MODELES[a.modele]
    refus_chemin = os.path.join(RACINE, "audio", "es_refus_%s.json" % dossier)
    refus = json.load(io.open(refus_chemin, encoding="utf-8")) if os.path.exists(refus_chemin) else {}
    a_faire = [e for e in manifest_es.entrees(a.variante)
               if e["niveau"] in niveaux and not os.path.exists(os.path.join(sortie, e["id"] + ".mp3"))]
    if a.reprendre_refus:
        a_faire = [e for e in a_faire if e["id"] in refus]
        for e in a_faire:
            del refus[e["id"]]
        # Les prises brutes portent la porteuse dans leur dossier : une autre
        # porteuse ne doit pas reprendre l'ancienne prise.
        bruts = os.path.join(bruts, "".join(c if c.isalnum() else "_" for c in a.porteuse))
    texte_de = lambda e: (a.porteuse % e["texte"]) if " " not in e["texte"] else e["texte"]
    cout = int(sum(len(texte_de(e)) for e in a_faire) * taux)
    print("voix %s -> audio/mp3/%s/   modele %s" % (voix, dossier, modele))
    print("%d fichiers a produire (%d mots seuls en porteuse), environ %d credits"
          % (len(a_faire), sum(1 for e in a_faire if " " not in e["texte"]), cout))
    if a.a_blanc or not a_faire:
        return

    os.makedirs(sortie, exist_ok=True)
    os.makedirs(bruts, exist_ok=True)
    cle = generer.cle_api()
    depense = faits = 0
    debut = time.time()
    try:
        for e in a_faire:
            if e["id"] in refus:
                continue
            texte = texte_de(e)
            prix = int(len(texte) * taux)
            if depense + prix > a.plafond:
                print("plafond atteint (%d credits). Relancer reprend la suite." % depense)
                break
            cible = os.path.join(sortie, e["id"] + ".mp3")
            try:
                if texte is e["texte"]:
                    son = appeler(voix, texte, generer.REGLAGES, modele, cle)
                    open(cible + ".part", "wb").write(son)
                    os.replace(cible + ".part", cible)
                else:
                    brut = os.path.join(bruts, e["id"] + ".mp3")
                    if not os.path.exists(brut):
                        son = appeler(voix, texte, dict(generer.REGLAGES, speed=VITESSE_PORTEUSE), modele, cle)
                        open(brut, "wb").write(son)
                    try:
                        recouper(brut, cible + ".part", texte=e["texte"])
                        os.replace(cible + ".part", cible)
                    except Refus as err:
                        refus[e["id"]] = {"texte": e["texte"], "raison": str(err)}
                        if os.path.exists(cible + ".part"):
                            os.remove(cible + ".part")
            except generer.TexteBloque as err:
                refus[e["id"]] = {"texte": e["texte"], "raison": "refuse par ElevenLabs"}
            depense += prix
            faits += 1
            if faits % 100 == 0:
                ecoule = time.time() - debut
                print("  %5d/%d  %7d credits  reste ~%d min" % (faits, len(a_faire), depense,
                      int((len(a_faire) - faits) * ecoule / faits / 60)), flush=True)
                json.dump(refus, io.open(refus_chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    except KeyboardInterrupt:
        print("interrompu -- ce qui est fait est garde.")
    json.dump(refus, io.open(refus_chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("fait : %d appels, %d credits, %d refus au total" % (faits, depense, len(refus)))


if __name__ == "__main__":
    main()
