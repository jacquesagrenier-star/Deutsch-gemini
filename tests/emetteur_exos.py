# -*- coding: utf-8 -*-
"""Le fabricant commun des lots d'exercices.

Chaque jeu se ramene a la meme forme : quelques CAS -- deux ou trois, jamais
plus -- et une liste de phrases qui disent chacune a quel cas elles
appartiennent. L'explication et l'indice viennent du cas, pas de la phrase.

⚠️ POURQUOI COMPOSER PLUTOT QU'ECRIRE. Un jeu de cinquante exercices demande
450 chaines dans cinq langues. Ecrites une a une, elles derivent : le meme
point de grammaire finit explique de trois facons dans le meme jeu, et la
traduction turque d'aujourd'hui ne ressemble pas a celle de la semaine
prochaine. Composees a partir de deux ou trois cas, elles sont regulieres par
construction -- et l'apprenant retrouve la MEME phrase a chaque fois qu'il
retrouve la meme faute, ce qui est exactement ce qu'on veut d'une explication.

⚠️ ET L'INDICE NE NOMME JAMAIS LE CAS. Defaut attrape par le verificateur le
15 septembre : un indice par cas revient a ecrire la reponse au-dessus du
champ. Un seul indice par jeu, qui rappelle la question.
"""
import io
import json
import os

RACINE = r"C:\Users\jacqu\OneDrive\Desktop\Mes Projets\DeutschAI"
LANGUES = ["fr", "en", "tr", "uk", "fa"]


def ecrire(jeu, topic, cas, indice, lot, nom_fichier):
    """cas : {cle: (fr,en,tr,uk,fa)} ; indice : (fr,en,tr,uk,fa) ;
       lot : [(question, bonne, options, cle_de_cas, (fr,en,tr,uk,fa))]"""
    entrees, langues = [], []
    vues = set()
    for q, c, o, k, phr in lot:
        if q in vues:
            raise SystemExit("  ! question en double dans %s : %s" % (jeu, q))
        vues.add(q)
        # o = None : question a FRAPPE LIBRE. wortstellungFrage est ainsi
        # depuis toujours -- proposer deux boutons donnerait la reponse, la
        # question etant justement « quel verbe, et a quelle place ».
        if o is not None and c not in o:
            raise SystemExit("  ! la bonne reponse n'est pas dans les options : " + q)
        if k not in cas:
            raise SystemExit("  ! cas inconnu (%s) : %s" % (k, q))
        entrees.append({"q": q, "c": c, "o": o,
                        "fr": phr[0], "en": phr[1],
                        "h": indice[0], "he": indice[1],
                        "x": cas[k][0], "xe": cas[k][1]})
        e = {"q": q}
        for i, lg in enumerate(LANGUES):
            e["t_" + lg] = phr[i]
            e["h_" + lg] = indice[i]
            e["x_" + lg] = cas[k][i]
        langues.append(e)

    base = os.path.join(RACINE, "ajouts", nom_fichier)
    io.open(base + ".json", "w", encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": jeu, "topic": topic, "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    io.open(base + "-langues.json", "w", encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": jeu, "entrees": langues},
                   ensure_ascii=False, indent=1) + "\n")
    print("  %-38s %d entrees" % (jeu, len(entrees)))
