# -*- coding: utf-8 -*-
"""L'ALLEMAND QUI FUIT DANS L'APP ESPAGNOLE : un compte espagnol neuf, de bout
en bout, et tout ce qu'il voit ou entend d'allemand.

Ne le 21 oct. 2026 (v908) : Marc-Antoine installe l'app en espagnol, compte
neuf, et recoit des ses premieres cartes « Tisch ». Les deux verificateurs et
le parcours de la fusion (fusion-espagnol/parcours.py) ne le voyaient pas :
le parcours ouvre chaque tuile une fois, il ne VIT pas les premiers jours d'un
compte -- la visite, Premiers pas, la seance du jour 1, 2, 3, l'A1 voyage, les
reperes, la scene du jour -- et ne cherche pas l'allemand dans ce qu'il releve.

    python tests/allemand_dans_espagnol.py                 # le parcours, puis les fuites
    python tests/allemand_dans_espagnol.py --jours 5       # cinq jours au lieu de trois
    python tests/allemand_dans_espagnol.py --releve r.json # garde tout le releve

Sortie : chaque fuite, avec l'ecran (le chemin dans le parcours), le mot
allemand, la ligne ou il apparait, et la source (texte affiche, voix, ou
fichier allemand demande au serveur). Code de sortie 1 s'il y en a.

COMMENT ON RECONNAIT L'ALLEMAND, sans dictionnaire externe :
  - un mot a « a / o » trema ou « ss » allemand (ä ö ß) : jamais espagnol ni
    francais ; le « u » trema seulement hors du corpus espagnol (pingüino) ;
  - un mot du CORPUS ALLEMAND (themes.json, verbe.json, adjectif.json,
    adverbe.json, funktionswort.json, et une liste de mots-outils) qui n'est
    ni dans le corpus espagnol (espanol/datos/, ses traductions francaises
    comprises) ni dans le texte francais de l'interface ;
  - un fichier de donnees ALLEMAND demande au serveur (themes.json a la
    racine, scene-<nom>.js sans .es, audio/...) : la source, avant meme
    qu'un mot s'affiche.
Le texte de l'interface (francais) est pris par la page elle-meme
(I18N.fr) : un mot francais qui ressemble a de l'allemand (« un », « die »
n'en est pas) ne fait pas de faux positif.

Meme etalonnage que parcours.py : heure figee (et avancee d'un jour pour les
jours suivants), hasard a graine, navigateur vierge, service worker bloque.
Il ne se connecte pas : les ecrans s'ouvrent par leurs fonctions.
"""
import argparse
import functools
import glob
import http.server
import json
import os
import re
import socketserver
import sys
import threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8793
PAGE = "index.html"   # --page : une autre copie (une ancienne version), a la racine
JOUR_1 = (2026, 10, 21)

HASARD_FIGE = r"""
(() => {
  let graine = 20261021;
  const suivant = () => {            // mulberry32
    graine |= 0; graine = (graine + 0x6D2B79F5) | 0;
    let t = Math.imul(graine ^ (graine >>> 15), 1 | graine);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  Math.random = suivant;
})();
"""

# Tout ce qui se dit : direAllemand (la voix de l'app), la synthese du
# navigateur, et les fichiers son. Pose avant les scripts de la page, et
# rebranche sur direAllemand des qu'elle existe.
ECOUTE_VOIX = r"""
(() => {
  window.__dit = [];
  const noter = (source, texte) => { try{ window.__dit.push(source + "\t" + String(texte)); }catch(e){} };
  try{
    const parler = speechSynthesis.speak.bind(speechSynthesis);
    speechSynthesis.speak = (u) => { noter("synthese[" + (u && u.lang) + "]", u && u.text); try{ setTimeout(() => { try{ u.onend && u.onend({}); }catch(e){} }, 10); }catch(e){} };
  }catch(e){}
  try{
    const jouer = HTMLMediaElement.prototype.play;
    HTMLMediaElement.prototype.play = function(){
      noter("son", this.currentSrc || this.src || "");
      try{ setTimeout(() => { try{ this.dispatchEvent(new Event("ended")); }catch(e){} }, 10); }catch(e){}
      return Promise.resolve();
    };
  }catch(e){}
  const brancher = () => {
    if(typeof window.direAllemand === "function" && !window.direAllemand.__ecoute){
      const vrai = window.direAllemand;
      const f = function(texte, opts){ noter("direAllemand", texte); return vrai.apply(this, arguments); };
      f.__ecoute = true;
      window.direAllemand = f;
    }
  };
  document.addEventListener("DOMContentLoaded", brancher);
  window.addEventListener("load", brancher);
  setInterval(brancher, 200);
})();
"""

# Le texte visible : la page entiere (les bulles, les fenetres, les toasts
# vivent hors de l'ecran actif), sans le contenu des <iframe>, pris a part.
TEXTE_PAGE = r"""
() => {
  const s = document.querySelector(".screen.active");
  return { ecran: s ? s.id : "(aucun)", texte: document.body.innerText || "" };
}
"""

# Dans le cadre d'une scene (visuel/prototype) : chaque zone touchee en mode
# Decouvrir -- l'etiquette affichee (« la mesa = la table ») et le mot dit.
BALAYAGE_SCENE = r"""() => {
  const out = [];
  try{ window.dire = t => out.push('DIT ' + t); }catch(e){}
  let zones = []; try{ zones = ZONES; }catch(e){ out.push('ERR pas de ZONES'); }
  for(const p of zones){
    try{ toucher(p.id, null); }catch(e){ out.push('ERR ' + e); }
    out.push([...document.querySelectorAll('.etiquette')].map(e => e.innerText.replace(/\n/g, ' ')).join(' / '));
  }
  return out;
}"""

# Les fichiers de donnees ALLEMANDS. Ce qui se termine par l'un de ces noms
# et n'est PAS sous espanol/ ou une scene .es.js est une source allemande.
FICHIERS_ALLEMANDS = re.compile(
    r"^(themes|verbe|adjectif|adverbe|funktionswort|redewendung|reperes|premiers-pas|a1-voyage|"
    r"exercices|grammaire|prononciation|conjugaison|synonymes|frequence|pruefung)\.json$"
    r"|^dict/|^audio/|^scenes/|^visuel/prototype/scene-[^/]+(?<!\.es)\.js$"
    r"|^visuel/prototype/[^/]+\.points\.json$")


def serveur():
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    gestion = functools.partial(Muet, directory=RACINE)
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


# ------------------------------------------------------------------ lexiques

MOT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+(?:-[A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+)*")

# Les mots-outils allemands que le corpus ne porte pas en entree. Les courts
# qui sont aussi espagnols ou francais (« es », « des », « den », « das »,
# « am », « um ») n'y sont pas : ils feraient du bruit sans rien prouver.
OUTILS_ALLEMANDS = set("""
der die dem ich und nicht ist ein eine einen einem einer eines mit auf
sie wir ihr bin bist sind hat habe hast haben wird werden wurde kein keine
auch noch schon sehr gut nein bitte danke heute morgen gestern hier dort
oder aber weil dass wenn wie was wer wo wohin woher warum zum zur vom beim
im ins aus bei nach von zu für über unter mein dein sein unser euer
""".split())


# Des mots de l'interface (francais, ou noms propres de l'app) qui sont AUSSI
# des entrees du corpus allemand. Le texte de l'interface n'est pas soustrait
# en bloc : une phrase allemande glissee dans une chaine francaise (un exemple
# « der Tisch » dans une aide) serait une fuite, et elle passerait.
FAUX_AMIS = """
coiffeur anna mark
""".split()


def chaines(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if not str(k).startswith("_"):     # les modes d'emploi (_lisez_moi)
                yield from chaines(v)
    elif isinstance(o, list):
        for v in o:
            yield from chaines(v)


def jetons(texte):
    return [m.group(0) for m in MOT.finditer(texte or "")]


def lexique_allemand():
    """Les mots du corpus allemand, cote allemand seulement : le mot, son
    pluriel, ses formes conjuguees et ses phrases d'exemple allemandes."""
    mots = set()
    cles_de = ("mot", "pluriel", "infinitif", "exemple", "perfekt", "praeteritum", "konjunktiv2")

    def prendre(e):
        if not isinstance(e, dict):
            return
        for c in cles_de:
            v = e.get(c)
            if isinstance(v, str):
                mots.update(jetons(v))
            elif isinstance(v, dict):          # une conjugaison : { ich: bin, ... }
                for x in v.values():
                    if isinstance(x, str):
                        mots.update(jetons(x))
        if isinstance(e.get("praesens"), dict):
            for x in e["praesens"].values():
                if isinstance(x, str):
                    mots.update(jetons(x))

    for f in ("themes.json", "verbe.json", "adjectif.json", "adverbe.json", "funktionswort.json"):
        try:
            d = json.load(open(os.path.join(RACINE, f), encoding="utf-8"))
        except Exception as e:
            print("%s illisible : %s" % (f, e))
            continue
        if f == "themes.json":
            for th in d.get("themes", []):
                for e in th.get("mots", []):
                    prendre(e)
        else:
            for v in d.values():
                for e in (v if isinstance(v, list) else []):
                    prendre(e)
    return {m.lower() for m in mots if len(m) >= 4} | OUTILS_ALLEMANDS


def lexique_espagnol_et_francais(textes_interface):
    """Ce qui n'est PAS une preuve d'allemand : tout le corpus espagnol (avec
    ses traductions), et le texte de l'interface dans ses langues."""
    mots = set()
    for f in glob.glob(os.path.join(RACINE, "espanol", "datos", "*.json")) + \
            glob.glob(os.path.join(RACINE, "espanol", "vocabulario.json")) + \
            glob.glob(os.path.join(RACINE, "visuel", "prototype", "espanol", "mots.json")):
        # (les autres fichiers des scenes espagnoles citent les zones par leur
        # mot allemand : ils ne prouvent rien.)
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for s in chaines(d):
            mots.update(m.lower() for m in jetons(s))
    for s in textes_interface:
        mots.update(m.lower() for m in jetons(s))
    return mots


def allemand_dans(texte, all_, pas_all):
    """Les mots allemands d'un texte : [(mot, ligne)]."""
    trouves = []
    for ligne in (texte or "").split("\n"):
        for m in jetons(ligne):
            b = m.lower()
            # Present dans le corpus espagnol ou ses traductions (le turc a
            # aussi des « ö ») : pas une preuve.
            if b in pas_all:
                continue
            if re.search(r"[äößÄÖ]", m) or (re.search(r"[üÜ]", m) and b not in pas_all) or b in all_:
                trouves.append((m, ligne.strip()[:160]))
    return trouves


# ------------------------------------------------------------------ parcours

def parcourir(jours, seance_max, niveau, variante, langue, bloquer=()):
    from playwright.sync_api import sync_playwright
    adresse = "http://127.0.0.1:%d/%s?apprendre=es" % (PORT, PAGE)
    releve = []          # { chemin, ecran, texte, cadres, dit, fichiers, erreurs }
    srv = serveur()
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            ctx = nav.new_context(locale=langue, viewport={"width": 390, "height": 844},
                                  service_workers="block")
            ctx.add_init_script(HASARD_FIGE)
            ctx.add_init_script(ECOUTE_VOIX)
            page = ctx.new_page()
            erreurs, fichiers = [], []
            page.on("pageerror", lambda e: erreurs.append("pageerror: " + str(e).split("\n")[0]))
            page.on("dialog", lambda d: d.dismiss())

            def requete(r):
                u = r.url.split("?")[0]
                pref = "http://127.0.0.1:%d/" % PORT
                if u.startswith(pref):
                    fichiers.append(u[len(pref):])
            page.on("request", requete)
            # --bloquer : un fichier qui ne repond pas (reseau mobile). Les
            # listes « de secours » ecrites en dur prennent alors sa place.
            if bloquer:
                ctx.route("**/*", lambda rt: rt.abort() if any(b in rt.request.url for b in bloquer) else rt.continue_())

            def attendre(ms=350):
                try:
                    page.wait_for_load_state("networkidle", timeout=6000)
                except Exception:
                    pass
                page.wait_for_timeout(ms)

            def js(code, *args):
                try:
                    return page.evaluate(code, *args) if args else page.evaluate(code)
                except Exception as e:
                    erreurs.append("evaluate: " + str(e).split("\n")[0][:200])
                    return None

            def noter(chemin):
                etat = js(TEXTE_PAGE) or {"ecran": "?", "texte": ""}
                cadres = []
                for fr in page.frames[1:]:
                    # Un cadre cache rend son textContent (scripts compris) :
                    # seul compte celui qu'on voit.
                    try:
                        if not fr.frame_element().is_visible():
                            continue
                        cadres.append(fr.evaluate("() => document.body ? document.body.innerText : ''"))
                    except Exception:
                        pass
                dit = js("() => { const d = window.__dit || []; window.__dit = []; return d; }") or []
                releve.append({"chemin": chemin, "ecran": etat["ecran"], "texte": etat["texte"],
                               "cadres": cadres, "dit": dit, "fichiers": list(fichiers),
                               "erreurs": list(erreurs)})
                fichiers.clear(); erreurs.clear()
                print("  %-60s %s" % (chemin[:60], etat["ecran"]))

            def jour(n):
                y, m, d = JOUR_1
                page.clock.set_fixed_time("%04d-%02d-%02dT09:%02d:00" % (y, m, d + n - 1, 0))

            def ouvrir():
                if variante == "latam":
                    page.goto(adresse)
                    js("() => localStorage.setItem('wortandoEs_variante', 'latam')")
                page.goto(adresse)
                attendre(1500)
                js("() => new Promise(ok => { const t0 = Date.now(); (function f(){ if((typeof themesLoaded !== 'undefined' && themesLoaded) || Date.now() - t0 > 15000) ok(); else setTimeout(f, 150); })(); })")
                attendre()

            # Une carte de la pile courante (seance, Premiers pas, visite) :
            # recto, verso, puis on la passe comme l'eleve le ferait.
            def cartes(prefixe, maxi):
                # Le paquet ENTIER, d'abord : une carte que le parcours ne
                # montre pas (sautee, au-dela de maxi) est relevee quand meme.
                paquet = js("""() => (typeof currentCards !== 'undefined' && currentCards || []).map((c, i) => {
                    const morceaux = [];
                    const prendre = v => { if(typeof v === 'string') morceaux.push(v);
                        else if(Array.isArray(v)) v.forEach(prendre);
                        else if(v && typeof v === 'object') Object.keys(v).forEach(k => prendre(v[k])); };
                    prendre(c.word); prendre(c.phrase); prendre(c.tableau); prendre(c.choix); prendre(c.contexte);
                    // Le mode et le theme (« redewendungen », « praep »...) sont des
                    // noms internes, allemands : en tete, avant « :: », hors analyse.
                    return (i + 1) + ' ' + (c.mode || '') + ' ' + (c.forme || '') + ' ' + (c.themeId || '') + ' :: ' + morceaux.join(' | ');
                })""") or []
                if paquet:
                    releve.append({"chemin": prefixe + " (paquet entier)", "ecran": "paquet", "texte": "\n".join(paquet),
                                   "cadres": [], "dit": [], "fichiers": [], "erreurs": []})
                vues = 0
                while vues < maxi:
                    info = js("""() => {
                        const s = document.querySelector('.screen.active');
                        const it = (typeof currentCards !== 'undefined' && currentCards) ? currentCards[currentFlashcard] : null;
                        return { ecran: s ? s.id : '', a: !!it, mode: it ? (it.mode || '') : '', forme: it ? (it.forme || '') : '',
                                 i: typeof currentFlashcard === 'number' ? currentFlashcard : -1,
                                 n: (typeof currentCards !== 'undefined' && currentCards) ? currentCards.length : 0,
                                 visite: typeof decouverteEnCours === 'function' && decouverteEnCours() };
                    }""")
                    if not info or not info["a"] or info["ecran"] not in ("flashcards", "decouverte"):
                        break
                    vues += 1
                    nom = "%s carte %d/%d %s%s" % (prefixe, info["i"] + 1, info["n"], info["mode"],
                                                   (" " + info["forme"]) if info["forme"] else "")
                    noter(nom + " [recto]")
                    if info["mode"] != "phrase":
                        js("() => { try{ flipCard(); }catch(e){} try{ if(document.querySelector('.verb-extra.hidden')) toggleVerbExtra(); }catch(e){} }")
                        attendre(250)
                        noter(nom + " [verso]")
                        avant = info["i"]
                        js("() => { try{ reviewGood(); }catch(e){ try{ nextFlashcard(); }catch(e2){} } }")
                        attendre(250)
                    else:
                        # Le premier choix offert, puis Continuer. Un champ a
                        # remplir (dictee) recoit un mot, et son bouton.
                        js("""() => {
                            const el = document.getElementById('cartePhrase');
                            if(!el) return;
                            const champ = el.querySelector('input, textarea');
                            if(champ){ champ.value = 'x'; champ.dispatchEvent(new Event('input', {bubbles:true})); }
                            const bts = [...el.querySelectorAll('button')].filter(b => b.offsetParent !== null
                                && !b.classList.contains('primary') && !b.classList.contains('av-bulle-eux'));
                            const choix = bts.find(b => b.closest('.cp-choix, .cp-tuiles, .cp-blocs, .cp-options')) || bts[0];
                            if(choix) choix.click();
                        }""")
                        attendre(300)
                        noter(nom + " [reponse]")
                        # Le choix a pu faire avancer la pile (un tableau a lire,
                        # dont le bouton EST la suite) : rien de plus, alors.
                        if js("() => currentFlashcard") != info["i"]:
                            continue
                        js("""() => {
                            const el = document.getElementById('cartePhrase');
                            const suite = el && [...el.querySelectorAll('button.primary')].find(b => b.offsetParent !== null);
                            if(suite) suite.click();
                            else { try{ cacherCartePhrase(); }catch(e){} try{ nextFlashcard(); }catch(e){} }
                        }""")
                        attendre(250)
                    # Une carte qui ne bouge pas (un geste attendu qu'on ne
                    # connait pas) : on la passe, pour ne pas tourner en rond.
                    apres = js("() => typeof currentFlashcard === 'number' ? currentFlashcard : -1")
                    if apres == info["i"] and js("() => document.querySelector('.screen.active') && document.querySelector('.screen.active').id") in ("flashcards", "decouverte"):
                        js("() => { try{ cacherCartePhrase(); }catch(e){} try{ nextFlashcard(); }catch(e){} }")
                        attendre(250)
                noter(prefixe + " fin")

            def ecran():
                return js("() => { const s = document.querySelector('.screen.active'); return s ? s.id : ''; }")

            def accueil(nom):
                js("() => { try{ goHome(); }catch(e){} }")
                attendre(600)
                noter(nom)

            # ---------------- jour 1 : le compte neuf
            jour(1)
            ouvrir()
            noter("j1 ouverture")
            # Les tuiles Verbes et Adjectifs (A1), avant tout le reste : la
            # premiere carte, recto et verso, SANS la juger (le compte reste
            # neuf pour la suite). C'est la que se voient les listes de secours
            # quand verbos.json ou adjetivos.json n'arrivent pas (--bloquer).
            for nom, appel in [("tuile verbes A1", "startVerbeLevel('A1')"), ("tuile adjectifs A1", "startAdjektiveLevel('A1')")]:
                js("() => { try{ " + appel + "; }catch(e){} }")
                attendre(1500)
                noter(nom + " [recto]")
                if ecran() == "flashcards":
                    js("() => { try{ flipCard(); }catch(e){} }")
                    attendre(300)
                    noter(nom + " [verso]")
                js("() => { try{ goHome(); }catch(e){} }")
                attendre(300)

            # L'ecran de bienvenue de l'inscription (ouvrirBienvenue), le niveau
            # declare, CONTINUER ; puis le profil s'il est pose, et la visite.
            js("() => { try{ ouvrirBienvenue(); }catch(e){} }")
            attendre(500)
            js("(n) => { try{ choisirNiveauDeclare(n); }catch(e){} }", niveau)
            noter("j1 bienvenue")
            js("() => { try{ completeInitialSetup(); }catch(e){} }")
            attendre(800)
            for k in range(2):
                if ecran() != "profil":
                    break
                noter("j1 profil %d" % (k + 1))
                js("""() => { const vis = sel => [...document.querySelectorAll(sel)].find(b => b.offsetParent !== null);
                              const b = vis('#profil [data-raison]') || vis('#profil [data-facon]'); if(b) b.click(); }""")
                attendre(900)
            noter("j1 visite intro")
            for etape in range(1, 7):
                if not js("() => { try{ return decouverteEnCours(); }catch(e){ return false; } }"):
                    break
                js("(n) => { try{ allerEtapeDecouverte(n); }catch(e){} }", etape)
                attendre(1500)
                noter("j1 visite etape %d" % etape)
                if etape == 2:
                    cartes("j1 visite", 12)
            js("() => { try{ if(decouverteEnCours()) terminerDecouverte(); }catch(e){} try{ if(decouverteEnCours()) fermerDecouverte(); }catch(e){} }")
            attendre(800)
            noter("j1 apres visite")
            accueil("j1 accueil")
            js("() => { try{ reafficherReperes(); }catch(e){} }")
            for i in range(6):
                ok = js("""(i) => { const b = [...document.querySelectorAll('[data-repere]')].filter(e => e.offsetParent !== null)[i];
                                    if(!b) return false; b.click(); return true; }""", i)
                if not ok:
                    break
                attendre(300)
                noter("j1 repere %d" % (i + 1))

            for n in range(1, jours + 1):
                if n > 1:
                    jour(n)
                    ouvrir()
                    accueil("j%d accueil" % n)
                # Premiers pas (le bouton 🌱), s'il est encore en cours.
                if js("() => { try{ return premiersPasEnCours(); }catch(e){ return false; } }"):
                    js("() => { try{ ouvrirPremiersPas(); }catch(e){} }")
                    attendre(1200)
                    cartes("j%d premiers pas" % n, seance_max)
                    accueil("j%d accueil apres premiers pas" % n)
                # La seance du jour, cartes et scene.
                js("() => { try{ ouvrirSeanceDuJour(true); }catch(e){} }")
                attendre(1500)
                cartes("j%d seance" % n, seance_max)
                accueil("j%d accueil apres seance" % n)
                # La scene du jour, dans son cadre.
                js("() => { try{ ouvrirSceneSeance(); }catch(e){} }")
                attendre(3000)
                noter("j%d scene du jour" % n)
                for k in range(6):
                    if not page.frames[1:]:
                        break
                    fr = page.frames[1]
                    try:
                        fr.evaluate("""() => { const b = [...document.querySelectorAll('button, .zone, [data-zone]')].filter(e => e.offsetParent !== null);
                                               const x = b[Math.min(b.length - 1, 1)]; if(x) x.click(); }""")
                    except Exception:
                        pass
                    attendre(700)
                    noter("j%d scene du jour geste %d" % (n, k + 1))
                accueil("j%d accueil apres scene" % n)
                # Ecouter, repeter : le bouton ▶ de l'accueil, comme l'usager.
                js("() => { try{ ecouterDepuisAccueil(); }catch(e){} }")
                attendre(6000)
                noter("j%d ecouter, repeter" % n)
                js("() => { try{ quitterEcoute(); }catch(e){} }")
                accueil("j%d fin" % n)

            # LES SCENES, OBJET PAR OBJET : en mode Decouvrir (celui de la
            # visite), chaque zone touchee, son etiquette et ce qui se dit.
            # Toutes les scenes de l'app, et celle de la visite.
            noms = js("() => { try{ return [SCENE_DECOUVERTE].concat(SCENES_SEANCE.map(s => s.nom)); }catch(e){ return []; } }") or []
            cadre = ctx.new_page()
            for nom in dict.fromkeys(noms):
                try:
                    cadre.goto("http://127.0.0.1:%d/visuel/prototype/index.html?scene=%s&visite=1&lang=fr&apprendre=es&variante=%s"
                               % (PORT, nom, variante))
                    cadre.wait_for_timeout(900)
                    vu = cadre.evaluate(BALAYAGE_SCENE)
                except Exception as e:
                    vu = ["ERR " + str(e).split("\n")[0][:150]]
                releve.append({"chemin": "scene %s (chaque objet touche)" % nom, "ecran": "scene",
                               "texte": "\n".join(v for v in vu if not v.startswith("DIT ")),
                               "cadres": [], "dit": ["direAllemand\t" + v[4:] for v in vu if v.startswith("DIT ")],
                               "fichiers": list(fichiers), "erreurs": [v for v in vu if v.startswith("ERR ")]})
                fichiers.clear()
                print("  %-60s %s" % ("scene %s" % nom, len(vu)))
            cadre.close()

            # L'APP INSTALLEE (21 oct. 2026, Marc-Antoine) : l'icone de l'ecran
            # d'accueil ouvre le start_url du manifeste, avec un stockage
            # VIERGE (iOS ne lui passe rien de Safari). Elle doit s'ouvrir en
            # espagnol.
            vierge = nav.new_context(locale="fr-FR", service_workers="block")
            pg = vierge.new_page()
            try:
                pg.goto(adresse)
                pg.wait_for_timeout(800)
                lien = pg.evaluate("() => { const l = document.querySelector('link[rel=\"manifest\"]'); return l ? l.href : ''; }")
                man = pg.evaluate("(u) => fetch(u).then(r => r.json()).then(m => new URL(m.start_url || './', u).href).catch(() => '')", lien)
                vierge.close()
                vierge = nav.new_context(locale="fr-FR", service_workers="block")
                pg = vierge.new_page()
                pg.goto(man)
                pg.wait_for_timeout(800)
                langue = pg.evaluate("() => { try{ return LANGUE_APPRISE; }catch(e){ return '?'; } }")
            except Exception as e:
                lien, man, langue = "", "", "? " + str(e).split("\n")[0][:100]
            vierge.close()
            releve.append({"chemin": "app installee (start_url du manifeste, stockage vierge)", "ecran": "manifeste",
                           "texte": "", "cadres": [], "dit": [], "fichiers": [], "erreurs": [],
                           "langue_installee": langue, "manifeste": lien, "start_url": man})
            print("  %-60s %s" % ("app installee : " + man.replace("http://127.0.0.1:%d/" % PORT, ""), langue))

            # L'A1 voyage, s'il existe pour ce compte.
            if js("() => { try{ activerA1Voyage(); return true; }catch(e){ return false; } }"):
                attendre(800)
                js("() => { try{ ouvrirSeanceDuJour(true); }catch(e){} }")
                attendre(1500)
                cartes("a1 voyage seance", seance_max)
                accueil("a1 voyage fin")
            nav.close()
    finally:
        srv.shutdown()
    return releve


def analyser(releve, all_, pas_all):
    fuites = []
    for r in releve:
        vus = set()
        texte_vu = r["texte"]
        if r["ecran"] == "paquet":
            texte_vu = "\n".join(l.split(" :: ", 1)[-1] for l in texte_vu.split("\n"))
        for source, texte in [("paquet" if r["ecran"] == "paquet" else "affiche", texte_vu)] + [("cadre", c) for c in r["cadres"]]:
            for mot, ligne in allemand_dans(texte, all_, pas_all):
                cle = (source, mot, ligne)
                if cle in vus:
                    continue
                vus.add(cle)
                fuites.append({"chemin": r["chemin"], "ecran": r["ecran"], "source": source,
                               "mot": mot, "ligne": ligne})
        for d in r["dit"]:
            source, _, texte = d.partition("\t")
            if source == "son":
                chemin = texte.replace("http://127.0.0.1:%d/" % PORT, "").split("?")[0]
                if FICHIERS_ALLEMANDS.search(chemin):
                    fuites.append({"chemin": r["chemin"], "ecran": r["ecran"], "source": "son",
                                   "mot": chemin, "ligne": chemin})
                continue
            for mot, ligne in allemand_dans(texte, all_, pas_all):
                fuites.append({"chemin": r["chemin"], "ecran": r["ecran"], "source": "voix " + source,
                               "mot": mot, "ligne": ligne})
        if r.get("ecran") == "manifeste" and r.get("langue_installee") != "es":
            fuites.append({"chemin": r["chemin"], "ecran": r["ecran"], "source": "app installee",
                           "mot": str(r.get("langue_installee")),
                           "ligne": "le manifeste %s ouvre %s, qui demarre en « %s »" % (
                               r.get("manifeste"), r.get("start_url"), r.get("langue_installee"))})
        for f in r["fichiers"]:
            if FICHIERS_ALLEMANDS.search(f):
                fuites.append({"chemin": r["chemin"], "ecran": r["ecran"], "source": "fichier",
                               "mot": f, "ligne": f})
    return fuites


def main():
    global PORT, PAGE
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=int, default=3)
    ap.add_argument("--seance-max", type=int, default=60, help="cartes au plus par paquet")
    ap.add_argument("--niveau", default="zero", help="la reponse a « tu connais deja un peu ? » : zero, peu, A2...")
    ap.add_argument("--variante", default="es", choices=["es", "latam"], help="Espagne ou Amerique latine")
    ap.add_argument("--locale", default="fr-FR", help="la langue du telephone (l'interface la suit)")
    ap.add_argument("--port", type=int, default=PORT)
    ap.add_argument("--page", default=PAGE, help="autre fichier que index.html, a la racine du depot")
    ap.add_argument("--bloquer", action="append", help="fichier qui ne repond pas (ex. verbos.json) ; repetable")
    ap.add_argument("--releve", help="ecrire tout le releve (JSON) ici")
    ap.add_argument("--relire", help="analyser un releve deja pris, sans navigateur")
    a = ap.parse_args()
    PORT = a.port
    PAGE = a.page
    all_ = lexique_allemand()
    pas_all = lexique_espagnol_et_francais(FAUX_AMIS)
    all_ -= pas_all
    if a.relire:
        releve = json.load(open(a.relire, encoding="utf-8"))
    else:
        releve = parcourir(a.jours, a.seance_max, a.niveau, a.variante, a.locale, a.bloquer or ())
        if a.releve:
            with open(a.releve, "w", encoding="utf-8") as f:
                json.dump(releve, f, ensure_ascii=False, indent=1)
    fuites = analyser(releve, all_, pas_all)
    erreurs = [(r["chemin"], e) for r in releve for e in r["erreurs"]]
    print()
    if erreurs:
        print("%d erreur(s) JavaScript :" % len(erreurs))
        for c, e in erreurs[:30]:
            print("  %-40s %s" % (c[:40], e[:150]))
        print()
    if not fuites:
        print("%d ecrans releves : aucune fuite d'allemand." % len(releve))
        return 0
    print("%d fuite(s) d'allemand sur %d ecrans :" % (len(fuites), len(releve)))
    for f in fuites:
        print("  [%s] %s (%s) : %s -- %s" % (f["source"], f["chemin"], f["ecran"], f["mot"], f["ligne"]))
    return 1


if __name__ == "__main__":
    sys.exit(main())
