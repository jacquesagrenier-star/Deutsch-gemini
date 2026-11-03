# -*- coding: utf-8 -*-
"""Les voix des themes illustres : ce que chaque page peut dire, ce qui est deja enregistre, ce qui manque.

    python visuel/voix_themes.py            # l'inventaire, sons.json, et le chiffrage de ce qui manque (gratuit)

1. Il ouvre chaque page (famille, Decrire une personne) en espagnol d'Espagne, en espagnol d'Amerique latine et en
   allemand, et lui demande textesAVoix() : les fiches de la decouverte et les mots cles qu'elle dit apres une
   reponse. -> visuel/<theme>/voix.json, que lisent audio/manifest.py et audio/manifest_es.py (source <theme>),
   pour que les generateurs habituels les enregistrent (generer.py, generer_es.py --sources familia,descripcion).
2. Il ecrit visuel/prototype/themes/sons.json : pour chaque dossier de voix (de, es-es, es-419), les fichiers qui
   existent pour ces textes (et pour ceux des emotions). C'est avec lui que themes/voix.js sait, AVANT de jouer,
   s'il faut le fichier ou la voix du telephone. A RELANCER APRES CHAQUE ENREGISTREMENT, avant le depot.
3. Il chiffre ce qui manque, en credits (multilingual v2 : un credit par caractere dit ; un mot seul passe dans
   sa porteuse, « Palabra: <mot>. »).
"""
import functools, hashlib, http.server, io, json, os, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "audio"))
import lectures                                   # noqa : les nombres en lettres
PORT = int(os.environ.get("THEMES_PORT", "8808"))
THEMES = ["familia", "descripcion", "manger"]
CAS = {"es": ("es", "es"), "latam": ("es", "latam"), "de": ("de", "")}       # cle de voix.json -> (apprendre, variante)
DOSSIER = {"es": "es-es", "latam": "es-419", "de": ""}


def ident(t):
    return hashlib.sha1(t.encode("utf-8")).hexdigest()[:16]


def textes_des_pages():
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Muet, directory=RACINE))
    srv.handle_error = lambda *a: None
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    out = {}
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for th in THEMES:
            out[th] = {}
            for cle, (app, var) in CAS.items():
                page = nav.new_page()
                page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&variante=%s&lang=fr" % (PORT, th, app, var))
                page.wait_for_function("() => typeof textesAVoix === 'function' && (typeof IDS === 'undefined' || IDS.length > 0) && (typeof D === 'undefined' || D)")
                page.wait_for_timeout(300)
                out[th][cle] = sorted(set(t for t in page.evaluate("() => textesAVoix()") if t))
                page.close()
        nav.close()
    srv.shutdown()
    return out


def emotions():
    import manifest
    return {"es": manifest.emociones_textes("es"), "latam": manifest.emociones_textes("latam"), "de": manifest.emociones_textes("de")}


def main():
    textes = textes_des_pages()
    for th, d in textes.items():
        chemin = os.path.join(ICI, th, "voix.json")
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print("  -> %s" % os.path.relpath(chemin, RACINE))
    try:
        textes["emociones"] = emotions()
    except Exception as e:
        print("  (emotions non lues : %s)" % e)
    sons = {}
    total = 0
    print("\n  CE QUI MANQUE (multilingual v2)")
    for cle, dos in DOSSIER.items():
        langue = "de" if cle == "de" else "es"
        dossier = os.path.join(RACINE, "audio", "mp3", dos)
        ids = set()
        for th, d in textes.items():
            manque, credits = [], 0
            for t in d.get(cle, []):
                i = ident(t)
                if os.path.exists(os.path.join(dossier, i + ".mp3")):
                    ids.add(i)
                elif th != "emociones":
                    dit = lectures.lecture(langue, t)
                    credits += len(("Palabra: %s." % dit) if (" " not in t and langue == "es") else dit)
                    manque.append(t)
            if th != "emociones":
                total += credits
                print("  %-12s %-6s %3d textes, %3d sans fichier, ~%d credits" % (th, cle, len(d.get(cle, [])), len(manque), credits))
                if manque: print("      " + " | ".join(manque))
        sons[dos or "de"] = sorted(ids)
    chemin = os.path.join(ICI, "prototype", "themes", "sons.json")
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(sons, indent=1) + "\n")
    print("\n  -> %s ; a enregistrer en tout : ~%d credits" % (os.path.relpath(chemin, RACINE), total))


if __name__ == "__main__":
    main()
