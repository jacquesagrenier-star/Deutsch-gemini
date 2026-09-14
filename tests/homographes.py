# -*- coding: utf-8 -*-
"""Les homographes FRANCAIS : quand ce n'est pas l'allemand qui est ambigu.

Une collision de glose n'est pas toujours un defaut. Quatre especes :
  1. de VRAIS synonymes allemands (Couch / Sofa) -- rien a corriger
  2. un masculin et son feminin (Koch / Koechin) -- rien a corriger
  3. un mot et son derive (kalt / Kaelte) -- rien a corriger
  4. DEUX MOTS SANS AUCUN RAPPORT qui tombent sur le meme mot francais
     parce que c'est LE FRANCAIS qui est ambigu : « entree » (Eingang,
     Vorspeise), « plat » (Gericht, flach), « personne » (Person, niemand).

Seule la quatrieme est un defaut, et elle se detecte : les deux mots ne
partagent ni racine, ni categorie grammaticale, ni theme.
"""
import io
import json
import collections
import re

SYN = json.load(io.open("synonymes.json", encoding="utf-8"))["voisins"]


def voisins(m):
    s = set(SYN.get(m, []))
    for k, v in SYN.items():
        if m in v:
            s.add(k)
            s.update(v)
    s.discard(m)
    return s


# ---- 1. ramasser toutes les entrees, AVEC leur theme -------------------
entrees = []   # (mot, glose, categorie, theme)


def ajouter(o, cat, theme):
    m = o.get("mot") or o.get("infinitif")
    t = (o.get("traduction") or "").strip()
    if m and t:
        entrees.append((m.strip(), t, cat, theme))


th = json.load(io.open("themes.json", encoding="utf-8"))


def parcourir_themes(o, nom=None):
    if isinstance(o, dict):
        n = o.get("nom") or o.get("titre") or o.get("id") or nom
        if "mots" in o and isinstance(o["mots"], list):
            for w in o["mots"]:
                if isinstance(w, dict):
                    ajouter(w, "nom", n)
        for v in o.values():
            parcourir_themes(v, n)
    elif isinstance(o, list):
        for v in o:
            parcourir_themes(v, nom)


parcourir_themes(th)

for fich, cat in [("verbe.json", "verbe"), ("adjectif.json", "adjectif"),
                  ("adverbe.json", "adverbe"), ("funktionswort.json", "outil"),
                  ("redewendung.json", "expression")]:
    try:
        d = json.load(io.open(fich, encoding="utf-8"))
    except Exception:
        continue
    pile = [d]
    while pile:
        o = pile.pop()
        if isinstance(o, dict):
            if ("mot" in o or "infinitif" in o) and "traduction" in o:
                ajouter(o, cat, cat)
            pile.extend(o.values())
        elif isinstance(o, list):
            pile.extend(o)

# ---- 2. grouper par glose normalisee ----------------------------------


def norme(t):
    t = t.lower().strip()
    t = re.sub(r"\s*\(.*?\)\s*", " ", t)      # « apres (cela) » -> « apres »
    t = re.sub(r"^(le |la |l'|les |un |une |se |s'|de )", "", t)
    return re.sub(r"\s+", " ", t).strip(" ,;")


par = collections.defaultdict(dict)
for m, t, cat, theme in entrees:
    par[norme(t)].setdefault(m, (t, cat, theme))


def racine(a, b):
    a, b = a.lower().replace("sich ", ""), b.lower().replace("sich ", "")
    if a in b or b in a:
        return True
    n = 5
    return any(a[i:i + n] in b for i in range(max(0, len(a) - n + 1)))


sortie = []
for g, mots in sorted(par.items()):
    if len(mots) < 2:
        continue
    noms = sorted(mots)
    paires = [(a, b) for i, a in enumerate(noms) for b in noms[i + 1:]]
    # on ne garde que les paires SANS rapport : ni synonymes declares,
    # ni meme racine, ni meme theme.
    dures = []
    for a, b in paires:
        if b in voisins(a):
            continue
        if racine(a, b):
            continue
        if mots[a][2] and mots[a][2] == mots[b][2]:
            continue                       # meme theme = champ lexical commun
        dures.append((a, b))
    if dures:
        sortie.append((g, mots, dures))

print()
print("  %d gloses francaises portent DEUX MOTS ALLEMANDS SANS RAPPORT" % len(sortie))
print("  (ni synonymes, ni meme racine, ni meme theme)")
print()
for g, mots, dures in sortie:
    print("  « %s »" % g)
    for m in sorted(mots):
        t, cat, theme = mots[m]
        print("        %-24s %-28s [%s]" % (m, t, theme or cat))
    print()

# ---- 3. LE TRI QUI COMPTE ---------------------------------------------
# Une collision de glose n'aveugle l'apprenant que si les DEUX gloses sont
# ecrites PAREIL. Des que l'une porte une precision -- « entree (prix) »,
# « la langue (organe) » -- la carte se distingue deja d'elle-meme, et il
# n'y a rien a reparer.
print()
print("=" * 72)
aveugles, deja = [], []
for g, mots, dures in sortie:
    for a, b in dures:
        ta, tb = mots[a][0].strip().lower(), mots[b][0].strip().lower()
        (aveugles if ta == tb else deja).append((g, a, mots[a], b, mots[b]))

print("  A REPARER : %d paires ou les DEUX gloses sont ecrites pareil" % len(aveugles))
print("  (l'apprenant voit le francais, deux allemands repondent, un seul passe)")
print()
for g, a, ia, b, ib in aveugles:
    print("    « %-28s %-22s [%-26s vs  %-20s [%s]" % (
        g + " »", a, (ia[2] or ia[1]) + "]", b, ib[2] or ib[1]))
print()
print("  DEJA DISTINGUEES par une precision entre parentheses : %d paires" % len(deja))

# ---- 4. LES TROIS PILES ------------------------------------------------
# Les 59 paires aveugles ne demandent pas le meme geste :
#   REGISTRE  une locution et un adverbe simple qui disent la MEME chose
#             (« par consequent » : Infolgedessen / folglich). Le sens est
#             identique -- c'est le niveau de langue qui differe. Gloser
#             autrement serait mentir ; il faut marquer le registre.
#   SYNONYME  deux mots allemands vraiment interchangeables (Couch / Sofa,
#             Handy / Mobiltelefon). Rien a regloser : a DECLARER dans
#             synonymes.json, pour que les deux reponses soient acceptees.
#   HOMOGRAPHE  c'est le francais qui est ambigu. Les deux allemands n'ont
#             aucun rapport (Eingang / Vorspeise). La glose doit trancher.
REGISTRE = {"au bout du compte", "d'accord", "d'apres cela", "en fin de compte",
            "encore une fois", "heureusement", "indeniable", "neanmoins",
            "negliger", "occuper de", "par consequent", "peu a peu",
            "a la maison", "tout a fait, completement"}
SYNONYME = {"ascenseur", "baccalaureat", "canape", "creche, garderie",
            "nom de famille", "telephone portable", "energie eolienne",
            "courant artistique", "diplome"}


def sansacc(t):
    for a, b in zip("àâäéèêëîïôöùûüç", "aaaeeeeiioouuuc"):
        t = t.replace(a, b)
    return t


piles = collections.OrderedDict([("REGISTRE", []), ("SYNONYME", []),
                                 ("HOMOGRAPHE FRANCAIS", [])])
for g, a, ia, b, ib in aveugles:
    k = sansacc(g)
    nom = "REGISTRE" if k in REGISTRE else "SYNONYME" if k in SYNONYME \
        else "HOMOGRAPHE FRANCAIS"
    piles[nom].append((g, a, ia, b, ib))

for nom, lst in piles.items():
    print()
    print("  ---- %s : %d paires ----" % (nom, len(lst)))
    for g, a, ia, b, ib in lst:
        print("    %-30s %-22s [%-26s %-22s [%s]" % (
            "« " + g + " »", a, (ia[2] or ia[1]) + "]", b, ib[2] or ib[1]))
