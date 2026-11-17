# -*- coding: utf-8 -*-
"""UNE REVISION PAR QUESTION, scenes (ligne 95, lot 2 ; decision de Jacques du 13 nov. 2026 : « une meme approche pour
les grandes reserves : phrases, themes, scenes »).

Un compte neuf joue la meme scene dans la seance (5 questions) une fois par jour pendant N jours, en reussissant
tout : en A1 (« Trouve ! ») et en A2 (questions a choix, plus une « Trouve ! » de l'A1). On regarde chaque question
(la scene et son texte, ou le mot a trouver) :
  redites : une question deja REUSSIE reposee avant 60 jours ;
  replis  : parmi elles, celles posees faute de question jamais vue ou due (seulement apres la ligne 95) ;
  jamais  : combien de questions differentes la scene a montrees -- la reserve doit defiler.
Lancer sur la version d'avant (--racine d'une copie, --attendu avant) puis sur la branche : AVANT / APRES.
Usage : python tests/scenes_revision.py [--racine DOSSIER] [--port 8825] [--jours 30] [--scenes klassenzimmer,baeckerei]
        [--niveaux A1,A2] [--langues de,es] [--attendu apres|avant]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


EN_COURS = {}


def charger(page, url):
    """Ouvre l'app et attend qu'elle soit prete (ses fonctions), pas que le reseau se taise ;
    une requete encore en vol apres 15 s est nommee, pas fatale."""
    cle = id(page)
    if cle not in EN_COURS:
        EN_COURS[cle] = set()
        page.on("request", lambda r: EN_COURS[cle].add(r.url))
        page.on("requestfinished", lambda r: EN_COURS[cle].discard(r.url))
        page.on("requestfailed", lambda r: EN_COURS[cle].discard(r.url))
    page.goto(url, wait_until="domcontentloaded", timeout=90000)
    page.wait_for_function("typeof showScreen === 'function' && typeof chargerCadre === 'function'"
                           " && typeof ouvrirThemeIllustre === 'function' && typeof baseScenes === 'function'",
                           timeout=90000)
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        reste = sorted(EN_COURS[cle])[:5]
        print("     (reseau encore actif apres 15 s : %s)" % ", ".join(u[:90] for u in reste), flush=True)

OUVRIR = r"""
([jour, nom, niv]) => {
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); }
  Date.now = () => window.__vraiNow() + jour * 86400000;
  try{ localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1'); }catch(e){}
  sceneOuverteDepuis = "seance";
  chargerCadre(document.getElementById("sceneCadre"), baseScenes() + "index.html?scene=" + encodeURIComponent(nom)
    + "&seance=1&niveau=" + niv + "&nb=5&lang=fr" + langueDeScene() + "&vitesse=1&t=" + Date.now());
  showScreen("sceneSeance");
  return true;
}
"""

ETAPE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const rang = cle => typeof rangRevision === 'function' ? rangRevision(cle) : null;
  if (attendUnToucher()){
    const mot = attenteToucher, cle = NOM_SCENE + '|trouve|' + mot, r = rang(cle), b0 = bons;
    const pr = proprietaire(mot), zs = zonesDe(mot);
    const z = zs.find(id => !pr || racine(P[id]) === pr) || zs[0];
    toucher(z);
    await pause(60);
    const juste = bons > b0;
    const s = document.querySelector('#bas .suite'); if (s) s.click();
    await pause(80);
    return { cle, rang: r, juste };
  }
  if (niveau !== 'A1' && COUCHES[niveau] && COUCHES[niveau].ordre){
    const q = COUCHES[niveau].ordre[i];
    if (!q) return { fin: true };
    if (q._trouve){ await pause(150); return { attente: true }; }
    const cle = NOM_SCENE + '|' + (q._niv || niveau) + '|' + q.q, r = rang(cle), b0 = bons;
    const bon = Array.from(document.querySelectorAll('#bas .choix')).find(x => x.textContent === q.c[0]);
    if (!bon) return { bloque: 'pas de bonne reponse a toucher' };
    bon.click();
    await pause(60);
    const juste = bons > b0;
    const s = document.querySelector('#bas .suite'); if (s) s.click();
    await pause(80);
    return { cle, rang: r, juste };
  }
  return { fin: true };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8825)
    ap.add_argument("--jours", type=int, default=30)
    ap.add_argument("--scenes", default="klassenzimmer,baeckerei")
    ap.add_argument("--niveaux", default="A1,A2")
    ap.add_argument("--langues", default="de,es")
    ap.add_argument("--attendu", choices=["apres", "avant"], default="apres")
    a = ap.parse_args()

    class S(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x, **k):
            pass

        def handle(self):
            try:
                super().handle()
            except (ConnectionError, OSError):
                pass

    srv = socketserver.ThreadingTCPServer(("127.0.0.1", a.port), functools.partial(S, directory=a.racine))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = []
    from playwright.sync_api import sync_playwright

    def cadre(page, nom):
        for f in page.frames:
            if f != page.main_frame and ("scene=" + nom) in f.url:
                return f
        return None

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for langue in a.langues.split(","):
            for nom in a.scenes.split(","):
                for niv in a.niveaux.split(","):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    err = []
                    page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    url = "http://127.0.0.1:%d/index.html?apprendre=%s" % (a.port, langue)
                    reussie, poses, redites, replis, ratees = {}, 0, [], 0, 0
                    for jour in range(a.jours + 1):
                        charger(page, url)
                        page.wait_for_timeout(500)
                        page.evaluate(OUVRIR, [jour, nom, niv])
                        f = None
                        for _ in range(40):
                            page.wait_for_timeout(250)
                            f = cadre(page, nom)
                            if f:
                                try:
                                    f.wait_for_load_state("load")
                                    if f.evaluate("() => typeof attendUnToucher === 'function' && (attenteToucher !== null || (typeof COUCHES !== 'undefined' && COUCHES[niveau] && COUCHES[niveau].ordre))"):
                                        break
                                except Exception:
                                    pass
                        if not f:
                            fautes.append("%s %s %s jour %d : la scene ne s'ouvre pas" % (langue, nom, niv, jour))
                            break
                        page.wait_for_timeout(300)
                        for _ in range(40):
                            e = f.evaluate(ETAPE)
                            if e.get("fin"):
                                break
                            if e.get("bloque"):
                                fautes.append("%s %s %s jour %d : %s" % (langue, nom, niv, jour, e["bloque"]))
                                break
                            if e.get("attente"):
                                continue
                            poses += 1
                            if not e["juste"]:
                                ratees += 1
                            j0 = reussie.get(e["cle"])
                            if j0 is not None and jour - j0 < 60:
                                redites.append((jour, jour - j0, e["cle"][:70]))
                                if e["rang"] == 2:
                                    replis += 1
                            if e["juste"]:
                                reussie[e["cle"]] = jour
                    notees = page.evaluate("() => typeof lireRevisions === 'function' ? Object.keys(lireRevisions().s).length : -1")
                    print("     revisions notees par l'app (type s) : %d" % notees, flush=True)
                    if a.attendu == "apres" and notees < len(reussie):
                        fautes.append("%s %s : l'app n'a note que %d questions sur %d" % (langue, nom, notees, len(reussie)))
                    print("%s %-13s %s, %d jours : %d questions posees, %d differentes, %d redites avant 60 jours (dont %d replis), %d ratees par la sonde"
                          % (langue, nom, niv, a.jours, poses, len(reussie), len(redites), replis, ratees), flush=True)
                    for r in redites[:3]:
                        print("     jour %d, %d jours apres sa reussite : %s" % r, flush=True)
                    if err:
                        print("     erreurs JavaScript : %s" % err[:3], flush=True)
                    if a.attendu == "apres":
                        if len(redites) - replis:
                            fautes.append("%s %s %s : %d questions reussies reposees avant 60 jours alors qu'il y en avait d'autres"
                                          % (langue, nom, niv, len(redites) - replis))
                        if not poses:
                            fautes.append("%s %s %s : aucune question posee" % (langue, nom, niv))
                    ctx.close()
        nav.close()
    srv.shutdown()
    print()
    if fautes:
        print("ECHEC (%d)" % len(fautes))
        for x in fautes:
            print("  - " + x)
        sys.exit(1)
    print("OK" if a.attendu == "apres" else "RELEVE (version d'avant)")


if __name__ == "__main__":
    main()
