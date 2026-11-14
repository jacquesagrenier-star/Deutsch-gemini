# -*- coding: utf-8 -*-
"""Les voix des themes illustres : ce que chaque page peut dire, ce qui est deja enregistre, ce qui manque.

    python visuel/voix_themes.py            # l'inventaire, sons.json, et le chiffrage de ce qui manque (gratuit)

1. Il ouvre chaque page des 22 themes en espagnol d'Espagne, en espagnol d'Amerique latine, en allemand (et en
   anglais si le theme y est ouvert), et lui demande textesAVoix() : les fiches de la decouverte et les mots cles.
   Puis il ENUMERE ce que la page dit apres une reponse (7 nov. 2026 ; avant, 150 parties au hasard, qui laissaient
   passer des phrases) : chaque sorte de question tiree TIRAGES_VOIX fois (2000), une reponse touchee au hasard ; le
   releve dit, par sorte, combien de phrases neuves sortaient encore dans les 20 % derniers tirages (0 = epuisee).
   -> visuel/<theme>/voix.json (COMPLETE : un ancien texte qui a son fichier y reste), que lisent audio/manifest.py
   et audio/manifest_es.py (source <theme>), pour que les generateurs habituels les enregistrent.
2. Il COMPLETE visuel/prototype/themes/sons.json (jamais il ne le reduit) : pour chaque dossier de voix (de, es-es,
   es-419, en-us), les fichiers qui existent pour ces textes. C'est avec lui que themes/voix.js sait, AVANT de jouer,
   s'il faut le fichier ou la voix du telephone. A RELANCER APRES CHAQUE ENREGISTREMENT ; a pousser APRES le depot.
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
# Les 22 themes (7 nov. 2026 ; avant, une liste partielle -- et main() REECRIVAIT sons.json avec elle seule : les
# fichiers des themes absents de la liste en sortaient, et leurs phrases passaient a la voix du telephone).
THEMES = ["familia", "descripcion", "emociones", "contrarios", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "transportes",
          "loisirs", "animales", "meteo", "logement", "demarches", "courses", "vacances", "travail", "ecole", "ciudad", "fetes"]
# les themes ouverts a l'anglais (`en: true` dans THEMES_ILLUSTRES d'index.html) : les autres ne sont jamais lus en anglais
ANGLAIS = ["familia", "descripcion", "contrarios", "emociones", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "loisirs",
           "animales", "meteo", "logement", "demarches"]
SANS_EN = [t for t in THEMES if t not in ANGLAIS]
THEMES_EN = []                                   # (ancien : l'anglais seul pour quelques themes ; tout est enumere desormais)
# L'ENUMERATION (7 nov. 2026, la session des emotions : les 150 parties tirees au hasard laissaient passer des phrases
# de contraste et des pieges, qui partaient donc au telephone). Chaque SORTE de question (EX) est tiree TIRAGES fois,
# une reponse touchee au hasard (juste ou fausse : les deux font dire quelque chose), et tout ce que Voix.dire recoit
# est releve. `tard` : les phrases neuves des 20 % derniers tirages d'une sorte (0 = la sorte est epuisee).
# PAR MOT (7 nov. 2026, la session de la coherence des personnages : les phrases du medecin de cuerpo, « Diego
# arbeitet in dieser Praxis. Er ist Arzt. », n'etaient jamais relevees). L'app ne pose JAMAIS une question sans mot :
# montrer() appelle EX[sorte](mot) pour chaque mot de la partie (Tirage.plan), dans les 22 pages. Appeler EX[sorte]()
# a vide prenait les branches au hasard -- et ratait celles qui dependent du mot (w.doc, w.c...), tout en comptant
# des phrases que l'app ne dit pas. On fait donc comme montrer() : chaque mot de motsDuTheme(), chaque sorte qui
# l'accepte (EX rend faux sinon), TIRAGES / nombre de mots fois (au moins 20).
# LES QUESTIONS (13 nov. 2026, Jacques : « ¿Quién está enojado? » dit par le telephone). La phrase de l'enonce, dite
# a l'entree de chaque carte, passe par le dire() interne de themes/voix.js, pas par Voix.dire : elle n'etait jamais
# relevee, donc jamais enregistree (~11 000 textes par voix au 13 nov.). Voix.enonce() rend ce que la carte posee
# dit a son entree, a la regle de voix.js ; on le releve juste apres EX[sorte](mot), avant la reponse.
TIRAGES = int(os.environ.get("TIRAGES_VOIX", "2000"))
ENUMERER = """async (n) => {
  const dits = new Set(), parDire = new Set(), enonces = new Set(), orig = Voix.dire;
  Voix.dire = t => { if (t) { dits.add(t); parDire.add(t); } };
  const liste = Object.keys(EX).filter(x => typeof SORTES === 'undefined' || SORTES.includes(x));
  const mots = typeof motsDuTheme === 'function' ? motsDuTheme() : [];
  const hasard = a => a[Math.floor(Math.random() * a.length)], sortes = {};
  const k = Math.max(20, Math.ceil(n / Math.max(1, mots.length)));
  const vider = () => { for (const v of ['motQ', 'vuQ', 'sensQ']) { try { eval(v + ' = null'); } catch (e) {} } };
  for (const t of liste) {
    const avant = dits.size; let tard = 0, poses = 0, erreurs = 0;
    try { sorteCourante = t; } catch (e) {}
    for (const w of mots) {
      for (let i = 0; i < k; i++) {
        const s0 = dits.size;
        try {
          repondu = false; vider();
          if (!EX[t](w)) break;
          poses++;
          if (Voix.enonce) { const q = Voix.enonce(); if (q) { dits.add(q); enonces.add(q); } }
          const z = document.getElementById('zone');
          const c = Array.from(z.querySelectorAll('#choix button'));
          if (c.length) hasard(c).click();
          else if (typeof testerOrdre === 'function' && z.querySelector('.ordre')) testerOrdre();
          else { const a = Array.from(z.querySelectorAll('.arbre g.p:not(.ego), .rangee button, .corps .zone, .plan .cible'));
                 if (a.length) hasard(a).dispatchEvent(new MouseEvent('click', {bubbles: true})); }
        } catch (e) { erreurs++; break; }
        if (i >= k * 0.8) tard += dits.size - s0;
      }
    }
    sortes[t] = {phrases: dits.size - avant, tard, poses, erreurs};
  }
  Voix.dire = orig;
  return {dits: [...dits], enonces: [...enonces].filter(q => !parDire.has(q)), sortes, mots: mots.length};
}"""
CAS = {"es": ("es", "es"), "latam": ("es", "latam"), "de": ("de", ""), "en": ("en", "us")}       # cle de voix.json -> (apprendre, variante)
DOSSIER = {"es": "es-es", "latam": "es-419", "de": "", "en": "en-us"}
# l'anglais (3 nov. 2026) : Sarah, americaine, A1-A2 ; le britannique n'a pas de voix enregistree. Rien ne s'enregistre
# sans l'accord de Jacques (une ecoute a l'aveugle Sarah / Google / Azure d'abord) : ce qui manque est seulement liste.
# AUDIO_RACINE : le dossier ou vit audio/mp3 (le dossier principal ; un worktree ne l'a pas).
AUDIO = os.environ.get("AUDIO_RACINE", RACINE)
# VOIX_CLES=en : ne relire que ces langues (les autres gardent ce qu'elles ont dans voix.json)
CLES = [c for c in os.environ.get("VOIX_CLES", "").split(",") if c]
# VOIX_THEMES=emociones,cuerpo : ne relire que ces themes (6 nov. 2026, la coherence des personnages). Leur voix.json
# est refait, mais PAS themes/sons.json, qui se calcule sur tous les themes : un texte neuf n'y est pas de toute facon
# (il n'a pas de fichier), la page prend la voix du telephone.
SEULS = [c for c in os.environ.get("VOIX_THEMES", "").split(",") if c]


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
    out, enon = {}, {}
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for th in THEMES + THEMES_EN:
            if SEULS and th not in SEULS:
                continue
            out[th] = {}
            for cle, (app, var) in CAS.items():
                if CLES and cle not in CLES:
                    continue
                if cle == "en" and th in SANS_EN:
                    continue
                if th in THEMES_EN and cle != "en":
                    continue
                page = nav.new_page()
                page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&variante=%s&lang=fr" % (PORT, th, app, var))
                page.wait_for_function("() => typeof textesAVoix === 'function' && typeof EX !== 'undefined' && (typeof IDS === 'undefined' || IDS.length > 0) && (typeof D === 'undefined' || D)")
                page.wait_for_timeout(300)
                textes = set(t for t in page.evaluate("() => textesAVoix()") if t)
                if th in THEMES:
                    e = page.evaluate(ENUMERER, TIRAGES)
                    ouvertes = {s: v["tard"] for s, v in e["sortes"].items() if v["tard"]}
                    print("  %-12s %-6s %4d phrases dites apres une reponse ; sortes non epuisees : %s" % (th, cle, len(e["dits"]), ouvertes or "aucune"))
                    textes |= set(e["dits"])
                    enon.setdefault(th, {})[cle] = sorted(e["enonces"])
                out[th][cle] = sorted(textes)
                page.close()
        try:
            nav.close()
        except Exception:
            pass                                  # un navigateur qui ferme mal n'enleve rien aux textes lus
    srv.shutdown()
    return out, enon


def main():
    textes, enonces = textes_des_pages()
    for th, d in textes.items():
        chemin = os.path.join(ICI, th, "voix.json")
        # en COMPLETANT le voix.json du theme : une langue qu'on n'a pas relue y reste ; et dans une langue relue, un
        # ancien texte qui A SON FICHIER reste aussi (une phrase deja payee ne sort jamais de la liste ; un texte perime
        # sans fichier, lui, sort, pour que le chiffrage ne compte que ce que la page dit)
        ancien = json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else {}
        for cle, l in list(d.items()):
            dos = os.path.join(AUDIO, "audio", "mp3", DOSSIER[cle])
            garde = [t for t in ancien.get(cle, []) if os.path.exists(os.path.join(dos, ident(t) + ".mp3"))]
            d[cle] = sorted(set(l) | set(garde))
        ancien.update(d)
        # « enonces » (13 nov. 2026) : les questions que la page pose sans jamais les dire ailleurs -- le vrai ou faux
        # affirme aussi le FAUX (« Pablo ist Koch. » pour un boulanger) ; tests/themes_illustres.py ne les juge donc pas
        # sur les fiches. Les manifestes ne lisent que les cles de langue : ces phrases s'enregistrent comme le reste.
        if th in enonces:
            ancien.setdefault("enonces", {}).update(enonces[th])
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(ancien, ensure_ascii=False, indent=1) + "\n")
        print("  -> %s" % os.path.relpath(chemin, RACINE))
    if SEULS:
        print("\n  VOIX_THEMES : themes/sons.json n'est pas refait (il se calcule sur tous les themes)")
        return
    # les contraires (3 nov. 2026) : la decouverte et les mots cles, tels que contrarios.json les donne
    # (audio/manifest.py, contrarios_textes ; l'Amerique latine dit les memes textes que l'Espagne)
    # -- en COMPLETANT l'anglais lu dans la page (THEMES_EN), jamais en le remplacant
    import manifest
    # (7 nov. : en UNION avec ce que la page a dit, comme la decouverte des emotions)
    for c in ("es", "latam", "de"):
        textes.setdefault("contrarios", {})[c] = sorted(set(textes["contrarios"].get(c, [])) | set(manifest.contrarios_textes(c)))
        if "emociones" in textes:
            textes["emociones"][c] = sorted(set(textes["emociones"].get(c, [])) | set(manifest.emociones_textes(c)))
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
                else:
                    dit = lectures.lecture(langue, t)
                    credits += len(((("Word: %s." if langue == "en" else "Palabra: %s.") % dit)) if (" " not in t and langue in ("es", "en")) else dit)
                    manque.append(t)
            total += credits
            print("  %-12s %-6s %3d textes, %3d sans fichier, ~%d credits" % (th, cle, len(d.get(cle, [])), len(manque), credits))
            if manque: print("      " + (" | ".join(manque) if len(manque) <= 30 else " | ".join(manque[:30]) + " | ... %d de plus" % (len(manque) - 30)))
        sons[dos or "de"] = sorted(ids)
    # sons.json : TOUJOURS COMPLETE, JAMAIS REDUIT (7 nov. 2026). Il sert aussi les decouvertes des emotions, les
    # contraires et tout theme qu'un passage ne relit pas ; le reecrire avec ce seul passage en faisait sortir des
    # fichiers en ligne, dits ensuite par le telephone. ⚠️ Ne le pousser qu'APRES le depot des fichiers neufs.
    chemin = os.path.join(ICI, "prototype", "themes", "sons.json")
    avant = json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else {}
    for dos, ids in avant.items():
        sons[dos] = sorted(set(sons.get(dos, [])) | set(ids))
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(sons, indent=1, sort_keys=True) + "\n")
    print("\n  -> %s ; a enregistrer en tout : ~%d credits" % (os.path.relpath(chemin, RACINE), total))


if __name__ == "__main__":
    main()
