# -*- coding: utf-8 -*-
"""Des questions reelles d'un theme illustre, pour les RELIRE : l'enonce, puis le retour apres une reponse touchee au
hasard (la phrase juste, sa traduction, le mot et son sens), N par sorte, et la decouverte. Aucune ecriture.

    python visuel/echantillon_theme.py contrarios "pt" 4
    python visuel/echantillon_theme.py contrarios "pt&variante=br" 4

Ouvre un navigateur : sous le verrou du navigateur (~/.wortando/REGLE-VERROU-PARCOURS.txt), port THEMES_PORT (8871).
"""
import functools, http.server, os, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TH, APP, N = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 4
PORT = int(os.environ.get("THEMES_PORT", "8871"))


class Muet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def handle(self):
        try: super().handle()
        except Exception: pass


socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Muet, directory=R))
srv.handle_error = lambda *a: None
threading.Thread(target=srv.serve_forever, daemon=True).start()
JS = """async (n) => {
  const out = [], txt = e => e ? e.innerText.replace(/\\s+/g, ' ').trim() : '';
  const dec = txt(document.getElementById('zone')).slice(0, 400);
  const mots = typeof motsDuTheme === 'function' ? motsDuTheme() : [];
  const liste = typeof SORTES !== 'undefined' ? SORTES : Object.keys(EX);
  for (const t of liste) {
    let fait = 0, essais = 0;
    while (fait < n && essais < 60) {
      essais++;
      const w = mots[Math.floor(Math.random() * mots.length)];
      try { repondu = false; for (const v of ['motQ','cleQ','tradQ','choixTexte','choixImage','fauxQ','vuQ','sensQ']) { try { eval(v + ' = null'); } catch (e) {} }
            sorteCourante = t; if (!EX[t](w)) continue; } catch (e) { out.push([t, 'ERREUR ' + e.message]); break; }
      const z = document.getElementById('zone');
      const enonce = txt(z.querySelector('.enonce')) || txt(z.querySelector('.consigne'));
      const c = Array.from(z.querySelectorAll('#choix button, .rangee button, .arbre g.p:not(.ego), .corps .zone, .plan .cible, #zone .choix button'));
      const opts = Array.from(z.querySelectorAll('#choix button')).map(b => b.textContent).join(' | ');
      if (c.length) c[Math.floor(Math.random() * c.length)].dispatchEvent(new MouseEvent('click', {bubbles: true}));
      out.push([t, (w && (w.mot || w.k)) + ' :: ' + enonce + (opts ? '  [' + opts + ']' : '') + '\\n        -> ' + txt(document.getElementById('msg'))]);
      fait++;
    }
  }
  return {dec, out, mots: mots.map(w => w.mot + (w.genre ? '(' + w.genre + ')' : '') + '/' + (w.cat || '')).join(', ')};
}"""
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    nav = p.chromium.launch(); page = nav.new_page(viewport={"width": 390, "height": 844}); err = []
    page.on("pageerror", lambda e: err.append(str(e).split("\n")[0][:160]))
    page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=%s&lang=fr" % (PORT, TH, APP))
    page.wait_for_function("() => typeof EX !== 'undefined' && (typeof D === 'undefined' || D)", timeout=20000)
    page.wait_for_timeout(800)
    r = page.evaluate(JS, N)
    print("== %s %s\nDECOUVERTE : %s\nMOTS : %s" % (TH, APP, r["dec"], r["mots"]))
    for t, s in r["out"]: print("  %-10s %s" % (t, s))
    print("ERREURS JS :", err or "aucune")
    try: nav.close()
    except Exception: pass
srv.shutdown()
