# -*- coding: utf-8 -*-
"""LES PHRASES TRADUITES DES THEMES ILLUSTRES DANS TOUTES LES LANGUES D'INTERFACE -- l'outillage (lot 0 de l'alignement
des langues, 13 nov. 2026 ; plan : side-session-notes du chef, alignement-themes-langues-plan.md).

LE CONSTAT. Une page de theme (visuel/prototype/<theme>.html) montre la PHRASE traduite en francais, anglais,
portugais (et allemand pour qui apprend l'espagnol) : la page la fabrique avec son propre code, morceau par morceau.
En turc, ukrainien, persan, arabe, polonais et russe, elle ne montre que la glose du mot (gloses.json), jamais la
phrase. L'arabe manque aussi a qui apprend l'espagnol.

LA METHODE (celle du telc, visuel/prototype/telc/outils/langues.js, eprouvee le 7 nov.). Un DICTIONNAIRE par langue,
commun aux 22 themes : visuel/prototype/themes/langues/<lg>.json = { "phrase francaise affichee": "traduction" }.
Le francais sert de pivot : toutes les pages le fabriquent, et il porte le genre et le nombre que le turc, l'arabe,
le russe, le polonais et l'ukrainien demandent (« Anna se leve », « ils / elles »). Une page ouverte a une langue
fabriquera la phrase en francais puis la cherchera dans le dictionnaire (branchement : lots suivants) ; sans entree,
la glose du mot, comme aujourd'hui -- jamais de francais affiche a la place.

LE FRANCAIS NE PORTE PAS TOUJOURS LE CAS (releve de gato, 14 nov.) : « sur la table » traduit aussi bien « auf dem
Tisch » (Wo?) que « auf den Tisch » (Wohin?) -- en ukrainien « на столі » / « на стіл », en russe « на столе » /
« на стол », en polonais « na stole » / « na stół » ; et pour l'espagnol, « a la mesa » / « sobre la mesa » donnent en
arabe « إلى » / « على ». Une phrase francaise qui vient de PLUSIEURS sources (dans un meme theme et une meme langue
apprise) est AMBIGUE : son entree est un objet { "source dans la langue apprise": "traduction" }, une par source
(la page connait sa source : elle l'ecrit juste avant la traduction) ; les autres restent une simple chaine.

    python visuel/langues_themes.py extraire [theme...]   # joue les pages en francais (navigateur, VERROU des parcours)
                                                          #   -> themes/langues/source.json
    python visuel/langues_themes.py controler [lg...]     # ce qui manque, theme par theme et langue par langue
                                                          #   (sans navigateur ; code de sortie 1 s'il manque)
    python visuel/langues_themes.py construire <lg>       # themes/langues/<lg>.js (window.TRAD_THEMES) depuis <lg>.json

L'EXTRACTION. Chaque page est ouverte avec lang=fr, en allemand puis en espagnol appris. On parcourt la decouverte
(decouvrir() puis chaque bouton, sur deux niveaux : onglets puis elements), puis chaque SORTE de question (EX) pour
chaque mot du theme (motsDuTheme()), comme visuel/voix_themes.py, avec une reponse touchee au hasard (juste ou
fausse : les deux montrent une traduction, la phrase juste et le choix faux). Apres chaque geste, on releve le texte
de chaque .trad de la page : la phrase traduite, et dans un .trad.faux ce qui suit le dernier « — » (le sens du choix
faux). La source (la phrase de la langue apprise a cote, [lang=de|es]) est notee pour les traducteurs.
Les GLOSES (un mot et sa traduction du corpus) ne vont pas au dictionnaire : la page les donne deja dans chaque
langue. Est une glose un texte dont la traduction (apres le dernier « — », ou le texte entier) est une valeur
francaise des gloses du theme (D.gloses, gloses.json, GLOSES).
`tard` : les textes neufs des 20 % derniers tirages d'une sorte ; 0 = la sorte est epuisee. Un theme dont une sorte
n'est pas epuisee se relance avec plus de tirages (LANGUES_TIRAGES, 2000 par defaut).

Langues d'interface : allemand appris -> tr, uk, fa, ar, pl, ru par le dictionnaire (fr, en, pt : la page) ;
espagnol appris -> ar (fr, en, pt, de : la page). Port : LANGUES_PORT (8858 par defaut, jamais 8791).
"""
import functools, http.server, io, json, os, re, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
DOSSIER = os.path.join(ICI, "prototype", "themes", "langues")
SOURCE = os.path.join(DOSSIER, "source.json")
PORT = int(os.environ.get("LANGUES_PORT", "8858"))
TIRAGES = int(os.environ.get("LANGUES_TIRAGES", "2000"))
THEMES = ["familia", "descripcion", "emociones", "contrarios", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "transportes",
          "loisirs", "animales", "meteo", "logement", "demarches", "courses", "vacances", "travail", "ecole", "ciudad", "fetes"]
# la langue apprise -> les langues d'interface que le DICTIONNAIRE doit couvrir (les autres, la page les fabrique)
BESOIN = {"de": ["tr", "uk", "fa", "ar", "pl", "ru"], "es": ["ar"]}
LANGUES = ["tr", "uk", "fa", "ar", "pl", "ru"]

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

ENUMERER = r"""async ([n, relever]) => {
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
    for (let i = 0; i < n1 && gestes < 600; i++) {
      try { await decouvrir(); const b1 = boutons()[i]; if (!b1) continue; b1.click(); gestes++; await pause(0); noter();
            const n2 = boutons().length;
            for (let j = 0; j < n2 && gestes < 600; j++) {
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
                    e = page.evaluate(ENUMERER, [TIRAGES, RELEVER])
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
                          "%d gestes, %d gloses ecartees ; sortes non epuisees : %s%s"
                          % (th, app, len(srcs), len(phrases), ambigus, e["decouverte"], e["gestes"], gloses, ouvertes or "aucune",
                             ("  ERREURS JS : " + " | ".join(erreurs[:3])) if erreurs else ""), flush=True)
                    page.close()
            try:
                nav.close()
            except Exception:
                pass
    finally:
        srv.shutdown()
    os.makedirs(DOSSIER, exist_ok=True)
    io.open(SOURCE, "w", encoding="utf-8", newline="\n").write(json.dumps(source, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print("  -> %s" % os.path.relpath(SOURCE, RACINE))


def mots(s):
    return len(re.findall(r"\w+", s, re.U))


def dico(lg):
    f = os.path.join(DOSSIER, lg + ".json")
    return json.load(io.open(f, encoding="utf-8")) if os.path.exists(f) else {}


def controler(langues):
    if not os.path.exists(SOURCE):
        print("pas de %s : lancer d'abord « extraire »" % os.path.relpath(SOURCE, RACINE))
        return 2
    source = json.load(io.open(SOURCE, encoding="utf-8"))
    dicos = {lg: dico(lg) for lg in langues}
    manque_total, uniques, ambigus_total = 0, {lg: {} for lg in langues}, 0
    print("  %-12s %-3s %6s %6s %7s   %s" % ("theme", "app", "phr.", "ambig.", "mots fr", "  ".join("%-5s" % lg for lg in langues)))
    for th in THEMES:
        for app in ("de", "es"):
            l = source.get(th, {}).get(app)
            if l is None:
                continue
            srcs = {}
            for x in l:
                srcs.setdefault(x["fr"], set()).add(x.get("src", ""))
            ambigus = {fr for fr, v in srcs.items() if len(v) > 1}
            ambigus_total += len(ambigus)
            cols = []
            for lg in langues:
                if lg not in BESOIN[app]:
                    cols.append("  -  ")
                    continue
                m = []
                for x in l:
                    v = dicos[lg].get(x["fr"])
                    if x["fr"] in ambigus:
                        # une traduction par source ; une chaine seule ne suffit pas (elle ne dit pas le cas)
                        ok = isinstance(v, dict) and (v.get(x.get("src", "")) or "").strip()
                    else:
                        ok = isinstance(v, str) and v.strip() or isinstance(v, dict) and (v.get(x.get("src", "")) or "").strip()
                    if not ok:
                        m.append(x)
                for x in m:
                    uniques[lg][(x["fr"], x.get("src", "") if x["fr"] in ambigus else "")] = True
                manque_total += len(m)
                cols.append("%5d" % len(m))
            print("  %-12s %-3s %6d %6d %7d   %s" % (th, app, len(srcs), len(ambigus), sum(mots(fr) for fr in srcs), "  ".join(cols)))
    print("\n  entrees DISTINCTES a traduire (un texte commun a deux themes ne se traduit qu'une fois ; une phrase ambigue "
          "compte une fois par source) :")
    for lg in langues:
        print("    %s : %d entrees, %d mots" % (lg, len(uniques[lg]), sum(mots(fr) for fr, _ in uniques[lg])))
    print("  phrases francaises ambigues (plusieurs sources) : %d" % ambigus_total)
    defauts = 0
    for lg in langues:
        for k, v in dicos[lg].items():
            vals = list(v.values()) if isinstance(v, dict) else [v]
            if not vals or any(not isinstance(w, str) or (w.strip() and len(w.strip()) < 2 and len(k) > 3) for w in vals):
                print("  DEFAUT %s : « %s » -> %r" % (lg, k, v))
                defauts += 1
    return 1 if (manque_total or defauts) else 0


def construire(lg):
    d = dico(lg)
    sortie = os.path.join(DOSSIER, lg + ".js")
    io.open(sortie, "w", encoding="utf-8", newline="\n").write(
        "// %s : dictionnaire francais -> %s des phrases des themes illustres. DERIVE de themes/langues/%s.json par\n"
        "// python visuel/langues_themes.py construire %s -- ne pas corriger ici.\n"
        "window.TRAD_THEMES = %s;\n" % (lg, lg, lg, lg, json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))))
    print("  -> %s (%d phrases)" % (os.path.relpath(sortie, RACINE), len(d)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("extraire", "controler", "construire"):
        sys.exit(__doc__)
    if a[0] == "extraire":
        extraire([x for x in a[1:] if x in THEMES])
    elif a[0] == "controler":
        sys.exit(controler([x for x in a[1:] if x in LANGUES] or LANGUES))
    else:
        if len(a) < 2 or a[1] not in LANGUES:
            sys.exit("construire <lg> : une de " + ", ".join(LANGUES))
        construire(a[1])
