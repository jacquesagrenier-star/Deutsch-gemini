# -*- coding: utf-8 -*-
"""Inventaire langue x contenu : ce que l'allemand, l'espagnol et l'anglais
offrent vraiment, mesure dans les fichiers et dans l'app (27 oct. 2026).

    python anglais/outils/inventaire.py            (donnees + ecrans)
    python anglais/outils/inventaire.py --donnees  (donnees seulement, sans navigateur)

Deux mesures, jamais une deduction :
  1. les DONNEES : chaque fichier que le moteur lit, compte par niveau ;
  2. les ECRANS : l'app ouverte en allemand, en espagnol et en anglais (Playwright),
     « Tout le contenu », chaque tuile VISIBLE, chaque option VISIBLE de son
     panneau, et les elements de l'accueil (offsetParent, pas la presence dans
     le DOM : c'est ce qu'a cache la liste blanche de la v983).
Sortie : anglais/outils/inventaire.json (et un resume a l'ecran).
"""
import functools, http.server, io, json, os, re, socketserver, sys, threading

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NIV = ["A1", "A2", "B1", "B2", "C1"]
DOSSIERS = {
    "de": ("", {"themes.json": "themes.json", "verbe.json": "verbe.json", "adjectif.json": "adjectif.json",
                "adverbe.json": "adverbe.json", "redewendung.json": "redewendung.json",
                "funktionswort.json": "funktionswort.json", "exercices.json": "exercices.json",
                "grammaire.json": "grammaire.json", "conjugaison.json": "conjugaison.json",
                "reperes.json": "reperes.json", "prononciation.json": "prononciation.json",
                "premiers-pas.json": "premiers-pas.json", "a1-voyage.json": "a1-voyage.json",
                "pruefung.json": "pruefung.json", "synonymes.json": "synonymes.json",
                "frequence.json": "frequence.json"}),
    "es": ("espanol/", {"themes.json": "datos/temas.json", "verbe.json": "datos/verbos.json",
                        "adjectif.json": "datos/adjetivos.json", "adverbe.json": "datos/adverbios.json",
                        "redewendung.json": "datos/expresiones.json", "funktionswort.json": "datos/funcionales.json",
                        "exercices.json": "datos/ejercicios.json"}),
    "en": ("anglais/", {"themes.json": "datos/themes.json", "verbe.json": "datos/verbes.json",
                        "adjectif.json": "datos/adjectifs.json", "adverbe.json": "datos/adverbes.json",
                        "redewendung.json": "datos/expressions.json", "funktionswort.json": "datos/fonctionnels.json"}),
}


def chemin(langue, fichier):
    base, renvoi = DOSSIERS[langue]
    if langue == "de":
        return os.path.join(RACINE, renvoi.get(fichier, fichier))
    return os.path.join(RACINE, base, renvoi.get(fichier, "datos/" + fichier))


def lire(langue, fichier):
    p = chemin(langue, fichier)
    if not os.path.exists(p):
        return None
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def par_niveau(d):
    if not isinstance(d, dict):
        return {}
    return {n: len(d.get(n) or []) for n in NIV if d.get(n)}


def donnees(langue):
    r = {}
    th = lire(langue, "themes.json")
    if th:
        t = th.get("themes", th) if isinstance(th, dict) else th
        r["noms"] = {n: sum(len(x.get("mots", [])) for x in t if (x.get("niveau") or "").upper() == n) for n in NIV}
        r["noms"] = {k: v for k, v in r["noms"].items() if v}
        r["themes"] = len(t)
    for cle, f in (("verbes", "verbe.json"), ("adjectifs", "adjectif.json"), ("adverbes", "adverbe.json"),
                   ("expressions", "redewendung.json")):
        d = lire(langue, f)
        r[cle] = par_niveau(d) if d else {}
    fw = lire(langue, "funktionswort.json")
    if fw:
        r["mots_outils"] = sum(len(v) for v in fw.values() if isinstance(v, list))
    ex = lire(langue, "exercices.json")
    jeux = (ex or {}).get("jeux") if isinstance(ex, dict) and "jeux" in ex else ex
    if isinstance(jeux, dict):
        jeux = {k: v for k, v in jeux.items() if isinstance(v, list)}
        r["series"] = len(jeux)
        r["questions"] = sum(len(v) for v in jeux.values())
        r["noms_series"] = sorted(jeux)
    gr = lire(langue, "grammaire.json")
    if gr:
        fiches = gr.get("fiches") if isinstance(gr, dict) and "fiches" in gr else None
        r["fiches_grammaire"] = len(fiches) if fiches is not None else (
            "%d rubriques" % len([k for k in gr if not k.startswith("_")]) if isinstance(gr, dict) else 0)
    cj = lire(langue, "conjugaison.json")
    if cj:
        r["feuilles"] = {n: len(v) for n, v in cj.get("niveaux", {}).items()}
    rp = lire(langue, "reperes.json")
    if rp:
        r["reperes"] = [x["id"] for x in rp.get("reperes", [])]
    pr = lire(langue, "prononciation.json")
    if pr:
        r["prononciation"] = sum(len(g.get("regles", [])) for g in pr.get("groupes", []))
    pp = lire(langue, "premiers-pas.json")
    if pp:
        e = pp.get("etapes", [])
        r["premiers_pas"] = {"etapes": len(e), "cartes": sum(len(x.get("cartes", [])) for x in e),
                             "phrases": sum(len(x.get("phrases", [])) for x in e)}
    av = lire(langue, "a1-voyage.json")
    if av:
        r["a1_voyage"] = {k: len(v) for k, v in av.items() if isinstance(v, list)}
    pf = lire(langue, "pruefung.json")
    if pf:
        r["examen"] = {k: len(v) for k, v in pf.items() if isinstance(v, list)}
    for f in ("synonymes.json", "frequence.json", "variantes.json"):
        r[f.split(".")[0]] = os.path.exists(chemin(langue, f))
    proto = os.path.join(RACINE, "visuel", "prototype")
    suff = {"de": ".js", "es": ".es.js", "en": ".en.js"}[langue]
    sc = [n for n in os.listdir(proto) if re.match(r"^scene-[a-z-]+" + re.escape(suff) + "$", n)]
    r["scenes"] = len(sc)
    couches = {}
    for n in sc:
        t = io.open(os.path.join(proto, n), encoding="utf-8").read()
        d = json.loads(t[t.index("{"):t.rindex("}") + 1])
        for niv, c in (d.get("couches") or {}).items():
            if c.get("qs"):
                couches[niv] = couches.get(niv, 0) + 1
    r["scenes_avec_questions"] = couches
    ep = [n for n in os.listdir(os.path.join(RACINE, "scenes")) if n.endswith(".json") and n != "personnages.json"]
    r["episodes"] = len([n for n in ep if (n.startswith("es-") if langue == "es" else
                                           n.startswith("en-") if langue == "en" else re.match(r"^\d", n))])
    return r


ECRANS = r"""async () => {
  const vis = e => !!e && e.offsetParent !== null && getComputedStyle(e).visibility !== "hidden";
  const txt = e => (e.innerText || "").split("\n").map(s => s.trim()).filter(Boolean)[0] || "";
  goHome(); await new Promise(r => setTimeout(r, 600));
  const accueil = {};
  for (const [nom, sel] of [["seance", "[data-orbid=seance], .seance-pilule, #pilluleSeance"],
       ["scenes", "#explorerScenes"], ["ecouter", "#ecouteLigneAccueil"], ["episodes", "#episodeLigne"],
       ["mosaique", "#carteMosaique"], ["recherche", ".search-launch"], ["mis_de_cote", "[data-orbid=gardes]"]])
    accueil[nom] = [...document.querySelectorAll(sel)].some(vis);
  if (typeof ouvrirToutLeContenu === "function") { ouvrirToutLeContenu(); await new Promise(r => setTimeout(r, 600)); }
  const tuiles = [...document.querySelectorAll("#home [data-orbid]")].filter(vis)
    .map(e => ({ id: e.dataset.orbid, titre: txt(e) }));
  const panneaux = {};
  for (const t of tuiles) {
    goHome(); await new Promise(r => setTimeout(r, 200));
    if (typeof ouvrirToutLeContenu === "function") { ouvrirToutLeContenu(); await new Promise(r => setTimeout(r, 300)); }
    const el = document.querySelector('#home [data-orbid="' + t.id + '"]');
    try { el.click(); } catch (e) {}
    await new Promise(r => setTimeout(r, 900));
    const ecran = document.querySelector(".screen.active");
    panneaux[t.id] = { ecran: ecran ? ecran.id : "",
      options: ecran && ecran.id === "orbPanel" ? [...document.querySelectorAll("#orbPanel .orb-opt")].filter(vis).map(txt) : [] };
  }
  return { accueil, tuiles, panneaux };
}"""


def ecrans():
    from playwright.sync_api import sync_playwright
    port = 8795
    g = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    g.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", port), g)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    sortie = {}
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for langue in ("de", "es", "en"):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                page = ctx.new_page()
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html?apprendre=%s" % (port, langue))
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(2500)
                sortie[langue] = page.evaluate(ECRANS)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    return sortie


def main():
    rapport = {"donnees": {l: donnees(l) for l in DOSSIERS}}
    if "--donnees" not in sys.argv:
        rapport["ecrans"] = ecrans()
    with io.open(os.path.join(ICI, "inventaire.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)
    for l, d in rapport["donnees"].items():
        print("==", l, json.dumps({k: v for k, v in d.items() if k != "noms_series"}, ensure_ascii=False))
    for l, e in rapport.get("ecrans", {}).items():
        print("== ecrans", l, "accueil", e["accueil"])
        for t in e["tuiles"]:
            print("   %-16s %-26s %s" % (t["id"], t["titre"][:26], " | ".join(e["panneaux"].get(t["id"], {}).get("options", []))[:220]))


if __name__ == "__main__":
    main()
