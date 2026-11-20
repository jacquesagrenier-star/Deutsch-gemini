# -*- coding: utf-8 -*-
"""« Converser » sur l'accueil : UNE TUILE COMME LES AUTRES (ligne 154, decision de Jacques du 20 nov. 2026), a la
place de la ligne posee sous « Ecouter, repeter » le 16 nov. A 360 x 740 :
  - francais et arabe, de jour et de nuit (allemand appris, palier 3) : la tuile est dans la grille, de la meme taille
    que ses voisines, avec une icone DESSINEE (un svg, pas d'emoji) et son libelle entier ; la ligne n'existe plus ;
    la page tient en 360 px ;
  - la toucher ouvre la LISTE des conversations, et la liste montre exactement les conversations PUBLIEES de la langue
    apprise (index.json, « publies » : elle grandit toute seule) ; « ‹ » ramene a l'accueil ;
  - l'espagnol appris : la meme tuile, la liste espagnole ;
  - les 11 langues d'interface : le libelle tient dans la tuile ;
  - un debutant (palier 1) la voit des le premier jour (depuis la ligne 156b ; avant, elle attendait le palier 2).
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/converser_tuile.py <racine> <port> <dossier-captures> [<index-avant.html>]
(avec l'index d'avant en 4e argument, la sonde montre l'etat d'avant : la ligne, pas de tuile ; elle ne juge pas)"""
import functools, http.server, io, json, os, re, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT, OUT = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
AVANT = io.open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) > 4 else None
SUF = "-avant" if AVANT else ""
LANGUES_UI = {"de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"], "es": ["fr", "en", "pt", "ar", "de"]}
PREFIXE = {"de": "deutschAI_", "es": "wortandoEs_"}


class Calme(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


def publiees(langue):
    """Les conversations que la liste doit montrer : celles des lots publies, dans la langue apprise."""
    d = os.path.join(RACINE, "visuel", "prototype", "conversation", "donnees")
    idx = json.load(io.open(os.path.join(d, "index.json"), encoding="utf-8"))
    ids = []
    for lot in idx["lots"]:
        if lot not in idx.get("publies", []):
            continue
        f = os.path.join(d, "lot-%s.json" % lot)
        if os.path.exists(f):
            for c in json.load(io.open(f, encoding="utf-8"))["conversations"]:
                if langue in c.get("langues", []):
                    ids.append(c["id"])
    return ids


POSER = """(a) => {
  localStorage.clear();
  localStorage.setItem('wortando_langueApprise', a.apprise);
  localStorage.setItem(a.p + 'uiLang', a.ui); localStorage.setItem(a.p + 'setupDone', '1'); localStorage.setItem(a.p + 'onboardingSeen', '1');
  if(a.niveau) localStorage.setItem(a.p + 'niveauSeance', a.niveau);
}"""
FAUX_COMPTE = """() => { window.firebaseAuth = window.firebaseAuth || {};
  const u = { uid: 'demo-locale', email: '', displayName: '', isAnonymous: false };
  try{ Object.defineProperty(window.firebaseAuth, 'currentUser', { value: u, configurable: true }); }catch(e){ window.firebaseAuth.currentUser = u; }
  return true; }"""
ACCUEIL = """async (nuit) => {
  try{ const sp = document.getElementById('splashOuverture'); if(sp) sp.remove(); }catch(e){}
  try{ applyAppTheme(nuit ? 'dark' : 'light'); }catch(e){}
  try{ showScreen('home'); }catch(e){}
  try{ majPaliersAccueil(); }catch(e){}
  // la liste des conversations publiees est lue au reseau : on laisse a la tuile (ou a la ligne) le temps de venir
  const vue = () => { const tu = document.querySelector('.tg[data-tg="converser"]'), li = document.getElementById('converserLigne');
                      return (tu && !tu.classList.contains('hidden')) || (li && !li.classList.contains('hidden')); };
  let n = 0; while(!vue() && n++ < 40) await new Promise(r => setTimeout(r, 250));
  await new Promise(r => setTimeout(r, 600));
  const rect = e => { const b = e.getBoundingClientRect(); return { h: Math.round(b.top), b: Math.round(b.bottom), g: Math.round(b.left), d: Math.round(b.right), l: Math.round(b.width), ht: Math.round(b.height) }; };
  const tuiles = Array.from(document.querySelectorAll('#grilleAccueil .tg')).filter(b => !b.classList.contains('hidden') && b.offsetParent !== null && !b.classList.contains('tg-tab'))
    .map(b => { const lib = b.querySelector('.tg-lib'); return { tg: b.dataset.tg, lib: lib ? lib.textContent.trim() : '', r: rect(b), svg: !!b.querySelector('.tg-ico svg'),
                couleur: b.classList.contains('tg-ambre') ? 'ambre' : (b.classList.contains('tg-ardoise') ? 'ardoise' : '?'),
                libTient: lib ? (lib.scrollWidth <= lib.clientWidth + 1 && lib.scrollHeight <= lib.clientHeight + 1) : false,
                encre: lib ? getComputedStyle(lib).color : '' }; });
  const ligne = document.getElementById('converserLigne');
  const home = document.getElementById('home');
  return { tuiles: tuiles, ligne: ligne ? (ligne.classList.contains('hidden') || ligne.offsetParent === null ? 'cachee' : 'visible : ' + ligne.textContent.replace(/\\s+/g, ' ').trim().slice(0, 80)) : 'absente',
           palier: (home.className.match(/palier-\\d/) || [''])[0], nuit: document.body.getAttribute('data-theme') === 'dark', dir: document.documentElement.dir || '',
           page: document.documentElement.scrollWidth, ecran: (document.querySelector('.screen.active') || {}).id };
}"""
LISTE = """async () => {
  let n = 0;
  while(n++ < 80){ const a = document.querySelectorAll('.liste a'); if(a.length) break; await new Promise(r => setTimeout(r, 250)); }
  await new Promise(r => setTimeout(r, 500));
  return { titres: Array.from(document.querySelectorAll('.liste a b')).map(b => b.textContent.trim()),
           ids: Array.from(document.querySelectorAll('.liste a')).map(a => (new URL(a.href)).searchParams.get('c')),
           surtitre: (document.getElementById('surtitre') || {}).textContent || '', page: document.documentElement.scrollWidth,
           enConversation: !!document.querySelector('.repondre, .carte.debut') };
}"""


def main():
    os.makedirs(OUT, exist_ok=True)
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []

    def voir(nom, vrai, detail=""):
        print("    %-78s %s%s" % (nom, "ok" if vrai else "NON", (" -- " + detail) if detail and not vrai else ""), flush=True)
        if not vrai and not AVANT:
            bilan.append(nom + (" (" + detail + ")" if detail else ""))

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()

            def ouvrir(apprise, ui, niveau):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 740}, device_scale_factor=2, service_workers="block", has_touch=True, is_mobile=True)
                for motif in ("**/*firebase*", "**/*gstatic*", "**/*googleapis*", "**/*recaptcha*"):
                    ctx.route(motif, lambda r: r.abort())
                if AVANT:
                    ctx.route("**/index.html*", lambda r: r.fulfill(status=200, content_type="text/html; charset=utf-8", body=AVANT))
                page = ctx.new_page()
                page.erreurs = []
                page.on("pageerror", lambda e: page.erreurs.append(str(e).splitlines()[0][:140] if str(e) else ""))
                page.on("dialog", lambda d: d.dismiss())
                adresse = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if apprise == "es" else "")
                page.goto(adresse, wait_until="domcontentloaded")
                page.wait_for_timeout(2500)
                page.evaluate(POSER, {"apprise": apprise, "ui": ui, "niveau": niveau, "p": PREFIXE[apprise]})
                page.reload(wait_until="domcontentloaded"); page.wait_for_timeout(4500)
                page.evaluate(FAUX_COMPTE)
                return ctx, page

            def tuile(s):
                return next((x for x in s["tuiles"] if x["tg"] == "converser"), None)

            # ---- 1. francais et arabe, jour et nuit, allemand appris
            for ui in ("fr", "ar"):
                for nuit in (False, True):
                    nom = "de/%s %s" % (ui, "nuit" if nuit else "jour")
                    ctx, page = ouvrir("de", ui, "A2")
                    s = page.evaluate(ACCUEIL, nuit)
                    tu = tuile(s)
                    print("  %s%s : %s, tuiles %s ; ligne %s ; page %d px" % (nom, " (AVANT)" if AVANT else "", s["palier"], [(x["tg"], x["lib"], x["couleur"]) for x in s["tuiles"]], s["ligne"], s["page"]), flush=True)
                    voir("%s : la tuile Converser est dans la grille" % nom, bool(tu))
                    voir("%s : la ligne « Converser » n'existe plus" % nom, s["ligne"] == "absente", s["ligne"])
                    if tu:
                        autres = [x for x in s["tuiles"] if x["tg"] != "converser"]
                        voir("%s : la meme taille que les autres tuiles" % nom, all(abs(x["r"]["l"] - tu["r"]["l"]) <= 1 and abs(x["r"]["ht"] - tu["r"]["ht"]) <= 1 for x in autres), "%s contre %s" % (tu["r"], [x["r"]["l"] for x in autres]))
                        voir("%s : une icone dessinee, pas d'emoji" % nom, tu["svg"] and not re.search("[\U0001F300-\U0001FAFF☀-➿]", tu["lib"]), tu["lib"])
                        voir("%s : le libelle « %s » tient dans la tuile" % (nom, tu["lib"]), bool(tu["lib"]) and tu["libTient"])
                        ordre = [x["tg"] for x in s["tuiles"]]
                        # ligne 156b : « Tout le contenu » n'est plus une tuile (une ligne dessous) ; Converser ferme les tuiles
                        voir("%s : elle est la derniere des tuiles, dans la rangee du bas" % nom, ordre[-1] == "converser" and "tout" not in ordre and len(ordre) >= 4, str(ordre))
                        voir("%s : les couleurs alternent toujours" % nom, all(s["tuiles"][k]["couleur"] != s["tuiles"][k + 1]["couleur"] for k in range(len(s["tuiles"]) - 1)), str([x["couleur"] for x in s["tuiles"]]))
                    voir("%s : la nuit est bien %s" % (nom, "allumee" if nuit else "eteinte"), s["nuit"] == nuit)
                    voir("%s : la page tient en 360 px" % nom, s["page"] <= 360, "%d px" % s["page"])
                    page.evaluate("() => { const g = document.getElementById('grilleAccueil'); if(g) g.scrollIntoView({ block: 'center' }); }")
                    page.wait_for_timeout(500)
                    page.screenshot(path=os.path.join(OUT, "converser-%s-%s%s.png" % (ui, "nuit" if nuit else "jour", SUF)))
                    # ---- la liste
                    if tu and not AVANT:
                        attendues = publiees("de")
                        page.evaluate("() => document.querySelector('.tg[data-tg=\"converser\"]').click()")
                        page.wait_for_timeout(2500)
                        ecran = page.evaluate("() => ({ ecran: (document.querySelector('.screen.active') || {}).id, src: (document.getElementById('sceneCadre') || {}).src || '' })")
                        cadre = next((f for f in page.frames if "conversation.html" in f.url), None)
                        voir("%s : toucher la tuile ouvre la page des conversations, sur la liste" % nom, ecran["ecran"] == "sceneSeance" and cadre is not None and "&c=" not in ecran["src"], str(ecran)[:150])
                        if cadre:
                            l = cadre.evaluate(LISTE)
                            print("    liste : %d conversations %s ; publiees dans les donnees : %s" % (len(l["ids"]), l["titres"], attendues))
                            voir("%s : la liste montre exactement les conversations publiees (%d)" % (nom, len(attendues)), l["ids"] == attendues, "%s" % l["ids"])
                            voir("%s : la liste tient en 360 px" % nom, l["page"] <= 360, "%d px" % l["page"])
                            page.screenshot(path=os.path.join(OUT, "converser-liste-%s-%s.png" % (ui, "nuit" if nuit else "jour")))
                            cadre.evaluate("() => document.getElementById('retour').click()")
                            page.wait_for_timeout(1500)
                            retour = page.evaluate("() => (document.querySelector('.screen.active') || {}).id")
                            voir("%s : « ‹ » depuis la liste ramene a l'accueil" % nom, retour == "home", str(retour))
                    if page.erreurs:
                        voir("%s : aucune erreur JavaScript" % nom, False, str(page.erreurs[:2]))
                    ctx.close()

            if not AVANT:
                # ---- 2. l'espagnol appris
                ctx, page = ouvrir("es", "fr", "A2")
                s = page.evaluate(ACCUEIL, False)
                tu = tuile(s)
                print("  es/fr jour : %s, tuiles %s ; ligne %s" % (s["palier"], [(x["tg"], x["lib"]) for x in s["tuiles"]], s["ligne"]), flush=True)
                voir("es/fr : la tuile Converser est dans la grille", bool(tu))
                if tu:
                    attendues = publiees("es")
                    page.evaluate("() => document.querySelector('.tg[data-tg=\"converser\"]').click()")
                    page.wait_for_timeout(2500)
                    cadre = next((f for f in page.frames if "conversation.html" in f.url), None)
                    l = cadre.evaluate(LISTE) if cadre else {"ids": [], "titres": []}
                    print("    liste : %s ; publiees : %s" % (l["titres"], attendues))
                    voir("es/fr : la liste montre les conversations espagnoles publiees (%d)" % len(attendues), l["ids"] == attendues and "apprendre=es" in (cadre.url if cadre else ""), str(l["ids"]))
                ctx.close()

                # ---- 3. les 11 langues d'interface : le libelle tient
                for apprise in ("de", "es"):
                    for ui in LANGUES_UI[apprise]:
                        if (apprise, ui) in (("de", "fr"), ("de", "ar"), ("es", "fr")):
                            continue
                        ctx, page = ouvrir(apprise, ui, "A2")
                        s = page.evaluate(ACCUEIL, False)
                        tu = tuile(s)
                        voir("%s/%s : la tuile est la, son libelle « %s » tient, la page fait 360 px" % (apprise, ui, tu["lib"] if tu else "?"),
                             bool(tu) and bool(tu["lib"]) and tu["libTient"] and s["page"] <= 360, "tuile %s, page %d" % (tu, s["page"]))
                        if ui in ("ru", "de", "uk"):
                            page.evaluate("() => { const g = document.getElementById('grilleAccueil'); if(g) g.scrollIntoView({ block: 'center' }); }")
                            page.wait_for_timeout(400)
                            page.screenshot(path=os.path.join(OUT, "converser-%s-%s.png" % (apprise, ui)))
                        ctx.close()

                # ---- 4. le debutant (palier 1) la voit des le premier jour (ligne 156b, Jacques, 20 nov. :
                #         « On a l'idee de mettre converser tout de suite. »)
                ctx, page = ouvrir("de", "fr", "A1")
                s = page.evaluate(ACCUEIL, False)
                print("  debutant : %s, tuiles %s" % (s["palier"], [x["tg"] for x in s["tuiles"]]), flush=True)
                voir("debutant (palier 1) : la tuile Converser est la des le premier jour", s["palier"] == "palier-1" and bool(tuile(s)), "%s, %s" % (s["palier"], [x["tg"] for x in s["tuiles"]]))
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    if AVANT:
        print("MESURE D'AVANT : pas de bilan")
    else:
        print("BILAN OK" if not bilan else "BILAN A REVOIR : " + " | ".join(bilan))


if __name__ == "__main__":
    main()
