# -*- coding: utf-8 -*-
"""Du FRANCAIS a l'ecran quand l'interface est dans une autre langue.

    python tests/francais_ailleurs.py --app de                 # les 9 langues
    python tests/francais_ailleurs.py --app es --langues en,pt
    python tests/francais_ailleurs.py --app de --complet       # + chaque option des panneaux
    python tests/francais_ailleurs.py --app de --sortie releve.json

POURQUOI. Le 27 oct. 2026, les captures App Store en anglais montraient
« maitrise », « en cours » et « Premiers pas » en francais : l'accueil ne se
redessinait pas au changement de langue. Rien ne le voyait : cles_manquantes.js
mesure le dictionnaire, francais_en_dur.py le HTML statique ; ni l'un ni
l'autre ne voit un texte ecrit en JS, ni un ecran construit avant la bascule.

CE QU'IL FAIT, pour chaque langue :
  - A FROID : l'app ouverte directement dans la langue, chaque ecran visite ;
  - A CHAUD : l'app ouverte en francais, chaque ecran visite une fois, puis la
    langue changee dans les reglages comme le ferait l'usager, et les ecrans
    revisites. C'est ce mode-la qui voit un ecran qui garde l'ancienne langue.
Chaque ligne visible (et les title, aria-label, placeholder) est comparee au
releve francais. Est signalee une ligne IDENTIQUE a une ligne du releve
francais ET qui porte un marqueur du francais. L'identite ecarte la langue
cible elle-meme ; le marqueur ecarte le contenu allemand ou espagnol, qui est
le meme dans toutes les langues. Pour l'espagnol, les marqueurs qu'il partage
avec le francais (la, de, que, e accent aigu...) ne comptent pas.

Il ne se connecte PAS (comme fusion-espagnol/parcours.py) : les ecrans
s'ouvrent par leurs fonctions. Pour les reglages, qui exigent un compte, un
faux utilisateur est pose le temps de l'appel ; rien ne part chez Firebase.
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

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8793
HEURE_FIGEE = "2026-10-10T09:00:00"
LANGUES = {"de": ["en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"],
           "es": ["en", "pt", "ar"]}

HASARD_FIGE = r"""
(() => {
  let graine = 20261010;
  Math.random = () => {
    graine |= 0; graine = (graine + 0x6D2B79F5) | 0;
    let t = Math.imul(graine ^ (graine >>> 15), 1 | graine);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  window.__regrainer = (g) => { graine = g; };
})();
"""

# Tout ce qui se lit : le texte rendu de la page (les fenetres par-dessus
# l'ecran comprises), et les attributs que lit un lecteur d'ecran ou une bulle.
LIGNES = r"""
() => {
  document.querySelectorAll('.screen.active details').forEach(d => d.open = true);
  // Le toast (« Gel de serie disponible ») passe en trois secondes : ouvert
  // pendant l'echauffement, il serait releve dans l'ecran suivant.
  const toast = document.getElementById('badgeToast');
  if(toast) toast.style.visibility = 'hidden';
  const out = new Set();
  const texte = document.body.innerText;
  if(toast) toast.style.visibility = '';
  for(const l of texte.split('\n')){
    const s = l.replace(/[ \t ]+/g, ' ').trim();
    if(s) out.add(s);
  }
  document.querySelectorAll('[title],[aria-label],[placeholder]').forEach(e => {
    if(!e.getClientRects().length) return;
    for(const a of ['title', 'aria-label', 'placeholder']){
      const v = e.getAttribute(a);
      if(v && v.trim()) out.add('@' + a + ' ' + v.trim());
    }
  });
  return { ecran: (document.querySelector('.screen.active') || {}).id || '(aucun)', lignes: [...out] };
}
"""

# Les ecrans a visiter, ouverts par leur fonction depuis l'accueil. Une
# fonction absente (de/es n'ont pas tous les memes) est sautee sans bruit.
REGLAGES = """(() => {
  const vrai = window.firebaseAuth;
  window.firebaseAuth = { currentUser: { email: 'releve@exemple.test', uid: 'releve' } };
  try{ openSettings(); } finally { window.firebaseAuth = vrai; }
})()"""
ECRANS = [
    ("tout le contenu", "ouvrirToutLeContenu()"),
    ("seance du jour", "entrerSeanceDuJour()"),
    ("liste de la seance", "basculerListeSeance(new Event('click'))"),
    ("scene de la seance", "ouvrirSceneSeance()"),
    ("ecouter (menu)", "ouvrirEcouteMenu()"),
    ("ecouter (accueil)", "ecouterDepuisAccueil()"),
    ("feuilles", "ouvrirMesFeuilles()"),
    ("carnet de phrases", "ouvrirCarnetPhrases()"),
    ("galerie", "ouvrirGalerieMosaiques()"),
    ("mosaique plein ecran", "ouvrirMosaiquePleinEcran()"),
    ("badges", "ouvrirBadges()"),
    ("progression", "ouvrirInfoProgression()"),
    ("episodes", "ouvrirMesEpisodes()"),
    ("mis de cote", "ouvrirGardes()"),
    ("prononciation", "ouvrirPrononciation()"),
    ("mon vocabulaire", "openMyVocab()"),
    ("date de la seance", "ouvrirDateSeance()"),
    ("calendrier", "ouvrirCalendrierSerie(new Event('click'))"),
    ("gel de serie", "showStreakFreezeDetail()"),
    ("profil", "ouvrirProfil(() => goHome())"),
    ("recherche", "openWordSearch()"),
    ("abonnement", "ouvrirAbonnement(true)"),
    ("indice de grammaire", "abrirIndiceGramatica()"),
    ("themes du niveau", "ouvrirThemesDuNiveau()"),
    ("verbes A1", "startVerbeLevel('A1')"),
    ("adjectifs A1", "startAdjektiveLevel('A1')"),
    ("reglages", REGLAGES),
    ("connexion", "openAuth(); setAuthMode('login')"),
    ("inscription", "openAuth(); setAuthMode('signup')"),
]

# Ce qui ne trahit pas le francais, meme identique au releve francais.
MOTS_FR = r"le|les|des|du|au|aux|et|est|sont|pour|avec|dans|sur|pas|ne|tu|ton|ta|tes|ce|cette|ces|je|" \
          r"mon|ma|mes|ses|leur|nous|vous|qui|quoi|ou|où|plus|très|déjà|encore|ici|voici|jour|jours|" \
          r"semaine|mot|mots|carte|cartes|niveau|une?|que|la|de|en|à|écouter|réglages|séance|retour"
# Les mots que l'espagnol ecrit comme le francais (ou presque).
COMMUNS_ES = {"la", "le", "qui", "de", "en", "que", "un", "une", "tu", "ta", "mes", "ne", "ce", "ma", "les", "ses", "sur",
              "pas", "plus", "jour"}
# Les mots que l'allemand ecrit comme le francais : « du bist », le son « au ».
COMMUNS_DE = {"du", "au", "ma"}
ACCENTS_FR = "èêàçùâîôûœëï"
# Le nom de chaque langue dans sa langue, au choix de la langue d'interface.
ENDONYMES = {"Français", "Türkçe", "Português (Brasil)",
             "Sonne",   # le mot allemand de la prononciation (« ça sonne » en francais)
             "des",     # l'article allemand du genitif, seul sur un bouton de reponse
             "Nuance/Ton — attitude"}   # « attitude » s'ecrit aussi en anglais


def marqueur(ligne, app, langue=None):
    if ligne in ENDONYMES or re.fullmatch(r"(?:\[[^\]]*\]\s*)+", ligne):   # un son en API : [ç]
        return False
    mots = MOTS_FR.split("|")
    if langue == "pt":
        mots = [m for m in mots if m != "ou"]   # « ser ou estar » : le « ou » portugais
    if app == "de":
        mots = [m for m in mots if m not in COMMUNS_DE]
    if app == "es":
        mots = [m for m in mots if m not in COMMUNS_ES]
        accents = ACCENTS_FR
    else:
        accents = ACCENTS_FR + "é"
    if any(c in ligne.lower() for c in accents):
        return True
    # Une phrase espagnole du contenu (« Estudio para el examen. ») : ses mots
    # qui s'ecrivent aussi en francais ne trahissent rien.
    if app == "es" and re.search(r"[¿¡ñáíóú]|(?<!\w)(?:el|los|las|para|con|que|es|y|del|una)(?!\w)", ligne, re.I):
        return False
    # De meme une ligne allemande (« Nom. der die das die », « das Abonnement »).
    if app == "de" and re.search(r"[äöüß]|(?<!\w)(?:der|die|das|dem|den|ein|eine|einen|ich|und|ist|nicht|mit|Nom|Akk|Dat|Gen)(?!\w)", ligne):
        return False
    # Le trait d'union : « -en », « -e » sont des terminaisons, pas « en ».
    if re.search(r"(?<![\w’'-])(?:%s)(?![\w’'-])" %"|".join(map(re.escape, mots)), ligne, re.I):
        return True
    return any(m.lower() in lexique_fr() for m in re.findall(r"[^\W\d_]{3,}", ligne))


@functools.lru_cache(None)
def lexique_fr():
    """Les mots de l'interface francaise qu'aucune autre langue n'emploie.

    Sans lui, « Noms », « Verbes », « Particules » passaient : ni accent, ni
    petit mot. Un mot present aussi dans une autre langue (Akkusativ, Wortando,
    un exemple allemand ou espagnol cite) n'en fait pas partie."""
    import subprocess
    brut = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js")],
                          capture_output=True, check=True).stdout.decode("utf-8")
    dico = json.loads(brut)
    def mots(textes, minuscules=False):
        out = set()
        for v in textes:
            if isinstance(v, str):
                for m in re.findall(r"[^\W\d_]{3,}", re.sub(r"<[^>]*>", " ", v)):
                    if not minuscules or m.islower():
                        out.add(m.lower())
        return out
    autres = set()
    for lg, d in dico.items():
        if lg != "fr":
            autres |= mots(d.values())
    # Un mot qui ne s'ecrit jamais en minuscules est un nom allemand cite
    # (« Sonne » dans la prononciation), pas du francais.
    return frozenset(mots(dico["fr"].values(), minuscules=True) - autres)


class Muet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass


def serveur():
    gestion = functools.partial(Muet, directory=RACINE)
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), gestion)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


class Session:
    def __init__(self, nav, app, langue):
        self.app = app
        self.ctx = nav.new_context(locale="fr-FR", viewport={"width": 390, "height": 844},
                                   service_workers="block")
        self.ctx.add_init_script(HASARD_FIGE)
        self.page = self.ctx.new_page()
        self.page.clock.set_fixed_time(HEURE_FIGEE)
        self.erreurs = []
        self.page.on("pageerror", lambda e: self.erreurs.append(str(e).split("\n")[0]))
        self.page.on("dialog", lambda d: self.erreurs.append("dialogue : " + d.message[:200]) or d.dismiss())
        adresse = "http://127.0.0.1:%d/index.html%s" % (PORT, "?apprendre=es" if app == "es" else "")
        self.page.goto(adresse)
        self.page.wait_for_load_state("networkidle")
        self.page.evaluate("(l) => localStorage.setItem(UI_LANG_KEY, l)", langue)
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1500)
        self.releve = {}

    def attendre(self):
        try:
            self.page.wait_for_load_state("networkidle", timeout=3000)
        except Exception:
            pass
        self.page.wait_for_timeout(300)

    def js(self, code):
        try:
            self.page.evaluate("() => { " + code + "; }")
        except Exception as e:
            self.erreurs.append(str(e).split("\n")[0][:200])

    def existe(self, code):
        nom = re.match(r"([A-Za-z_]\w*)\(", code)
        return nom is None or self.page.evaluate("(n) => typeof window[n] === 'function'", nom.group(1))

    def accueil(self):
        # Les fenetres laissees ouvertes par l'ecran precedent : un usager les
        # ferme avant d'aller ailleurs. Restees la, elles seraient relevees
        # partout, dans la langue ou on les a ouvertes.
        self.js("window.__regrainer(20261010); "
                "for(let i = 0; i < 6; i++){ try{ if(!fermerFenetreDessus()) break; }catch(e){ break; } } "
                "for(const f of ['fermerListeSeance', 'fermerInfoProgression', 'fermerCalendrierSerie', 'fermerRepere', "
                "'fermerNiveauEcoute', 'fermerBullePP']) try{ window[f](); }catch(e){} "
                "const toast = document.getElementById('badgeToast'); if(toast) toast.classList.remove('show'); "
                "if(typeof VUE_CONTENU !== 'undefined') VUE_CONTENU = false; goHome()")
        self.attendre()

    def noter(self, chemin):
        etat = self.page.evaluate(LIGNES)
        self.releve[chemin] = {"ecran": etat["ecran"], "lignes": etat["lignes"], "erreurs": list(self.erreurs)}
        self.erreurs.clear()
        return etat["ecran"]

    def suite(self, chemin, ecran):
        """Le verso d'une carte, la reponse d'un exercice et son resultat."""
        if ecran == "flashcards":
            self.js("try{ flipCard(); }catch(e){} try{ if(document.querySelector('.verb-extra.hidden')) toggleVerbExtra(); }catch(e){}")
            self.attendre()
            self.noter(chemin + " [verso]")
        elif ecran == "exercise":
            self.js("const b = document.querySelector('#answerOptions button'); "
                    "if(b) b.click(); else { const a = document.getElementById('answer'); "
                    "if(a){ a.value = 'xyz'; } const c = document.getElementById('checkButton'); if(c) c.click(); }")
            self.attendre()
            self.noter(chemin + " [reponse]")
            self.js("showResults()")
            self.attendre()
            self.noter(chemin + " [resultat]")

    def visiter(self, ecrans, prefixe="", tuiles=True, complet=False):
        self.accueil()
        self.noter(prefixe + "accueil")
        for nom, code in ecrans:
            if not self.existe(code):
                continue
            self.accueil()
            self.js(code)
            self.attendre()
            self.suite(prefixe + nom, self.noter(prefixe + nom))
        if not tuiles:
            return
        self.js("ouvrirToutLeContenu()")
        self.attendre()
        orbs = self.page.evaluate("() => [...document.querySelectorAll('#home [data-orbid]')]"
                                  ".filter(e => e.offsetParent !== null).map(e => e.dataset.orbid)")
        for orb in orbs:
            self.accueil()
            self.js("ouvrirToutLeContenu(); document.querySelector('#home [data-orbid=\"%s\"]').click()" % orb)
            self.attendre()
            ecran = self.noter(prefixe + "tuile " + orb)
            self.suite(prefixe + "tuile " + orb, ecran)
            if not complet or ecran != "orbPanel":
                continue
            n = self.page.evaluate("() => document.querySelectorAll('#orbPanel .orb-opt').length")
            for i in range(n):
                self.accueil()
                self.js("ouvrirToutLeContenu(); document.querySelector('#home [data-orbid=\"%s\"]').click()" % orb)
                self.attendre()
                self.js("document.querySelectorAll('#orbPanel .orb-opt')[%d].click()" % i)
                self.attendre()
                ch = "%stuile %s > %d" % (prefixe, orb, i + 1)
                self.suite(ch, self.noter(ch))

    def basculer(self, langue):
        """Comme l'usager : depuis les reglages, puis le bouton de retour."""
        self.accueil()
        self.js(REGLAGES)
        self.attendre()
        self.js("selectUiLangChoice('%s')" % langue)
        self.page.wait_for_timeout(800)
        self.noter("apres bascule : reglages")
        self.js("history.back()")
        self.page.wait_for_timeout(800)
        self.noter("apres bascule : retour")


def signaler(releve_fr, releve, app, langue=None):
    vu_fr = set()
    for r in releve_fr.values():
        vu_fr.update(r["lignes"])
    trouves = {}
    for chemin, r in releve.items():
        for l in r["lignes"]:
            if l in vu_fr and marqueur(l, app, langue):
                trouves.setdefault(l, []).append(chemin)
    return trouves


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", choices=["de", "es"], required=True)
    ap.add_argument("--langues", help="liste separee par des virgules (defaut : toutes)")
    ap.add_argument("--complet", action="store_true", help="chaque option des panneaux aussi")
    ap.add_argument("--sans-chaud", action="store_true")
    ap.add_argument("--sortie")
    ap.add_argument("--port", type=int, help="pour lancer plusieurs langues en parallele")
    a = ap.parse_args()
    global PORT
    if a.port:
        PORT = a.port
    langues = a.langues.split(",") if a.langues else LANGUES[a.app]
    from playwright.sync_api import sync_playwright
    srv = serveur()
    resultat = {"app": a.app, "langues": {}}
    total = 0
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            print("francais (reference)...")
            s = Session(nav, a.app, "fr")
            s.visiter(ECRANS, complet=a.complet)
            ref = s.releve
            s.ctx.close()
            for lg in langues:
                print(lg + " a froid...")
                s = Session(nav, a.app, lg)
                s.visiter(ECRANS, complet=a.complet)
                froid = signaler(ref, s.releve, a.app, lg)
                erreurs = sorted({e for r in s.releve.values() for e in r["erreurs"]})
                s.ctx.close()
                chaud = {}
                if not a.sans_chaud:
                    print(lg + " a chaud...")
                    s = Session(nav, a.app, "fr")
                    s.visiter(ECRANS, tuiles=False)
                    s.releve = {}
                    s.basculer(lg)
                    s.visiter(ECRANS, prefixe="chaud : ", tuiles=False)
                    chaud = {l: c for l, c in signaler(ref, s.releve, a.app, lg).items() if l not in froid}
                    s.ctx.close()
                resultat["langues"][lg] = {"froid": froid, "chaud": chaud, "erreurs": erreurs}
                total += len(froid) + len(chaud)
                for titre, d in (("A FROID", froid), ("A CHAUD seulement", chaud)):
                    if d:
                        print("  %s, %d ligne(s) :" % (titre, len(d)))
                        for l, c in sorted(d.items(), key=lambda x: -len(x[1])):
                            print("    %-70s  %s%s" % (l[:70], ", ".join(c[:3]), " (+%d)" % (len(c) - 3) if len(c) > 3 else ""))
                if erreurs:
                    print("  erreurs JS : " + " | ".join(erreurs[:5]))
            nav.close()
    finally:
        srv.shutdown()
    if a.sortie:
        with open(a.sortie, "w", encoding="utf-8") as f:
            json.dump(resultat, f, ensure_ascii=False, indent=1)
    print("\n%d ligne(s) francaise(s) hors du francais." % total)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
