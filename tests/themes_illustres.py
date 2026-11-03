# -*- coding: utf-8 -*-
"""Le controle des themes illustres (visuel/prototype/<theme>.html), en espagnol et en allemand.

    python tests/themes_illustres.py                 # tous les themes, 3000 tirages par sorte
    python tests/themes_illustres.py familia 500     # un theme, moins de tirages

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
THEMES = ["familia", "descripcion", "emociones", "contrarios", "gato", "ropa", "cuerpo", "journee", "manger", "metiers", "transportes"]          # un theme qui s'ajoute s'ajoute ici et dans THEMES_ILLUSTRES (index.html)
# L'ANGLAIS (3 nov. 2026) : les themes qui ont deja leurs phrases anglaises, a mesure qu'ils les recoivent ; et le
# britannique, la variante (« en&variante=gb »)
ANGLAIS = ["familia", "descripcion", "contrarios"]
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
          const g = z.querySelector('.arbre g.p:not(.ego)') || z.querySelector('.rangee button') || z.querySelector('.corps .zone');
          if (g) g.dispatchEvent(new MouseEvent('click', {bubbles: true}));
          const j = z.querySelector('.arbre g.juste, .rangee button.juste, .corps .zone.juste'); rep = j ? j.dataset.id : '';
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


def main():
    themes = [a for a in sys.argv[1:] if not a.isdigit()] or THEMES
    tirages = int(next((a for a in sys.argv[1:] if a.isdigit()), 3000))
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    g = functools.partial(Muet, directory=RACINE)
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), g)
    srv.handle_error = lambda *a: None      # le navigateur qui ferme une connexion n'est pas une faute
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    echec = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for th in themes:
            for app in ("es", "de") + (("en", "en&variante=gb") if th in ANGLAIS else ()):
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
        nav.close()
    srv.shutdown()
    if echec:
        print("\nECHEC :\n  " + "\n  ".join(echec))
        sys.exit(1)
    print("\nOK : chaque theme a au moins %d questions differentes par langue, aucune serie fautive." % PLANCHER)


if __name__ == "__main__":
    main()
