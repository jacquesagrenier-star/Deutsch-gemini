# -*- coding: utf-8 -*-
"""Ligne 143 (v1224, 19 nov. 2026), cinq petits defauts de la revue A a Z, a 360 x 740 :
  F4  la visite guidee, etape 1 : la page ne depasse plus l'ecran (fr, fr de nuit, en, ar) ;
  A5  derniere etape de la visite : « Continuer » en moins de 3 s, jamais sur l'etiquette du tableau, et la
      quitter en pleine demonstration mene a la fin de la visite ;
  A6  la bulle du premier accueil nomme le bouton (reperes_seance contient seance_commencer_long, 11 langues) ;
  F10 la serie « Quel cas apres ce verbe ? » dans la langue d'interface (ar, tr, uk ; fr inchange) ;
  E11 « Se preparer au C1 » > les feuilles de conjugaison : B2 et C1, toutes consultables, retour au panneau,
      et « Mes feuilles » ordinaire inchange (compte A2, fr et ar).
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/revue_143.py <racine> <port> <dossier-captures> [<index-avant.html>]
(avec un index d'avant la v1224 en 4e argument, la sonde montre les cinq defauts)"""
import io, json, os, sys, threading, functools, http.server
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT, OUT = sys.argv[1], int(sys.argv[2]), sys.argv[3]
AVANT = io.open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) > 4 else None
SUF = "-avant" if AVANT else ""


class Calme(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


FAUX_COMPTE = """() => { window.firebaseAuth = window.firebaseAuth || {};
  const u = { uid: 'demo-locale', email: '', displayName: '', isAnonymous: false };
  try{ Object.defineProperty(window.firebaseAuth, 'currentUser', { value: u, configurable: true }); }catch(e){ window.firebaseAuth.currentUser = u; }
  return true; }"""

POSER = """(a) => {
  localStorage.clear();
  const P = 'deutschAI_';
  localStorage.setItem('wortando_langueApprise', 'de');
  localStorage.setItem(P + 'uiLang', a.ui); localStorage.setItem(P + 'setupDone', '1'); localStorage.setItem(P + 'onboardingSeen', '1');
  if(a.niveau) localStorage.setItem(P + 'niveauSeance', a.niveau);
}"""

MESURE = """() => {
  const r = s => { const e = document.querySelector(s); if(!e) return null; const b = e.getBoundingClientRect(); return [Math.round(b.left), Math.round(b.right), Math.round(b.width)]; };
  const cadre = document.querySelector('#decouverteScene .sp-fili-cadre, #home .sp-fili-cadre');
  return { ecran: window.innerWidth, html: document.documentElement.scrollWidth, body: document.body.scrollWidth,
           etape: (typeof decouverte !== 'undefined' && decouverte) ? decouverte.etape : null,
           pilule: r('#seancePilule'), piste: r('.spf-piste'), cadre: r('.sp-fili-cadre'),
           piluleDansVisite: !!document.querySelector('#decouverteScene #seancePilule'),
           rognage: cadre ? getComputedStyle(cadre).overflowX : null };
}"""

VISITE = """async () => {
  await lancerDecouverte();
  await new Promise(r => setTimeout(r, 1500));
  let n = 0;
  while(!(decouverte && decouverte.pret) && n++ < 40) await new Promise(r => setTimeout(r, 250));
  allerEtapeDecouverte(1);
  await new Promise(r => setTimeout(r, 1800));
  return decouverte ? decouverte.etape : null;
}"""

SERIE = """async () => {
  let n = 0;
  while(!(typeof verbeTheme !== 'undefined' && verbeTheme && verbeTheme.words && verbeTheme.words.length) && n++ < 60) await new Promise(r => setTimeout(r, 250));
  const liste = buildVerbRektionExercises();
  const lire = ex => ({ q: texteTraduit(ex, 'question'), tr: texteTraduit(ex, 'translation'), ind: texteTraduit(ex, 'hint'), expl: texteTraduit(ex, 'explanation') });
  const anglais = liste.filter(ex => { const l = lire(ex); return /Which case|governs the/.test(l.q + ' ' + l.expl); }).length;
  const vides = liste.filter(ex => { const l = lire(ex); return !l.q || !l.tr || !l.ind || !l.expl; }).length;
  const reste = liste.filter(ex => { const l = lire(ex); return /[{}]/.test(l.q + l.expl); }).length;
  const par = {};
  ['Akkusativ', 'Dativ', 'Akkusativ + Dativ', 'Nominativ'].forEach(c => { const ex = liste.find(x => x.correct === c); if(ex) par[c] = lire(ex); });
  startVerbRektionExercise();
  await new Promise(r => setTimeout(r, 2500));
  const actif = document.querySelector('section.active, .screen.active') || document.body;
  return { n: liste.length, anglais: anglais, vides: vides, accolades: reste, exemples: par, ecran: (actif.id || '?'),
           texte: (actif.innerText || '').replace(/\\s+/g, ' ').slice(0, 420), html: document.documentElement.scrollWidth };
}"""

REPONDRE = """async () => {
  const b = Array.from(document.querySelectorAll('button')).filter(x => x.offsetParent && /^(Akkusativ|Dativ|Nominativ|Akkusativ \\+ Dativ)$/.test((x.innerText || '').trim()));
  if(!b.length) return 'aucun bouton de cas';
  b[0].click();
  await new Promise(r => setTimeout(r, 1800));
  const actif = document.querySelector('section.active, .screen.active') || document.body;
  return (actif.innerText || '').replace(/\\s+/g, ' ').slice(0, 520);
}"""

MOTS = {"fr": "Quel cas est-ce que", "ar": "يقتضيها", "tr": "hangi hali", "uk": "Якого відмінка"}


A5 = """async (max) => {
  const t0 = performance.now();
  allerEtapeDecouverte(5);
  const suite = document.getElementById('decouverteSuite');
  const vis = () => !!(suite && !suite.classList.contains('hidden') && suite.offsetParent);
  const tout0 = vis();
  let n = 0;
  while(!vis() && n++ < max * 10) await new Promise(r => setTimeout(r, 100));
  const eti = document.getElementById('decouverteProjection');
  return { etape: decouverte ? decouverte.etape : null, tout0: tout0, delai: Math.round(performance.now() - t0), visible: vis(),
           etiquette: eti && !eti.classList.contains('hidden') ? eti.textContent : '' };
}"""

ETAT5 = """() => {
  const r = id => { const e = document.getElementById(id); if(!e || e.classList.contains('hidden') || !e.offsetParent) return null; const b = e.getBoundingClientRect(); return [Math.round(b.top), Math.round(b.bottom)]; };
  const eti = document.getElementById('decouverteProjection');
  return { etape: decouverte ? decouverte.etape : null, suite: r('decouverteSuite'), fermer: r('decouverteFermer'), mosaique: r('decouverteMosaique'),
           etiquetteRect: r('decouverteProjection'), etiquette: eti && !eti.classList.contains('hidden') ? eti.textContent : '', haut: window.innerHeight,
           titre: (document.getElementById('decouverteTitre') || {}).textContent, html: document.documentElement.scrollWidth };
}"""

BULLE = """() => {
  const b = document.querySelector('.bulle-repere');
  const bt = document.getElementById('spPlayTxt');
  const s = document.querySelector('section.screen.active');
  const r = b ? b.getBoundingClientRect() : null;
  const langues = Object.keys(I18N).filter(c => I18N[c].reperes_seance);
  const fautes = langues.filter(c => I18N[c].reperes_seance.indexOf('\\u25B6') >= 0 || I18N[c].reperes_seance.indexOf(I18N[c].seance_commencer_long) < 0);
  return { ecran: s ? s.id : '?', bulle: b ? b.innerText.replace(/\\s+/g, ' ') : null, bouton: bt ? bt.textContent.trim() : null,
           rect: r ? [Math.round(r.left), Math.round(r.right), Math.round(r.top), Math.round(r.bottom)] : null,
           langues: langues.length, fautes: fautes, html: document.documentElement.scrollWidth };
}"""


def suite_visite(page, nom, bilan):
    """A5 : « Continuer » tot a la derniere etape ; A6 : la bulle du premier accueil nomme le bouton."""
    a = page.evaluate(A5, 45 if AVANT else 8)
    print("  A5 %s : etape %s, bouton deja la a l'ouverture %s, « Continuer » visible apres %s ms (%s) ; etiquette « %s »" % (
        nom, a["etape"], a["tout0"], a["delai"], "visible" if a["visible"] else "TOUJOURS CACHE", a["etiquette"][:70]), flush=True)
    page.wait_for_timeout(700)
    page.screenshot(path=os.path.join(OUT, "visite5-%s%s.png" % (nom, SUF)))
    if AVANT:
        page.evaluate("() => passerDecouverte()")
    else:
        if a["tout0"]:
            bilan.append("A5 %s : le bouton est la des l'ouverture (double toucher)" % nom)
        if not a["visible"] or a["delai"] > 3000:
            bilan.append("A5 %s : « Continuer » apres %s ms" % (nom, a["delai"]))
        page.wait_for_timeout(4500)
        e = page.evaluate(ETAT5)
        page.screenshot(path=os.path.join(OUT, "visite5-%s-plus-tard.png" % nom))
        print("     5 s plus tard : etiquette « %s », etiquette %s, bouton %s, ecran %s px de haut, page %s px" % (
            e["etiquette"][:70], e["etiquetteRect"], e["suite"], e["haut"], e["html"]), flush=True)
        if e["etiquette"] == a["etiquette"]:
            print("     (l'etiquette n'a pas change en 5 s)", flush=True)
        if e["etiquetteRect"] and e["suite"] and e["etiquetteRect"][1] > e["suite"][0] and e["etiquetteRect"][0] < e["suite"][1]:
            bilan.append("A5 %s : le bouton couvre l'etiquette (%s / %s)" % (nom, e["etiquetteRect"], e["suite"]))
        page.click("#decouverteSuite")
        page.wait_for_timeout(1200)
        f1 = page.evaluate(ETAT5)
        page.wait_for_timeout(6000)
        f2 = page.evaluate(ETAT5)
        page.screenshot(path=os.path.join(OUT, "visite-fin-%s.png" % nom))
        print("     apres « Continuer » en pleine demonstration : etape %s, titre « %s », bouton de fin %s, Continuer %s, tableau %s ; 6 s plus tard : tableau %s, etiquette « %s »" % (
            f1["etape"], f1["titre"], f1["fermer"], f1["suite"], f1["mosaique"], f2["mosaique"], f2["etiquette"][:40]), flush=True)
        if f1["etape"] != 6 or not f1["fermer"] or f1["suite"] or f2["mosaique"] or f2["etiquetteRect"] or f2["titre"] != f1["titre"]:
            bilan.append("A5 %s : la fin de la visite n'est pas propre apres « Continuer »" % nom)
        page.click("#decouverteFermer")
    page.wait_for_timeout(2200)
    b = page.evaluate(BULLE)
    page.screenshot(path=os.path.join(OUT, "bulle-%s%s.png" % (nom, SUF)))
    print("  A6 %s : ecran %s, bouton « %s », bulle %s : « %s » ; %d langues, fautes %s" % (
        nom, b["ecran"], b["bouton"], b["rect"], b["bulle"], b["langues"], b["fautes"]), flush=True)
    if not AVANT:
        if not b["bulle"]:
            bilan.append("A6 %s : pas de bulle apres la visite" % nom)
        elif "▶" in b["bulle"] or (b["bouton"] or "?") not in b["bulle"]:
            bilan.append("A6 %s : la bulle ne nomme pas le bouton « %s »" % (nom, b["bouton"]))
        if b["rect"] and (b["rect"][0] < 0 or b["rect"][1] > 360):
            bilan.append("A6 %s : la bulle sort de l'ecran %s" % (nom, b["rect"]))
        if b["fautes"] or b["langues"] != 11:
            bilan.append("A6 : %d langues, fautes %s" % (b["langues"], b["fautes"]))
        if b["html"] > 360:
            bilan.append("A6 %s : l'accueil fait %s px" % (nom, b["html"]))


LIRE_F = """() => {
  const s = document.querySelector('section.screen.active');
  const q = sel => Array.from(document.querySelectorAll(sel));
  const det = q('#feuillesListe .fc-detail').filter(e => !e.classList.contains('hidden'));
  return { ecran: s ? s.id : '?', panneau: (typeof openOrbId !== 'undefined') ? openOrbId : null,
           titre: (document.querySelector('#mesFeuilles h2') || {}).textContent, sous: (document.querySelector('#mesFeuilles .carnet-sous') || {}).textContent,
           rub: q('#feuillesListe .carnet-rub').map(e => e.textContent), lignes: q('#feuillesListe .fc-ligne').length,
           grisees: q('#feuillesListe .fc-ligne').filter(e => e.disabled).length,
           etiquettes: q('#feuillesListe .fc-ligne i').map(e => e.textContent.trim()).filter(Boolean).slice(0, 3),
           premiere: (document.querySelector('#feuillesListe .fc-ligne b') || {}).textContent,
           ouvertes: det.length, contenu: det.length ? det[0].innerText.replace(/\\s+/g, ' ').slice(0, 160) : '',
           entrainer: det.length ? !!det[0].querySelector('.fc-entrainer') : false, html: document.documentElement.scrollWidth };
}"""

OUVRIR_F = """async () => {
  ouvrirBlocC1();
  await new Promise(r => setTimeout(r, 1500));
  const o = (orbPanelData(openOrbId).options || []).find(x => /Feuilles/.test(x.action || ''));
  if(!o) return { action: null, panneau: openOrbId };
  const panneau = openOrbId;
  orbAction(o.action);
  await new Promise(r => setTimeout(r, 2200));
  return { action: o.action, panneau: panneau, titreTuile: o.title, descTuile: o.desc };
}"""

DOS = "() => { const s = document.querySelector('section.screen.active'); const b = s && s.querySelector('button.back'); if(b) b.click(); return !!b; }"


def feuilles(page, ui, bilan):
    """E11 : la tuile du bloc C1 ouvre les feuilles B2 et C1, consultables ; « Mes feuilles » ordinaire inchange."""
    o = page.evaluate(OUVRIR_F)
    v = page.evaluate(LIRE_F)
    page.screenshot(path=os.path.join(OUT, "feuilles-c1-%s%s.png" % (ui, SUF)))
    print("  %s : la tuile « %s » (%s) lance %s depuis %s -> ecran %s, titre « %s », sous-titre « %s », rubriques %s, %d feuilles dont %d grisees, etiquettes %s, page %s px" % (
        ui, o.get("titreTuile"), o.get("descTuile"), o["action"], o["panneau"], v["ecran"], v["titre"], v["sous"], v["rub"], v["lignes"], v["grisees"], v["etiquettes"], v["html"]), flush=True)
    if AVANT:
        return
    if v["ecran"] != "mesFeuilles" or len(v["rub"]) != 2 or not v["rub"][0].startswith("B2") or not v["rub"][1].startswith("C1") or v["lignes"] != 18 or v["grisees"]:
        bilan.append("E11 %s : la vue de l'examen n'est pas B2 + C1, 18 feuilles ouvertes (%s, %d, %d grisees)" % (ui, v["rub"], v["lignes"], v["grisees"]))
    if v["html"] > 360:
        bilan.append("E11 %s : page de %s px" % (ui, v["html"]))
    # une feuille B2 s'ouvre : son tableau, et M'entrainer
    page.click("#feuillesListe .fc-ligne >> nth=0")
    page.wait_for_timeout(900)
    d = page.evaluate(LIRE_F)
    page.screenshot(path=os.path.join(OUT, "feuilles-c1-%s-ouverte.png" % ui))
    print("     la 1re feuille (%s) touchee : %d ouverte, M'entrainer %s, contenu « %s »" % (d["premiere"], d["ouvertes"], d["entrainer"], d["contenu"]), flush=True)
    if d["ouvertes"] != 1 or not d["contenu"]:
        bilan.append("E11 %s : la feuille ne s'ouvre pas" % ui)
    # la derniere (C1) aussi
    page.click("#feuillesListe .fc-ligne >> nth=17")
    page.wait_for_timeout(700)
    d2 = page.evaluate(LIRE_F)
    if d2["ouvertes"] != 2:
        bilan.append("E11 %s : la derniere feuille C1 ne s'ouvre pas" % ui)
    if d["entrainer"]:
        page.click("#feuillesListe .fc-detail:not(.hidden) .fc-entrainer >> nth=0")
        page.wait_for_timeout(2800)
        e = page.evaluate(LIRE_F)
        page.screenshot(path=os.path.join(OUT, "feuilles-c1-%s-serie.png" % ui))
        print("     M'entrainer : ecran %s" % e["ecran"], flush=True)
        if e["ecran"] == "mesFeuilles":
            bilan.append("E11 %s : M'entrainer n'ouvre rien" % ui)
        page.evaluate(DOS)
        page.wait_for_timeout(1800)
        r = page.evaluate(LIRE_F)
        print("     « ‹ » depuis la serie : ecran %s, rubriques %s" % (r["ecran"], r["rub"]), flush=True)
        if r["ecran"] != "mesFeuilles" or len(r["rub"]) != 2:
            bilan.append("E11 %s : le retour de la serie ne ramene pas aux feuilles de l'examen (%s, %s)" % (ui, r["ecran"], r["rub"]))
    # « ‹ » ramene au panneau du C1
    page.evaluate("() => { const b = document.querySelector('#mesFeuilles button.back'); if(b) b.click(); }")
    page.wait_for_timeout(1200)
    p = page.evaluate(LIRE_F)
    print("     « ‹ » depuis les feuilles : ecran %s, panneau %s" % (p["ecran"], p["panneau"]), flush=True)
    if p["ecran"] != "orbPanel" or p["panneau"] != o["panneau"]:
        bilan.append("E11 %s : « ‹ » ne ramene pas au panneau du C1 (%s, %s)" % (ui, p["ecran"], p["panneau"]))
    # « Mes feuilles » ordinaire : inchange (le niveau du compte, a venir grisees), retour a l'accueil
    page.evaluate("async () => { await ouvrirMesFeuilles(); }")
    page.wait_for_timeout(900)
    n = page.evaluate(LIRE_F)
    page.screenshot(path=os.path.join(OUT, "feuilles-ordinaires-%s.png" % ui))
    print("     « Mes feuilles » ordinaire : titre « %s », sous-titre « %s », rubriques %s, %d feuilles dont %d grisees, etiquettes %s" % (
        n["titre"], (n["sous"] or "")[:50], n["rub"], n["lignes"], n["grisees"], n["etiquettes"]), flush=True)
    if len(n["rub"]) != 1 or not n["rub"][0].startswith("A2") or n["lignes"] != 12 or n["grisees"] != 12 or n["titre"] == v["titre"]:
        bilan.append("E11 %s : « Mes feuilles » ordinaire a change" % ui)
    page.evaluate("() => { const b = document.querySelector('#mesFeuilles button.back'); if(b) b.click(); }")
    page.wait_for_timeout(900)
    h = page.evaluate(LIRE_F)
    if h["ecran"] != "home":
        bilan.append("E11 %s : « ‹ » de Mes feuilles ordinaire ne ramene pas a l'accueil (%s)" % (ui, h["ecran"]))


def main():
    os.makedirs(OUT, exist_ok=True)
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()

            def ouvrir(ui, nuit=False, niveau=None):
                ctx = nav.new_context(viewport={"width": 360, "height": 740}, device_scale_factor=2, service_workers="block", has_touch=True, is_mobile=True)
                for motif in ("**/*firebase*", "**/*gstatic*", "**/*googleapis*", "**/*recaptcha*"):
                    ctx.route(motif, lambda r: r.abort())
                if AVANT:
                    ctx.route("**/index.html*", lambda r: r.fulfill(status=200, content_type="text/html; charset=utf-8", body=AVANT))
                page = ctx.new_page()
                page.erreurs = []
                page.on("pageerror", lambda e: page.erreurs.append(str(e).splitlines()[0][:140] if str(e) else ""))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html" % PORT, wait_until="domcontentloaded")
                page.wait_for_timeout(2500)
                page.evaluate(POSER, {"ui": ui, "nuit": nuit, "niveau": niveau})
                page.reload(wait_until="domcontentloaded"); page.wait_for_timeout(4500)
                page.evaluate(FAUX_COMPTE)
                if nuit:
                    page.evaluate("() => setAppTheme('dark')"); page.wait_for_timeout(400)
                return ctx, page

            print("===== F4 : la visite guidee, etape 1, 360 px%s" % (" (AVANT)" if AVANT else ""), flush=True)
            for ui, nuit in (("fr", False), ("fr", True), ("en", False), ("ar", False)):
                ctx, page = ouvrir(ui, nuit)
                nom = ui + ("-nuit" if nuit else "")
                acc = page.evaluate(MESURE)
                if not AVANT and ui == "fr":
                    page.screenshot(path=os.path.join(OUT, "accueil-%s.png" % nom))
                et = page.evaluate(VISITE)
                m = page.evaluate(MESURE)
                page.screenshot(path=os.path.join(OUT, "visite1-%s%s.png" % (nom, SUF)))
                # un geste de cote : la page ne doit pas glisser
                page.evaluate("() => window.scrollTo(400, 0)"); page.wait_for_timeout(300)
                glisse = page.evaluate("() => Math.round(window.scrollX)")
                print("  %s : accueil html %s px ; visite etape %s : html %s, body %s, pilule %s, piste %s, cadre %s, dans la visite %s, rognage %s ; glissement de cote %s px ; erreurs JS %d %s" % (
                    nom, acc["html"], et, m["html"], m["body"], m["pilule"], m["piste"], m["cadre"], m["piluleDansVisite"], m["rognage"], glisse, len(page.erreurs), page.erreurs[:2]), flush=True)
                if et != 1 or not m["piluleDansVisite"]:
                    bilan.append("F4 %s : la sonde n'est pas a l'etape 1 avec la carte de seance" % nom)
                if m["html"] > m["ecran"] or glisse:
                    bilan.append("F4 %s : la page fait %s px pour %s (glissement %s)" % (nom, m["html"], m["ecran"], glisse))
                if acc["html"] > acc["ecran"]:
                    bilan.append("F4 %s : l'accueil fait %s px" % (nom, acc["html"]))
                page.evaluate("() => window.scrollTo(0, 0)")
                suite_visite(page, nom, bilan)
                if page.erreurs:
                    bilan.append("F4 / A5 / A6 %s : erreurs JS %s" % (nom, page.erreurs[:2]))
                ctx.close()

            print("===== F10 : la serie « Quel cas apres ce verbe ? »%s" % (" (AVANT)" if AVANT else ""), flush=True)
            for ui in ("fr", "ar", "tr", "uk"):
                ctx, page = ouvrir(ui)
                r = page.evaluate(SERIE)
                page.screenshot(path=os.path.join(OUT, "serie-%s%s.png" % (ui, SUF)))
                apres = page.evaluate(REPONDRE)
                page.screenshot(path=os.path.join(OUT, "serie-%s-reponse%s.png" % (ui, SUF)))
                print("  %s : %d questions, %d en anglais, %d champs vides, %d accolades ; ecran %s, page %s px ; erreurs JS %d %s" % (
                    ui, r["n"], r["anglais"], r["vides"], r["accolades"], r["ecran"], r["html"], len(page.erreurs), page.erreurs[:2]), flush=True)
                for c, l in r["exemples"].items():
                    print("     %s : %s | %s | %s | %s" % (c, l["q"], l["tr"], l["ind"], l["expl"]), flush=True)
                print("     a l'ecran : %s" % r["texte"], flush=True)
                print("     apres une reponse : %s" % apres, flush=True)
                if ui != "fr" and r["anglais"]:
                    bilan.append("F10 %s : %d questions en anglais" % (ui, r["anglais"]))
                if r["vides"] or r["accolades"]:
                    bilan.append("F10 %s : %d champs vides, %d accolades" % (ui, r["vides"], r["accolades"]))
                if MOTS[ui] not in r["texte"]:
                    bilan.append("F10 %s : la question dans la langue n'est pas a l'ecran" % ui)
                if page.erreurs:
                    bilan.append("F10 %s : erreurs JS" % ui)
                ctx.close()
            print("===== E11 : les feuilles B2 et C1 depuis « Se preparer au C1 », compte A2%s" % (" (AVANT)" if AVANT else ""), flush=True)
            for ui in ("fr", "ar"):
                ctx, page = ouvrir(ui, niveau="A2")
                feuilles(page, ui, bilan)
                if page.erreurs:
                    bilan.append("E11 %s : erreurs JS %s" % (ui, page.erreurs[:2]))
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("BILAN", "OK" if not bilan else "A REVOIR : " + " | ".join(bilan), flush=True)


main()
