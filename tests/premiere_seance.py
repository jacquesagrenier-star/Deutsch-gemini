# -*- coding: utf-8 -*-
"""La premiere seance d'un compte neuf, juste apres la visite guidee (revue d'usage du 11 nov. 2026).

    python tests/premiere_seance.py                 (de et es, « zero » puis « peu »)
    python tests/premiere_seance.py --captures DOSSIER

Sur un navigateur vierge, sans compte : l'ecran de bienvenue (« Je pars de zero »), le profil s'il est pose,
la visite guidee jouee jusqu'au bout (« Commencer »), puis le vrai bouton « Commencer la seance » de l'accueil.
Controle :
  - la seance ouverte n'est pas vide : l'ecran des cartes, une carte a l'ecran, un paquet de plus de 5 cartes ;
  - la premiere carte d'un mot jamais vu se presente par la langue apprise (proposition 1 de la revue) ;
  - « Passer » des l'introduction mene aussi a une seance pleine.
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
PORT = int(os.environ.get("PREMIERE_PORT", "8817"))

INSCRIRE = r"""
async ([niveau]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const vu = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetParent); };
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  showScreen('setup'); await pause(300);
  if(vu('setupPortes')){ choisirPorteBienvenue(niveau === 'zero' ? 'zero' : 'tard'); }
  else choisirNiveauDeclare(niveau);
  await pause(200);
  if(ecran() === 'setup') document.querySelector('#setup button.primary[onclick="completeInitialSetup()"]').click();
  await pause(600);
  if(ecran() === 'profil'){ choisirRaisonProfil('plaisir'); await pause(500); choisirFaconProfil('tout'); await pause(900); }
  return ecran();
}
"""

VISITE = r"""
async ([passer]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const vu = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && getComputedStyle(e).display !== 'none'); };
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  const journal = [];
  for(let i = 0; i < 30 && !vu('decouverteDebut') && ecran() === 'decouverte'; i++) await pause(300);
  if(passer){ passerDecouverte(); await pause(900); return { journal: ['passer'], ecran: ecran() }; }
  document.getElementById('decouverteDebut').click(); await pause(1200);
  for(let i = 0; i < 60 && ecran() === 'decouverte'; i++){
    const et = decouverte ? decouverte.etape : null;
    if(vu('decouverteFermer')){ journal.push('fermer@' + et); document.getElementById('decouverteFermer').click(); await pause(1200); break; }
    if(vu('decouverteSuite')){ journal.push('suite@' + et); document.getElementById('decouverteSuite').click(); await pause(900); continue; }
    if(vu('decouverteFin')){ journal.push('fin@' + et); document.getElementById('decouverteFin').click(); await pause(900); continue; }
    if(et === 2){
      const act = document.getElementById('flashcardActions');
      if(act && !act.classList.contains('hidden')){ journal.push('bon'); reviewGood(); await pause(700); }
      else { journal.push('retourne'); try{ flipCard(); }catch(e){ journal.push('flip!' + e.message); } await pause(700); }
      continue;
    }
    journal.push('attente@' + et); await pause(800);
  }
  return { journal, ecran: ecran() };
}
"""

SEANCE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  await pause(1500);
  // les bulles de reperes, s'il y en a, se ferment au premier clic : on les ferme d'abord
  try{ fermerRepere(); }catch(e){}
  const bouton = document.querySelector('#home .pa-entrer');
  const accueil = { ecran: ecran(), bouton: bouton ? bouton.textContent.trim() : null, boutonVisible: !!(bouton && bouton.offsetParent) };
  if(bouton) bouton.click(); else await ouvrirSeanceDuJour();
  for(let i = 0; i < 40 && ecran() !== 'flashcards'; i++) await pause(250);
  await pause(1500);
  const fc = document.getElementById('flashcards');
  const carte = document.getElementById('flashcard');
  const r = carte ? carte.getBoundingClientRect() : null;
  const premier = currentCards[0] || null;
  return { accueil, ecran: ecran(), cartes: currentCards.length, plein: currentCardsFull ? currentCardsFull.length : null,
           carteVisible: !!(r && r.height > 40 && r.width > 40 && carte.offsetParent), carteDansEcran: !!(carte && fc && fc.contains(carte)),
           wrapperDansEcran: !!(fc && fc.querySelector('.flashcard-wrapper')), actionsDansEcran: !!(fc && fc.querySelector('#flashcardActions')),
           recto: (document.getElementById('flashFront') || carte || {}).textContent ? ((document.getElementById('flashFront') || carte).textContent || '').replace(/\s+/g, ' ').trim().slice(0, 120) : null,
           premier: premier ? { mode: premier.mode, forme: premier.forme || null, theme: premier.themeId, index: premier.index } : null,
           finPaquet: fc ? fc.classList.contains('fin-paquet') : null, titre: (document.getElementById('flashThemeTitle') || {}).textContent || null,
           presentee: !!document.querySelector('#flashcardActions.presentation'), retournee: !!(carte && carte.classList.contains('flipped')) };
}
"""

# Proposition 1 : « Je l'ai » sur la carte presentee -> la carte suivante, et la meme carte revient plus loin, demandee.
JE_L_AI = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const b = document.querySelector('#flashcardActions.presentation .presente-ok');
  if(!b || !b.offsetParent) return { bouton: false };
  const avant = currentCards.length, item = currentCards[currentFlashcard], i0 = currentFlashcard;
  b.click(); await pause(900);
  const revient = currentCards.findIndex((c, i) => i > i0 && c === item);
  return { bouton: true, avant, apres: currentCards.length, suivante: currentFlashcard, revientA: revient,
           suivantePresentee: !!document.querySelector('#flashcardActions.presentation') };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captures")
    ap.add_argument("--langues", default="de,es")
    ap.add_argument("--index", help="sert ce fichier a la place d'index.html (l'ancienne version)")
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
    fautes = 0
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris in a.langues.split(","):
                for niveau, passer in (("zero", False), ("peu", False), ("zero", True)):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1500)
                    nom = "%s-%s%s" % (appris, niveau, "-passee" if passer else "")
                    try:
                        e1 = page.evaluate(INSCRIRE, [niveau])
                        v = page.evaluate(VISITE, [passer])
                        s = page.evaluate(SEANCE)
                        if a.captures:
                            os.makedirs(a.captures, exist_ok=True)
                            page.screenshot(path=os.path.join(a.captures, "%s-%s%s-carte1.png" % (appris, niveau, "-passee" if passer else "")))
                        s["jeLai"] = page.evaluate(JE_L_AI) if s.get("presentee") else None
                    except Exception as e:
                        print("== %s ERREUR %s" % (nom, str(e).split("\n")[0][:300]), flush=True)
                        fautes += 1
                        ctx.close()
                        continue
                    if a.captures:
                        os.makedirs(a.captures, exist_ok=True)
                        page.screenshot(path=os.path.join(a.captures, nom + ".png"))
                    vide = (s["ecran"] != "flashcards") or (s["cartes"] < 5) or not s["carteVisible"] or not s["wrapperDansEcran"]
                    fautes += 1 if vide else 0
                    print("== %s %s  apres bienvenue: %s ; visite: %s -> %s" % (nom, "VIDE" if vide else "ok", e1, " ".join(v["journal"]), v["ecran"]), flush=True)
                    print("   " + json.dumps(s, ensure_ascii=False), flush=True)
                    err = sorted(set(x for x in erreurs if "synonymes" not in x))
                    if err:
                        print("   erreurs JS", err[:5], flush=True)
                    ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("aucune seance vide" if not fautes else "%d cas en defaut" % fautes))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
