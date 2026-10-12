# -*- coding: utf-8 -*-
"""Brouillon russe -> fichier de correction pour les exercices (exercices.json).

Version russe de .claude/russe/outils/exos_convertir.py (ecrit pour pt).

    python russe/outils/exos_convertir.py <brouillon.txt> <dossier_releve> <dossier_sortie>

Le releve <jeu>.txt vient de exos_dump.py (une ligne JSON par exercice a
traduire, dans l'ordre du jeu). Le brouillon est un texte, une ligne par
exercice, alignee PAR NUMERO sur le releve :

    jeu <nom du jeu>
    M<TAB><regex><TAB><remplacement>        (moules, appliques dans l'ordre)
    P<TAB><texte francais><TAB><russe>       (moule litteral, sans regex)
    <n><TAB><translation><TAB><explanation>[<TAB>cle=valeur]...

- n : rang dans le releve (0, 1, 2...) ; un trou ou un decalage est refuse.
- "-" : champ absent du releve ; "*" : fabrique a partir du FRANCAIS par les
  moules ; cle = hint, question, correct ou options (options en liste JSON).
- hint et question absents de la ligne valent "*" quand le jeu a des moules.

Garde-fous : un mot francais distinctif qui survit aux moules, un champ du
releve oublie, une liste d'options de mauvaise longueur, un caractere de
controle, et toute valeur russe sans lettre cyrillique (sauf tuiles
allemandes de correct/options) sont refuses.
"""
import io, json, os, re, sys

FRANCAIS = [" le ", " la ", " les ", "verbe", "personne", "avec ",
            "Avec ", " est ", " car ", " une ", " un ", " et ", " pas ",
            " se termine", " qui ", " dans ", " sur ", "masculin", "féminin",
            "neutre", "pluriel", "phrase", "Prétérit", "prétérit", " ici",
            "toujours", " donc ", "Nominatif", "Accusatif", "Datif", "Génitif",
            "fém.", "masc.", " à ", "comme ", " de ", " ou ", " en ",
            " ne ", " que ", " se ", " sans ", " pour ", " par ", " son ", " sa ",
            " ses ", " ce ", " cette ", "C'est", "c'est", "l'", "d'", "qu'", "n'",
            "Remets", " mots", "ordre"]  # pas " du ", " des ", " au " : allemand
CYR = re.compile("[А-Яа-яЁё]")


def fabriquer(fr, moules, ou):
    v = fr
    for motif, rempl in moules:
        v = re.sub(motif, rempl, v)
    return verifier(v, ou, fr)


def verifier(v, ou, fr=""):
    if any(ord(c) < 32 for c in v):
        sys.exit("CARACTERE DE CONTROLE dans %s : %r" % (ou, v))
    for m in FRANCAIS:
        if m in v:
            sys.exit("FRANCAIS RESTANT %r dans %s :\n   fr : %s\n   ru : %s" % (m, ou, fr, v))
    if not CYR.search(v):
        sys.exit("SANS CYRILLIQUE dans %s : %r" % (ou, v))
    return v


def main():
    src, rel_dir, out_dir = sys.argv[1:4]
    lignes = [l.rstrip("\n") for l in io.open(src, encoding="utf-8")]
    lignes = [l for l in lignes if l.strip() and not l.startswith("#")]
    if not lignes[0].startswith("jeu "):
        sys.exit("premiere ligne : jeu <nom>")
    jeu = lignes[0][4:].strip()
    moules, entrees_b = [], []
    for l in lignes[1:]:
        if l.startswith("M\t"):
            _, motif, rempl = l.split("\t")
            moules.append((motif, rempl))
        elif l.startswith("P\t"):
            _, fr, ru = l.split("\t")
            moules.append((re.escape(fr), ru.replace("\\", "\\\\")))
        else:
            entrees_b.append(l.split("\t"))
    releve = [json.loads(l) for l in io.open(os.path.join(rel_dir, jeu + ".txt"), encoding="utf-8") if l.strip()]
    if len(releve) != len(entrees_b):
        sys.exit("NOMBRE : releve %d, brouillon %d" % (len(releve), len(entrees_b)))
    entrees = []
    for n, (r, b) in enumerate(zip(releve, entrees_b)):
        if b[0] != str(n):
            sys.exit("DECALAGE : ligne %d porte le numero %r" % (n, b[0]))
        ou = "%s #%d %s" % (jeu, n, r["_q"][:40])
        ent = {"question": r["_q"]}
        if "_cle" in r:
            ent["cle_translation"] = r["_cle"]
        trad, expl = b[1], b[2]
        extras = {}
        for kv in b[3:]:
            k, v = kv.split("=", 1)
            extras[k] = json.loads(v) if v.startswith("[") else v
        if "translation" in r:
            if trad in ("-", "*"):
                sys.exit("TRADUCTION MANQUANTE " + ou)
            ent["translation_ru"] = verifier(trad, ou)
        elif trad != "-":
            sys.exit("TRADUCTION EN TROP " + ou)
        if "explanation" in r:
            ent["explanation_ru"] = (fabriquer(r["explanation"], moules, ou + " expl")
                                     if expl == "*" else verifier(expl, ou + " expl", r["explanation"]))
        elif expl != "-":
            sys.exit("EXPLICATION EN TROP " + ou)
        for k in ("hint", "question"):
            if k in r and k not in extras and moules:
                extras[k] = "*"
        for k, v in extras.items():
            if k not in r:
                sys.exit("CHAMP %s EN TROP %s" % (k, ou))
            if k in ("correct", "options"):
                fr = r[k]["fr"]
                if isinstance(fr, list):
                    if not isinstance(v, list) or len(v) != len(fr):
                        sys.exit("OPTIONS %s" % ou)
                    for x in v:
                        if any(ord(c) < 32 for c in x):
                            sys.exit("CONTROLE " + ou)
                ent[k + "Ru"] = v
            else:
                ent[k + "_ru"] = (fabriquer(r[k], moules, ou + " " + k) if v == "*"
                                  else verifier(v, ou + " " + k, r[k]))
        manque = [k for k in r if not k.startswith("_") and
                  (k + "_ru" not in ent and k + "Ru" not in ent)]
        if manque:
            sys.exit("CHAMP OUBLIE %s pour %s" % (manque, ou))
        entrees.append(ent)
    sortie = os.path.join(out_dir, "corr_" + jeu + ".json")
    io.open(sortie, "w", encoding="utf-8").write(
        json.dumps({"jeu": jeu, "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
    print("%s : %d entrees -> %s" % (jeu, len(entrees), sortie))


if __name__ == "__main__":
    main()
