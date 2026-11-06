"""Le controle des sons (audio/controler_sons.py : SATURE, CLIC, TRAINE…) sur les pistes de l'ecoute du telc, qui vivent
dans audio/mp3/dtz/telc/ du DEPOT PRINCIPAL (controler_sons.py ne regarde que le depot ou il est lance).

    python visuel/prototype/telc/outils/controler_ecouter.py
"""
import importlib.util
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
TELC = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(TELC)))
PRINCIPAL = os.path.normpath(os.path.join(DEPOT, "..", "..", ".."))
if not os.path.exists(os.path.join(PRINCIPAL, "firebase.json")):
    PRINCIPAL = DEPOT
spec = importlib.util.spec_from_file_location("controler_sons", os.path.join(DEPOT, "audio", "controler_sons.py"))
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

base = os.path.join(PRINCIPAL, "audio", "mp3", "dtz", "telc")
manifeste = json.load(open(os.path.join(TELC, "donnees", "voix-ecouter.json"), encoding="utf-8"))
graves = 0
for cle, f in sorted(manifeste.items()):
    chemin = os.path.join(PRINCIPAL, "audio", "mp3", "dtz", f)
    if not os.path.exists(chemin):
        print("  %-18s ABSENT  %s" % (cle, f)); graves += 1; continue
    m = C.mesurer(chemin)
    d = ["ILLISIBLE"] if m is None else C.defauts(m, "")
    g = set(d) & {"SATURE", "CLIC", "TRAINE", "ILLISIBLE"}
    graves += bool(g)
    print("  %-18s %-24s crete %5.1f  rms %5.1f  duree %5.1f s" % (cle, ",".join(d) or "ok", (m or {}).get("crete", 0), (m or {}).get("rms", 0), (m or {}).get("duree", 0)))
print("%d piste(s), %d avec un defaut grave." % (len(manifeste), graves))
sys.exit(1 if graves else 0)
