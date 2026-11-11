# -*- coding: utf-8 -*-
"""Le controle des themes illustres (visuel/prototype/<theme>.html), en espagnol et en allemand.

    python tests/themes_illustres.py                 # tous les themes, 3000 tirages par sorte
    python tests/themes_illustres.py familia 500     # un theme, moins de tirages
    python tests/themes_illustres.py --coherence     # la coherence des personnes seule, sans navigateur

Pour chaque theme et chaque langue apprise, il mesure :
  - les questions DIFFERENTES que chaque sorte produit (enonce + bonne reponse ; pour « qui est le plus grand », le
    trio compare fait partie de la question). Jacques, 3 nov. 2026 : « J'irais une centaine de questions par
    theme » -- c'est ce chiffre-la, la reserve, pas la longueur d'une partie (20, et 6 dans la seance) ;
  - les erreurs JavaScript, les doublons de choix, et sur 200 series entieres : une question deux fois dans la
    meme serie, ou deux fois la meme sorte de suite.
Sort en erreur si un theme a moins de 100 questions differentes dans une langue, ou un defaut quelconque.
Demande Playwright (pip install playwright ; python -m playwright install chromium), comme fusion-espagnol/parcours.py.
"""
import functools, http.server, json, os, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 8798 par defaut ; THEMES_PORT=<n> quand une autre session en lance en meme temps (3 nov. 2026 : avec
# allow_reuse_address, deux serveurs sur le meme port se lisent l'un l'autre sous Windows -- vecu).
PORT = int(os.environ.get("THEMES_PORT", "8798"))
THEMES = ["familia", "descripcion", "emociones", "contrarios", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "transportes", "loisirs", "animales", "meteo", "logement", "demarches", "courses", "vacances", "travail", "ecole", "ciudad", "fetes"]          # un theme qui s'ajoute s'ajoute ici et dans THEMES_ILLUSTRES (index.html)
# L'ANGLAIS (3 nov. 2026) : les themes qui ont deja leurs phrases anglaises, a mesure qu'ils les recoivent ; et le
# britannique, la variante (« en&variante=gb »)
ANGLAIS = ["familia", "descripcion", "contrarios", "emociones", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "loisirs", "animales", "meteo", "logement", "demarches"]
PLANCHER = 100

COMPTER = """(n) => {
  const sortes = SORTES, res = {}, total = new Set(), defauts = [];
  for (const t of Object.keys(EX).filter(x => sortes.includes(x))) {
    const vus = new Set();
    for (let i = 0; i < n; i++) {
      try {
        repondu = false; EX[t]();
        const z = document.getElementById('zone'), en = z.querySelector('.enonce');
        const choix = Array.from(z.querySelectorAll('#choix button')).map(b => b.textContent);
        if (new Set(choix).size !== choix.length) defauts.push(t + ' : choix en double ' + choix.join(' / '));
        const imgs = t === 'taille' ? Array.from(z.querySelectorAll('img')).map(x => x.getAttribute('src')).sort().join(',') : '';
        let rep = '';
        const b = z.querySelector('#choix button');
        if (b) { b.click(); const j = z.querySelector('#choix button.juste'); rep = j ? j.textContent : ''; }
        else if (typeof testerOrdre === 'function' && z.querySelector('.ordre')) rep = testerOrdre();   // la journee : remettre dans l'ordre, en quatre gestes
        else {
          // .plan .cible : les ronds a toucher sur le plan d'« En ville »
          const g = z.querySelector('.arbre g.p:not(.ego)') || z.querySelector('.rangee button') || z.querySelector('.corps .zone') || z.querySelector('.plan .cible');
          if (g) g.dispatchEvent(new MouseEvent('click', {bubbles: true}));
          const j = z.querySelector('.arbre g.juste, .rangee button.juste, .corps .zone.juste, .plan .cible.juste'); rep = j ? j.dataset.id : '';
        }
        if (!rep) defauts.push(t + ' : pas de bonne reponse marquee');
        const k = t + '|' + (en ? en.textContent : '') + '|' + imgs + '|' + rep;
        vus.add(k); total.add(k);
      } catch (e) { defauts.push(t + ' : ' + e.message); }
    }
    res[t] = vus.size;
  }
  res.TOTAL = total.size;
  return {res, defauts: defauts.slice(0, 8), nbDefauts: defauts.length};
}"""
# une partie suit les mots (tirage.js) : la page seule n'a pas d'etats, tous ses mots sont neufs ; on verifie que chaque
# question vise le mot de la file, qu'aucune ne revient dans la partie et que deux sortes ne se suivent jamais
SERIES = """async () => {
  let doubles = 0, suites = 0, rates = 0, erreurs = [], longueur = 0;
  for (let s = 0; s < 120; s++) {
    await demarrer(); const cles = new Set(); let avant = null;
    for (let r = 0; r < file.length; r++) {
      if (r) { rang = r; try { montrer(); } catch (e) { erreurs.push(e.message); } }
      const k = cleQuestion(); if (cles.has(k)) doubles++; cles.add(k);
      if (avant && sorteCourante === avant) suites++; avant = sorteCourante;
      const w = file[r], q = motQ ? (Array.isArray(motQ) ? mot(motQ[0], motQ[1]) : motQ.mot) : null;
      if (q !== w.mot) rates++;
    }
    longueur = file.length;
  }
  return {NB: longueur, doubles, suites, rates, erreurs: erreurs.slice(0, 3)};
}"""


# ---------------------------------------------------------------------------------------------------------------
# LA COHERENCE DES PERSONNES (decision de Jacques du 6 nov. 2026 ; la fiche : visuel/personnes.json). Sans navigateur :
# elle lit la donnee des pages et les phrases fabriquees (les voix.json de chaque theme, que visuel/voix_themes.py
# releve en jouant les pages, et visuel/transportes/toutes-les-phrases.json).
#   python tests/themes_illustres.py --coherence      # elle seule, quelques secondes, hors du verrou du navigateur
# Elle verifie : un seul metier par personne (celui de la fiche) ; aucun trait de la liste noire sur une personne
# recurrente ; l'orthographe des prenoms (Inés, Tomás) ; jamais « zur Schule » pour un enfant de moins de 6 ans ; et
# aucune phrase contraire a une phrase en « nie » / « nunca » / « never » ou « immer » / « siempre » / « always ».
import re

def _textes():
    """{langue: set(phrases)} : tout ce que les themes disent ou ecrivent (une chaine avec une espace)."""
    out = {"de": set(), "es": set(), "en": set()}
    def poser(langue, o):
        if isinstance(o, str):
            if " " in o.strip():
                out[langue].add(o.strip())
        elif isinstance(o, dict):
            for v in o.values():
                poser(langue, v)
        elif isinstance(o, list):
            for v in o:
                poser(langue, v)
    LANG = {"de": "de", "es": "es", "latam": "es", "en": "en"}
    # Une phrase qui A DEJA SON FICHIER reste dans voix.json meme quand la page ne la dit plus (voix_themes.py, 7 nov. :
    # « une phrase deja payee ne sort jamais de la liste ») : « Javier ist geizig. » y reste apres la coherence. Ces
    # phrases-la ne sont donc pas jugees ici sur voix.json ; celles que la page dit encore le sont par sa donnee (plus bas)
    # et par les controles de structure de coherence() (metiers, medecins, serveurs, traits).
    DOSSIER = {"de": "de", "es": "es-es", "latam": "es-419", "en": "en-us"}
    f = os.path.join(RACINE, "visuel", "prototype", "themes", "sons.json")
    sons = {k: set(v) for k, v in json.load(open(f, encoding="utf-8")).items()} if os.path.exists(f) else {}
    import hashlib
    for th in sorted(os.listdir(os.path.join(RACINE, "visuel"))):
        f = os.path.join(RACINE, "visuel", th, "voix.json")
        if os.path.exists(f):
            for k, v in json.load(open(f, encoding="utf-8")).items():
                if k in LANG:
                    connus = sons.get(DOSSIER[k], set())
                    poser(LANG[k], [t for t in v if not (isinstance(t, str) and
                                    hashlib.sha1(t.encode("utf-8")).hexdigest()[:16] in connus)])
    f = os.path.join(RACINE, "visuel", "transportes", "toutes-les-phrases.json")
    if os.path.exists(f):
        for k, v in json.load(open(f, encoding="utf-8")).items():
            if k in LANG:
                poser(LANG[k], v)
    # les phrases de la donnee des pages, par langue apprise (cles « de », « es », « en » d'un dictionnaire)
    def descendre(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("de", "es", "en", "latam", "dei", "es_latam"):
                    poser({"dei": "de", "es_latam": "es"}.get(k, LANG.get(k, k)), v)
                else:
                    descendre(v)
        elif isinstance(o, list):
            for v in o:
                descendre(v)
    for th in THEMES:
        f = os.path.join(RACINE, "visuel", "prototype", th, th + ".json")
        if os.path.exists(f):
            descendre(json.load(open(f, encoding="utf-8")))
    return out


def coherence():
    sys.path.insert(0, os.path.join(RACINE, "visuel"))
    import personnes as PERS
    fautes = ["fiche : " + f for f in PERS.verifier()]
    textes = _textes()
    noms = {PERS.nom(k): k for k in list(PERS.RECURRENTS) + list(PERS.RESERVES)}
    NOM = "(" + "|".join(sorted(map(re.escape, noms), key=len, reverse=True)) + ")"

    # 1. LA DONNEE : le metier des pages contre la fiche
    def lire(th):
        return json.load(open(os.path.join(RACINE, "visuel", "prototype", th, th + ".json"), encoding="utf-8"))
    met = lire("metiers")
    for pid, p in met["personnes"].items():
        if p.get("nom"):
            if PERS.metier(pid) != p["metier"]:
                fautes.append("metiers : %s est %s, %s dans la fiche" % (p["nom"], p["metier"], PERS.metier(pid)))
            if p["nom"] != PERS.nom(pid):
                fautes.append("metiers : « %s » au lieu de « %s »" % (p["nom"], PERS.nom(pid)))
    for s, p in lire("cuerpo")["medicos"].items():
        if PERS.metier(p) != "arzt":
            fautes.append("cuerpo : le medecin %s n'est pas medecin dans la fiche (%s)" % (p, PERS.metier(p)))
    man = lire("manger")
    for p, r in man["roles"].items():
        role = (r.get("de") or {}).get("mot", "")
        if role.startswith("Kellner") and p not in man.get("anonymes", {}) and PERS.metier(p) != "kellner":
            fautes.append("manger : %s est %s au cafe, %s dans la fiche" % (p, role, PERS.metier(p)))
    emo = lire("emociones")
    for t, gens in emo["traits"].items():
        for p in gens:
            if t in PERS.TRAITS_INTERDITS and PERS.recurrent(p):
                fautes.append("emociones : %s (personne recurrente) porte le trait %s" % (PERS.nom(p), t))

    # 2. LES PHRASES : un metier par personne. Les mots des metiers (de, es, en), pris dans metiers.json
    mots = {"de": {}, "es": {}, "en": {}}
    for mid, m in met["metiers"].items():
        for s in "mf":
            mots["de"][m["de"][s]["mot"]] = mid
            mots["es"][m["es"][s]["mot"]] = mid
        for x in m["trad"]["en"]:
            mots["en"][x] = mid
    for mot_, mid in (("Kellner", "kellner"), ("Kellnerin", "kellner"), ("camarero", "kellner"), ("camarera", "kellner"),
                      ("mesero", "kellner"), ("mesera", "kellner"), ("waiter", "kellner"), ("waitress", "kellner")):
        mots["de" if mot_[0].isupper() else ("en" if mot_.startswith("wait") else "es")][mot_] = mid
    def alt(d):
        return "(" + "|".join(sorted(map(re.escape, d), key=len, reverse=True)) + ")"
    MOTIFS = {
        "de": [NOM + r" (?:ist|arbeitet als) (?:der |die |ein |eine )?(?:gute[rn]? |neue[rn]? )?" + alt(mots["de"]) + r"\b",
               NOM + r" arbeitet [^.]*\. (?:Er|Sie) ist (?:ein |eine )?" + alt(mots["de"]) + r"\b"],
        "es": [NOM + r" (?:es|trabaja de) (?:el |la |un |una )?(?:buen |buena )?" + alt(mots["es"]) + r"\b",
               NOM + r" trabaja [^.]*\. Es (?:el |la |un |una )?" + alt(mots["es"]) + r"\b"],
        "en": [NOM + r" (?:is|works as) (?:a |an |the )?(?:good )?" + alt(mots["en"]) + r"\b",
               NOM + r" works [^.]*\. (?:He|She) is (?:a |an |the )?" + alt(mots["en"]) + r"\b"]}
    vus = {}
    for langue, motifs in MOTIFS.items():
        for t in textes[langue]:
            for mo in motifs:
                for m in re.finditer(mo, t):
                    vus.setdefault(noms[m.group(1)], {}).setdefault(mots[langue][m.group(2)], t)
    for k, ms in sorted(vus.items()):
        attendu = PERS.metier(k)
        for mid, t in ms.items():
            if mid != attendu:
                fautes.append("metier : %s est %s dans « %s » (fiche : %s)" % (PERS.nom(k), mid, t, attendu or "aucun metier"))

    # 3. LA LISTE NOIRE sur les recurrents (« Diego ist arm. », « Hugo ist arm. Tomás ist das Gegenteil: Er ist reich. »)
    MOTIFS = {"de": [NOM + r" ist (?:sehr |ein bisschen |oft )?" + alt(PERS.MOTS_INTERDITS["de"]) + r"\b",
                     NOM + r" ist das Gegenteil: (?:Er|Sie) ist " + alt(PERS.MOTS_INTERDITS["de"]) + r"\b"],
              "es": [NOM + r" es (?:muy |un poco )?" + alt(PERS.MOTS_INTERDITS["es"]) + r"\b",
                     NOM + r", al contrario, es " + alt(PERS.MOTS_INTERDITS["es"]) + r"\b"],
              "en": [NOM + r" is (?:very |a bit )?" + alt(PERS.MOTS_INTERDITS["en"]) + r"\b",
                     NOM + r" is the opposite: (?:he|she) is " + alt(PERS.MOTS_INTERDITS["en"]) + r"\b"]}
    for langue, motifs in MOTIFS.items():
        for t in sorted(textes[langue]):
            for mo in motifs:
                for m in re.finditer(mo, t):
                    if PERS.recurrent(noms[m.group(1)]):
                        fautes.append("liste noire : « %s » (%s est une personne recurrente)" % (t, m.group(1)))

    # 4. L'ORTHOGRAPHE des prenoms : « Ines », « Tomas » sans accent
    for k, n in PERS.noms().items():
        for langue, ts in textes.items():
            for t in sorted(ts):
                if re.search(r"\b" + re.escape(k) + r"\b", t):
                    fautes.append("orthographe : « %s » dans « %s » (%s)" % (k, t, n))

    # 5. L'AGE COMMANDE LE LIEU : avant 6 ans la Kita, jamais l'ecole
    petits = [PERS.nom(k) for k in PERS.RECURRENTS if PERS.lieu_enfant(k) == "kita"]
    P = "(?:" + "|".join(map(re.escape, petits)) + ")"
    MOTIFS = {"de": [r"\b" + P + r"\b(?: \w+){0,2} (?:zur Schule|in die Schule|in der Schule|von der Schule)", r"\bdie Kinder\b(?: \w+){0,2} zur Schule"],
              "es": [r"\b(?:a )?" + P + r"\b(?: \w+){0,2} (?:al colegio|a la escuela|en el colegio|en la escuela)", r"\ba los niños al colegio\b", r"\ba los niños a la escuela\b"],
              "en": [r"\b" + P + r"\b(?: \w+){0,2} (?:to school|at school|from school)", r"\bthe children to school\b"]}
    for langue, motifs in MOTIFS.items():
        for t in sorted(textes[langue]):
            if any(re.search(mo, t) for mo in motifs):
                fautes.append("age : « %s » (%s va a la Kita)" % (t, " / ".join(petits)))

    # 6. « NIE » ET « IMMER » : la phrase contraire ne se dit nulle part (« Anna fährt nie mit dem Auto zur Arbeit. »
    # contre « Anna fährt mit dem Auto zur Arbeit. », que Les transports fabriquaient)
    jr = lire("journee")
    adv = jr.get("adverbes", {})
    regles = {"de": [], "es": []}
    for f in jr.get("frequences", []):
        for langue in ("de", "es"):
            gabarit = f.get(langue)
            if not gabarit or "{A}" not in gabarit or f["f"] not in ("nunca", "siempre"):
                continue
            nie = gabarit.replace("{A}", adv["nunca"][langue])
            sans = re.sub(r"\s+", " ", gabarit.replace("{A}", "")).replace(" .", ".")
            if f["f"] == "nunca":
                regles[langue].append((nie, sans))
            else:
                regles[langue].append((gabarit.replace("{A}", adv["siempre"][langue]), nie))
    for langue, rs in regles.items():
        for vrai, contraire in rs:
            if contraire in textes[langue]:
                fautes.append("nie / immer : « %s » contredit « %s »" % (contraire, vrai))
    return fautes


def main():
    # la coherence des personnes d'abord (sans navigateur) ; --coherence : elle seule
    fautes = coherence()
    print("coherence des personnes (visuel/personnes.json) : " + ("%d faute(s)" % len(fautes) if fautes else "aucune faute"))
    for f in fautes:
        print("  " + f)
    if "--coherence" in sys.argv:
        sys.exit(1 if fautes else 0)
    themes = [a for a in sys.argv[1:] if not a.isdigit() and not a.startswith("--")] or THEMES
    tirages = int(next((a for a in sys.argv[1:] if a.isdigit()), 3000))
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    g = functools.partial(Muet, directory=RACINE)
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), g)
    srv.handle_error = lambda *a: None      # le navigateur qui ferme une connexion n'est pas une faute
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    echec = ["coherence : " + f for f in fautes]
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for th in themes:
            # THEMES_APPS=en,en&variante=gb : seulement ces langues (une page qu'on met en anglais, avant d'etre dans ANGLAIS)
            apps = tuple(os.environ["THEMES_APPS"].split(",")) if os.environ.get("THEMES_APPS") else ("es", "de") + (("en", "en&variante=gb") if th in ANGLAIS else ())
            for app in apps:
                for seance in ("", "&seance=1"):
                    ctx = nav.new_context(viewport={"width": 390, "height": 844})
                    page = ctx.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                    page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&lang=fr%s" % (PORT, th, app, seance))
                    page.wait_for_timeout(1500)
                    s = page.evaluate(SERIES)
                    ligne = "%-12s %s %-8s partie de %2d : %d doublon(s), %d sorte(s) de suite, %d question(s) a cote du mot" % (th, app, "seance" if seance else "seul", s["NB"], s["doubles"], s["suites"], s["rates"])
                    if not seance:
                        c = page.evaluate(COMPTER, tirages)
                        ligne += " ; %d questions differentes %s" % (c["res"]["TOTAL"], json.dumps({k: v for k, v in c["res"].items() if k != "TOTAL"}, ensure_ascii=False))
                        if c["res"]["TOTAL"] < PLANCHER: echec.append("%s %s : %d questions differentes (< %d)" % (th, app, c["res"]["TOTAL"], PLANCHER))
                        if c["nbDefauts"]: echec.append("%s %s : %d defaut(s), dont %s" % (th, app, c["nbDefauts"], c["defauts"]))
                    if s["doubles"] or s["suites"] or s["rates"] or s["erreurs"]: echec.append("%s %s%s : %s" % (th, app, seance, s))
                    if erreurs: echec.append("%s %s : erreurs JavaScript %s" % (th, app, erreurs[:3]))
                    print(ligne)
                    ctx.close()
        try:
            nav.close()
        except Exception:
            pass                                  # un navigateur qui ferme mal (11 nov. 2026) ne cache plus le verdict
    srv.shutdown()
    if echec:
        print("\nECHEC :\n  " + "\n  ".join(echec))
        sys.exit(1)
    print("\nOK : chaque theme a au moins %d questions differentes par langue, aucune serie fautive." % PLANCHER)


if __name__ == "__main__":
    main()
