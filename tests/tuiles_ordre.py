# -*- coding: utf-8 -*-
"""Les tuiles d'une serie, a l'ecran : LA BONNE REPONSE N'EST PLUS TOUJOURS LA PREMIERE (defaut D9 de la revue A a Z,
19 nov. 2026 ; remede dans les donnees : tests/ordre_options.py). Une serie reordonnee par langue apprise ; son
premier bloc est joue en entier, question par question :
  - les tuiles affichees sont celles du fichier, DANS L'ORDRE DU FICHIER (pas de melange a l'affichage) ;
  - toucher la tuile de la bonne reponse est compte juste (la reponse est designee par son texte : rien n'a casse) ;
  - sur le bloc, la bonne reponse ne tient pas la meme place dans plus de 60 % des questions, ni toujours la premiere.
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/tuiles_ordre.py <racine> <port> [apps, ex. de,es]"""
import collections, functools, http.server, io, json, os, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT = os.path.abspath(sys.argv[1]), int(sys.argv[2])
sys.path.insert(0, os.path.join(RACINE, "tests"))
import ordre_options as oo

# app -> (fichier, serie reordonnee par la ligne 149)
SERIES = {
    "de": ("exercices.json", "werdenExercises"),
    "es": ("espanol/datos/ejercicios.json", "preposicionesExercises"),
    "en": ("anglais/datos/exercices.json", "ordreAdjectifsEnExercises"),
    "pt": ("portugais/datos/exercices.json", "perifrasesA2PtExercises"),
    "ja": ("japonais/datos/exercices.json", "particulesJaExercises"),
}
APPS = sys.argv[3].split(",") if len(sys.argv) > 3 else list(SERIES)


class Calme(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


# Ce que l'ecran montre : les tuiles, dans l'ordre, de la carte de la seance (#cartePhrase) ou de l'ancien ecran
# d'exercices (#answerOptions) ; le verdict une fois la reponse donnee.
ETAT = """() => {
  const vis = e => !!(e && e.offsetParent !== null);
  const cp = document.getElementById('cartePhrase');
  if(cp && !cp.classList.contains('hidden') && cp.querySelector('.cp-choix')){
    const r = cp.querySelector('.cp-retour:not(.hidden)');
    return { mode: 'cartes', tuiles: Array.from(cp.querySelectorAll('.cp-choix button')).map(b => b.textContent),
             question: (cp.querySelector('.cp-phrase') || {}).textContent || '',
             verdict: r ? (r.classList.contains('bon') ? 'bon' : 'faux') : null };
  }
  const w = document.getElementById('answerOptions');
  if(w && vis(w) && w.querySelector('.option-pill')){
    const f = document.getElementById('feedback');
    return { mode: 'ecran', tuiles: Array.from(w.querySelectorAll('.option-pill')).map(b => b.textContent),
             question: (document.getElementById('question') || {}).textContent || '',
             verdict: f && f.classList.contains('correct') ? 'bon' : (f && f.classList.contains('wrong') ? 'faux' : null) };
  }
  return { mode: null, tuiles: [], question: '', verdict: null };
}"""
TOUCHER = """(i) => {
  const cp = document.getElementById('cartePhrase');
  if(cp && !cp.classList.contains('hidden') && cp.querySelector('.cp-choix')){ cp.querySelectorAll('.cp-choix button')[i].click(); return 'cartes'; }
  document.querySelectorAll('#answerOptions .option-pill')[i].click();
  document.getElementById('checkButton').click(); return 'ecran';
}"""
SUITE = """() => {
  const cp = document.getElementById('cartePhrase');
  const b = cp && !cp.classList.contains('hidden') ? cp.querySelector('.cp-actions button.primary:not(.hidden)') : null;
  if(b){ b.click(); return 'cartes'; }
  const n = document.getElementById('nextButton');
  if(n && !n.classList.contains('hidden')){ n.click(); return 'ecran'; }
  return null;
}"""


def main():
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for app in APPS:
                fichier, nom = SERIES[app]
                serie = json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8"))["jeux"][nom]
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 740}, service_workers="block")
                for motif in ("**/*firebase*", "**/*gstatic*", "**/*googleapis*", "**/*recaptcha*"):
                    ctx.route(motif, lambda r: r.abort())
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).splitlines()[0][:140] if str(e) else ""))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "" if app == "de" else "?apprendre=" + app), wait_until="domcontentloaded")
                page.wait_for_function("() => typeof startExerciseSet === 'function' && typeof goHome === 'function'", timeout=60000)
                page.wait_for_timeout(3000)
                page.evaluate("(nom) => { startExerciseSet(nom, 'fc_kicker', () => goHome(), null); }", nom)
                page.wait_for_timeout(2500)
                places, lignes, mode = [], [], None
                for tour in range(10):
                    s = page.evaluate(ETAT)
                    if not s["tuiles"]:
                        break
                    mode = s["mode"]
                    # la question du fichier qui a ces tuiles, dans cet ordre
                    cand = [ex for ex in serie if oo.a_options(ex) and [str(o) for o in ex["options"]] == s["tuiles"]]
                    morceau = lambda ex: max(str(ex.get("question", "")).split("___"), key=len).strip()
                    precis = [ex for ex in cand if morceau(ex) and morceau(ex) in s["question"]]
                    cand = precis or cand
                    if not cand:
                        bilan.append("%s %s, question %d : les tuiles %s ne sont l'ordre d'aucune question du fichier" % (app, nom, tour + 1, s["tuiles"]))
                        break
                    ex = cand[0]
                    i = oo.place(ex)
                    page.evaluate(TOUCHER, i)
                    page.wait_for_timeout(700)
                    v = page.evaluate(ETAT)["verdict"]
                    if v != "bon":
                        bilan.append("%s %s, question %d : la tuile %d (« %s ») n'est pas comptee juste (%s)" % (app, nom, tour + 1, i + 1, s["tuiles"][i], v))
                    places.append(i)
                    lignes.append("%d/%d" % (i + 1, len(s["tuiles"])))
                    if not page.evaluate(SUITE):
                        break
                    page.wait_for_timeout(1300)
                c = collections.Counter(places)
                if len(places) < 6:
                    bilan.append("%s %s : %d questions jouees seulement" % (app, nom, len(places)))
                else:
                    part = max(c.values()) / len(places)
                    if part > 0.6:
                        bilan.append("%s %s : la tuile %d est la bonne dans %d %% du bloc" % (app, nom, c.most_common(1)[0][0] + 1, round(100 * part)))
                    if len(c) < 2:
                        bilan.append("%s %s : la bonne reponse toujours a la meme place" % (app, nom))
                # Les erreurs JS sont dites, pas comptees : l'espagnol en a 13 connues (synonymes.json absent,
                # es-v1075), sans rapport avec les tuiles. Ce qui juge, ce sont les trois controles ci-dessus.
                print("  %s %-28s (%s) : place de la bonne tuile, question par question : %s ; erreurs JS %d%s"
                      % (app, nom, mode, " ".join(lignes), len(erreurs), (" (" + erreurs[0] + ")") if erreurs else ""), flush=True)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("BILAN OK" if not bilan else "BILAN A REVOIR : " + " | ".join(bilan))


if __name__ == "__main__":
    main()
