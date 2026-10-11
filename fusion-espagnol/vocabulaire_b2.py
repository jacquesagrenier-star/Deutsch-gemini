# -*- coding: utf-8 -*-
"""Le B2 de l'espagnol etoffe, et des mots remis a leur niveau (10 oct. 2026).

    python fusion-espagnol/vocabulaire_b2.py

Releve par la relecture de Gemini et verifie : le B2 n'avait que 121 verbes
(contre 316 en B1) et 17 adverbes, sans les verbes de nuance et de registre
qu'un B2 attend (acatar, propiciar, soslayar...). Et des mots ajoutes pour
les scenes etaient trop rares pour le B1 (colinabo, grosella espinosa,
omoplato) : ils passent en B2, comme dans le corpus allemand.

LES CONJUGAISONS SONT CALCULEES (conjugueur.py), jamais tapees : la regle a
ete mesuree sur les 832 verbes du corpus (563 reguliers reproduits a
l'identique, les differences etant de vrais irreguliers ou des fautes des
donnees, corrigees par corriger_verbos.py). Ne sont pris ici que des verbes
reguliers ; les -iar sans accent passent par regulier_ar().

Rien n'est insere au milieu d'une liste rangee par position : les verbes
sont ranges par infinitif (CLES_STABLES), les adverbes ajoutes a la fin du
B2, dernier niveau de l'espagnol. Idempotent.
"""
import io, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conjugueur as C          # noqa
from corriger_verbos import regulier_ar  # noqa

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")

# (infinitif, fr, en, exemple, exemple fr, exemple en, construction)
VERBES = [
 ("acatar", "respecter, se conformer à", "to comply with", "Todos deben acatar las normas.", "Tout le monde doit respecter les règles.", "Everyone must comply with the rules.", None),
 ("propiciar", "favoriser, provoquer", "to foster, to bring about", "El diálogo propició un acuerdo.", "Le dialogue a favorisé un accord.", "Dialogue brought about an agreement.", None),
 ("escatimar", "lésiner sur, ménager", "to skimp on, to spare", "No escatimaron esfuerzos para ayudarnos.", "Ils n'ont pas ménagé leurs efforts pour nous aider.", "They spared no effort to help us.", None),
 ("constatar", "constater", "to note, to confirm", "Los médicos constataron una mejora.", "Les médecins ont constaté une amélioration.", "The doctors noted an improvement.", None),
 ("soslayar", "éluder, contourner", "to sidestep", "El ministro soslayó la pregunta.", "Le ministre a éludé la question.", "The minister sidestepped the question.", None),
 ("desencadenar", "déclencher", "to trigger", "La noticia desencadenó una ola de protestas.", "La nouvelle a déclenché une vague de protestations.", "The news triggered a wave of protests.", None),
 ("tergiversar", "déformer (des propos)", "to twist, to distort", "Los periodistas tergiversaron sus palabras.", "Les journalistes ont déformé ses propos.", "The journalists twisted his words.", None),
 ("recalcar", "souligner, insister sur", "to stress", "La profesora recalcó la importancia del repaso.", "La professeure a insisté sur l'importance des révisions.", "The teacher stressed the importance of revision.", None),
 ("vislumbrar", "entrevoir", "to glimpse, to make out", "Ya se vislumbra una solución.", "On entrevoit déjà une solution.", "A solution is already in sight.", None),
 ("agilizar", "accélérer, simplifier", "to speed up", "Hay que agilizar los trámites.", "Il faut accélérer les démarches.", "The procedures need speeding up.", None),
 ("afrontar", "affronter, faire face à", "to face", "Tenemos que afrontar el problema.", "Nous devons faire face au problème.", "We have to face the problem.", None),
 ("solventar", "résoudre, régler", "to sort out, to settle", "Solventamos el error en una hora.", "Nous avons réglé l'erreur en une heure.", "We sorted out the error in an hour.", None),
 ("menospreciar", "sous-estimer, mépriser", "to underestimate, to look down on", "No menosprecies a tus rivales.", "Ne sous-estime pas tes adversaires.", "Don't underestimate your rivals.", None),
 ("desempeñar", "exercer, jouer (un rôle)", "to perform, to play (a role)", "Desempeña un papel clave en la empresa.", "Il joue un rôle clé dans l'entreprise.", "He plays a key role in the company.", None),
 ("fomentar", "encourager, promouvoir", "to promote, to encourage", "El programa fomenta la lectura.", "Le programme encourage la lecture.", "The programme promotes reading.", None),
 ("cuestionar", "remettre en question", "to question", "Nadie cuestiona su honestidad.", "Personne ne met en doute son honnêteté.", "Nobody questions her honesty.", None),
 ("reivindicar", "revendiquer", "to demand, to claim", "Los trabajadores reivindican mejores salarios.", "Les travailleurs revendiquent de meilleurs salaires.", "Workers are demanding better pay.", None),
 ("conllevar", "impliquer, entraîner", "to entail", "Este cargo conlleva mucha responsabilidad.", "Ce poste implique beaucoup de responsabilités.", "This post entails a lot of responsibility.", None),
 ("otorgar", "accorder, décerner", "to grant, to award", "Le otorgaron un premio por su investigación.", "On lui a décerné un prix pour ses recherches.", "She was awarded a prize for her research.", None),
 ("desestimar", "rejeter, écarter", "to dismiss, to reject", "El juez desestimó la demanda.", "Le juge a rejeté la plainte.", "The judge dismissed the claim.", None),
 ("postergar", "reporter, ajourner", "to postpone", "Postergaron la reunión hasta el lunes.", "Ils ont reporté la réunion à lundi.", "They postponed the meeting until Monday.", None),
 ("fundamentar", "fonder, étayer", "to base, to back up", "Fundamenta bien tus argumentos.", "Étaye bien tes arguments.", "Back up your arguments properly.", None),
 ("ahondar", "approfondir", "to go deeper into", "El libro ahonda en la historia del barrio.", "Le livre approfondit l'histoire du quartier.", "The book delves into the history of the neighbourhood.", "ahondar en algo"),
 ("esbozar", "esquisser", "to sketch, to outline", "Esbozó una sonrisa.", "Il a esquissé un sourire.", "He gave a faint smile.", None),
 ("enfatizar", "mettre l'accent sur", "to emphasise", "El informe enfatiza la necesidad de invertir.", "Le rapport met l'accent sur la nécessité d'investir.", "The report emphasises the need to invest.", None),
 ("sopesar", "peser (le pour et le contre)", "to weigh up", "Hay que sopesar las ventajas y los inconvenientes.", "Il faut peser le pour et le contre.", "You have to weigh up the pros and cons.", None),
 ("derrochar", "gaspiller", "to waste, to squander", "No derroches el agua.", "Ne gaspille pas l'eau.", "Don't waste water.", None),
 ("acaparar", "accaparer", "to monopolise, to hog", "Siempre acapara la atención.", "Il accapare toujours l'attention.", "He always hogs the attention.", None),
 ("agravar", "aggraver", "to worsen", "La lluvia agravó la situación.", "La pluie a aggravé la situation.", "The rain made the situation worse.", None),
 ("mermar", "diminuer, réduire", "to diminish, to erode", "La crisis mermó sus ahorros.", "La crise a réduit leurs économies.", "The crisis eroded their savings.", None),
 ("entorpecer", "entraver, gêner", "to hinder, to hold up", "Las obras entorpecen el tráfico.", "Les travaux gênent la circulation.", "The roadworks are holding up traffic.", None),
 ("carecer", "manquer de", "to lack", "El pueblo carece de servicios básicos.", "Le village manque de services de base.", "The village lacks basic services.", "carecer de algo"),
 ("abarcar", "couvrir, englober", "to cover, to span", "El curso abarca toda la gramática.", "Le cours couvre toute la grammaire.", "The course covers all the grammar.", None),
 ("ratificar", "ratifier", "to ratify", "El Parlamento ratificó el tratado.", "Le Parlement a ratifié le traité.", "Parliament ratified the treaty.", None),
 ("descartar", "écarter, exclure", "to rule out", "No descartamos ninguna opción.", "Nous n'écartons aucune option.", "We're not ruling out any option.", None),
 ("plasmar", "exprimer, concrétiser", "to capture, to set out", "Plasmó sus ideas en un libro.", "Il a exprimé ses idées dans un livre.", "He set out his ideas in a book.", None),
 ("suscitar", "susciter", "to arouse, to spark", "La propuesta suscitó un gran debate.", "La proposition a suscité un grand débat.", "The proposal sparked a big debate.", None),
 ("conciliar", "concilier", "to reconcile, to balance", "Es difícil conciliar el trabajo y la familia.", "Il est difficile de concilier travail et famille.", "It's hard to balance work and family.", None),
 ("compaginar", "combiner, concilier", "to combine", "Compagina los estudios con un trabajo.", "Elle combine ses études et un travail.", "She combines her studies with a job.", None),
 ("sobrellevar", "supporter (une épreuve)", "to cope with", "Sobrelleva la enfermedad con valentía.", "Il supporte la maladie avec courage.", "He's coping with the illness bravely.", None),
 ("vaticinar", "prédire", "to predict", "Los expertos vaticinan una recuperación.", "Les experts prédisent une reprise.", "Experts are predicting a recovery.", None),
 ("disuadir", "dissuader", "to dissuade, to deter", "Intentaron disuadirlo de viajar.", "Ils ont essayé de le dissuader de voyager.", "They tried to talk him out of travelling.", None),
 ("eludir", "éluder, éviter", "to evade, to avoid", "Eludió responder a la pregunta.", "Il a évité de répondre à la question.", "He avoided answering the question.", None),
 ("incidir", "insister sur, avoir une incidence sur", "to stress, to have an impact on", "La profesora incidió en ese punto.", "La professeure a insisté sur ce point.", "The teacher stressed that point.", "incidir en algo"),
 ("aludir", "faire allusion à", "to allude to", "Aludió a la crisis sin nombrarla.", "Il a fait allusion à la crise sans la nommer.", "He alluded to the crisis without naming it.", "aludir a algo"),
 ("propugnar", "prôner, défendre", "to advocate", "El partido propugna una reforma fiscal.", "Le parti prône une réforme fiscale.", "The party advocates tax reform.", None),
 ("subsanar", "corriger, réparer (une erreur)", "to rectify", "Hay que subsanar los errores del formulario.", "Il faut corriger les erreurs du formulaire.", "The errors on the form must be rectified.", None),
 ("mitigar", "atténuer", "to mitigate", "Las medidas buscan mitigar el impacto.", "Les mesures cherchent à atténuer l'impact.", "The measures aim to mitigate the impact.", None),
 ("respaldar", "soutenir, appuyer", "to back, to support", "El equipo respalda al entrenador.", "L'équipe soutient l'entraîneur.", "The team is backing the coach.", None),
]
SANS_ACCENT_IAR = {"propiciar", "menospreciar", "conciliar"}

# (mot, categorie, fr, en, exemple, exemple fr, exemple en)
ADVERBES = [
 ("inevitablemente", "modo", "inévitablement", "inevitably", "Inevitablemente, los precios subirán.", "Inévitablement, les prix vont augmenter.", "Inevitably, prices will rise."),
 ("francamente", "discurso", "franchement", "frankly", "Francamente, no me convence.", "Franchement, ça ne me convainc pas.", "Frankly, I'm not convinced."),
 ("categóricamente", "modo", "catégoriquement", "categorically", "Lo negó categóricamente.", "Il l'a nié catégoriquement.", "He categorically denied it."),
 ("paulatinamente", "modo", "progressivement", "gradually", "La situación mejora paulatinamente.", "La situation s'améliore progressivement.", "The situation is gradually improving."),
 ("sumamente", "cantidad", "extrêmement", "extremely", "Es un tema sumamente delicado.", "C'est un sujet extrêmement délicat.", "It's an extremely delicate matter."),
 ("meramente", "modo", "simplement, purement", "merely", "Es meramente una sugerencia.", "C'est simplement une suggestion.", "It's merely a suggestion."),
 ("supuestamente", "duda", "soi-disant, prétendument", "supposedly", "Supuestamente llegaba a las ocho.", "Il était censé arriver à huit heures.", "He was supposedly arriving at eight."),
 ("indudablemente", "afirmacion", "sans aucun doute", "undoubtedly", "Es, indudablemente, el mejor jugador.", "C'est sans aucun doute le meilleur joueur.", "He is undoubtedly the best player."),
 ("previamente", "tiempo", "au préalable", "beforehand", "Hay que reservar previamente.", "Il faut réserver au préalable.", "You have to book beforehand."),
 ("posteriormente", "tiempo", "par la suite", "subsequently", "Posteriormente se mudó a Lima.", "Par la suite, il a déménagé à Lima.", "He subsequently moved to Lima."),
 ("notablemente", "cantidad", "nettement, notablement", "considerably", "Las ventas han crecido notablemente.", "Les ventes ont nettement augmenté.", "Sales have grown considerably."),
 ("rotundamente", "modo", "catégoriquement, sans appel", "flatly", "Se negó rotundamente.", "Il a refusé sans appel.", "He flatly refused."),
 ("aparentemente", "duda", "apparemment", "apparently", "Aparentemente, todo está en orden.", "Apparemment, tout est en ordre.", "Apparently, everything is in order."),
 ("a la larga", "tiempo", "à la longue", "in the long run", "A la larga, saldrás ganando.", "À la longue, tu y gagneras.", "In the long run, you'll come out ahead."),
 ("de antemano", "tiempo", "d'avance", "in advance", "Gracias de antemano.", "Merci d'avance.", "Thanks in advance."),
 ("a grandes rasgos", "discurso", "dans les grandes lignes", "broadly speaking", "A grandes rasgos, el plan es bueno.", "Dans les grandes lignes, le plan est bon.", "Broadly speaking, the plan is good."),
 ("en cierto modo", "discurso", "dans une certaine mesure", "in a way", "En cierto modo, tienes razón.", "Dans une certaine mesure, tu as raison.", "In a way, you're right."),
 ("con creces", "cantidad", "largement", "amply, by far", "Superó las expectativas con creces.", "Il a largement dépassé les attentes.", "He far exceeded expectations."),
 ("a regañadientes", "modo", "à contrecœur", "reluctantly", "Aceptó a regañadientes.", "Il a accepté à contrecœur.", "He reluctantly agreed."),
 ("sin lugar a dudas", "afirmacion", "sans aucun doute", "without a doubt", "Es, sin lugar a dudas, la mejor opción.", "C'est, sans aucun doute, la meilleure option.", "It's without a doubt the best option."),
]

# Des noms trop rares pour leur niveau : vers un theme B2 (cree si besoin).
NOUVEAUX_THEMES = [
 {"id": "frutas_verduras_b2", "niveau": "B2", "nom_theme": "Fruit and vegetables (advanced)", "nom_theme_es": "Frutas y verduras poco comunes", "svg_de": "obst_gemuese_b2"},
 {"id": "el_cuerpo_b2", "niveau": "B2", "nom_theme": "The body in detail", "nom_theme_es": "El cuerpo en detalle", "svg_de": "koerperteile_b2"},
]
DEPLACER = {
 "grosella": "frutas_verduras_b2", "grosella espinosa": "frutas_verduras_b2", "colinabo": "frutas_verduras_b2",
 "acelga": "frutas_verduras_b2", "alcachofa": "frutas_verduras_b2", "hinojo": "frutas_verduras_b2",
 "apio": "frutas_verduras_b2", "higo": "frutas_verduras_b2", "granada": "frutas_verduras_b2",
 "papaya": "frutas_verduras_b2", "boniato": "frutas_verduras_b2",
 "costilla": "el_cuerpo_b2", "columna vertebral": "el_cuerpo_b2", "omóplato": "el_cuerpo_b2",
 "corva": "el_cuerpo_b2", "nalgas": "el_cuerpo_b2",
 "trasero": "partes_del_cuerpo",
}
# Seuls les mots ajoutes le 10 oct. sont deplaces : ils sont en fin de leur
# theme d'origine, ou dans un theme ne le 10 oct. -- personne n'a encore de
# progression qu'un deplacement decalerait.
ORIGINES = {"frutas_verduras_b1", "cuerpo_humano", "las_verduras", "las_frutas"}


def lire(nom):
    return json.load(io.open(os.path.join(DATOS, nom), encoding="utf-8"))


def ecrire(nom, d):
    io.open(os.path.join(DATOS, nom), "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def main():
    # 1. Les verbes.
    verbos = lire("verbos.json")
    deja = {x["infinitif"] for n in verbos.values() for x in n}
    n_v = 0
    for inf, fr, en, ex, exf, exe, cons in VERBES:
        if inf in deja:
            continue
        if inf in SANS_ACCENT_IAR:
            conj = regulier_ar(inf)
        else:
            assert C.verbe_sur(inf), inf
            conj = C.conjuguer(inf)
        e = {"traduction": fr, "traduction_en": en, "exemple": ex, "exemple_fr": exf, "exemple_en": exe,
             "theme_source": "verbos_b2", "mot": inf, "infinitif": inf}
        e.update(conj)
        if cons:
            e["construccion"] = cons
        verbos["B2"].append(e)
        n_v += 1
    # Controle : des formes que l'on sait par coeur.
    idx = {x["infinitif"]: x for n in verbos.values() for x in n}
    for inf, rang, forme in (("recalcar", 0, "recalqué"), ("otorgar", 0, "otorgué"), ("agilizar", 0, "agilicé"),
                             ("mitigar", 0, "mitigué"), ("abarcar", 0, "abarqué")):
        assert idx[inf]["preterito"][rang] == forme, (inf, idx[inf]["preterito"][rang])
    assert idx["entorpecer"]["praesens"]["ich"] == "entorpezco" and idx["carecer"]["subjuntivo"][0] == "carezca"
    assert idx["propiciar"]["praesens"]["ich"] == "propicio"
    ecrire("verbos.json", verbos)

    # 2. Les adverbes, a la fin du B2.
    adv = lire("adverbios.json")
    deja = {x["mot"] for n in adv.values() for x in n}
    n_a = 0
    for mot, cat, fr, en, ex, exf, exe in ADVERBES:
        if mot in deja:
            continue
        adv["B2"].append({"traduction": fr, "traduction_en": en, "exemple": ex, "exemple_fr": exf,
                          "exemple_en": exe, "theme_source": "adverbios_b2", "mot": mot, "kategorie": cat})
        n_a += 1
    ecrire("adverbios.json", adv)

    # 3. Les noms remis a leur niveau.
    temas = lire("temas.json")
    par_id = {t["id"]: t for t in temas["themes"]}
    allemand = {t["id"]: t for t in json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]}
    for nt in NOUVEAUX_THEMES:
        if nt["id"] in par_id:
            continue
        t = {"id": nt["id"], "nom_theme": nt["nom_theme"], "nom_theme_es": nt["nom_theme_es"], "niveau": nt["niveau"],
             "svg": allemand[nt["svg_de"]].get("svg", ""), "mots": []}
        rang = max(i for i, x in enumerate(temas["themes"]) if x.get("niveau") == nt["niveau"])
        temas["themes"].insert(rang + 1, t)
        par_id[t["id"]] = t
    n_d = 0
    for mot, dest in DEPLACER.items():
        if any(m["mot"] == mot for m in par_id[dest]["mots"]):
            continue
        for tid in ORIGINES:
            t = par_id.get(tid)
            if not t:
                continue
            for i, m in enumerate(t["mots"]):
                if m["mot"] == mot:
                    e = t["mots"].pop(i)
                    e["theme_source"] = dest
                    par_id[dest]["mots"].append(e)
                    n_d += 1
                    break
    ecrire("temas.json", temas)
    print("verbes B2 : +%d   adverbes B2 : +%d   noms deplaces : %d" % (n_v, n_a, n_d))


if __name__ == "__main__":
    main()
