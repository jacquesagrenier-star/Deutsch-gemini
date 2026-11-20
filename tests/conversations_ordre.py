# -*- coding: utf-8 -*-
"""Les choix d'une conversation, A L'ECRAN (ligne 150, 20 nov. 2026) : le piege n'est plus toujours le dernier.
Le controle sans navigateur (node tests/conversations_ordre.js) juge toutes les conversations sur l'ordre calcule ;
cette sonde verifie que la PAGE montre bien cet ordre, et que rien n'a casse autour. Une conversation jouee jusqu'a
sa fin, en allemand et en espagnol appris, interface en francais et en arabe, a 360 px :
  - les boutons affiches sont les choix du noeud, dans l'ordre d'ordreDesChoix(), chacun avec son texte ;
  - a chaque noeud qui a un piege, on le touche d'abord : la conversation y revient, LES CHOIX GARDENT LE MEME ORDRE,
    et c'est bien le bouton du piege qui est barre et desactive (le choix est repere par son indice des donnees) ;
  - puis une reponse juste fait avancer, jusqu'a l'ecran de fin ;
  - sur le chemin, le piege n'est pas toujours a la meme place, ni toujours le dernier ; la page tient en 360 px.
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/conversations_ordre.py <racine> <port> [conversation, defaut a2-assurance]"""
import collections, functools, http.server, os, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT = os.path.abspath(sys.argv[1]), int(sys.argv[2])
CONV = sys.argv[3] if len(sys.argv) > 3 else "a2-assurance"
PASSES = [("de", "fr"), ("de", "ar"), ("es", "fr"), ("es", "ar")]


class Calme(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


# Ce que la page montre, et ce qu'elle devrait montrer : les boutons visibles, et les choix du noeud dans l'ordre
# calcule (ordreDesChoix), avec leur indice des donnees.
ETAT = """() => {
  const zone = document.querySelector('.repondre');
  const visible = !!(zone && !zone.hidden && zone.querySelector('.choix button'));
  const fin = !!document.querySelector('.carte.fin');
  if(!visible) return { visible: false, fin: fin, noeud: (typeof noeud !== 'undefined') ? noeud : null };
  const boutons = Array.from(zone.querySelectorAll('.choix button')).map(b => ({
    texte: (b.querySelector('b') || {}).textContent || '', barre: b.classList.contains('faux-essaye'), inactif: b.disabled }));
  const brut = (C.noeuds[noeud].choix || []);
  const attendus = choixDe(noeud).map(c => ({ i: c.i, faux: !!c.faux, repete: !!c.repete, texte: gabarit(T(c, 't'), LANGUE) }));
  return { visible: true, fin: fin, noeud: noeud, boutons: boutons, attendus: attendus, fichier: brut.map((c, i) => i),
           essayes: Array.from((S.essaye[noeud] || new Set())), page: document.documentElement.scrollWidth, dir: document.documentElement.dir || document.body.dir || '' };
}"""


def main():
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for apprise, ui in PASSES:
                nom = "%s/%s" % (apprise, ui)
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 740}, service_workers="block")
                page = ctx.new_page()
                erreurs = []
                page.on("pageerror", lambda e: erreurs.append(str(e).splitlines()[0][:140] if str(e) else ""))
                page.goto("http://127.0.0.1:%d/visuel/prototype/conversation.html?c=%s&apprendre=%s&lang=%s" % (PORT, CONV, apprise, ui), wait_until="domcontentloaded")
                try:
                    page.wait_for_selector("button.gros", timeout=30000)
                except Exception:
                    bilan.append("%s : la conversation %s ne s'ouvre pas" % (nom, CONV)); ctx.close(); continue
                page.evaluate("() => document.querySelector('button.gros').click()")

                def attendre_choix(maxi=60000):
                    t = 0
                    while t < maxi:
                        s = page.evaluate(ETAT)
                        if s["visible"] or s["fin"]:
                            return s
                        page.wait_for_timeout(400); t += 400
                    return page.evaluate(ETAT)

                places, noeuds_vus, reordonnes = [], 0, 0
                for tour in range(30):
                    s = attendre_choix()
                    if not s["visible"]:
                        break
                    noeuds_vus += 1
                    if noeuds_vus == 2 and os.environ.get("CAPTURES"):
                        page.screenshot(path=os.path.join(os.environ["CAPTURES"], "conv-ordre-%s-%s.png" % (apprise, ui)))
                    textes = [b["texte"] for b in s["boutons"]]
                    if textes != [a["texte"] for a in s["attendus"]]:
                        bilan.append("%s, noeud %s : les boutons ne suivent pas l'ordre calcule (%s)" % (nom, s["noeud"], textes[:3]))
                        break
                    if [a["i"] for a in s["attendus"]] != s["fichier"][:len(s["attendus"])]:
                        reordonnes += 1
                    if s["page"] > 360:
                        bilan.append("%s, noeud %s : la page fait %d px" % (nom, s["noeud"], s["page"]))
                    pieges = [k for k, a in enumerate(s["attendus"]) if a["faux"]]
                    libres = [k for k in pieges if s["attendus"][k]["i"] not in s["essayes"]]
                    if libres:
                        k = libres[0]
                        corps = len([a for a in s["attendus"] if not (a["repete"] and not a["faux"])])
                        places.append((k, corps))
                        avant = [a["i"] for a in s["attendus"]]
                        page.evaluate("(k) => document.querySelectorAll('.repondre .choix button')[k].click()", k)
                        page.wait_for_timeout(600)
                        s2 = attendre_choix()
                        if not s2["visible"] or s2["noeud"] != s["noeud"]:
                            bilan.append("%s, noeud %s : apres le piege, la conversation ne revient pas au meme noeud" % (nom, s["noeud"])); break
                        if [a["i"] for a in s2["attendus"]] != avant or [b["texte"] for b in s2["boutons"]] != textes:
                            bilan.append("%s, noeud %s : l'ordre des choix a change apres l'erreur" % (nom, s["noeud"]))
                        marques = [j for j, b in enumerate(s2["boutons"]) if b["barre"] and b["inactif"]]
                        if marques != [k]:
                            bilan.append("%s, noeud %s : le bouton barre est %s, le piege touche etait a la place %d" % (nom, s["noeud"], marques, k + 1))
                        s = s2
                    justes = [k for k, a in enumerate(s["attendus"]) if not a["faux"] and not a["repete"]]
                    if not justes:
                        bilan.append("%s, noeud %s : aucune reponse juste a toucher" % (nom, s["noeud"])); break
                    page.evaluate("(k) => document.querySelectorAll('.repondre .choix button')[k].click()", justes[0])
                    page.wait_for_timeout(600)
                fini = page.evaluate("() => !!document.querySelector('.carte.fin')")
                if not fini:
                    bilan.append("%s : la conversation n'arrive pas a sa fin" % nom)
                if len(places) >= 4:
                    c = collections.Counter(k for k, n in places)
                    derniers = sum(1 for k, n in places if k == n - 1)
                    if max(c.values()) == len(places):
                        bilan.append("%s : le piege toujours a la place %d" % (nom, c.most_common(1)[0][0] + 1))
                    if derniers == len(places):
                        bilan.append("%s : le piege toujours en dernier" % nom)
                elif not places:
                    bilan.append("%s : aucun piege rencontre sur le chemin" % nom)
                if erreurs:
                    bilan.append("%s : erreurs JS %s" % (nom, erreurs[:2]))
                print("  %s %s : %d noeuds joues (%d dans un autre ordre que le fichier) ; place du piege, noeud par noeud : %s ; fin atteinte %s ; erreurs JS %d"
                      % (nom, CONV, noeuds_vus, reordonnes, " ".join("%d/%d" % (k + 1, n) for k, n in places), fini, len(erreurs)), flush=True)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("BILAN OK" if not bilan else "BILAN A REVOIR : " + " | ".join(bilan))


if __name__ == "__main__":
    main()
