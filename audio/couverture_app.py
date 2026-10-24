# -*- coding: utf-8 -*-
"""Ce que l'APP demande a voix haute, et ce qui n'a pas de fichier.

    python audio/couverture_app.py                 # espagnol, deux voix
    python audio/couverture_app.py --app de        # allemand
    python audio/couverture_app.py --json sortie.json

NE LE 24 OCT. 2026. Jacques : « il y a des mots qui sont toujours lus avec le
cellulaire ». Les manifestes (manifest.py, manifest_es.py) disent ce qu'on a
CRU devoir generer ; le telephone parle quand le texte que l'app demande n'est
pas celui-la. On part donc de l'app : on la charge (Chromium, comme
fusion-espagnol/parcours.py), et pour chaque carte de chaque paquet on appelle
SES fonctions -- celles qui fabriquent le texte passe a direAllemand() :

  carte.*       loadFlashcard() puis etapesChaineCarte() : mot, pluriel, phrase
  seance.*      phraseDeCarte() (la phrase a remettre en ordre, et chaque tuile
                telle que la dit le clic : ponctuation retiree, minuscules en
                espagnol) et motDictee()
  ecoute.*      poolEcoute() puis contenuEcoute() : le mot et la phrase cibles

Premiers pas, reperes, scenes et A1 voyage sont des donnees lues telles
quelles : ils viennent du manifeste (source « manifeste.* »).

Le texte est ensuite chiffre comme l'app (sha1, 16 caracteres) et cherche dans
audio/mp3/<voix>/ -- le dossier depose sur Hosting.
"""
import argparse, collections, functools, hashlib, http.server, io, json, os, re, socketserver, sys, threading

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
PORT = 8793
PORTEUSE = "Palabra. ... %s"

COLLECTE = r"""
async () => {
  const out = {};
  const add = (cat, t) => { if(t == null) return; t = String(t); if(!t.trim()) return; (out[cat] = out[cat] || new Set()).add(t); };
  window.accesComplet = () => true;
  window.direAllemand = (t) => add("autre", t);
  const paquets = [];
  const pousser = (mode, theme, filtre) => { if(!theme || !theme.words) return;
    theme.words.forEach((w, i) => paquets.push({ mode, it: { word: w, index: i, themeId: theme.id } })); };
  try{ if(typeof loadThemesJson === "function") await loadThemesJson(); }catch(e){}
  themesComptes().forEach(th => LEVELS.forEach(l => { const d = th.levels[l];
    if(d) d.words.forEach((w, i) => paquets.push({ mode: "nomen", it: { word: w, index: i, themeId: d.id } })); }));
  const autres = { verben: "verbeTheme", adjektive: "adjektiveTheme", adverbien: "adverbienTheme",
                   redewendungen: "redewendungenTheme", partikeln: "partikelnTheme", konjunktionen: "konjunktionenTheme",
                   praep: "praepTheme", zahlen: "zahlenTheme" };
  // Pronoms : un paquet allemand seulement (« man ») -- l'espagnol n'en a pas.
  if(LANGUE_APPRISE !== "es") autres.pronomen = "pronomenVokabularTheme";
  for(const [mode, nom] of Object.entries(autres)){ try{ pousser(mode, eval(nom)); }catch(e){} }
  let rates = 0;
  const net = (m) => { let d = m.replace(/^[¿¡«"(]+|[.,;:!?»")]+$/g, ""); if(LANGUE_APPRISE === "es") d = d.toLowerCase();
                       return d && /[\p{L}\p{N}]/u.test(d) ? d : ""; };
  for(const p of paquets){
    try{
      flashcardMode = p.mode; currentCards = [p.it]; currentCardsFull = [p.it]; currentFlashcard = 0;
      loadFlashcard();
      try{ flipCard(); }catch(e){}
      add("carte.mot", texteCarteAPrononcer());
      etapesChaineCarte().forEach(e => add("carte." + e.groupe, e.texte));
      if(typeof texteAudioPluriel !== "undefined") add("carte.pluriel", texteAudioPluriel);
      if(typeof texteAudioExemple !== "undefined") add("carte.phrase", texteAudioExemple);
    }catch(e){ rates++; }
    try{
      const it = Object.assign({ mode: p.mode }, p.it);
      const ph = phraseDeCarte(it, 11);
      if(ph){ add("seance.phrase", ph.de); ph.mots.forEach(m => add("seance.tuile", net(m))); }
      if(["nomen", "verben", "adjektive"].indexOf(p.mode) >= 0) add("seance.dictee", motDictee(it));
    }catch(e){}
  }
  // La feuille de conjugaison : la phrase d'un autre temps du verbe, 3 a 10 mots
  // (preparerFeuille / verbeVuPourFeuille). En espagnol le champ est
  // « exemple_<temps> » (champTempsFeuille) ; en allemand, le nom du temps.
  paquets.filter(p => p.mode === "verben").forEach(p => {
    Object.keys(p.it.word).forEach(k => {
      const v = p.it.word[k];
      if(typeof v !== "string" || (LANGUE_APPRISE === "es" ? !/^exemple_(preterito|imperfecto|perfecto|futuro|condicional|subjuntivo|imperativo)$/.test(k) : !/^(perfekt|praeteritum|konjunktiv2|futur|plusquamperfekt)$/.test(k))) return;
      const mots = motsPhrase(v);
      if(mots.length < 3 || mots.length > 10) return;
      add("feuille.phrase", v.trim()); mots.forEach(m => add("feuille.tuile", net(m)));
    });
  });
  // L'ecran « Ecouter » des phrases, et celui de « Construire la phrase ».
  try{ phrasesEcoutables("ALL").forEach(ph => add("ecoute_phrases", ph.de)); }catch(e){ out.__ecoute_phrases = new Set([String(e)]); }
  try{ phrasesTraduisibles("ALL").forEach(ph => add("construire.phrase", ph.de)); }catch(e){}
  // Les exercices : le texte que direPhraseExercice() demande.
  try{
    const ex = await (await fetch(urlDonnees("exercices.json"))).json();
    const jeux = ex && ex.jeux ? ex.jeux : ex;
    const listes = Array.isArray(jeux) ? [jeux] : Object.values(jeux).filter(Array.isArray);
    listes.forEach(l => l.forEach(e => { try{ add("exercice", phraseAllemandeDeLExercice(e)); }catch(x){} }));
  }catch(e){ out.__exercices = new Set([String(e)]); }
  try{ LEVELS.concat(["ALL"]).forEach(n => { (poolEcoute(n) || []).forEach(item => {
      const c = contenuEcoute(item); add("ecoute.mot", c.cibleMot); add("ecoute.phrase", c.ciblePhrase); }); }); }catch(e){ out.__ecoute = new Set([String(e)]); }
  const res = {}; for(const k in out) res[k] = Array.from(out[k]);
  res.__paquets = [String(paquets.length), String(rates)];
  return res;
}
"""


def serveur():
    gestion = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    gestion.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def collecter(app, variante):
    from playwright.sync_api import sync_playwright
    adresse = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if app == "es" else "")
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
        page = ctx.new_page()
        page.on("dialog", lambda d: d.dismiss())
        page.goto(adresse)
        page.wait_for_load_state("networkidle")
        if variante == "latam":
            page.evaluate("() => localStorage.setItem(PREFIXE_STOCKAGE + 'variante', 'latam')")
            page.reload()
            page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        assert page.evaluate("() => VARIANTE_ESPAGNOL") == (variante or "es"), "variante non prise"
        r = page.evaluate(COLLECTE)
        nav.close()
    return r


def manifeste(app, variante):
    """Les surfaces lues telles quelles dans les donnees."""
    out = collections.defaultdict(set)
    garder = ("premiers_pas", "a1_voyage", "reperes", "scenes", "tuiles", "conjugaison", "fiches", "scene")
    if app == "es":
        import manifest_es
        for t, s, n in manifest_es.recolter(variante):
            if s.startswith(garder):
                out["manifeste." + s.split(".")[0]].add(t)
    else:
        for e in json.load(io.open(os.path.join(RACINE, "audio", "manifest.json"), encoding="utf-8")):
            for s in e.get("sources", []):
                if s.startswith(garder) or s.startswith(("premiers", "a1", "repere", "scene", "kapitel")):
                    out["manifeste." + s.split(".")[0]].add(e["texte"])
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--app", default="es", choices=["es", "de"])
    p.add_argument("--json", default="")
    a = p.parse_args()
    voix = [("es", "es-es"), ("latam", "es-419")] if a.app == "es" else [(None, "")]
    import logging
    srv = serveur()
    rapport = {}
    try:
        for variante, dossier in voix:
            base = os.path.join(RACINE, "audio", "mp3", dossier)
            present = lambda t: os.path.exists(os.path.join(base, hashlib.sha1(t.encode("utf-8")).hexdigest()[:16] + ".mp3"))
            r = collecter(a.app, variante)
            paquets, rates = r.pop("__paquets")
            cats = {k: set(v) for k, v in r.items() if not k.startswith("__")}
            for k, v in manifeste(a.app, variante).items():
                cats[k] = v
            nom = dossier or "de"
            print("%s : %s cartes parcourues (%s en erreur)" % (nom, paquets, rates))
            for k in r:
                if k.startswith("__"):
                    print("  ECHEC %s : %s" % (k, list(r[k])[0][:160]))
            tous_manquants = set()
            rapport[nom] = {}
            for k in sorted(cats):
                manq = sorted(t for t in cats[k] if not present(t))
                tous_manquants |= set(manq)
                rapport[nom][k] = {"textes": len(cats[k]), "sans_fichier": manq}
                print("  %-26s %6d textes  %5d sans fichier  %s" % (k, len(cats[k]), len(manq),
                      " | ".join(manq[:4])))
            cout = sum(len(PORTEUSE % t) if " " not in t else len(t) for t in tous_manquants)
            print("  TOTAL distincts sans fichier : %d, environ %d credits (v2 ; porteuse pour les mots seuls)"
                  % (len(tous_manquants), cout))
    finally:
        srv.shutdown()
    if a.json:
        json.dump(rapport, io.open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
