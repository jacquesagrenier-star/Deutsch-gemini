# -*- coding: utf-8 -*-
"""La barre de la seance du jour sur les reprises (retour de Jacques, 8 nov. 2026, v1139).

    python tests/barre_reprises.py                     (de et es, seance legere coupee puis allumee)
    python tests/barre_reprises.py --app es
    python tests/barre_reprises.py --index AUTRE.html  (sert ce fichier a la place d'index.html)

« Tout a coup, j'ai des cartes, mais je ne vois plus de progression. » La barre
en parties ne vaut que pour le paquet de l'ouverture ; toute reprise en met un
autre a l'ecran. Le parcours n'ouvre pas la seance : il ne le voit pas.

Chaque cas ouvre une seance du jour, va jusqu'au geste, et regarde #seanceParts
sur la premiere carte de la reprise, puis sur la deuxieme (la barre doit avancer) :
  ouverture, fin courte (« ‹ » puis Continuer la seance) : les parties ;
  en faire plus / Encore une seance (le meme bouton, selon la seance legere) ;
  les cartes revenues, les cartes « Encore », les phrases ratees (sans ecran de fin) ;
  Refaire les mots rates, Revoir les cartes non maitrisees / maitrisees.
Il ne se connecte pas, il appelle les fonctions de la page. Il ouvre un
navigateur : a lancer SOUS LE VERROU des parcours
(~/.wortando/REGLE-VERROU-PARCOURS.txt).
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
PORT = int(os.environ.get("PARCOURS_PORT", "8796"))
INDEX = None


class Silencieux(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass

    def translate_path(self, path):
        if INDEX and path.split("?")[0].rstrip("/") in ("", "/index.html"):
            return INDEX
        return super().translate_path(path)


CAS = ["ouverture", "fin_courte", "en_plus", "revenues", "encore", "phrases_ratees",
       "refaire_erreurs", "non_maitrisees", "maitrisees"]

MESURE = r"""
async ([cas, legere]) => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  try { localStorage.setItem(AIDE_CONTINUER_KEY, '1'); } catch(e) {}
  if(!window.__orig){ window.__orig = window.essaiActif; }
  window.essaiActif = n => n === 'seance_legere' ? legere : window.__orig(n);
  try { hideFlashcardEnd(); } catch(e) {}
  try { fermerFinCourte(); } catch(e) {}
  try { ajouterSerieNeufs(); } catch(e) {}
  await ouvrirSeanceDuJour(true);
  await pause(500);
  const lire = () => {
    const b = document.getElementById('seanceParts');
    const i = b ? b.querySelector('i.ici') : null;
    return { visible: !!(b && !b.classList.contains('hidden') && b.offsetHeight > 0), parts: b ? b.children.length : 0,
             q: i ? i.style.getPropertyValue('--q') : null, parties: seancePartsActive(),
             rang: currentFlashcard, n: currentCards.length, titre: (document.getElementById('flashThemeTitle') || {}).textContent || '' };
  };
  const ouvert = currentCards;
  const finir = () => { currentFlashcard = currentCards.length; return showFlashcardEnd(); };
  const motDuPaquet = () => currentCards.find(c => c && c.word && c.mode !== 'phrase' && typeof c.index === 'number');
  const enDernier = () => { currentFlashcard = Math.max(0, currentCards.length - 1); };
  let note = '';
  if(cas === 'fin_courte'){
    currentFlashcard = Math.min(2, currentCards.length - 1); loadFlashcard();
    montrerFinCourte(); await pause(100); reprendreSeanceCourte(); await pause(100);
    return { cas, avant: lire(), apres: lire(), note: 'meme paquet : ' + (currentCards === ouvert) };
  }
  if(cas === 'en_plus'){
    finir(); await pause(200);
    note = 'bouton visible : ' + !document.getElementById('encoreNeufsBtn').classList.contains('hidden');
    encoreDesMotsNeufs();
    for(let k = 0; k < 40 && currentCards === ouvert; k++) await pause(100);
    await pause(400);
  }
  if(cas === 'revenues' || cas === 'encore'){
    const it = motDuPaquet();
    (currentCardsFull || []).forEach(c => { const s = getWordState(c.themeId, c.index); if(s.due && !s.mastered && c !== it){ s.due = Date.now() + 864e5; if(!s.srsHits) s.srsHits = 1; setWordState(c.themeId, c.index, s); } });
    const st = getWordState(it.themeId, it.index);
    st.srsHits = 0; st.mastered = false; st.vu = Date.now();
    st.due = cas === 'revenues' ? Date.now() - 1000 : Date.now() + 60000;
    setWordState(it.themeId, it.index, st);
    enDernier(); nextFlashcard(); await pause(300);
  }
  if(cas === 'phrases_ratees'){
    const it = motDuPaquet();
    RETOURS_FIN_SEANCE.length = 0; RETOURS_FIN_SEANCE.push(it, currentCards.find(c => c !== it && c.word && c.mode !== 'phrase') || it);
    (currentCardsFull || []).forEach(c => { const s = getWordState(c.themeId, c.index); if(s.due && !s.mastered){ s.due = Date.now() + 864e5; if(!s.srsHits) s.srsHits = 1; setWordState(c.themeId, c.index, s); } });
    enDernier(); nextFlashcard(); await pause(300);
  }
  if(cas === 'refaire_erreurs'){
    const mots = currentCards.filter(c => c && c.word && c.mode !== 'phrase').slice(0, 3);
    ERREURS_SEANCE.length = 0;
    mots.forEach(it => { try { noterErreurSeance(it, 'x' + it.index, 'y'); } catch(e) { note = String(e); } });
    finir(); await pause(200); note += ' erreurs : ' + erreursDeLaSeance().length;
    refaireErreurs(); await pause(300);
  }
  if(cas === 'non_maitrisees' || cas === 'maitrisees'){
    finir(); await pause(200);
    if(cas === 'maitrisees'){ const it = currentCardsFull[0]; const s = getWordState(it.themeId, it.index); s.mastered = true; setWordState(it.themeId, it.index, s);
      const j = currentCardsFull[1]; const r = getWordState(j.themeId, j.index); r.mastered = true; setWordState(j.themeId, j.index, r); }
    const cache = window.getComputedStyle(document.querySelector('[onclick="retryUnmastered()"]')).display === 'none';
    note = 'bouton cache : ' + cache;
    if(cas === 'non_maitrisees') retryUnmastered(); else retryMastered();
    hideFlashcardEnd(); await pause(300);
  }
  const avant = lire();
  if(currentCards.length > 1){ currentFlashcard = 1; try { loadFlashcard(); } catch(e) { note += ' err ' + e; } await pause(150); }
  return { cas, avant, apres: lire(), note, change: currentCards !== ouvert };
}
"""


def verdict(r):
    a, b = r["avant"], r["apres"]
    if not a["visible"] or not b["visible"]:
        return "SANS BARRE"
    if r["cas"] in ("ouverture", "fin_courte"):
        return "ok" if a["parts"] >= 1 else "SANS BARRE"
    if a["parties"]:
        return "ok"  # une seance entiere rouverte : ses parties
    if a["n"] > 1 and b["q"] != "%d%%" % round(100 * b["rang"] / b["n"]):
        return "BARRE FAUSSE"
    return "ok"


def main():
    global INDEX
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", choices=["de", "es"], action="append")
    ap.add_argument("--index")
    a = ap.parse_args()
    INDEX = os.path.abspath(a.index) if a.index else None
    from playwright.sync_api import sync_playwright
    socketserver.ThreadingTCPServer.allow_reuse_address = False
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), functools.partial(Silencieux, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    fautes = 0
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for langue in (a.app or ["de", "es"]):
                for legere in (False, True):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844}, service_workers="block")
                    page = ctx.new_page()
                    erreurs = []
                    page.on("pageerror", lambda e: erreurs.append(str(e).split("\n")[0]))
                    page.on("dialog", lambda d: d.dismiss())
                    page.goto("http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if langue == "es" else ""))
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(2000)
                    print("== %s, seance legere %s" % (langue, "allumee" if legere else "coupee"), flush=True)
                    for cas in CAS:
                        try:
                            r = page.evaluate(MESURE, [cas, legere])
                            v = verdict(r)
                        except Exception as e:
                            r, v = None, "ERREUR " + str(e).split("\n")[0][:200]
                        if v != "ok":
                            fautes += 1
                        if r:
                            x, y = r["avant"], r["apres"]
                            print("  %-16s %-11s parties=%-5s tranches=%d q %s -> %s  carte %d/%d  %s" % (
                                cas, v, x["parties"], x["parts"], x["q"], y["q"], x["rang"] + 1, x["n"], r.get("note", "")), flush=True)
                        else:
                            print("  %-16s %s" % (cas, v), flush=True)
                    print("  erreurs JS :", json.dumps(sorted(set(erreurs))[:5], ensure_ascii=False), flush=True)
                    ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    print("RESULTAT : %s" % ("aucune reprise sans barre" if not fautes else "%d cas en defaut" % fautes))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
