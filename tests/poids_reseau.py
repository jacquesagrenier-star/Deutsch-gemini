# -*- coding: utf-8 -*-
"""Ce que l'application telecharge vraiment a chaque lancement.

POURQUOI CET OUTIL EXISTE. Le 3 septembre 2026, verbe.json etait servi par
GitHub en `application/octet-stream` -- et Fastly ne compresse que les types
texte. L'app tirait donc 2 096 Ko a chaque demarrage pour ce seul fichier, la
ou themes.json, plus gros sur le disque, n'en pesait que 561. Personne ne
regardait, et le defaut a vecu des mois.

Le verificateur ne peut pas faire ce controle : il doit rester hors ligne et
tenir en quelques secondes (voir CLAUDE.md). Cet outil-ci sort donc a part, et
se lance a la main -- apres avoir grossi un fichier de donnees, ou quand un
testeur trouve le demarrage lent.

CE QU'IL NE FAIT PAS. Il ne devine pas la regle de GitHub. J'ai cherche et
ecarte : la taille brute, le non-ASCII en tete, l'UTF-8 invalide, le BOM, les
octets de controle, les attributs git. Aucune n'explique. L'outil se contente
donc de MESURER et de nommer ce qui n'est pas compresse -- un fait verifiable
vaut mieux qu'une regle inventee.

    python tests/poids_reseau.py
"""
import os
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = ("https://raw.githubusercontent.com/"
        "jacquesagrenier-star/Deutsch-gemini/main/")

# Charges des le demarrage, dans cet ordre (voir les appels a urlDonnees).
DEMARRAGE = ["adjectif.json", "verbe.json", "adverbe.json", "redewendung.json",
             "pruefung.json", "funktionswort.json", "themes.json",
             "grammaire.json"]
# Charges seulement quand l'utilisateur en a besoin.
DEMANDE = ["exercices.json"]


def peser(fichier):
    """Rend (octets sur le fil, type servi, compresse ?)."""
    requete = urllib.request.Request(
        BASE + fichier, method="HEAD",
        headers={"Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(requete, timeout=30) as r:
            entetes = r.headers
            return (int(entetes.get("Content-Length") or 0),
                    (entetes.get("Content-Type") or "?").split(";")[0],
                    (entetes.get("Content-Encoding") or "") != "")
    except Exception as e:
        return (None, str(e)[:40], False)


def bloc(titre, fichiers):
    total = 0
    suspects = []
    print(u"\n%s" % titre)
    for f in fichiers:
        fil, type_, compresse = peser(f)
        disque = os.path.getsize(os.path.join(RACINE, f)) if os.path.exists(
            os.path.join(RACINE, f)) else 0
        if fil is None:
            print(u"   %-18s INJOIGNABLE : %s" % (f, type_))
            continue
        total += fil
        marque = u"" if compresse else u"   <-- NON COMPRESSE"
        print(u"   %-18s %7.0f Ko sur le fil  %7.0f Ko sur disque  %-12s%s"
              % (f, fil / 1024.0, disque / 1024.0, type_, marque))
        if not compresse:
            suspects.append((f, fil, disque))
    return total, suspects


d, s1 = bloc(u"AU DEMARRAGE, a chaque lancement (rien n'est mis en cache : "
             u"urlDonnees() ajoute ?v=Date.now())", DEMARRAGE)
a, s2 = bloc(u"A LA DEMANDE", DEMANDE)

print(u"\n" + u"-" * 74)
print(u"   demarrage : %.0f Ko  |  a la demande : %.0f Ko"
      % (d / 1024.0, a / 1024.0))

suspects = s1 + s2
if suspects:
    print(u"\n   %d fichier(s) servis SANS compression :" % len(suspects))
    for f, fil, disque in suspects:
        print(u"     %s -- %.0f Ko payes pour %.0f Ko de donnees."
              % (f, fil / 1024.0, disque / 1024.0))
    print(u"\n   Ce qui a marche pour verbe.json : le reecrire A RAISON D'UNE")
    print(u"   ENTREE PAR LIGNE. Meme poids que du JSON entierement compacte,")
    print(u"   mais les diffs git nomment encore l'entree modifiee.")
else:
    print(u"\n   Tout est servi compresse.")
