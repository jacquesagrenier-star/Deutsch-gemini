# -*- coding: utf-8 -*-
"""Tout le contenu : les maladresses M1, M3, M4 de la revue A a Z (12 nov. 2026) et « Relier ses idees » (es).

    python tests/lot69_contenu.py                      (sur index.html)
    python tests/lot69_contenu.py --index AUTRE.html   (l'ancienne version : les defauts doivent s'y voir)

Sur un navigateur vierge, sans compte. Chaque chemin est joue jusqu'au retour a l'accueil :
  M1  le titre de l'ecran de resultat suit le score (33 % : pas « Tres bien ! ») ;
  M3a « ‹ » depuis Noms > Les terminaisons, Noms > Par niveau, Verbes > Par niveau, Adjectifs > Par niveau : retour
      au panneau d'origine, puis « ‹ » du panneau : l'accueil ;
  M3b « Accueil » de l'ecran de resultat d'une serie lancee depuis un panneau : retour a ce panneau ;
  M3c la tuile Ecouter de l'accueil ouvre ses trois modes (ecran ecouteMenu) ;
  M4  Examens > Comprendre l'examen > M'entrainer : ecouter : une serie de 10, pas 80 ;
  es  Expressions > « Relier ses idees », la dose du jour reduite a un mot : au moins 10 cartes.
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
PORT = int(os.environ.get("LOT69_PORT", "8834"))

PREPARER = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  try{ markSetupDone(); }catch(e){}
  goHome(); await pause(300);
  for(let i = 0; i < 40 && !themesLoaded; i++) await pause(250);
  return themesLoaded;
}
"""

CAS_DE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  const retour = () => { const b = document.querySelector('section.screen.active button.back'); if(b) b.click(); };
  const out = {};
  // M3a : les pages d'explication ou de liste ouvertes depuis un panneau
  for(const [panneau, action] of [["nomen", "ouvrirReglesGenre"], ["nomen", "openNomenNiveau"], ["verben", "openVerbenNiveau"], ["adjektive", "openAdjektive"]]){
    goHome(); await pause(200);
    ouvrirToutLeContenu(); await pause(200);
    openOrbPanel(panneau); await pause(300);
    orbAction(action); await pause(700);
    const page = ecran();
    retour(); await pause(500);
    const apres = ecran() + (ecran() === "orbPanel" ? ":" + openOrbId : "");
    retour(); await pause(500);
    out["M3a " + panneau + " > " + action] = { page, apresRetour: apres, puis: ecran() };
  }
  // M3b et M1 : une serie lancee depuis un panneau, terminee a 33 %, puis « Accueil »
  goHome(); await pause(200); ouvrirToutLeContenu(); await pause(200);
  openOrbPanel("nomen"); await pause(300);
  orbAction("startQuizArticle"); await pause(1200);
  const serie = ecran();
  activeExercises = (activeExercises || []).slice(0, 3); if(activeExercises.length < 3) activeExercises = [{}, {}, {}];
  scoreValue = 1; exerciseResults = [];
  showResults(); await pause(400);
  const titre = (document.getElementById('resultTitle') || {}).textContent;
  const bouton = document.querySelector('#result [data-retour]');
  const libelle = bouton ? bouton.textContent.trim() : null;
  if(bouton) bouton.click(); await pause(600);
  const apresAccueil = ecran() + (ecran() === "orbPanel" ? ":" + openOrbId : "");
  retour(); await pause(400);
  out["M1+M3b serie nomen 33 %"] = { serie, titre, bouton: libelle, apres: apresAccueil, puis: ecran() };
  // M3c : la tuile Ecouter de l'accueil
  goHome(); await pause(400);
  const tuile = document.querySelector('#home [data-tg="ecouter"]');
  if(tuile) tuile.click(); await pause(1200);
  const apresTuile = ecran();
  try{ arreterEcoute(); }catch(e){}
  goHome(); await pause(400);
  out["M3c tuile Ecouter"] = { ecran: apresTuile, puis: ecran() };
  // M4 : l'ecoute d'examen
  goHome(); await pause(200); ouvrirToutLeContenu(); await pause(200);
  openOrbPanel("pruefung"); await pause(400);
  orbAction("openPruefungInfo"); await pause(600);
  try{ await loadPruefungJson(); }catch(e){}
  startPruefungHoeren(); await pause(1500);
  out["M4 ecouter l'examen"] = { ecran: ecran(), questions: (activeExercises || []).length, serie: exerciseBlocTotal ? (exerciseBlocNo + 1) + "/" + exerciseBlocTotal : null,
                                 compteur: ((document.getElementById('exerciseProgress') || document.querySelector('#exercise .pill') || {}).textContent || '').trim() };
  goHome(); await pause(300);
  out["fin"] = ecran();
  return out;
}
"""

CAS_ES = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const ecran = () => (document.querySelector('section.screen.active') || {}).id || '?';
  // la dose du jour reduite a un mot, comme sur le compte de la revue
  let garde = 0;
  while(placeNeufsRestante() > 1 && garde++ < 200) noterMotNeuf();
  const dose = placeNeufsRestante();
  goHome(); await pause(200); ouvrirToutLeContenu(); await pause(200);
  openOrbPanel("redewendungen"); await pause(400);
  orbAction("ausdrueckeDiskussion"); await pause(900);
  const r = { dose, ecran: ecran(), cartes: currentCards.length, groupe: (currentCardsFull || []).length };
  handleFlashcardBack(); await pause(500);
  goHome(); await pause(300);
  r.fin = ecran();
  return r;
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index")
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
            nav = p.chromium.launch(args=["--marque-" + os.environ["LOT69_MARQUE"]] if os.environ.get("LOT69_MARQUE") else [])
            for appris, cas in (("de", CAS_DE), ("es", CAS_ES)):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else ""))
                page.wait_for_load_state("networkidle"); page.wait_for_timeout(1500)
                page.evaluate(PREPARER)
                r = page.evaluate(cas)
                if appris == "de":
                    for k, v in r.items():
                        print("== de %-36s %s" % (k, json.dumps(v, ensure_ascii=False)), flush=True)
                    for k, v in r.items():
                        if k.startswith("M3a") and not str(v.get("apresRetour", "")).startswith("orbPanel"):
                            fautes.append("%s : « ‹ » ne ramene pas au panneau (%s)" % (k, v.get("apresRetour")))
                        if k.startswith("M3a") and v.get("puis") != "home":
                            fautes.append("%s : le panneau ne ramene pas a l'accueil" % k)
                    s = r["M1+M3b serie nomen 33 %"]
                    if s["titre"] and "bien" in s["titre"].lower():
                        fautes.append("M1 : « %s » a 33 %%" % s["titre"])
                    if not str(s["apres"]).startswith("orbPanel"):
                        fautes.append("M3b : « %s » sort du panneau (%s)" % (s["bouton"], s["apres"]))
                    if r["M3c tuile Ecouter"]["ecran"] != "ecouteMenu":
                        fautes.append("M3c : la tuile Ecouter ouvre %s, pas ses trois modes" % r["M3c tuile Ecouter"]["ecran"])
                    if r["M4 ecouter l'examen"]["questions"] > 15:
                        fautes.append("M4 : %d questions d'un seul tenant" % r["M4 ecouter l'examen"]["questions"])
                    if r["fin"] != "home":
                        fautes.append("de : pas de retour a l'accueil a la fin")
                else:
                    print("== es Relier ses idees %s" % json.dumps(r, ensure_ascii=False), flush=True)
                    if r["cartes"] < min(10, r["groupe"]):
                        fautes.append("es : « Relier ses idees » ouvre %d carte(s) sur %d" % (r["cartes"], r["groupe"]))
                    if r["fin"] != "home":
                        fautes.append("es : pas de retour a l'accueil")
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
