"""La relecture germanophone de l'ecoute du telc (Hoeren et Hoeren und Schreiben), ramassee par outils/relecture.py
dans retours/A-RELIRE-TELC.md. Session « telc : Ecouter », 6 nov. 2026.

section(lignes) ajoute les textes allemands au format du fichier : le texte, puis une ligne « → ».
"""
import json
import os

TELC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _charger(nom):
    return json.load(open(os.path.join(TELC, "donnees", nom), encoding="utf-8"))


def _repliques(lignes, audio, rollen):
    for l in audio:
        qui = (rollen or {}).get(l["wer"]) or l["wer"]
        lignes.append("> **%s** : %s" % (qui, l["text"]))
        lignes.append(">")
    if audio:
        lignes.pop()
    lignes.append("")
    lignes.append("→ ")
    lignes.append("")


def section(lignes):
    h = _charger("hoeren.json")
    hs = _charger("hoeren-schreiben.json")
    lignes.append("## Écouter (Hören) et Écouter et noter (Hören und Schreiben)")
    lignes.append("")
    lignes.append("Ces textes sont DITS (des conversations, des annonces, des messages de répondeur) : ils doivent sonner "
                  "comme de l'allemand parlé de tous les jours, au niveau A2-B1. Questions : la langue est-elle naturelle "
                  "à l'oral ? Chaque question a-t-elle **une seule** bonne réponse d'après ce qu'on entend ? Les phrases "
                  "« richtig / falsch » et les solutions sont-elles claires ? Les nombres sont écrits en chiffres ; la "
                  "voix les dira en lettres.")
    lignes.append("")
    lignes.append("### Les consignes")
    lignes.append("")
    for t in ("T1", "T2", "T3", "T4", "ende"):
        lignes.append("- %s : %s" % (t, h["consignes"][t]["text"]))
        lignes.append("  → ")
    lignes.append("- Hören und Schreiben : %s" % hs["consigne"]["text"])
    lignes.append("  → ")
    lignes.append("")
    for s in h["series"]:
        t1, t2, t3, t4 = s["T1"], s["T2"], s["T3"], s["T4"]
        lignes.append("### Hören, série %d · Teil 1 (entendu deux fois) · %s" % (s["id"], t1["situation_fr"]))
        lignes.append("")
        _repliques(lignes, t1["audio"], t1["rollen"])
        sol = {x["b"]: x["text"] for x in t1["loesungen"]}
        lignes.append("%s" % t1["frage"])
        for x in t1["loesungen"]:
            lignes.append("- %s) %s" % (x["b"], x["text"]))
        for it in t1["items"]:
            lignes.append("- **%d. %s → %s) %s**" % (it["nr"], it["frage"], it["bon"], sol[it["bon"]]))
        lignes.append("  → ")
        lignes.append("")
        lignes.append("### Hören, série %d · Teil 2 (entendu une fois) · %s" % (s["id"], t2["situation_fr"]))
        lignes.append("")
        _repliques(lignes, t2["audio"], t2["rollen"])
        for it in t2["items"]:
            lignes.append("- %d. %s **(%s)**" % (it["nr"], it["aussage"], "richtig" if it["bon"] else "falsch"))
            lignes.append("  → ")
        lignes.append("")
        lignes.append("### Hören, série %d · Teil 3 (chaque annonce deux fois)" % s["id"])
        lignes.append("")
        for a in t3:
            lignes.append("%d. %s" % (a["nr"], a["typ"]))
            lignes.append("")
            _repliques(lignes, a["audio"], a["rollen"])
            lignes.append("- %s **(%s)**" % (a["aussage"], "richtig" if a["bon"] else "falsch"))
            lignes.append("  → ")
            lignes.append("")
        lignes.append("### Hören, série %d · Teil 4 (chaque avis une fois) · %s" % (s["id"], t4["thema"]))
        lignes.append("")
        _repliques(lignes, t4["intro"], t4["rollen"])
        sol = {x["b"]: x["text"] for x in t4["saetze"]}
        for x in t4["saetze"]:
            lignes.append("- %s) %s" % (x["b"], x["text"]))
        lignes.append("")
        for p in t4["personen"]:
            _repliques(lignes, p["audio"], {p["wer"]: p["name"]})
            lignes.append("- **%d → %s) %s**" % (p["nr"], p["bon"], sol[p["bon"]]))
            lignes.append("  → ")
            lignes.append("")
    for s in hs["series"]:
        lignes.append("### Hören und Schreiben, série %d (chaque message deux fois)" % s["id"])
        lignes.append("")
        for m in s["nachrichten"]:
            _repliques(lignes, m["audio"], m["rollen"])
            note = " / ".join(z.replace("{}", "**%s**" % m["loesung"]) for z in m["notiz"]["zeilen"])
            lignes.append("- %d. Notiz « %s » : %s" % (m["nr"], m["notiz"]["titel"], note))
            lignes.append("  → ")
            lignes.append("")
