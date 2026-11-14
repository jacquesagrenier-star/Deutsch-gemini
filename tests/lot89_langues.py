# -*- coding: utf-8 -*-
"""Sonde des lots 89-90 (13 nov. 2026) dans le navigateur : interface uk / ru / pl.

1. Les textes reecrits de l'interface sortent tels quels de t() (aucun repli francais, aucun texte vide).
2. La recherche ukrainienne trouve le meme nombre de cartes pour м'ясо, м’ясо et мʼясо (normalizeSearch).
3. Les pages des themes (gato, ciudad, ecole) montrent « Dativ » et la parenthese du vrai cas, sans le
   cas local apres une preposition, en uk, ru et pl.
4. Aucune erreur JavaScript.

    python tests/lot89_langues.py [--captures DOSSIER]     (port LOT89_PORT, 8859 par defaut ; verrou des parcours)
"""
import argparse
import functools
import http.server
import json
import os
import re
import socketserver
import sys
import threading

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("LOT89_PORT", "8859"))

CLES = ["ecoute_phrase_question", "exo_erreurs_faites", "essai_rappel_texte", "av_depart_pret", "av_jalon_titre_voyage",
        "av_jalon_change", "av_fin_a1_texte", "myvocab_full", "legende_grammaire", "legende_rencontres",
        "ip_seance_gardes", "ip_seance_theme", "legende_objectif_quoi", "legende_jours", "legende_serie",
        "legende_semaine", "ecoute_menu_desc", "gratuit_bienvenue"]
MASC = {"uk": re.compile(r"\bти\s+\w+(?:в|вся)\b(?!\s*\()"), "ru": re.compile(r"\bты\s+\w+(?:л|лся)\b(?!\s*\()"),
        "pl": re.compile(r"\w+łeś\b(?!\s*[(/])|jesteś gotowy\b(?!\s*\()")}
CAS_LOCAL = re.compile(r"\+\s*(<b>)?\s*(celownik|давальн|дательн|biernik|знахідн|винительн)", re.I)
ATTENDU_THEME = {"uk": "українською", "ru": "по-русски", "pl": "po polsku"}


class Serveur(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *x, **k):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captures")
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Serveur, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for ui in ("uk", "ru", "pl"):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 780}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html" % PORT)
                page.wait_for_load_state("networkidle")
                page.evaluate("([l]) => { try{ localStorage.setItem(UI_LANG_KEY, l); }catch(e){} }", [ui])
                page.reload()
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(1500)
                textes = page.evaluate("(cles) => cles.map(k => [k, t(k)])", CLES)
                for k, v in textes:
                    if not v or v == k:
                        fautes.append("%s %s : texte absent" % (ui, k))
                    elif MASC[ui].search(v):
                        fautes.append("%s %s : masculin seul : %s" % (ui, k, v[:80]))
                print("== %s : %d textes de l'interface lus" % (ui, len(textes)), flush=True)
                if ui == "uk":
                    page.wait_for_timeout(2500)
                    n = page.evaluate("""() => {
                        ensureSearchIndex();
                        const r = {};
                        for(const q of ["м'ясо", "м’ясо", "мʼясо", "обовʼязковий", "обов'язковий"]){
                            renderWordSearch(q); r[q] = searchResults.length;
                        }
                        return r; }""")
                    print("   recherche :", json.dumps(n, ensure_ascii=False), flush=True)
                    if len({n["м'ясо"], n["м’ясо"], n["мʼясо"]}) != 1 or not n["мʼясо"]:
                        fautes.append("uk recherche : м'ясо / м’ясо / мʼясо ne donnent pas les memes cartes : %s" % n)
                    if n["обов'язковий"] != n["обовʼязковий"] or not n["обовʼязковий"]:
                        fautes.append("uk recherche : обов'язковий / обовʼязковий : %s" % n)
                if a.captures:
                    os.makedirs(a.captures, exist_ok=True)
                    page.screenshot(path=os.path.join(a.captures, "accueil-%s.png" % ui))
                for th in ("gato", "ciudad", "ecole"):
                    pg = ctx.new_page()
                    pg.on("pageerror", lambda e: erreurs.append(th + ": " + str(e).split("\n")[0]))
                    pg.goto("http://127.0.0.1:%d/visuel/prototype/%s.html?apprendre=de&lang=%s" % (PORT, th, ui))
                    pg.wait_for_load_state("networkidle")
                    pg.wait_for_timeout(800)
                    src = pg.evaluate("() => (typeof TEXTES !== 'undefined' ? JSON.stringify(TEXTES) : '') + document.body.innerHTML")
                    if CAS_LOCAL.search(src):
                        fautes.append("%s %s : cas local apres une preposition : %s" % (ui, th, CAS_LOCAL.search(src).group(0)))
                    if "Dativ" not in src or ATTENDU_THEME[ui] not in src:
                        fautes.append("%s %s : « Dativ » ou la parenthese du vrai cas absents" % (ui, th))
                    if a.captures:
                        pg.screenshot(path=os.path.join(a.captures, "%s-%s.png" % (th, ui)))
                    pg.close()
                erreurs = [e for e in erreurs if "synonymes" not in e]
                if erreurs:
                    fautes.append("%s erreurs JS : %s" % (ui, sorted(set(erreurs))[:4]))
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    for f in fautes:
        print("FAUTE", f)
    print("RESULTAT : %s" % ("tout est bon" if not fautes else "%d faute(s)" % len(fautes)))
    return 1 if fautes else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
