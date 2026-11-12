# -*- coding: utf-8 -*-
"""Controle des conversations jouees (visuel/prototype/conversation/donnees/). Gratuit, sans navigateur.

    python tests/conversations.py            # tout
    python tests/conversations.py pp1-pass   # une conversation, dans toutes ses langues

Ce qu'il verifie, et pourquoi (visuel/CONVERSATIONS.md) :
  - LA STRUCTURE : le debut existe, chaque « va » mene a un noeud, chaque personne est dans personnes.json avec un
    visage pour l'expression demandee (ou son repli), chaque replique et chaque choix ont leur francais ;
  - UNE FIN REUSSIE : depuis le debut, chaque reponse juste mene a une fin (« va »: null), sans boucle ; une faute
    (« faux ») ou une demande de repetition (« repete ») revient au meme noeud et ne compte pas comme un echange ;
  - LA LONGUEUR (regle de Jacques du 11 nov. 2026, « que ce ne soit pas trop long, surtout au debut ») : le nombre
    d'echanges (les reponses de l'apprenant) de chaque chemin, selon le niveau : Premiers pas 3-4, fin de l'A1 5-6,
    A2 6-8, B1 et plus jusqu'a 10 ; Premiers pas : une seule branche ;
  - LE REGISTRE : au Sie / usted, aucune replique juste en du / tu (une faute peut l'etre, c'est sa raison d'etre) ;
  - LES NOMBRES : un chiffre ecrit a sa lecture en lettres (champ « dit », ou {x:mots}) ;
  - LES MOTS VUS (Premiers pas) : chaque reponse juste de l'apprenant a l'etape N n'emploie que des mots des
    phrases et des cartes des etapes 1 a N (premiers-pas.json), plus quelques noms propres (pays, villes) ; ce que
    dit la personne en face est seulement signale (on comprend plus qu'on ne dit).
  - LA LISTE : donnees/index.json et les fichiers concordent.
"""
import io, json, os, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "visuel", "prototype", "conversation")
DONNEES = os.path.join(DOSSIER, "donnees")
PP = {"de": os.path.join(RACINE, "premiers-pas.json"), "es": os.path.join(RACINE, "espanol", "datos", "premiers-pas.json"),
      "en": os.path.join(RACINE, "anglais", "datos", "premiers-pas.json"),
      "en-gb": os.path.join(RACINE, "anglais", "datos-gb", "premiers-pas.json")}
LONGUEUR = {"premiers-pas": (3, 4), "voyage": (5, 6), "A2": (6, 8), "B1": (1, 10), "B2": (1, 10), "C1": (1, 10)}
REPLI = {"question": ["attentive", "sourire"], "attentive": ["question", "sourire"], "surprise": ["attentive", "sourire"],
         "perplexe": ["attentive", "surprise", "sourire"], "amuse": ["sourire"], "sourire": ["attentive"]}
TUTOIEMENT = {"Sie": r"\b(du|dich|dir|dein\w*)\b", "usted": r"\b(t[uú]|te|ti|contigo|tus?)\b"}
# Les noms propres qu'une reponse peut dire sans les avoir vus en carte : ils se comprennent tels quels.
PROPRES = {"kanada", "frankreich", "belgien", "schweiz", "berlin", "deutschland", "canada", "francia", "belgica", "suiza",
           "madrid", "espana", "montreal", "france", "boston", "usa", "america"}
erreurs, avis = [], []


def plier(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").replace("ß", "ss")
    return re.sub(r"[^a-z0-9 ]+", " ", s).split()


def vocabulaire(langue, etape):
    d = json.load(io.open(PP[langue], encoding="utf-8"))
    mots = set()
    for e in d["etapes"][:etape]:
        for p in e.get("phrases", []):
            mots.update(plier(p["p"]))
        for c in e.get("cartes", []):
            mots.update(plier(c[0] if isinstance(c, list) else str(c)))
    return mots


def sans_gabarit(s):
    return re.sub(r"\{\w+(?::\w+)?\}", " ", s or "")


def controler(chemin, personnes):
    nom = os.path.basename(chemin)
    try:
        c = json.load(io.open(chemin, encoding="utf-8"))
    except ValueError as e:
        erreurs.append("%s : JSON illisible (%s)" % (nom, e)); return
    E = lambda m: erreurs.append("%s : %s" % (nom, m))
    A = lambda m: avis.append("%s : %s" % (nom, m))
    langue = c.get("langue")
    for k in ("id", "langue", "niveau", "registre", "titre", "intro", "personnes", "debut", "noeuds", "bilan"):
        if k not in c:
            E("champ « %s » absent" % k)
    if nom != "%s.%s.json" % (c.get("id"), langue):
        E("le nom du fichier ne suit pas <id>.<langue>.json")
    noeuds = c.get("noeuds", {})
    if c.get("debut") not in noeuds:
        E("debut « %s » introuvable" % c.get("debut")); return
    for q in c.get("personnes", []):
        if q not in personnes:
            E("personne « %s » absente de personnes.json" % q)

    def replique(r, ou):
        if "recit" in r:
            if not (r["recit"] or {}).get("fr"):
                E("%s : recit sans francais" % ou)
            return
        if r.get("qui") not in c.get("personnes", []):
            E("%s : « %s » ne fait pas partie de la conversation" % (ou, r.get("qui")))
            return
        v = personnes[r["qui"]]["visages"]
        air = r.get("air", "sourire")
        if air not in v and not any(a in v for a in REPLI.get(air, [])):
            A("%s : %s n'a pas de visage « %s » (ni de repli)" % (ou, r["qui"], air))
        if not r.get("t") or not r.get("fr"):
            E("%s : replique sans texte ou sans francais" % ou)
        if re.search(r"\d", sans_gabarit(r.get("t"))) and not r.get("dit"):
            E("%s : « %s » a des chiffres sans lecture en lettres (champ dit)" % (ou, r.get("t")))
        if re.search(TUTOIEMENT.get(c.get("registre"), r"$^"), plier_texte(r.get("t", ""))):
            E("%s : tutoiement dans une conversation au %s : « %s »" % (ou, c.get("registre"), r.get("t")))

    vu = vocabulaire(langue, c["etape"]) if c.get("parcours") == "premiers-pas" and langue in PP else None
    vu_gb = vocabulaire("en-gb", c["etape"]) if vu is not None and langue == "en" else None
    autour = set()
    for nid, n in noeuds.items():
        for r in n.get("dit", []):
            replique(r, nid)
            if vu is not None and "t" in r:
                autour.update(m for m in plier(sans_gabarit(r["t"])) if m not in vu and m not in PROPRES)
        if not n.get("choix"):
            E("%s : aucun choix" % nid)
        for i, ch in enumerate(n.get("choix", [])):
            ou = "%s, choix %d" % (nid, i + 1)
            if not ch.get("t") or not ch.get("fr"):
                E("%s : choix sans texte ou sans francais" % ou)
            for r in ch.get("puis", []):
                replique(r, ou)
            if ch.get("faux"):
                if not (ch.get("aide") or {}).get("fr"):
                    E("%s : faute sans explication (aide)" % ou)
                continue
            if "va" not in ch:
                E("%s : « va » absent (null pour la fin)" % ou)
            elif ch["va"] is not None and ch["va"] not in noeuds:
                E("%s : va « %s » introuvable" % (ou, ch["va"]))
            if re.search(r"\d", sans_gabarit(ch.get("t"))):
                E("%s : chiffres dans une reponse : ecrire les nombres en lettres" % ou)
            if re.search(TUTOIEMENT.get(c.get("registre"), r"$^"), plier_texte(ch.get("t", ""))):
                E("%s : tutoiement dans une reponse juste au %s : « %s »" % (ou, c.get("registre"), ch["t"]))
            if vu is not None:
                inconnus = [m for m in plier(sans_gabarit(ch["t"])) if m not in vu and m not in PROPRES]
                if inconnus:
                    E("%s : mot(s) pas encore vu(s) a l'etape %d : %s" % (ou, c["etape"], ", ".join(inconnus)))
                # l'anglais britannique (variante=gb) : sa reponse propre doit venir de SES etapes (the bill, pas the check)
                if ch.get("t_gb") and vu_gb is not None:
                    inconnus = [m for m in plier(sans_gabarit(ch["t_gb"])) if m not in vu_gb and m not in PROPRES]
                    if inconnus:
                        E("%s : variante britannique, mot(s) pas encore vu(s) : %s" % (ou, ", ".join(inconnus)))
    if autour:
        A("la personne en face dit des mots pas encore vus (normal en petite quantite) : %s" % ", ".join(sorted(autour)))

    # Les chemins : chaque reponse juste, sauf repetition, est un echange ; la fin doit etre atteinte sans boucle.
    longueurs, branches = [], 0
    for nid, n in noeuds.items():
        suites = {ch.get("va") for ch in n.get("choix", []) if not ch.get("faux") and not ch.get("repete")}
        if len(suites) > 1:
            branches += 1

    def marcher(nid, pile, n):
        if nid in pile:
            E("boucle : " + " > ".join(pile + [nid])); return
        justes = [ch for ch in noeuds[nid].get("choix", []) if not ch.get("faux") and not ch.get("repete")]
        if not justes:
            E("%s : aucune reponse juste" % nid); return
        for ch in justes:
            if ch.get("va") is None:
                longueurs.append(n + 1)
            elif ch["va"] in noeuds:
                marcher(ch["va"], pile + [nid], n + 1)
    marcher(c["debut"], [], 0)
    if not longueurs:
        E("aucun chemin n'arrive a la fin")
    else:
        cle = c.get("parcours") if c.get("parcours") in LONGUEUR else c.get("niveau")
        mini, maxi = LONGUEUR.get(cle, (1, 10))
        if min(longueurs) < mini or max(longueurs) > maxi:
            E("longueur : de %d a %d echanges, la regle pour « %s » est %d-%d" % (min(longueurs), max(longueurs), cle, mini, maxi))
        if c.get("parcours") == "premiers-pas" and branches > 1:
            E("Premiers pas : %d branches, une seule permise" % branches)
        print("  %-24s %s  %d-%d echanges, %d branche(s), %d chemin(s)" % (nom, c.get("niveau"), min(longueurs), max(longueurs), branches, len(longueurs)))


def plier_texte(s):
    return " ".join(plier(sans_gabarit(s)))


def main():
    personnes = json.load(io.open(os.path.join(DOSSIER, "personnes.json"), encoding="utf-8"))
    personnes = {k: v for k, v in personnes.items() if not k.startswith("_")}
    for q, p in personnes.items():
        for air, img in p.get("visages", {}).items():
            if not os.path.exists(os.path.join(RACINE, "visuel", "prototype", img)):
                erreurs.append("personnes.json : %s %s : image absente (%s)" % (q, air, img))
    idx = json.load(io.open(os.path.join(DONNEES, "index.json"), encoding="utf-8"))
    attendus = {"%s.%s.json" % (e["id"], l) for e in idx["conversations"] for l in e["langues"]}
    presents = {f for f in os.listdir(DONNEES) if f.endswith(".json") and f != "index.json"}
    for f in sorted(attendus - presents):
        erreurs.append("index.json annonce %s, absent" % f)
    for f in sorted(presents - attendus):
        erreurs.append("%s n'est pas dans index.json" % f)
    choisis = sys.argv[1:]
    for f in sorted(presents):
        if not choisis or f.split(".")[0] in choisis:
            controler(os.path.join(DONNEES, f), personnes)
    for a in avis:
        print("  avis   ", a)
    for e in erreurs:
        print("  ERREUR ", e)
    print("  %d erreur(s), %d avis" % (len(erreurs), len(avis)))
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
