# -*- coding: utf-8 -*-
"""Les clips de la visite guidee (voix-visite/), mesures comme controler_sons.py mesure les mots : SATURE, CLIC,
COURT, ILLISIBLE -- et le DEBIT (lettres par seconde de parole) de chaque clip refait, compare aux clips de la meme
langue : un clip tronque ou qui s'egare (eleven_v3 en persan) sort de la fourchette. Controle aussi que l'empreinte
de textes.json est celle du texte affiche. Sans navigateur, sans reseau.
    python audio/controler_visite.py <racine> <liste-a-blanc.txt>
(la liste : la sortie de « python audio/voix_visite.py --a-blanc », gardee AVANT de generer)"""
import hashlib, io, json, os, statistics, sys
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.join(RACINE, "audio"))
import controler_sons as cs
import voix_visite as vv

touches = set()
for l in io.open(sys.argv[2], encoding="utf-8"):
    p = l.split()
    if len(p) == 4 and p[3] == "caracteres":
        touches.add((p[0], p[1]))

textes = vv.textes_de_l_app()
es = vv.textes_espagnols(textes)
manifeste = json.load(io.open(os.path.join(RACINE, "voix-visite", "textes.json"), encoding="utf-8"))
taches = [(l, l, c, textes[l], os.path.join(RACINE, "voix-visite", l)) for l in vv.LANGUES for c in vv.CLIPS]
taches += [("es-" + l, l, c, es[l], os.path.join(RACINE, "voix-visite", "es", l))
           for l in vv.LANGUES_ES for c in vv.CLIPS_PROPRES_ES]

mesures, graves, perimes, a_ecouter = {}, [], [], []
for cle, langue, clip, t, dossier in taches:
    texte = vv.prononcer(vv.composer([t[k] for k in vv.CLIPS[clip]]), langue)
    f = os.path.join(dossier, clip + ".mp3")
    if not os.path.exists(f):
        graves.append("%s %s : fichier absent" % (cle, clip)); continue
    m = cs.mesurer(f)
    if m is None:
        graves.append("%s %s : ILLISIBLE" % (cle, clip)); continue
    d = [x for x in cs.defauts(m, texte) if x != "TRAINE"]
    if hashlib.sha1(texte.encode("utf-8")).hexdigest() != manifeste.get(cle, {}).get(clip):
        perimes.append("%s %s" % (cle, clip))
    m["debit"] = cs.lettres(texte) / max(m["parole"], 0.1)
    m["lettres"] = cs.lettres(texte)
    mesures[(cle, clip)] = (langue, m, d)
    if d and (cle, clip) in touches:
        graves.append("%s %s : %s (crete %.1f, rms %.1f)" % (cle, clip, ",".join(d), m["crete"], m["rms"]))

print("%d clips mesures, %d refaits" % (len(mesures), len(touches)))
for langue in vv.LANGUES:
    debits = [m["debit"] for (cle, clip), (l, m, d) in mesures.items() if l == langue]
    med = statistics.median(debits)
    ligne = []
    for (cle, clip), (l, m, d) in sorted(mesures.items()):
        if l != langue or (cle, clip) not in touches:
            continue
        ecart = m["debit"] / med - 1
        marque = ""
        if abs(ecart) > 0.30:
            marque = " !DEBIT"
            a_ecouter.append("%s %s : debit %.1f lettres/s pour une mediane de %.1f (%+.0f %%), %.1f s pour %d lettres" % (
                cle, clip, m["debit"], med, 100 * ecart, m["parole"], m["lettres"]))
        ligne.append("%s %s %.1f s %+.0f %%%s%s" % (cle, clip, m["parole"], 100 * ecart, " " + ",".join(d) if d else "", marque))
    print("  %s (mediane %.1f lettres/s) : %s" % (langue, med, " ; ".join(ligne)))
print("empreintes en retard sur le texte affiche : %s" % (", ".join(perimes) or "aucune"))
# Le debit ne condamne pas un clip (un clip court, ou plein de nombres, sort vite de la fourchette) : il designe
# ceux qu'une oreille doit entendre.
for x in a_ecouter:
    print("A ECOUTER :", x)
print("BILAN OK" if not graves and not perimes else "BILAN A REVOIR : " + " | ".join(graves + ["en retard : " + x for x in perimes]))
