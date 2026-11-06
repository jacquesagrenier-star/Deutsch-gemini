"""Controle des donnees de l'ecrit du telc Deutsch A2·B1 : le courriel (partie LS, donnees/lesen-schreiben.json) et la
reponse courte (partie S, donnees/schreiben.json, qui porte aussi la grille, le bareme et les formules utiles).

Usage : python tests/telc_ecrire.py

Le format vient de preparation-examens/FORMAT-TELC.md (le Uebungstest gratuit du telc, format seulement) :
  Lesen und Schreiben (29-31) : un courriel recu qui pose des questions ; 29 Richtig/Falsch, 30 un choix a 2 ;
    31 y repondre (critere I sur 15).
  Schreiben (57) : repondre a un message court qui pose une question (wann, was, warum nicht, welches, wie lange,
    wo, wohin), en plus d'un mot (critere I sur 5).
Le controle verifie aussi :
  - chaque texte pour l'eleve en francais ET en anglais (suffixes _fr / _en, lus par champTelc) ;
  - les lettres modeles : formule d'appel, salutation, registre tenu (du / Sie), chaque note citant un extrait EXACT
    de sa lettre, sans chevauchement ; la lettre B1 plus longue que la lettre A2 ;
  - le courriel recu : formule d'appel, salutation, 3 ou 4 points, au moins autant de « ? » que de points ;
  - la feuille non devinable : la bonne reponse de 29 et de 30 n'est pas toujours a la meme place ;
  - les indices des points sont des expressions regulieres valides ;
  - le bareme et les temps de FORMAT-TELC.md.
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(RACINE, "visuel", "prototype", "telc", "donnees")
APPELS = ("Sehr geehrte", "Liebe ", "Lieber ", "Hallo ", "Hi ")
FINS = re.compile(r"(Mit freundlichen Grüßen|(Viele|Liebe|Herzliche) Grüße|Bis bald|Bis morgen|Bis Samstag|Bis Sonntag)")
DU = re.compile(r"(?<![^\W\d_])(du|dich|dir|dein|deine|deinen|deinem|deiner|euch)(?![^\W\d_])", re.I)
SIE_MILIEU = re.compile(r"[^.!?:\n]\s+(Sie|Ihnen|Ihr|Ihre|Ihren|Ihrem|Ihrer)(?![^\W\d_])")
FRAGEN = ("wann", "was", "warum nicht", "welches", "wie lange", "wo", "wohin")

fautes = []


def faute(ou, quoi):
    fautes.append(ou + " : " + quoi)


def mots(lignes):
    return sum(len([w for w in l.split() if re.search(r"[^\W\d_]", w)]) for l in lignes)


def bilingue(ou, o, noms):
    for nom in noms:
        for lang in ("fr", "en"):
            v = o.get(nom + "_" + lang)
            if not v or (isinstance(v, str) and not v.strip()) or (isinstance(v, list) and any(not str(x).strip() for x in v)):
                faute(ou, "« %s_%s » vide ou absent" % (nom, lang))
        a, b = o.get(nom + "_fr"), o.get(nom + "_en")
        if isinstance(a, list) and isinstance(b, list) and len(a) != len(b):
            faute(ou, "%s_fr et %s_en n'ont pas le meme nombre de lignes" % (nom, nom))


def lettre(ou, lignes, registre):
    if not lignes:
        faute(ou, "aucune ligne")
        return
    if not lignes[0].startswith(APPELS):
        faute(ou, "pas de formule d'appel : %r" % lignes[0][:40])
    if not any(FINS.search(l) for l in lignes[-3:]):
        faute(ou, "pas de salutation dans les trois dernieres lignes")
    corps = "\n".join(lignes)
    if registre == "formel":
        m = DU.search(corps)
        if m:
            faute(ou, "registre formel, mais « %s »" % m.group(1))
    else:
        m = SIE_MILIEU.search(corps)
        if m:
            faute(ou, "registre informel, mais « %s » au milieu d'une phrase" % m.group(1))


def modeles(ou, s):
    mod = s.get("modeles") or {}
    for niv in ("a2", "b1"):
        m = mod.get(niv)
        o2 = ou + ", modele " + niv.upper()
        if not m:
            faute(o2, "absent")
            continue
        lettre(o2, m.get("lignes") or [], s.get("registre"))
        notes = m.get("notes") or []
        if not notes:
            faute(o2, "aucune note")
        places = []
        for j, n in enumerate(notes):
            o3 = o2 + ", note %d" % (j + 1)
            bilingue(o3, n, ["note"])
            ex = n.get("de") or ""
            ligne = next((k for k, l in enumerate(m.get("lignes") or []) if ex and ex in l), None)
            if ligne is None:
                faute(o3, "l'extrait n'est pas dans la lettre : %r" % ex)
                continue
            debut = m["lignes"][ligne].index(ex)
            for (l2, d2, f2) in places:
                if l2 == ligne and debut < f2 and debut + len(ex) > d2:
                    faute(o3, "l'extrait chevauche une autre note : %r" % ex)
            places.append((ligne, debut, debut + len(ex)))
    if mod.get("a2") and mod.get("b1") and mots(mod["b1"].get("lignes") or []) <= mots(mod["a2"].get("lignes") or []):
        faute(ou, "la lettre B1 n'est pas plus longue que la lettre A2")
    bilingue(ou, s, ["passer"])
    return mots(mod.get("a2", {}).get("lignes") or []), mots(mod.get("b1", {}).get("lignes") or [])


def regex(ou, liste):
    if not liste:
        faute(ou, "aucun indice")
    for x in liste or []:
        try:
            re.compile(x)
        except re.error as e:
            faute(ou, "indice invalide %r : %s" % (x, e))


def ids_uniques(nom, series):
    ids = [s.get("id") for s in series]
    if len(set(ids)) != len(ids):
        faute(nom, "deux series ont le meme id")


def courriels():
    d = json.load(open(os.path.join(DONNEES, "lesen-schreiben.json"), encoding="utf-8"))
    series = d.get("series") or []
    if len(series) < 3:
        faute("lesen-schreiben.json", "moins de 3 series (%d)" % len(series))
    ids_uniques("lesen-schreiben.json", series)
    if {s.get("registre") for s in series} != {"formel", "informel"}:
        faute("lesen-schreiben.json", "il faut des courriels formels ET informels")
    longueurs = []
    for s in series:
        ou = "courriel %s" % s.get("id")
        if s.get("registre") not in ("formel", "informel"):
            faute(ou, "registre inconnu : %r" % s.get("registre"))
        bilingue(ou, s, ["situation"])
        m = s.get("mail") or {}
        for c in ("von", "an", "betreff", "lignes"):
            if not m.get(c):
                faute(ou, "mail.%s vide" % c)
        lettre(ou + ", courriel recu", m.get("lignes") or [], s.get("registre"))
        nq = sum(l.count("?") for l in m.get("lignes") or [])
        punkte = s.get("punkte") or []
        if not 3 <= len(punkte) <= 4:
            faute(ou, "%d points a traiter (3 ou 4 attendus)" % len(punkte))
        if nq < len(punkte):
            faute(ou, "%d points a traiter, mais %d « ? » dans le courriel" % (len(punkte), nq))
        for k, p in enumerate(punkte):
            o2 = ou + ", point %d" % (k + 1)
            if not (p.get("de") or "").strip():
                faute(o2, "« de » vide")
            bilingue(o2, p, ["aide"])
            regex(o2, p.get("indices"))
        fragen = s.get("fragen") or []
        if [f.get("n") for f in fragen] != [29, 30]:
            faute(ou, "les questions doivent etre 29 puis 30 : %r" % [f.get("n") for f in fragen])
        for f in fragen:
            o2 = ou + ", question %s" % f.get("n")
            bilingue(o2, f, ["erkl"])
            if not (f.get("de") or "").strip():
                faute(o2, "enonce vide")
            if f.get("n") == 29 and (f.get("typ") != "rf" or f.get("bon") not in (0, 1)):
                faute(o2, "29 est un Richtig/Falsch (typ rf, bon 0 ou 1)")
            if f.get("n") == 30:
                o = f.get("o") or []
                if f.get("typ") != "ab" or len(o) != 2 or len(set(o)) != 2 or f.get("bon") not in (0, 1):
                    faute(o2, "30 est un choix a 2 (typ ab, deux choix differents, bon 0 ou 1)")
        longueurs.append(modeles(ou, s))
    for n in (29, 30):
        bons = [f["bon"] for s in series for f in s.get("fragen") or [] if f.get("n") == n and "bon" in f]
        if len(bons) >= 3 and len(set(bons)) == 1:
            faute("lesen-schreiben.json", "question %d : la bonne reponse est toujours la meme (%r)" % (n, bons[0]))
    return len(series), longueurs


def reponses_courtes(d):
    series = d.get("series") or []
    if len(series) < 3:
        faute("schreiben.json", "moins de 3 series (%d)" % len(series))
    ids_uniques("schreiben.json", series)
    longueurs = []
    for s in series:
        ou = "message court %s" % s.get("id")
        if s.get("registre") not in ("formel", "informel"):
            faute(ou, "registre inconnu : %r" % s.get("registre"))
        if s.get("frage") not in FRAGEN:
            faute(ou, "mot interrogatif hors du format : %r" % s.get("frage"))
        bilingue(ou, s, ["situation", "conseil"])
        n = s.get("nachricht") or {}
        texte = " ".join(n.get("lignes") or [])
        if not n.get("von") or not n.get("art") or not texte:
            faute(ou, "nachricht incomplete")
        if "?" not in texte:
            faute(ou, "le message ne pose pas de question")
        mot = (s.get("frage") or "").split()[0] if s.get("frage") else ""
        if mot and not re.search(r"(?i)(?<![^\W\d_])" + re.escape(mot) + r"(?![^\W\d_])", texte):
            faute(ou, "le message ne contient pas « %s »" % mot)
        regex(ou, s.get("indices"))
        longueurs.append(modeles(ou, s))
        for niv in ("a2", "b1"):
            if mots((s.get("modeles") or {}).get(niv, {}).get("lignes") or []) < 3:
                faute(ou, "modele %s : il faut plus d'un mot" % niv)
    return len(series), longueurs


def grille(d):
    k = d.get("kriterien") or []
    if [x.get("id") for x in k] != ["I", "II", "III", "IV"]:
        faute("kriterien", "les quatre criteres I a IV, dans l'ordre")
    for x in k:
        if not x.get("de"):
            faute("kriterien " + str(x.get("id")), "nom allemand absent")
        bilingue("kriterien " + str(x.get("id")), x, ["titre", "b1", "a2", "moins"])
    b = d.get("bareme") or {}
    if b.get("paliers") != ["b1p", "b1", "a2p", "a2", "moins"]:
        faute("bareme", "paliers inattendus")
    if b.get("email_I") != [15, 11, 9, 8, 4]:
        faute("bareme", "courriel : FORMAT-TELC.md donne 15, 11, 9, 8, 4")
    if b.get("ensemble") != [10, 8, 6, 4, 2]:
        faute("bareme", "criteres d'ensemble : FORMAT-TELC.md donne 10, 8, 6, 4, 2")
    if (b.get("kurz_I") or [None])[0] != 5:
        faute("bareme", "message court : 5 points au critere I")
    t = d.get("temps") or {}
    if t.get("ls_bloc_min") != 35 or t.get("s_min") != 10:
        faute("temps", "FORMAT-TELC.md : 35 min (Sprachbausteine + Lesen und Schreiben), 10 min (Schreiben)")


def redemittel(d):
    groupes = d.get("redemittel") or []
    total = 0
    for g in groupes:
        bilingue("formules " + str(g.get("id")), g, ["titre"])
        for it in g.get("items") or []:
            total += 1
            o = "formules %s, %r" % (g.get("id"), (it.get("de") or "")[:30])
            if not (it.get("de") or "").strip():
                faute(o, "« de » vide")
            if it.get("reg") not in ("du", "Sie", "beide"):
                faute(o, "registre inconnu : %r" % it.get("reg"))
            bilingue(o, it, ["sens"])
    if total < 20:
        faute("formules", "moins de 20 formules (%d)" % total)
    return len(groupes), total


s = json.load(open(os.path.join(DONNEES, "schreiben.json"), encoding="utf-8"))
ne, le = courriels()
nk, lk = reponses_courtes(s)
grille(s)
ng, nf = redemittel(s)
print("Courriels (LS) : %d series ; lettres modeles A2 %s mots, B1 %s mots" % (ne, [a for a, b in le], [b for a, b in le]))
print("Reponses courtes (S) : %d series ; A2 %s mots, B1 %s mots" % (nk, [a for a, b in lk], [b for a, b in lk]))
print("Formules utiles : %d groupes, %d formules" % (ng, nf))
if fautes:
    print("\n%d faute(s) :" % len(fautes))
    for f in fautes:
        print("   " + f)
    sys.exit(1)
print("OK : le format du telc est respecte.")
