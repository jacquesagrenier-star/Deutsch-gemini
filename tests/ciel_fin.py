# -*- coding: utf-8 -*-
"""La constellation de l'ecran de fin, pour tout le monde (decisions du 8 nov. 2026).

    python tests/ciel_fin.py                       (de et es, plus l'arabe en interface)
    python tests/ciel_fin.py --captures DOSSIER    (captures 360 x 780, clair et nuit)
    python tests/ciel_fin.py --largeur DOSSIER     (la phrase de distance la plus longue, 320 et 360 px, toutes les langues d'interface)

Sur un navigateur vierge, donc un compte qui n'est PAS admin (essai seance_legere coupe) :
  - Premiers pas : la Grande Ourse, le trait, l'etoile qui s'allume sans plein ecran ;
  - A1 voyage : les Gemeaux, « Encore une seance », l'etoile filante des la 2e seance seulement ;
  - la fin d'une etape : le plein ecran, une seule fete, puis le trait vers l'etoile suivante ;
  - le plus charge (9 etoiles sur 12) : les noms ne se chevauchent ni ne se coupent ;
  - le son : rien en transit sans son.
Il appelle les fonctions de la page. Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours
(~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("PARCOURS_PORT", "8796"))


class Silencieux(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass


PREPARER = r"""
([zero]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1');
  localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(zero) localStorage.setItem(NIVEAU_DECLARE_KEY, 'zero');
}
"""

MESURE = r"""
async ([cas]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const finir = () => { currentFlashcard = currentCards.length; return showFlashcardEnd(); };
  const lire = () => {
    const el = document.getElementById('finCiel'), v = el && !el.classList.contains('hidden') && el.offsetHeight > 0;
    if(!v) return { ciel: false, anneau: !document.getElementById('flashEndAnneau').classList.contains('hidden') };
    const q = x => el.querySelector(x);
    const svg = q('.fc-cst').getBoundingClientRect();
    const noms = [...el.querySelectorAll('.fc-nom')].map(x => { const r = x.getBoundingClientRect(); return { t: x.textContent, l: r.left, r: r.right, h: r.top, b: r.bottom }; });
    let chev = 0, coup = 0;
    noms.forEach((a, i) => {
      if(a.l < svg.left || a.r > svg.right || a.h < svg.top || a.b > svg.bottom) coup++;
      noms.slice(i + 1).forEach(b => { if(a.l < b.r && b.l < a.r && a.h < b.b && b.h < a.b) chev++; });
    });
    const enc = document.getElementById('encoreNeufsBtn');
    return { ciel: true, cnom: q('.fc-cnom').textContent, compte: q('.fc-compte').textContent, proch: q('.fc-proch-t').textContent, dist: q('.fc-proch-d').textContent,
             titre: q('.fc-titre').textContent, phrase: q('.fc-phrase').textContent, pastille: !!q('.fc-fois'), anneauFin: document.getElementById('flashEndAnneau').textContent,
             noms: noms.map(n => n.t).join(','), chev, coup, filante: !!q('.fc-filante'), trait: !!q('.fc-nouveau'), neuve: !!q('.fc-neuve'),
             bouton: enc && el.contains(enc) ? enc.textContent : '(hors du ciel)', hauteur: Math.round(el.getBoundingClientRect().height), joue: el.classList.contains('fc-joue') };
  };
  const legere = essaiActif('seance_legere');
  let r = {}, note = '';
  const pp = (p, prec) => { ecrirePremiersPas({ a: true, p }); if(prec) etoileEcrire(CIEL_PART_KEY, prec); };
  const sansPP = () => localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  await chargerPremiersPas(); await chargerCiel();
  if(cas === 'pp_chemin'){
    const seq = sequencePremiersPas(), p = seq.findIndex(x => x.jourPP === 1) + 6;
    pp(p, { g:'premiers_pas', n:1, p:.1 });
    await ouvrirPremiersPas(); await pause(700); finir(); await pause(200); r = lire();
  }
  if(cas === 'pp_etoile'){
    const seq = sequencePremiersPas(), p = seq.findIndex(x => x.jourPP === 1) + 2;
    pp(p, { g:'premiers_pas', n:0, p:.9 });
    await ouvrirPremiersPas(); await pause(700); finir(); await pause(200); r = lire();
    note = 'plein ecran : ' + !!document.querySelector('.fete-etoile');
  }
  if(cas === 'a1_deux_seances'){
    sansPP();
    await ouvrirSeanceDuJour(); await pause(900);
    note = 'taille ' + currentCards.length + ' / legere ' + legere;
    finir(); await pause(300); const un = lire();
    const ouvert = currentCards;
    document.getElementById('encoreNeufsBtn').click();
    document.getElementById('encoreNeufsBtn').click();
    for(let k = 0; k < 60 && currentCards === ouvert; k++) await pause(100);
    await pause(700);
    note += ' / encore : ' + currentCards.length + ' cartes, barre : ' + !document.getElementById('seanceParts').classList.contains('hidden');
    finir(); await pause(300); const deux = lire();
    return { cas, un, r: deux, note, legere, seances: seancesFiniesAujourdhui(), attendu: tf('legere_fin_n', { n: 2 }), une: t('legere_fin_une') };
  }
  if(cas === 'a1_etoile'){
    sansPP();
    await ouvrirSeanceDuJour(); await pause(900);
    etoileEcrire(ETOILE_ATTENTE_KEY, { g: 'a1_escales', n: CIEL_AV.n, total: 12, id: CIEL_AV.lieu.id || '', s: CIEL_AV.lieu.s || '', j: getTodayStr() });
    finir(); await pause(1500); r = lire();
    const ov = !!document.querySelector('.fete-etoile');
    fermerFeteEtoile();
    await pause(1500);
    note = 'plein ecran : ' + ov + ' ; trait joue apres fermeture : ' + document.getElementById('finCiel').classList.contains('fc-joue');
  }
  if(cas === 'a1_charge'){
    sansPP();
    const s = lireA1Voyage(); s.a = true; s.e = 9; ecrireA1Voyage(s);
    await ouvrirSeanceDuJour(); await pause(900);
    note = 'etape ' + (CIEL_AV ? CIEL_AV.n : 'aucune');
    finir(); await pause(300); r = lire();
  }
  if(cas === 'compte_objectif'){
    sansPP();
    localStorage.setItem(DAILY_GOAL_STORAGE_KEY, '50');
        const home = { anneau: getComputedStyle(document.getElementById('spAnneau')).display, reglage: getComputedStyle(document.getElementById('reglageObjectif')).display };
    await ouvrirSeanceDuJour(); await pause(900);
    const taille = currentCards.length, tailleCalc = tailleSeance();
    let paliers = 0;
    for(let k = 0; k < 70; k++){ if(recordDailyActivity() > 0) paliers++; }
    note = JSON.stringify({ home, taille, tailleCalc, paliers, serie: getStreakCount(), compte: getDailyActivityCount(), compteur: document.getElementById('flashCounter').textContent, objectifGarde: localStorage.getItem(DAILY_GOAL_STORAGE_KEY) });
    finir(); await pause(300); r = lire();
    r.objectifFin = document.getElementById('flashEndObjectif').classList.contains('hidden') ? '' : document.getElementById('flashEndObjectif').textContent;
  }
  if(cas === 'a2_tableau'){
    sansPP();
    localStorage.setItem(NIVEAU_SEANCE_KEY, 'A2');
    await ouvrirSeanceDuJour(); await pause(900);
    note = 'niveau ' + niveauSeance() + ', ciel_av ' + !!CIEL_AV;
    finir(); await pause(2500);
    const f = document.getElementById('finTableau');
    return { cas, r: { ciel: false, sansCiel: !lire().ciel, tableau: !!f, texte: f ? f.textContent : '', anneau: document.getElementById('flashEndAnneau').textContent, mot: document.getElementById('flashEndObjectif').textContent, bouton: document.getElementById('encoreNeufsBtn').textContent }, note, legere };
  }
  if(cas === 'a2_deux_seances'){
    // Sans ciel (A2 et plus) : la meme phrase sous le tableau, et l'anneau de fin sans « ×2 ».
    sansPP();
    localStorage.setItem(NIVEAU_SEANCE_KEY, 'A2');
    await ouvrirSeanceDuJour(); await pause(900);
    finir(); await pause(300);
    const anneau = () => document.getElementById('flashEndAnneau').textContent;
    const mot = () => document.getElementById('flashEndObjectif').textContent;
    const un = { mot: mot(), anneau: anneau() };
    const ouvert = currentCards;
    document.getElementById('encoreNeufsBtn').click();
    for(let k = 0; k < 60 && currentCards === ouvert; k++) await pause(100);
    await pause(700);
    finir(); await pause(300);
    return { cas, r: { ciel: false, un, mot: mot(), anneau: anneau() }, attendu: tf('legere_fin_n', { n: 2 }), une: t('legere_fin_une'), note, legere };
  }
  if(cas === 'dictee_cartes'){
    // La dictee de la v1141, jouee en cartes : elle compte dans le compte du jour, sans palier ni fete, meme objectif bas.
    sansPP();
    localStorage.setItem(DAILY_GOAL_STORAGE_KEY, '5');
    let fetes = 0;
    const vraie = triggerDailyGoalCelebration;
    triggerDailyGoalCelebration = function(m){ fetes++; return vraie(m); };
    const liste = [0, 1, 2].map(i => ({ dictation: true, topic: 'x', answers: [], question: '',
      carteDictee: { word: ['Haus' + i, 'das', 'maison'], mode: 'nomen', themeId: 't', index: i } }));
    activeExercises = liste;
    exerciseKickerKey = 'kicker_dictation_exercise';
    exerciseJeuNom = '';
    const possible = serieEnCartesPossible(liste, exerciseKickerKey);
    ouvrirSerieEnCartes(); await pause(500);
    const forme = currentCards[0] && currentCards[0].forme;
    const avant = getDailyActivityCount();
    let retours = 0;
    for(let k = 0; k < 40; k++){ if(repondrePhrase(currentCards[k % 3], true) > 0) retours++; }
    const compte = getDailyActivityCount() - avant;
    finirSerieEnCartes(); await pause(300);
    showScreen('home'); await pause(800);
    triggerDailyGoalCelebration = vraie;
    return { cas, r: { ciel: false, possible, forme, retours, fetes, compte }, note: 'objectif garde ' + localStorage.getItem(DAILY_GOAL_STORAGE_KEY), legere };
  }
  if(cas === 'son'){
    sansPP();
    await ouvrirSeanceDuJour(); await pause(900);
    finir(); await pause(400);
    const avec = !!cristalBus;
    arreterCristal();
    SON_COUPE = true;
    jouerCielFin(); await pause(100);
    const sans = !!cristalBus;
    note = 'son normal : ' + avec + ' ; transit sans son : ' + sans;
    SON_COUPE = false;
    r = lire();
  }
  return { cas, r, note, legere };
}
"""

LARGEUR = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas(); await chargerCiel();
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  const feteLabels = () => {
  // Le plein ecran de la nouvelle etoile : chaque etoile de chaque constellation, le nom et la distance dans le dessin,
  // sans toucher une etoile ni un trait allume.
  const zone = document.createElement('div');
  zone.style.cssText = 'position:fixed;left:0;top:0;width:375px;height:372px;visibility:hidden;';
  document.body.appendChild(zone);
  let total = 0, hors = 0, coupe = 0, large = 0, deux = 0; const exemples = [];
  const lg = getUiLang(), W = CIEL.boite[0], H = CIEL.boite[1];
  Object.entries(CIEL.constellations).forEach(([cle, c]) => c.etoiles.forEach((e, n) => {
    const nom = nomEtoileAffiche(e, lg), dist = phraseDistanceEtoile(e), fin = n === c.etoiles.length - 1;
    zone.innerHTML = svgConstellationFete(c, n, fin, nom, dist);
    const ne = zone.querySelector('.fe-ne-nom');
    ne.textContent = nom;
    const ls = lignesDistanceEtoile(dist); if(ls.length > 1) deux++;
    zone.querySelectorAll('.fe-ne-dist').forEach((x, k) => { x.textContent = ls[k] || ''; });
    const b = zone.querySelector('.fe-nom-et').getBBox();
    total++; large = Math.max(large, Math.round(b.width));
    const bb = [b.x, b.y, b.x + b.width, b.y + b.height];
    const lit = i => i <= n;
    let touche = 0;
    c.traits.filter(([i, j]) => lit(i) && lit(j)).forEach(([i, j]) => {
      for(let k = 0; k <= 40; k++){ const x = c.etoiles[i].x + (c.etoiles[j].x - c.etoiles[i].x) * k / 40, y = c.etoiles[i].y + (c.etoiles[j].y - c.etoiles[i].y) * k / 40;
        if(x > bb[0] && x < bb[2] && y > bb[1] && y < bb[3]){ touche++; break; } }
    });
    c.etoiles.forEach((p, j) => { if(j === n) return; const r = p.r * (lit(j) ? 3 : 1.4) + 1, nx = Math.min(Math.max(p.x, bb[0]), bb[2]), ny = Math.min(Math.max(p.y, bb[1]), bb[3]); if(Math.hypot(nx - p.x, ny - p.y) < r) touche++; });
    const h = bb[0] < 0 || bb[2] > W || bb[1] < 0 || bb[3] > H;
    if(h) hors++;
    if(touche) coupe++;
    if((h || touche) && exemples.length < 6) exemples.push(cle + ' ' + n + ' ' + nom + ' x=' + Math.round(bb[0]) + '-' + Math.round(bb[2]) + ' t=' + touche);
  }));
  zone.remove();
  return { total, hors, coupe, large, deux, exemples };
  };
  // Les vraies distances d'abord (le plein ecran), puis la phrase la plus longue partout (l'ecran de fin et le plein ecran).
  const reel = feteLabels();
  Object.values(CIEL.constellations).forEach(c => c.etoiles.forEach(e => { e.affiche = 1100; e.environ = true; }));
  const finir = () => { currentFlashcard = currentCards.length; return showFlashcardEnd(); };
  await ouvrirSeanceDuJour(); await pause(900);
  finir(); await pause(300);
  const ouvert = currentCards;
  document.getElementById('encoreNeufsBtn').click();
  for(let k = 0; k < 60 && currentCards === ouvert; k++) await pause(100);
  await pause(700);
  finir(); await pause(400);
  const el = document.getElementById('finCiel');
  if(!el || el.classList.contains('hidden')) return { faute: 'pas de ciel' };
  const q = x => el.querySelector(x), bord = el.getBoundingClientRect();
  const lignes = n => { const g = document.createRange(); g.selectNodeContents(n); return new Set([...g.getClientRects()].map(x => Math.round(x.top))).size; };
  const dedans = n => { const g = document.createRange(); g.selectNodeContents(n); const b = g.getBoundingClientRect(); return b.left >= bord.left + 6 && b.right <= bord.right - 6; };
  const enc = document.getElementById('encoreNeufsBtn').getBoundingClientRect();
  const ecran = {
    distance: q('.fc-proch-d').textContent, l_distance: lignes(q('.fc-proch-d')), dans_distance: dedans(q('.fc-proch-d')),
    titre: q('.fc-titre').textContent, l_titre: lignes(q('.fc-titre')), dans_titre: dedans(q('.fc-titre')), dans_phrase: dedans(q('.fc-phrase')),
    debord: document.documentElement.scrollWidth > window.innerWidth, hauteur: Math.round(bord.height), bouton_bas: Math.round(enc.bottom - bord.top), bouton_dans: enc.bottom <= bord.bottom + 1
  };
  return { ecran, fete: feteLabels(), reel };
}
"""

LANGUES_LARGEUR = [("de", u) for u in ("fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru")] + [("es", "de")]

CAS = ["pp_chemin", "pp_etoile", "a1_deux_seances", "a1_etoile", "a1_charge", "compte_objectif", "dictee_cartes", "a2_tableau", "a2_deux_seances", "son"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captures")
    ap.add_argument("--largeur", help="seulement la largeur : l'ecran de fin et le plein ecran, toutes les langues ; DOSSIER des captures")
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Silencieux, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = 0
    SCENARIOS = [("de", "fr", "light"), ("de", "ar", "dark"), ("es", "fr", "dark")]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, ui in (LANGUES_LARGEUR if a.largeur else []):
                for largeur, hauteur in ((320, 568), (360, 780)):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": largeur, "height": hauteur}, service_workers="block")
                    page = ctx.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.evaluate(PREPARER, [False])
                    page.evaluate("([l]) => localStorage.setItem(UI_LANG_KEY, l)", [ui])
                    page.reload()
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1200)
                    try:
                        res = page.evaluate(LARGEUR)
                    except Exception as e:
                        fautes += 1
                        print("%s %d ERREUR %s" % (ui, largeur, str(e).split("\n")[0][:200]), flush=True)
                        ctx.close()
                        continue
                    e = res.get("ecran") or {}
                    f = res.get("fete") or {}
                    ok = e and e["dans_distance"] and e["dans_titre"] and e["dans_phrase"] and not e["debord"] and e["bouton_dans"] and not f["hors"] and not res["reel"]["hors"]
                    if not ok:
                        fautes += 1
                    print("%s %d %s %s" % (ui, largeur, "ok" if ok else "FAUTE", json.dumps(res, ensure_ascii=False)[:700]), flush=True)
                    if a.largeur:
                        os.makedirs(a.largeur, exist_ok=True)
                        page.evaluate("() => { document.getAnimations().forEach(x => { const t = x.effect.getComputedTiming(); if(t.iterations !== Infinity){ try{ x.finish(); }catch(e){} } }); const f = document.getElementById('finCiel'); if(f) f.scrollIntoView({block:'start'}); }")
                        page.wait_for_timeout(300)
                        page.screenshot(path=os.path.join(a.largeur, "%s-%s-%d.png" % (appris, ui, largeur)))
                    ctx.close()
            for appris, ui, theme in ([] if a.largeur else SCENARIOS):
                print("== apprend %s, interface %s, %s" % (appris, ui, theme), flush=True)
                for cas in CAS:
                    if ui != "fr" and cas in ("son",):
                        continue
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 780}, service_workers="block")
                    page = ctx.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    url = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else "")
                    page.goto(url)
                    page.wait_for_load_state("networkidle")
                    page.evaluate(PREPARER, [cas.startswith("pp")])
                    page.evaluate("([l]) => localStorage.setItem(UI_LANG_KEY, l)", [ui])
                    page.reload()
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(1200)
                    page.evaluate("([t]) => document.body.setAttribute('data-theme', t)", [theme])
                    try:
                        res = page.evaluate(MESURE, [cas])
                    except Exception as e:
                        fautes += 1
                        print("  %-16s ERREUR %s" % (cas, str(e).split("\n")[0][:200]), flush=True)
                        ctx.close()
                        continue
                    r = res.get("r") or {}
                    ok = r.get("ciel") and not r.get("chev") and not r.get("coup") and res.get("legere")
                    if cas == "a2_tableau":
                        ok = r.get("sansCiel") and r.get("tableau")
                    if cas == "dictee_cartes":
                        ok = r.get("possible") and r.get("forme") == "dictee_mot" and r.get("compte") == 40 and not r.get("retours") and not r.get("fetes")
                    if cas == "a1_deux_seances":
                        ok = ok and res["un"].get("ciel") and not res["un"].get("filante") and r.get("filante")
                        ok = ok and res["un"].get("titre") == res.get("une") and r.get("titre") == res.get("attendu")
                        ok = ok and not r.get("pastille") and "×" not in (r.get("anneauFin") or "")
                    if cas == "a2_deux_seances":
                        ok = r["un"]["mot"] == res.get("une") and r.get("mot") == res.get("attendu") and "×" not in r.get("anneau", "")
                    if not ok:
                        fautes += 1
                    print("  %-16s %s %s" % (cas, "ok" if ok else "FAUTE", json.dumps({k: v for k, v in res.items() if k not in ("cas", "legere")}, ensure_ascii=False)[:900]), flush=True)
                    if erreurs:
                        print("      erreurs JS :", sorted(set(erreurs))[:4], flush=True)
                    if a.captures:
                        os.makedirs(a.captures, exist_ok=True)
                        page.evaluate("() => { document.getAnimations().forEach(x => { const t = x.effect.getComputedTiming(); if(t.iterations !== Infinity){ try{ x.finish(); }catch(e){} } }); const f = document.getElementById('finCiel'); if(f) f.scrollIntoView({block:'start'}); }")
                        page.wait_for_timeout(300)
                        page.screenshot(path=os.path.join(a.captures, "%s-%s-%s-%s.png" % (appris, ui, theme, cas)))
                    ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not fautes else "%d cas en defaut" % fautes))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
