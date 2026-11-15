# -*- coding: utf-8 -*-
"""UNE PARTIE GRAMMAIRE DANS CHAQUE SEANCE (decision de Jacques du 12 nov. 2026 : « Ouais, j'aimerais avoir une partie
grammaire dans chaque seance »).

Cas joues de bout en bout (de et es, jour et nuit), la barre relevee a chaque carte :
  palier1   : un compte A1 hors Premiers pas, 0 mot vu (pas de question « gram » avant 60 vus) ;
  regles    : le meme, profil « regles » : cinq cartes de grammaire au moins (trois pour les autres) ;
  pp-jour1  : Premiers pas, premiere seance (le tableau « Etre : sein / ser » dans Grammaire) ;
  pp-milieu : Premiers pas au milieu de l'etape 1 (sans tableau : trois questions tirees du tableau) ;
  es-latam  : le palier 1 et le milieu d'etape avec la variante d'Amerique latine.
Ce qui doit tenir : « grammaire » dans la barre des la premiere carte, et la barre ne change pas en route ; au moins
trois cartes de grammaire ; la longueur de la seance = celle du paquet suivi (l'anneau compte les cartes ajoutees).
Puis l'UNICITE : chaque question tiree d'un tableau (toutes les etapes, de, es, es-latam, en ; 40 tirages) n'a qu'une
option juste -- pour « sie ___ », aucune option n'est la forme d'une autre ligne qui partage un pronom.
Enfin une carte « gram » (palier 2 et plus) range dans Grammaire.
Usage : python tests/grammaire_chaque_seance.py [--racine DOSSIER] [--port 8815] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PREPARER = """
([pp, regles, latam]) => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(!pp) localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  else localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true }));
  if(regles) localStorage.setItem(PROFIL_KEY, JSON.stringify({ f: 'regles' }));
  if(latam) localStorage.setItem(PREFIXE_STOCKAGE + 'variante', 'latam'); }
"""
MILIEU = """
async () => { await chargerPremiersPas(); const seq = sequencePremiersPas(); const i = seq.findIndex(x => x.forme === 'pp_tableau' && x.jourPP === 0);
  const s = lirePremiersPas(); s.p = i + 5; ecrirePremiersPas(s); return s.p; }
"""
BARRE = r"""
() => {
  const enPP = currentTheme && currentTheme.id === 'seance_premiers_pas';
  const parts = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? SEANCE_PARTS.parts : enPP ? partsPremiersPas(currentCards) : null;
  const segs = parts ? segmentsSeance(currentCards, parts) : null;
  const noms = [...document.querySelectorAll('#seancePartsNoms > *')].map(x => x.textContent);
  const gram = parts ? currentCards.filter(c => parts.get(c) === 'grammaire') : [];
  return { segs: segs ? segs.map(s => s.p) : null, noms, n: currentCards.length,
           suivi: (typeof seanceSuivie !== 'undefined' && seanceSuivie && seanceSuivie.paquet) ? seanceSuivie.paquet.length : null,
           gram: gram.map(c => c.forme + (c.gramTableau ? '/tableau' : c.jeu ? '/' + c.jeu : '') + (c.ex ? ' « ' + c.ex.question + ' »' : '')) };
}
"""
JOUER = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const releves = [];
  const barre = """ + BARRE.strip() + r""";
  for(let pas = 0; pas < 200; pas++){
    await pause(50);
    const vis = id => { const e = document.getElementById(id); return !!(e && !e.classList.contains('hidden') && e.offsetHeight > 0); };
    if(vis('flashcardEnd') || vis('finRevision')) break;
    if(currentFlashcard >= currentCards.length) break;
    const scr = (document.querySelector('.screen.active') || {}).id;
    const c = currentCards[currentFlashcard];
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    if(go && go.offsetHeight > 0){ go.click(); await pause(120); continue; }
    if(scr === 'sceneSeance'){
      releves.push(barre());
      if(c && c.forme === 'pp_scene') break;
      revenirDeLArret(); await pause(220); continue;
    }
    if(scr !== 'flashcards') break;
    releves.push(barre());
    const n0 = currentFlashcard, q0 = currentCards;
    if(c.mode === 'phrase'){
      if(c.forme === 'gram'){ const b = document.querySelector('#cartePhrase .cp-choix button'); if(b){ b.click(); await pause(150); } }
      try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){}
      nextFlashcard();
    } else reviewGood();
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(50);
  }
  return releves;
}
"""
UNICITE = r"""
async ([n]) => {
  await chargerPremiersPas();
  const fautes = [], vus = [];
  const pronoms = PRONOMS_TABLEAU[LANGUE_APPRISE] || [];
  joursPremiersPas().forEach((j, d) => {
    const lignes = (j.tableau.l || []);
    const decoupe = lignes.map(l => { const m = /^(.+?)\s+(\S+)$/.exec(String(l[0]).trim()); if(!m) return null;
      const pr = m[1].split(/\s*·\s*/); return pr.every(x => pronoms.indexOf(x) >= 0) ? { pr: pr.map(x => x.toLowerCase()), f: m[2] } : null; });
    for(let k = 0; k < n; k++){
      questionsDeTableau(j.tableau, 99).forEach(it => {
        const ex = it.ex, q = ex.question;
        if(new Set(ex.options).size !== ex.options.length) fautes.push('etape ' + (d + 1) + ' options en double : ' + q + ' ' + ex.options);
        if(ex.options.indexOf(ex.answers[0]) < 0) fautes.push('etape ' + (d + 1) + ' reponse absente : ' + q);
        let justes;
        if(/ ___$/.test(q)){
          const pr = q.replace(/ ___$/, '').split(/\s*·\s*/).map(x => x.toLowerCase());
          const permises = new Set(decoupe.filter(e => e && e.pr.some(x => pr.indexOf(x) >= 0)).map(e => e.f));
          justes = ex.options.filter(o => permises.has(o));
          if(k === 0) vus.push(q + ' → ' + ex.options.join(' / '));
        } else {
          const sens = lignes.filter(l => l[0] === q).map(l => sensPremiersPas(l[1]).toLowerCase());
          justes = ex.options.filter(o => sens.indexOf(o.toLowerCase()) >= 0);
          if(k === 0 && vus.length < 40) vus.push(q + ' → ' + ex.options.join(' / '));
        }
        if(justes.length !== 1) fautes.push('etape ' + (d + 1) + ' ' + justes.length + ' options justes : ' + q + ' [' + ex.options.join(' / ') + ']');
      });
    }
  });
  return { fautes: [...new Set(fautes)].slice(0, 6), vus: vus.slice(0, 14) };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8815)
    ap.add_argument("--captures")
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
    if a.captures:
        os.makedirs(a.captures, exist_ok=True)
    from playwright.sync_api import sync_playwright
    fautes = 0
    PERMIS = ["cartes", "grammaire", "images", "conv"]

    def ouvrir(nav, appris, pp, regles=False, latam=False, nuit=False):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
        page = ctx.new_page()
        err = []
        page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        url = {"de": "", "es": "?apprendre=es", "en": "?apprendre=en"}[appris]
        page.goto("http://127.0.0.1:%d/index.html%s" % (a.port, url))
        page.wait_for_load_state("networkidle")
        page.evaluate(PREPARER, [pp, regles, latam])
        page.evaluate("([n]) => localStorage.setItem(THEME_STORAGE_KEY, n ? 'dark' : 'light')", [nuit])
        page.reload()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        return ctx, page, err

    with sync_playwright() as p:
        nav = p.chromium.launch()
        cas_liste = []
        for appris in ("de", "es"):
            for cas in ("palier1", "regles", "pp-jour1", "pp-milieu"):
                for nuit in (False, True):
                    cas_liste.append((appris, cas, nuit, False))
        cas_liste += [("es", "palier1", False, True), ("es", "pp-milieu", False, True)]
        for appris, cas, nuit, latam in cas_liste:
            pp = cas.startswith("pp")
            ctx, page, err = ouvrir(nav, appris, pp, regles=(cas == "regles"), latam=latam, nuit=nuit)
            if cas == "pp-milieu":
                page.evaluate(MILIEU)
            page.evaluate("async () => { await ouvrirSeanceDuJour(); }")
            page.wait_for_timeout(1600)
            tag = "%s-%s%s-%s" % (appris, cas, "-latam" if latam else "", "nuit" if nuit else "jour")
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, "gram-%s-1-debut.png" % tag))
                # la premiere carte de grammaire, ecran de passage compris
                page.evaluate("""async () => { const enPP = currentTheme.id === 'seance_premiers_pas';
                    const parts = (SEANCE_PARTS && currentCards === SEANCE_PARTS.paquet) ? SEANCE_PARTS.parts : partsPremiersPas(currentCards);
                    const k = currentCards.findIndex(c => parts.get(c) === 'grammaire');
                    if(k > 0){ currentFlashcard = k; loadFlashcard(); await new Promise(r => setTimeout(r, 700)); } }""")
                page.screenshot(path=os.path.join(a.captures, "gram-%s-2-passage.png" % tag))
                page.evaluate("""async () => { const go = document.querySelector('#cartePhrase .cp-passage-go'); if(go && go.offsetHeight > 0){ go.click(); await new Promise(r => setTimeout(r, 600)); } }""")
                page.screenshot(path=os.path.join(a.captures, "gram-%s-3-grammaire.png" % tag))
                page.evaluate("async () => { currentFlashcard = 0; PASSAGES_VUS.clear(); loadFlashcard(); await new Promise(r => setTimeout(r, 400)); }")
            debut = page.evaluate(BARRE)
            rel = page.evaluate(JOUER)
            juge = []
            d = debut["segs"] or []
            if "grammaire" not in d:
                juge.append("pas de Grammaire dans la barre")
            if [x for x in PERMIS if x in d] != d:
                juge.append("ordre ou partie fausse : %s" % d)
            if len(debut["gram"]) < (5 if cas == "regles" else 3):
                juge.append("%d carte(s) de grammaire" % len(debut["gram"]))
            if debut["suivi"] is not None and debut["suivi"] != debut["n"]:
                juge.append("paquet suivi %s != seance %s" % (debut["suivi"], debut["n"]))
            changes = [r for r in rel if r["segs"] and r["segs"] != d]
            if changes:
                juge.append("la barre change en route (%d fois, ex. %s)" % (len(changes), changes[0]["segs"]))
            if cas == "pp-milieu" and not any("/tableau" in g for g in debut["gram"]):
                juge.append("pas de question tiree du tableau")
            er = sorted(set(x for x in err if "synonymes" not in x))
            if er:
                juge.append("erreurs JS %s" % er[:2])
            fautes += 1 if juge else 0
            print("== %-24s %s  barre %s  noms %s  %d cartes" % (tag, "ok" if not juge else "FAUTE " + " ; ".join(juge), d, debut["noms"], debut["n"]), flush=True)
            for g in debut["gram"][:4]:
                print("     ", g, flush=True)
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, "gram-%s-4-fin.png" % tag))
            ctx.close()

        # L'unicite de la bonne reponse, sur tous les tableaux.
        for appris, latam in (("de", False), ("es", False), ("es", True), ("en", False)):
            ctx, page, err = ouvrir(nav, appris, True, latam=latam)
            r = page.evaluate(UNICITE, [40])
            tag = appris + ("-latam" if latam else "")
            fautes += 1 if r["fautes"] else 0
            print("== unicite %-8s %s" % (tag, "ok" if not r["fautes"] else "FAUTE %s" % r["fautes"]), flush=True)
            for v in r["vus"][:8]:
                print("     ", v, flush=True)
            ctx.close()

        # Une carte « gram » du palier 2 range dans Grammaire.
        ctx, page, err = ouvrir(nav, "de", False)
        g = page.evaluate("() => [partDeCarteSeance({ mode: 'phrase', forme: 'gram', cible: null }, null, new Map()), groupePartie('gram')]")
        ok = g == ["gram", "grammaire"]
        fautes += 0 if ok else 1
        print("== carte gram du palier 2 %s %s" % ("ok" if ok else "FAUTE", g), flush=True)
        ctx.close()
        nav.close()
    srv.shutdown()
    print("RESULTAT :", "tout est bon" if not fautes else "%d cas a voir" % fautes)


if __name__ == "__main__":
    main()
