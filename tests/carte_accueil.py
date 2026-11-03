# -*- coding: utf-8 -*-
"""La carte du monde de l'accueil ne doit pas boucler juste apres le depart.

    python tests/carte_accueil.py              # de et es, 12 s d'accueil chacun
    CARTE_PORT=8794 python tests/carte_accueil.py

Ne le 3 nov. 2026 (Jacques, iPhone) : « Lorsque j'ouvre l'application allemande, on voit la map se deplacer vers la
gauche. Mais apres 5 ou 6 secondes, il y a un petit flash comme si l'image se retourne. [...] seulement avec
l'allemand. » Le defilement part du pays de la langue apprise (poserPaysCarte, un delai negatif) ; pour l'allemand,
ce point tombait a la fin de la boucle, qui recommencait 4,4 s apres l'arrivee sur l'accueil (en espagnol 11 s). Le
saut de 960 px ne se voit pas sur l'ordinateur, la carte se repetant, mais l'iPhone redessine alors la couche.
Ce controle releve la position REELLE de la piste toutes les 250 ms pendant 12 s apres goHome(), au format du
telephone, et sort en erreur au moindre saut. Demande Playwright, comme fusion-espagnol/parcours.py.
"""
import functools, http.server, os, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("CARTE_PORT", "8794"))
MESURE = """() => { const p = document.querySelector('#fondMonde .fm-piste');
  const m = p ? getComputedStyle(p).transform : 'none';
  return {x: m && m !== 'none' ? parseFloat(m.split(',')[4]) : null, delai: p ? p.style.animationDelay : ''}; }"""


def main():
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Muet, directory=RACINE))
    srv.handle_error = lambda *a: None      # le navigateur qui ferme une connexion n'est pas une faute
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    echec = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for nom, q in (("de", ""), ("es", "?apprendre=es")):
            ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
            page = ctx.new_page()
            page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, q), wait_until="domcontentloaded", timeout=90000)
            try:
                page.wait_for_load_state("networkidle", timeout=30000)
            except Exception:
                pass
            page.evaluate("() => { if('VUE_CONTENU' in window) VUE_CONTENU = false; goHome(); }")
            xs = []
            for k in range(49):
                xs.append(page.evaluate(MESURE))
                page.wait_for_timeout(250)
            ctx.close()
            v = [m["x"] for m in xs if m["x"] is not None]
            sauts = [(k, a, b) for k, (a, b) in enumerate(zip(v, v[1:])) if abs(b - a) > 20]
            immobile = len(v) > 1 and abs(v[-1] - v[0]) < 5
            print("  %s : depart %.0f px, apres 12 s %.0f px, delai %s, %d saut(s)%s" % (
                nom, v[0] if v else 0, v[-1] if v else 0, xs[0]["delai"], len(sauts), " -- la carte ne bouge pas" if immobile else ""))
            if sauts: echec.append("%s : la piste saute de %.0f a %.0f px apres %.2f s" % (nom, sauts[0][1], sauts[0][2], (sauts[0][0] + 1) * 0.25))
            if immobile or not v: echec.append("%s : la carte ne defile pas sur l'accueil" % nom)
        nav.close()
    srv.shutdown()
    if echec:
        print("\nECHEC :\n  " + "\n  ".join(echec))
        sys.exit(1)
    print("\nOK : la carte defile sans boucler pendant les 12 premieres secondes de l'accueil, en allemand et en espagnol.")


if __name__ == "__main__":
    main()
