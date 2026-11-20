# -*- coding: utf-8 -*-
"""Le tableau en plein ecran se ferme par un bouton qu'on VOIT (ligne 155, retour de Jacques du 20 nov. 2026).

    python tests/mosaique_fermer.py                     (de et es, fr et ar, jour et nuit, 360 x 640 et 360 x 780)
    python tests/mosaique_fermer.py --captures DOSSIER  (une capture de la fiche et une de l'agrandissement par cas)
    python tests/mosaique_fermer.py --index AUTRE.html  (sert ce fichier a la place d'index.html : l'ancienne version)

Ne de Jacques, en espagnol, apres le tableau de Riquer : « on ne voit pas comment retourner a l'accueil. Je me suis
rendu compte qu'il fallait que je clique n'importe ou, sauf dans la mosaique. » La fiche du tableau (#mosaiquePlein)
n'avait aucun bouton ; le tableau, lui, ouvre l'agrandissement (themes/zoom.js, son « × »). Pour chaque cas, un tableau
GAGNE (avec la notice du peintre, le plus long) et le tableau EN COURS :
  - le rond « ‹ » est la, a l'ecran, a sa taille, en haut a gauche (a droite en arabe), au premier plan, sans rien
    recouvrir, avec le texte cache « ‹ Retour » de la langue d'interface ;
  - le toucher sur le rond ferme la fiche et laisse l'accueil ;
  - le toucher sur le tableau ouvre l'agrandissement, dont le « × » est a l'ecran et au premier plan ; il le ferme
    et rend la fiche ;
  - le toucher a cote du tableau ferme toujours la fiche.
Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
"""
import argparse
import functools
import http.server
import os
import socketserver
import sys
import threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("MOSAIQUE_FERMER_PORT", "8828"))

PREPARER = """
([ui]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  if(ui) localStorage.setItem(UI_LANG_KEY, ui);
}
"""

# pose l'etat (tableaux 1 a 3 gagnes, le 4e en cours), le theme, et ouvre la fiche
OUVRIR = r"""
async ([appris, theme, rang]) => {
  await chargerMosaiques(); await chargerPeintres();
  const es = appris === 'es';
  localStorage.setItem(MOSAIQUE_CLE, JSON.stringify({ r: 4, c: 420, g: [1, 2, 3], j: getTodayStr(), n: 0, x: 1,
    s: es ? 'es' : '', h: es ? [1] : [], b: '', tj: '', t: 0, cn: 0 }));
  try{ applyAppTheme(theme); }catch(e){ document.body.setAttribute('data-theme', theme); }
  goHome();
  ouvrirMosaiquePleinEcran(rang || undefined);
  for(let i = 0; i < 40; i++){
    await new Promise(r => setTimeout(r, 100));
    const l = document.getElementById('mosaiquePleinLegende');
    if(l && l.textContent.trim() && !document.getElementById('mosaiquePlein').classList.contains('hidden')) break;
  }
  await new Promise(r => setTimeout(r, 300));
}
"""

# ce qu'on voit : le bouton, sa place, ce qui est au-dessus de lui, ce qu'il recouvre
MESURER = r"""
() => {
  const vue = document.getElementById('mosaiquePlein');
  const b = vue.querySelector('.mos-plein-fermer');
  const W = innerWidth, H = innerHeight;
  const res = { ouverte: !vue.classList.contains('hidden'), bouton: !!b, W, H, dir: document.documentElement.dir || 'ltr' };
  if(!b) return res;
  const r = b.getBoundingClientRect();
  res.rect = [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)];
  const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
  const dessus = document.elementFromPoint(cx, cy);
  res.auPremierPlan = !!(dessus && (dessus === b || b.contains(dessus)));
  res.visible = getComputedStyle(b).visibility !== 'hidden' && getComputedStyle(b).display !== 'none' && r.width > 0;
  res.dansEcran = r.left >= 0 && r.top >= 0 && r.right <= W && r.bottom <= H;
  res.texte = b.textContent.trim();
  res.attendu = t('back_button');
  const chev = getComputedStyle(b, '::before').content;
  res.chevron = chev;
  const croise = el => { if(!el || el.classList.contains('hidden')) return false; const q = el.getBoundingClientRect();
    return q.width > 0 && q.height > 0 && !(q.right <= r.left || q.left >= r.right || q.bottom <= r.top || q.top >= r.bottom); };
  res.recouvre = ['mosaiquePleinIntro', 'mosaiquePleinToile', 'mosaiquePleinLegende'].filter(id => croise(document.getElementById(id)));
  const leg = document.getElementById('mosaiquePleinLegende').getBoundingClientRect();
  const toile = document.getElementById('mosaiquePleinToile').getBoundingClientRect();
  res.legende = [Math.round(leg.top), Math.round(leg.bottom)];
  res.toile = [Math.round(toile.top), Math.round(toile.bottom), Math.round(toile.width)];
  // fond et couleur : le rond doit se detacher (jour : verre clair, encre ; nuit : verre sombre, clair)
  res.couleur = getComputedStyle(b).color;
  return res;
}
"""

ZOOM = r"""
() => {
  const v = document.querySelector('.zoom-voile');
  if(!v || v.hidden) return { ouvert: false };
  const f = v.querySelector('.zoom-fermer');
  const r = f.getBoundingClientRect();
  const dessus = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
  return { ouvert: true, rect: [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)],
           dansEcran: r.left >= 0 && r.top >= 0 && r.right <= innerWidth && r.bottom <= innerHeight,
           auPremierPlan: !!(dessus && (dessus === f || f.contains(dessus))), label: f.getAttribute('aria-label') };
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index")
    ap.add_argument("--captures")
    ap.add_argument("--cas", help="ne joue que les cas dont le nom contient ce texte (ex. : 'de ar light 780 gagne')")
    a = ap.parse_args()
    index = os.path.abspath(a.index) if a.index else None
    if a.captures:
        os.makedirs(a.captures, exist_ok=True)

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

    def essai(nav, appris, ui, theme, hauteur, rang):
        f = []
        ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": hauteur}, service_workers="block",
                              has_touch=True)
        page = ctx.new_page()
        erreurs = []
        page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
        page.on("dialog", lambda d: d.dismiss())
        url = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if appris == "es" else "")
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.evaluate(PREPARER, [ui])
        page.reload()
        page.wait_for_load_state("networkidle")
        # l'ecran d'ouverture (le W, 4,5 s) recouvre tout tant qu'il n'est pas parti : on l'attend
        page.wait_for_function("""() => { const s = document.getElementById('splashOuverture');
            if(!s) return true; const c = getComputedStyle(s);
            return s.classList.contains('parti') || c.display === 'none' || c.visibility === 'hidden' || +c.opacity === 0; }""",
                               timeout=30000)
        page.wait_for_timeout(500)
        nom = "%s-%s-%s-%d-%s" % (appris, ui, theme, hauteur, "gagne" if rang else "en-cours")
        r = {}
        try:
            # 1. la fiche : le rond se voit
            page.evaluate(OUVRIR, [appris, theme, rang])
            r = page.evaluate(MESURER)
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, nom + "-fiche.png"))
            if not r.get("ouverte"):
                f.append("la fiche ne s'ouvre pas")
            if not r.get("bouton"):
                f.append("aucun bouton de fermeture")
            else:
                if not r["visible"]:
                    f.append("le bouton est cache")
                if not r["dansEcran"]:
                    f.append("le bouton sort de l'ecran %s" % r["rect"])
                if not r["auPremierPlan"]:
                    f.append("le bouton est recouvert")
                if r["rect"][2] < 40 or r["rect"][3] < 40:
                    f.append("le bouton est trop petit %s" % r["rect"])
                if r["recouvre"]:
                    f.append("le bouton recouvre %s" % r["recouvre"])
                if r["texte"] != r["attendu"]:
                    f.append("texte cache %r (attendu %r)" % (r["texte"], r["attendu"]))
                cote_droit = r["rect"][0] + r["rect"][2] / 2 > r["W"] / 2
                if (ui == "ar") != cote_droit:
                    f.append("le bouton est du mauvais cote (%s, dir %s)" % (r["rect"], r["dir"]))
                if r["legende"][1] > r["H"] + 1:
                    f.append("la legende sort par le bas (%s sur %d)" % (r["legende"], r["H"]))
            # 2. le rond ferme et laisse l'accueil
            if r.get("bouton"):
                page.locator("#mosaiquePlein .mos-plein-fermer").tap()
                page.wait_for_timeout(300)
                ferme = page.evaluate("() => document.getElementById('mosaiquePlein').classList.contains('hidden')")
                accueil = page.evaluate("() => !!document.querySelector('#home.active')")
                if not ferme:
                    f.append("le rond ne ferme pas la fiche")
                if not accueil:
                    f.append("apres le rond, l'accueil n'est pas l'ecran actif")
            # 3. le tableau ouvre l'agrandissement, dont le « × » se voit et rend la fiche
            page.evaluate(OUVRIR, [appris, theme, rang])
            page.locator("#mosaiquePleinToile").tap()
            page.wait_for_timeout(500)
            z = page.evaluate(ZOOM)
            if a.captures:
                page.screenshot(path=os.path.join(a.captures, nom + "-zoom.png"))
            if not z.get("ouvert"):
                f.append("le tableau n'ouvre pas l'agrandissement")
            else:
                if not z["dansEcran"] or not z["auPremierPlan"]:
                    f.append("le « × » de l'agrandissement n'est pas visible %s" % z)
                page.locator(".zoom-voile .zoom-fermer").tap()
                page.wait_for_timeout(300)
                if page.evaluate("() => { const v = document.querySelector('.zoom-voile'); return !!(v && !v.hidden); }"):
                    f.append("le « × » ne ferme pas l'agrandissement")
                if page.evaluate("() => document.getElementById('mosaiquePlein').classList.contains('hidden')"):
                    f.append("fermer l'agrandissement a aussi ferme la fiche")
            # 4. le toucher a cote du tableau ferme toujours
            page.evaluate("() => { if(document.getElementById('mosaiquePlein').classList.contains('hidden')) ouvrirMosaiquePleinEcran(); }")
            page.wait_for_timeout(600)
            page.mouse.click(180 if ui != "ar" else 180, hauteur - 6)
            page.wait_for_timeout(300)
            if not page.evaluate("() => document.getElementById('mosaiquePlein').classList.contains('hidden')"):
                f.append("le toucher a cote du tableau ne ferme plus")
        except Exception as e:
            f.append(str(e).split("\n")[0][:300])
        ctx.close()
        erreurs = [e for e in erreurs if "synonymes" not in e]
        if erreurs:
            f.append("erreurs JS %s" % sorted(set(erreurs))[:3])
        return r, f

    total = 0
    essais = []
    for appris in ("de", "es"):
        for ui in ("fr", "ar"):
            for theme in ("light", "dark"):
                for hauteur in (640, 780):
                    for rang in (1, 0):
                        essais.append((appris, ui, theme, hauteur, rang))
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, ui, theme, hauteur, rang in essais:
                if a.cas and a.cas not in "%s %s %s %d %s" % (appris, ui, theme, hauteur, "gagne" if rang else "en-cours"):
                    continue
                r, fautes = essai(nav, appris, ui, theme, hauteur, rang)
                total += 1 if fautes else 0
                print("== %s %s %-5s 360x%d %-8s %s %s" % (appris, ui, theme, hauteur, "gagne" if rang else "en-cours",
                                                          "ok" if not fautes else "FAUTE", fautes), flush=True)
                if r and r.get("bouton"):
                    print("   rond %s, texte %r, toile %s, legende %s, couleur %s" % (
                        r.get("rect"), r.get("texte"), r.get("toile"), r.get("legende"), r.get("couleur")), flush=True)
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not total else "%d cas en defaut" % total))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
