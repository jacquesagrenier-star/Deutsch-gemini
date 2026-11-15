# -*- coding: utf-8 -*-
"""LA SEANCE EN PARTIES D'UNE SEULE SORTE (ligne 98, decisions de Jacques du 14 nov. 2026) : Mots, Phrases, Grammaire,
Images, et la Conversation les jours ou il y en a une.

Rejoue une seance du jour en vrai, en de et en es, A1 (une escale de l'A1 voyage) et A2 :
  - les cartes de mots jugees par les fonctions des boutons : reviewAgain (« Encore ») sur la 2e, reviewGood sur les
    autres (un mot neuf presente fait son retour de 10 minutes) ; la premiere carte-phrase ratee, les autres reussies ;
  - en quittant la premiere partie, l'horloge avance de 12 minutes (le temps d'une vraie seance : les retours sont dus).
Trois regles verifiees a chaque carte montree :
  (1) la carte est de la sorte de la partie allumee dans la barre (une carte de mot sous Grammaire = le defaut du 14 nov.) ;
  (2) un meme mot n'est montre qu'une fois (une carte revenue -- Encore, retour -- n'est pas un doublon) ;
  (3) la barre n'avance que dans un sens (la partie allumee ne recule jamais).
Lancer sur la version d'avant (--racine d'une copie, --attendu avant) puis sur la branche : AVANT / APRES.
--captures DOSSIER : la barre a 4 et 5 parties (la conversation ajoutee pour l'image), jour et nuit, 375 px ; puis la
barre a 5 parties dans les 11 langues d'interface.
Usage : python tests/seance_parties.py [--racine DOSSIER] [--port 8828] [--attendu apres|avant] [--captures DOSSIER]
Sous le verrou du navigateur (~/.wortando/verrou-parcours).
"""
import argparse, functools, http.server, json, os, socketserver, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SEMER = r"""
async ([niv]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  localStorage.setItem(PROFIL_KEY, JSON.stringify({ r: 'cours', f: 'tout' }));
  fixerNiveauSeance(niv, true);
  const NIV = ['A1', 'A2', 'B1', 'B2', 'C1'], avant = NIV.slice(0, NIV.indexOf(niv));
  avant.forEach(a => paquetDuNiveau(a).forEach(c => { const st = getWordState(c.themeId, c.index); st.vu = true; st.connu = true; st.srsHits = 4; st.mastered = true; st.due = Date.now() + 400 * 86400000; setWordState(c.themeId, c.index, st); }));
  // l'A1 : quelques mots deja vus et dus, pour qu'il y ait des revisions (et des cartes-phrases) des la premiere seance
  if(niv === 'A1') paquetDuNiveau('A1').filter(c => c.mode !== 'phrase').slice(0, 60).forEach(c => { const st = getWordState(c.themeId, c.index); st.vu = true; st.srsHits = 2; st.reviews = 2; st.due = Date.now() - 3600000; setWordState(c.themeId, c.index, st); });
  if(!window.__vraiNow){ window.__vraiNow = Date.now.bind(Date); window.__decalage = 0; Date.now = () => window.__vraiNow() + window.__decalage; }
  return niveauSeance();
}
"""

OUVRIR = r"""
async () => {
  await ouvrirSeanceDuJour(); await new Promise(r => setTimeout(r, 2000));
  return { n: currentCards.length };
}
"""

# la sorte d'une carte, vue de l'exterieur (la meme avant et apres la ligne 98)
COMMUN = r"""
const sorteDe = c => {
  if(!c) return null;
  const f = c.forme || '', tid = String(c.themeId || '');
  if(/^(av_escale_fin|av_jalon|av_fin_a1|pp_fin)$/.test(f)) return 'fin';
  if(f === 'conv_arret') return 'conv';
  if(/^(scene_arret|theme_arret|pp_scene)$/.test(f)) return 'images';
  if(c.mode !== 'phrase') return 'cartes';
  if(tid.indexOf('son_') === 0) return 'grammaire';
  if(tid.indexOf('rp_') === 0 || c.rpTableau) return (/^(rp_article|rp_pluriel)$/.test(f) || c.rpType === 'genre' || c.rpType === 'pluriel') ? 'grammaire' : 'cartes';
  if(f === 'gram' || c.gramTableau || c.avTableau || c.fcFeuille) return 'grammaire';
  return 'phrases';
};
const nu = s => String(s || '').toLowerCase().normalize('NFC').replace(/[¿?¡!.,;:«»"()]/g, ' ')
  .replace(/^\s*(el|la|los|las|un|una|der|die|das|den|dem|ein|eine|the|o|os|as)\s+/, '').replace(/\s+/g, ' ').trim();
const motVu = c => {
  if(!c) return null;
  if(c.mode !== 'phrase'){ const w = c.word; const m = Array.isArray(w) ? w[0] : (w && (w.infinitif || w.mot)) || ''; return m ? nu(m) : null; }
  if(c.cible || c.forme === 'pp_tableau' || c.av) return null;
  if(String(c.themeId || '').indexOf('rp_') === 0 && c.phrase && c.phrase.de){ const k = nu(c.phrase.de); return k.split(' ').length <= 2 ? k : null; }
  if(c.gramTableau && c.ex && c.ex.sens) return nu(c.ex.question);
  return null;
};
"""

ETAPE = r"""
async ([etat]) => {
""" + COMMUN + r"""
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const P = SEANCE_PARTS;
  if(!P || P.paquet !== currentCards) return { fin: 'plus de seance' };
  const i = currentFlashcard, c = currentCards[i];
  if(!c) return { fin: 'fin du paquet' };
  const segs = segmentsSeance(P.paquet, P.parts);
  const k = segs.findIndex(s => i >= s.debut && i < s.debut + s.n);
  const barre = k >= 0 ? segs[k].p : null;
  const sorte = sorteDe(c);
  const w = c.word, txt = c.mode !== 'phrase' ? (Array.isArray(w) ? w[0] : (w && (w.infinitif || w.mot)) || '') : (c.ex ? c.ex.question : c.phrase ? c.phrase.de : c.forme);
  const out = { i, len: currentCards.length, barre, rangBarre: k, sorte, forme: c.forme || c.mode, txt: String(txt || '').slice(0, 44),
                mot: motVu(c), cle: c.themeId + ':' + c.index, segs: segs.map(s => s.p) };
  if(/^(scene_arret|theme_arret|conv_arret|pp_scene)$/.test(c.forme || '')){ out.fin = 'images'; return out; }
  if(k > 0 && !etat.horloge){ window.__decalage += 12 * 60000; out.horloge = true; }
  if(c.mode !== 'phrase' && c.word){
    if(!etat.encore && etat.motsJuges >= 1){ reviewAgain(); out.geste = 'Encore'; }
    else { reviewGood(); out.geste = 'Je savais'; }
    await pause(1700);
  } else {
    try{ if(c.av) marquerCarteA1V(c); }catch(e){}
    let juste = true;
    if(c.cible && c.phrase && !etat.phraseRatee && !c.prepaDictee){ juste = false; out.geste = 'phrase ratee'; }
    try{ if(c.cible){ repondrePhrase(c, juste); noterPhraseRatee(c, juste); } }catch(e){}
    nextFlashcard(); await pause(500);
  }
  return out;
}
"""

FORCER_CONV = r"""
async ([avecConv]) => {
  const P = SEANCE_PARTS;
  if(avecConv && !P.paquet.some(c => c && c.forme === 'conv_arret')){
    const conv = { mode: 'phrase', forme: 'conv_arret', cible: null, themeId: 'conv_test', index: 0, word: '', phrase: null };
    P.paquet.push(conv); P.parts.set(conv, 'conv');
  }
  // une carte au milieu de la premiere partie, pour voir une partie en cours
  currentFlashcard = Math.max(1, Math.min(3, P.paquet.length - 1));
  try{ GROUPES_SEANCE.forEach(g => PASSAGES_VUS.add(g)); }catch(e){}
  loadFlashcard();
  await new Promise(r => setTimeout(r, 1200));
  const segs = segmentsSeance(P.paquet, P.parts).map(s => s.p);
  const noms = Array.from(document.querySelectorAll('#seancePartsNoms > *')).map(e => ({ t: e.textContent, deborde: e.scrollWidth > e.clientWidth + 1 }));
  return { segs, noms };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--port", type=int, default=8828)
    ap.add_argument("--niveaux", default="A1,A2")
    ap.add_argument("--langues", default="de,es")
    ap.add_argument("--attendu", choices=["apres", "avant"], default="apres")
    ap.add_argument("--captures", default="")
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

    def ouvrir(nav, langue, niv, theme="light", ui="fr", largeur=390, hauteur=844):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": largeur, "height": hauteur}, service_workers="block")
        page = ctx.new_page()
        err = []
        page.on("pageerror", lambda e: err.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        page.goto("http://127.0.0.1:%d/index.html?apprendre=%s" % (a.port, langue))
        page.wait_for_load_state("networkidle"); page.wait_for_timeout(1200)
        page.evaluate(SEMER, [niv])
        page.evaluate("([th, ui]) => { try{ if(ui !== getUiLang()) setUiLang(ui); }catch(e){} try{ applyAppTheme(th); }catch(e){} }", [theme, ui])
        page.wait_for_timeout(500)
        return ctx, page, err

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for langue in a.langues.split(","):
            for niv in a.niveaux.split(","):
                ctx, page, err = ouvrir(nav, langue, niv)
                page.evaluate(OUVRIR)
                etat = {"encore": False, "phraseRatee": False, "horloge": False, "motsJuges": 0}
                montres, mauvaises, doublons, reculs, retours = [], 0, 0, 0, 0
                vus_mots, vus_cles, rang_max, segs0 = {}, set(), -1, None
                for _ in range(160):
                    e = page.evaluate(ETAPE, [etat])
                    if e.get("fin") and not e.get("sorte"):
                        break
                    if segs0 is None:
                        segs0 = e["segs"]
                    if e.get("geste") == "Encore":
                        etat["encore"] = True
                    if e.get("geste") == "phrase ratee":
                        etat["phraseRatee"] = True
                    if e.get("horloge"):
                        etat["horloge"] = True
                    if e.get("sorte") == "cartes" and e.get("geste") in ("Encore", "Je savais"):
                        etat["motsJuges"] += 1
                    marque = []
                    revenue = e["cle"] in vus_cles and e["sorte"] == "cartes"
                    if revenue:
                        retours += 1
                    vus_cles.add(e["cle"])
                    if e["sorte"] not in ("fin",) and e["barre"] and e["sorte"] != e["barre"] and not (e["sorte"] == "cartes" and e["barre"] == "revisions"):
                        mauvaises += 1; marque.append("SORTE %s SOUS %s" % (e["sorte"], e["barre"]))
                    if e["mot"] and not revenue:
                        if e["mot"] in vus_mots and vus_mots[e["mot"]] != e["cle"] + e["forme"]:
                            doublons += 1; marque.append("DOUBLON")
                        vus_mots.setdefault(e["mot"], e["cle"] + e["forme"])
                    if e["rangBarre"] is not None and e["rangBarre"] < rang_max:
                        reculs += 1; marque.append("LA BARRE RECULE")
                    rang_max = max(rang_max, e["rangBarre"] if e["rangBarre"] is not None else -1)
                    montres.append("   %3d/%-3d %-10s %-10s %-14s « %s »%s%s" % (e["i"], e["len"], e["barre"], e["sorte"], e["forme"], e["txt"],
                                   ("  [%s]" % e["geste"]) if e.get("geste") else "", ("   <-- " + ", ".join(marque)) if marque else ""))
                    if e.get("fin"):
                        break
                print("== %s %s : barre %s" % (langue, niv, segs0), flush=True)
                for l in montres:
                    if "<--" in l or "[Encore]" in l or "phrase ratee" in l:
                        print(l, flush=True)
                print("   %d cartes montrees ; %d d'une autre sorte que la partie allumee, %d doublons de mot, %d reculs de la barre, %d retours (Encore, 10 min)"
                      % (len(montres), mauvaises, doublons, reculs, retours), flush=True)
                if err:
                    print("   erreurs JavaScript : %s" % err[:3], flush=True)
                if a.attendu == "apres":
                    if mauvaises: fautes.append("%s %s : %d cartes d'une autre sorte que la partie allumee" % (langue, niv, mauvaises))
                    if doublons: fautes.append("%s %s : %d doublons de mot" % (langue, niv, doublons))
                    if reculs: fautes.append("%s %s : la barre recule %d fois" % (langue, niv, reculs))
                    if not montres: fautes.append("%s %s : aucune carte montree" % (langue, niv))
                ctx.close()
        if a.captures:
            os.makedirs(a.captures, exist_ok=True)
            for avec in (False, True):
                for theme in ("light", "dark"):
                    ctx, page, err = ouvrir(nav, "de", "A2", theme, "fr", 375, 812)
                    page.evaluate(OUVRIR)
                    r = page.evaluate(FORCER_CONV, [avec])
                    nom = "barre-%d-parties-%s.png" % (len(r["segs"]), "nuit" if theme == "dark" else "jour")
                    page.screenshot(path=os.path.join(a.captures, nom))
                    print("capture %s : %s %s" % (nom, r["segs"], [x["t"] for x in r["noms"]]), flush=True)
                    ctx.close()
            for ui, appris in (("fr", "de"), ("en", "de"), ("tr", "de"), ("uk", "de"), ("fa", "de"), ("ar", "de"), ("pt", "de"),
                               ("pl", "de"), ("ru", "de"), ("de", "es"), ("es", "de")):
                ctx, page, err = ouvrir(nav, appris, "A2", "light", ui, 375, 812)
                page.evaluate(OUVRIR)
                r = page.evaluate(FORCER_CONV, [True])
                debords = [x["t"] for x in r["noms"] if x["deborde"]]
                nom = "barre-5-parties-%s.png" % ui
                try:
                    zone = page.evaluate("() => { const b = document.getElementById('seanceParts').getBoundingClientRect(), n = document.getElementById('seancePartsNoms').getBoundingClientRect(); return {x: 0, y: Math.max(0, b.top - 60), width: 375, height: (n.bottom - b.top) + 80}; }")
                    page.screenshot(path=os.path.join(a.captures, nom), clip=zone)
                except Exception:
                    page.screenshot(path=os.path.join(a.captures, nom))
                print("capture %s : %s%s" % (nom, [x["t"] for x in r["noms"]], ("  DEBORDE : %s" % debords) if debords else ""), flush=True)
                if debords and a.attendu == "apres":
                    fautes.append("nom de partie trop large a 375 px en %s : %s" % (ui, debords))
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
