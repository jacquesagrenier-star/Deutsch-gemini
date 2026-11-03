# -*- coding: utf-8 -*-
"""Le palier de l'objectif du jour, franchi dans les cartes et dans un theme illustre : la fete montre-t-elle le tableau ?

    python tests/palier_themes.py          # THEMES_PORT=<n> pour un autre port que 8789

Jacques, 3 nov. 2026 (iPhone) : « il n'y a pas d'affichage de la mosaique, avec le cercle de progression »,
« dans un theme illustre ». Le palier y etait compte (exerciceDeScene) sans aucune fete. Ce controle franchit le
palier pour de bon, en allemand et en espagnol, objectif 10 puis 30, hors trophee puis pendant un trophee (le
tableau suivant se construit, `cn`) :
  - CARTES : scheduleReview(), le chemin d'une carte jugee ;
  - THEME : la page d'un theme ouverte dans le cadre (ouvrirThemeIllustre), une vraie reponse touchee dans la page ;
et verifie que .mos-palier contient une toile dessinee, au premier plan. Les SCENES gardent leur regle (pas de fete
par-dessus l'image) : on verifie seulement que rien ne parait. Un profil d'administrateur est simule (les essais
anneau_palier et carreau_partout), sans connexion : rien ne part chez Firebase.
Demande Playwright, comme fusion-espagnol/parcours.py.
"""
import functools, http.server, os, socketserver, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("THEMES_PORT", "8789"))

PREPARER = """async ([objectif, trophee]) => {
  isAdminUser = () => true;
  localStorage.setItem(DAILY_GOAL_STORAGE_KEY, String(objectif));
  await chargerMosaiques();
  // un tableau entame (40 carreaux) ; pendant un trophee, le tableau gagne en haut et le suivant (cn) en bas
  const v = etatMosaique();
  if (trophee) { v.c = MOSAIQUE_CARREAUX; v.t = 3; v.cn = 40; } else { v.c = 40; v.t = 0; v.cn = 0; v.b = ""; }
  ecrireMosaique(v);
  localStorage.setItem(directionScopedKey(DAILY_ACTIVITY_KEY), JSON.stringify({date: getTodayStr(), count: objectif - 1, milestonesCelebrated: 0}));
  return getDailyGoalTarget();
}"""
FETE = """() => {
  const b = document.querySelector('#confettiContainer .mos-palier');
  if (!b) return {palier: false};
  const t = b.querySelector('canvas'), r = b.getBoundingClientRect();
  const dessus = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
  let peint = false;
  if (t) { const d = t.getContext('2d').getImageData(0, 0, t.width, t.height).data; for (let i = 3; i < d.length; i += 4 * 97) if (d[i]) { peint = true; break; } }
  return {palier: true, toile: !!t, peint, auPremierPlan: !!(dessus && b.contains(dessus)) || getComputedStyle(document.getElementById('confettiContainer')).pointerEvents === 'none'};
}"""


def main():
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Muet, directory=RACINE))
    srv.handle_error = lambda *a: None
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    echecs = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for app in ("de", "es"):
            for objectif in (10, 30):
                for trophee in (False, True):
                    for contexte in ("cartes", "theme", "scene"):
                        ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                        ctx.set_default_timeout(120000)   # machine chargee (3 nov.) : 30 s ne suffisent pas toujours a charger la page
                        page = ctx.new_page()
                        erreurs = []
                        page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                        page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if app == "es" else ""))
                        page.wait_for_load_state("networkidle"); page.wait_for_timeout(1500)
                        page.evaluate(PREPARER, [objectif, trophee])
                        if contexte == "cartes":
                            page.evaluate("() => { currentCards = [{themeId: 'essai', index: 0}]; currentFlashcard = 0; nextFlashcard = () => {}; scheduleReview(10, true); poserCarreau(); }")
                        elif contexte == "theme":
                            page.evaluate("() => ouvrirThemeIllustre('emociones')")
                            cadre = page.frame_locator("#sceneCadre")
                            cadre.locator("#suite").click()                         # la decouverte -> les questions
                            page.wait_for_timeout(1200)
                            cadre.locator("#choix button").first.click()           # une vraie reponse
                        else:
                            page.evaluate("() => { sceneOuverteDepuis = 'tuile'; const m = t => window.postMessage(Object.assign({source: 'wortando-scene'}, t), '*');"
                                          " m({type: 'exercice', juste: true}); m({type: 'bonne'}); }")
                        page.wait_for_timeout(1400)
                        f = page.evaluate(FETE)
                        cas = "%s, objectif %d, %s, %s" % (app, objectif, "trophee" if trophee else "hors trophee", contexte)
                        ok = (not f["palier"]) if contexte == "scene" else (f["palier"] and f.get("toile") and f.get("peint") and f.get("auPremierPlan"))
                        print("  %-4s %-45s %s" % ("OK" if ok else "FAUX", cas, f))
                        if not ok or erreurs:
                            echecs.append(cas + (" ; erreurs JS " + str(erreurs[:2]) if erreurs else ""))
                        ctx.close()
        nav.close()
    srv.shutdown()
    if echecs:
        print("\nECHEC :\n  " + "\n  ".join(echecs))
        sys.exit(1)
    print("\nOK : le palier montre son tableau dans les cartes et les themes ; les scenes gardent leur regle.")


if __name__ == "__main__":
    main()
