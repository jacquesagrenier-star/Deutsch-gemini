# -*- coding: utf-8 -*-
"""Les reperes de la seance : les noms sous la barre et un paysage par partie (choix de Jacques, 10 nov. 2026).

    python tests/reperes_seance.py                     (de et es)
    python tests/reperes_seance.py --captures DOSSIER

Sur un navigateur vierge, sans compte. A 320 x 568 et 360 x 780, clair, nuit, RTL :
  - les noms sous la barre, un par partie, ne debordent pas, meme a six parties dans la langue la plus longue ;
  - le paysage suit la partie (sept paysages, le son du jour compris), et il s'arrete au-dessus des boutons du verso ;
  - le fond de tout l'ecran prend la couleur de la partie, et le texte de l'en-tete y reste lisible (4,5:1 au moins) ;
  - la barre : la partie en cours en encre (blanc la nuit), les parties faites en vert avec le crochet ;
  - aucun nom sous la barre ne laisse une lettre seule sur sa ligne (le « s » de Revisions lu comme un 5) ;
  - la carte reste au-dessus de lui ; aucun paysage sur l'accueil ni a la fin de la seance ;
  - l'ecran de passage montre deja le paysage de la partie qui vient ;
  - sur une scene de la seance, la bande du repere est au-dessus du cadre, et disparait en quittant la scene ;
  - la scene, le theme et la scene de fin d'etape de Premiers pas : la bande dans la couleur de la partie, et la page en
    cadre qui prend le fond de la seance (&fond=, pose par themes/verre.js) ; hors seance (Explorer les scenes, Tout le
    contenu), la page garde son fond ;
  - 11 nov. (Jacques, iPhone) : la fleche du rond claire sur un fond fonce des sa premiere image, foncee sur un fond
    clair ; une carte revenue apres la scene dans une partie « Revisions », pas « Scene » ; le cadre plein ecran
    (et ses marges d'encoche) dans le fond de la partie, aussi au retour des reglages.
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
PORT = int(os.environ.get("REPERES_PORT", "8806"))

POSER = """
([pp]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(pp){ localStorage.setItem(NIVEAU_DECLARE_KEY, 'zero'); localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true, k: 0 })); }
  else localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
}
"""

MESURE = r"""
async ([cas]) => {
const LIRE_FOND = () => {
  const fd = document.getElementById('seanceFond');
  const vis = !!(fd && !fd.classList.contains('hidden') && getComputedStyle(fd).display !== 'none');
  if(!vis) return { fond: false };
  const lum = ([r,g,b]) => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
  const rapp = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); };
  const st = (fd.style.background.match(/rgb\(\d+, \d+, \d+\)/g) || []).map(c => c.match(/\d+/g).map(Number));
  if(st.length < 2) return { fond: true, faute: 'degrade illisible' };
  const H = innerHeight, rep = [];
  const els = [document.getElementById('flashKicker'), document.getElementById('flashThemeTitle'), ...document.querySelectorAll('#seancePartsNoms > *')].filter(x => x && x.offsetParent && x.textContent.trim());
  els.forEach(e => { const r = e.getBoundingClientRect(), f = Math.max(0, Math.min(1, (r.top + r.height / 2) / H)), bg = st[0].map((v, i) => v + (st[1][i] - v) * f), c = getComputedStyle(e).color.match(/[\d.]+/g).map(Number);
                     rep.push([Math.round(rapp(c, bg) * 10) / 10, e.textContent.trim().slice(0, 18)]); });
  rep.sort((a, b) => a[0] - b[0]);
  const box = document.getElementById('seanceParts');
  const fait = box ? [...box.querySelectorAll('i.fait')].map(i => getComputedStyle(i).backgroundColor)[0] || null : null;
  const ici = box ? ((getComputedStyle(box.querySelector('i.ici') || box).backgroundImage.match(/rgb\(\d+, \d+, \d+\)/) || [null])[0]) : null;
  return { fond: true, haut: 'rgb(' + st[0].join(',') + ')', pire: rep[0] || null, fait, ici };
};

  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas();
  const lire = () => {
    const box = document.getElementById('seanceParts'), n = document.getElementById('seancePartsNoms'), p = document.getElementById('seancePaysage'), W = innerWidth;
    const svg = p && p.querySelector('svg'), vis = !!(p && !p.classList.contains('hidden') && getComputedStyle(p).display !== 'none');
    const noms = n ? [...n.children] : [];
    const lignes = x => { const g = document.createRange(); g.selectNodeContents(x); return new Set([...g.getClientRects()].map(q => Math.round(q.top))).size; };
    const debord = noms.filter(x => { const r = x.getBoundingClientRect(); return r.right > W - 2 || r.left < 2 || x.scrollWidth > x.clientWidth + 1; }).map(x => x.textContent);
    return { noms: noms.map(x => x.textContent), ici: noms.filter(x => x.tagName === 'B').map(x => x.textContent), barres: box ? box.children.length : 0, maxLignes: noms.length ? Math.max(...noms.map(lignes)) : 0, debord,
             paysage: vis, largeurPay: svg ? Math.round(svg.getBoundingClientRect().width) : 0, marque: typeof PAYSAGE_MONTRE === 'undefined' ? null : PAYSAGE_MONTRE, pageDebord: document.documentElement.scrollWidth > W, fond: LIRE_FOND() };
  };
  if(cas === 'pp'){ await ouvrirPremiersPas(); await pause(900); return { pp: lire(), titre: document.getElementById('flashThemeTitle').textContent }; }
  await ouvrirSeanceDuJour(); await pause(1500);
  const out = { depart: lire(), parts: SEANCE_PARTS ? segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).map(s => s.p + ':' + s.n) : null };
  // le verso : le paysage s'arrete au-dessus des boutons
  let k = currentCards.findIndex((c, i) => i > 0 && c.mode !== 'phrase');
  if(k >= 0){ currentFlashcard = k; PASSAGES_VUS.add(SEANCE_PARTS.parts.get(currentCards[k])); segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).forEach(s => PASSAGES_VUS.add(s.p)); loadFlashcard(); await pause(500); try{ flipCard(); }catch(e){} await pause(700); }
  const act = document.getElementById('flashcardActions'), svg = document.querySelector('#seancePaysage svg'), carte = document.getElementById('flashcard');
  const a = act && act.getBoundingClientRect(), s = svg && svg.getBoundingClientRect(), c = carte && carte.getBoundingClientRect();
  out.verso = { actionsVisibles: !!(a && a.height > 0 && !act.classList.contains('hidden')), boutonsHaut: a ? Math.round(a.top) : null, paysageBas: s ? Math.round(s.bottom) : null, carteBas: c ? Math.round(c.bottom) : null, H: innerHeight,
                sousBoutons: !!(a && s && a.height > 0 && s.bottom > a.top + 1), etat: lire() };
  window.__versoPret = true;
  return out;
}
"""

SIX = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1200);
  const box = document.getElementById('seanceParts');
  const pp = ['revisions','lieu','feuille','reperes','scene','theme'];
  const segs = pp.map((p,i) => ({ p, debut: i*3, n: 3 }));
  currentFlashcard = 7;
  dessinerSegmentsSeance(box, segs);
  await pause(120);
  const n = document.getElementById('seancePartsNoms'), W = innerWidth;
  const lignes = x => { const g = document.createRange(); g.selectNodeContents(x); return new Set([...g.getClientRects()].map(q => Math.round(q.top))).size; };
  const sortants = [...n.children].filter(x => { const g = document.createRange(); g.selectNodeContents(x); const r = g.getBoundingClientRect(), c = x.getBoundingClientRect(); return r.left < c.left - 1 || r.right > c.right + 1; }).map(x => x.textContent);
  const seules = [...n.children].filter(x => { const g = document.createRange(); g.selectNodeContents(x); const parLigne = {}; [...g.getClientRects()].forEach(q => { if(q.width > 0){ const k = Math.round(q.top); parLigne[k] = (parLigne[k] || 0) + q.width; } }); return Object.values(parLigne).some(w => w < 9); }).map(x => x.textContent);
  return { noms: [...n.children].map(x => x.textContent), max: Math.max(...[...n.children].map(lignes)), sortants, seules, dir: document.documentElement.dir, large: Math.round(n.getBoundingClientRect().width), page: document.documentElement.scrollWidth > W };
}
"""

PAYSAGES = r"""
async ([k]) => { paysageSeance(k); await new Promise(r => setTimeout(r, 120)); const fd = document.getElementById("seanceFond"); return { marque: PAYSAGE_MONTRE, fond: fd && !fd.classList.contains("hidden") ? fd.style.background.slice(0, 60) : null }; }
"""

PASSAGE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1400);
  const segs = segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts);
  const s = segs[1];
  currentFlashcard = s.debut; loadFlashcard(); await pause(500);
  const pas = document.querySelector('.cp-passage');
  return { passage: !!pas, texte: pas ? pas.innerText.replace(/\n+/g, ' | ') : '', vers: s.p, marque: PAYSAGE_MONTRE, ici: [...document.querySelectorAll('#seancePartsNoms b')].map(x => x.textContent) };
}
"""

SCENE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1400);
  const k = currentCards.findIndex(c => c && c.forme === 'scene_arret');
  if(k < 0) return { faute: 'pas de scene' };
  segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).forEach(s => PASSAGES_VUS.add(s.p));
  currentFlashcard = k; loadFlashcard(); await pause(1500);
  const sec = document.getElementById('sceneSeance'), f = document.getElementById('sceneCadre').getBoundingClientRect(), r = document.getElementById('sceneRepere').getBoundingClientRect();
  const res = { avec: sec.classList.contains('avec-repere'), cadreHaut: Math.round(f.top), repereBas: Math.round(r.bottom), noms: [...document.querySelectorAll('#scenePartsNoms > *')].map(x => x.textContent), ici: [...document.querySelectorAll('#scenePartsNoms b')].map(x => x.textContent), paysageCache: getComputedStyle(document.getElementById('seancePaysage')).display === 'none' };
  window.__sceneOuverte = true;
  return res;
}
"""

SORTIE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  showScreen('home'); await pause(250);
  const p = document.getElementById('seancePaysage');
  const fd = document.getElementById('seanceFond');
  return { accueilCache: (!p || getComputedStyle(p).display === 'none') && (!fd || getComputedStyle(fd).display === 'none'), sansBande: !document.getElementById('sceneSeance').classList.contains('avec-repere') };
}
"""

CADRE = r"""
async ([quoi]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const lireCadre = async () => {
    const f = document.getElementById('sceneCadre');
    for(let i = 0; i < 80; i++){
      try{
        const d = f.contentDocument;
        if(d && d.readyState === 'complete' && d.body && (d.location.href || '').indexOf('about:') !== 0){
          await pause(500);
          const fm = d.getElementById('fondMonde'), w = d.defaultView;
          return { adresseFond: (f.dataset.page || '').indexOf('&fond=') >= 0, fondPose: !!d.getElementById('fondSeance'),
                   fondPage: w.getComputedStyle(d.body).backgroundImage.slice(0, 70), carteCachee: !fm || w.getComputedStyle(fm).display === 'none' };
        }
      }catch(e){}
      await pause(150);
    }
    return { faute: 'cadre non charge' };
  };
  const bande = () => { const b = document.getElementById('sceneRepere'), sec = document.getElementById('sceneSeance');
    return { avec: sec.classList.contains('avec-repere'), fond: getComputedStyle(b).backgroundColor, clair: b.classList.contains('clair'),
             noms: [...document.querySelectorAll('#scenePartsNoms > *')].map(x => x.textContent), ici: [...document.querySelectorAll('#sceneParts i.ici')].length }; };
  if(quoi === 'libre'){ ouvrirSceneLibre('kueche'); await pause(300); const c = await lireCadre(); return { quoi, bande: bande(), cadre: c }; }
  if(quoi === 'theme-libre'){ ouvrirThemeIllustre('familia'); await pause(300); const c = await lireCadre(); return { quoi, bande: bande(), cadre: c }; }
  let forme = quoi === 'theme' ? 'theme_arret' : quoi === 'pp' ? 'pp_scene' : 'scene_arret';
  if(quoi === 'pp'){ await chargerPremiersPas(); await ouvrirPremiersPas(); } else await ouvrirSeanceDuJour();
  await pause(1400);
  let k = currentCards.findIndex(c => c && c.forme === forme);
  if(k < 0 && quoi === 'pp') k = currentCards.findIndex(c => c && c.forme === 'scene_arret');
  if(k < 0) return { quoi, faute: 'pas de carte ' + forme };
  const formeVue = currentCards[k].forme;
  if(typeof SEANCE_PARTS !== 'undefined' && SEANCE_PARTS) segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).forEach(s => PASSAGES_VUS.add(s.p));
  currentFlashcard = k; loadFlashcard(); await pause(600);
  const c = await lireCadre();
  window.__cadrePret = true;
  return { quoi, forme: formeVue, bande: bande(), cadre: c };
}
"""

FLECHE = r"""
async ([quoi]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1400);
  const forme = quoi === 'theme' ? 'theme_arret' : 'scene_arret';
  const k = currentCards.findIndex(c => c && c.forme === forme);
  if(k < 0) return { faute: 'pas de carte ' + forme };
  segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).forEach(s => PASSAGES_VUS.add(s.p));
  currentFlashcard = k; loadFlashcard();
  const f = document.getElementById('sceneCadre');
  let d = null;
  for(let i = 0; i < 80; i++){ try{ d = f.contentDocument; if(d && d.readyState === 'complete' && d.body && d.getElementById('verreBoutonsCss')) break; }catch(e){} await pause(150); }
  if(!d) return { faute: 'cadre' };
  await pause(600);
  const w = d.defaultView;
  // un rond « Continuer » pose au bas de la page, comme apres une reponse, et lu a sa toute premiere image
  const b = d.createElement('button'); b.className = 'suite'; b.textContent = 'Continuer';
  b.style.cssText = 'position:fixed;bottom:12px;left:20px;right:20px;height:54px;z-index:5000';
  // le rond sur le fond de la page (une bande vide, comme le bas d'une page de theme) : il lit la couleur du fond
  const vide = d.createElement('div'); vide.style.cssText = 'position:fixed;left:0;right:0;bottom:0;height:120px;z-index:4999;background:transparent'; d.body.appendChild(vide);
  // dans la scene, une photo brune sous le rond (le sol de l'aeroport, Jacques, 11 nov.)
  if(quoi === 'scene'){ const c = d.createElement('canvas'); c.width = c.height = 16; const x = c.getContext('2d'); x.fillStyle = '#6B4A2E'; x.fillRect(0, 0, 16, 16);
    const im = d.createElement('img'); im.src = c.toDataURL('image/png'); im.style.cssText = 'position:fixed;left:0;right:0;bottom:0;width:100%;height:110px;object-fit:cover;z-index:4998'; d.body.insertBefore(im, vide); }
  d.body.appendChild(b);
  await new Promise(r => w.requestAnimationFrame(() => r()));
  const premiere = { encre: w.getComputedStyle(b).getPropertyValue('--v-encre').trim(), fleche: !!b.querySelector('.v-fleche'), rond: b.classList.contains('v-rond') };
  await pause(1500);
  const ensuite = w.getComputedStyle(b).getPropertyValue('--v-encre').trim();
  return { quoi, sombre: d.documentElement.classList.contains('fond-sombre'), premiere, ensuite };
}
"""

BARRE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1400);
  const P = SEANCE_PARTS, k = P.paquet.findIndex(c => c && c.forme === 'scene_arret');
  if(k < 0) return { faute: 'pas de scene' };
  // une carte ratee plus tot, rattrapee juste apres la scene (comme rattraperAvantLeTheme)
  const revue = P.paquet.find((c, i) => i < k && c && c.forme !== 'scene_arret');
  P.paquet.splice(k + 1, 0, revue); currentCards = P.paquet;
  segmentsSeance(P.paquet, P.parts).forEach(s => PASSAGES_VUS.add(s.p));
  currentFlashcard = k + 1; loadFlashcard(); await pause(400);
  const segs = segmentsSeance(P.paquet, P.parts).map(s => s.p);
  return { segs, ici: [...document.querySelectorAll('#seancePartsNoms b')].map(x => x.textContent), titre: document.getElementById('flashThemeTitle').textContent };
}
"""

CADRE_FOND = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await ouvrirSeanceDuJour(); await pause(1400);
  const k = currentCards.findIndex(c => c && c.forme === 'scene_arret');
  segmentsSeance(SEANCE_PARTS.paquet, SEANCE_PARTS.parts).forEach(s => PASSAGES_VUS.add(s.p));
  currentFlashcard = k; loadFlashcard(); await pause(900);
  const sec = document.getElementById('sceneSeance');
  const seance = sec.style.background;
  showScreen('settings'); await pause(300);
  quitterReglages(); await pause(300);
  const retour = { avec: sec.classList.contains('avec-repere'), fond: sec.style.background };
  showScreen('home'); await pause(200);
  ouvrirSceneLibre('kueche'); await pause(500);
  const libre = { avec: sec.classList.contains('avec-repere'), fond: sec.style.background };
  return { seance: seance.slice(0, 60), retour: { avec: retour.avec, fond: retour.fond.slice(0, 60) }, libre };
}
"""

LANGUES = [("de", "fr"), ("de", "en"), ("de", "tr"), ("de", "uk"), ("de", "fa"), ("de", "ar"), ("de", "pt"), ("de", "pl"), ("de", "ru"), ("es", "de"), ("es", "fr")]


class Serveur(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *x, **k):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captures")
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Serveur, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = []

    def page_de(nav, appris, ui, theme, w, h, pp=False):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": w, "height": h}, service_workers="block")
        page = ctx.new_page()
        page._erreurs = []
        page.on("pageerror", lambda e: page._erreurs.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "" if appris == "de" else "?apprendre=" + appris))
        page.wait_for_load_state("networkidle")
        page.evaluate(POSER, [pp])
        page.evaluate("([l]) => { try{ localStorage.setItem(UI_LANG_KEY, l); }catch(e){} }", [ui])
        page.reload()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1400)
        page.evaluate("([t]) => document.body.setAttribute('data-theme', t)", [theme])
        return ctx, page

    def note(nom, ok, detail):
        if not ok:
            fautes.append(nom)
        print("== %s %s %s" % (nom, "ok" if ok else "FAUTE", json.dumps(detail, ensure_ascii=False)[:760]), flush=True)

    def capt(page, nom):
        if a.captures:
            os.makedirs(a.captures, exist_ok=True)
            page.evaluate("() => document.getAnimations().forEach(x => { const t = x.effect.getComputedTiming(); if(t.iterations !== Infinity){ try{ x.finish(); }catch(e){} } })")
            page.wait_for_timeout(200)
            page.screenshot(path=os.path.join(a.captures, nom + ".png"))

    def js(page):
        e = [x for x in page._erreurs if "synonymes" not in x]
        return sorted(set(e))[:3]

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, ui, theme, w, h in (("de", "fr", "light", 360, 780), ("de", "fr", "dark", 320, 568), ("es", "fr", "light", 320, 568), ("es", "fr", "dark", 360, 780), ("de", "ar", "dark", 320, 568), ("de", "ar", "light", 360, 780)):
                nom = "%s-%s-%s-%d" % (appris, ui, theme, w)
                ctx, page = page_de(nav, appris, ui, theme, w, h)
                r = page.evaluate(MESURE, ["seance"])
                d, v = r["depart"], r["verso"]
                fo = v["etat"]["fond"]
                ok = d["paysage"] and d["noms"] and len(d["noms"]) == d["barres"] and len(d["ici"]) == 1 and not d["debord"] and not d["pageDebord"] and not v["sousBoutons"]
                ok = ok and fo.get("fond") and fo.get("pire") and fo["pire"][0] >= 4.5
                if v["actionsVisibles"] is False:
                    ok = False
                note("seance " + nom, ok and not js(page), r)
                capt(page, "seance-verso-" + nom)
                ctx.close()
            for appris, ui, theme, w, h in (("de", "fr", "light", 360, 780), ("es", "fr", "dark", 320, 568)):
                nom = "%s-%s-%s-%d" % (appris, ui, theme, w)
                ctx, page = page_de(nav, appris, ui, theme, w, h, pp=True)
                r = page.evaluate(MESURE, ["pp"])
                ok = r["pp"]["paysage"] and r["pp"]["marque"].startswith("pp") and not r["pp"]["debord"]
                note("premiers pas " + nom, ok and not js(page), r)
                capt(page, "pp-" + nom)
                ctx.close()
            for appris, ui in LANGUES:
                ctx, page = page_de(nav, appris, ui, "light" if ui != "ar" else "dark", 320, 568)
                r = page.evaluate(SIX)
                ok = not r["sortants"] and not r["seules"] and not r["page"] and r["max"] <= 2 and len(r["noms"]) == 6
                note("six parties %s/%s" % (appris, ui), ok and not js(page), r)
                capt(page, "six-%s-%s" % (appris, ui))
                ctx.close()
            for theme in ("light", "dark"):
                ctx, page = page_de(nav, "de", "fr", theme, 360, 780)
                page.evaluate("() => ouvrirSeanceDuJour()")
                page.wait_for_timeout(1400)
                for k in ("pp", "rev", "mots", "conj", "scene", "theme", "son"):
                    m = page.evaluate(PAYSAGES, [k])
                    note("paysage %s %s" % (k, theme), m["marque"] == k + (":n" if theme == "dark" else ":j") and bool(m["fond"]), m)
                    capt(page, "paysage-%s-%s" % (k, theme))
                ctx.close()
            for appris, theme in (("de", "light"), ("es", "dark")):
                ctx, page = page_de(nav, appris, "fr", theme, 360, 780)
                r = page.evaluate(PASSAGE)
                note("passage %s" % appris, r["passage"] and bool(r["marque"]) and not js(page), r)
                capt(page, "passage-%s-%s" % (appris, theme))
                ctx.close()
            ctx, page = page_de(nav, "es", "de", "light", 360, 780)
            r = page.evaluate(PASSAGE)
            suite = r["texte"].split("Als Nächstes: ")
            note("passage interface allemande, majuscule gardee", r["passage"] and len(suite) == 2 and suite[1][:1].isupper() and not js(page), r)
            capt(page, "passage-es-ui-de")
            ctx.close()
            for appris, theme, w, h in (("de", "light", 360, 780), ("de", "dark", 320, 568), ("es", "light", 320, 568)):
                ctx, page = page_de(nav, appris, "fr", theme, w, h)
                r = page.evaluate(SCENE)
                ok = r.get("avec") and r["cadreHaut"] >= r["repereBas"] - 1 and len(r["ici"]) == 1 and r["paysageCache"]
                capt(page, "scene-%s-%s-%d" % (appris, theme, w))
                s = page.evaluate(SORTIE)
                note("scene %s %s %d" % (appris, theme, w), ok and s["accueilCache"] and s["sansBande"], [r, s])
                ctx.close()
            for appris, theme, w, h, quoi in (("de", "light", 360, 780, "scene"), ("es", "dark", 360, 780, "scene"), ("de", "light", 360, 780, "theme"), ("es", "dark", 320, 568, "theme"),
                                              ("de", "light", 360, 780, "pp"), ("es", "dark", 360, 780, "pp"), ("de", "fr-ar", 360, 780, "scene"),
                                              ("de", "light", 360, 780, "libre"), ("es", "dark", 360, 780, "theme-libre")):
                ui = "ar" if theme == "fr-ar" else "fr"
                th = "dark" if theme == "fr-ar" else theme
                ctx, page = page_de(nav, appris, ui, th, w, h, pp=(quoi == "pp"))
                r = page.evaluate(CADRE, [quoi])
                b, c = r.get("bande") or {}, r.get("cadre") or {}
                if quoi in ("libre", "theme-libre"):
                    ok = not b.get("avec") and not c.get("adresseFond") and not c.get("fondPose") and not c.get("faute")
                else:
                    ok = (b.get("avec") and b.get("fond") != "rgb(22, 34, 47)" and b.get("clair") == (th == "light") and b.get("ici") == 1
                          and c.get("adresseFond") and c.get("fondPose") and c.get("carteCachee") and "gradient" in (c.get("fondPage") or ""))
                note("cadre %s %s %s %s %d" % (quoi, appris, ui, th, w), ok and not js(page), r)
                capt(page, "cadre-%s-%s-%s-%s-%d" % (quoi, appris, ui, th, w))
                ctx.close()
            for appris, theme, quoi in (("es", "dark", "scene"), ("de", "light", "scene"), ("es", "dark", "theme"), ("de", "light", "theme")):
                ctx, page = page_de(nav, appris, "fr", theme, 390, 844)
                r = page.evaluate(FLECHE, [quoi])
                p1 = r.get("premiere") or {}
                claire = lambda e: e.replace(" ", "").startswith("rgb(243") or e.replace(" ", "").startswith("rgba(243")
                if quoi == "scene":
                    # sur la photo brune : la fleche blanche, de jour comme de nuit
                    ok = p1.get("rond") and p1.get("fleche") and claire(r.get("ensuite", "")) and (theme != "dark" or claire(p1.get("encre", "")))
                elif theme == "dark":
                    ok = r.get("sombre") and p1.get("rond") and p1.get("fleche") and claire(p1.get("encre", "")) and claire(r.get("ensuite", ""))
                else:
                    ok = p1.get("rond") and p1.get("fleche") and not claire(p1.get("encre", "")) and not r.get("sombre")
                note("fleche %s %s %s" % (quoi, appris, theme), ok and not js(page), r)
                capt(page, "fleche-%s-%s-%s" % (quoi, appris, theme))
                ctx.close()
            for appris, theme in (("de", "light"), ("es", "dark")):
                ctx, page = page_de(nav, appris, "fr", theme, 390, 844)
                r = page.evaluate(BARRE)
                segs = r.get("segs") or []
                # 12 nov. 2026, la barre en trois parties : plus de partie qui nait apres la scene -- une carte posee la
                # (cas force par la sonde ; la seance rattrape desormais AVANT les images) compte dans Images, et la
                # barre garde ses parties : Cartes, (Grammaire,) Images.
                ok = bool(segs) and "revisions" not in segs and segs == [x for x in ["cartes", "grammaire", "images", "conv"] if x in segs] and r.get("ici")
                note("barre apres la scene %s %s" % (appris, theme), ok and not js(page), r)
                capt(page, "barre-apres-scene-%s-%s" % (appris, theme))
                ctx.close()
            for appris, theme in (("de", "light"), ("es", "dark")):
                ctx, page = page_de(nav, appris, "fr", theme, 390, 844)
                r = page.evaluate(CADRE_FOND)
                ok = "gradient" in r.get("seance", "") and r["retour"]["avec"] and "gradient" in r["retour"]["fond"] and not r["libre"]["avec"] and not r["libre"]["fond"]
                note("cadre sans bandes %s %s" % (appris, theme), ok and not js(page), r)
                ctx.close()
            ctx, page = page_de(nav, "en", "fr", "light", 360, 780)
            d = page.evaluate("async () => { await ouvrirSeanceDuJour(); await new Promise(r => setTimeout(r, 1200)); const p = document.getElementById('seancePaysage'); return { dispo: repereSeanceDispo(), paysage: !!(p && !p.classList.contains('hidden')) }; }")
            note("anglais sans repere", not d["dispo"] and not d["paysage"], d)
            ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not fautes else "%d defaut(s) : %s" % (len(fautes), fautes)))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
