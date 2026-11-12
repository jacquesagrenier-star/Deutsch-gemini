# -*- coding: utf-8 -*-
"""Le mot neuf presente avant d'etre demande (revue d'usage du 11 nov. 2026, proposition 1 ; precisions de Jacques).

    python tests/presentation_mot_neuf.py --captures DOSSIER        (de et es)

Sur un navigateur vierge, sans compte : « Je pars de zero », la visite passee, la seance du jour. Trois cas :
  presente : la carte neuve arrive par son verso (bandeau « Nouveau mot », le mot, la traduction) ; un seul geste, la
             bille a sa place habituelle, Encore et Mettre de cote invisibles a leur place ; elle revient plus loin et
             se demande depuis le francais (decision de Jacques du 11 nov. : la bille seule, pas de « Je le connaissais deja ») ;
  rate     : presente, puis rate a la demande (« Encore ») -> il revient, comme toute carte ratee.
Les points des cartes (v1164) ne changent pas. Il ouvre un navigateur : a lancer SOUS LE VERROU.
"""
import argparse
import functools
import http.server
import json
import os
import socketserver
import sys
import threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("PRESENTATION_PORT", "8818"))

PREPARER = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  showScreen('setup'); await pause(200);
  const portes = document.getElementById('setupPortes');
  if(portes && !portes.classList.contains('hidden')) choisirPorteBienvenue('zero'); else choisirNiveauDeclare('zero');
  completeInitialSetup(); await pause(600);
  if(document.querySelector('#profil.active')){ choisirRaisonProfil('plaisir'); await pause(400); choisirFaconProfil('tout'); await pause(800); }
  try{ document.getElementById('badgeToast').classList.remove('show'); }catch(e){}
  for(let i = 0; i < 40 && !decouverte; i++) await pause(250);
  if(decouverte) passerDecouverte();
  await pause(900);
  try{ fermerRepere(); }catch(e){}
  await ouvrirSeanceDuJour(true);
  for(let i = 0; i < 40 && !(currentCards && currentCards.length); i++) await pause(250);
  await pause(800);
  if(SEANCE_PARTS) segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).forEach(s => PASSAGES_VUS.add(s.p));
  return currentCards.length;
}
"""

# Avance jusqu'a la premiere carte presentee (les cartes-phrases, scenes et themes passent sans jugement).
VERS_PRESENTEE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  for(let k = 0; k < 60; k++){
    const it = currentCards[currentFlashcard];
    if(!it) return null;
    if(document.querySelector('#flashcardActions.presentation')) return { i: currentFlashcard, mot: (document.getElementById('flashBackWord') || {}).textContent, mode: it.mode || flashcardMode };
    if(it.mode === 'phrase' || it.forme){ nextFlashcard(); await pause(500); continue; }
    try{ flipCard(); }catch(e){} await pause(300); reviewGood(); await pause(1300);
  }
  return null;
}
"""

ETAT = r"""
() => {
  const vis = sel => { const e = document.querySelector(sel); return !!(e && e.offsetParent && !e.classList.contains('hidden')); };
  const tx = id => ((document.getElementById(id) || {}).textContent || '').replace(/\s+/g, ' ').trim();
  return { presentation: vis('#flashcardActions.presentation'), retournee: document.getElementById('flashcard').classList.contains('flipped'),
           etiquette: vis('#flashNouveauVerso') ? tx('flashNouveauVerso') : null, mot: tx('flashBackWord'), traduction: vis('#flashTranslation') ? tx('flashTranslation') : null,
           continuer: vis('#flashcardActions .judge-good'), recto: tx('flashWord'),
           encoreVisible: vis('#flashcardActions .judge-again') && getComputedStyle(document.querySelector('#flashcardActions .judge-again')).visibility !== 'hidden',
           gardeVisible: vis('#flashcardActions .judge-garde') && getComputedStyle(document.querySelector('#flashcardActions .judge-garde')).visibility !== 'hidden',
           bille: (() => { const b = document.querySelector('#flashcardActions .judge-good'); if(!b) return null; const r = b.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)]; })(),
           points: tx('srsLadderText'), i: currentFlashcard, n: currentCards.length };
}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captures", required=True)
    ap.add_argument("--langues", default="de,es")
    a = ap.parse_args()
    os.makedirs(a.captures, exist_ok=True)

    class Serveur(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x, **k):
            pass

        def handle(self):
            try:
                super().handle()
            except (ConnectionError, OSError):
                pass

    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Serveur, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--marque-" + os.environ["PRESENTATION_MARQUE"]] if os.environ.get("PRESENTATION_MARQUE") else [])
            for appris in a.langues.split(","):
                for cas in ("presente", "rate"):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1500)
                    cap = lambda nom: page.screenshot(path=os.path.join(a.captures, "%s-%s-%s.png" % (appris, cas, nom)), timeout=120000, animations="disabled")
                    nb = page.evaluate(PREPARER)
                    pres = page.evaluate(VERS_PRESENTEE)
                    if not pres:
                        fautes.append("%s %s : aucune carte presentee (paquet %s)" % (appris, cas, nb))
                        print("== %s %s FAUTE aucune carte presentee" % (appris, cas), flush=True)
                        ctx.close()
                        continue
                    page.wait_for_timeout(1400)
                    bulle = page.evaluate("() => { const b = document.querySelector('.bulle-repere'); return b ? b.textContent : null; }")
                    if bulle:
                        cap("0-bulle")
                    page.evaluate("() => { try{ fermerRepere(); }catch(e){} }")
                    page.wait_for_timeout(300)
                    e1 = page.evaluate(ETAT)
                    e1["bulle"] = bulle
                    cap("1-presentee")
                    if not bulle:
                        fautes.append("%s %s : pas de bulle au premier mot neuf" % (appris, cas))
                    ok1 = e1["presentation"] and e1["retournee"] and e1["continuer"] and not e1["encoreVisible"] and not e1["gardeVisible"] and bool(e1["traduction"]) and bool(e1["etiquette"])
                    if not ok1:
                        fautes.append("%s %s : presentation incomplete %s" % (appris, cas, e1))
                    i0 = pres["i"]
                    page.click("#flashcardActions .judge-good")
                    page.wait_for_timeout(900)
                    # jusqu'a la demande de la meme carte
                    trouve = page.evaluate(r"""
                    async ([i0]) => {
                      const pause = ms => new Promise(r => setTimeout(r, ms));
                      const cible = currentCards[i0];
                      for(let k = 0; k < 40; k++){
                        if(currentCards[currentFlashcard] === cible && currentFlashcard > i0) return currentFlashcard;
                        const it = currentCards[currentFlashcard];
                        if(!it) return -1;
                        if(document.querySelector('#flashcardActions.presentation')){ motPresenteVu(); await pause(600); continue; }
                        if(it.mode === 'phrase' || it.forme){ nextFlashcard(); await pause(500); continue; }
                        try{ flipCard(); }catch(e){} await pause(300); reviewGood(); await pause(1300);
                      }
                      return -1;
                    }""", [i0])
                    page.wait_for_timeout(500)
                    e2 = page.evaluate(ETAT)
                    cap("2-demandee-recto")
                    page.evaluate("() => flipCard()")
                    page.wait_for_timeout(700)
                    cap("3-demandee-verso")
                    e3 = page.evaluate(ETAT)
                    if trouve < 0 or e2["presentation"] or e2["retournee"]:
                        fautes.append("%s %s : la carte n'est pas redemandee (%s, %s)" % (appris, cas, trouve, e2))
                    ligne = "== %s %s presentee %s | redemandee a %s, recto « %s », verso : Encore visible %s, bille %s (presentee %s)" % (appris, cas, json.dumps(e1, ensure_ascii=False), trouve, e2["recto"], e3["encoreVisible"], e3["bille"], e1["bille"])
                    if e3["bille"] != e1["bille"]:
                        fautes.append("%s %s : la bille change de place (%s puis %s)" % (appris, cas, e1["bille"], e3["bille"]))
                    if cas == "rate":
                        page.click("#flashcardActions .judge-again")
                        page.wait_for_timeout(500)
                        cap("4-ratee")
                        revient = page.evaluate("([i]) => currentCards.slice(i + 1).includes(currentCards[i])", [trouve])
                        ligne += " | ratee : revient %s" % revient
                        if not revient:
                            fautes.append("%s rate : le mot rate ne revient pas" % appris)
                    print(ligne, flush=True)
                    err = sorted(set(x for x in erreurs if "synonymes" not in x))
                    if err:
                        print("   erreurs JS", err[:4], flush=True)
                    ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    for f in fautes:
        print("FAUTE", f)
    print("RESULTAT : %s" % ("tout est bon" if not fautes else "%d faute(s)" % len(fautes)))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
