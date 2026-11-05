# -*- coding: utf-8 -*-
"""La question du changement de niveau (v1113), de bout en bout dans la page.

    python tests/changement_niveau.py              (allemand)
    python tests/changement_niveau.py --app es     (ou en, pt)

Decide par Jacques le 5 nov. 2026 (decisions/DECISIONS.md, « Changement de
niveau ») : en montant de niveau, l'app demande si les mots commences plus bas
sont deja connus. Ce test pose 3 mots A1 vus, dont 1 rate, monte de l'A1 au B1
et verifie :
  1. la question s'affiche, avec 3 mots ; chacun recoit q (posee une fois) ;
  2. « Garde ceux que j'ai rates » : la seance B1 ne ramene que le mot rate ;
     la seance A1, elle, ramene encore les trois ;
  3. « Oui, je les connais » : la seance B1 n'en ramene aucun, et aucun n'est
     marque maitrise (les compteurs ne bougent pas) ;
  4. une deuxieme montee ne repose pas la question sur les memes mots ;
  5. en descendant (B1 -> A1), pas de question.
Il ne se connecte pas : comme fusion-espagnol/parcours.py, il appelle les
fonctions de la page. Il ouvre un navigateur : a lancer SOUS LE VERROU des
parcours (~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("PARCOURS_PORT", "8797"))

# Trois mots A1 de la seance : deux vus sans faute, un rate (reviews > srsHits).
POSER = r"""
() => {
  localStorage.setItem(NIVEAU_SEANCE_KEY, "A1");
  const p = paquetSeanceDuNiveau("A1").slice(0, 3);
  const hier = Date.now() - 86400000;
  const etats = [
    { mastered: false, due: hier, reviews: 1, srsHits: 1 },
    { mastered: false, due: hier, reviews: 2, srsHits: 2 },
    { mastered: false, due: hier, reviews: 2, srsHits: 0 }   // reussi, puis rate
  ];
  p.forEach((it, i) => setWordState(it.themeId, it.index, etats[i]));
  window.__mots = p.map(it => ({ k: it.themeId, i: it.index }));
  return p.length;
}
"""
ETAT = r"""
(niv) => {
  const cles = new Set(window.__mots.map(m => m.k + "|" + m.i));
  const dues = echeancesDeSeance(niv, accesComplet())
    .filter(it => cles.has(it.themeId + "|" + it.index))
    .filter(it => !estNeuf(getWordState(it.themeId, it.index)));
  const v = document.querySelector(".niveau-voile");
  return {
    question: !!v,
    titre: v ? v.querySelector(".niveau-titre").textContent : "",
    dues: dues.length,
    q: window.__mots.filter(m => getWordState(m.k, m.i).q).length,
    connus: window.__mots.filter(m => getWordState(m.k, m.i).connu).length,
    maitrises: window.__mots.filter(m => getWordState(m.k, m.i).mastered).length
  };
}
"""


def serveur():
    gestion = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RACINE)
    gestion.log_message = lambda *a, **k: None
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default="de", choices=["de", "es", "en", "pt"])
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    chemin = "index.html" + ("" if a.app == "de" else "?apprendre=" + a.app)
    srv = serveur()
    fautes = []

    def attendu(nom, vrai):
        print("  %-62s %s" % (nom, "ok" if vrai else "FAUX"))
        if not vrai:
            fautes.append(nom)

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for bouton in ("garder", "oui"):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844},
                                      service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.goto("http://127.0.0.1:%d/%s" % (PORT, chemin))
                page.wait_for_function("() => typeof paquetSeanceDuNiveau === 'function' && paquetSeanceDuNiveau('A1').length > 0",
                                       timeout=60000)
                print("\n[%s] reponse « %s »" % (a.app, bouton))
                n = page.evaluate(POSER)
                attendu("trois mots A1 poses", n == 3)
                e = page.evaluate(ETAT, "B1")
                attendu("sans reponse, la regle vaut deja : en B1, seul le rate", e["dues"] == 1)
                page.evaluate("() => fixerNiveauSeance('B1', true)")
                page.wait_for_selector(".niveau-voile", timeout=10000)
                e = page.evaluate(ETAT, "B1")
                attendu("A1 -> B1 : la question s'affiche", e["question"])
                attendu("le titre compte 3 mots", "3" in e["titre"])
                attendu("les 3 mots recoivent q", e["q"] == 3)
                page.click(".niveau-" + bouton)
                page.wait_for_timeout(300)
                e = page.evaluate(ETAT, "B1")
                attendu("la fenetre se ferme", not e["question"])
                if bouton == "garder":
                    attendu("seance B1 : seul le mot rate revient", e["dues"] == 1)
                    attendu("aucun mot marque connu", e["connus"] == 0)
                    attendu("seance A1 : les 3 reviennent encore", page.evaluate(ETAT, "A1")["dues"] == 3)
                else:
                    attendu("seance B1 : aucun mot ne revient", e["dues"] == 0)
                    attendu("les 3 mots marques connus", e["connus"] == 3)
                attendu("aucun mot marque maitrise", e["maitrises"] == 0)
                # Redescendre puis remonter : pas de question, ni a la descente
                # ni sur des mots deja presentes.
                page.evaluate("() => fixerNiveauSeance('A1', true)")
                page.wait_for_timeout(800)
                attendu("B1 -> A1 : pas de question", not page.evaluate(ETAT, "A1")["question"])
                page.evaluate("() => fixerNiveauSeance('B1', true)")
                page.wait_for_timeout(800)
                attendu("remonter : pas de seconde question sur les memes mots", not page.evaluate(ETAT, "B1")["question"])
                attendu("aucune erreur JavaScript", not erreurs)
                for x in erreurs:
                    print("     ", x)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("\n%s" % ("TOUT EST BON" if not fautes else "%d FAUTE(S)" % len(fautes)))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
