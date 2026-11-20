# -*- coding: utf-8 -*-
"""La voix de la visite guidee (voix-visite/, audio/voix_visite.py), a 360 x 740 : A CHAQUE ETAPE, LE CLIP JOUE ET
DIT LE TEXTE AFFICHE. Pour chaque langue qui a une voix (fr, en, tr, uk, fa, ar, pt), la visite entiere :
  - aucune etape muette (clipDePage() ne rend pas null, la liste des clips en attente est vide) ;
  - le fichier demande est voix-visite/<langue>/<clip>.mp3?r=<revision>, il repond 200 et il JOUE (la lecture avance) ;
  - sa duree dans la page est celle du fichier du depot ;
  - le titre et le texte a l'ecran (ou l'etiquette du tableau) sont ceux d'I18N, et l'empreinte de ce texte est
    celle de voix-visite/textes.json : le clip a ete fait a partir de CE texte.
Puis des passes courtes : les trois clips des mots (mots, mot_peu, mot) en anglais, et la visite espagnole (ses
clips propres dans voix-visite/es/).
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/visite_voix.py <racine> <port> <dossier-captures> [langues, ex. fr,en,ar]"""
import functools, hashlib, http.server, io, json, os, re, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT, OUT = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
sys.path.insert(0, os.path.join(RACINE, "audio"))
import controler_sons as cs
import voix_visite as vv

LANGUES = sys.argv[4].split(",") if len(sys.argv) > 4 else list(vv.LANGUES)
HTML = io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()
REVISION = re.search(r'const VOIX_VISITE = \{ revision: "(\d+)"', HTML).group(1)
MANIFESTE = json.load(io.open(os.path.join(RACINE, "voix-visite", "textes.json"), encoding="utf-8"))
TEXTES = vv.textes_de_l_app()
TEXTES_ES = vv.textes_espagnols(TEXTES)
PAGE = {"intro": 0, "t5": 1, "mots": 2, "mot_peu": 2, "mot": 2, "scene": 3, "ecoute": 4, "t4": 5, "t6": 6}
ATTENDUS = ["intro", "t5", "MOTS", "scene", "ecoute", "t4", "d1", "d2", "d3", "d4", "d5", "pretour", "t6"]


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
  const P = a.apprise === 'es' ? 'wortandoEs_' : 'deutschAI_';
  localStorage.setItem('wortando_langueApprise', a.apprise);
  localStorage.setItem(P + 'uiLang', a.ui); localStorage.setItem(P + 'setupDone', '1'); localStorage.setItem(P + 'onboardingSeen', '1');
}"""

# Chaque appel de la voix est note : le clip, ce que l'ecran montre a cet instant, le fichier demande, et jusqu'ou
# la lecture est allee. La fonction d'origine fait tout le travail.
ESPION = """() => {
  window.__voix = [];
  const vraie = window.narrerDecouverte;
  window.narrerDecouverte = function(clip){
    const lire = id => { const e = document.getElementById(id); return e ? e.textContent : ''; };
    const e = { clip: clip, etape: (typeof decouverte !== 'undefined' && decouverte) ? decouverte.etape : null,
                titre: lire('decouverteTitre'), texte: lire('decouverteTexte'), etiquette: lire('decouverteProjection'),
                src: '', pos: 0, duree: null, fin: null };
    window.__voix.push(e);
    const p = vraie(clip);
    let son = null;
    try{ son = audioEnCours; e.src = son ? (son.getAttribute('src') || son.src || '') : ''; }catch(x){}
    const suivre = setInterval(() => {
      try{ if(son && (son.getAttribute('src') || son.src || '') === e.src){ e.pos = Math.max(e.pos, son.currentTime || 0); if(Number.isFinite(son.duration)) e.duree = son.duration; } }catch(x){}
    }, 150);
    Promise.resolve(p).then(v => { e.fin = v; setTimeout(() => clearInterval(suivre), 300); });
    return p;
  };
  return typeof vraie;
}"""

ETAT = """() => ({ voix: window.__voix || [],
  etape: (typeof decouverte !== 'undefined' && decouverte) ? decouverte.etape : null,
  pret: !!(typeof decouverte !== 'undefined' && decouverte && decouverte.pret),
  attente: (typeof clipsEnAttente === 'function') ? clipsEnAttente() : null,
  dispo: (typeof voixVisiteDispo === 'function') ? voixVisiteDispo() : null,
  page: document.documentElement.scrollWidth })"""


def duree_fichier(chemin):
    x = cs.pcm(chemin)
    return len(x) / cs.SR


def attendu(apprise, ui, clip):
    """(cle du manifeste, dossier, texte compose de l'ecran, texte dit)"""
    propre = apprise == "es" and clip in vv.CLIPS_PROPRES_ES
    t = TEXTES_ES[ui] if (apprise == "es" and ui in TEXTES_ES) else TEXTES[ui]
    ecran = vv.composer([t[k] for k in vv.CLIPS[clip]])
    return (("es-" + ui) if propre else ui,
            os.path.join(RACINE, "voix-visite", "es", ui) if propre else os.path.join(RACINE, "voix-visite", ui),
            ecran, vv.prononcer(ecran, ui))


def juger(apprise, ui, e, reponses, bilan, nom):
    clip = e["clip"]
    if not clip:
        bilan.append("%s : une etape sans clip (etape %s)" % (nom, e["etape"])); return "MUET"
    cle, dossier, ecran, dit = attendu(apprise, ui, clip)
    fautes = []
    chemin = ("voix-visite/es/" if cle.startswith("es-") else "voix-visite/") + ui + "/" + clip + ".mp3?r=" + REVISION
    if not e["src"].endswith(chemin):
        fautes.append("demande %s au lieu de %s" % (e["src"][-60:], chemin))
    if reponses.get(chemin) != 200:
        fautes.append("reponse %s" % reponses.get(chemin))
    f = os.path.join(dossier, clip + ".mp3")
    d = duree_fichier(f) if os.path.exists(f) else None
    # Un clip d'une seconde (« 60 », « 90 ») ne peut pas avoir joue une seconde entiere : la position est relevee
    # toutes les 150 ms. Il suffit qu'il soit alle presque au bout.
    if (e["pos"] or 0) < min(1.0, (d or 1.0) - 0.4):
        fautes.append("ne joue pas (lecture %.1f s)" % (e["pos"] or 0))
    if d is None or e["duree"] is None or abs(d - e["duree"]) > 0.35:
        fautes.append("duree %s dans la page, %s dans le depot" % (e["duree"], d))
    vu = vv.composer([e["titre"], e["texte"]]) if clip in PAGE else vv.composer([e["etiquette"]])
    if vu != ecran:
        fautes.append("l'ecran ne montre pas le texte du clip : « %s » / « %s »" % (vu[:70], ecran[:70]))
    if hashlib.sha1(dit.encode("utf-8")).hexdigest() != MANIFESTE.get(cle, {}).get(clip):
        fautes.append("empreinte de textes.json differente du texte affiche")
    for x in fautes:
        bilan.append("%s %s : %s" % (nom, clip, x))
    return "ok %.1f s" % d if not fautes else "A REVOIR"


def main():
    os.makedirs(OUT, exist_ok=True)
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])

            def ouvrir(apprise, ui):
                ctx = nav.new_context(viewport={"width": 360, "height": 740}, device_scale_factor=2, service_workers="block", has_touch=True, is_mobile=True)
                for motif in ("**/*firebase*", "**/*gstatic*", "**/*googleapis*", "**/*recaptcha*"):
                    ctx.route(motif, lambda r: r.abort())
                page = ctx.new_page()
                page.erreurs, page.reponses = [], {}
                page.on("pageerror", lambda e: page.erreurs.append(str(e).splitlines()[0][:140] if str(e) else ""))
                page.on("dialog", lambda d: d.dismiss())

                def note(r):
                    if "/voix-visite/" in r.url:
                        page.reponses[r.url.split("/", 3)[3]] = r.status
                page.on("response", note)
                adresse = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if apprise == "es" else "")
                page.goto(adresse, wait_until="domcontentloaded")
                page.wait_for_timeout(2500)
                page.evaluate(POSER, {"ui": ui, "apprise": apprise})
                page.reload(wait_until="domcontentloaded"); page.wait_for_timeout(4500)
                page.evaluate(FAUX_COMPTE)
                page.evaluate(ESPION)
                return ctx, page

            def attendre(page, test, maxi_ms):
                t = 0
                while t < maxi_ms:
                    if test(page.evaluate(ETAT)):
                        return True
                    page.wait_for_timeout(300); t += 300
                return False

            def joue(clip, mini=1.2):
                return lambda s: any(v["clip"] == clip and (v["pos"] or 0) >= mini for v in s["voix"])

            def lancer(page, reponse):
                page.evaluate("(r) => { lancerDecouverte(r || undefined); }", reponse)
                attendre(page, lambda s: s["pret"], 15000)

            print("===== la visite entiere, une langue apres l'autre (allemand appris, revision %s)" % REVISION, flush=True)
            for ui in LANGUES:
                ctx, page = ouvrir("de", ui)
                lancer(page, None)
                s = page.evaluate(ETAT)
                if s["attente"]:
                    bilan.append("%s : des clips se taisent encore : %s" % (ui, s["attente"]))
                if not s["dispo"]:
                    bilan.append("%s : pas de voix pour cette langue" % ui)
                attendre(page, joue("intro"), 9000)
                for n in (1, 2, 3, 4):
                    page.evaluate("(n) => allerEtapeDecouverte(n)", n)
                    attendre(page, lambda s, n=n: any(v["etape"] == n and (v["pos"] or 0) >= 1.2 for v in s["voix"]), 9000)
                    if n == 1:
                        page.screenshot(path=os.path.join(OUT, "voix-seance-%s.png" % ui))
                page.evaluate("() => allerEtapeDecouverte(5)")
                fini = attendre(page, joue("pretour"), 150000)
                page.screenshot(path=os.path.join(OUT, "voix-tableau-%s.png" % ui))
                page.evaluate("() => finVisiteDecouverte()")
                attendre(page, joue("t6"), 9000)
                s = page.evaluate(ETAT)
                entendus, lignes = [], []
                for e in s["voix"]:
                    verdict = juger("de", ui, e, page.reponses, bilan, ui)
                    entendus.append(e["clip"])
                    lignes.append("%s %s" % (e["clip"], verdict))
                manque = [c for c in ATTENDUS if (c != "MOTS" and c not in entendus) or (c == "MOTS" and not {"mots", "mot", "mot_peu"} & set(entendus))]
                if manque:
                    bilan.append("%s : clips jamais lances : %s" % (ui, ", ".join(manque)))
                if s["page"] > 360:
                    bilan.append("%s : la page fait %d px" % (ui, s["page"]))
                if page.erreurs:
                    bilan.append("%s : erreurs JS %s" % (ui, page.erreurs[:2]))
                print("  %s : %s ; demonstration finie %s ; erreurs JS %d" % (ui, " | ".join(lignes), fini, len(page.erreurs)), flush=True)
                ctx.close()

            print("===== les clips des mots, selon la reponse du profil (allemand et espagnol appris)", flush=True)
            for apprise, ui in (("de", "en"), ("es", "en"), ("es", "fr")):
                if ui not in LANGUES:
                    continue
                ctx, page = ouvrir(apprise, ui)
                cles = page.evaluate("() => Object.keys(contenuDecouverte())")
                vus = []
                for r in cles:
                    page.evaluate("() => { window.__voix.length = 0; }")
                    lancer(page, r)
                    page.evaluate("() => allerEtapeDecouverte(2)")
                    attendre(page, lambda s: any(v["etape"] == 2 and (v["pos"] or 0) >= 1.2 for v in s["voix"]), 9000)
                    for e in page.evaluate(ETAT)["voix"]:
                        if e["etape"] == 2:
                            vus.append("%s -> %s %s" % (r, e["clip"], juger(apprise, ui, e, page.reponses, bilan, "%s/%s" % (apprise, ui))))
                    page.evaluate("() => { try{ passerDecouverte(); }catch(e){} }")
                    page.wait_for_timeout(900)
                if apprise == "es":
                    page.evaluate("() => { window.__voix.length = 0; }")
                    lancer(page, None)
                    page.evaluate("() => allerEtapeDecouverte(5)")
                    attendre(page, joue("pretour"), 150000)
                    for e in page.evaluate(ETAT)["voix"]:
                        if e["etape"] == 5:
                            vus.append("%s %s" % (e["clip"], juger(apprise, ui, e, page.reponses, bilan, "%s/%s" % (apprise, ui))))
                print("  %s appris, interface %s : %s ; erreurs JS %d" % (apprise, ui, " | ".join(vus), len(page.erreurs)), flush=True)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("BILAN OK" if not bilan else "BILAN A REVOIR : " + " | ".join(bilan))


if __name__ == "__main__":
    main()
