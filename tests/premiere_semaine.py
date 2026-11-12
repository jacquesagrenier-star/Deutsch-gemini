# -*- coding: utf-8 -*-
"""LA PREMIERE SEMAINE D'UN DEBUTANT (proposition 3 de la revue de l'app, 11 nov. 2026).

Un compte neuf qui part de zero (Premiers pas), jours 1 a 7, en allemand et en espagnol : chaque jour, la seance du jour
est ouverte et jouee (toutes les cartes sues), et l'on releve ce que la scene et le theme demandent.

Ce qui doit tenir :
  - la scene, chaque jour, ne demande JAMAIS un mot que la personne n'a pas encore rencontre : soit des mots vus (dans
    les cartes de Premiers pas ou du corpus), soit elle commence par Decouvrir (on touche, on entend) et Trouve ! ne
    porte que sur ce qui a ete touche ;
  - le theme est un des quatre themes simples (le corps, les animaux, les contraires, les emotions), ouvert sur sa
    decouverte, en trois questions d'une sorte simple (une image et un mot) ; la famille n'apparait pas.

Usage : python tests/premiere_semaine.py [--racine DOSSIER] [--jours 7] [--port 8806]
  --racine : un autre depot (par exemple main, pour comparer avant / apres).
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, datetime, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
() => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true }));
}
"""

JOUR = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas();
  const debut = typeof premiereSemaineDebutant === 'function' ? premiereSemaineDebutant() : null;
  const etape = jourPremiersPas();
  await ouvrirSeanceDuJour(); await pause(1500);
  const paquet = currentCards.slice();
  const nom = c => !c ? '?' : (c.forme === 'theme_arret' ? 'THEME' : c.forme === 'scene_arret' ? 'SCENE' : c.forme === 'pp_scene' ? 'SCENE_ETAPE' : c.mode === 'phrase' ? 'ph' : 'mot');
  // ce qui est deja vu AVANT la seance, scene par scene (la regle de l'app, et le simple « non neuf » du corpus)
  const arrets = [], VUS = {};
  for(const c of paquet.filter(x => x && (x.forme === 'scene_arret' || x.forme === 'pp_scene'))){
    const nomScene = c.forme === 'pp_scene' ? c.scene : c.scene.nom;
    let vus = null;
    try{ vus = await motsVusDeScene(nomScene); }catch(e){}
    const mots = (c.mots || []).map(m => m[0]);
    arrets.push({ forme: c.forme, scene: nomScene, mots, decouvrir: !!c.decouvrir, inconnus: vus ? mots.filter(m => !vus.has(m)) : null, vus: vus ? vus.size : null });
    if(vus) VUS[nomScene] = Array.from(vus.keys());
  }
  const th = paquet.find(x => x && x.forme === 'theme_arret');
  const theme = th ? { nom: th.theme, nb: th.nb, decouvrir: !!th.decouvrir, simple: !!th.simple } : null;
  const segs = (SEANCE_PARTS && SEANCE_PARTS.paquet === currentCards) ? segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).map(s => s.p) : null;
  // jouer la seance ; dans chaque scene et chaque theme, regarder la page avant de revenir
  const vu = [];
  for(let pas = 0; pas < 200; pas++){
    await pause(60);
    if(currentFlashcard >= currentCards.length) break;
    const scr = (document.querySelector('.screen.active') || {}).id;
    const c = currentCards[currentFlashcard];
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    if(go && go.offsetHeight > 0){ go.click(); await pause(120); continue; }
    if(scr === 'sceneSeance'){
      const f = document.getElementById('sceneCadre');
      let w = null;
      for(let k = 0; k < 80; k++){ try{ w = f.contentWindow; if(w && w.document.readyState === 'complete' && w.document.body && w.document.body.children.length) break; }catch(e){} await pause(150); }
      await pause(1600);
      const x = { quoi: nom(c), url: (f.getAttribute('src') || '').replace(/^.*\//, '').replace(/&t=\d+/, '').slice(0, 160) };
      try{
        if(c.forme === 'theme_arret'){
          const suite = w.document.getElementById('suite');
          x.ouverture = (suite && !suite.hidden) ? 'decouverte' : 'questions';
          if(x.ouverture === 'decouverte'){ suite.click(); await pause(1200); }
          x.sorte = w.eval('typeof sorteCourante !== "undefined" ? sorteCourante : null');
          const en = w.document.querySelector('.enonce, #zone .consigne');
          x.question = en ? en.textContent.trim().slice(0, 70) : '';
        } else {
          x.mode = w.eval('typeof modeA1 !== "undefined" ? modeA1 : null');
          x.demande = w.eval('typeof attenteToucher !== "undefined" ? attenteToucher : null');
          const sc = c.forme === 'pp_scene' ? c.scene : c.scene.nom;
          // les mots vus AU MOMENT de la scene : une carte de la seance meme a pu les montrer
          let ici = null; try{ ici = await motsVusDeScene(sc); }catch(e){}
          x.inconnu = x.mode === 'trouver' && x.demande && ici && !ici.has(x.demande) ? x.demande : null;
          const q = w.document.querySelector('#carte .question');
          x.question = q ? q.textContent.replace(/\s+/g, ' ').trim().slice(0, 60) : '';
        }
      }catch(e){ x.err = String(e).slice(0, 80); }
      vu.push(x);
      if(c.forme === 'pp_scene'){ try{ revenirDeLArret(); }catch(e){} } else revenirDeLArret();
      await pause(250); continue;
    }
    if(scr !== 'flashcards') break;
    const n0 = currentFlashcard, q0 = currentCards;
    if(c.mode === 'phrase'){ try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){} nextFlashcard(); }
    else reviewGood();
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(60);
  }
  await pause(600);
  return { debut, etape, taille: paquet.length, ordre: paquet.map(nom).filter(n => n !== 'mot' && n !== 'ph').join(' '), segs, arrets, theme, vu, finies: seancesFiniesAujourdhui() };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--jours", type=int, default=7)
    ap.add_argument("--port", type=int, default=8806)
    ap.add_argument("--langues", default="de,es")
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
    base = datetime.datetime(2026, 11, 16, 9, 0, 0)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for appris in a.langues.split(","):
            ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
            page = ctx.new_page()
            erreurs = []
            page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
            page.on("dialog", lambda d: d.dismiss())
            page.clock.install(time=base)
            url = "http://127.0.0.1:%d/index.html%s" % (a.port, "?apprendre=es" if appris == "es" else "")
            page.goto(url)
            page.wait_for_load_state("networkidle")
            page.evaluate(PREPARER)
            for j in range(1, a.jours + 1):
                page.clock.set_system_time(base + datetime.timedelta(days=j - 1))
                page.reload()
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(1500)
                try:
                    r = page.evaluate(JOUR)
                except Exception as e:
                    print("== %s jour %d ERREUR %s" % (appris, j, str(e).split("\n")[0][:200]), flush=True)
                    fautes += 1
                    continue
                inconnus = [m for x in r["arrets"] for m in (x["inconnus"] or [])]
                th = r["theme"] or {}
                juge = []
                if inconnus:
                    juge.append("mots inconnus demandes : " + ", ".join(inconnus))
                if r["debut"] is not None and not r["debut"]:
                    juge.append("pas en premiere semaine")
                if th and th.get("nom") == "familia":
                    juge.append("la famille")
                SIMPLES = {"cuerpo": ["tocar", "nombrar"], "animales": ["nom", "entendre"], "contrarios": ["comment", "cual", "entendre"], "emociones": ["quien"]}
                for v in r["vu"]:
                    if v["quoi"] == "THEME" and v.get("ouverture") != "decouverte":
                        juge.append("theme sans decouverte")
                    if v["quoi"] == "THEME" and th.get("simple") and v.get("sorte") and v.get("sorte") not in SIMPLES.get(th.get("nom"), []):
                        juge.append("question de theme pas simple : " + str(v.get("sorte")))
                    if v.get("inconnu"):
                        juge.append("la scene demande un mot inconnu : " + v["inconnu"])
                fautes += 1 if juge else 0
                print("== %s jour %d  %s  (etape %s, %s cartes)" % (appris, j, "ok" if not juge else "FAUTE " + " ; ".join(juge), r["etape"] + 1, r["taille"]), flush=True)
                print("   barre :", " ".join(r["segs"] or []), "| arrets :", r["ordre"], flush=True)
                for x in r["arrets"]:
                    print("   scene %-13s %s mots=%s vus=%s inconnus=%s" % (x["scene"], "DECOUVRIR" if x["decouvrir"] else ("etape    " if x["forme"] == "pp_scene" else "trouve   "), x["mots"], x["vus"], x["inconnus"]), flush=True)
                if th:
                    print("   theme %-13s nb=%s decouvrir=%s simple=%s" % (th["nom"], th["nb"], th["decouvrir"], th["simple"]), flush=True)
                for v in r["vu"]:
                    print("   vu :", json.dumps(v, ensure_ascii=False), flush=True)
            err = sorted(set(e for e in erreurs if "synonymes" not in e))
            if err:
                print("   erreurs JS :", err[:4], flush=True)
            ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d jour(s) a voir" % fautes)


if __name__ == "__main__":
    main()
