# -*- coding: utf-8 -*-
"""LES PHRASES TRADUITES DES THEMES ILLUSTRES DANS TOUTES LES LANGUES D'INTERFACE -- l'outillage (lot 0 de l'alignement
des langues, 13 nov. 2026 ; plan : side-session-notes du chef, alignement-themes-langues-plan.md).

LE CONSTAT. Une page de theme (visuel/prototype/<theme>.html) montre la PHRASE traduite en francais, anglais,
portugais (et allemand pour qui apprend l'espagnol) : la page la fabrique avec son propre code, morceau par morceau.
En turc, ukrainien, persan, arabe, polonais et russe, elle ne montre que la glose du mot (gloses.json), jamais la
phrase. L'arabe manque aussi a qui apprend l'espagnol.

LA METHODE : LE CHEMIN NATIF (decision du chef du 14 nov., apres le releve des 22 themes). Un dictionnaire de
phrases entieres (essaye au lot 0) demanderait 12 053 entrees, environ 107 000 mots par langue, et ne serait jamais
complet : 14 themes sont COMBINATOIRES (chaque prix des courses, chaque addition, chaque horaire, chaque suite
d'etapes de la journee). On traduit donc les MORCEAUX que chaque theme assemble, la ou l'anglais et le portugais
l'ont deja fait : dans le generateur (visuel/<theme>/langues.py, appele par visuel/<theme>/<theme>.py) ou dans
l'objet de la page. Chaque langue y a sa petite grammaire (le cas apres la preposition, l'ordre des mots, le
suffixe turc apres l'heure). Ce n'est plus le francais qui sert de pivot : la phrase allemande, qui porte son cas
(« auf dem Tisch » / « auf den Tisch »), recoit sa traduction directement.

Themes branches (lot par lot, dans l'ordre fixe par le chef : tr, uk, pl, ru, puis fa et ar, l'arabe de l'espagnol
en lot 7) : BRANCHES ci-dessous. Les points douteux de chaque langue : retours/A-RELIRE-THEMES-<LG>.md.

    python visuel/langues_themes.py extraire [theme...]        # joue les pages en FRANCAIS (navigateur, VERROU des
                                                               #   parcours) -> visuel/langues_themes/source.json
    python visuel/langues_themes.py verifier <theme...> [lg..] # LE CONTROLE : chaque page ouverte dans chaque langue
                                                               #   (navigateur, VERROU) ; code 1 s'il y a un defaut

LE CONTROLE (verifier). La meme promenade qu'extraire, la page ouverte en allemand appris et dans la langue. Defauts :
aucune phrase traduite ; une traduction francaise (une phrase de source.json, ou une glose francaise) ; en ukrainien
et en russe, des lettres latines ; une erreur JavaScript. LANGUES_EXEMPLES=<fichier.json> ecrit les phrases vues,
pour la relecture.

L'EXTRACTION. Chaque page est ouverte avec lang=fr, en allemand puis en espagnol appris. On parcourt la decouverte
(decouvrir() puis chaque bouton, sur deux niveaux : onglets puis elements), puis chaque SORTE de question (EX) pour
chaque mot du theme (motsDuTheme()), comme visuel/voix_themes.py, avec une reponse touchee au hasard (juste ou
fausse : les deux montrent une traduction, la phrase juste et le choix faux). Apres chaque geste, on releve le texte
de chaque .trad de la page : la phrase traduite, et dans un .trad.faux ce qui suit le dernier « — » (le sens du choix
faux). La source (la phrase de la langue apprise a cote, [lang=de|es]) est notee pour les traducteurs.
Les GLOSES (un mot et sa traduction du corpus) ne comptent pas : la page les donne deja dans chaque langue. Est une glose un texte dont la traduction (apres le dernier « — », ou le texte entier) est une valeur
francaise des gloses du theme (D.gloses, gloses.json, GLOSES).
`tard` : les textes neufs des 20 % derniers tirages d'une sorte ; 0 = la sorte est epuisee. Un theme dont une sorte
n'est pas epuisee se relance avec plus de tirages (LANGUES_TIRAGES, 2000 par defaut).

LIMITES CONNUES DU PROMENEUR (16 nov. 2026, lot 3 « Les contraires », a corriger plus tard) :
1. « donnee vue N / M » lit D.trad (ATTENDUS) : juste pour gato et journee, ou D.trad porte les phrases ; dans
   contrarios (et tout theme ou D.trad porte les GLOSES des mots), la mesure compte des gloses, que le releve exclut :
   « 0 / 18 » n'y dit rien.
2. Dans contrarios, la sorte « endung » (« Das ist ein großer Koffer. ») n'est jamais atteinte : ni le francais de
   source.json ni le controle n'en voient une phrase (35 phrases vues sur 58). La page les traduit bien (sonde
   directe de EX.endung en fr, ru, ar, 16 nov.) : la cause est dans ENUMERER, pas dans la page. Jusqu'a la
   correction, une sorte absente du releve se sonde a part.

Langues d'interface a aligner : allemand appris -> tr, uk, fa, ar, pl, ru (fr, en, pt : deja la) ; espagnol appris
-> ar (fr, en, pt, de : deja la). Port : LANGUES_PORT (8858 par defaut, jamais 8791).
"""
import functools, http.server, io, json, os, re, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
# hors des fichiers servis (publication/construire_site.py) : le releve sert au controle, pas a la page
DOSSIER = os.path.join(ICI, "langues_themes")
SOURCE = os.path.join(DOSSIER, "source.json")
PORT = int(os.environ.get("LANGUES_PORT", "8858"))
# la langue apprise du controle (de par defaut ; es pour l'arabe de qui apprend l'espagnol)
APPRENDRE_CTRL = os.environ.get("LANGUES_APPRENDRE", "de")
TIRAGES = int(os.environ.get("LANGUES_TIRAGES", "2000"))
# la decouverte (onglets puis elements) s'arrete a ce nombre de gestes ; atteint = releve peut-etre tronque, signale
PLAFOND = int(os.environ.get("LANGUES_GESTES", "3000"))
THEMES = ["familia", "descripcion", "emociones", "contrarios", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "transportes",
          "loisirs", "animales", "meteo", "logement", "demarches", "courses", "vacances", "travail", "ecole", "ciudad", "fetes", "heure"]
# la langue apprise -> les langues d'interface que le DICTIONNAIRE doit couvrir (les autres, la page les fabrique)
BESOIN = {"de": ["tr", "uk", "fa", "ar", "pl", "ru"], "es": ["ar"]}
LANGUES = ["tr", "uk", "fa", "ar", "pl", "ru"]
# les themes deja branches, et leurs langues (lot 1 : journee + gato, 14 nov. 2026)
# lot 2 (ligne 111, 15 nov.) : la famille d'Anna dans les six langues, dans la page (visuel/prototype/familia/langues.js),
# l'arabe aussi pour qui apprend l'espagnol (LANGUES_APPRENDRE=es)
# lot 3 (16 nov.) : les contraires dans les six langues, phrase par phrase dans le generateur (visuel/contrarios/langues.py)
# lot 4 (16 nov.) : les demarches dans les six langues, morceaux et grammaire dans la page (visuel/prototype/demarches/langues.js)
# lot 5 (16 nov.) : l'ecole dans les six langues, de meme (visuel/prototype/ecole/langues.js)
# lot 6 (16 nov.) : les fetes et invitations dans les six langues, de meme (visuel/prototype/fetes/langues.js)
# lot 7 (16 nov.) : faire les courses dans les six langues, de meme (visuel/prototype/courses/langues.js)
# lot 8 (16 nov.) : les vacances dans les six langues, chaque etape conjuguee (visuel/prototype/vacances/langues.js)
# lot 9 (16 nov.) : les loisirs dans les six langues (visuel/prototype/loisirs/langues.js)
# lot 10 (16 nov.) : manger et gouter dans les six langues (visuel/prototype/manger/langues.js)
# lot 11 (16 nov.) : les metiers dans les six langues, chaque phrase refaite par sa grammaire dans le generateur (visuel/metiers/langues.py)
# lot 12 (16 nov.) : la meteo dans les six langues, ses phrases fixes, ses mois et ses degres (visuel/meteo/langues.py)
# lot 13 (16 nov.) : les animaux dans les six langues, chaque phrase refaite par sa grammaire dans le generateur (visuel/animales/langues.py)
# lot 14 (16 nov.) : la ville dans les six langues, les lieux, les questions et les itineraires refaits par le generateur (visuel/ciudad/langues.py)
BRANCHES = {"gato": ["tr", "uk", "pl", "ru"], "journee": ["tr", "uk", "pl", "ru"], "familia": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "contrarios": ["tr", "uk", "pl", "ru", "fa", "ar"], "demarches": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "ecole": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "fetes": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "courses": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "vacances": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "loisirs": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "manger": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "metiers": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "meteo": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "animales": ["tr", "uk", "pl", "ru", "fa", "ar"],
            # l'heure et les dates (16 nov.) : ne avec ses six langues, chaque phrase fabriquee par sa grammaire
            # (visuel/prototype/heure/dire.js, le meme fichier que la langue apprise)
            "heure": ["tr", "uk", "pl", "ru", "fa", "ar"],
            "ciudad": ["tr", "uk", "pl", "ru", "fa", "ar"]}
BRANCHEES = ["tr", "uk", "pl", "ru"]

RELEVER = r"""() => {
  const out = [];
  document.querySelectorAll('.trad').forEach(el => {
    let t = (el.textContent || '').replace(/\s+/g, ' ').trim(), faux = el.classList.contains('faux');
    if (!t) return;
    // choix faux : « Tu as choisi : <le choix touche> — <son sens> » ; la source est le choix, pas la phrase juste
    let srcFaux = null;
    if (faux) { const i = t.lastIndexOf(' — '); if (i < 0) return; const avant = t.slice(0, i), d = avant.indexOf(': ');
                srcFaux = (d >= 0 ? avant.slice(d + 2) : avant).trim(); t = t.slice(i + 3).trim(); if (!t) return; }
    // la phrase de la langue apprise est ecrite JUSTE AVANT sa traduction (cible(phrase) + traduction(...)) : le
    // dernier [lang] qui precede le .trad, pas le premier du parent (« Sehr gut! », « Richtig », un bouton)
    const p = el.parentElement;
    const avants = p ? Array.from(p.querySelectorAll('[lang="' + APPRENDRE + '"]'))
      .filter(x => !x.contains(el) && !el.contains(x) && (x.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)) : [];
    const s = avants.length ? avants[avants.length - 1] : null;
    out.push({fr: t, src: srcFaux !== null ? srcFaux : (s ? (s.textContent || '').replace(/\s+/g, ' ').trim() : ''), faux});
  });
  return out;
}"""

# toutes les valeurs francaises des gloses connues de la page (pour reconnaitre une glose)
GLOSES_FR = r"""() => {
  const fr = new Set();
  const prendre = o => { if (!o || typeof o !== 'object') return;
    for (const v of Object.values(o)) { if (v && typeof v === 'object') { if (typeof v.fr === 'string') fr.add(v.fr.trim()); else prendre(v); } } };
  try { if (typeof D !== 'undefined' && D && D.gloses) prendre(D.gloses); } catch (e) {}
  try { if (typeof GLOSES !== 'undefined') prendre(GLOSES); } catch (e) {}
  return [...fr];
}"""

ENUMERER = r"""async ([n, relever, PLAFOND_GESTES]) => {
  const vus = new Map(), relev = eval(relever);
  const noter = () => { for (const r of relev()) { const k = r.fr + '\u0001' + r.src; if (!vus.has(k)) vus.set(k, {fr: r.fr, src: r.src, faux: r.faux}); } };
  const pause = ms => new Promise(r => setTimeout(r, ms));
  try { if (typeof Voix !== 'undefined') Voix.dire = () => {}; } catch (e) {}
  // 1. la decouverte : chaque bouton, puis chaque bouton qui apparait (onglets -> elements)
  const boutons = () => Array.from(document.querySelectorAll('#zone button')).filter(b => !b.classList.contains('ecoute'));
  let gestes = 0;
  if (typeof decouvrir === 'function') {
    try { await decouvrir(); } catch (e) {}
    noter();
    const n1 = boutons().length;
    for (let i = 0; i < n1 && gestes < PLAFOND_GESTES; i++) {
      try { await decouvrir(); const b1 = boutons()[i]; if (!b1) continue; b1.click(); gestes++; await pause(0); noter();
            const n2 = boutons().length;
            for (let j = 0; j < n2 && gestes < PLAFOND_GESTES; j++) {
              try { await decouvrir(); const a = boutons()[i]; if (!a) break; a.click(); const b2 = boutons()[j]; if (!b2) continue; b2.click(); gestes++; noter(); } catch (e) {}
            } } catch (e) {}
    }
  }
  const apresDecouverte = vus.size;
  // 2. les questions : chaque sorte, pour chaque mot, comme montrer() (voix_themes.py)
  const liste = Object.keys(EX).filter(x => typeof SORTES === 'undefined' || SORTES.includes(x));
  const mots = typeof motsDuTheme === 'function' ? motsDuTheme() : [];
  const hasard = a => a[Math.floor(Math.random() * a.length)], sortes = {};
  const k = Math.max(20, Math.ceil(n / Math.max(1, mots.length)));
  const vider = () => { for (const v of ['motQ', 'vuQ', 'sensQ']) { try { eval(v + ' = null'); } catch (e) {} } };
  for (const t of liste) {
    const avant = vus.size; let tard = 0, poses = 0, erreurs = 0;
    try { sorteCourante = t; } catch (e) {}
    for (const w of (mots.length ? mots : [undefined])) {
      for (let i = 0; i < k; i++) {
        const s0 = vus.size;
        try {
          repondu = false; vider();
          if (!EX[t](w)) break;
          poses++;
          const z = document.getElementById('zone');
          const c = Array.from(z.querySelectorAll('#choix button'));
          if (c.length) hasard(c).click();
          else if (typeof testerOrdre === 'function' && z.querySelector('.ordre')) testerOrdre();
          else { const a = Array.from(z.querySelectorAll('.arbre g.p:not(.ego), .rangee button, .corps .zone, .plan .cible'));
                 if (a.length) hasard(a).dispatchEvent(new MouseEvent('click', {bubbles: true})); }
          noter();
        } catch (e) { erreurs++; break; }
        if (i >= k * 0.8) tard += vus.size - s0;
      }
    }
    sortes[t] = {textes: vus.size - avant, tard, poses, erreurs};
  }
  return {textes: [...vus.values()], sortes, mots: mots.length, decouverte: apresDecouverte, gestes};
}"""


def extraire(seuls):
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Muet, directory=RACINE))
    srv.handle_error = lambda *a: None
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    source = json.load(io.open(SOURCE, encoding="utf-8")) if os.path.exists(SOURCE) else {}
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for th in THEMES:
                if seuls and th not in seuls:
                    continue
                source[th] = {}
                for app in ("de", "es"):
                    page = nav.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0][:160]))
                    page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&lang=fr" % (PORT, th, app))
                    page.wait_for_function("() => typeof EX !== 'undefined' && (typeof IDS === 'undefined' || IDS.length > 0) && (typeof D === 'undefined' || D)", timeout=30000)
                    page.wait_for_timeout(600)
                    gl = set(page.evaluate(GLOSES_FR))
                    e = page.evaluate(ENUMERER, [TIRAGES, RELEVER, PLAFOND])
                    phrases, gloses = [], 0
                    for x in e["textes"]:
                        if x["fr"] in gl:
                            gloses += 1
                            continue
                        phrases.append({"fr": x["fr"], "src": x["src"]} if x["src"] else {"fr": x["fr"]})
                    phrases.sort(key=lambda x: (x["fr"], x.get("src", "")))
                    source[th][app] = phrases
                    ouvertes = {s: v["tard"] for s, v in e["sortes"].items() if v["tard"]}
                    # une meme phrase francaise pour deux sources (« sur la table » : auf dem / auf den Tisch) : le
                    # francais ne porte pas le cas que l'ukrainien, le russe ou le polonais demandent
                    srcs = {}
                    for x in phrases:
                        srcs.setdefault(x["fr"], set()).add(x.get("src", ""))
                    ambigus = sum(1 for v in srcs.values() if len(v) > 1)
                    print("  %-12s %s  %4d phrases francaises (%d couples avec la source, %d ambigus), %d par la decouverte, "
                          "%d gestes%s, %d gloses ecartees ; sortes non epuisees : %s%s"
                          % (th, app, len(srcs), len(phrases), ambigus, e["decouverte"], e["gestes"], " (PLAFOND ATTEINT)" if e["gestes"] >= PLAFOND else "", gloses, ouvertes or "aucune",
                             ("  ERREURS JS : " + " | ".join(erreurs[:3])) if erreurs else ""), flush=True)
                    page.close()
                jamais = phrases_de_la_donnee(th) - {x["fr"] for a in source[th].values() for x in a}
                if jamais:
                    print("  %-12s    %d phrase(s) de la donnee (3 mots et plus) jamais affichee(s) : %s"
                          % (th, len(jamais), " | ".join(sorted(jamais)[:4])), flush=True)
            try:
                nav.close()
            except Exception:
                pass
    finally:
        srv.shutdown()
    os.makedirs(DOSSIER, exist_ok=True)
    io.open(SOURCE, "w", encoding="utf-8", newline="\n").write(json.dumps(source, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print("  -> %s" % os.path.relpath(SOURCE, RACINE))


def phrases_de_la_donnee(th):
    """Les valeurs « fr » de 3 mots et plus des JSON du theme (visuel/prototype/<theme>/*.json, sauf gloses.json) :
    controle de couverture -- une phrase de la donnee que l'extraction n'a jamais vue est un geste oublie (ou un
    texte que la page n'affiche pas, a verifier). Les gloses et noms d'objets (1-2 mots) n'y entrent pas."""
    res, d = set(), os.path.join(ICI, "prototype", th)
    def prendre(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "fr" and isinstance(v, str) and mots(v) >= 3:
                    res.add(re.sub(r"\s+", " ", v).strip())
                else:
                    prendre(v)
        elif isinstance(o, list):
            for v in o:
                prendre(v)
    if os.path.isdir(d):
        for f in os.listdir(d):
            if f.endswith(".json") and f != "gloses.json":
                try:
                    prendre(json.load(io.open(os.path.join(d, f), encoding="utf-8")))
                except ValueError:
                    pass
    return res


def mots(s):
    return len(re.findall(r"\w+", s, re.U))


GLOSES_LG = r"""(lg) => {
  const out = new Set();
  const prendre = o => { if (!o || typeof o !== 'object') return;
    for (const v of Object.values(o)) { if (v && typeof v === 'object') { if (typeof v[lg] === 'string') out.add(v[lg].trim()); else prendre(v); } } };
  try { if (typeof D !== 'undefined' && D && D.gloses) prendre(D.gloses); } catch (e) {}
  try { if (typeof GLOSES !== 'undefined') prendre(GLOSES); } catch (e) {}
  return [...out];
}"""

# ce que la donnee du theme a traduit dans la langue (gato : D.trad.de et D.groupes.de ; journee : les frequences) --
# pour dire combien la promenade en a montre
ATTENDUS = r"""(lg) => {
  const out = new Set();
  try { for (const v of Object.values((D.trad || {})[APPRENDRE] || {})) if (v[lg]) out.add(v[lg]); } catch (e) {}
  try { for (const f of (D.frequences || [])) if (f[lg]) out.add(f[lg]); } catch (e) {}
  return [...out];
}"""

LATIN = re.compile(r"[A-Za-zÀ-ÿ]{3,}")
NOMS_LATINS = {"Moritz"}


def verifier(seuls, langues):
    """Chaque theme branche (lot par lot), ouvert en allemand appris et dans chaque langue : la promenade d'extraire
    (decouverte, puis chaque sorte et chaque mot, une reponse au hasard), et chaque .trad releve. DEFAUTS : une page
    sans aucune phrase traduite ; une traduction FRANCAISE (connue de source.json, ou une glose francaise) ; en
    ukrainien et en russe, des lettres latines (un mot resté en francais, en allemand ou en anglais) ; une erreur
    JavaScript. Le nombre de phrases traduites vues est donne, et pour gato et journee, la part de la donnee vue."""
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Muet, directory=RACINE))
    srv.handle_error = lambda *a: None
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    source = json.load(io.open(SOURCE, encoding="utf-8")) if os.path.exists(SOURCE) else {}
    defauts, exemples = 0, {}
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for th in seuls:
                francais = {x["fr"] for x in source.get(th, {}).get(APPRENDRE_CTRL, []) if mots(x["fr"]) >= 2}
                for lg in langues:
                    page = nav.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0][:160]))
                    page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&lang=%s" % (PORT, th, APPRENDRE_CTRL, lg))
                    page.wait_for_function("() => typeof EX !== 'undefined' && (typeof IDS === 'undefined' || IDS.length > 0) && (typeof D === 'undefined' || D)", timeout=30000)
                    page.wait_for_timeout(600)
                    gl_fr = set(page.evaluate(GLOSES_FR))
                    gl_lg = set(page.evaluate(GLOSES_LG, lg))
                    attendus = set(page.evaluate(ATTENDUS, lg))
                    e = page.evaluate(ENUMERER, [TIRAGES, RELEVER, PLAFOND])
                    vues, fautes = set(), []
                    for x in e["textes"]:
                        t = x["fr"]
                        if t in gl_lg:
                            continue
                        if t in francais or (t in gl_fr and mots(t) >= 2):
                            fautes.append("en francais : « %s »" % t)
                        elif lg in ("uk", "ru") and [w for w in LATIN.findall(t) if w not in NOMS_LATINS]:
                            fautes.append("lettres latines : « %s »" % t)
                        vues.add(t)
                    if not vues:
                        fautes.append("aucune phrase traduite")
                    fautes += ["erreur JS : " + x for x in erreurs[:3]]
                    defauts += len(fautes)
                    part = (" ; donnee vue %d / %d" % (len(attendus & vues), len(attendus))) if attendus else ""
                    print("  %-10s %s  %4d phrases traduites vues%s, %d gestes%s  %s"
                          % (th, lg, len(vues), part, e["gestes"], " (PLAFOND ATTEINT)" if e["gestes"] >= PLAFOND else "",
                             "DEFAUTS : %d" % len(fautes) if fautes else "ok"), flush=True)
                    for f in fautes[:8]:
                        print("      " + f)
                    exemples[(th, lg)] = sorted(vues)
                    page.close()
            try:
                nav.close()
            except Exception:
                pass
    finally:
        srv.shutdown()
    if os.environ.get("LANGUES_EXEMPLES"):
        sortie = os.environ["LANGUES_EXEMPLES"]
        io.open(sortie, "w", encoding="utf-8", newline="\n").write(json.dumps(
            {"%s/%s" % k: v for k, v in exemples.items()}, ensure_ascii=False, indent=1) + "\n")
        print("  -> %s" % sortie)
    return 1 if defauts else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("extraire", "verifier"):
        sys.exit(__doc__)
    if a[0] == "extraire":
        extraire([x for x in a[1:] if x in THEMES])
    else:
        th = [x for x in a[1:] if x in THEMES]
        if not th:
            sys.exit("verifier <theme...> [lg...] : au moins un theme")
        sys.exit(verifier(th, [x for x in a[1:] if x in LANGUES] or BRANCHEES))
