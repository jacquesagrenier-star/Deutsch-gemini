# -*- coding: utf-8 -*-
"""Ligne 152 (20 nov. 2026) : les defauts qu'un nouvel utilisateur voit dans sa premiere semaine (revue A a Z, APP.md,
« A corriger avant le 22 ? »), a 360 x 740, interface en francais et en arabe :
  A3  visite guidee, deux premiers ecrans : le toast « C'est note… » ne recouvre plus la barre du bouton ;
  C2  ecran de fin de seance : l'en-tete est celui de la seance, plus le nom de la derniere partie (« Images ») ;
  B6  Premiers pas : l'etiquette « Premiers pas » tient sur une ligne ;
  B4  Premiers pas, tableau « Etre : sein » : ce que la fleche couvre (mesure ; le degrade de la ligne 110 est le
      remede en place, le defilement automatique est decide pour apres le 22) ;
  B5  carte « Tes premiers pas sont faits ! » : « Recommencer… » n'est plus dans la barre flottante ;
  C5  « Tu t'arretes ici » : l'anneau et « Il reste N cartes » comptent la meme seance ;
  C3  l'accueil apres une 2e seance du jour entamee : le libelle du bouton (mesure : le defaut se reproduit-il ?) ;
  B3  « Ta semaine » : pas de « 0 acquis » ; et l'experience de la cause -- cinq mots reussis jour apres jour, l'horloge
      avancee d'un jour a chaque passage : quel jour le compteur « acquis » bouge-t-il ?
  E4  fin d'une conversation : le titre du resultat est visible (page conversation.html).
Navigateur : SOUS LE VERROU du parcours. Derniere ligne : « BILAN OK » ou « BILAN A REVOIR : … ».
    python tests/revue_152.py <racine> <port> <dossier-captures> [<index-avant.html> [<conversation-avant.html>]]
(avec les pages d'avant en 4e et 5e arguments, la sonde montre les defauts : elle ne juge pas, elle mesure)"""
import functools, http.server, io, json, os, sys, threading
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

RACINE, PORT, OUT = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
AVANT = io.open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) > 4 else None
AVANT_CONV = io.open(sys.argv[5], encoding="utf-8").read() if len(sys.argv) > 5 else None
SUF = "-avant" if AVANT else ""
LANGUES = ["fr", "ar"]


class Calme(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def handle(self):
        try:
            super().handle()
        except (ConnectionError, OSError):
            pass


# L'horloge avancee (experience B3) : new Date() et Date.now() ensemble, les minuteries intactes.
HORLOGE = """(() => { const D = Date; let off = 0; window.__avancerJours = j => { off += j * 86400000; };
  class F extends D { constructor(...a){ if(a.length) super(...a); else super(D.now() + off); } static now(){ return D.now() + off; } }
  window.Date = F; })();"""

FAUX_COMPTE = """() => { window.firebaseAuth = window.firebaseAuth || {};
  const u = { uid: 'demo-locale', email: '', displayName: '', isAnonymous: false };
  try{ Object.defineProperty(window.firebaseAuth, 'currentUser', { value: u, configurable: true }); }catch(e){ window.firebaseAuth.currentUser = u; }
  return true; }"""

POSER = """(a) => {
  localStorage.clear();
  const P = 'deutschAI_';
  localStorage.setItem('wortando_langueApprise', 'de');
  localStorage.setItem(P + 'uiLang', a.ui); localStorage.setItem(P + 'setupDone', '1'); localStorage.setItem(P + 'onboardingSeen', '1');
  if(a.niveau) localStorage.setItem(P + 'niveauSeance', a.niveau);
}"""

OUTILS = """() => {
  window.__rect = e => { if(!e || !e.offsetParent && getComputedStyle(e).position !== 'fixed') return null; const b = e.getBoundingClientRect(); return b.width && b.height ? { h: Math.round(b.top), b: Math.round(b.bottom), g: Math.round(b.left), d: Math.round(b.right) } : null; };
  window.__croise = (a, b) => !!(a && b && a.h < b.b && b.h < a.b && a.g < b.d && b.g < a.d);
  window.__pause = ms => new Promise(r => setTimeout(r, ms));
  // passer une carte comme le ferait quelqu'un qui sait : « Continuer » sur un mot presente, sinon retourner et ✓
  window.__passer = async () => {
    const cp = document.getElementById('cartePhrase');
    if(cp && !cp.classList.contains('hidden')){ const b = cp.querySelector('.cp-actions button.primary:not(.hidden)'); if(b){ b.click(); await __pause(900); return 'phrase'; } return 'phrase-sans-suite'; }
    if(document.querySelector('#flashcardActions.presentation')){ motPresenteVu(); await __pause(900); return 'presente'; }
    const f = document.getElementById('flashcard'); if(f && !f.classList.contains('flipped')) flipCard();
    await __pause(150); reviewGood(); await __pause(1500); return 'su';
  };
  return true; }"""

A3 = """async () => {
  await lancerDecouverte();
  let n = 0; while(!(decouverte && decouverte.pret) && n++ < 60) await __pause(250);
  await __pause(600);
  const lire = () => { const toast = document.getElementById('badgeToast'), bas = document.querySelector('.dec-bas');
    const bt = Array.from(document.querySelectorAll('.dec-bas button')).find(b => !b.classList.contains('hidden') && b.offsetParent !== null);
    return { etape: decouverte ? decouverte.etape : null, toast: __rect(toast), barre: __rect(bas), bouton: bt ? (bt.textContent || '').trim().slice(0, 30) : null,
             boutonRect: __rect(bt), surLaBarre: __croise(__rect(toast), __rect(bas)), surLeBouton: __croise(__rect(toast), __rect(bt)),
             visible: !!(toast && toast.classList.contains('show')), texte: toast ? toast.textContent.trim() : '', page: document.documentElement.scrollWidth }; };
  showInfoToast(t('profil_ok_tout')); await __pause(700);
  const e0 = lire();
  allerEtapeDecouverte(1); await __pause(1500);
  showInfoToast(t('profil_ok_tout')); await __pause(700);
  const e1 = lire();
  return [e0, e1];
}"""

# C2 : la seance du jour, amenee a sa derniere carte, puis le retour d'un arret (revenirDeLArret), comme au sortir du theme.
C2 = """async () => {
  await ouvrirSeanceDuJour();
  let n = 0; while(!(currentCards && currentCards.length > 3 && document.getElementById('flashcards').classList.contains('active')) && n++ < 80) await __pause(250);
  await __pause(800);
  const parts = Array.from(document.querySelectorAll('#seancePartsNoms *')).map(x => x.textContent.trim()).filter(Boolean);
  const derniere = currentCards[currentCards.length - 1];
  currentFlashcard = currentCards.length - 1;
  try{ cacherCartePhrase(); }catch(e){}
  revenirDeLArret();
  await __pause(2500);
  const fin = document.getElementById('flashcardEnd');
  return { cartes: currentCards.length, derniereForme: derniere ? (derniere.forme || derniere.mode || '') : '', parties: parts.slice(0, 8),
           finOuverte: !!(fin && !fin.classList.contains('hidden')), finTitre: (document.getElementById('flashEndTitre') || {}).textContent || '',
           kicker: document.getElementById('flashKicker').textContent, titre: document.getElementById('flashThemeTitle').textContent,
           nomSeance: currentTheme ? currentTheme.name : '', page: document.documentElement.scrollWidth };
}"""

# Premiers pas : le tableau de l'etape 1 (B6, B4), puis la carte de fin (B5).
PP_TABLEAU = """async () => {
  try{ const s = lirePremiersPas(); if(s.a === false){ s.a = true; ecrirePremiersPas(s); } }catch(e){}
  await ouvrirPremiersPas();
  let n = 0; while(!(currentCards && currentCards.length > 3 && document.getElementById('flashcards').classList.contains('active')) && n++ < 80) await __pause(250);
  await __pause(600);
  const i = currentCards.findIndex(c => c && c.forme === 'pp_tableau');
  if(i < 0) return { erreur: 'pas de tableau dans la seance', formes: currentCards.slice(0, 12).map(c => c.forme || c.mode) };
  try{ cacherCartePhrase(); }catch(e){}
  currentFlashcard = i; loadFlashcard();
  await __pause(1500);
  scrollTo(0, 0); await __pause(400);
  const cp = document.getElementById('cartePhrase');
  const eti = cp.querySelector('.cp-type b.cp-pp');
  const rond = cp.querySelector('.cp-actions button.primary:not(.hidden)');
  const blocs = Array.from(cp.children).filter(e => e.offsetParent !== null && !e.classList.contains('cp-actions') && !e.classList.contains('cp-retour'));
  const note = blocs[blocs.length - 1];
  const lire = () => ({ note: __rect(note), rond: __rect(rond), rondSurLaNote: __croise(__rect(note), __rect(rond)), degrade: document.body.classList.contains('cp-reste-dessous'),
                        defile: Math.round((document.scrollingElement || document.documentElement).scrollTop), haut: innerHeight });
  const haut = lire();
  const se = document.scrollingElement || document.documentElement; se.scrollTop = se.scrollHeight; await __pause(600);
  const bas = lire();
  scrollTo(0, 0); await __pause(300);
  return { etiquette: eti ? eti.textContent.trim() : null, etiquetteHaut: eti ? Math.round(eti.getBoundingClientRect().height) : null,
           etiquetteLignes: eti ? Math.round(eti.getBoundingClientRect().height / parseFloat(getComputedStyle(eti).lineHeight || 18)) : null,
           noteTexte: note ? note.textContent.trim().slice(0, 60) : '', enHaut: haut, enBas: bas, page: document.documentElement.scrollWidth };
}"""

PP_FIN = """async () => {
  try{ cacherCartePhrase(); }catch(e){}
  const i = currentFlashcard;
  currentCards[i] = { mode: 'phrase', forme: 'pp_fin', pp: true, cible: null, themeId: 'premiers_pas2_de_fin', index: 0, jourPP: 99, phrase: null, word: '' };
  loadFlashcard();
  await __pause(1500);
  scrollTo(0, 0); await __pause(400);
  const cp = document.getElementById('cartePhrase');
  const fixes = Array.from(cp.querySelectorAll('.cp-actions button')).filter(b => !b.classList.contains('hidden') && b.offsetParent !== null || getComputedStyle(b).position === 'fixed');
  const visibles = Array.from(cp.querySelectorAll('.cp-actions button')).filter(b => !b.classList.contains('hidden') && __rect(b));
  const suite = cp.querySelector('.av-suite');
  const reco = Array.from(cp.querySelectorAll('button.secondary')).find(b => __rect(b));
  const lire = () => ({ suite: __rect(suite), boutonsDuBas: visibles.map(b => ({ t: (b.textContent || '').trim().slice(0, 28), r: __rect(b), surLaSuite: __croise(__rect(b), __rect(suite)) })),
                        recommencer: reco ? { dansLaBarre: !!reco.closest('.cp-actions'), r: __rect(reco) } : null,
                        defile: Math.round((document.scrollingElement || document.documentElement).scrollTop) });
  const haut = lire();
  const se = document.scrollingElement || document.documentElement; se.scrollTop = se.scrollHeight; await __pause(600);
  const bas = lire();
  scrollTo(0, 0); await __pause(300);
  return { titre: (cp.querySelector('.cp-fete-pp h2') || {}).textContent || '', aLaSuite: !!suite, enHaut: haut, enBas: bas, page: document.documentElement.scrollWidth };
}"""

# C5 : six cartes passees, puis « ‹ » : l'anneau et la ligne « Il reste… ».
C5 = """async () => {
  await ouvrirSeanceDuJour();
  let n = 0; while(!(currentCards && currentCards.length > 3 && document.getElementById('flashcards').classList.contains('active')) && n++ < 80) await __pause(250);
  await __pause(800);
  const depart = currentCards.length, gestes = [];
  for(let k = 0; k < 6; k++){ gestes.push(await __passer()); }
  const s = seanceCourante();
  handleFlashcardBack();
  await __pause(900);
  const fc = document.getElementById('finCourte');
  const an = document.getElementById('finCourteAnneau');
  const chiffres = x => (String(x || '').match(/\\d+/g) || []).map(Number);
  const reste = (document.getElementById('finCourteReste') || {}).textContent || '';
  return { gestes: gestes, paquetAuDepart: depart, paquetMaintenant: currentCards.length, rang: currentFlashcard, suivie: s ? { n: s.n, p: s.p } : null,
           ouverte: !!(fc && !fc.classList.contains('hidden')), anneau: an ? (an.querySelector('b').textContent + ' ' + an.querySelector('small').textContent) : '',
           anneauChiffres: an ? chiffres(an.querySelector('b').textContent + ' ' + an.querySelector('small').textContent) : [],
           resume: (document.getElementById('finCourteResume') || {}).textContent || '', reste: reste, resteChiffres: chiffres(reste), page: document.documentElement.scrollWidth };
}"""

# C3 : une seance finie, « Encore une seance », trois cartes, « ‹ », « Revenir a l'accueil » : que dit le bouton ?
C3 = """async () => {
  const lireAccueil = () => ({ etat: (typeof etatSeanceAccueil === 'function') ? etatSeanceAccueil() : null, bouton: (document.getElementById('spPlayTxt') || {}).textContent || '',
                              plan: ((document.querySelector('#seancePilule .pa-contenu') || {}).textContent || '').trim(), finies: seancesFiniesAujourdhui(),
                              seances: lireSeances().filter(x => x && x.d).slice(-3).map(x => ({ n: x.n, p: x.p, f: x.f })) });
  // 1re seance : on la reprend la ou C5 l'a laissee, et on la mene a sa fin.
  try{ reprendreSeanceCourte(); }catch(e){}
  await __pause(500);
  try{ cacherCartePhrase(); }catch(e){}
  currentFlashcard = currentCards.length - 1;
  nextFlashcard();
  await __pause(2500);
  const fin1 = !!(document.getElementById('flashcardEnd') && !document.getElementById('flashcardEnd').classList.contains('hidden'));
  goHome(); await __pause(1200);
  const apres1 = lireAccueil();
  // « Encore une seance » : le bouton de la carte de l'accueil.
  entrerSeanceDuJour();
  let n = 0; while(!(document.getElementById('flashcards').classList.contains('active') && currentCards && currentCards.length > 3) && n++ < 80) await __pause(250);
  await __pause(900);
  const bilan = document.querySelector('.bilan-voile, .bilan-carte'); if(bilan){ try{ fermerBilanSemaine(); }catch(e){} await __pause(400); }
  const gestes = []; for(let k = 0; k < 3; k++) gestes.push(await __passer());
  const pendant = { cartes: currentCards.length, rang: currentFlashcard, kicker: document.getElementById('flashKicker').textContent };
  handleFlashcardBack(); await __pause(900);
  const court = !!(document.getElementById('finCourte') && !document.getElementById('finCourte').classList.contains('hidden'));
  if(court){ quitterSeanceCourte(); await __pause(1200); }
  const ecran = (document.querySelector('.screen.active') || {}).id;
  return { fin1: fin1, apres1: apres1, gestes: gestes, pendant: pendant, ecranCourt: court, ecran: ecran, apres2: lireAccueil() };
}"""

# B3, l'affichage : « Ta semaine » avec un compte ou rien n'est acquis.
B3_VUE = """async () => {
  // l'ecran d'ouverture attend la connexion, que la sonde n'a pas : on l'ote pour voir la fenetre
  try{ const sp = document.getElementById('splashOuverture'); if(sp) sp.remove(); showScreen('home'); }catch(e){}
  const b = calculerBilan();
  ouvrirBilanSemaine();
  await __pause(900);
  const carte = document.querySelector('.bilan-chiffres');
  const cases = carte ? Array.from(carte.querySelectorAll('.bilan-chiffre')).map(c => c.textContent.replace(/\\s+/g, ' ').trim()) : [];
  const larg = carte ? Array.from(carte.querySelectorAll('.bilan-chiffre')).map(c => Math.round(c.getBoundingClientRect().width)) : [];
  const r = { calcul: { exercices: b.exercices, jours: b.jours, acquis: b.acquis }, cases: cases, largeurs: larg, boite: carte ? Math.round(carte.getBoundingClientRect().width) : 0,
              page: document.documentElement.scrollWidth };
  return r;
}"""

# B3, la cause : cinq mots du niveau, reussis chaque jour par le vrai chemin (retourner, ✓), l'horloge avancee d'un jour.
B3_JOUR = """async (jour) => {
  if(!window.__mots){
    let n = 0; while(!(typeof paquetSeanceDuNiveau === 'function' && paquetSeanceDuNiveau('A2').length > 0) && n++ < 120) await __pause(250);
    window.__mots = paquetSeanceDuNiveau('A2').filter(x => x && x.mode !== 'phrase' && x.themeId !== undefined).slice(0, 5);
  }
  const mots = window.__mots;
  // le paquet, comme montrerCartesDecouverte() l'installe
  currentCardsFull = mots.slice(); currentCards = mots.slice(); currentFlashcard = 0;
  currentTheme = { id: 'essai_b3', name: 'essai' }; retourSeanceAccueil = true; panneauAvantFlashcards = null; flashcardFromSearch = false;
  flashcardMode = mots[0].mode || 'nomen'; sessionVues = 0; sessionSues = 0;
  try{ hideFlashcardEnd(); }catch(e){}
  showScreen('flashcards'); loadFlashcard();
  await __pause(700);
  const gestes = [];
  for(let k = 0; k < 14 && currentFlashcard < currentCards.length && !paquetTermine(); k++){ gestes.push(await __passer()); }
  const etats = mots.map(m => { const st = getWordState(m.themeId, m.index); return (st.srsHits || 0) + (st.mastered ? 'M' : ''); });
  let journal = 0; try{ journal = (JSON.parse(localStorage.getItem(directionScopedKey(MASTERY_LOG_KEY)) || '[]') || []).length; }catch(e){}
  const r = { jour: jour, gestes: gestes.join(','), points: etats.join(' '), journal: journal, acquis: calculerBilan().acquis };
  try{ goHome(); }catch(e){}
  await __pause(500);
  window.__avancerJours(1);
  return r;
}"""

E4 = """async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  document.querySelector('button.gros').click();
  let fini = false;
  for(let k = 0; k < 40 && !fini; k++){
    let n = 0;
    while(n++ < 150){ const z = document.querySelector('.repondre'); if(document.querySelector('.carte.fin')){ fini = true; break; } if(z && !z.hidden && z.querySelector('.choix button')) break; await pause(400); }
    if(fini) break;
    const cs = choixDe(noeud); const j = cs.findIndex(c => !c.faux && !c.repete);
    document.querySelectorAll('.repondre .choix button')[Math.max(0, j)].click();
    await pause(700);
  }
  await pause(1500);
  const carte = document.querySelector('.carte.fin'), fil = document.querySelector('.fil');
  if(!carte) return { erreur: 'pas d ecran de fin' };
  const titre = carte.querySelector('h2'), f = fil.getBoundingClientRect(), tr = titre.getBoundingClientRect();
  const boutons = Array.from(carte.querySelectorAll('button.gros')).map(b => { const r = b.getBoundingClientRect(); return { t: b.textContent.trim().slice(0, 26), visible: r.top >= f.top - 1 && r.bottom <= f.bottom + 1 }; });
  return { titre: titre.textContent.trim(), titreHaut: Math.round(tr.top), titreBas: Math.round(tr.bottom), filHaut: Math.round(f.top), filBas: Math.round(f.bottom),
           titreVisible: tr.top >= f.top - 1 && tr.bottom <= f.bottom + 1, carteHaute: Math.round(carte.getBoundingClientRect().height), filHauteur: Math.round(f.height),
           defile: Math.round(fil.scrollTop), boutons: boutons, page: document.documentElement.scrollWidth };
}"""


def main():
    os.makedirs(OUT, exist_ok=True)
    http.server.ThreadingHTTPServer.allow_reuse_address = False
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Calme, directory=RACINE))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    bilan = []

    def voir(nom, vrai, detail=""):
        print("    %-74s %s%s" % (nom, "ok" if vrai else "NON", (" -- " + detail) if detail and not vrai else ""), flush=True)
        if not vrai and not AVANT:
            bilan.append(nom + (" (" + detail + ")" if detail else ""))

    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()

            def ouvrir(ui, niveau, horloge=False):
                ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 740}, device_scale_factor=2, service_workers="block", has_touch=True, is_mobile=True)
                for motif in ("**/*firebase*", "**/*gstatic*", "**/*googleapis*", "**/*recaptcha*"):
                    ctx.route(motif, lambda r: r.abort())
                if AVANT:
                    ctx.route("**/index.html*", lambda r: r.fulfill(body=AVANT, content_type="text/html; charset=utf-8"))
                if horloge:
                    ctx.add_init_script(HORLOGE)
                page = ctx.new_page()
                page.erreurs = []
                page.on("pageerror", lambda e: page.erreurs.append(str(e).splitlines()[0][:140] if str(e) else ""))
                page.on("dialog", lambda d: d.dismiss())
                page.goto("http://127.0.0.1:%d/index.html" % PORT, wait_until="domcontentloaded")
                page.wait_for_timeout(2500)
                page.evaluate(POSER, {"ui": ui, "niveau": niveau})
                page.reload(wait_until="domcontentloaded"); page.wait_for_timeout(4500)
                page.evaluate(FAUX_COMPTE); page.evaluate(OUTILS)
                return ctx, page

            def essai(nom, f):
                try:
                    return f()
                except Exception as e:
                    print("    %s : la sonde a echoue (%s)" % (nom, str(e).splitlines()[0][:160]), flush=True)
                    if not AVANT:
                        bilan.append("%s : sonde en echec" % nom)
                    return None

            for ui in LANGUES:
                print("===== interface %s%s" % (ui, " (AVANT)" if AVANT else ""), flush=True)

                # ---- A3 : la visite
                ctx, page = ouvrir(ui, "A1")
                r = essai("A3", lambda: page.evaluate(A3))
                if r:
                    for e in r:
                        print("  A3 etape %s : toast %s, barre %s, bouton « %s »" % (e["etape"], e["toast"], e["barre"], e["bouton"]))
                        voir("A3 %s etape %s : le toast est visible et ne touche ni la barre ni le bouton" % (ui, e["etape"]),
                             e["visible"] and not e["surLaBarre"] and not e["surLeBouton"], "sur la barre %s, sur le bouton %s" % (e["surLaBarre"], e["surLeBouton"]))
                        voir("A3 %s etape %s : la page tient en 360 px" % (ui, e["etape"]), e["page"] <= 360, "%s px" % e["page"])
                    page.screenshot(path=os.path.join(OUT, "A3-%s%s.png" % (ui, SUF)))
                ctx.close()

                # ---- Premiers pas : B6, B4, B5
                ctx, page = ouvrir(ui, "A1")
                r = essai("B6/B4", lambda: page.evaluate(PP_TABLEAU))
                if r and not r.get("erreur"):
                    print("  B6 : etiquette « %s », %s px de haut ; B4 : note « %s… », en haut %s, en bas %s" % (r["etiquette"], r["etiquetteHaut"], r["noteTexte"][:34], r["enHaut"], r["enBas"]))
                    voir("B6 %s : « %s » tient sur une ligne" % (ui, r["etiquette"]), (r["etiquetteHaut"] or 99) <= 30, "%s px de haut" % r["etiquetteHaut"])
                    voir("B4 %s : tant que la fleche couvre la note, le degrade le signale" % ui, (not r["enHaut"]["rondSurLaNote"]) or r["enHaut"]["degrade"])
                    voir("B4 %s : la page defilee jusqu'en bas, la fleche ne couvre plus la note" % ui, not r["enBas"]["rondSurLaNote"])
                    voir("B6/B4 %s : la page tient en 360 px" % ui, r["page"] <= 360, "%s px" % r["page"])
                    page.screenshot(path=os.path.join(OUT, "B4-B6-%s%s.png" % (ui, SUF)))
                elif r:
                    print("  B6/B4 :", r)
                    voir("B6/B4 %s : le tableau de Premiers pas s'ouvre" % ui, False, str(r)[:120])
                r = essai("B5", lambda: page.evaluate(PP_FIN))
                if r:
                    print("  B5 : « %s », bloc La suite %s ; en haut %s" % (r["titre"], r["aLaSuite"], json.dumps(r["enHaut"], ensure_ascii=False)[:420]))
                    bas = r["enHaut"]["boutonsDuBas"]
                    voir("B5 %s : un seul bouton dans la barre flottante" % ui, len(bas) == 1, "%d boutons : %s" % (len(bas), [b["t"] for b in bas]))
                    reco = r["enHaut"]["recommencer"]
                    voir("B5 %s : « Recommencer… » est dans la carte, pas dans la barre" % ui, bool(reco) and not reco["dansLaBarre"])
                    voir("B5 %s : la page defilee, rien ne couvre plus « La suite »" % ui, not any(b["surLaSuite"] for b in r["enBas"]["boutonsDuBas"]))
                    voir("B5 %s : la page tient en 360 px" % ui, r["page"] <= 360, "%s px" % r["page"])
                    page.screenshot(path=os.path.join(OUT, "B5-%s%s.png" % (ui, SUF)))
                    page.evaluate("() => { const se = document.scrollingElement || document.documentElement; se.scrollTop = se.scrollHeight; }")
                    page.wait_for_timeout(500)
                    page.screenshot(path=os.path.join(OUT, "B5-bas-%s%s.png" % (ui, SUF)))
                ctx.close()

                # ---- C2 : la fin de seance
                ctx, page = ouvrir(ui, "A2")
                r = essai("C2", lambda: page.evaluate(C2))
                if r:
                    print("  C2 : %d cartes, derniere « %s », parties %s ; fin ouverte %s « %s » ; en-tete « %s » / « %s »"
                          % (r["cartes"], r["derniereForme"], r["parties"], r["finOuverte"], r["finTitre"], r["kicker"], r["titre"]))
                    voir("C2 %s : l'ecran de fin est ouvert" % ui, r["finOuverte"])
                    voir("C2 %s : le titre de l'en-tete est celui de la seance (« %s »)" % (ui, r["nomSeance"]), r["titre"] == r["nomSeance"], "« %s »" % r["titre"])
                    voir("C2 %s : le titre n'est pas le nom d'une partie" % ui, r["titre"] not in r["parties"], "« %s »" % r["titre"])
                    voir("C2 %s : la page tient en 360 px" % ui, r["page"] <= 360, "%s px" % r["page"])
                    page.screenshot(path=os.path.join(OUT, "C2-%s%s.png" % (ui, SUF)))
                ctx.close()

                # ---- C5 puis C3 : la seance quittee au milieu
                ctx, page = ouvrir(ui, "A2")
                r = essai("C5", lambda: page.evaluate(C5))
                if r:
                    print("  C5 : gestes %s ; paquet %d -> %d, rang %d, seance suivie %s ; anneau « %s », « %s », « %s »"
                          % (r["gestes"], r["paquetAuDepart"], r["paquetMaintenant"], r["rang"], r["suivie"], r["anneau"], r["resume"], r["reste"]))
                    a, re_ = r["anneauChiffres"], r["resteChiffres"]
                    voir("C5 %s : l'ecran « Tu t'arretes ici » est ouvert" % ui, r["ouverte"])
                    voir("C5 %s : l'anneau et « Il reste » comptent la meme seance (fait + reste = total)" % ui,
                         len(a) == 2 and len(re_) >= 1 and a[0] + re_[0] == a[1], "anneau %s, reste %s" % (a, re_))
                    voir("C5 %s : la page tient en 360 px" % ui, r["page"] <= 360, "%s px" % r["page"])
                    page.screenshot(path=os.path.join(OUT, "C5-%s%s.png" % (ui, SUF)))
                r = essai("C3", lambda: page.evaluate(C3))
                if r:
                    print("  C3 : 1re seance finie %s -> accueil %s ; 2e seance %s, gestes %s, ecran court %s ; puis accueil (%s) %s"
                          % (r["fin1"], json.dumps(r["apres1"], ensure_ascii=False)[:200], r["pendant"], r["gestes"], r["ecranCourt"], r["ecran"], json.dumps(r["apres2"], ensure_ascii=False)[:260]))
                    voir("C3 %s : apres la 1re seance, l'accueil la dit faite" % ui, r["apres1"]["etat"] == "faite", str(r["apres1"]["etat"]))
                    voir("C3 %s : la 2e seance entamee, l'accueil propose de la continuer" % ui, r["apres2"]["etat"] == "entamee", "etat %s, bouton « %s »" % (r["apres2"]["etat"], r["apres2"]["bouton"]))
                    page.screenshot(path=os.path.join(OUT, "C3-%s%s.png" % (ui, SUF)))
                ctx.close()

                # ---- B3 : l'affichage
                ctx, page = ouvrir(ui, "A2")
                r = essai("B3", lambda: page.evaluate(B3_VUE))
                if r:
                    print("  B3 : calcul %s ; cases %s ; largeurs %s dans %s px" % (r["calcul"], r["cases"], r["largeurs"], r["boite"]))
                    voir("B3 %s : rien d'acquis, donc pas de case « 0 »" % ui, r["calcul"]["acquis"] == 0 and len(r["cases"]) == 2, "%d cases : %s" % (len(r["cases"]), r["cases"]))
                    voir("B3 %s : les cases remplissent la ligne" % ui, bool(r["largeurs"]) and abs(sum(r["largeurs"]) + 8 * (len(r["largeurs"]) - 1) - r["boite"]) <= 4, "%s dans %s" % (r["largeurs"], r["boite"]))
                    voir("B3 %s : la page tient en 360 px" % ui, r["page"] <= 360, "%s px" % r["page"])
                    page.screenshot(path=os.path.join(OUT, "B3-%s%s.png" % (ui, SUF)))
                ctx.close()

                # ---- E4 : la fin d'une conversation (de, puis es)
                for apprise in ("de", "es"):
                    ctx = nav.new_context(locale="fr-FR", viewport={"width": 360, "height": 740}, device_scale_factor=2, service_workers="block")
                    if AVANT_CONV:
                        ctx.route("**/conversation.html*", lambda r: r.fulfill(body=AVANT_CONV, content_type="text/html; charset=utf-8"))
                    page = ctx.new_page()
                    page.goto("http://127.0.0.1:%d/visuel/prototype/conversation.html?c=pp1-pass&apprendre=%s&lang=%s" % (PORT, apprise, ui), wait_until="domcontentloaded")
                    try:
                        page.wait_for_selector("button.gros", timeout=30000)
                        r = essai("E4", lambda: page.evaluate(E4))
                    except Exception as e:
                        r = None; print("    E4 %s/%s : la conversation ne s'ouvre pas" % (apprise, ui))
                    if r and not r.get("erreur"):
                        print("  E4 %s : « %s » de %d a %d px, fil de %d a %d ; carte %d px pour %d ; boutons %s" % (apprise, r["titre"], r["titreHaut"], r["titreBas"], r["filHaut"], r["filBas"], r["carteHaute"], r["filHauteur"], r["boutons"]))
                        voir("E4 %s/%s : le titre du resultat est entierement visible" % (apprise, ui), r["titreVisible"], "titre %d-%d, fil %d-%d" % (r["titreHaut"], r["titreBas"], r["filHaut"], r["filBas"]))
                        voir("E4 %s/%s : les boutons de fin sont a l'ecran aussi" % (apprise, ui), all(b["visible"] for b in r["boutons"]) or r["carteHaute"] > r["filHauteur"],
                             "%s ; carte %d px, fil %d px" % ([b["t"] for b in r["boutons"] if not b["visible"]], r["carteHaute"], r["filHauteur"]))
                        voir("E4 %s/%s : la page tient en 360 px" % (apprise, ui), r["page"] <= 360, "%s px" % r["page"])
                        page.screenshot(path=os.path.join(OUT, "E4-%s-%s%s.png" % (apprise, ui, SUF)))
                    elif r:
                        voir("E4 %s/%s : la conversation arrive a son ecran de fin" % (apprise, ui), False)
                    ctx.close()

            # ---- B3, la cause : l'experience des cinq mots (une fois, en francais ; le code est le meme avant et apres)
            if not AVANT:
                print("===== B3, la cause : cinq mots reussis chaque jour, l'horloge avancee d'un jour a chaque passage", flush=True)
                ctx, page = ouvrir("fr", "A2", horloge=True)
                premier = None
                for jour in range(7):
                    r = essai("B3-cause", lambda: page.evaluate(B3_JOUR, jour))
                    if not r:
                        break
                    print("  jour %d : gestes %s ; points des cinq mots : %s ; journal de maitrise %d ; « acquis » %d" % (r["jour"], r["gestes"], r["points"], r["journal"], r["acquis"]), flush=True)
                    if premier is None and r["acquis"] > 0:
                        premier = r["jour"]
                print("  -> le compteur « acquis » bouge pour la premiere fois au jour %s (jour 0 = le jour ou le mot est appris)" % premier)
                voir("B3 cause : un mot reussi a chaque echeance finit par compter dans « acquis »", premier is not None)
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    if AVANT:
        print("MESURE D'AVANT : pas de bilan")
    else:
        print("BILAN OK" if not bilan else "BILAN A REVOIR : " + " | ".join(bilan))


if __name__ == "__main__":
    main()
