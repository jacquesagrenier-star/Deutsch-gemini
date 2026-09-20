# -*- coding: utf-8 -*-
"""LE BANC DE TOURNAGE -- il pilote l'app et en rapporte des images et des clips.

    python video/banc.py --liste
    python video/banc.py --photos                        toutes les scenes, en images
    python video/banc.py --photos --langue tr            les memes, en turc
    python video/banc.py --clips --scene tableau         une scene, en video
    python video/banc.py --photos --appareil iphone67    au format demande par l'App Store

POURQUOI UN PROGRAMME PLUTOT QU'UN ENREGISTREMENT A LA MAIN. L'app a change
sept fois le 20 septembre 2026, dans la meme journee. Toute capture filmee a la
main est perimee avant d'avoir servi, et refaire six langues a la main ne se
fait pas deux fois. Ici, une evolution de l'app coute UNE RELANCE : les plans
reviennent a jour en minutes, dans les six langues, et les memes scenes donnent
les captures obligatoires de l'App Store.

CE QU'IL FAUT AVOIR
    pip install playwright && python -m playwright install chromium
    ffmpeg dans le PATH (deja la, les scripts de montage s'en servent)

⚠️ IL NE SE CONNECTE A AUCUN COMPTE, ET C'EST VOULU. L'app exige une
authentification (AUTH_REQUIRED), mais un banc de tournage qui porte un mot de
passe finit par le porter dans un depot public. Il pose donc l'etat a la main
dans localStorage et montre l'ecran voulu -- ce que l'app fait elle-meme une
fois connectee. Les ecritures Firestore echouent alors en silence, sans rien
casser a l'image : c'est exactement ce qu'on veut d'un banc.

⚠️ LE SERVICE WORKER EST BLOQUE (service_workers="block"). Il sert index.html
depuis son cache : sans ce blocage, le banc filmerait la version d'avant-hier
sans qu'aucune erreur ne le dise. Vu le 20 septembre, sur ce banc meme -- la
page servie etait la v630 alors que le fichier sur le disque etait la v632.

⚠️ LES DONNEES VIENNENT DE GITHUB, PAS DU DISQUE. themes.json, verbe.json et
les tableaux sont charges depuis raw.githubusercontent au moment ou l'app en a
besoin : le banc a donc besoin du reseau, et une scene qui montre des mots
montre CE QUI EST EN LIGNE, pas ce qui est en cours de modification ici.
"""
import argparse
import functools
import time
import http.server
import socketserver
import shutil
import subprocess
import sys
import threading
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "video" / "demo"

# 430x932 @3 = 1290x2796, la taille 6,7 pouces demandee par App Store Connect ;
# 414x896 @3 = 1242x2688, la 6,5 pouces. Les tailles exigees changent avec les
# modeles : a verifier dans App Store Connect au moment de la soumission, pas
# de memoire.
# ⚠️ `reduced_motion` ETEINT L'ECRAN D'OUVERTURE, et ce n'est pas un bricolage :
# le logo anime du demarrage dure 4,1 s et l'app le masque deja pour qui demande
# moins d'animation (`prefers-reduced-motion`). Le banc se declare donc tel quel
# plutot que d'attendre une animation au chronometre -- une attente reglee a la
# main filme le logo le jour ou la machine est lente. Vu au banc : la premiere
# photo prise apres un rechargement ne montrait que le W sur fond creme.
APPAREILS = {
    "iphone67": {"viewport": {"width": 430, "height": 932}, "device_scale_factor": 3,
                 "is_mobile": True, "has_touch": True, "reduced_motion": "reduce"},
    "iphone65": {"viewport": {"width": 414, "height": 896}, "device_scale_factor": 3,
                 "is_mobile": True, "has_touch": True, "reduced_motion": "reduce"},
    "web": {"viewport": {"width": 1280, "height": 800}, "device_scale_factor": 2,
            "is_mobile": False, "has_touch": False, "reduced_motion": "reduce"},
    # ⚠️ POUR LES CLIPS, ET SEULEMENT POUR EUX. Playwright FILME LA PAGE A SA
    # TAILLE CSS : il ignore device_scale_factor, qui ne sert qu'aux captures.
    # Un clip tourne en 430 de large doit donc etre agrandi 2,5 fois pour
    # atteindre 1080, et le texte en sort mou. En 720, l'agrandissement tombe a
    # 1,5.
    # ⚠️ 720 ET PAS 1080 : au-dela de 768 px, l'app passe a sa mise en page
    # large et ce n'est plus un telephone qu'on filme. La limite du produit
    # commande le format du tournage, pas l'inverse.
    "clip720": {"viewport": {"width": 720, "height": 1560}, "device_scale_factor": 1,
                "is_mobile": True, "has_touch": True, "reduced_motion": "reduce"},
}

LANGUES = ["fr", "en", "tr", "uk", "fa", "ar"]


# ============ LE SERVEUR ============
def servir():
    """Sert le depot sur un port libre. Rendu : (port, arret)."""
    gestionnaire = functools.partial(http.server.SimpleHTTPRequestHandler,
                                     directory=str(RACINE))
    # Sans allow_reuse_address, deux tournages qui se suivent trop vite se
    # disputent le port -- et le second echoue sur une erreur qui n'a rien a
    # voir avec ce qu'on filme.
    socketserver.TCPServer.allow_reuse_address = True
    serveur = socketserver.TCPServer(("127.0.0.1", 0), gestionnaire)
    serveur.RequestHandlerClass.log_message = lambda *a, **k: None
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    return serveur.server_address[1], serveur.shutdown


# ============ LE PILOTE ============
class Pilote:
    """Le vocabulaire d'une scene. Tout ce qu'une scene sait faire est ici."""

    def __init__(self, page, dossier, nom_scene, depart=None):
        self.page = page
        self.dossier = dossier
        self.scene = nom_scene
        self.prise = 0
        # ⚠️ PLAYWRIGHT ENREGISTRE TOUT LE CONTEXTE, du premier octet a la
        # fermeture : la video brute contient l'ecran d'ouverture, la pose de
        # l'etat, le rechargement, les ecrans qu'on traverse. Filmer utile
        # demande donc de savoir QUAND le mouvement commence. C'est ce que ces
        # deux marques notent, en secondes depuis la creation du contexte ; la
        # coupe se fait apres, quand le fichier existe.
        self.depart = depart
        self.top = None
        self.fin = None

    def moteur(self):
        """Ici commence ce qu'on garde."""
        self.top = time.monotonic() - self.depart if self.depart else None

    def coupez(self):
        """Ici finit ce qu'on garde."""
        self.fin = time.monotonic() - self.depart if self.depart else None

    # ---- amener l'app dans un etat ----
    def js(self, code):
        """Evalue du JS dans la page. Le corps est enveloppe dans une fonction
        asynchrone : `await` y marche, et la derniere expression est rendue."""
        return self.page.evaluate("async () => { " + code + " }")

    def attendre(self, secondes):
        self.page.wait_for_timeout(int(secondes * 1000))

    def langue(self, code):
        # setUiLang() range la preference ; applyUiLang() repeint le DOM. Les
        # deux, parce que setUiLang seul ne retouche pas une page deja ouverte
        # -- constate au banc, et c'est vrai des libelles d'origine aussi.
        self.js("setUiLang('%s'); if(typeof applyUiLang === 'function') applyUiLang();" % code)
        self.attendre(0.4)

    def ecran(self, identifiant):
        """Pose un decor : montre un ecran, sans rien declencher d'autre.

        ⚠️ ON MANIPULE `.screen.active` A LA MAIN, ET CE N'EST PAS PARCE QUE
        showScreen() REFUSERAIT -- il n'a aucune garde d'authentification, je
        l'ai ecrit ici pendant deux versions et c'etait faux. La raison est
        qu'il fait DAVANTAGE : il ferme le panneau d'information, retient
        l'ecran d'ou l'on vient pour le formulaire de retour, declenche le
        chargement du cours. Pour poser un decor, on ne veut que le changement
        d'ecran. Les scenes qui filment un PARCOURS, elles, appellent les vraies
        fonctions de l'app -- ouvrirSeanceDuJour(), ouvrirEcouteMenu() -- parce
        que la fidelite compte plus que la sobriete des que ca bouge."""
        self.js("""
            document.querySelectorAll('.screen.active').forEach(s => s.classList.remove('active'));
            const e = document.getElementById(%r);
            if(!e) throw new Error('ecran inconnu : %s');
            e.classList.add('active');
            e.classList.remove('hidden');
        """ % (identifiant, identifiant))
        self.attendre(0.3)

    def mosaique(self, rang=1, carreaux=0, gagnees=None, trophee=0):
        """Pose l'etat du tableau : quel tableau, ou il en est, lesquels sont
        gagnes, combien de jours de trophee restent."""
        self.js("""
            localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(
                {r: %d, c: %d, j: "", n: 0, g: %s, t: %d, tj: ""}));
            if(typeof majMosaiqueAccueil === 'function') majMosaiqueAccueil();
        """ % (rang, carreaux, list(gagnees or []), trophee))
        self.attendre(1.2)

    def vie(self, maitrises=0, serie=0, seance=0):
        """Donne a l'ecran une vie deja commencee : des mots sus, une serie, une
        seance en cours.

        ⚠️ UN COMPTE NEUF EST LA PIRE VITRINE. « 0 / 860 » et « 0 / 30 » disent
        « personne ne s'en sert » -- c'est ce que rapportait le banc a sa
        premiere prise, et c'est exactement l'image qu'il ne faut pas envoyer a
        l'App Store.
        ⚠️ ON PASSE PAR setWordState(), JAMAIS PAR localStorage EN DUR. La forme
        d'un etat de mot ({mastered, due, reviews}), la cle du paquet et le
        prefixe de direction sont des details de l'app : les recopier ici, c'est
        signer un banc qui filmera un ecran vide le jour ou l'un des trois
        change, sans rien dire."""
        self.js("""
            // Les themes arrivent de GitHub : on attend qu'ils soient la plutot
            // que de supposer un delai.
            for(let i = 0; i < 100 && (!themes || !themes.length); i++)
                await new Promise(r => setTimeout(r, 100));
            // ⚠️ ON PASSE PAR LES PAQUETS DE getProgress(), PAS PAR themes[].mots.
            // Un theme charge ne porte PAS ses mots a ce niveau : « familie » est
            // un theme, mais les mots vivent dans « familie_a1 », « familie_a2 »...
            // La premiere version du banc bouclait sur `t.mots`, toujours vide :
            // elle ne marquait rien, ne levait aucune erreur, et rendait un
            // ecran a « 0 / 860 » -- exactement l'image qu'elle devait eviter.
            const paquets = getProgress();
            let reste = %d;
            for(const cle of Object.keys(paquets)){
                if(reste <= 0) break;
                if(cle === '__migrations' || !/_a1$/.test(cle)) continue;
                for(const i of Object.keys(paquets[cle] || {})){
                    if(reste <= 0) break;
                    paquets[cle][i] = { mastered: true, due: Date.now() + 86400000, reviews: 3 };
                    reste--;
                }
            }
            saveProgress(paquets);
            // saveProgress() differe l'ecriture ; le banc ferme la page bien
            // avant le delai. On pose sur le disque tout de suite.
            if(typeof ecrireProgressionMaintenant === 'function') ecrireProgressionMaintenant();
            const jour = getTodayStr();
            if(%d) localStorage.setItem(directionScopedKey(STREAK_KEY),
                    JSON.stringify({ count: %d, date: jour }));
            if(%d) localStorage.setItem(directionScopedKey(DAILY_ACTIVITY_KEY),
                    JSON.stringify({ count: %d, date: jour }));
            // ⚠️ L'APP DEVERROUILLE LES BADGES A CHAQUE REUSSITE, pas au
            // chargement : sans cet appel, le banc filme quelqu'un qui a douze
            // jours de serie ET un badge << 3 jours de suite >> toujours
            // verrouille -- un etat qui n'existe sur l'appareil de personne.
            if(typeof checkAndUnlockBadges === 'function') checkAndUnlockBadges();
            if(typeof updateGlobalProgress === 'function') updateGlobalProgress();
        """ % (maitrises, serie, serie, seance, seance))
        self.attendre(1.0)

    def sequence(self, nom, n):
        """Une prise IMAGE PAR IMAGE, a la resolution des captures.

        ⚠️ POURQUOI PAS LA VIDEO. Playwright filme la page a sa taille CSS :
        430 px de large pour un telephone, qu'il faut ensuite agrandir 2,5 fois.
        Elargir la fenetre a 720 rend le texte net mais change la MISE EN PAGE
        -- l'app s'y etale, le contenu devient court, et il reste un tiers
        d'ecran blanc en bas. Essaye au banc le 20 septembre : plus net, moins
        cadre. On ne filme donc pas ce plan, on le PHOTOGRAPHIE, une image a la
        fois, en 1290 x 2796.
        ⚠️ CA NE MARCHE QUE POUR UN MOUVEMENT QU'ON PILOTE. Une transition CSS
        de 0,55 s ne s'arrete pas pour poser : la carte qui tourne reste filmee.
        Ici, chaque etat de la mosaique est pose par nous, donc chaque image est
        exacte."""
        dossier = self.dossier / "sequences" / nom
        dossier.mkdir(parents=True, exist_ok=True)
        for f in dossier.glob("*.png"):
            f.unlink()
        return dossier

    def recharger(self):
        """Relit l'app depuis l'etat pose.

        ⚠️ C'EST LA SEULE FACON HONNETE DE RAFRAICHIR. L'accueil est peint par
        une demi-douzaine de fonctions -- l'anneau du niveau, la colonne de la
        serie, l'objectif du jour, la mosaique -- et les rappeler une a une,
        c'est tenir a jour une liste qui vieillit a chaque version de l'app. Le
        banc a filme deux fois un ecran a << 0 / 860 >> alors que la progression
        etait bien posee : les chiffres etaient justes DANS localStorage et
        faux A L'ECRAN. Un rechargement fait exactement ce que fait le telephone
        de quelqu'un au reveil."""
        self.page.reload(wait_until="load")
        self.page.wait_for_function("typeof majMosaiqueAccueil === 'function'", timeout=30000)
        self.attendre(1.5)
        # ⚠️ REPEINDRE CE QUE SEUL openSettings() PEINT. La grille des badges
        # n'est dessinee que la, et openSettings() sort immediatement quand
        # personne n'est connecte : sans cet appel, la carte Badges est VIDE sur
        # toutes les captures des reglages -- ce qui se lit comme une carte
        # cassee alors que rien ne l'est.
        # ⚠️ POSE DANS vie(), L'APPEL ETAIT PERDU : le rechargement qui suit
        # remet le DOM a neuf. Il doit venir APRES, ici.
        # ⚠️ ET LA BANDE << PROCHAIN BADGE >> DE L'ACCUEIL NE REAPPARAITRA PAS :
        # elle est eteinte volontairement (`#nextBadgeBox{display:none
        # !important}`), le prochain badge vit dans les reglages. L'element
        # reste dans le DOM pour que le JS puisse y ecrire sans planter. J'ai
        # cru a un defaut du banc et cherche une demi-heure : ce n'en est pas
        # un.
        self.js("if(typeof renderBadgesGrid === 'function') renderBadgesGrid();")
        self.attendre(0.4)

    def vers(self, cle_i18n):
        """Amene sous les yeux la carte des reglages qui porte cette cle.

        ⚠️ ON VISE PAR LA CLE DE TRADUCTION, PAS PAR LE TEXTE NI PAR UN RANG.
        Le texte change avec la langue -- un banc qui cherche << Compte >> ne
        trouve rien en turc -- et le rang change des qu'on insere une carte.
        La cle i18n, elle, est la meme dans les six langues et survit aux
        deplacements."""
        # ⚠️ LE SELECTEUR SE CONSTRUIT AVEC DES GUILLEMETS DOUBLES. Une
        # premiere version passait la cle par %r : Python rendait 'retour_titre'
        # avec ses apostrophes, et le selecteur devenait '[data-i18n='retour...
        # -- une erreur de syntaxe JS, pas une carte introuvable.
        self.js('''
            const e = document.querySelector('[data-i18n="%s"]');
            if(!e) throw new Error('carte introuvable : %s');
            const carte = e.closest('.card') || e;
            carte.scrollIntoView({ block: 'center' });
        ''' % (cle_i18n, cle_i18n))
        self.attendre(0.6)

    def clic(self, selecteur):
        self.page.click(selecteur)
        self.attendre(0.5)

    def clic_texte(self, texte):
        """Clique le premier element qui PORTE ce texte. Sert aux tuiles, dont
        les identifiants changent plus souvent que les mots."""
        self.page.get_by_text(texte, exact=False).first.click()
        self.attendre(0.6)

    # ---- rapporter ----
    def photo(self, nom=None):
        self.prise += 1
        nom = nom or ("%02d" % self.prise)
        chemin = self.dossier / ("%s-%s.png" % (self.scene, nom))
        self.page.screenshot(path=str(chemin))
        return chemin


# ============ LES SCENES ============
# Une scene = une fonction. Elle recoit le pilote, elle laisse des images.
# ⚠️ UNE PHRASE DE NARRATION PAR SCENE, ET LA SCENE SE COUPE SUR LA PHRASE.
# C'est ce qui rend la bande-son independante de l'app : quand un ecran change,
# on remplace l'image dans son creneau et la voix ne bouge pas. L'inverse --
# une narration collee aux gestes filmes -- oblige a reenregistrer six langues
# a chaque evolution.
SCENES = {}


def scene(nom, phrase):
    def poser(f):
        f.phrase = phrase
        SCENES[nom] = f
        return f
    return poser


@scene("accueil", "Chaque jour, une seance qui t'attend.")
def scene_accueil(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.mosaique(rang=3, carreaux=240, gagnees=[1, 2])
    p.recharger()
    p.ecran("home")
    p.photo("01")


@scene("tableau", "Chaque carte affine un tableau du monde germanophone.")
def scene_tableau(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.mosaique(rang=3, carreaux=120, gagnees=[1, 2])
    p.recharger()
    p.ecran("home")
    p.photo("01-debut")
    # L'arc du parcours, en trois etats : les premiers sont les plus beaux.
    for carreaux, nom in ((360, "02-milieu"), (690, "03-presque")):
        p.mosaique(rang=3, carreaux=carreaux, gagnees=[1, 2])
        p.photo(nom)
    # Le denouement : a la derniere carte, la mosaique DEVIENT le tableau.
    p.mosaique(rang=3, carreaux=700, gagnees=[1, 2, 3], trophee=3)
    p.photo("04-gagne")


@scene("galerie", "Les tableaux gagnes restent dans ta galerie.")
def scene_galerie(p):
    p.vie(maitrises=540, serie=31, seance=24)
    p.mosaique(rang=6, carreaux=300, gagnees=[1, 2, 3, 4, 5])
    p.recharger()
    p.ecran("home")
    p.js("ouvrirGalerieMosaiques();")
    p.attendre(2.5)
    p.photo("01")


@scene("adapter", "Tu regles l'app a ta facon : le niveau, l'objectif, ce que la carte prononce.")
def scene_adapter(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    p.ecran("settings")
    for cle, nom in (("setup_settings_title", "01-configuration"),
                     ("settings_daily_goal", "02-objectif"),
                     ("carte_dire_titre", "03-ce-que-la-carte-dit"),
                     ("voice_title", "04-voix"),
                     ("settings_progress_by_category", "05-progression")):
        try:
            p.vers(cle)
            p.photo(nom)
        except Exception:
            # ⚠️ UNE CARTE ABSENTE NE FAIT PAS TOMBER LA SCENE. Les cles des
            # reglages bougent plus souvent que les ecrans ; ce qui manque se
            # voit a l'image manquante, et le reste de la serie est sauve.
            pass


@scene("carte", "Tu reponds. Ce qui resiste revient plus souvent, ce qui est acquis s'espace.")
def scene_carte(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    p.ecran("home")
    # ⚠️ LA VRAIE PORTE, PAS UN DECOR. Une carte posee a la main montrerait un
    # mot ; celle-ci montre LA carte que l'app a choisie pour aujourd'hui --
    # echeances comprises. C'est la difference entre une capture et une preuve.
    p.js("await ouvrirSeanceDuJour();")
    p.attendre(3.0)
    p.photo("01-recto")
    p.js("if(typeof flipCard === 'function') flipCard();")
    p.attendre(1.8)
    p.photo("02-verso")


@scene("ecoute", "Quand tu ne peux pas regarder, tu ecoutes : l'allemand continue.")
def scene_ecoute(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    p.js("ouvrirEcouteMenu();")
    p.attendre(2.0)
    p.photo("01-menu")
    p.js("demarrerEcoute('A1');")
    p.attendre(3.5)
    p.photo("02-en-ecoute")


@scene("dictionnaire", "Un mot te manque ? Il est deja dans l'app.")
def scene_dictionnaire(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    # Un mot qui n'est PAS dans les cartes : c'est tout l'interet du
    # dictionnaire, et c'est le cas qu'un testeur a signale le 15 septembre.
    p.js("ouvrirRechercheDepuisAccueil('Scherbe');")
    p.attendre(3.0)
    p.photo("01")


@scene("examens", "Le vocabulaire des listes officielles du Goethe-Institut et du DTZ.")
def scene_examens(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    p.js("openOrbPanel('pruefung');")
    p.attendre(2.0)
    p.photo("01-panneau")


@scene("retournement", "La carte se retourne -- le geste de l'app, filme, pas imite.")
def scene_retournement(p):
    """⚠️ LE MOUVEMENT EST DANS L'APP, ON NE LE REFABRIQUE PAS. La carte tourne
    sur `rotateY(180deg)` en 0,55 s (voir .flashcard dans index.html). Toute
    imitation au montage -- un ecrasement horizontal, un fondu -- sera moins
    juste que la chose elle-meme, et vieillira le jour ou l'animation changera.
    On filme."""
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    p.ecran("home")
    p.js("await ouvrirSeanceDuJour();")
    p.attendre(3.0)
    p.moteur()
    p.attendre(1.0)          # un temps sur le recto : on lit le mot
    p.page.click("#flashcard")
    p.attendre(2.2)          # la bascule (0,55 s) puis le verso
    p.coupez()


@scene("affinage", "La mosaique s affine, carte apres carte, jusqu au tableau.")
def scene_affinage(p):
    """⚠️ LE SEUL PLAN QU UNE IMAGE FIXE NE PEUT PAS RACONTER. Deux captures --
    la mosaique a mi-chemin, puis l oeuvre finie -- ne disent pas que c est le
    MEME tableau : elles se lisent comme deux ecrans differents. Le mouvement
    est l information.
    ⚠️ ON NE PASSE PAS PAR poserCarreau() : il est plafonne a 80 carreaux par
    jour, ce qui est la regle du produit et n a aucune raison de plier pour un
    tournage. On pose l etat et on redessine -- la subdivision affichee est la
    vraie, seul le rythme est celui du film."""
    p.vie(maitrises=312, serie=12, seance=18)
    p.mosaique(rang=3, carreaux=120, gagnees=[1, 2])
    p.recharger()
    p.ecran("home")
    p.js("document.getElementById('carteMosaique').scrollIntoView({block:'start'});")
    p.attendre(1.0)
    p.moteur()
    p.js("""
        const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE));
        for(let c = 120; c <= 700; c += 29){
            v.c = c;
            localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(v));
            majMosaiqueAccueil();
            await new Promise(r => setTimeout(r, 110));
        }
        // La derniere carte : la mosaique DEVIENT le tableau, et la plaque
        // arrive avec lui.
        v.c = 700; v.g = [1, 2, 3]; v.t = 3;
        localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(v));
        majMosaiqueAccueil();
    """)
    p.attendre(2.5)
    p.coupez()


@scene("affinage_net", "La mosaique s affine -- photographiee, pas filmee.")
def scene_affinage_net(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.mosaique(rang=3, carreaux=120, gagnees=[1, 2])
    p.recharger()
    p.ecran("home")
    p.js("document.getElementById('carteMosaique').scrollIntoView({block:'start'});")
    p.attendre(1.0)
    dossier = p.sequence("affinage", 0)
    etapes = list(range(120, 701, 12))
    for i, c in enumerate(etapes):
        p.js("""
            const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE));
            v.c = %d;
            localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(v));
            majMosaiqueAccueil();
            await new Promise(r => setTimeout(r, 90));
        """ % c)
        p.page.screenshot(path=str(dossier / ("%03d.png" % i)))
    # Le denouement, tenu quelques images : la mosaique DEVIENT le tableau.
    p.js("""
        const v = JSON.parse(localStorage.getItem(MOSAIQUE_CLE));
        v.c = 700; v.g = [1, 2, 3]; v.t = 3;
        localStorage.setItem(MOSAIQUE_CLE, JSON.stringify(v));
        majMosaiqueAccueil();
        await new Promise(r => setTimeout(r, 600));
    """)
    for j in range(18):
        p.page.screenshot(path=str(dossier / ("%03d.png" % (len(etapes) + j))))


@scene("ecoute_suite", "Le mot suivant arrive tout seul : les mains restent libres.")
def scene_ecoute_suite(p):
    p.vie(maitrises=312, serie=12, seance=18)
    p.recharger()
    p.js("ouvrirEcouteMenu();")
    p.attendre(1.5)
    p.js("demarrerEcoute('A1');")
    p.attendre(2.0)
    p.moteur()
    p.attendre(6.0)
    p.coupez()


@scene("credits", "Ce qui vient d'ailleurs est nomme, et ce qui n'est pas a nous est dit.")
def scene_credits(p):
    p.ecran("settings")
    p.vers("credits_title")
    p.photo("01")


@scene("zero", "Les remises a plat sont ensemble, de la plus douce a la plus definitive.")
def scene_zero(p):
    p.ecran("settings")
    p.vers("settings_zero_title")
    p.photo("01")


@scene("badges", "Sept badges : quatre sur l'experience, trois sur la serie.")
def scene_badges(p):
    p.vie(maitrises=312, serie=12, seance=18)
    # ⚠️ LES BADGES NE SE PEIGNENT QUE DEPUIS openSettings(), qui sort tout de
    # suite quand personne n'est connecte -- et le banc ne se connecte jamais.
    # La grille restait donc VIDE sur toutes les captures des reglages, ce qui
    # se lit comme une carte cassee alors que rien ne l'est. On appelle le
    # peintre nous-memes.
    # ⚠️ ON PASSE PAR addXp(), PAS PAR localStorage. getXp() fait tourner
    # migrateXpScaleIfNeeded() au passage : une valeur posee a la main est
    # relue comme si elle datait de l'ancienne echelle et se retrouve DIVISEE.
    # Le banc a filme des badges d'experience grisses avec 260 points au
    # compteur -- ils valaient 26 une fois la migration passee, et rien ne le
    # disait.
    p.js("""
        if(typeof addXp === 'function') addXp(300);
        if(typeof checkAndUnlockBadges === 'function') checkAndUnlockBadges();
        if(typeof renderBadgesGrid === 'function') renderBadgesGrid();
    """)
    p.attendre(1.0)
    p.ecran("settings")
    p.vers("settings_badges_title")
    p.photo("01")


@scene("bande", "Le prochain badge se rappelle a l'accueil, quand il est proche.")
def scene_bande(p):
    p.vie(maitrises=312, serie=12, seance=18)
    # ⚠️ L'EXPERIENCE AVANT LE DEVERROUILLAGE, sinon la bande annonce un badge
    # a 1 sur 1 : vie() a deja fait son controle quand l'XP arrive, et l'app,
    # elle, contrôle a chaque reussite. Un ordre inverse filme un etat qui
    # n'existe sur l'appareil de personne.
    p.js("""
        if(typeof addXp === 'function') addXp(300);
        if(typeof checkAndUnlockBadges === 'function') checkAndUnlockBadges();
    """)
    p.recharger()
    p.ecran("home")
    p.photo("01")


@scene("rappels", "Un rappel quotidien, si tu en veux un.")
def scene_rappels(p):
    p.ecran("settings")
    p.vers("notif_title")
    p.photo("01")


@scene("retour", "Une idee, un defaut : ca s'ecrit dans l'app, le contexte suit tout seul.")
def scene_retour(p):
    p.ecran("settings")
    p.vers("retour_titre")
    p.photo("01")


@scene("reglages", "Ton compte t'appartient : tu peux le supprimer d'ici.")
def scene_reglages(p):
    p.ecran("settings")
    p.js("""
        const b = document.getElementById('suppressionCompteOuvrir');
        if(b) b.scrollIntoView({block:'center'});
    """)
    p.attendre(0.5)
    p.photo("01")


# ============ LE TOURNAGE ============
def tourner(scenes, langue, appareil, clips):
    from playwright.sync_api import sync_playwright

    port, arreter = servir()
    dossier = SORTIE / langue / appareil
    dossier.mkdir(parents=True, exist_ok=True)
    url = "http://127.0.0.1:%d/index.html" % port
    faits, rates = [], []

    with sync_playwright() as pw:
        navigateur = pw.chromium.launch()
        try:
            for nom in scenes:
                contexte = navigateur.new_context(
                    service_workers="block",
                    record_video_dir=str(dossier / "clips") if clips else None,
                    record_video_size=APPAREILS[appareil]["viewport"] if clips else None,
                    **APPAREILS[appareil])
                depart = time.monotonic()
                page = contexte.new_page()
                p = None
                try:
                    page.goto(url, wait_until="load", timeout=60000)
                    # L'app se monte en plusieurs temps ; on attend la fonction
                    # qui n'existe qu'une fois le script principal execute.
                    page.wait_for_function("typeof majMosaiqueAccueil === 'function'",
                                           timeout=30000)
                    p = Pilote(page, dossier, nom, depart)
                    p.langue(langue)
                    SCENES[nom](p)
                    faits.append(nom)
                except Exception as e:
                    # ⚠️ UNE SCENE QUI TOMBE N'ARRETE PAS LE TOURNAGE, mais elle
                    # se dit. Un banc qui avale ses erreurs rend des images
                    # manquantes qu'on ne decouvre qu'au montage.
                    rates.append((nom, str(e).split("\n")[0][:120]))
                finally:
                    page.close()
                    contexte.close()
                    if clips:
                        renommer_clip(dossier, nom, getattr(p, "top", None),
                                      getattr(p, "fin", None))
        finally:
            navigateur.close()
            arreter()

    return dossier, faits, rates


def renommer_clip(dossier, nom, top=None, fin=None):
    """Playwright nomme ses videos au hasard et ne les ferme qu'a la fermeture
    du contexte : on les recupere APRES, on coupe autour de ce qui compte, et
    on convertit en mp4.

    ⚠️ SANS MARQUES, ON GARDE TOUT -- y compris l'ecran d'ouverture et la pose
    de l'etat. Une scene qui veut un clip montrable appelle p.moteur() juste
    avant le mouvement et p.coupez() juste apres."""
    clips = dossier / "clips"
    orphelins = sorted(clips.glob("*.webm"), key=lambda f: f.stat().st_mtime)
    if not orphelins:
        return
    source = orphelins[-1]
    cible = clips / (nom + ".mp4")
    if shutil.which("ffmpeg"):
        commande = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(source)]
        if top is not None:
            # -ss APRES -i : plus lent, mais exact a l'image pres. Avant -i, la
            # coupe saute a l'image-cle la plus proche et rate un mouvement de
            # 0,55 s.
            commande += ["-ss", "%.2f" % max(0, top)]
            if fin is not None and fin > top:
                commande += ["-t", "%.2f" % (fin - top)]
        commande += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                     "-pix_fmt", "yuv420p", str(cible)]
        subprocess.run(commande, check=False)
        source.unlink(missing_ok=True)
    else:
        source.rename(clips / (nom + ".webm"))


def main():
    a = argparse.ArgumentParser(description="Le banc de tournage de l'app.")
    a.add_argument("--liste", action="store_true", help="les scenes disponibles")
    a.add_argument("--photos", action="store_true", help="rapporter des images")
    a.add_argument("--clips", action="store_true", help="rapporter des videos")
    a.add_argument("--scene", nargs="*", help="limiter a ces scenes")
    a.add_argument("--langue", default="fr", choices=LANGUES)
    a.add_argument("--appareil", default="iphone67", choices=sorted(APPAREILS))
    args = a.parse_args()

    if args.liste or not (args.photos or args.clips):
        print("Scenes :")
        for nom, f in SCENES.items():
            print("  %-10s %s" % (nom, f.phrase))
        print("\nExemple : python video/banc.py --photos --langue tr")
        return 0

    scenes = args.scene or list(SCENES)
    inconnues = [s for s in scenes if s not in SCENES]
    if inconnues:
        print("Scene inconnue : " + ", ".join(inconnues))
        return 1

    dossier, faits, rates = tourner(scenes, args.langue, args.appareil, args.clips)
    print("%d scene(s) tournee(s) dans %s" % (len(faits), dossier))
    for nom, erreur in rates:
        print("  RATE  %-10s %s" % (nom, erreur))
    return 1 if rates else 0


if __name__ == "__main__":
    sys.exit(main())
