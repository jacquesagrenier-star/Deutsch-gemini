# -*- coding: utf-8 -*-
"""L'OUVERTURE DE LA LISTE DES CONVERSATIONS, IMAGE PAR IMAGE (ligne 156, retour de Jacques du 20 nov. 2026 sur la
v1229 : « quand je clique sur la tuile, il y a un flash avant d'ouvrir, de montrer les 4 conversations »).
La tuile « Converser » de l'accueil est touchee, puis l'ecran est photographie aussi vite que possible pendant quatre
secondes, a 360 x 740, avec Chromium et WebKit (le moteur de l'iPhone), en francais et en arabe, de jour et de nuit.
Le reseau de la page des conversations est ralenti (RETARD ms par fichier) : sur un telephone, chaque fichier met ce
temps-la, et c'est ce qui rend l'eclair visible.
Pour chaque image : l'ecran actif, ce que le cadre montre (rien, la page sans la liste, la liste), la couleur moyenne
et la luminance du milieu de l'ecran. Entre le toucher et la liste, l'ecran ne doit faire qu'UN chemin : de l'accueil
a la page qui attend ses donnees, puis la liste s'y pose. Un ECLAIR, c'est :
  - une image dont la luminance sort de ce chemin de plus de SEUIL (plus claire ou plus sombre que l'accueil ET que la
    page en attente : le bleu nuit du cadre, la page claire en mode nuit) ;
  - la page qui change d'aspect une fois dans le cadre, avant la liste (le paysage qui arrive apres coup) ;
  - ce qui ne doit jamais paraitre : l'etiquette « Maquette », la page claire en mode nuit.
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/converser_flash.py <racine> <port> <dossier-captures> [<index-avant.html> [<conversation-avant.html>]]
(avec les pages d'avant, la sonde montre l'eclair : elle mesure, sans juger)"""
import functools, http.server, io, json, os, sys, threading, time
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image
from playwright.sync_api import sync_playwright

RACINE, PORT, OUT = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
AVANT = io.open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) > 4 else None
AVANT_CONV = io.open(sys.argv[5], encoding="utf-8").read() if len(sys.argv) > 5 else None
SUF = "-avant" if AVANT else ""
RETARD = 0.25      # secondes par fichier de la page des conversations
SEUIL = 16         # ecart de luminance (0-255) qui se voit
DUREE = 4.0


class Lent(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if "/visuel/prototype/conversation" in self.path:
            time.sleep(RETARD)
        return super().do_GET()

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


POSER = """(a) => {
  localStorage.clear();
  localStorage.setItem('wortando_langueApprise', 'de');
  localStorage.setItem('deutschAI_uiLang', a.ui); localStorage.setItem('deutschAI_setupDone', '1'); localStorage.setItem('deutschAI_onboardingSeen', '1');
  localStorage.setItem('deutschAI_niveauSeance', 'A2');
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
  let n = 0;
  const tuile = () => document.querySelector('.tg[data-tg="converser"]:not(.hidden)');
  while(!tuile() && n++ < 60) await new Promise(r => setTimeout(r, 250));
  if(!tuile()) return false;
  tuile().scrollIntoView({ block: 'center' });
  await new Promise(r => setTimeout(r, 900));
  return true;
}"""
ETAT = """() => ({ ecran: (document.querySelector('.screen.active') || {}).id || '', voile: getComputedStyle(document.getElementById('sceneCadre')).opacity })"""
CADRE = """() => { const m = document.getElementById('marque');
  return { nuit: document.documentElement.classList.contains('nuit'), liste: document.querySelectorAll('.liste a').length,
           maquette: !!(m && !m.hidden && m.offsetParent !== null), pret: document.readyState }; }"""


def mesure(octets):
    im = Image.open(io.BytesIO(octets)).convert("RGB")
    w, h = im.size
    zone = im.crop((int(w * .06), int(h * .16), int(w * .94), int(h * .84))).resize((44, 62))
    px = list(zone.get_flattened_data()) if hasattr(zone, "get_flattened_data") else list(zone.getdata())
    n = len(px)
    r, g, b = (sum(p[i] for p in px) / n for i in range(3))
    blancs = sum(1 for p in px if min(p) > 238) / n
    return (round(r), round(g), round(b)), round(.2126 * r + .7152 * g + .0722 * b, 1), round(100 * blancs)


def main():
    os.makedirs(OUT, exist_ok=True)
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Lent, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []
    try:
        with sync_playwright() as p:
            for moteur in ("chromium", "webkit"):
                nav = getattr(p, moteur).launch()
                for ui in ("fr", "ar"):
                    for nuit in (False, True):
                        nom = "%s %s %s" % (moteur, ui, "nuit" if nuit else "jour")
                        ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 740}, service_workers="block")
                        for motif in ("**/*firebase*", "**/*gstatic*", "**/*googleapis*", "**/*recaptcha*"):
                            ctx.route(motif, lambda r: r.abort())
                        if AVANT:
                            ctx.route("**/index.html*", lambda r: r.fulfill(status=200, content_type="text/html; charset=utf-8", body=AVANT))
                        if AVANT_CONV:
                            ctx.route("**/conversation.html*", lambda r: (time.sleep(RETARD), r.fulfill(status=200, content_type="text/html; charset=utf-8", body=AVANT_CONV)))
                        page = ctx.new_page()
                        page.on("dialog", lambda d: d.dismiss())
                        page.goto("http://127.0.0.1:%d/index.html" % PORT, wait_until="domcontentloaded")
                        page.wait_for_timeout(2500)
                        page.evaluate(POSER, {"ui": ui})
                        page.reload(wait_until="domcontentloaded"); page.wait_for_timeout(4500)
                        page.evaluate(FAUX_COMPTE)
                        if not page.evaluate(ACCUEIL, nuit):
                            print("  %s : la tuile Converser n'est pas sur l'accueil" % nom); bilan.append("%s : pas de tuile" % nom); ctx.close(); continue
                        avant_img = page.screenshot(type="jpeg", quality=70)
                        coul0, lum0, _ = mesure(avant_img)
                        images = []
                        t0 = time.time()
                        page.evaluate("() => { setTimeout(() => document.querySelector('.tg[data-tg=\"converser\"]').click(), 0); }")
                        while time.time() - t0 < DUREE:
                            octets = page.screenshot(type="jpeg", quality=70)
                            t = round(1000 * (time.time() - t0))
                            e = page.evaluate(ETAT)
                            c = None
                            cadre = next((f for f in page.frames if "conversation.html" in f.url), None)
                            if cadre:
                                try:
                                    c = cadre.evaluate(CADRE)
                                except Exception:
                                    c = None
                            coul, lum, blancs = mesure(octets)
                            images.append({"t": t, "ecran": e["ecran"], "voile": e["voile"], "cadre": c, "coul": coul, "lum": lum, "blancs": blancs, "octets": octets})
                        fin = images[-1]
                        liste_a = next((k for k, im in enumerate(images) if im["cadre"] and im["cadre"]["liste"] > 0), None)
                        ouvert_a = next((k for k, im in enumerate(images) if im["ecran"] == "sceneSeance"), None)
                        if liste_a is None or ouvert_a is None:
                            print("  %s : la liste n'est pas apparue en %d s (ecran %s)" % (nom, DUREE, fin["ecran"])); bilan.append("%s : pas de liste" % nom); ctx.close(); continue
                        # la liste posee (les visages peuvent arriver un peu apres le texte) : la derniere image fait foi
                        lum_fin = fin["lum"]
                        # la page en attente de ses donnees : la derniere image avant la liste
                        attente = images[max(0, liste_a - 1)]
                        bas, haut = min(lum0, attente["lum"]) - SEUIL, max(lum0, attente["lum"]) + SEUIL
                        eclairs, maquette, clair_de_nuit, aspects = [], [], [], []
                        for k, im in enumerate(images):
                            if im["ecran"] != "sceneSeance" or k >= liste_a:
                                continue
                            if im["lum"] < bas or im["lum"] > haut:
                                eclairs.append(k)
                            # les aspects successifs de la page une fois dans le cadre (couleur moyenne a 12 pres)
                            if im["cadre"] and im["cadre"]["pret"] != "loading":
                                if not aspects or max(abs(a - b) for a, b in zip(aspects[-1], im["coul"])) > 12:
                                    aspects.append(im["coul"])
                            if im["cadre"] and im["cadre"]["maquette"]:
                                maquette.append(k)
                            if nuit and im["cadre"] and not im["cadre"]["nuit"] and im["cadre"]["pret"] != "loading":
                                clair_de_nuit.append(k)
                        # le resume, image par image, les images semblables regroupees
                        lignes, dernier = [], None
                        for k, im in enumerate(images):
                            etat = "accueil" if im["ecran"] != "sceneSeance" else ("liste" if (im["cadre"] and im["cadre"]["liste"]) else ("page sans liste" if im["cadre"] else "cadre vide"))
                            cle = (etat, round(im["lum"] / 6), bool(im["cadre"] and im["cadre"]["maquette"]))
                            if cle != dernier:
                                lignes.append("%d ms %s lum %.0f rgb%s%s%s" % (im["t"], etat, im["lum"], im["coul"], " MAQUETTE" if cle[2] else "",
                                                                             " ECLAIR" if k in eclairs else ""))
                                dernier = cle
                                io.open(os.path.join(OUT, "flash-%s-%s-%s%s-%02d-%dms.jpg" % (moteur, ui, "nuit" if nuit else "jour", SUF, len(lignes), im["t"])), "wb").write(im["octets"])
                        print("  %s%s : accueil lum %.0f ; %d images en %.1f s ; ecran ouvert a %d ms, liste a %d ms, fin lum %.0f" % (
                            nom, " (AVANT)" if AVANT else "", lum0, len(images), DUREE, images[ouvert_a]["t"], images[liste_a]["t"], lum_fin), flush=True)
                        for l in lignes:
                            print("        " + l)
                        defauts = []
                        if eclairs:
                            defauts.append("%d image(s) hors du chemin accueil %.0f -> page en attente %.0f (de %d a %d ms, luminances %s)" % (
                                len(eclairs), lum0, attente["lum"], images[eclairs[0]]["t"], images[eclairs[-1]]["t"], sorted({round(images[k]["lum"]) for k in eclairs})))
                        if len(aspects) > 1:
                            defauts.append("la page change %d fois d'aspect avant la liste (%s)" % (len(aspects) - 1, " -> ".join("rgb%s" % (a,) for a in aspects)))
                        if maquette:
                            defauts.append("« Maquette » a l'ecran sur %d image(s)" % len(maquette))
                        if clair_de_nuit:
                            defauts.append("page claire en mode nuit sur %d image(s)" % len(clair_de_nuit))
                        print("    %-66s %s" % (nom + " : aucun eclair entre le toucher et la liste", "ok" if not defauts else "NON -- " + " ; ".join(defauts)), flush=True)
                        if defauts and not AVANT:
                            bilan.append(nom + " : " + " ; ".join(defauts))
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
