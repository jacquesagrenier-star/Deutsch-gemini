# -*- coding: utf-8 -*-
"""LE MODE SIMPLE DES THEMES DE LA PREMIERE SEMAINE (&simple=1 : une image et un mot ; v1168, proposition 3 de la revue).

Releve de la session du lot P3 (12 nov. 2026) : sur une page ou tous les mots sont neufs -- un debutant au jour 1 --, le
corps, les animaux et les emotions donnaient parfois une partie VIDE ou d'une seule question (le corps en espagnol : 24
parties vides sur 150), et les emotions, une seule sorte simple, la meme question de suite.

Pour chacun des quatre themes simples et chaque langue apprise, la sonde ouvre la page en seance et en mode simple, tous
les mots neufs (la demande d'etats a l'app est remplacee par « aucun etat »), et joue 150 parties de NB questions :
  - aucune partie vide, et toujours NB questions (3 dans la seance) ;
  - seulement des sortes simples ;
  - jamais deux fois la meme sorte de suite quand le theme en a plusieurs.
Usage : python tests/themes_simples.py [--racine DOSSIER] [--port 8803] [--parties 150]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

THEMES = ["cuerpo", "animales", "contrarios", "emociones"]
LANGUES = ["de", "es", "en", "pt", "pt&variante=br"]   # le portugais depuis la v1173 (lot P3)
NB = 3

JOUER = r"""
async ([n, nb]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  for(let k = 0; k < 80 && typeof Tirage === 'undefined'; k++) await pause(100);
  await pause(800);
  Tirage.demander = async () => null;                       // tous les mots neufs : le jour 1
  const e = s => { try{ return eval(s); }catch(x){ return undefined; } };
  const simples = e('typeof sortesDuMode === "function" ? sortesDuMode(false) : null');
  const res = { vides: 0, courtes: 0, longueurs: {}, sortes: {}, deSuite: 0, horsSimple: [], fini: 0, simples };
  let fini = false;
  if(typeof parler === 'function'){ const p = parler; parler = (t, d) => { if(t === 'fini') fini = true; try{ return p(t, d); }catch(x){} }; }
  for(let i = 0; i < n; i++){
    fini = false; eval('sorteCourante = null');
    await demarrer(); await pause(20);
    let q = 0, avant = null;
    for(let r = 0; r < 40; r++){
      const so = e('sorteCourante');
      if(!so || (e('file') || []).length === 0 || fini) break;
      q++;
      res.sortes[so] = (res.sortes[so] || 0) + 1;
      if(simples && simples.indexOf(so) < 0 && res.horsSimple.length < 5) res.horsSimple.push(so);
      if(avant && so === avant) res.deSuite++;
      avant = so;
      const rangNow = e('rang'), fl = e('file').length;
      if(rangNow + 1 >= fl) break;
      eval('rang++'); montrer(); await pause(5);
    }
    if(fini && q === 0) res.fini++;
    if(q === 0) res.vides++;
    else if(q < nb) res.courtes++;
    res.longueurs[q] = (res.longueurs[q] || 0) + 1;
  }
  return res;
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8803)
    ap.add_argument("--parties", type=int, default=150)
    a = ap.parse_args()

    class Serveur(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x, **k):
            pass

        def handle(self):
            try:
                super().handle()
            except (ConnectionError, OSError):
                pass

    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", a.port), functools.partial(Serveur, directory=a.racine))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    from playwright.sync_api import sync_playwright
    fautes = 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for th in THEMES:
            for lg in LANGUES:
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844})
                page = ctx.new_page()
                err = []
                page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
                page.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?seance=1&simple=1&nb=%d&apprendre=%s&lang=fr" % (a.port, th, NB, lg))
                page.wait_for_load_state("networkidle")
                try:
                    r = page.evaluate(JOUER, [a.parties, NB])
                except Exception as e:
                    print("FAUX  %-11s %s  %s" % (th, lg, str(e).split("\n")[0][:160]), flush=True)
                    fautes += 1
                    ctx.close()
                    continue
                plusieurs = len([s for s in (r["simples"] or []) if s]) > 1
                ok = r["vides"] == 0 and r["courtes"] == 0 and not r["horsSimple"] and (not plusieurs or r["deSuite"] == 0) and not err
                fautes += 0 if ok else 1
                print("%s %-11s %s  vides %3d  courtes %3d  longueurs %s  de suite %3d  hors simple %s  sortes %s%s" % (
                    "ok   " if ok else "FAUX ", th, lg, r["vides"], r["courtes"], json.dumps(r["longueurs"]), r["deSuite"],
                    r["horsSimple"] or "-", json.dumps(r["sortes"], ensure_ascii=False), ("  erreurs " + str(sorted(set(err))[:2])) if err else ""), flush=True)
                ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
