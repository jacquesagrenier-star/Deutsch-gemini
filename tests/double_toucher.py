# -*- coding: utf-8 -*-
"""Le deuxieme toucher ne compte rien (7 nov. 2026), de bout en bout dans la page.

    python tests/double_toucher.py              (allemand)
    python tests/double_toucher.py --app es     (ou en, pt)

Ne de la maquette des quatre points : en v1131, un deuxieme toucher sur ✓
pendant les 950 ms ou la carte reste a l'ecran la jugeait une seconde fois (un
mot a un point passait a trois) et ne faisait pas passer plus vite. Regle du
chef, d'apres Jacques (« rien ne doit ralentir quelqu'un qui sait ») : un seul
effet par carte ; le deuxieme toucher ne compte rien et passe tout de suite a
la carte suivante.

Chaque cas touche les boutons comme un doigt (la souris au centre du bouton,
sans attendre que l'animation se pose), deux fois, 300 ms d'ecart :
  1. ✓ puis ✓        : un seul point (1 -> 2), la carte suivante tout de suite ;
  2. ✓ puis Encore   : toujours 2 points, pas de remise a zero ;
  3. au 4e point, ✓ ✓ : maitrise une fois (un entretien, une revision) ;
  4. Mettre de cote deux fois : le mot reste mis de cote ;
  5. rappel actif, choix juste puis ✓ ✓ : un seul point ;
  6. un seul ✓ : la carte suivante arrive encore a l'heure (950 ms), rien n'a
     raccourci le passage de qui ne touche qu'une fois.
Il ne se connecte pas, il appelle les fonctions de la page. Il ouvre un
navigateur : a lancer SOUS LE VERROU des parcours
(~/.wortando/REGLE-VERROU-PARCOURS.txt).
"""
import argparse
import functools
import http.server
import os
import socketserver
import sys
import threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("PARCOURS_PORT", "8797"))

# Tous les mots A1 du premier theme de 10 mots ou plus, deja vus (hits points),
# dus maintenant ; le rappel actif force ou retire ; la bulle du premier
# « Continuer » deja vue (elle retient la carte, ce n'est pas le sujet ici).
PREPARER = r"""
([rappel, hits]) => {
  try { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); } catch(e) {}
  const orig = window.essaiActif;
  window.essaiActif = n => n === 'rappel_actif' ? rappel : orig(n);
  const th = themes.find(t => t.levels && t.levels.A1 && (t.levels.A1.words || []).length >= 10);
  const lv = th.levels.A1;
  lv.words.forEach((w, i) => setWordState(lv.id, i, {mastered: false, due: Date.now() - 60000,
      reviews: hits, srsHits: hits, srsDailyStreak: Math.max(0, hits - 1)}));
  startTheme(th.id, 'A1');
  return th.id;
}
"""
CARTE = r"""
() => {
  const it = currentCards[currentFlashcard];
  window.__it = it ? { k: it.themeId, i: it.index } : null;
  window.__rang = currentFlashcard;
  return !!it;
}
"""
ETAT = r"""
() => {
  const s = getWordState(window.__it.k, window.__it.i);
  return { hits: s.srsHits || 0, mastered: !!s.mastered, entretiens: s.entretiens || 0,
           reviews: s.reviews || 0, garde: !!s.garde, rang: currentFlashcard,
           avance: currentFlashcard !== window.__rang,
           rappel: !document.getElementById('rappelActif').classList.contains('hidden') };
}
"""
# Combien de ms apres ce moment la carte change-t-elle ?
ATTENDRE_PASSAGE = r"""
async () => {
  const r0 = window.__rang, t0 = performance.now();
  while (currentFlashcard === r0 && performance.now() - t0 < 4000) await new Promise(r => setTimeout(r, 10));
  return Math.round(performance.now() - t0);
}
"""


def serveur():
    gestion = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    gestion.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="de", choices=["de", "es", "en", "pt"])
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    chemin = "index.html" + ("" if a.app == "de" else "?apprendre=" + a.app)
    srv = serveur()
    fautes = []

    def attendu(nom, vrai, detail=""):
        print("  %-66s %s%s" % (nom, "ok" if vrai else "FAUX", "" if vrai or not detail else "  (" + detail + ")"))
        if not vrai:
            fautes.append(nom)

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()

            def ouvrir(rappel, hits):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 375, "height": 812}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.goto("http://127.0.0.1:%d/%s" % (PORT, chemin))
                page.wait_for_function("() => typeof startTheme === 'function' && typeof themes !== 'undefined' && themes.length > 0",
                                       timeout=60000)
                page.wait_for_timeout(1200)
                page.evaluate("() => goHome()")
                page.wait_for_timeout(600)
                page.evaluate(PREPARER, [rappel, hits])
                page.wait_for_timeout(1200)
                return ctx, page, erreurs

            def toucher(page, sel):
                """Un doigt : au centre du bouton, sans attendre qu'il soit « stable »."""
                b = page.evaluate("(s) => { const e = document.querySelector(s); if(!e || !e.offsetParent) return null;"
                                  " const r = e.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }", sel)
                if not b:
                    return False
                page.mouse.click(b[0], b[1])
                return True

            def verso(page):
                page.evaluate("() => { try{ flipCard(); }catch(e){} }")
                page.wait_for_timeout(700)
                page.evaluate(CARTE)

            BON, ENCORE, GARDE = "#flashcardActions .judge-good", "#flashcardActions .judge-again", "#gardeBtn"

            print("\n[%s] 1. ✓ puis ✓" % a.app)
            ctx, page, err = ouvrir(False, 1)
            verso(page)
            toucher(page, BON)
            page.wait_for_timeout(300)
            e1 = page.evaluate(ETAT)
            attendu("apres le 1er ✓ : 2 points, la carte encore la", e1["hits"] == 2 and not e1["avance"], str(e1))
            attendu("le 2e toucher trouve le bouton", toucher(page, BON))
            ms = page.evaluate(ATTENDRE_PASSAGE)
            e2 = page.evaluate(ETAT)
            attendu("apres le 2e ✓ : toujours 2 points", e2["hits"] == 2, str(e2))
            attendu("la carte suivante tout de suite (%d ms)" % ms, ms < 200)
            attendu("aucune erreur JavaScript", not err, "; ".join(err[:2]))
            ctx.close()

            print("\n[%s] 2. ✓ puis Encore" % a.app)
            ctx, page, err = ouvrir(False, 1)
            verso(page)
            toucher(page, BON)
            page.wait_for_timeout(300)
            toucher(page, ENCORE)
            ms = page.evaluate(ATTENDRE_PASSAGE)
            e = page.evaluate(ETAT)
            attendu("toujours 2 points, pas de remise a zero", e["hits"] == 2, str(e))
            attendu("la carte suivante tout de suite (%d ms)" % ms, ms < 200)
            attendu("aucune erreur JavaScript", not err, "; ".join(err[:2]))
            ctx.close()

            print("\n[%s] 3. le 4e point, ✓ ✓" % a.app)
            ctx, page, err = ouvrir(False, 3)
            verso(page)
            avant = page.evaluate(ETAT)
            toucher(page, BON)
            page.wait_for_timeout(300)
            toucher(page, BON)
            ms = page.evaluate(ATTENDRE_PASSAGE)
            e = page.evaluate(ETAT)
            attendu("maitrise", e["mastered"], str(e))
            attendu("un seul entretien (%d)" % e["entretiens"], e["entretiens"] == 1)
            attendu("une seule revision de plus (%d -> %d)" % (avant["reviews"], e["reviews"]), e["reviews"] == avant["reviews"] + 1)
            attendu("la carte suivante tout de suite (%d ms)" % ms, ms < 200)
            attendu("aucune erreur JavaScript", not err, "; ".join(err[:2]))
            ctx.close()

            print("\n[%s] 4. Mettre de cote deux fois" % a.app)
            ctx, page, err = ouvrir(False, 1)
            verso(page)
            if toucher(page, GARDE):
                page.wait_for_timeout(300)
                toucher(page, GARDE)
                ms = page.evaluate(ATTENDRE_PASSAGE)
                e = page.evaluate(ETAT)
                attendu("le mot reste mis de cote", e["garde"], str(e))
                attendu("les points n'ont pas bouge (%d)" % e["hits"], e["hits"] == 1)
                attendu("la carte suivante tout de suite (%d ms)" % ms, ms < 200)
            else:
                attendu("le bouton Mettre de cote est a l'ecran", False)
            attendu("aucune erreur JavaScript", not err, "; ".join(err[:2]))
            ctx.close()

            print("\n[%s] 5. rappel actif : choix juste, puis ✓ ✓" % a.app)
            ctx, page, err = ouvrir(True, 1)
            page.evaluate(CARTE)
            r = page.evaluate(ETAT)
            attendu("le rappel actif est a l'ecran", r["rappel"], str(r))
            if r["rappel"]:
                toucher(page, "#rappelActif .ra-choix button[data-juste]")
                page.wait_for_timeout(700)
                toucher(page, BON)
                page.wait_for_timeout(300)
                toucher(page, BON)
                ms = page.evaluate(ATTENDRE_PASSAGE)
                e = page.evaluate(ETAT)
                attendu("un seul point (1 -> %d)" % e["hits"], e["hits"] == 2)
                attendu("la carte suivante tout de suite (%d ms)" % ms, ms < 200)
            attendu("aucune erreur JavaScript", not err, "; ".join(err[:2]))
            ctx.close()

            print("\n[%s] 6. un seul ✓ : le passage garde sa duree" % a.app)
            ctx, page, err = ouvrir(False, 1)
            verso(page)
            toucher(page, BON)
            ms = page.evaluate(ATTENDRE_PASSAGE)
            e = page.evaluate(ETAT)
            attendu("2 points", e["hits"] == 2, str(e))
            attendu("la carte suivante vers 950 ms (%d ms)" % ms, 850 <= ms <= 1300)
            attendu("aucune erreur JavaScript", not err, "; ".join(err[:2]))
            ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("\n%s" % ("TOUT EST BON" if not fautes else "%d FAUTE(S)" % len(fautes)))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
