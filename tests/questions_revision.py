# -*- coding: utf-8 -*-
"""UNE REVISION PAR QUESTION, themes illustres (ligne 95, lot 1 ; decision de Jacques du 13 nov. 2026 : « une meme
approche pour les grandes reserves : phrases, themes, scenes »).

Un compte neuf joue une partie d'un theme par jour pendant N jours (la tuile, hors seance), en reussissant tout. Le
mot reste choisi par sa carte ; on regarde la QUESTION qui l'habille :
  redites  : une question deja REUSSIE reposee avant 60 jours (la regle : pas avant 60 jours) ;
  replis   : parmi ces redites, celles que la page a posees faute d'autre question pour ce mot (Tirage.statut le dit
             avant la reponse ; seulement apres la ligne 95) ;
  ms       : le temps moyen d'une question (le tirage par paliers ne doit pas alourdir la page).
Lancer sur la version d'avant (--racine d'une copie de main, --attendu avant) puis sur la branche : AVANT / APRES.
Usage : python tests/questions_revision.py [--racine DOSSIER] [--port 8824] [--jours 30] [--themes familia,emociones]
        [--langues de,es] [--attendu apres|avant]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, collections, functools, http.server, json, os, socketserver, sys, threading, time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OUVRIR = r"""
async ([jour, nom]) => {
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); }
  Date.now = () => window.__vraiNow() + jour * 86400000;
  try{ localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1'); }catch(e){}
  ouvrirThemeIllustre(nom);
  return sceneOuverteDepuis;
}
"""

# dans le cadre : avancer le temps comme l'app, lancer la partie
DEMARRER = r"""
async ([jour]) => {
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); }
  Date.now = () => window.__vraiNow() + jour * 86400000;
  await demarrer();
  await new Promise(r => setTimeout(r, 400));
  return { n: (typeof file !== 'undefined' && file) ? file.length : 0, rang: typeof rang !== 'undefined' ? rang : -1 };
}
"""

# une question : sa cle, son statut avant la reponse, puis une bonne reponse et la suivante
QUESTION = r"""
async () => {
  if(!file.length || rang >= file.length) return null;
  // la meme cle avant et apres la ligne 95 : celle de la page et le mot vise
  const m = typeof motQ !== 'undefined' ? motQ : null;
  const mt = !m ? '' : Array.isArray(m) ? m.join(' ') : typeof m === 'object' ? ((m.genre || '') + ' ' + (m.mot || '')).trim() : String(m);
  const brute = cleQuestion(), cle = mt ? brute + '|' + mt : brute;
  const statut = (typeof Tirage !== 'undefined' && Tirage.statut) ? Tirage.statut(brute) : null;
  const t0 = performance.now();
  juger(true, '');
  const s = document.getElementById('suite');
  if(s) s.click();
  const ms = performance.now() - t0;
  await new Promise(r => setTimeout(r, 30));
  return { cle, statut, ms, fin: rang >= file.length };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8824)
    ap.add_argument("--jours", type=int, default=30)
    ap.add_argument("--themes", default="familia,emociones,demarches,ropa")
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
            if f != page.main_frame and (nom + ".html") in f.url:
                return f
        return None

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for langue in a.langues.split(","):
            for nom in a.themes.split(","):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                page = ctx.new_page()
                err = []
                page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                url = "http://127.0.0.1:%d/index.html?apprendre=%s" % (a.port, langue)
                reussie = {}            # cle -> jour de la derniere reussite
                poses, redites, replis, temps, vides = 0, [], 0, [], 0
                for jour in range(a.jours + 1):
                    page.goto(url)
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(600)
                    page.evaluate(OUVRIR, [jour, nom])
                    f = None
                    for _ in range(40):
                        page.wait_for_timeout(250)
                        f = cadre(page, nom)
                        if f:
                            try:
                                f.wait_for_load_state("load")
                                if f.evaluate("() => typeof demarrer === 'function' && typeof IDS !== 'undefined' ? true : typeof demarrer === 'function'"):
                                    break
                            except Exception:
                                pass
                    if not f:
                        fautes.append("%s %s jour %d : le cadre du theme ne s'ouvre pas" % (langue, nom, jour))
                        break
                    page.wait_for_timeout(1200)       # les donnees du theme (fetch de la page)
                    d = f.evaluate(DEMARRER, [jour])
                    if not d["n"]:
                        vides += 1
                        continue
                    for _ in range(60):
                        q = f.evaluate(QUESTION)
                        if q is None:
                            break
                        poses += 1
                        temps.append(q["ms"])
                        j0 = reussie.get(q["cle"])
                        if j0 is not None and jour - j0 < 60:
                            redites.append((jour, jour - j0, q["cle"][:70]))
                            if q["statut"] == "attente":
                                replis += 1
                        reussie[q["cle"]] = jour
                        if q["fin"]:
                            break
                notees = page.evaluate("() => typeof lireRevisions === 'function' ? Object.keys(lireRevisions().t).length : -1")
                print("     revisions notees par l'app (type t) : %d" % notees, flush=True)
                if a.attendu == "apres" and notees < len(reussie):
                    fautes.append("%s %s : l'app n'a note que %d questions sur %d" % (langue, nom, notees, len(reussie)))
                distinctes = len(reussie)
                moy = sum(temps) / len(temps) if temps else 0
                print("%s %-11s %d jours : %d questions posees, %d differentes, %d redites avant 60 jours (dont %d replis), "
                      "%d jours sans partie, %.1f ms par question" % (langue, nom, a.jours, poses, distinctes, len(redites),
                                                                       replis, vides, moy), flush=True)
                for r in redites[:3]:
                    print("     jour %d, %d jours apres sa reussite : %s" % r, flush=True)
                if err:
                    print("     erreurs JavaScript : %s" % err[:3], flush=True)
                if a.attendu == "apres":
                    if len(redites) - replis:
                        fautes.append("%s %s : %d questions reussies reposees avant 60 jours alors qu'il y en avait d'autres"
                                      % (langue, nom, len(redites) - replis))
                    if not poses:
                        fautes.append("%s %s : aucune question posee" % (langue, nom))
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
