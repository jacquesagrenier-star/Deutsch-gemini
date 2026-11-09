# -*- coding: utf-8 -*-
"""La fin de la seance du jour : le theme illustre est la derniere etape (decisions de Jacques, 8 nov. 2026).

    python tests/fin_de_seance.py                      (de et es, tous les cas, puis le libelle dans quelques langues)
    python tests/fin_de_seance.py --index AUTRE.html   (sert ce fichier a la place d'index.html : l'ancienne version)

Sur un navigateur vierge, sans compte. Chaque cas joue une seance en appelant les fonctions de la page et note ce qui suit le theme :
  tout_bien     : le theme en dernier, l'ecran de fin, une seance comptee ;
  encore_dernier: « Encore » sur le dernier mot avant la scene et le theme : la carte repasse AVANT le theme ;
  echu_scene    : une carte ratee redevenue due pendant la scene : AVANT le theme, dans la barre en parties ;
  echu_theme    : une carte devenue due pendant le theme : rien apres lui, elle attend la seance suivante, et la seance compte ;
  phrase_ratee  : une phrase ratee revient avant le theme ;
  son           : le son du jour avant le theme ;
  arriere       : des mots dus hors de la seance : rien ne s'ajoute apres le theme ;
  encore_seance : « Encore une seance » : barre en parties, surtitre « 2e seance du jour », « Bravo, 2 seances » a la fin.
Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("FIN_SEANCE_PORT", "8802"))

PREPARER = """
() => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1'); }
"""

MESURE = r"""
async ([cas]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas(); await chargerCiel();
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  const vraiNow = Date.now.bind(Date); let decalage = 0; Date.now = () => vraiNow() + decalage;
  if(cas === 'son') jourDApprentissage = () => 5;
  if(cas === 'arriere'){
    const hier = Date.now() - 2 * 86400000;
    paquetDuNiveau('A1').filter(c => c.mode !== 'phrase').slice(0, 60).forEach(c => {
      const st = getWordState(c.themeId, c.index); st.vu = true; st.srsHits = 2; st.due = hier; setWordState(c.themeId, c.index, st);
    });
  }
  const nom = c => !c ? '?' : (c.forme === 'theme_arret' ? 'THEME' : c.forme === 'scene_arret' ? 'SCENE' : c.mode === 'phrase' ? ('ph:' + (c.forme || '') + (String(c.themeId || '').indexOf('son_') === 0 ? ':son' : '')) : ('mot:' + c.themeId + ':' + c.index));
  const part = c => (SEANCE_PARTS && SEANCE_PARTS.parts.get(c)) || '-';
  const barre = () => { const b = document.getElementById('seanceParts'), f = b.children[0], z = document.getElementById('flashcards'), k = document.getElementById('flashKicker');
    return { cachee: b.classList.contains('hidden'), segs: [...b.children].map(x => x.className || '_').join(','), q: f ? f.style.getPropertyValue('--q') : '', fond: f ? getComputedStyle(f).backgroundImage.slice(0, 60) : '', finPaquet: z.classList.contains('fin-paquet'),
             kicker: k.textContent, kicker_lignes: (() => { const g = document.createRange(); g.selectNodeContents(k); return new Set([...g.getClientRects()].map(x => Math.round(x.top))).size; })(), kicker_deborde: k.scrollWidth > k.clientWidth + 1, titre: document.getElementById('flashThemeTitle').textContent, actif: seancePartsActive() }; };
  const jouer = async () => {
    const paquet = currentCards.slice();
    const T = paquet.findIndex(c => c && c.forme === 'theme_arret');
    const motsAvant = paquet.map((c, i) => [c, i]).filter(([c, i]) => i < T && c.mode !== 'phrase').map(x => x[1]);
    const encore = new Set(), fois = new Map();
    if(cas === 'encore_dernier') encore.add(paquet[motsAvant[motsAvant.length - 1]]);
    if(cas === 'echu_scene' || cas === 'echu_theme') encore.add(paquet[motsAvant[1]]);
    let phraseRatee = null;
    if(cas === 'phrase_ratee') phraseRatee = paquet.find(c => c.mode === 'phrase' && c.phrase && c.cible && c.forme !== 'gram' && c.exo === undefined && !c.av) || null;
    const joue = [], passages = [], apres = []; let vuTheme = false, tours = 0;
    const barreEntree = barre();
    for(let pas = 0; pas < 160; pas++){
      await pause(70);
      if(currentFlashcard >= currentCards.length) break;
      const scr = (document.querySelector('.screen.active') || {}).id;
      const c = currentCards[currentFlashcard];
      const go = document.querySelector('#cartePhrase .cp-passage-go');
      if(go && go.offsetHeight > 0){ passages.push(document.querySelector('.cp-passage').innerText.replace(/\n+/g, ' | ')); go.click(); await pause(120); continue; }
      if(scr === 'sceneSeance'){
        joue.push(nom(c));
        if(c.forme === 'scene_arret' && cas === 'echu_scene') decalage += 11 * 60 * 1000;
        if(c.forme === 'theme_arret'){ vuTheme = true; if(cas === 'echu_theme') decalage += 11 * 60 * 1000; }
        revenirDeLArret(); await pause(220); continue;
      }
      if(scr !== 'flashcards'){ joue.push('ecran:' + scr); break; }
      const n0 = currentFlashcard, q0 = currentCards;
      joue.push(nom(c));
      if(vuTheme) apres.push({ c: nom(c), rang: currentFlashcard + '/' + currentCards.length, part: part(c), barre: barre() });
      if(c.mode === 'phrase'){
        const juste = c === phraseRatee ? false : true;
        try{
          repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : juste);
          // le rappel de fin de seance d'une phrase ratee (appele par le rendu de la carte dans l'app)
          if(c === phraseRatee) noterPhraseRatee(c, false);
        }catch(e){ joue.push('err:' + e.message); }
        nextFlashcard();
      } else if(encore.has(c) && !fois.get(c)){ fois.set(c, 1); reviewAgain(); }
      else reviewGood();
      for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(60);
    }
    await pause(500);
    return { T, taille: paquet.length, joue, apres, passages, barreEntree, retenus: [...encore].map(nom), phraseRatee: phraseRatee && nom(phraseRatee), paquetFinal: currentCards === (SEANCE_PARTS || {}).paquet };
  };
  const finale = () => { const fin = document.getElementById('finCiel'), v = !!(fin && !fin.classList.contains('hidden') && fin.offsetHeight > 0);
    return { ciel: v, titre: v ? fin.querySelector('.fc-titre').textContent : '', mot: document.getElementById('flashEndObjectif').textContent, seances: seancesFiniesAujourdhui(), attendu2: tf('legere_fin_n', { n: 2 }) }; };
  await ouvrirSeanceDuJour(); await pause(1400);
  const un = await jouer();
  const finUn = finale();
  let deuxieme = null;
  if(cas === 'encore_seance'){
    const av = currentCards;
    document.getElementById('encoreNeufsBtn').click();
    for(let k = 0; k < 100 && currentCards === av; k++) await pause(100);
    await pause(1400);
    const entree = { taille: currentCards.length, ordre: currentCards.map(c => nom(c).split(':')[0] + '@' + part(c)).join(' '), barre: barre(), segments: SEANCE_PARTS ? segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).map(s => s.p + ':' + s.n) : null };
    const j2 = await jouer();
    deuxieme = { entree, joue: j2.joue.slice(-3), fin: finale() };
  }
  return { un, finUn, deuxieme };
}
"""

CAS = ["tout_bien", "encore_dernier", "echu_scene", "echu_theme", "phrase_ratee", "son", "arriere", "encore_seance"]
LANGUES_LIBELLE = ["ar", "ru", "tr"]


def juger(cas, r):
    u = r["un"]; j = u["joue"]; f = r["finUn"]
    if "THEME" not in j:
        return ["pas de theme joue"]
    fautes = []
    apres = j[j.index("THEME") + 1:]
    if apres:
        fautes.append("apres le theme : %s" % apres[:5])
    if f["seances"] != 1:
        fautes.append("seances %s" % f["seances"])
    if not f["ciel"] and cas != "arriere":   # avec des revisions d'avance, ce compte n'est plus dans l'A1 voyage : pas de ciel
        fautes.append("pas de ciel a la fin")
    avant = j[:j.index("THEME")]
    if cas == "encore_dernier" and u["retenus"] and avant.count(u["retenus"][0]) != 2:
        fautes.append("la carte ne repasse pas avant le theme")
    if cas == "echu_scene":
        if not u["retenus"] or avant.count(u["retenus"][0]) < 3:
            fautes.append("la carte echue ne repasse pas avant le theme : %s fois" % (avant.count(u["retenus"][0]) if u["retenus"] else "?"))
    if cas == "son" and not any(x.endswith(":son") for x in avant):
        fautes.append("pas de son avant le theme")
    if any("Le thème illustré : c'est fait" in p for p in u["passages"]):
        fautes.append("un passage apres le theme")
    if cas == "encore_seance":
        d = r["deuxieme"]
        if not d:
            return fautes + ["pas de deuxieme seance"]
        if not d["entree"]["segments"] or len(d["entree"]["segments"]) < 2:
            fautes.append("barre d'un seul morceau : %s" % d["entree"]["segments"])
        if "2" not in d["entree"]["barre"]["kicker"]:
            fautes.append("surtitre sans le rang : %s" % d["entree"]["barre"]["kicker"])
        if d["fin"]["titre"] != d["fin"]["attendu2"] or d["fin"]["seances"] != 2:
            fautes.append("fin de la 2e seance : %s, %s" % (d["fin"]["titre"], d["fin"]["seances"]))
    return fautes


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
    total = 0

    def essai(nav, appris, cas, ui, largeur):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": largeur, "height": 780}, service_workers="block")
        page = ctx.new_page()
        erreurs = []
        page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else ""))
        page.wait_for_load_state("networkidle")
        page.evaluate(PREPARER)
        if ui:
            page.evaluate("([l]) => localStorage.setItem(UI_LANG_KEY, l)", [ui])
        page.reload()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1200)
        try:
            r = page.evaluate(MESURE, [cas])
        except Exception as e:
            ctx.close()
            return None, [str(e).split("\n")[0][:300]], erreurs
        ctx.close()
        return r, juger(cas, r), erreurs

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris in ("de", "es"):
                for cas in CAS:
                    r, fautes, erreurs = essai(nav, appris, cas, None, 360 if cas != "encore_seance" else 320)
                    total += 1 if fautes else 0
                    print("== %s %-15s %s %s" % (appris, cas, "ok" if not fautes else "FAUTE", fautes), flush=True)
                    if r:
                        u = r["un"]
                        j = u["joue"]
                        print("   T %s/%s, suite du theme %s, 2 dernieres avant %s, fin %s" % (u["T"], u["taille"], j[j.index("THEME") + 1:][:6] if "THEME" in j else "?", j[max(0, j.index("THEME") - 2):j.index("THEME")] if "THEME" in j else "?", json.dumps(r["finUn"], ensure_ascii=False)), flush=True)
                        for x in u["apres"][:2]:
                            print("   apres :", json.dumps(x, ensure_ascii=False), flush=True)
                        print("   passages :", u["passages"], flush=True)
                        if r["deuxieme"]:
                            print("   2e seance :", json.dumps(r["deuxieme"], ensure_ascii=False)[:900], flush=True)
                    erreurs = [e for e in erreurs if "synonymes" not in e]
                    if erreurs:
                        print("   erreurs JS", sorted(set(erreurs))[:4], flush=True)
            for ui in LANGUES_LIBELLE:
                r, fautes, erreurs = essai(nav, "de", "encore_seance", ui, 320)
                total += 1 if fautes else 0
                d = (r or {}).get("deuxieme") or {}
                print("== libelle %s %s %s %s" % (ui, "ok" if not fautes else "FAUTE", fautes, json.dumps(d.get("entree", {}).get("barre"), ensure_ascii=False)), flush=True)
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not total else "%d cas en defaut" % total))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
