# -*- coding: utf-8 -*-
"""Les etoiles suivent les seances (ligne 158, decision de Jacques du 20 nov. 2026, DECISIONS.md 3ffe92b).

    python tests/ciel_seances.py                      (de et es)
    python tests/ciel_seances.py --captures DOSSIER   (Ton ciel a 360 px, fr et ar, jour et nuit)

Quatre comptes, sur un navigateur vierge (le compte Firebase est simule : seule sa date de creation compte) :
  a1-vers-b1 : un compte A1 d'avant (Premiers pas finis, 6e escale : 13 etoiles) passe en B1 -- rien ne bouge ;
  neuf-b1    : un compte cree apres la regle, place en B1 -- il part de 0 (plus de figures offertes) ;
  a2-avant   : un compte A2 d'avant -- les 30 etoiles de l'A1 gardees, la seance suivante allume la 31e (la Lyre) ;
  bout       : la derniere etoile du voyage, puis une seance -- le deuxieme tour (la Grande Ourse, « Tour 2 »),
               toutes les figures en souvenir.
Et a chaque fois : une seance finie n'allume qu'une etoile (le meme paquet reaffiche n'en rallume pas), l'ecran
Ton ciel sans debordement, « encore N seances ». Il ouvre un navigateur : a lancer SOUS LE VERROU
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
PORT = int(os.environ.get("TON_CIEL_PORT", "8806"))

AVANT, APRES = "2026-10-01T12:00:00Z", "2026-11-25T12:00:00Z"

POSER = """
([cas]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  if(cas === 'a1-vers-b1'){ localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true })); localStorage.setItem(A1_VOYAGE_KEY, JSON.stringify({ a: true, e: 5, t: true, b: 0 })); }
  if(cas === 'neuf-b1'){ localStorage.setItem(NIVEAU_SEANCE_KEY, 'B1'); }
  if(cas === 'a2-avant'){ localStorage.setItem(NIVEAU_SEANCE_KEY, 'A2'); }
}
"""

MESURE = r"""
async ([cas, avant, apres]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  const compte = cree => Object.defineProperty(window, 'firebaseAuth', { configurable: true, writable: true,
      value: { currentUser: { uid: 'sonde', isAnonymous: false, metadata: { creationTime: cree } } } });
  await chargerCiel();
  const T = totalEtoilesCiel(), O = ordreCiel();
  const lire = async () => { const e = await etatDuCiel(); const v = e.groupes.find(x => x.g === e.courant); return { somme: e.somme, courant: e.courant, n: v.n, t: v.t, tour: e.tour, figures: e.groupes.length }; };
  const r = { T: T, figures: O.length, etapes: [] };
  if(cas === 'a1-vers-b1'){
    compte(avant);
    r.etapes.push(['A1', await lire()]);
    localStorage.setItem(NIVEAU_SEANCE_KEY, 'B1');
    r.etapes.push(['B1', await lire()]);
  }
  if(cas === 'neuf-b1'){ compte(apres); r.etapes.push(['B1', await lire()]); }
  if(cas === 'a2-avant'){ compte(avant); r.etapes.push(['A2', await lire()]); }
  if(cas === 'bout'){ compte(avant); localStorage.setItem(CIEL_COMPTE_KEY, JSON.stringify({ n: T - 1, m: 1 })); r.etapes.push(['derniere', await lire()]); }
  // une seance finie, puis le meme paquet reaffiche
  const paquet = [{ sonde: true }];
  noterSeanceLegereFinie(paquet);
  r.allumee = CIEL_FIN_SEANCE;
  noterSeanceLegereFinie(paquet);
  r.etapes.push(['apres une seance', await lire()]);
  r.stocke = compteCielStocke();
  // Ton ciel
  await ouvrirCiel(); await pause(400);
  const ciel = document.getElementById('tonCiel');
  r.page = { actif: (document.querySelector('.screen.active') || {}).id, total: document.getElementById('tcTotal').textContent,
             pastilles: document.querySelectorAll('.tc-pastille').length, actives: [...document.querySelectorAll('.tc-pastille.active')].map(b => b.textContent),
             info: document.getElementById('tcInfo').innerText.replace(/\n+/g, ' | '),
             debord: ciel.scrollWidth > ciel.clientWidth + 1 || document.documentElement.scrollWidth > window.innerWidth };
  return r;
}
"""


def juger(cas, r):
    f = []
    et = dict((k, v) for k, v in r["etapes"])
    apres = et["apres une seance"]
    if r["T"] != 434 or r["figures"] != 57:
        f.append("le ciel : %s etoiles, %s figures" % (r["T"], r["figures"]))
    if cas == "a1-vers-b1":
        if et["A1"]["somme"] != 13 or et["A1"]["courant"] != "gemeaux" or et["A1"]["n"] != 5:
            f.append("A1 : %s" % et["A1"])
        if et["B1"] != et["A1"]:
            f.append("le passage en B1 a bouge le ciel : %s" % et["B1"])
        attendu = 14
    elif cas == "neuf-b1":
        if et["B1"]["somme"] != 0 or et["B1"]["courant"] != "ourse":
            f.append("neuf B1 : %s" % et["B1"])
        attendu = 1
    elif cas == "a2-avant":
        if et["A2"]["somme"] != 30 or et["A2"]["courant"] != "lyre" or et["A2"]["n"] != 0:
            f.append("A2 d'avant : %s" % et["A2"])
        if apres["courant"] != "lyre" or apres["n"] != 1:
            f.append("la 31e : %s" % apres)
        attendu = 31
    else:
        if et["derniere"]["tour"] != 0 or et["derniere"]["n"] != et["derniere"]["t"] - 1:
            f.append("derniere etoile : %s" % et["derniere"])
        if apres["tour"] != 1 or apres["courant"] != "ourse" or apres["n"] != 0 or apres["figures"] != 57:
            f.append("deuxieme tour : %s" % apres)
        attendu = r["T"]
    if r["stocke"] != attendu or apres["somme"] != attendu:
        f.append("une seance (le paquet reaffiche compris) : %s etoiles, attendu %s" % (r["stocke"], attendu))
    if r["allumee"] != attendu - 1:
        f.append("etoile allumee a l'ecran de fin : rang %s" % r["allumee"])
    p = r["page"]
    if p["actif"] != "tonCiel" or p["debord"]:
        f.append("Ton ciel : %s" % p)
    if cas == "bout" and ("2" not in p["total"] or p["pastilles"] != 57):
        f.append("Ton ciel au deuxieme tour : %s" % p)
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
    CAS = []
    for cas in ("a1-vers-b1", "neuf-b1", "a2-avant", "bout"):
        CAS += [("de", "fr", "light", cas), ("de", "ar", "dark", cas)]
    CAS += [("de", "fr", "dark", "a2-avant"), ("de", "ar", "light", "a2-avant"), ("es", "fr", "light", "a2-avant"), ("es", "fr", "dark", "a1-vers-b1"),
            ("es", "ar", "light", "bout")]
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, ui, theme, cas in CAS:
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 780}, service_workers="block")
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
                nom = "%s-%s-%s-360-%s" % (appris, ui, theme, cas)
                try:
                    r = page.evaluate(MESURE, [cas, AVANT, APRES])
                    fautes = juger(cas, r)
                    if a.captures:
                        os.makedirs(a.captures, exist_ok=True)
                        page.screenshot(path=os.path.join(a.captures, nom + ".png"))
                except Exception as e:
                    r = None
                    fautes = [str(e).split("\n")[0][:300]]
                total += 1 if fautes else 0
                print("== %s %s %s" % (nom, "ok" if not fautes else "FAUTE", fautes), flush=True)
                print("   " + json.dumps(r, ensure_ascii=False)[:1200], flush=True)
                erreurs = [e for e in erreurs if "synonymes" not in e]
                if erreurs:
                    print("   erreurs JS", sorted(set(erreurs))[:4], flush=True)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not total else "%d cas en defaut" % total))


if __name__ == "__main__":
    main()
