# -*- coding: utf-8 -*-
"""La seance hors ligne de l'app installee, de bout en bout (v967, v969).

    python tests/hors_ligne.py            # allemand
    python tests/hors_ligne.py --app es   # espagnol

Ce que fait l'app installee avec @capacitor/filesystem, simule ici par un faux
systeme de fichiers en memoire (window.__fs) :
  1. le web n'est pas touche : sans le module, rien ne tourne ;
  2. METTRE DE COTE : la seance a venir (cartes de mots ET exercices de
     phrases), ses voix et le lecteur sont ranges ; la seance en ligne ne voit
     rien passer (cycle des formes, paquet courant intacts) ;
  3. LE LECTEUR : chaque carte est jouee, avec la bonne reponse, sauf une
     phrase ratee expres, qui doit revenir plus loin ;
  4. RECOLLER : une revision par carte (la derniere reponse), « repeter » et
     la grammaire pour l'objectif seulement ; un second recollage ne compte rien.

Le lecteur est ouvert seul (sans la page hors ligne de l'app, qui vit dans le
depot wortando-ios) : il atteint alors les modules par window.parent, qui est
la page elle-meme.

Il ne prouve pas ce que seul un telephone dit : la place reelle, la vitesse du
telechargement, les voix jouees. Pour cela, l'essai en mode avion.
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
PORT = 8793

FAUX_FS = r"""
window.__fs = window.__fs || {};
window.__telecharges = 0;
(function(){
  const fs = window.__fs;
  const cle = (o, p) => (o.directory || 'DATA') + ':' + (p || o.path);
  const F = {
    readFile: async o => { const k = cle(o); if(!(k in fs)) throw new Error('File does not exist'); return { data: fs[k] }; },
    writeFile: async o => { fs[cle(o)] = o.data; return {}; },
    deleteFile: async o => { delete fs[cle(o)]; return {}; },
    mkdir: async o => ({}),
    rmdir: async o => { const pre = cle(o) + '/'; Object.keys(fs).forEach(k => { if(k.startsWith(pre)) delete fs[k]; }); return {}; },
    readdir: async o => { const pre = cle(o) + '/'; const n = Object.keys(fs).filter(k => k.startsWith(pre)).map(k => ({ name: k.slice(pre.length) }));
                          if(!n.length) throw new Error('nope'); return { files: n }; },
    copy: async o => { const a = o.directory + ':' + o.from; if(!(a in fs)) throw new Error('nope'); fs[(o.toDirectory || o.directory) + ':' + o.to] = fs[a]; return {}; },
    rename: async o => { const a = o.directory + ':' + o.from + '/', b = (o.toDirectory || o.directory) + ':' + o.to + '/';
                         Object.keys(fs).forEach(k => { if(k.startsWith(a)){ fs[b + k.slice(a.length)] = fs[k]; delete fs[k]; } }); return {}; },
    downloadFile: async o => { window.__telecharges++; fs[cle(o)] = 'SUQz'; return { path: o.path }; }
  };
  window.Capacitor = { isNativePlatform: () => true, getPlatform: () => 'ios',
    Plugins: { Filesystem: F,
      LocalNotifications: { schedule: async () => ({}), cancel: async () => ({}), checkPermissions: async () => ({ display: 'granted' }), requestPermissions: async () => ({ display: 'granted' }) },
      Haptics: { impact: async () => ({}), notification: async () => ({}), vibrate: async () => ({}) } } };
})();
"""

# Des mots deja vus, pour que la seance ait des revisions et des phrases.
PROGRESSION = """() => {
    const items = paquetDuNiveau('A1').slice(0, 120);
    items.forEach(it => setWordState(it.themeId, it.index,
        { mastered: false, due: Date.now() - 3600000, reviews: 3, srsHits: 1 }));
    return items.length;
}"""

# Joue la carte a l'ecran avec la bonne reponse (ou une fausse si rater).
JOUER = """async ([c, rater]) => {
    const $ = id => document.getElementById(id);
    const attendre = () => new Promise(r => setTimeout(r, 30));
    if(c.m !== 'phrase'){
        $('hlCarteBloc').click(); await attendre();
        (rater ? $('hlEncore') : $('hlContinuer')).click(); await attendre();
        return 'carte';
    }
    const z = $('hlPhrase');
    const boutons = () => Array.from(z.querySelectorAll('.hl-choix button'));
    const verifier = () => z.querySelector('.hl-verifier').click();
    const saisir = v => { const ch = z.querySelector('.hl-saisie'); ch.value = v; };
    if(c.f === 'ecoute') boutons().find(b => (b.textContent === c.sens) !== rater).click();
    else if(c.f === 'trou') boutons()[c.options.findIndex(o => !!o.juste !== rater)].click();
    else if(c.f === 'gram' && c.options) boutons().find(b => c.rep.some(a => a.toLowerCase() === b.textContent.toLowerCase()) !== rater).click();
    else if(c.f === 'gram'){ saisir(rater ? 'zzz' : c.rep[0]); verifier(); }
    else if(c.f === 'dictee'){ saisir(rater ? 'zzz' : c.de); verifier(); }
    else if(c.f === 'dictee_mot'){ saisir(rater ? 'zzz' : c.mot); verifier(); }
    else if(c.f === 'ordre'){
        const voulus = rater ? c.mots.slice().reverse() : c.mots;
        for(const m of voulus){
            const t = Array.from(z.querySelectorAll('.hl-banque .hl-tuile')).find(x => x.textContent === m);
            if(t) t.click();
        }
        verifier();
    }
    await attendre();
    const retour = z.querySelector('.hl-retour');
    const verdict = retour && !retour.hidden ? (retour.classList.contains('bon') ? 'bon' : 'faux') : 'sans';
    const suite = Array.from(z.querySelectorAll('.hl-primaire')).find(b => !b.hidden && !b.classList.contains('hl-verifier'));
    if(!suite) return 'BLOQUE:' + c.f;
    suite.click();
    await attendre();
    return c.f + ':' + verdict;
}"""


def servir():
    gestion = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    gestion.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main():
    from playwright.sync_api import sync_playwright
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="de", choices=["de", "es"])
    a = ap.parse_args()
    url = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if a.app == "es" else "")
    srv = servir()
    fautes = []

    def verifier(cond, quoi):
        print(("  ok    " if cond else "  FAUTE ") + quoi)
        if not cond:
            fautes.append(quoi)

    with sync_playwright() as p:
        b = p.chromium.launch()

        print("1. Le web")
        pg = b.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(url)
        pg.wait_for_timeout(5000)
        verifier(pg.evaluate("horsLignePossible()") is False, "sans module, horsLignePossible() est faux")
        verifier(pg.evaluate("document.getElementById('spHorsLigne').classList.contains('hidden')"), "la mention reste cachee")
        verifier(pg.evaluate("horsLigneApresRestauration().then(() => 'ok')") == "ok", "le recollage rend tout de suite")
        verifier(not err, "aucune erreur JavaScript %s" % (err[:2] if err else ""))
        pg.close()

        print("2. Mettre de cote")
        ctx = b.new_context()
        ctx.add_init_script(FAUX_FS)
        pg = ctx.new_page()
        err = []
        pg.on("pageerror", lambda e: err.append(str(e)))
        pg.goto(url)
        pg.wait_for_timeout(9000)
        pg.evaluate("window.uidCourant = () => 'u-essai-123'")
        pg.evaluate(PROGRESSION)
        avant = pg.evaluate("[localStorage.getItem(CYCLE_FORMES_KEY), currentCardsFull === null ? 'null' : typeof currentCardsFull]")
        pg.evaluate("mettreSeanceDeCote()")
        pg.wait_for_function("JSON.parse(localStorage.getItem('wortando_horsLigne') || 'null') !== null", timeout=90000)
        apres = pg.evaluate("[localStorage.getItem(CYCLE_FORMES_KEY), currentCardsFull === null ? 'null' : typeof currentCardsFull]")
        fs = pg.evaluate("window.__fs")
        seance = json.loads(fs["CACHE:hors-ligne/seance.json"])
        cartes = seance["cartes"]
        formes = {}
        for c in cartes:
            k = c.get("f") or c["m"]
            formes[k] = formes.get(k, 0) + 1
        print("        %d cartes : %s" % (len(cartes), json.dumps(formes, ensure_ascii=False)))
        verifier(len(cartes) >= 30, "au moins 30 cartes avec des revisions dues")
        verifier(any(c["m"] == "phrase" for c in cartes), "des exercices de phrases")
        verifier(avant == apres, "le cycle des formes et le paquet en ligne sont intacts (%s)" % apres)
        verifier(not any(k.startswith("CACHE:hors-ligne-neuf/") for k in fs), "pas de dossier neuf qui traine")
        sons = [k for k in fs if k.startswith("CACHE:hors-ligne/sons/")]
        verifier(len(sons) > 0, "%d voix rangees" % len(sons))
        verifier(pg.evaluate("!document.getElementById('spHorsLigne').classList.contains('hidden')"), "la mention parait")
        verifier(not err, "aucune erreur JavaScript %s" % (err[:2] if err else ""))

        print("3. Le lecteur")
        pre = "window.__fs = " + json.dumps({"CACHE:hors-ligne/seance.json": fs["CACHE:hors-ligne/seance.json"]}) + ";"
        ctx2 = b.new_context()
        ctx2.add_init_script(pre + FAUX_FS)
        pl = ctx2.new_page()
        err2 = []
        pl.on("pageerror", lambda e: err2.append(str(e)))
        pl.set_content(fs["CACHE:hors-ligne/lecteur.html"])
        pl.wait_for_timeout(800)
        verifier(not pl.evaluate("document.getElementById('hlAccueil').hidden"), "l'accueil hors ligne parait")
        pl.click("#hlCommencer")
        rate = next((i for i, c in enumerate(cartes) if c.get("f") in ("ecoute", "trou", "dictee", "ordre")), None)
        vus, joues, revenue = 0, [], False
        while vus < len(cartes) * 2 + 5:
            if not pl.evaluate("document.getElementById('hlFin').hidden"):
                break
            idx = int(pl.evaluate("document.body.getAttribute('data-carte')"))
            rater = idx == rate and idx not in [j for j, _ in joues]
            if idx == rate and idx in [j for j, _ in joues]:
                revenue = True
            v = pl.evaluate(JOUER, [cartes[idx], rater])
            joues.append((idx, v))
            vus += 1
            if v.startswith("BLOQUE"):
                print("        bloque sur : " + json.dumps(cartes[idx], ensure_ascii=False)[:300])
                break
        verdicts = [v for _, v in joues]
        bloques = [v for v in verdicts if v.startswith("BLOQUE")]
        verifier(not bloques, "chaque forme se joue jusqu'au bout %s" % (bloques[:3] if bloques else ""))
        verifier(not pl.evaluate("document.getElementById('hlFin').hidden"), "la fin de seance arrive (%d gestes)" % len(joues))
        verifier(all(v.endswith(":bon") or v.endswith(":sans") or v == "carte" for i, v in enumerate(verdicts) if joues[i][0] != rate or i != [j for j, _ in joues].index(rate)),
                 "toutes les bonnes reponses sont jugees bonnes")
        if rate is not None:
            verifier(revenue, "la phrase ratee (%s) revient plus loin" % cartes[rate]["f"])
        journal = json.loads(pl.evaluate("window.__fs['DATA:hors-ligne-journal.json']"))["entrees"]
        verifier(len(journal) == len(joues), "une ligne de journal par reponse (%d)" % len(journal))
        verifier(not err2, "aucune erreur JavaScript %s" % (err2[:2] if err2 else ""))

        print("4. Recoller")
        pg.evaluate("j => { window.__fs['DATA:hors-ligne-journal.json'] = j; }",
                    json.dumps({"entrees": journal}))
        groupes = set()
        for e in journal:
            if e["juste"] is None:
                groupes.add("n:%s:%s" % (e["k"], e["i"]))
            elif e.get("g") or e["k"] is None:
                groupes.add("g:" + (e.get("g") or e["id"]))
            else:
                groupes.add("%s:%s" % (e["k"], e["i"]))
        c0 = pg.evaluate("getDailyActivityCount()")
        pg.evaluate("recollerHorsLigne()")
        pg.wait_for_timeout(800)
        c1 = pg.evaluate("getDailyActivityCount()")
        print("        objectif %d -> %d, %d groupes (cartes, repeter, grammaire)" % (c0, c1, len(groupes)))
        verifier(0 < c1 - c0 <= len(groupes), "l'objectif avance, une fois par groupe au plus")
        verifier(json.loads(pg.evaluate("window.__fs['DATA:hors-ligne-journal.json']"))["entrees"] == [], "le journal est vide apres")
        pg.evaluate("j => { window.__fs['DATA:hors-ligne-journal.json'] = j; recollerHorsLigne(); }", json.dumps({"entrees": journal}))
        pg.wait_for_timeout(800)
        verifier(pg.evaluate("getDailyActivityCount()") == c1, "un second recollage ne compte rien")
        pg.evaluate("effacerHorsLigneDuCompte('u-essai-123')")
        pg.wait_for_timeout(300)
        fs = pg.evaluate("window.__fs")
        verifier(not any(k.startswith("CACHE:hors-ligne/") for k in fs), "« Supprimer mon compte » efface la seance rangee")
        verifier(not err, "aucune erreur JavaScript %s" % (err[:2] if err else ""))
        b.close()
    srv.shutdown()
    print("\n%s" % ("OK : la seance hors ligne tient." if not fautes else "%d FAUTE(S)." % len(fautes)))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
