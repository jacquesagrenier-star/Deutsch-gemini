# -*- coding: utf-8 -*-
"""« Essentiel » pendant la visite guidee (revue d'usage du 11 nov. 2026, defaut grave, reproduit deux fois).

    python tests/visite_essentiel.py                       (de et es, sur index.html)
    python tests/visite_essentiel.py --index AUTRE.html    (l'ancienne version : le defaut doit s'y voir)

Sur un navigateur vierge, sans compte : « Je pars de zero », la visite, l'etape des premiers mots ; on touche
« Essentiel » sur la carte (ouvrirAideExamen), puis « Revenir a la carte » (retourDepuisAideExamen). Controle :
  - on revient DANS la visite, la carte a l'ecran ;
  - la visite se finit, et la seance du jour s'ouvre avec ses cartes (carte visible dans l'ecran des cartes) ;
  - « rechargement » : un compte deja pris dans l'etat casse (l'ancienne version) retrouve une seance normale apres
    rechargement de la page.
Il ouvre un navigateur : a lancer SOUS LE VERROU (~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("VISITE_PORT", "8831"))

JUSQU_A_LA_CARTE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const vu = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetParent); };
  showScreen('setup'); await pause(200);
  const portes = document.getElementById('setupPortes');
  if(portes && !portes.classList.contains('hidden')) choisirPorteBienvenue('zero'); else choisirNiveauDeclare('zero');
  document.querySelector('#setup button.primary[onclick="completeInitialSetup()"]').click(); await pause(700);
  if(document.querySelector('#profil.active')){ choisirRaisonProfil('plaisir'); await pause(400); choisirFaconProfil('tout'); await pause(900); }
  for(let i = 0; i < 40 && !vu('decouverteDebut'); i++) await pause(250);
  document.getElementById('decouverteDebut').click(); await pause(1200);
  for(let i = 0; i < 20 && decouverte && decouverte.etape < 2; i++){ if(vu('decouverteSuite')) document.getElementById('decouverteSuite').click(); await pause(900); }
  await pause(900);
  const carte = document.getElementById('flashcard');
  if(carte && !carte.classList.contains('flipped')) flipCard();
  await pause(600);
  const coin = document.getElementById('flashExamenCoin');
  return { etape: decouverte ? decouverte.etape : null, coinVisible: !!(coin && !coin.classList.contains('hidden') && coin.offsetParent) };
}
"""

ESSENTIEL_ALLER_RETOUR = r"""
async ([parCoin]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  const coin = document.getElementById('flashExamenCoin');
  if(parCoin && coin && coin.offsetParent) coin.click(); else ouvrirAideExamen();
  await pause(700);
  const pendant = ecran();
  retourDepuisAideExamen(); await pause(800);
  const fc = document.getElementById('flashcards'), sc = document.getElementById('decouverteScene');
  return { pendant, apres: ecran(), visite: !!decouverte, carteDansVisite: !!(sc && sc.querySelector('#flashcard')),
           carteDansCartes: !!(fc && fc.querySelector('#flashcard')), carteVisible: !!(document.getElementById('flashcard') || {}).offsetParent };
}
"""

FINIR_VISITE_PUIS_SEANCE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const vu = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && getComputedStyle(e).display !== 'none'); };
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  for(let i = 0; i < 60 && decouverte; i++){
    if(vu('decouverteFermer')){ document.getElementById('decouverteFermer').click(); await pause(1000); break; }
    if(vu('decouverteSuite')){ document.getElementById('decouverteSuite').click(); await pause(900); continue; }
    if(decouverte.etape === 2){ const a = document.getElementById('flashcardActions'); if(a && !a.classList.contains('hidden')) reviewGood(); else { try{ flipCard(); }catch(e){} } await pause(800); continue; }
    await pause(800);
  }
  return await SEANCE();
}
"""

SEANCE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  try{ fermerRepere(); }catch(e){}
  if(ecran() !== 'home'){ goHome(); await pause(600); }
  try{ fermerRepere(); }catch(e){}
  const b = document.querySelector('#home .pa-entrer'); if(b) b.click(); else await ouvrirSeanceDuJour(true);
  for(let i = 0; i < 40 && ecran() !== 'flashcards'; i++) await pause(250);
  await pause(1500);
  const fc = document.getElementById('flashcards'), carte = document.getElementById('flashcard');
  return { ecran: ecran(), cartes: currentCards.length, visiteEnCours: !!decouverte,
           carteDansCartes: !!(fc && carte && fc.contains(carte)), carteVisible: !!(carte && carte.offsetParent && carte.getBoundingClientRect().height > 40) };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index")
    ap.add_argument("--langues", default="de,es")
    a = ap.parse_args()
    index = os.path.abspath(a.index) if a.index else None

    class Serveur(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x, **k):
            pass

        def translate_path(self, chemin):
            if index and chemin.split("?")[0] in ("/", "/index.html"):
                return index
            return super().translate_path(chemin)

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
            nav = p.chromium.launch(args=["--marque-" + os.environ["VISITE_MARQUE"]] if os.environ.get("VISITE_MARQUE") else [])
            for appris in a.langues.split(","):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                url = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else "")
                page.goto(url); page.wait_for_load_state("networkidle"); page.wait_for_timeout(1500)
                page.evaluate("() => { window.SEANCE = " + SEANCE.strip() + "; }")
                c = page.evaluate(JUSQU_A_LA_CARTE)
                r = page.evaluate(ESSENTIEL_ALLER_RETOUR, [True])
                ok_retour = r["apres"] == "decouverte" and r["visite"] and r["carteDansVisite"] and r["carteVisible"]
                print("== %s carte de la visite %s | Essentiel puis retour : %s" % (appris, json.dumps(c), json.dumps(r)), flush=True)
                if not ok_retour:
                    fautes.append("%s : le retour d'Essentiel ne ramene pas dans la visite" % appris)
                s = page.evaluate(FINIR_VISITE_PUIS_SEANCE) if r["visite"] else page.evaluate("() => SEANCE()")
                ok_seance = s["ecran"] == "flashcards" and s["cartes"] >= 5 and s["carteDansCartes"] and s["carteVisible"] and not s["visiteEnCours"]
                print("   seance du jour ensuite : %s %s" % ("ok" if ok_seance else "VIDE OU CASSEE", json.dumps(s)), flush=True)
                if not ok_seance:
                    fautes.append("%s : seance du jour sans carte apres la visite" % appris)
                ctx.close()
                # ABANDON (le cas reel) : apres le retour d'Essentiel, la personne revient a l'accueil et lance sa seance
                # sans finir la visite. Puis un compte deja pris dans cet etat : rechargement, et la seance.
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                page = ctx.new_page()
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                page.goto(url); page.wait_for_load_state("networkidle"); page.wait_for_timeout(1500)
                page.evaluate("() => { window.SEANCE = " + SEANCE.strip() + "; }")
                page.evaluate(JUSQU_A_LA_CARTE)
                page.evaluate(ESSENTIEL_ALLER_RETOUR, [True])
                s = page.evaluate("() => SEANCE()")
                ok_ab = s["ecran"] == "flashcards" and s["cartes"] >= 5 and s["carteDansCartes"] and s["carteVisible"] and not s["visiteEnCours"]
                print("   abandon (accueil puis seance) : %s %s" % ("ok" if ok_ab else "VIDE OU CASSEE", json.dumps(s)), flush=True)
                if not ok_ab:
                    fautes.append("%s : seance du jour sans carte apres abandon de la visite" % appris)
                # un compte deja pris dans l'etat casse : rechargement, puis la seance
                page.reload(); page.wait_for_load_state("networkidle"); page.wait_for_timeout(1500)
                page.evaluate("() => { window.SEANCE = " + SEANCE.strip() + "; }")
                s2 = page.evaluate("() => SEANCE()")
                ok2 = s2["ecran"] == "flashcards" and s2["cartes"] >= 5 and s2["carteDansCartes"] and s2["carteVisible"]
                print("   apres rechargement : %s %s" % ("ok" if ok2 else "TOUJOURS CASSEE", json.dumps(s2)), flush=True)
                if not ok2:
                    fautes.append("%s : la seance reste cassee apres rechargement" % appris)
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
