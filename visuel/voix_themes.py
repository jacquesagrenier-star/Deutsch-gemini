# -*- coding: utf-8 -*-
"""Les voix des themes illustres : ce que chaque page peut dire, ce qui est deja enregistre, ce qui manque.

    python visuel/voix_themes.py            # l'inventaire, sons.json, et le chiffrage de ce qui manque (gratuit)

1. Il ouvre chaque page (famille, Decrire une personne) en espagnol d'Espagne, en espagnol d'Amerique latine et en
   allemand, et lui demande textesAVoix() : les fiches de la decouverte et les mots cles. Puis il JOUE des parties
   (PARTIES) et releve ce que la page dit apres chaque reponse : depuis le 3 nov. 2026 (« Oui, partout »), la phrase
   affichee en entier, qui se fabrique depuis les donnees et ne peut pas s'enumerer autrement. Un echantillon, donc :
   le releve dit combien de phrases la derniere partie jouee a encore apportees (0 = l'echantillon couvre tout). -> visuel/<theme>/voix.json, que lisent audio/manifest.py et audio/manifest_es.py (source <theme>),
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
THEMES = ["familia", "descripcion", "ropa"]
THEMES_EN = ["contrarios"]      # ses voix es et de sont dans contrarios.json ; l'anglais passe par themes/voix.js
PARTIES = int(os.environ.get("PARTIES_VOIX", "150"))
# ce que la page dit apres chaque reponse, sur PARTIES parties : Voix.dire est ecoute, chaque question repondue
ECHANTILLON = """async (n) => { const dits = new Set(); let apport = 0; const orig = Voix.dire; Voix.dire = t => { if (t) dits.add(t); };
  for (let s = 0; s < n; s++){ const avant = dits.size; await demarrer();
    for (let r = 0; r < file.length; r++){ rang = r; try { montrer(); } catch (e) { continue; }
      const b = document.querySelector('#choix button, .rangee button, .arbre g.p:not(.ego)');
      if (b) b.dispatchEvent(new MouseEvent('click', {bubbles: true})); }
    apport = dits.size - avant; }
  Voix.dire = orig; return {dits: [...dits], apport}; }"""
CAS = {"es": ("es", "es"), "latam": ("es", "latam"), "de": ("de", ""), "en": ("en", "us")}       # cle de voix.json -> (apprendre, variante)
DOSSIER = {"es": "es-es", "latam": "es-419", "de": "", "en": "en-us"}
# l'anglais (3 nov. 2026) : Sarah, americaine, A1-A2 ; le britannique n'a pas de voix enregistree. Rien ne s'enregistre
# sans l'accord de Jacques (une ecoute a l'aveugle Sarah / Google / Azure d'abord) : ce qui manque est seulement liste.
# AUDIO_RACINE : le dossier ou vit audio/mp3 (le dossier principal ; un worktree ne l'a pas).
AUDIO = os.environ.get("AUDIO_RACINE", RACINE)


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
        for th in THEMES + THEMES_EN:
            out[th] = {}
            for cle, (app, var) in CAS.items():
                if th in THEMES_EN and cle != "en":
                    continue
                page = nav.new_page()
                page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&variante=%s&lang=fr" % (PORT, th, app, var))
                page.wait_for_function("() => typeof textesAVoix === 'function' && (typeof IDS === 'undefined' || IDS.length > 0) && (typeof D === 'undefined' || D)")
                page.wait_for_timeout(300)
                textes = set(t for t in page.evaluate("() => textesAVoix()") if t)
                if th in THEMES and cle != "en":
                    e = page.evaluate(ECHANTILLON, PARTIES)
                    print("  %-12s %-6s %4d phrases dites apres une reponse (la derniere partie en a ajoute %d)" % (th, cle, len(e["dits"]), e["apport"]))
                    textes |= set(e["dits"])
                out[th][cle] = sorted(textes)
                page.close()
        try:
            nav.close()
        except Exception:
            pass                                  # un navigateur qui ferme mal n'enleve rien aux textes lus
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
    # les contraires (3 nov. 2026) : la decouverte et les mots cles, tels que contrarios.json les donne
    # (audio/manifest.py, contrarios_textes ; l'Amerique latine dit les memes textes que l'Espagne)
    # -- en COMPLETANT l'anglais lu dans la page (THEMES_EN), jamais en le remplacant
    import manifest
    textes.setdefault("contrarios", {}).update({"es": manifest.contrarios_textes("es"), "latam": manifest.contrarios_textes("latam"), "de": manifest.contrarios_textes("de")})
    sons = {}
    total = 0
    print("\n  CE QUI MANQUE (multilingual v2)")
    for cle, dos in DOSSIER.items():
        langue = "de" if cle == "de" else "en" if cle == "en" else "es"
        dossier = os.path.join(AUDIO, "audio", "mp3", dos)
        ids = set()
        for th, d in textes.items():
            manque, credits = [], 0
            for t in d.get(cle, []):
                i = ident(t)
                if os.path.exists(os.path.join(dossier, i + ".mp3")):
                    ids.add(i)
                elif th != "emociones":
                    dit = lectures.lecture(langue, t)
                    credits += len(((("Word: %s." if langue == "en" else "Palabra: %s.") % dit)) if (" " not in t and langue in ("es", "en")) else dit)
                    manque.append(t)
            if th != "emociones":
                total += credits
                print("  %-12s %-6s %3d textes, %3d sans fichier, ~%d credits" % (th, cle, len(d.get(cle, [])), len(manque), credits))
                if manque: print("      " + (" | ".join(manque) if len(manque) <= 30 else " | ".join(manque[:30]) + " | ... %d de plus" % (len(manque) - 30)))
        sons[dos or "de"] = sorted(ids)
    chemin = os.path.join(ICI, "prototype", "themes", "sons.json")
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(sons, indent=1) + "\n")
    print("\n  -> %s ; a enregistrer en tout : ~%d credits" % (os.path.relpath(chemin, RACINE), total))


if __name__ == "__main__":
    main()
