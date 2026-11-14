# -*- coding: utf-8 -*-
"""UNE REVISION PAR PHRASE (ligne 84 ; decisions de Jacques du 13 nov. 2026 ; « Mi tia es profesora » revue par Jacques
le 14 nov. sur la v1189).

Deux parcours, une seance par jour, tout reussi (cartes de mots : appliquerReussite ; cartes-phrases : repondrePhrase) :
  tia   : un compte espagnol A1 (Premiers pas fini, 300 mots A1 maitrises dont profesora, « tia » du maintenant) ; la
          premiere seance pose « Mi tia es profesora », reussie ; puis 30 seances. Elle ne doit plus revenir (pas avant
          60 jours), et son echeance enregistree doit etre a 60 jours ;
  a1    : un compte neuf de et es, Premiers pas fini, 30 seances : cartes-phrases posees, phrases differentes, redites,
          doublons dans une meme seance, et l'anti-echo (une carte-phrase a moins de quatre cartes de la carte de son mot).
Lancer sur la version d'avant (--racine d'une copie de main) puis sur la branche : AVANT / APRES.
Usage : python tests/phrases_revision.py [--racine DOSSIER] [--port 8823] [--jours 30] [--cas tia,a1]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, collections, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SEMER_TIA = r"""
async () => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  localStorage.setItem(PROFIL_KEY, JSON.stringify({ r: 'cours', f: 'tout' }));
  await chargerPremiersPas();
  const a1 = paquetDuNiveau('A1').filter(c => c.mode !== 'phrase');
  const tia = a1.find(c => /famil/i.test(String(c.themeId)) && c.word && String(c.word[5] || '').indexOf('Mi tía es profesora') === 0);
  const prof = a1.filter(c => c.word && c.word[0] === 'profesora');
  const jour = 86400000, now = Date.now();
  const vus = prof.concat(a1.filter(c => c !== tia && prof.indexOf(c) < 0).slice(0, 300 - prof.length));
  vus.forEach(c => { const st = getWordState(c.themeId, c.index); st.vu = true; st.srsHits = 4; st.reviews = 4; st.mastered = true; st.due = now + 30 * jour; setWordState(c.themeId, c.index, st); });
  const st = getWordState(tia.themeId, tia.index);
  st.vu = true; st.srsHits = 0; st.reviews = 0; st.due = now - 60000; setWordState(tia.themeId, tia.index, st);
  return { tia: tia.themeId + '#' + tia.index, phrase: tia.word[5] };
}
"""

SEMER_A1 = r"""
() => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  localStorage.setItem(PROFIL_KEY, JSON.stringify({ r: 'cours', f: 'tout' }));
  fixerNiveauSeance('A1', true);
  return niveauSeance();
}
"""

SEANCE = r"""
async ([jour, cible]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); }
  Date.now = () => window.__vraiNow() + jour * 86400000;
  await ouvrirSeanceDuJour(); await pause(1500);
  const cartes = currentCards.slice();
  const cle = c => c.themeId + '#' + c.index;
  const phrases = [], echos = [];
  cartes.forEach((c, k) => {
    if(c.mode !== 'phrase' || !c.cible || !c.phrase) return;
    // Le bloc d'une dictee (« ordre », 3 a 5 cartes avant elle, v892) reprend VOULUMENT la phrase de la dictee.
    if(!c.prepaDictee) phrases.push(c.phrase.de);
    const kc = cle(c.cible);
    for(let j = Math.max(0, k - 4); j <= Math.min(cartes.length - 1, k + 4); j++){
      const d = cartes[j];
      if(j !== k && d && d.mode !== 'phrase' && cle(d) === kc){ echos.push(c.phrase.de + ' (mot a ' + (j - k) + ')'); break; }
    }
  });
  cartes.forEach(c => {
    try{
      if(c.av){ try{ marquerCarteA1V(c); }catch(e){} }
      if(c.mode === 'phrase'){ if(c.cible) repondrePhrase(c, true); return; }
      if(!c.word || c.themeId === undefined) return;
      const st = getWordState(c.themeId, c.index);
      if(!estNeuf(st) && (st.due || 0) > Date.now()) return;
      st.vu = true; appliquerReussite(st); setWordState(c.themeId, c.index, st);
    }catch(e){}
  });
  let etat = null;
  if(cible && typeof lireRevisions === 'function'){
    const x = lireRevisions().p[idRevision(cible)];
    if(x) etat = { reussites: x[0], echeanceDans: x[1] - jourRevision(), vue: x[2] - jourRevision() };
  }
  return { n: cartes.length, phrases, echos, etat };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8823)
    ap.add_argument("--jours", type=int, default=30)
    ap.add_argument("--cas", default="tia,a1")
    ap.add_argument("--attendu", choices=["apres", "avant"], default="apres",
                    help="apres : echoue si la regle n'est pas tenue ; avant : relever seulement")
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

    def ouvrir(nav, langue):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
        page = ctx.new_page()
        err = []
        page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        url = "http://127.0.0.1:%d/index.html?apprendre=%s" % (a.port, langue)
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1200)
        try:
            page.evaluate("() => { try{ if(typeof CODIGOS_VALIDOS !== 'undefined' && typeof CLAVE_ACCESO !== 'undefined') localStorage.setItem(CLAVE_ACCESO, CODIGOS_VALIDOS[0]); }catch(e){} }")
        except Exception:
            pass
        return ctx, page, url, err

    def seance(page, url, jour, cible=None):
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(700)
        return page.evaluate(SEANCE, [jour, cible])

    with sync_playwright() as p:
        nav = p.chromium.launch()
        cas = a.cas.split(",")
        if "tia" in cas:
            ctx, page, url, err = ouvrir(nav, "es")
            s = page.evaluate(SEMER_TIA)
            phrase = s["phrase"]
            print("tia : %s" % json.dumps(s, ensure_ascii=False), flush=True)
            r0 = seance(page, url, 0, phrase)
            pose0 = r0["phrases"].count(phrase)
            print("   jour 0 : « %s » posee %d fois, reussie ; etat %s" % (phrase, pose0, r0["etat"]), flush=True)
            if pose0 < 1:
                fautes.append("tia : la premiere seance n'a pas pose « %s » (le cas n'est pas rejoue)" % phrase)
            retours = []
            for j in range(1, a.jours + 1):
                r = seance(page, url, j, phrase)
                if phrase in r["phrases"]:
                    retours.append(j)
            print("   %d seances ensuite : « %s » revenue %d fois%s" % (a.jours, phrase, len(retours),
                  (" (jours %s)" % ", ".join(map(str, retours))) if retours else ""), flush=True)
            if r0["etat"] is not None:
                print("   echeance enregistree apres la reussite du jour 0 : dans %d jours" % r0["etat"]["echeanceDans"], flush=True)
            if a.attendu == "apres":
                if retours:
                    fautes.append("tia : « %s » revenue %d fois en %d jours (pas avant 60 jours attendu)" % (phrase, len(retours), a.jours))
                if not r0["etat"] or r0["etat"]["echeanceDans"] < 60:
                    fautes.append("tia : echeance apres la reussite = %s (60 jours attendus)" % (r0["etat"],))
            if err:
                print("   erreurs JavaScript : %s" % err[:3], flush=True)
            ctx.close()
        if "a1" in cas:
            for langue in ("de", "es"):
                ctx, page, url, err = ouvrir(nav, langue)
                page.evaluate(SEMER_A1)
                toutes, echos, doublons = [], [], 0
                for j in range(a.jours):
                    r = seance(page, url, j)
                    toutes += r["phrases"]
                    echos += r["echos"]
                    doublons += len(r["phrases"]) - len(set(r["phrases"]))
                c = collections.Counter(toutes)
                redites = len(toutes) - len(c)
                print("a1 %s, %d seances : %d cartes-phrases, %d phrases differentes, %d redites, %d doublons dans une seance, %d a moins de 4 cartes de leur mot ; la plus posee %s"
                      % (langue, a.jours, len(toutes), len(c), redites, doublons, len(echos), c.most_common(2)), flush=True)
                if a.attendu == "apres":
                    if redites:
                        fautes.append("a1 %s : %d redites en %d jours (aucune attendue : la reserve des jamais vues n'est pas vide)" % (langue, redites, a.jours))
                    if echos:
                        fautes.append("a1 %s : %d cartes-phrases a moins de 4 cartes de leur mot (%s)" % (langue, len(echos), echos[:2]))
                if err:
                    print("   erreurs JavaScript : %s" % err[:3], flush=True)
                ctx.close()
        nav.close()
    srv.shutdown()
    print()
    if fautes:
        print("ECHEC (%d)" % len(fautes))
        for f in fautes:
            print("  - " + f)
        sys.exit(1)
    print("OK" if a.attendu == "apres" else "RELEVE (version d'avant)")


if __name__ == "__main__":
    main()
