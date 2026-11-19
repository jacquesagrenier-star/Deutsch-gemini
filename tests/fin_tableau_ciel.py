# -*- coding: utf-8 -*-
"""Le ciel ET le tableau a l'ecran de fin de la seance (choix A de Jacques, « L'horizon », 19 nov. 2026).

    python tests/fin_tableau_ciel.py                       (de et es, jour et nuit, 375 et 320 px, l'arabe en RTL)
    python tests/fin_tableau_ciel.py --captures DOSSIER    (une capture par cas, pour le chef ou Jacques)
    python tests/fin_tableau_ciel.py --index AUTRE.html    (sert ce fichier a la place d'index.html : l'ancienne version)

Ne du retour de Jacques du 17 nov. (« on ne voit plus le tableau quand je termine une seance ; on voit que ca avance sur
l'etoile, mais je devrais aussi voir la progression de mon tableau »). Jusqu'a la v1219, le tableau n'etait dessine que la
ou il n'y avait pas de ciel. Sur un navigateur vierge, sans compte ; la seance du jour est ouverte, l'etat du tableau pose,
des carreaux ajoutes « pendant la seance », puis l'ecran de fin. Cas :
  avance   : 673 -> 697 sur 700 : la plaque dans la carte du ciel, au-dessus de « Encore une seance », « 673 » tant que
             le trait de l'etoile se dessine, puis « 697 / 700 », « Cette seance : +24 », « Il est presque a toi. » ;
  debut    : 100 -> 124 : pas de « presque » ;
  trophee  : le trophee en cours (t 2) : c'est le tableau SUIVANT qui se construit (cn 30 -> 40) ;
  complet  : 695 -> 700 par poserCarreau() : la fete du tableau passe d'abord, la plaque n'avance qu'apres sa fermeture ;
  reduit   : prefers-reduced-motion : le compte final tout de suite, sans animation ;
  A2       : au niveau A2 ; s'il n'y a pas de ciel, l'ancien tableau seul (.fin-tableau), jamais les deux ;
  sans_ciel: le ciel ne se dessine pas (rendreCielFin rendu inerte) : l'ancien tableau seul, comme avant le 19 nov.
Chaque cas verifie aussi que la plaque tient dans la carte (rien ne deborde a 320 px) et la couleur de son texte (encre le
jour, clair la nuit). Il ouvre un navigateur : a lancer SOUS LE VERROU des parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("FIN_TABLEAU_PORT", "8827"))

PREPARER = """
([ui]) => {
  localStorage.setItem(AIDE_CONTINUER_KEY, '1'); localStorage.setItem(AIDE_TRANSIT_KEY, '1');
  localStorage.setItem(PREMIERS_PAS_KEY, JSON.stringify({ a: false, p: 999, fini: true }));
  if(ui) localStorage.setItem(UI_LANG_KEY, ui);
}
"""

MESURE = r"""
async ([cas, appris, theme]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  await chargerPremiersPas(); await chargerCiel(); await chargerMosaiques();
  const jour = getTodayStr();
  const es = appris === 'es';
  const base = { j: jour, n: 0, x: 1, s: es ? 'es' : '', h: es ? [1] : [], b: '', tj: '', t: 0, cn: 0 };
  const poser = e => localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(Object.assign({}, base, e)));
  const etats = {
    avance:  [{ r: 4, c: 673, g: [1, 2, 3] }, v => { v.c = 697; }],
    debut:   [{ r: 4, c: 100, g: [1, 2, 3] }, v => { v.c = 124; }],
    trophee: [{ r: 3, c: 760, g: [1, 2, 3], t: 2, tj: jour, cn: 30 }, v => { v.cn = 40; }],
    complet: [{ r: 4, c: 695, g: [1, 2, 3] }, null],
    reduit:  [{ r: 4, c: 673, g: [1, 2, 3] }, v => { v.c = 697; }],
    A2:      [{ r: 4, c: 300, g: [1, 2, 3] }, v => { v.c = 320; }],
    sans_ciel: [{ r: 4, c: 300, g: [1, 2, 3] }, v => { v.c = 320; }]
  };
  const [debutEtat, pendant] = etats[cas];
  poser(debutEtat);
  // La branche sans constellation (japonais, anglais, ou un ciel qui ne se dessine pas) : le tableau seul, comme avant.
  if(cas === 'sans_ciel') window.rendreCielFin = () => false;
  if(cas === 'A2'){ try{ fixerNiveauSeance('A2', true); }catch(e){} }
  try{ applyAppTheme(theme); }catch(e){ document.body.setAttribute('data-theme', theme); }
  await ouvrirSeanceDuJour(); await pause(900);
  // « pendant la seance » : les carreaux gagnes, apres noterCarreauxDebut() (appelee a l'ouverture)
  if(pendant){ const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE)); pendant(v); localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(v)); }
  else { for(let k = 0; k < 5; k++){ try{ poserCarreau(true); }catch(e){} } }
  currentFlashcard = currentCards.length;
  const t0 = performance.now();
  showFlashcardEnd();
  const lire = () => {
    const ciel = document.getElementById('finCiel'), plaque = document.getElementById('finTableau');
    const cielVu = !!(ciel && !ciel.classList.contains('hidden') && ciel.offsetHeight > 0);
    if(!plaque) return { cielVu, plaque: false };
    const rc = ciel ? ciel.getBoundingClientRect() : null, rp = plaque.getBoundingClientRect();
    const enc = document.getElementById('encoreNeufsBtn');
    const toile = plaque.querySelector('canvas');
    let pleine = false;
    try{ const d = toile.getContext('2d').getImageData(Math.floor(toile.width / 2), Math.floor(toile.height / 2), 1, 1).data; pleine = d[3] > 0; }catch(e){}
    const lignes = [...plaque.querySelectorAll('.fh-ligne')].map(x => x.textContent);
    const deborde = [...plaque.querySelectorAll('*')].some(x => x.scrollWidth > x.clientWidth + 1 && getComputedStyle(x).overflow !== 'hidden');
    return { cielVu, plaque: true, classe: plaque.className, dansCiel: !!(ciel && ciel.contains(plaque)),
             avantEncore: !!(enc && ciel && ciel.contains(enc) && (plaque.compareDocumentPosition(enc) & Node.DOCUMENT_POSITION_FOLLOWING)),
             encoreDansCiel: !!(enc && ciel && ciel.contains(enc) && !enc.classList.contains('hidden')),
             compte: (plaque.querySelector('.fh-compte, .fin-tableau-bas') || {}).textContent || '', titre: (plaque.querySelector('.fh-titre') || {}).textContent || '',
             lignes, pleine, deborde,
             dedans: !rc || (rp.left >= rc.left - 1 && rp.right <= rc.right + 1 && rp.top >= rc.top - 1 && rp.bottom <= rc.bottom + 1),
             couleur: plaque.querySelector('.fh-ligne, .fh-titre') ? getComputedStyle(plaque.querySelector('.fh-titre')).color : '',
             jauge: plaque.querySelector('.fh-jauge i') ? plaque.querySelector('.fh-jauge i').style.width : '',
             avecTableau: !!(ciel && ciel.classList.contains('avec-tableau')) };
  };
  // la plaque arrive avec l'image du tableau
  for(let k = 0; k < 40 && !document.getElementById('finTableau'); k++) await pause(100);
  const tot = lire(); tot.ms = Math.round(performance.now() - t0);
  let fete = !!document.querySelector('.fete-tableau, .fete-etoile');
  let pendantFete = null;
  if(fete){
    await pause(2500);
    pendantFete = lire();
    const b = document.querySelector('.fete-tableau button, .fete-etoile button');
    if(b) b.click();
    for(let k = 0; k < 30 && document.querySelector('.fete-tableau, .fete-etoile'); k++) await pause(100);
  }
  await pause(5200);
  const tard = lire();
  return { tot, pendantFete, tard, fete, attendu: { seance: t('fin_tableau_seance'), presque: t('fin_tableau_presque'), titre: t('tableau_tuile') },
           etat: JSON.parse(localStorage.getItem(MOSAIQUE_CLE)), dir: document.documentElement.getAttribute('dir') || '' };
}
"""


def juger(cas, theme, r):
    f = []
    tot, tard = r["tot"], r["tard"]
    if cas == "sans_ciel":
        if tard.get("cielVu"):
            f.append("un ciel s'est dessine malgre tout")
        if not tard.get("plaque") or "fin-tableau" not in tard.get("classe", "") or tard.get("dansCiel"):
            f.append("pas l'ancien tableau seul : %s" % tard.get("classe"))
        elif not tard["compte"].replace(" ", "").startswith("320/"):
            f.append("compte %r (attendu 320 / 700)" % tard["compte"])
        return f
    if cas == "A2":
        if tard.get("plaque") and tard.get("cielVu") and not tard.get("dansCiel"):
            f.append("le ciel ET l'ancien tableau a part")
        if tard.get("plaque") and not tard.get("cielVu") and "fin-tableau" not in tard.get("classe", ""):
            f.append("sans ciel, pas l'ancien tableau : %s" % tard.get("classe"))
        if not tard.get("plaque"):
            f.append("aucun tableau a l'ecran de fin")
        return f
    if not tard.get("cielVu"):
        return ["pas de ciel a l'ecran de fin (le cas suppose un ciel)"]
    if not tard.get("plaque"):
        return ["pas de tableau dans l'ecran de fin"]
    if not tard["dansCiel"] or "fh-plaque" not in tard["classe"]:
        f.append("le tableau n'est pas sur l'horizon du ciel (%s)" % tard["classe"])
    if tard["encoreDansCiel"] and not tard["avantEncore"]:
        f.append("la plaque n'est pas au-dessus de « Encore une seance »")
    if not tard["dedans"]:
        f.append("la plaque deborde de la carte du ciel")
    if tard["deborde"]:
        f.append("un texte de la plaque deborde")
    if not tard["pleine"]:
        f.append("la toile est vide")
    if not tard["avecTableau"]:
        f.append("classe avec-tableau absente")
    if tard["titre"].strip().lower() != r["attendu"]["titre"].strip().lower():
        f.append("titre %r" % tard["titre"])
    att = {"avance": ("697", 24, True), "debut": ("124", 24, False), "trophee": ("40", 10, False),
           "complet": ("700", 5, False), "reduit": ("697", 24, True)}[cas]
    if not tard["compte"].replace(" ", "").startswith(att[0] + "/"):
        f.append("compte final %r (attendu %s / 700)" % (tard["compte"], att[0]))
    seance = r["attendu"]["seance"].replace("{n}", str(att[1]))
    if seance not in tard["lignes"]:
        f.append("ligne de la seance absente : %r dans %s" % (seance, tard["lignes"]))
    if att[2] != (r["attendu"]["presque"] in tard["lignes"]):
        f.append("« presque » %s" % ("absent" if att[2] else "en trop"))
    # le tableau attend le trait de l'etoile (ou la fete) : au premier releve, il n'a pas encore avance
    if cas in ("avance", "debut", "trophee") and tot.get("plaque") and tot["compte"].replace(" ", "").startswith(att[0] + "/") and tot["ms"] < 1200:
        f.append("le compte etait deja final a %d ms : il n'a pas attendu le ciel" % tot["ms"])
    if cas == "reduit" and tot.get("plaque") and not tot["compte"].replace(" ", "").startswith(att[0] + "/"):
        f.append("mouvement reduit : le compte n'etait pas final tout de suite (%r)" % tot["compte"])
    if cas == "complet":
        if not r["fete"]:
            f.append("pas de fete du tableau")
        elif r["pendantFete"] and r["pendantFete"].get("plaque") and r["pendantFete"]["compte"].replace(" ", "").startswith("700/"):
            f.append("la plaque a avance pendant la fete")
    nuit = theme == "dark"
    c = tard["couleur"]
    try:
        rgb = [int(x) for x in c[c.index("(") + 1:c.index(")")].split(",")[:3]]
        clair = sum(rgb) / 3 > 140
        if nuit != clair:
            f.append("couleur du texte %s %s" % (c, "trop sombre la nuit" if nuit else "trop claire le jour"))
    except Exception:
        f.append("couleur illisible %r" % c)
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index")
    ap.add_argument("--captures")
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
    total = 0

    def essai(nav, appris, cas, theme, largeur, ui=None):
        reduit = cas == "reduit"
        ctx = nav.new_context(locale="fr-FR", viewport={"width": largeur, "height": 820}, service_workers="block",
                              reduced_motion="reduce" if reduit else "no-preference")
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
        page.wait_for_timeout(1200)
        try:
            r = page.evaluate(MESURE, [cas, appris, theme])
        except Exception as e:
            ctx.close()
            return None, [str(e).split("\n")[0][:300]], erreurs
        if a.captures:
            nom = "%s-%s-%s-%d%s.png" % (appris, cas, theme, largeur, ("-" + ui) if ui else "")
            try:
                page.locator("#flashcardEnd").screenshot(path=os.path.join(a.captures, nom))
            except Exception:
                page.screenshot(path=os.path.join(a.captures, nom), full_page=True)
        ctx.close()
        return r, juger(cas, theme, r), erreurs

    essais = []
    for appris in ("de", "es"):
        for theme in ("light", "dark"):
            for cas in ("avance", "debut", "trophee", "complet", "reduit", "A2", "sans_ciel"):
                essais.append((appris, cas, theme, 375, None))
        essais.append((appris, "avance", "light", 320, None))
        essais.append((appris, "complet", "dark", 320, None))
    essais.append(("de", "avance", "light", 360, "ar"))
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for appris, cas, theme, largeur, ui in essais:
                r, fautes, erreurs = essai(nav, appris, cas, theme, largeur, ui)
                total += 1 if fautes else 0
                print("== %s %-8s %-5s %d%s %s %s" % (appris, cas, theme, largeur, (" " + ui) if ui else "", "ok" if not fautes else "FAUTE", fautes), flush=True)
                if r:
                    t = r["tard"]
                    print("   compte %r, lignes %s, dans le ciel %s, fete %s, au debut %r a %s ms, couleur %s, dir %s" % (
                        t.get("compte"), t.get("lignes"), t.get("dansCiel"), r["fete"], r["tot"].get("compte"), r["tot"].get("ms"), t.get("couleur"), r["dir"]), flush=True)
                erreurs = [e for e in erreurs if "synonymes" not in e]
                if erreurs:
                    print("   erreurs JS", sorted(set(erreurs))[:4], flush=True)
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("tout est bon" if not total else "%d cas en defaut" % total))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
