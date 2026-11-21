# -*- coding: utf-8 -*-
"""Ton ciel : l'acces a la constellation depuis l'accueil (proposition B, Jacques, 9 nov. 2026).

    python tests/ton_ciel.py                      (de et es)
    python tests/ton_ciel.py --captures DOSSIER

Sur un navigateur vierge, sans compte, l'etat pose dans le stockage :
  neuf      : rien d'atteint, la bande ne ressemble pas a une panne (« Ta premiere etoile ») ;
  pp        : Premiers pas, jour 3 : la Grande Ourse en cours ;
  a1        : A1 voyage, etape 6 : Grande Ourse finie, Gemeaux 5/12, Orion a venir ;
  a2        : un compte A2 d'avant (ligne 158) : les 30 etoiles de l'A1 gardees, la Lyre ensuite (0/6) ;
  voyage    : A1 voyage, etape 6, sans Premiers pas : ses 5 etoiles, dans l'ordre du voyage (la Grande Ourse 5/8) ;
  ancien    : A1 sans le voyage (ancien ordre) : un ciel qui part de 0 (ligne 158 : les etoiles suivent les seances) ;
  anglais   : pas de ciel hors de l'allemand et de l'espagnol.
Dans la page, seulement ce qu'on a atteint (Jacques, 10 nov.) : la figure en cours et celles commencees ou finies, jamais une
figure a venir, ni en pastille ni en dessin -- neuf, pp, voyage et ancien : 1 pastille, a1 : 2, a2 : 4.
A chaque fois : la bande coupee en deux sans debordement, puis la page, ses pastilles, une etoile touchee (nom et distance « de la
Terre »), a 320 et 360 px, clair, nuit et RTL.
Ligne 160 (Jacques, 20 nov.) : sous le dessin, la phrase PERMANENTE « Touche une etoile allumee… » des qu'une etoile de la figure
est allumee (et a la reouverture), jamais sans etoile allumee ; une etoile eteinte touchee ne dit que « A decouvrir » (ni nom,
ni distance, ni detail) ; une etoile allumee touchee, son nom, sa distance et, sous le dessin, l'annee ou sa lumiere est
partie ; le nom de la figure dans la langue apprise, avec son haut-parleur. Il ouvre un navigateur : a lancer SOUS LE VERROU (~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("TON_CIEL_PORT", "8805"))

POSER = """
([cas]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(cas === 'pp'){ localStorage.setItem(NIVEAU_DECLARE_KEY, 'zero'); localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: true, k: 6 })); }
  if(cas === 'a1'){ localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true })); localStorage.setItem(A1_VOYAGE_KEY, JSON.stringify({ a: true, e: 5, t: true, b: 0 }));
                    localStorage.setItem(CIEL_PART_KEY, JSON.stringify({ g: 'a1_escales', n: 5, p: .45 })); }
  if(cas === 'a2'){ localStorage.setItem(NIVEAU_SEANCE_KEY, 'A2'); localStorage.setItem(CIEL_COMPTE_KEY, JSON.stringify({ n: 30, m: 1 })); }
  if(cas === 'voyage'){ localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false })); localStorage.setItem(A1_VOYAGE_KEY, JSON.stringify({ a: true, e: 5, t: true, b: 0 })); }
  if(cas === 'ancien'){ localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false })); localStorage.setItem(A1_VOYAGE_KEY, JSON.stringify({ a: false, e: 0 })); }
}
"""

MESURE = r"""
async ([cas]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  showScreen('home'); try{ majGrilleAccueil(); }catch(e){}
  for(let k = 0; k < 40 && !tuileCielPrete && cielDisponible() && cas !== 'ancien'; k++) await pause(100);
  await pause(600);
  const rect = x => { const r = x.getBoundingClientRect(); return { l: Math.round(r.left), r: Math.round(r.right), h: Math.round(r.height), w: Math.round(r.width) }; };
  const ciel = document.querySelector('.tg[data-tg="ciel"]'), tab = document.querySelector('.tg[data-tg="tableau"]');
  const tv = !!(ciel && !ciel.classList.contains('hidden') && ciel.offsetHeight > 0), tabv = !!(tab && !tab.classList.contains('hidden') && tab.offsetHeight > 0);
  const inner = b => { const f = b.querySelector('.tg-filet').getBoundingClientRect(); return [...b.querySelectorAll('.tg-tab-pct, .tg-tab-titre')].filter(x => x.textContent).every(x => { const g = document.createRange(); g.selectNodeContents(x); const r = g.getBoundingClientRect(); return r.left >= f.left - 1 && r.right <= f.right + 1 && r.bottom <= f.bottom + 1; }); };
  const accueil = { ciel: tv, tableau: tabv, deux: !!document.querySelector('.tg-rangee.deux'), compte: tv ? document.getElementById('grilleCielCompte').textContent : '', titre: tv ? ciel.querySelector('.tg-tab-titre').textContent : '',
                    rects: [tv && rect(ciel), tabv && rect(tab)], dedans: (!tv || inner(ciel)) && (!tabv || inner(tab)), debord: document.documentElement.scrollWidth > window.innerWidth, dessin: tv ? document.querySelectorAll('#grilleCielDessin circle').length : 0 };
  if(!tv) return { accueil };
  await ouvrirCiel(); await pause(400);
  const lire = () => ({ actif: (document.querySelector('.screen.active') || {}).id, pastilles: [...document.querySelectorAll('.tc-pastille')].map(b => b.textContent + (b.classList.contains('active') ? ' *' : '')), total: document.getElementById('tcTotal').textContent, info: document.getElementById('tcInfo').innerText.replace(/\n+/g, ' | '), noms: document.querySelectorAll('#tcSvg .fc-nom').length, cible: document.querySelectorAll('#tcSvg .fc-cible').length, allumes: document.querySelectorAll('#tcSvg .fc-allume').length, debord: document.getElementById('tonCiel').scrollWidth > document.getElementById('tonCiel').clientWidth + 1 || document.documentElement.scrollWidth > window.innerWidth });
  const page = lire();
  const noteEl = document.getElementById('tcNote'), lireNote = () => { if(!noteEl) return null; const r = noteEl.getBoundingClientRect(), s = document.getElementById('tcSvg').getBoundingClientRect(), p = document.getElementById('tcPastilles').getBoundingClientRect();
    return { visible: !noteEl.hidden && noteEl.offsetHeight > 0, texte: noteEl.textContent, apresDessin: r.top >= s.bottom - 1, dansLargeur: r.left >= -1 && r.right <= window.innerWidth + 1, haut: Math.round(r.height) }; };
  page.note = lireNote();
  page.allumees = vueTonCiel().n;
  const hp = document.querySelector('#tcInfo .tc-appris .tc-hp');
  page.appris = { texte: (document.querySelector('#tcInfo .tc-appris span') || {}).textContent || '', hp: !!hp, langue: LANGUE_APPRISE, attendu: (vueTonCiel().c.noms || {})[LANGUE_APPRISE] || '' };
  const v = vueTonCiel(), svg = document.getElementById('tcSvg'), m = svg.getScreenCTM();
  const toucher = async k => { const b2 = v.c.etoiles[k]; svg.dispatchEvent(new MouseEvent('click', { bubbles: true, clientX: b2.x * m.a + m.e, clientY: b2.y * m.d + m.f })); await pause(120); };
  const detail = () => { const d = document.getElementById('tcDetail'); return { visible: !!d && !d.hidden && d.offsetHeight > 0, texte: d ? d.textContent : '' }; };
  // une etoile eteinte (la cible) : le mystere
  if(v.n < v.c.etoiles.length){
    await toucher(v.n);
    const e2 = document.querySelector('#tcEtiq .fe-nom-et');
    page.eteinte = { texte: e2 ? [...e2.querySelectorAll('tspan')].map(x => x.textContent).filter(Boolean).join(' / ') : null, attendu: t('ciel_a_decouvrir'), detail: detail(),
                     aria: (svg.querySelector('.tc-tact[data-i="' + v.n + '"]') || { getAttribute: () => '' }).getAttribute('aria-label') };
    await toucher(v.n);   // le deuxieme toucher referme
  }
  // une etoile allumee (la derniere) : son nom, sa distance, l'annee de sa lumiere
  const a = v.c.etoiles[Math.max(0, v.n - 1)];
  await toucher(Math.max(0, v.n - 1));
  page.detail = detail();
  page.lumiere = v.n > 0 ? phraseLumiereEtoile(a) : '';
  page.prochaine = { texte: (document.querySelector('#tcInfo .tc-proch') || {}).textContent || '', attendu: t('ciel_prochaine_mystere'), dist: !!document.querySelector('#tcInfo .tc-dist'),
                     enCours: v.n < v.t && (v.g === CIEL_ETAT.courant || v.n > 0) };
  const et = document.querySelector('#tcEtiq .fe-nom-et');
  const box = et && et.getBBox();
  const touche = et ? { texte: [...et.querySelectorAll('tspan')].map(x => x.textContent).join(' / '), x0: Math.round(box.x), x1: Math.round(box.x + box.width), y0: Math.round(box.y), y1: Math.round(box.y + box.height), dansCadre: box.x >= 0 && box.x + box.width <= 375 && box.y >= 0 && box.y + box.height <= 372, nomsCaches: svg.classList.contains('tc-choisie') } : null;
  page.noteApres = lireNote();
  window.__captureTouche = true;
  return { accueil, page, touche };
}
"""

REOUVRIR = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  showScreen('home'); await pause(150); await ouvrirCiel(); await pause(300);
  const el = document.getElementById('tcNote');
  return { visible: !!el && !el.hidden && el.offsetHeight > 0, allumees: vueTonCiel().n };
}
"""

AUTRE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const res = [];
  const bs = () => [...document.querySelectorAll('.tc-pastille')];
  for(let i = 0; i < bs().length; i++){
    bs()[i].click(); await pause(100);
    res.push({ pastille: bs()[i].textContent, info: document.getElementById('tcInfo').innerText.replace(/\n+/g, ' | '), allumes: document.querySelectorAll('#tcSvg .fc-allume').length, cible: document.querySelectorAll('#tcSvg .fc-cible').length });
  }
  return res;
}
"""


def juger(cas, r):
    a = r["accueil"]
    f = []
    if a["debord"] or not a["dedans"]:
        f.append("debordement a l'accueil")
    if cas == "anglais":
        if a["ciel"]:
            f.append("tuile presente")
        if a["tableau"] and a["deux"]:
            f.append("bande coupee sans ciel")
        return f
    if not a["ciel"]:
        return f + ["pas de tuile"]
    if a["tableau"] and not a["deux"]:
        f.append("bande non coupee")
    p = r["page"]
    if p["actif"] != "tonCiel":
        f.append("page non ouverte")
    if p["debord"]:
        f.append("debordement de la page")
    attendu = {"neuf": 1, "pp": 1, "a1": 2, "a2": 4, "voyage": 1, "ancien": 1}.get(cas)
    if len(p["pastilles"]) != attendu:
        f.append("pastilles %s (attendu %s)" % (p["pastilles"], attendu))
    for x in r.get("pastilles") or []:
        if "venir" in x["info"].lower() or "coming" in x["info"].lower():
            f.append("figure a venir montree : %s" % x["pastille"])
    if cas == "voyage" and p["pastilles"] and not any(x in p["pastilles"][0] for x in ("Ourse", "Osa", "Wagen", "Bär")):
        f.append("voyage : %s" % p["pastilles"])
    n0, n1, n2 = p.get("note") or {}, p.get("noteApres") or {}, r.get("reouvert") or {}
    if p.get("allumees"):
        if not n0.get("visible") or not n0.get("texte") or not n0.get("apresDessin") or not n0.get("dansLargeur"):
            f.append("phrase avant de toucher : %s" % n0)
        if not n1.get("visible"):
            f.append("phrase partie pendant la visite")
        if not n2.get("visible"):
            f.append("phrase absente a la reouverture : %s" % n2)
        d = p.get("detail") or {}
        if not d.get("visible") or d.get("texte") != p.get("lumiere") or not p.get("lumiere"):
            f.append("etoile allumee, l'annee de sa lumiere : %s / %s" % (d, p.get("lumiere")))
    elif n0.get("visible") or n2.get("visible"):
        f.append("phrase sans etoile allumee : %s" % n0)
    pr = p.get("prochaine") or {}
    if pr.get("enCours") and (pr.get("texte") != pr.get("attendu") or pr.get("dist")):
        f.append("prochaine etoile devoilee : %s" % pr)
    e = p.get("eteinte")
    if e is not None and (e.get("texte") != e.get("attendu") or e["detail"].get("visible") or e.get("aria") != e.get("attendu")):
        f.append("etoile eteinte, le mystere : %s" % e)
    ap = p.get("appris") or {}
    if ap.get("attendu") and (ap.get("texte") != ap.get("attendu") or not ap.get("hp")):
        f.append("nom dans la langue apprise : %s" % ap)
    t = r.get("touche")
    if not t or not t["texte"] or not t["dansCadre"]:
        f.append("etoile touchee : %s" % t)
    if cas in ("neuf", "ancien") and (a["compte"] == "" or "/" in a["compte"]):
        f.append("neuf : %s" % a["compte"])
    if cas == "a1" and a["compte"] != "5/12":
        f.append("a1 : %s" % a["compte"])
    if cas == "a2" and a["compte"] != "0/6":
        f.append("a2 (30 etoiles gardees, la Lyre ensuite) : %s" % a["compte"])
    return f


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
    total = 0
    CAS = [("de", "fr", "light", 360, "neuf"), ("de", "fr", "dark", 320, "neuf"), ("de", "fr", "light", 360, "pp"), ("de", "fr", "light", 360, "a1"), ("de", "fr", "dark", 320, "a1"),
           ("de", "ar", "dark", 320, "a1"), ("de", "ar", "light", 360, "a1"), ("de", "fr", "dark", 360, "a1"), ("de", "ar", "dark", 360, "a1"), ("de", "fa", "light", 320, "a1"), ("de", "ru", "light", 320, "a1"), ("de", "tr", "dark", 320, "a2"), ("de", "fr", "light", 360, "a2"),
           ("es", "fr", "light", 360, "a1"), ("es", "fr", "dark", 320, "neuf"), ("es", "de", "light", 320, "a2"),
           ("de", "fr", "light", 360, "voyage"), ("es", "fr", "dark", 320, "voyage"), ("de", "ar", "dark", 320, "pp"), ("es", "ar", "light", 360, "pp"), ("de", "fr", "light", 360, "ancien"), ("en", "fr", "light", 360, "anglais")]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, ui, theme, largeur, cas in CAS:
                ctx = nav.new_context(locale="fr-FR", viewport={"width": largeur, "height": 780}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                adresse = "http://127.0.0.1:%d/index.html%s" % (PORT, "" if appris == "de" else "?apprendre=" + appris)
                page.goto(adresse)
                page.wait_for_load_state("networkidle")
                page.evaluate(POSER, [cas])
                page.evaluate("([l]) => { try{ localStorage.setItem(UI_LANG_KEY, l); }catch(e){} }", [ui])
                page.reload()
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(1500)
                page.evaluate("([t]) => document.body.setAttribute('data-theme', t)", [theme])
                nom = "%s-%s-%s-%d-%s" % (appris, ui, theme, largeur, cas)
                try:
                    r = page.evaluate(MESURE, [cas])
                    if a.captures and r["accueil"].get("ciel"):
                        os.makedirs(a.captures, exist_ok=True)
                        page.screenshot(path=os.path.join(a.captures, nom + "-page.png"))
                    if r["accueil"].get("ciel"):
                        r["pastilles"] = page.evaluate(AUTRE)
                        r["reouvert"] = page.evaluate(REOUVRIR)
                    if a.captures:
                        os.makedirs(a.captures, exist_ok=True)
                        page.evaluate("() => { showScreen('home'); const g = document.getElementById('grilleAccueil'); if(g) g.scrollIntoView({ block: 'center' }); }")
                        page.wait_for_timeout(500)
                        page.screenshot(path=os.path.join(a.captures, nom + "-accueil.png"))
                    fautes = juger(cas, r)
                except Exception as e:
                    r = None
                    fautes = [str(e).split("\n")[0][:300]]
                total += 1 if fautes else 0
                print("== %s %s %s" % (nom, "ok" if not fautes else "FAUTE", fautes), flush=True)
                print("   " + json.dumps(r, ensure_ascii=False)[:1400], flush=True)
                erreurs = [e for e in erreurs if "synonymes" not in e]
                if erreurs:
                    print("   erreurs JS", sorted(set(erreurs))[:4], flush=True)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not total else "%d cas en defaut" % total))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
