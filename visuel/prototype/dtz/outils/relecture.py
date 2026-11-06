"""Fabrique visuel/prototype/dtz/RELECTURE-DE.md : les textes allemands du DTZ (Hoeren, Lesen, puis Sprechen et
Schreiben par outils/relecture_oral.py) pour une relectrice ou un relecteur
germanophone qui ne connait pas l'app.

    python visuel/prototype/dtz/outils/relecture.py

Demande du chef d'orchestre (3 nov. 2026) : « que la personne puisse relire sans connaitre l'app : le texte, le
niveau, la question posee, et une case ok ou correction ». Chaque texte porte un identifiant (H-S1-T3-10 = Hoeren,
serie 1, Teil 3, question 10) : la correction revient avec cet identifiant et se reporte dans donnees/*.json,
JAMAIS dans ce fichier, qui est refait a chaque fois.

Les explications en francais n'y sont pas : elles ne sont pas a relire par un germanophone. Le niveau vise est
A2-B1 (DTZ) pour tout le fichier.
"""
import json
import os
import sys

DTZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(DTZ)))
DONNEES = os.path.join(DTZ, "donnees")
SORTIE = os.path.join(DTZ, "RELECTURE-DE.md")
ABC = "abc"
CASE = "\n> ☐ OK   ☐ Korrektur: …………………………………………………………\n"


def charger(nom):
    with open(os.path.join(DONNEES, nom), encoding="utf-8") as f:
        return json.load(f)


def sprecher(voix, wer, rollen=None):
    # le role (Frau Brandt, Beamter), sinon Mark, Sprecher ou Sprecherin : comme la transcription de l'app
    if rollen and wer in rollen:
        return rollen[wer]
    if wer == "mark":
        return "Mark"
    return "Sprecher" if (voix.get(wer) or {}).get("sexe") == "m" else "Sprecherin"


def fragen(items, lettres=None):
    out = []
    for it in items:
        nr = "Beispiel" if it.get("beispiel") else "Aufgabe %s" % it["nr"]
        if it.get("rf"):
            out.append("- **%s** – *Richtig oder falsch?* %s → **%s**" % (nr, it["frage"], it["optionen"][it["bon"]]))
        else:
            out.append("- **%s** – %s" % (nr, it["frage"]))
            for i, o in enumerate(it["optionen"]):
                out.append("  - %s) %s%s" % (ABC[i], o, "  ✅" if i == it["bon"] else ""))
    return "\n".join(out)


def main():
    H = charger("hoeren.json")
    L = charger("lesen.json")
    v = H["voix"]
    o = []
    o.append("# DTZ-Vorbereitung „Mit Mark und Anna“ – Texte zum Korrekturlesen")
    o.append("")
    o.append("*Datei erstellt mit `python visuel/prototype/dtz/outils/relecture.py` – bitte nicht von Hand ändern.*")
    o.append("")
    o.append("## Worum es geht")
    o.append("")
    o.append("Wortando ist eine App zum Deutschlernen. Wir bereiten Lernende auf den **Deutsch-Test für Zuwanderer (DTZ)** vor, "
             "Niveau **A2–B1**. Alle Texte sind von uns geschrieben (keine Originalprüfung) und folgen nur dem **Format** des DTZ. "
             "Sie spielen im Alltag von Mark, einem jungen Kanadier aus Montreal, der in Berlin wohnt.")
    o.append("")
    o.append("**Bitte prüfen Sie:**")
    o.append("1. Ist das Deutsch **korrekt und natürlich**? Würde man das in Deutschland so sagen oder schreiben (Ansage, Brief, Anzeige …)?")
    o.append("2. Passt die **markierte Lösung (✅)** eindeutig zum Text, und sind die anderen Antworten eindeutig falsch?")
    o.append("3. Ist das Niveau ungefähr **A2–B1** (nicht viel schwerer)?")
    o.append("")
    o.append("Kreuzen Sie unter jedem Text **OK** an oder schreiben Sie Ihre **Korrektur** dazu. Kleine Hinweise genügen "
             "(„besser: …“). Die Kennung (z. B. **H-S1-T3-10**) hilft uns, die Stelle wiederzufinden.")
    o.append("")
    o.append("Hinweis: Die **Hörtexte** werden später von Sprecherinnen und Sprechern aufgenommen; hier lesen Sie sie als Text. "
             "Zahlen stehen in Ziffern, werden aber ausgeschrieben gesprochen.")
    o.append("")

    for s in H["series"]:
        o.append("---")
        o.append("")
        o.append("# Hören – Serie %s" % s["id"][1:])
        o.append("")
        titres = {"T1": "Teil 1 – Ansagen am Telefon und über Lautsprecher", "T2": "Teil 2 – Meldungen im Radio",
                  "T3": "Teil 3 – Gespräche", "T4": "Teil 4 – Meinungen in einer Radiosendung"}
        for teil in ("T1", "T2", "T3"):
            o.append("## " + titres[teil])
            o.append("")
            o.append("*Anweisung (gesprochen):* „%s“" % H["consignes"][teil]["de"])
            o.append(CASE)
            items = s[teil]
            vus = set()
            for it in items:
                if it.get("gleiches_audio") or id(it) in vus:
                    continue
                groupe = [it] + [x for x in items if x.get("gleiches_audio") == it["nr"]]
                ident = "H-%s-%s-%s" % (s["id"], teil, "Bsp" if it.get("beispiel") else "-".join(str(g["nr"]) for g in groupe))
                o.append("### %s · %s" % (ident, it.get("typ", "")))
                o.append("")
                for r in it["audio"]:
                    o.append("> **%s:** %s  " % (sprecher(v, r["wer"], it.get("rollen")), r["text"]))
                o.append("")
                o.append(fragen(groupe))
                o.append(CASE)
        t4 = s["T4"]
        o.append("## " + titres["T4"])
        o.append("")
        o.append("*Anweisung (gesprochen):* „%s“" % H["consignes"]["T4"]["de"])
        o.append("")
        o.append("**Thema:** %s" % t4["thema"])
        o.append("")
        o.append("**Sätze zur Auswahl:**")
        for x in t4["saetze"]:
            o.append("- %s) %s" % (x["b"], x["de"]))
        o.append(CASE)
        o.append("### H-%s-T4-Einleitung" % s["id"])
        o.append("")
        for r in t4["intro"]:
            o.append("> **%s:** %s" % (sprecher(v, r["wer"]), r["text"]))
        o.append(CASE)
        for a in t4["aussagen"]:
            ident = "H-%s-T4-%s" % (s["id"], "Bsp" if a.get("beispiel") else a["nr"])
            o.append("### %s · Lösung: Satz %s" % (ident, a["bon"]))
            o.append("")
            for r in a["audio"]:
                o.append("> **%s:** %s" % (sprecher(v, r["wer"]), r["text"]))
            o.append(CASE)

    for s in L["series"]:
        o.append("---")
        o.append("")
        o.append("# Lesen – Serie %s" % s["id"][1:])
        o.append("")
        t1 = s["T1"]
        o.append("## Teil 1 – Wegweiser, Verzeichnisse")
        o.append("")
        o.append("*Anweisung:* „%s“  \n*Situation:* „%s“" % (t1["aufgabe"], t1["situation"]))
        o.append("")
        o.append("### L-%s-T1-Text · %s" % (s["id"], t1["dokument"]["titel"]))
        o.append("")
        for z in t1["dokument"]["zeilen"]:
            o.append("> **%s:** %s  " % (z["etage"], z["inhalt"]))
        o.append(CASE)
        o.append("### L-%s-T1-Aufgaben" % s["id"])
        o.append("")
        o.append(fragen(t1["items"]))
        o.append(CASE)

        t2 = s["T2"]
        o.append("## Teil 2 – Kleinanzeigen")
        o.append("")
        o.append("*Anweisung:* „%s“" % t2["aufgabe"])
        o.append("")
        for a in t2["anzeigen"]:
            o.append("### L-%s-T2-Anzeige-%s · %s" % (s["id"], a["b"], a["titel"]))
            o.append("")
            o.append("> " + a["text"])
            o.append(CASE)
        o.append("### L-%s-T2-Situationen" % s["id"])
        o.append("")
        for it in t2["items"]:
            nr = "Beispiel" if it.get("beispiel") else "Aufgabe %s" % it["nr"]
            o.append("- **%s** – %s → **%s**" % (nr, it["situation"], "keine Anzeige (x)" if it["bon"] == "x" else "Anzeige " + it["bon"]))
        o.append(CASE)

        o.append("## Teil 3 – Presse, Mitteilungen")
        o.append("")
        o.append("*Anweisung:* „%s“" % s["T3"]["aufgabe"])
        o.append("")
        for tx in s["T3"]["texte"]:
            o.append("### L-%s-T3-%s · %s" % (s["id"], "-".join(str(i["nr"]) for i in tx["items"]), tx["titel"]))
            o.append("")
            o.append("> *%s*  " % tx["kopf"])
            o.append("> **%s**" % tx["titel"])
            for p in tx["absaetze"]:
                o.append(">")
                o.append("> " + p.replace("\n", "  \n> "))
            o.append("")
            o.append(fragen(tx["items"]))
            o.append(CASE)

        t4 = s["T4"]
        d = t4["dokument"]
        o.append("## Teil 4 – Informationsbroschüre")
        o.append("")
        o.append("*Anweisung:* „%s“" % t4["aufgabe"])
        o.append("")
        o.append("### L-%s-T4 · %s" % (s["id"], d["titel"]))
        o.append("")
        o.append("> *%s*  " % d["kopf"])
        o.append("> **%s**" % d["titel"])
        for a in d["abschnitte"]:
            o.append(">")
            o.append("> **%s.** %s" % (a["titel"], a["text"]))
        o.append("")
        o.append(fragen(t4["items"]))
        o.append(CASE)

        t5 = s["T5"]
        b = t5["brief"]
        o.append("## Teil 5 – Formeller Brief mit Lücken")
        o.append("")
        o.append("*Anweisung:* „%s“" % t5["aufgabe"])
        o.append("")
        o.append("### L-%s-T5 · Brief" % s["id"])
        o.append("")
        for bloc in (b["absender"], b["empfaenger"], b["datum"]):
            o.append("> " + bloc.replace("\n", "  \n> "))
            o.append(">")
        lues = {lu["nr"]: lu for lu in t5["luecken"]}
        def trou(t):
            for n, lu in lues.items():
                t = t.replace("{%d}" % n, "**(%d) ___**" % n)
            return t
        o.append("> **Betreff: %s**" % trou(b["betreff"]))
        for p in b["text"]:
            o.append(">")
            o.append("> " + trou(p))
        o.append("")
        for n, lu in lues.items():
            o.append("- **(%s)%s** – %s" % (n, " Beispiel" if lu.get("beispiel") else "",
                     " / ".join("%s) %s%s" % (ABC[i], x, " ✅" if i == lu["bon"] else "") for i, x in enumerate(lu["optionen"]))))
        o.append(CASE)

    # LES AUTRES EPREUVES (Sprechen, Schreiben) ecrivent leurs sections dans LE MEME fichier : un seul envoi au
    # germanophone. Leur module, outils/relecture_oral.py (session de l'oral et de l'ecrit), expose sections(o, CASE)
    # et ajoute ses lignes a la liste o. Absent : le fichier ne porte que Hoeren et Lesen.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import relecture_oral
    except ImportError:
        relecture_oral = None
    if relecture_oral:
        relecture_oral.sections(o, CASE)

    o.append("---")
    o.append("")
    o.append("Vielen Dank für Ihre Hilfe! Ihre Korrekturen gehen an Jacques zurück.")
    with open(SORTIE, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(o) + "\n")
    print("Ecrit : %s" % os.path.relpath(SORTIE, RACINE))


if __name__ == "__main__":
    main()
