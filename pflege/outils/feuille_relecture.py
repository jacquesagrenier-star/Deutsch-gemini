# -*- coding: utf-8 -*-
"""La feuille de relecture medicale d'un chapitre des Soins : seulement ce qui porte ⚕️, en allemand et en francais,
une case « juste / a corriger » et la place d'ecrire la correction. Pour une personne du metier (infirmiere,
Praxisanleiterin), imprimable. Plan de relecture : pflege/PLAN-CHAPITRES.md et le bilan du 16 nov. (point 4).

    python pflege/outils/feuille_relecture.py ch07_schmerz        # une feuille
    python pflege/outils/feuille_relecture.py --premiers          # douleur, releve, admission, telephone
    python pflege/outils/feuille_relecture.py --tous              # les 14 chapitres

Sortie : pflege/relecture/<chapitre>.html (et un resume a l'ecran). Fichiers DERIVES : on corrige les sources
(pflege/sources/...), jamais une feuille. Ce que la feuille rassemble, pour le chapitre :
  - les repliques des dialogues marquees relire (dialogues.json), avec la note du dialogue en tete ;
  - les mots, paires et abreviations du chapitre dont le champ relire est rempli (themes.json) ;
  - les cartes-phrases marquees relire (redemittel.json) ;
  - les ecrits (leur note ⚕️) ;
  - les explications des scenes qui portent ⚕️ (visuel/prototype/<scene>.points.json) ;
  - la section « L'allemand ⚕️ » du theme illustre du chapitre (pflege/sources/themes_soins/<cle>/A-RELIRE.md).

    python pflege/outils/feuille_relecture.py --premiers --lots <dossier>   # et les lots du second avis

Les lots (<dossier>/<chapitre>.txt, une ligne « id | contexte | allemand | francais | point » par point) servent a la
relecture croisee par un autre modele AVANT la soignante ; l'id (chapitre + empreinte du texte) ne change pas tant que
le texte ne change pas, pour rapprocher les reponses.
"""
import hashlib
import html
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
DATOS = os.path.join(RACINE, "pflege", "datos")
PROTO = os.path.join(RACINE, "visuel", "prototype")
SORTIE = os.path.join(RACINE, "pflege", "relecture")
PREMIERS = ["ch07_schmerz", "ch08_uebergabe", "ch01_aufnahme", "ch10_telefon"]
e = html.escape


def lire(nom):
    with open(os.path.join(DATOS, nom), encoding="utf-8") as f:
        return json.load(f)


def nettoyer(s):
    return re.sub(r"<[^>]+>", "", str(s or "")).strip()


def lignes_chapitre(c, donnees):
    """[(section, contexte, allemand, francais, point)]"""
    dlgs, themes, cartes, sujets = donnees
    out = []
    # les dialogues
    par_id = {d["id"]: d for d in dlgs}
    for did in c.get("dialogues", []):
        d = par_id.get(did)
        if not d:
            continue
        titre = "%s · %s" % (d.get("titre_de", ""), d.get("niveau", ""))
        if isinstance(d.get("relire"), str) and d["relire"].strip():
            out.append(("Dialogues", titre, "", "", d["relire"]))
        for nid, n in d.get("noeuds", {}).items():
            unites = [("", r) for r in n.get("dit", []) if "t" in r]
            for ch in n.get("choix", []):
                unites.append(("réponse fausse" if ch.get("faux") else "réponse", ch))
                unites += [("", r) for r in ch.get("puis", []) if "t" in r]
            for genre, u in unites:
                if not u.get("relire"):
                    continue
                qui = u.get("qui") or "soignant(e)"
                ctx = "%s · %s%s" % (titre, qui, (" · " + genre) if genre else "")
                out.append(("Dialogues", ctx, u.get("t", ""), u.get("fr", ""), u.get("relire_note") or ""))
    # les mots, paires, abreviations
    rangs = {}
    for th in themes:
        for i, w in enumerate(th.get("mots", [])):
            rangs["%s:%d" % (th["id"], i)] = w
    for cle in c.get("mots", []) + c.get("paires", []) + c.get("abreviations", []):
        w = rangs.get(cle)
        if not w or not (isinstance(w.get("relire"), str) and w["relire"].strip()):
            continue
        mot = ((w.get("genre") + " ") if w.get("genre") in ("der", "die", "das") else "") + w.get("mot", "")
        if w.get("sorte") == "paire":
            de = "« %s » → %s" % (w.get("patient", ""), mot)
            fr = "« %s » → %s" % (w.get("traduction_patient", ""), w.get("traduction", ""))
            sect = "Paires patient / service"
        else:
            de, fr = mot, w.get("traduction", "")
            sect = "Abréviations" if "(=" in w.get("mot", "") else "Mots"
        if w.get("exemple"):
            de += "\n" + w["exemple"]
            fr += "\n" + (w.get("exemple_fr") or "")
        out.append((sect, cle.split(":")[0], de, fr, w["relire"]))
    # les cartes-phrases
    par_carte = {k["id"]: k for k in cartes}
    for kid in c.get("cartes", []):
        k = par_carte.get(kid)
        if not k or not k.get("relire"):
            continue
        out.append(("Phrases du service", kid, k.get("de", ""), (k.get("trad") or {}).get("fr", ""),
                    k["relire"] if isinstance(k["relire"], str) else ""))
    # les ecrits
    par_sujet = {s["id"]: s for s in sujets}
    for sid in c.get("ecrits", []):
        s = par_sujet.get(sid)
        if s and isinstance(s.get("relire"), str) and s["relire"].strip():
            titre = s.get("titre_de") or ((s.get("titre") or {}).get("fr") if isinstance(s.get("titre"), dict) else "")
            out.append(("Écrits", sid, titre or "", (s.get("titre") or {}).get("fr", "") if isinstance(s.get("titre"), dict) else "", s["relire"]))
    # les scenes : les explications qui portent ⚕️
    for nom in c.get("scenes", []):
        p = os.path.join(PROTO, nom + ".points.json")
        if not os.path.exists(p):
            continue
        sc = json.load(open(p, encoding="utf-8"))
        for niv, couche in (sc.get("couches") or {}).items():
            for q in (couche.get("qs") or []) if isinstance(couche, dict) else []:
                n = q.get("n") if isinstance(q, dict) else None
                if isinstance(n, str) and "⚕" in n:
                    # la bonne reponse est toujours la PREMIERE de « c » (la scene les melange) ; « phrase » est la
                    # phrase entiere, donnee en plus quand la question est un trou
                    choix = q.get("c") or []
                    juste = choix[0] if choix else (q.get("phrase") or "")
                    de = nettoyer(q.get("q", "")) + "\n✓ " + nettoyer(juste)
                    if q.get("phrase") and q["phrase"] != juste:
                        de += "  (" + nettoyer(q["phrase"]) + ")"
                    if choix[1:]:
                        de += "\n✗ " + "\n✗ ".join(nettoyer(x) for x in choix[1:])
                    fr = ("✓ " + nettoyer(q["sens"])) if q.get("sens") else ""
                    out.append(("Scènes", "%s · %s" % (nom, niv), de, fr, nettoyer(n)))
    # le theme illustre : la section « L'allemand ⚕️ » de sa note de relecture
    note = os.path.join(RACINE, "pflege", "sources", "themes_soins", c.get("cle", ""), "A-RELIRE.md")
    if c.get("theme_illustre") and os.path.exists(note):
        dedans, puce = False, None
        for ligne in open(note, encoding="utf-8").read().splitlines() + ["## fin"]:
            if ligne.startswith("## "):
                if puce:
                    out.append(("Thème illustré", c["theme_illustre"].replace(".html", ""), puce, "", "⚕️ à valider"))
                dedans, puce = ("⚕" in ligne), None
            elif dedans and ligne.startswith("- "):
                if puce:
                    out.append(("Thème illustré", c["theme_illustre"].replace(".html", ""), puce, "", "⚕️ à valider"))
                puce = ligne[2:].strip()
            elif dedans and puce and ligne.strip():
                puce += " " + ligne.strip()
    # une meme replique marquee deux fois (deux branches du meme dialogue) n'est relue qu'une fois
    vues, uniques = set(), []
    for l in out:
        cle = (l[0], l[1], l[2], l[4])
        if cle not in vues:
            vues.add(cle)
            uniques.append(l)
    return uniques


def identifiant(cid, ligne):
    """Chapitre + empreinte de la section, du contexte, de la PREMIERE ligne de l'allemand (la replique, le mot, la
    question) et du point : la mise en forme du reste (exemple, choix d'une question) peut changer sans changer l'id."""
    sect, ctx, de, fr, point = ligne
    tete = de.split("\n")[0]
    return "%s-%s" % (cid.split("_")[0], hashlib.sha1(("%s|%s|%s|%s" % (sect, ctx, tete, point)).encode("utf-8")).hexdigest()[:6])


def second_avis(cid):
    """{id: (verdict, correction, raison)} : la relecture croisee par un autre modele (pflege/relecture/second-avis/
    <chapitre>.txt, une ligne « id | VERDICT | correction | raison »). Ce n'est PAS l'avis d'une personne du metier :
    il dit a la soignante ou regarder d'abord."""
    p = os.path.join(SORTIE, "second-avis", cid + ".txt")
    avis = {}
    if os.path.exists(p):
        for ligne in open(p, encoding="utf-8").read().splitlines():
            parts = [x.strip() for x in ligne.split("|")]
            if len(parts) >= 4 and parts[1] in ("JUSTE", "CORRIGER", "NUANCER", "INCERTAIN"):
                avis[parts[0]] = (parts[1], parts[2], " | ".join(parts[3:]))
    return avis


def lot(c, donnees):
    plat = lambda t: " ".join(str(t or "").replace("|", "/").split())
    return ["%s | %s · %s | %s | %s | %s" % (identifiant(c["id"], l), l[0], plat(l[1]), plat(l[2]), plat(l[3]), plat(nettoyer(l[4])))
            for l in lignes_chapitre(c, donnees)]


GABARIT = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relecture ⚕️ · {titre}</title>
<style>
body{{font-family:system-ui,-apple-system,"Segoe UI",sans-serif; color:#1C2430; margin:24px; line-height:1.4;}}
h1{{font-size:22px; margin:0 0 4px;}} h2{{font-size:16px; margin:22px 0 6px; border-bottom:2px solid #E8A23A; padding-bottom:3px;}}
.chapeau{{font-size:13px; color:#3D4656; max-width:900px;}}
table{{width:100%; border-collapse:collapse; font-size:12.5px;}}
th,td{{border:1px solid #C9CED6; padding:6px 7px; vertical-align:top; text-align:start;}}
th{{background:#F2F4F7; font-weight:700;}}
td.de{{font-weight:600; white-space:pre-line;}} td.fr{{white-space:pre-line; color:#2E3A48;}}
td.point{{color:#7A4A06;}} td.ctx{{color:#5B6470; font-size:11.5px; width:12%;}}
.id{{font-family:ui-monospace,Consolas,monospace; font-size:10px; color:#8A93A0;}}
td.case{{width:5%; text-align:center; font-size:16px;}} td.corr{{width:18%;}}
.doute{{margin-top:5px; padding:4px 6px; border-left:3px solid #C9CED6; background:#F7F8FA; color:#1C2430; font-size:11.5px;}}
.doute.corriger{{border-left-color:#B3261E; background:#FDECEA;}} .doute.nuancer{{border-left-color:#E8A23A;}}
@media print{{body{{margin:10mm;}} h2{{break-after:avoid;}} tr{{break-inside:avoid;}}}}
</style></head><body>
<h1>Relecture ⚕️ · Chapitre {numero} : {titre} <span lang="de" style="font-weight:400; font-style:italic">({de})</span></h1>
<p class="chapeau">Wortando Pflege, la partie de l'app pour les soignants étrangers qui préparent le telc Deutsch B1·B2 Pflege.
Cette feuille ne contient que les phrases et les mots marqués ⚕️ : ce qui touche aux soins, aux valeurs cliniques ou aux
usages du service. Pour chaque ligne, cochez « juste » si l'allemand est ce qu'on dit et fait au service, ou « à corriger »
avec la bonne formulation. Le français n'est qu'une aide ; l'allemand est ce qui compte. {total} lignes.</p>
<p class="chapeau">Certaines lignes portent un encadré « Un premier lecteur… » : c'est une première relecture faite par un
programme, pas par une personne du métier. Elle montre où regarder d'abord et peut se tromper ; c'est votre avis qui décide.</p>
{sections}
</body></html>
"""


def feuille(c, donnees):
    lignes = lignes_chapitre(c, donnees)
    sections, ordre = {}, []
    for l in lignes:
        sect, ctx, de, fr, point = l
        if sect not in sections:
            sections[sect] = []
            ordre.append(sect)
        sections[sect].append((identifiant(c["id"], l), ctx, de, fr, point))
    corps, n = [], 0
    avis = second_avis(c["id"])
    LIBELLES = {"CORRIGER": "Un premier lecteur pense que c'est faux", "NUANCER": "Un premier lecteur nuance",
                "INCERTAIN": "Un premier lecteur n'a pas pu trancher"}
    for sect in ordre:
        rangs = []
        for ident, ctx, de, fr, point in sections[sect]:
            n += 1
            doute = ""
            if ident in avis and avis[ident][0] != "JUSTE":
                v, corr, raison = avis[ident]
                doute = '<div class="doute %s"><b>%s.</b> %s%s</div>' % (
                    v.lower(), e(LIBELLES[v]), e(raison),
                    (' <span lang="de">Proposition : « %s »</span>' % e(corr)) if corr else "")
            rangs.append('<tr><td class="ctx">%d · <span class="id">%s</span><br>%s</td><td class="de" lang="de">%s</td><td class="fr">%s</td><td class="point">%s%s</td>'
                         '<td class="case">☐</td><td class="case">☐</td><td class="corr"></td></tr>'
                         % (n, e(ident), e(ctx), e(de), e(fr), e(nettoyer(point)), doute))
        corps.append('<h2>%s (%d)</h2><table><tr><th>N°</th><th>Allemand</th><th>Français</th><th>Point à vérifier</th>'
                     '<th>Juste</th><th>À corriger</th><th>Correction</th></tr>%s</table>' % (e(sect), len(rangs), "".join(rangs)))
    page = GABARIT.format(titre=e(c["titre"]["fr"]), numero=c["numero"], de=e(c.get("de", "")), total=n,
                          sections="".join(corps) or "<p>Rien à relire dans ce chapitre.</p>")
    return page, n, {s: len(v) for s, v in sections.items()}


def bilan(chapitres, donnees):
    """pflege/relecture/SECOND-AVIS.md : ce que le second avis conteste, par chapitre, les corrections d'abord."""
    plat = lambda t: " ".join(str(t or "").split())
    out = ["# Second avis sur les ⚕️ : ce qu'il conteste", "",
           "Fichier DÉRIVÉ (`python pflege/outils/feuille_relecture.py --premiers`). Le second avis est une relecture",
           "croisée par un autre modèle, dans le rôle d'une infirmière allemande : ce n'est **pas** l'avis d'une personne",
           "du métier. Règle de la maison : on n'applique que les FAITS vérifiables ; le reste attend la soignante.",
           "Les réponses complètes sont dans `pflege/relecture/second-avis/<chapitre>.txt`.", ""]
    total = {}
    for c in chapitres:
        avis = second_avis(c["id"])
        if not avis:
            continue
        par_id = {identifiant(c["id"], l): l for l in lignes_chapitre(c, donnees)}
        compte = {}
        for v, _, _ in avis.values():
            compte[v] = compte.get(v, 0) + 1
            total[v] = total.get(v, 0) + 1
        out += ["## Chapitre %d : %s (%s)" % (c["numero"], c["titre"]["fr"], c.get("de", "")), "",
                "%d lignes relues : %s." % (len(avis), ", ".join("%s %d" % (k, compte[k]) for k in ("JUSTE", "NUANCER", "CORRIGER", "INCERTAIN") if k in compte)), ""]
        for verdict, titre in (("CORRIGER", "À corriger selon lui"), ("INCERTAIN", "Pas tranché"), ("NUANCER", "À nuancer")):
            lignes = [(i, a) for i, a in avis.items() if a[0] == verdict]
            if not lignes:
                continue
            out += ["### %s (%d)" % (titre, len(lignes)), ""]
            for i, (_, corr, raison) in lignes:
                l = par_id.get(i)
                ou = ("%s · %s" % (l[0], plat(l[1]))) if l else "ligne disparue depuis la relecture"
                de = plat(l[2].split("\n")[0])[:220] if l else ""
                out.append("- `%s` %s%s — %s%s" % (i, ou, (" : « %s »" % de) if de else "", raison,
                                                   (" **Proposition :** « %s »" % corr) if corr else ""))
            out.append("")
    if total:
        out[6:6] = ["**Au total : %s.**" % ", ".join("%s %d" % (k, total[k]) for k in ("JUSTE", "NUANCER", "CORRIGER", "INCERTAIN") if k in total), ""]
        with open(os.path.join(SORTIE, "SECOND-AVIS.md"), "w", encoding="utf-8", newline=chr(10)) as f:
            f.write(chr(10).join(out) + chr(10))


def main():
    chapitres = lire("chapitres.json")["chapitres"]
    themes = lire("themes.json")
    themes = themes if isinstance(themes, list) else themes["themes"]
    donnees = (lire("dialogues.json")["dialogues"], themes, lire("redemittel.json")["cartes"], lire("ecrit.json")["sujets"])
    if "--tous" in sys.argv:
        ids = [c["id"] for c in chapitres]
    elif "--premiers" in sys.argv:
        ids = PREMIERS
    else:
        ids = [a for a in sys.argv[1:] if not a.startswith("-") and a.startswith("ch")]
    dossier_lots = sys.argv[sys.argv.index("--lots") + 1] if "--lots" in sys.argv else None
    if dossier_lots:
        os.makedirs(dossier_lots, exist_ok=True)
    if not ids:
        print(__doc__)
        return 1
    os.makedirs(SORTIE, exist_ok=True)
    for cid in ids:
        c = next((x for x in chapitres if x["id"] == cid), None)
        if not c:
            print("chapitre inconnu :", cid)
            return 1
        page, n, detail = feuille(c, donnees)
        with open(os.path.join(SORTIE, cid + ".html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page)
        print("%-20s %3d lignes  %s" % (cid, n, detail))
        if dossier_lots:
            with open(os.path.join(dossier_lots, cid + ".txt"), "w", encoding="utf-8", newline=chr(10)) as f:
                f.write(chr(10).join(lot(c, donnees)) + chr(10))
    bilan(chapitres, donnees)
    return 0


if __name__ == "__main__":
    sys.exit(main())
