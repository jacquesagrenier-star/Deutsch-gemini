# -*- coding: utf-8 -*-
"""LA GRILLE DE L'ACCUEIL NE LAISSE JAMAIS UNE TUILE SEULE (ligne 156b, decisions de Jacques du 20 nov. 2026, apres
« pas tres esthetique d'avoir 6 tuiles, puis apres ca, une »). A 360 x 740 :
  - « Tout le contenu » n'est plus une tuile : une LIGNE en verre (piste C) sous les tuiles et avant Ton tableau /
    Ton ciel -- icone dessinee dans un carre ardoise, titre, sous-titre, chevron (retourne en arabe) ; la toucher ouvre
    Tout le contenu ;
  - les tuiles restent carrees, toutes de la meme taille, et aucune rangee n'en a une seule des qu'il y en a plus d'une :
    4 -> 2 + 2, 5 -> 3 + 2, 6 -> 3 + 3, 7 -> 3 + 2 + 2 ; chaque rangee est centree ;
  - Converser est la des le premier jour (debutant, palier 1).
Les cas reels : allemand en francais et en arabe, de jour et de nuit (5 tuiles) ; avec un episode (6) ; le debutant
(4) ; l'espagnol ; l'anglais, le portugais et le japonais (essais) ; le mode Soins (4). Puis chaque nombre de tuiles de
1 a 7, impose a la grille.
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/accueil_grille.py <racine> <port> <dossier-captures> [<index-avant.html>]
(avec l'index d'avant, la sonde montre les rangees d'avant : elle mesure, sans juger)"""
import functools, http.server, io, json, os, re, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT, OUT = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
AVANT = io.open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) > 4 else None
SUF = "-avant" if AVANT else ""
PREFIXE = {"de": "deutschAI_", "es": "wortandoEs_", "en": "wortandoEn_", "pt": "wortandoPt_", "ja": "wortandoJa_"}


class Calme(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


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
# Avant de mesurer : l'accueil, le theme, et ce que le cas demande (un episode montre, le mode Soins, un nombre impose).
PREPARER = """async (a) => {
  try{ const sp = document.getElementById('splashOuverture'); if(sp) sp.remove(); }catch(e){}
  try{ applyAppTheme(a.nuit ? 'dark' : 'light'); }catch(e){}
  try{ showScreen('home'); }catch(e){}
  if(a.soins){ window.soinsActifs = () => true; window.modeAccueilSoins = () => true; try{ soinsActifs = () => true; modeAccueilSoins = () => true; }catch(e){} }
  if(a.episode){ const e = document.getElementById('episodeLigne'); if(e) e.classList.remove('hidden'); }
  if(a.impose){
    const noms = ['scenes', 'themes', 'ecouter', 'episodes', 'gardes', 'converser', 'sept'];
    const g = document.getElementById('grilleAccueil');
    if(a.impose > 6 && !g.querySelector('.tg[data-tg="sept"]')){
      const c = g.querySelector('.tg[data-tg="scenes"]').cloneNode(true); c.dataset.tg = 'sept';
      const apres = g.querySelector('.tg[data-tg="converser"]'); apres.parentNode.insertBefore(c, apres.nextSibling);
    }
    const vis = { tout: true, tableau: true, ciel: false };
    noms.slice(0, a.impose).forEach(n => { vis[n] = true; });
    try{ tuilesProposees = () => vis; }catch(e){ window.tuilesProposees = () => vis; }
  }
  try{ majPaliersAccueil(); }catch(e){}
  try{ majGrilleAccueil(); }catch(e){}
  // Converser attend la liste des conversations publiees (reseau) : on lui laisse le temps de venir, la ou il doit venir
  if(a.attendre){ let n = 0; while(!document.querySelector('.tg[data-tg="converser"]:not(.hidden)') && n++ < 40) await new Promise(r => setTimeout(r, 250)); }
  await new Promise(r => setTimeout(r, 700));
  const g = document.getElementById('grilleAccueil');
  if(g) g.scrollIntoView({ block: 'center' });
  await new Promise(r => setTimeout(r, 400));
  return true;
}"""
MESURE = """() => {
  const rect = e => { const b = e.getBoundingClientRect(); return { h: Math.round(b.top), b: Math.round(b.bottom), g: Math.round(b.left), d: Math.round(b.right), l: Math.round(b.width * 10) / 10, ht: Math.round(b.height * 10) / 10 }; };
  const g = document.getElementById('grilleAccueil'), home = document.getElementById('home');
  const vis = e => !!e && !e.classList.contains('hidden') && e.offsetParent !== null;
  const tuiles = Array.from(g.querySelectorAll('.tg:not(.tg-tab)')).filter(vis).map(b => ({ tg: b.dataset.tg, r: rect(b), lib: (b.querySelector('.tg-lib') || {}).textContent || '',
                couleur: b.classList.contains('tg-ambre') ? 'ambre' : (b.classList.contains('tg-ardoise') ? 'ardoise' : '?') }));
  const li = g.querySelector('.tg-ligne');
  let ligne = null;
  if(vis(li)){
    const titre = li.querySelector('strong'), sous = li.querySelector('.tgl-sous'), chev = li.querySelector('.tgl-chevron svg'), ico = li.querySelector('.tgl-ico');
    const cs = getComputedStyle(li);
    ligne = { r: rect(li), titre: titre ? titre.textContent.trim() : '', sous: sous ? sous.textContent.trim() : '', attendu: t('accueil_tout_titre'), sousAttendu: t('accueil_tout_sous'),
              tient: !!titre && titre.scrollWidth <= titre.clientWidth + 1 && !!sous && sous.scrollWidth <= sous.clientWidth + 1,
              svg: !!(ico && ico.querySelector('svg')), ico: ico ? rect(ico) : null, chevron: chev ? getComputedStyle(chev).transform : '', fond: cs.backgroundColor, encre: cs.color };
  }
  const ra = g.querySelector('.tg-rangee');
  return { tuiles: tuiles, ligne: ligne, rangee: vis(ra) ? rect(ra) : null, grille: rect(g), palier: (home.className.match(/palier-\\d/) || [''])[0],
           dir: document.documentElement.dir || 'ltr', nuit: document.body.getAttribute('data-theme') === 'dark', page: document.documentElement.scrollWidth,
           ecran: (document.querySelector('.screen.active') || {}).id };
}"""


def rangees(tuiles):
    """Les tuiles regroupees par rangee (le meme haut, a 3 px pres) : [[tuile, …], …]."""
    out = []
    for x in sorted(tuiles, key=lambda u: (u["r"]["h"], u["r"]["g"])):
        if out and abs(out[-1][0]["r"]["h"] - x["r"]["h"]) <= 3:
            out[-1].append(x)
        else:
            out.append([x])
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []

    def voir(nom, vrai, detail=""):
        print("    %-80s %s%s" % (nom, "ok" if vrai else "NON", (" -- " + detail) if detail and not vrai else ""), flush=True)
        if not vrai and not AVANT:
            bilan.append(nom + (" (" + detail + ")" if detail else ""))

    def juger(nom, s, attendues=None, tuiles_voulues=None):
        r = rangees(s["tuiles"])
        tailles = [len(x) for x in r]
        n = len(s["tuiles"])
        print("  %s%s : %s, %d tuiles %s -> rangees %s ; ligne %s ; page %d px" % (
            nom, " (AVANT)" if AVANT else "", s["palier"], n, [x["tg"] for x in s["tuiles"]], tailles,
            ("« %s » / « %s »" % (s["ligne"]["titre"], s["ligne"]["sous"])) if s["ligne"] else "absente", s["page"]), flush=True)
        voir("%s : aucune tuile seule sur sa rangee" % nom, n <= 1 or all(k >= 2 for k in tailles), str(tailles))
        if attendues is not None:
            voir("%s : les rangees sont %s" % (nom, attendues), tailles == attendues, str(tailles))
        if tuiles_voulues is not None:
            voir("%s : les tuiles sont %s" % (nom, tuiles_voulues), [x["tg"] for x in s["tuiles"]] == tuiles_voulues, str([x["tg"] for x in s["tuiles"]]))
        if s["tuiles"]:
            l0, h0 = s["tuiles"][0]["r"]["l"], s["tuiles"][0]["r"]["ht"]
            voir("%s : les tuiles sont carrees et de la meme taille" % nom, all(abs(x["r"]["l"] - l0) <= 1 and abs(x["r"]["ht"] - h0) <= 1 and abs(x["r"]["l"] - x["r"]["ht"]) <= 1.5 for x in s["tuiles"]),
                 str([(x["r"]["l"], x["r"]["ht"]) for x in s["tuiles"]]))
            G = s["grille"]
            voir("%s : chaque rangee est centree dans la grille" % nom, all(abs((x[0]["r"]["g"] - G["g"]) - (G["d"] - x[-1]["r"]["d"])) <= 3 for x in r),
                 str([(x[0]["r"]["g"] - G["g"], G["d"] - x[-1]["r"]["d"]) for x in r]))
        if s["tuiles"] and not AVANT:
            # un damier : deux voisines d'une rangee, et deux tuiles l'une sous l'autre (rangees de meme taille), different
            cote = all(x[k]["couleur"] != x[k + 1]["couleur"] for x in r for k in range(len(x) - 1))
            dessous = all(a[k]["couleur"] != b[k]["couleur"] for a, b in zip(r, r[1:]) if len(a) == len(b) for k in range(len(a)))
            voir("%s : les couleurs font un damier" % nom, cote and dessous and all(x["couleur"] != "?" for x in s["tuiles"]), str([[y["couleur"][:3] for y in x] for x in r]))
        voir("%s : « Tout le contenu » n'est plus une tuile carree" % nom, not any(x["tg"] == "tout" for x in s["tuiles"]))
        L = s["ligne"]
        voir("%s : la ligne « Tout le contenu » est la" % nom, bool(L))
        if L:
            bas_tuiles = max([x["r"]["b"] for x in s["tuiles"]] or [0])
            voir("%s : la ligne est sous les tuiles%s" % (nom, " et avant Ton tableau / Ton ciel" if s["rangee"] else ""),
                 L["r"]["h"] >= bas_tuiles and (not s["rangee"] or L["r"]["b"] <= s["rangee"]["h"]), "ligne %s, tuiles jusqu'a %s, rangee %s" % (L["r"], bas_tuiles, s["rangee"]))
            voir("%s : la ligne tient toute la largeur de la grille, sur 56 a 84 px de haut" % nom,
                 abs(L["r"]["g"] - s["grille"]["g"]) <= 1 and abs(L["r"]["d"] - s["grille"]["d"]) <= 1 and 56 <= L["r"]["ht"] <= 84, str(L["r"]))
            voir("%s : son titre et son sous-titre sont ceux de la langue, entiers" % nom, L["titre"] == L["attendu"] and L["sous"] == L["sousAttendu"] and bool(L["sous"]) and L["tient"],
                 "« %s » / « %s »" % (L["titre"], L["sous"]))
            voir("%s : une icone dessinee dans son carre, pas d'emoji" % nom, L["svg"] and bool(L["ico"]) and abs(L["ico"]["l"] - L["ico"]["ht"]) <= 1 and not re.search("[\U0001F300-\U0001FAFF☀-➿]", L["titre"] + L["sous"]))
            rtl = s["dir"] == "rtl"
            voir("%s : le chevron pointe %s" % (nom, "a gauche (droite a gauche)" if rtl else "a droite"), ("matrix(-1" in L["chevron"]) == rtl, L["chevron"])
            m = re.findall(r"[\d.]+", L["fond"])
            voir("%s : un verre (fond translucide), %s" % (nom, "clair le jour" if not s["nuit"] else "sombre la nuit"),
                 len(m) == 4 and float(m[3]) < 1 and ((float(m[0]) > 200) != s["nuit"]), L["fond"])
        voir("%s : la page tient en 360 px" % nom, s["page"] <= 360, "%d px" % s["page"])

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
                page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "" if apprise == "de" else "?apprendre=" + apprise), wait_until="domcontentloaded")
                page.wait_for_timeout(2500)
                page.evaluate(POSER, {"apprise": apprise, "ui": ui, "niveau": niveau, "p": PREFIXE[apprise]})
                page.reload(wait_until="domcontentloaded"); page.wait_for_timeout(4500)
                page.evaluate(FAUX_COMPTE)
                return ctx, page

            def cas(nom, apprise, ui, niveau, capture, attendues=None, tuiles_voulues=None, **prep):
                ctx, page = ouvrir(apprise, ui, niveau)
                try:
                    page.evaluate(PREPARER, dict({"nuit": False, "attendre": apprise in ("de", "es", "en") and not prep.get("soins") and not prep.get("impose")}, **prep))
                    s = page.evaluate(MESURE)
                    juger(nom, s, attendues, tuiles_voulues)
                    if capture:
                        page.screenshot(path=os.path.join(OUT, "grille-%s%s.png" % (capture, SUF)))
                    if page.erreurs and apprise == "de":
                        voir("%s : aucune erreur JavaScript" % nom, False, str(page.erreurs[:2]))
                    return ctx, page, s
                except Exception as e:
                    print("    %s : la sonde a echoue (%s)" % (nom, str(e).splitlines()[0][:160]), flush=True)
                    if not AVANT:
                        bilan.append("%s : sonde en echec" % nom)
                    return ctx, page, None

            # ---- 1. allemand, francais et arabe, jour et nuit : 5 tuiles
            for ui in ("fr", "ar"):
                for nuit in (False, True):
                    nom = "de/%s %s" % (ui, "nuit" if nuit else "jour")
                    ctx, page, s = cas(nom, "de", ui, "A2", "%s-%s" % (ui, "nuit" if nuit else "jour"), None if AVANT else [3, 2],
                                       None if AVANT else ["scenes", "themes", "ecouter", "gardes", "converser"], nuit=nuit)
                    if s and s["ligne"] and not AVANT and not nuit:
                        page.evaluate("() => document.querySelector('#grilleAccueil .tg-ligne').click()")
                        page.wait_for_timeout(1200)
                        vue = page.evaluate("() => ({ ecran: (document.querySelector('.screen.active') || {}).id, contenu: document.getElementById('home').classList.contains('vue-contenu') })")
                        voir("%s : toucher la ligne ouvre Tout le contenu" % nom, vue["ecran"] == "home" and vue["contenu"], str(vue))
                    ctx.close()

            # ---- 2. les autres nombres de tuiles, en vrai
            for nom, apprise, ui, niveau, capture, attendues, voulues, prep in (
                ("de/fr avec un episode (6)", "de", "fr", "A2", "6-tuiles", [3, 3], ["scenes", "themes", "ecouter", "episodes", "gardes", "converser"], {"episode": True}),
                ("de/fr debutant, palier 1 (4)", "de", "fr", "A1", "debutant", [2, 2], ["scenes", "themes", "ecouter", "converser"], {}),
                ("de/ar debutant, palier 1 (4)", "de", "ar", "A1", "debutant-ar", [2, 2], ["scenes", "themes", "ecouter", "converser"], {}),
                ("es/fr (5)", "es", "fr", "A2", "es", [3, 2], ["scenes", "themes", "ecouter", "gardes", "converser"], {}),
                ("mode Soins (4)", "de", "fr", "A2", "soins", [2, 2], ["soins_journee", "soins_dialogues", "soins_ecouter", "soins_telc"], {"soins": True}),
                ("mode Soins, nuit (4)", "de", "fr", "A2", "soins-nuit", [2, 2], None, {"soins": True, "nuit": True}),
                ("anglais appris (essai)", "en", "fr", "A2", "en", None, None, {}),
                ("portugais appris (essai)", "pt", "fr", "A2", "pt", None, None, {}),
                ("japonais appris (essai)", "ja", "fr", "A2", "ja", None, None, {}),
            ):
                ctx, page, s = cas(nom, apprise, ui, niveau, capture, None if AVANT else attendues, None if AVANT else voulues, **prep)
                ctx.close()

            # ---- 3. chaque nombre de tuiles, de 1 a 7, impose a la grille
            ATTENDU = {1: [1], 2: [2], 3: [3], 4: [2, 2], 5: [3, 2], 6: [3, 3], 7: [3, 2, 2]}
            for n in range(1, 8):
                ctx, page, s = cas("%d tuile(s) imposee(s)" % n, "de", "fr", "A2", "impose-%d" % n if n in (4, 7) else None, None if AVANT else ATTENDU[n], None, impose=n)
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
