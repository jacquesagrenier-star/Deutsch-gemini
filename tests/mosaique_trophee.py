# -*- coding: utf-8 -*-
"""Le trophee de la mosaique : trois JOURS D'OUVERTURE de l'app, puis le tableau suivant (decision de Jacques, 13 nov. 2026).

    python tests/mosaique_trophee.py                     (la page du depot)
    python tests/mosaique_trophee.py --index AUTRE.html  (sert ce fichier a la place d'index.html : l'ancienne version)
    python tests/mosaique_trophee.py --sans-seance       (saute les deux cas qui jouent une seance entiere)

Ne de son retour du 13 nov. (espagnol, iPhone v1182) : Navazio, « Naturaleza », gagne, restait a « 3/3 » des jours
durant. Le jour ne se comptait qu'en sortant des cartes par « TERMINER » ou « ‹ » ; fermer l'app sur l'ecran de fin
ne decomptait rien. L'horloge est simulee (une heure posee dans le stockage, que la page lit avant ses scripts) ;
chaque « ouverture » est un rechargement. Sur un navigateur vierge, sans compte.

Cas :
  jacques_fermee   : l'etat de Jacques, le 13 ; une seance jouee jusqu'a l'ecran de fin, puis l'app fermee (sans
                     TERMINER) ; ouvertures le 14 et le 15 -> le tableau suivant (rang 4, 352 carreaux d'avance) ;
  jacques_terminer : la meme seance finie par TERMINER ;
  jours_ouverture  : gagne le 10 (« jour 1 sur 3 ») ; ouvert deux fois le 11 (« jour 2 sur 3 »), pas le 12, le 13 (« jour 3 sur 3 »), le 14 le
                     suivant ; une semaine d'absence ne compte que pour un jour ;
  victoire         : le 700e carreau -> « 1/3 » le jour meme, et ce jour-la est le jour 1 ;
  bloque           : un tableau gagne sans trophee ni fin (ce que la fusion pouvait fabriquer) -> « 3/3 » ce jour, le
                     suivant au prochain jour d'ouverture ;
  ancien_b         : un etat ecrit par l'ancienne version (`b` pose hier) bascule a l'ouverture ;
  fusion           : fusionnerMosaique() -- le trophee ne remonte jamais, sur six paires d'etats.
Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
"""
import argparse
import datetime
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
PORT = int(os.environ.get("MOSAIQUE_TROPHEE_PORT", "8826"))

# L'heure simulee : `__horloge` = { cible, reel } ; l'heure de la page part de `cible` et avance au rythme reel.
HORLOGE = r"""
(() => {
  let h = null;
  try{ h = JSON.parse(localStorage.getItem('__horloge') || 'null'); }catch(e){}
  if(!h) return;
  const D = Date, decal = h.cible - h.reel;
  function F(...a){
    if(!(this instanceof F)) return new D(D.now() + decal).toString();
    return a.length ? new D(...a) : new D(D.now() + decal);
  }
  F.prototype = D.prototype; F.now = () => D.now() + decal; F.UTC = D.UTC; F.parse = D.parse;
  window.Date = F;
})();
"""

PREPARER = """
() => { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1'); }
"""

# L'etat lu dans Firestore le 13 nov. (usuariosEs, champ mosaique).
JACQUES = {"r": 3, "c": 765, "j": "2026-11-12", "n": 198, "g": [1, 2, 3], "t": 1, "tj": "2026-11-12", "x": 1,
           "s": "es", "h": [1], "b": "", "cn": 352}

# Ce que l'accueil montre : l'etat brut (avant tout appel de la sonde), puis apres l'accueil dessine.
LIRE = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const brut = JSON.parse(localStorage.getItem(MOSAIQUE_CLE) || 'null');
  try{ goHome(); }catch(e){}
  await chargerMosaiques();
  mosaiqueEnRetard = true; try{ majMosaiqueAccueil(); }catch(e){}
  await pause(1500);
  const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE) || 'null');
  const s = document.querySelector('#mosaiqueCartouche .mos-sejour'), c = document.getElementById('mosaiqueCartouche');
  const m = mosaiqueCourante();
  return { jour: getTodayStr(), brut: brut && { r: brut.r, t: brut.t, tj: brut.tj, b: brut.b },
           r: v.r, c: v.c, t: v.t, tj: v.tj, b: v.b, cn: v.cn, g: v.g,
           sejour: c && !c.classList.contains('hidden') && s ? s.textContent : '', tableau: m ? (m.peintre || '') + ' ' + (m.titre || '') : '' };
}
"""

# Une seance du jour jouee jusqu'a son ecran de fin (la boucle de tests/fin_de_seance.py).
JOUER = r"""
async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas(); await chargerCiel();
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  await ouvrirSeanceDuJour(); await pause(1400);
  let n = 0;
  for(let pas = 0; pas < 220; pas++){
    await pause(60);
    if(currentFlashcard >= currentCards.length) break;
    const scr = (document.querySelector('.screen.active') || {}).id;
    const c = currentCards[currentFlashcard];
    const go = document.querySelector('#cartePhrase .cp-passage-go');
    if(go && go.offsetHeight > 0){ go.click(); await pause(120); continue; }
    if(scr === 'sceneSeance'){ revenirDeLArret(); await pause(220); continue; }
    if(scr !== 'flashcards') break;
    const n0 = currentFlashcard, q0 = currentCards;
    if(c.mode === 'phrase'){ try{ repondrePhrase(c, c.forme === 'pp_tableau' || c.forme === 'av_bloc' ? null : true); }catch(e){} nextFlashcard(); }
    else reviewGood();
    n++;
    for(let k = 0; k < 40 && currentFlashcard === n0 && currentCards === q0; k++) await pause(50);
  }
  await pause(800);
  const fin = document.getElementById('flashcardEnd') || document.querySelector('.flash-end');
  const finVisible = !!document.querySelector('[onclick="handleFlashcardBack()"].primary') &&
                     [...document.querySelectorAll('[onclick="handleFlashcardBack()"].primary')].some(b => b.offsetHeight > 0);
  const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE) || 'null');
  return { cartes: n, ecran: (document.querySelector('.screen.active') || {}).id, finVisible, t: v.t, tj: v.tj, b: v.b, r: v.r, cn: v.cn };
}
"""

TERMINER = r"""
async () => {
  const b = [...document.querySelectorAll('[onclick="handleFlashcardBack()"].primary')].find(x => x.offsetHeight > 0);
  if(!b) return 'pas de bouton';
  b.click();
  await new Promise(r => setTimeout(r, 600));
  const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE) || 'null');
  return { ecran: (document.querySelector('.screen.active') || {}).id, t: v.t, tj: v.tj, b: v.b, r: v.r };
}
"""

FUSION = r"""
() => {
  if(typeof fusionnerMosaique !== 'function') return null;
  const base = { r: 3, c: 765, j: '2026-11-13', n: 10, g: [1, 2, 3], t: 1, tj: '2026-11-12', x: 1, s: 'es', h: [1], b: '', cn: 352 };
  const e = o => Object.assign({}, base, o);
  const f = (l, d) => { const r = fusionnerMosaique(l, d); return r && { r: r.r, c: r.c, t: r.t, tj: r.tj, b: r.b, cn: r.cn, g: r.g }; };
  return {
    // le nuage d'un autre appareil reste a « 2/3 », avec quelques carreaux de plus : le trophee ne remonte pas
    remonte: f(e({}), e({ t: 2, tj: '2026-11-11', cn: 360 })),
    // gagne d'un cote (t = 2), encore en cours de l'autre avec plus de carreaux : le trophee vient de celui qui l'a
    gagne_un_cote: f(e({ c: 720, t: 2, tj: '2026-11-12', cn: 0 }), e({ c: 780, t: 0, tj: '', g: [1, 2], cn: 0 })),
    // la fin ancienne (`b`) d'un cote : elle reste
    fin_un_cote: f(e({ t: 2, tj: '2026-11-11' }), e({ t: 0, b: '2026-11-12', cn: 340 })),
    // le nuage a deja le tableau suivant : il gagne entier
    suivant: f(e({}), { r: 4, c: 360, j: '2026-11-13', n: 5, g: [1, 2, 3], t: 0, tj: '', x: 1, s: 'es', h: [1], b: '', cn: 0 }),
    // le local a deja le tableau suivant : rien ne change
    local_devant: f({ r: 4, c: 360, j: '2026-11-13', n: 5, g: [1, 2, 3], t: 0, tj: '', x: 1, s: 'es', h: [1], b: '', cn: 0 }, e({ t: 3 })),
    // le meme etat : rien a ecrire
    pareil: f(e({}), e({}))
  };
}
"""


def jour(d):
    return datetime.datetime.strptime(d, "%Y-%m-%d").replace(hour=10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index")
    ap.add_argument("--sans-seance", action="store_true")
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
    fautes_total = []

    def ouvrir(nav, appris):
        ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 800}, service_workers="block")
        ctx.add_init_script(HORLOGE)
        page = ctx.new_page()
        erreurs = []
        page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        url = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else "")
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.evaluate(PREPARER)
        return ctx, page, url, erreurs

    def le(page, url, d, etat=None):
        """Ouvre l'app le jour d (un rechargement), apres avoir pose l'etat s'il est donne."""
        cible = int(jour(d).timestamp() * 1000)
        page.evaluate("([c, e]) => { localStorage.setItem('__horloge', JSON.stringify({ cible: c, reel: performance.timeOrigin + performance.now() }));"
                      " if(e) localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(e)); }", [cible, etat])
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        return page.evaluate(LIRE)

    def noter(cas, fautes, lignes):
        print("== %-16s %s %s" % (cas, "ok" if not fautes else "FAUTE", fautes), flush=True)
        for l in lignes:
            print("   " + json.dumps(l, ensure_ascii=False), flush=True)
        fautes_total.extend(cas + " : " + f for f in fautes)

    def bref(x):
        return {k: x.get(k) for k in ("jour", "brut", "r", "c", "t", "tj", "b", "cn", "sejour", "tableau") if k in x}

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()

            # --- l'etat de Jacques ---
            for cas in ([] if a.sans_seance else ["jacques_fermee", "jacques_terminer"]):
                ctx, page, url, err = ouvrir(nav, "es")
                l13 = le(page, url, "2026-11-13", JACQUES)
                seance = page.evaluate(JOUER)
                apres = page.evaluate(TERMINER) if cas == "jacques_terminer" else None
                l13b = le(page, url, "2026-11-13")
                l14 = le(page, url, "2026-11-14")
                l15 = le(page, url, "2026-11-15")
                f = []
                if not seance["finVisible"]:
                    f.append("la seance n'est pas arrivee a son ecran de fin (%s)" % seance["ecran"])
                if l13["r"] != 4 or l13["c"] != 352 or l13["t"] != 0:
                    f.append("le 13 a l'ouverture : rang %s, %s carreaux, t %s (attendu : rang 4, 352, 0)" % (l13["r"], l13["c"], l13["t"]))
                if l14["r"] != 4 or l15["r"] != 4:
                    f.append("le 14 / le 15 : rang %s / %s (attendu 4, le suivant)" % (l14["r"], l15["r"]))
                noter(cas, f, [{"le 13": bref(l13)}, {"seance": seance}, {"TERMINER": apres}, {"le 13, rouverte": bref(l13b)},
                               {"le 14": bref(l14)}, {"le 15": bref(l15)}] + ([{"erreurs JS": sorted(set(err))[:4]}] if err else []))
                ctx.close()

            # --- trois jours d'ouverture ---
            ctx, page, url, err = ouvrir(nav, "de")
            gagne = {"r": 5, "c": 700, "j": "2026-11-10", "n": 80, "g": [1, 2, 3, 4, 5], "t": 3, "tj": "2026-11-10", "x": 1,
                     "s": "", "h": [], "b": "", "cn": 40}
            s = [("le 10", le(page, url, "2026-11-10", gagne)), ("le 11", le(page, url, "2026-11-11")), ("le 11 encore", le(page, url, "2026-11-11")),
                 ("le 13", le(page, url, "2026-11-13")), ("le 14", le(page, url, "2026-11-14"))]
            f = []
            attendu = [(5, 3, "jour 1 sur 3"), (5, 2, "jour 2 sur 3"), (5, 2, "jour 2 sur 3"), (5, 1, "jour 3 sur 3"), (6, 0, "")]
            for (nom, x), (r, t, txt) in zip(s, attendu):
                if x["r"] != r or x["t"] != t or (txt not in x["sejour"]):
                    f.append("%s : rang %s, t %s, « %s » (attendu rang %s, t %s, « %s »)" % (nom, x["r"], x["t"], x["sejour"], r, t, txt))
            if s[-1][1]["c"] != 40:
                f.append("le suivant n'a pas garde son avance : %s carreaux (40 attendus)" % s[-1][1]["c"])
            # une semaine d'absence : un seul jour
            l1 = le(page, url, "2026-11-01", dict(gagne, tj="2026-11-01", j="2026-11-01"))
            l8 = le(page, url, "2026-11-08")
            if l8["t"] != 2:
                f.append("une semaine d'absence : t %s (2 attendu, un seul jour compte)" % l8["t"])
            noter("jours_ouverture", f, [{n: bref(x)} for n, x in s] + [{"le 1er": bref(l1)}, {"le 8": bref(l8)}])

            # --- la victoire : le jour meme est le jour 1 ---
            presque = {"r": 2, "c": 700, "j": "2026-11-13", "n": 80, "g": [1], "t": 0, "tj": "", "x": 1, "s": "", "h": [], "b": "", "cn": 0}
            v13 = le(page, url, "2026-11-13", presque)
            v13b = le(page, url, "2026-11-13")
            v14 = le(page, url, "2026-11-14")
            f = []
            if v13["t"] != 3 or "jour 1 sur 3" not in v13["sejour"] or 2 not in v13["g"]:
                f.append("le jour de la victoire : t %s, « %s », g %s" % (v13["t"], v13["sejour"], v13["g"]))
            if v13b["t"] != 3:
                f.append("rouverte le meme jour : t %s (3 attendu)" % v13b["t"])
            if v14["t"] != 2 or "jour 2 sur 3" not in v14["sejour"]:
                f.append("le lendemain : t %s, « %s »" % (v14["t"], v14["sejour"]))
            noter("victoire", f, [{"le 13": bref(v13)}, {"le 13 encore": bref(v13b)}, {"le 14": bref(v14)}])

            # --- le tableau bloque ---
            bloque = {"r": 3, "c": 760, "j": "2026-11-12", "n": 10, "g": [1, 2, 3], "t": 0, "tj": "", "x": 1, "s": "", "h": [], "b": "", "cn": 25}
            b13 = le(page, url, "2026-11-13", bloque)
            b14 = le(page, url, "2026-11-14")
            f = []
            if b13["r"] != 3 or b13["t"] != 1 or "jour 3 sur 3" not in b13["sejour"]:
                f.append("le 13 : rang %s, t %s, « %s » (attendu rang 3, t 1, « 3/3 »)" % (b13["r"], b13["t"], b13["sejour"]))
            if b14["r"] != 4 or b14["c"] != 25:
                f.append("le 14 : rang %s, %s carreaux (attendu 4, 25)" % (b14["r"], b14["c"]))
            noter("bloque", f, [{"le 13": bref(b13)}, {"le 14": bref(b14)}])

            # --- un etat de l'ancienne version, `b` pose ---
            ancien = {"r": 3, "c": 740, "j": "2026-11-12", "n": 10, "g": [1, 2, 3], "t": 0, "tj": "2026-11-12", "x": 1, "s": "", "h": [], "b": "2026-11-12", "cn": 12}
            a12 = le(page, url, "2026-11-12", ancien)
            a13 = le(page, url, "2026-11-13")
            f = []
            if a12["r"] != 3 or "jour 3 sur 3" not in a12["sejour"]:
                f.append("le jour de `b` : rang %s, « %s »" % (a12["r"], a12["sejour"]))
            if a13["r"] != 4 or a13["c"] != 12:
                f.append("le lendemain : rang %s, %s carreaux (attendu 4, 12)" % (a13["r"], a13["c"]))
            noter("ancien_b", f, [{"le 12": bref(a12)}, {"le 13": bref(a13)}])

            # --- la fusion ---
            fu = page.evaluate(FUSION)
            f = []
            if fu is None:
                f.append("fusionnerMosaique() absente (ancienne version)")
            else:
                if not fu["remonte"] or fu["remonte"]["t"] != 1 or fu["remonte"]["tj"] != "2026-11-12" or fu["remonte"]["cn"] != 360:
                    f.append("remonte : %s" % fu["remonte"])
                if not fu["gagne_un_cote"] or fu["gagne_un_cote"]["t"] != 2 or 3 not in fu["gagne_un_cote"]["g"]:
                    f.append("gagne_un_cote : %s" % fu["gagne_un_cote"])
                if not fu["fin_un_cote"] or fu["fin_un_cote"]["b"] != "2026-11-12" or fu["fin_un_cote"]["t"] != 0:
                    f.append("fin_un_cote : %s" % fu["fin_un_cote"])
                if not fu["suivant"] or fu["suivant"]["r"] != 4:
                    f.append("suivant : %s" % fu["suivant"])
                if fu["local_devant"] is not None:
                    f.append("local_devant : %s" % fu["local_devant"])
                if fu["pareil"] is not None:
                    f.append("pareil : %s" % fu["pareil"])
            noter("fusion", f, [fu])
            if err:
                print("   erreurs JS (de)", sorted(set(e for e in err if "synonymes" not in e))[:4], flush=True)
            ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not fautes_total else "%d faute(s)" % len(fautes_total)))
    sys.exit(1 if fautes_total else 0)


if __name__ == "__main__":
    main()
