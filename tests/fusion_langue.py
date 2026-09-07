# -*- coding: utf-8 -*-
"""Verse un lot de traductions d'interface dans le bloc I18N d'index.html.

    python tests/fusion_langue.py --langue fa --lot lot1.json

Le fichier de lot est un objet JSON {cle: texte}. Le bloc de la langue est cree
s'il n'existe pas, sinon complete -- une cle deja presente est REMPLACEE.

⚠️ IL RELIT CE QU'IL VIENT D'ECRIRE. Apres l'ecriture, le bloc est re-extrait
par `node tests/i18n_dump.js` et chaque chaine est comparee a ce qui etait
demande. Une apostrophe mal echappee casse le bloc entier, et verifier.py ne le
voit pas : il ne parse pas le JavaScript. C'est la lecon de l'ukrainien.
"""
import argparse, io, json, os, re, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(RACINE, "index.html")

def relire(langue):
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "i18n_dump.js")],
                       capture_output=True, cwd=RACINE)
    if r.returncode:
        sys.exit("node n'a pas pu evaluer le bloc I18N :\n" + r.stderr.decode("utf-8", "replace")[:800])
    return json.loads(r.stdout.decode("utf-8")).get(langue, {})

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", required=True)
    ap.add_argument("--lot", required=True)
    ap.add_argument("--apres", default=None, help="code de la langue apres laquelle inserer le bloc")
    a = ap.parse_args()

    lot = json.load(io.open(a.lot, encoding="utf-8"))
    s = io.open(INDEX, encoding="utf-8").read()

    entete = "\n    %s: {" % a.langue
    if entete in s:
        # Bloc existant : on insere les cles juste apres l'entete.
        pos = s.index(entete) + len(entete)
        deja = relire(a.langue)
        neuves = {k: v for k, v in lot.items() if k not in deja}
        remplacees = {k: v for k, v in lot.items() if k in deja and deja[k] != v}
        for k in remplacees:
            # Retire l'ancienne ligne de la cle, ou qu'elle soit dans le bloc.
            fin = s.index("\n    }", pos)
            avant, dedans = s[:pos], s[pos:fin]
            dedans = re.sub(r"\n        %s: (\"(\.|[^\"\])*\"|'(\.|[^'\])*'),"
                            % re.escape(k), "", dedans)
            s = avant + dedans + s[fin:]
        a_ecrire = dict(neuves); a_ecrire.update(remplacees)
    else:
        # NOUVEAU BLOC : insere JUSTE AVANT la fermeture de I18N, et non
        # « apres le bloc precedent ».
        #
        # ⚠️ LE DERNIER BLOC DE LANGUE SE FERME SANS VIRGULE : une accolade
        # a quatre espaces, puis "};". Chercher la fermeture AVEC une virgule
        # pour se placer derriere lui tombe donc sur une accolade SANS AUCUN
        # RAPPORT, 1 150 lignes plus bas, et le bloc atterrit hors de I18N.
        # C'est arrive au premier essai, et seule la relecture l'a vu : node
        # relit ce que le navigateur lirait, la ou une expression reguliere
        # avait ecrit un bloc parfaitement forme au mauvais endroit.
        deb = s.index('const I18N = {')
        fin = s.index(chr(10) + '};', deb)
        avant = s[:fin].rstrip()
        if not avant.endswith(','): avant += ','   # virgule du bloc precedent
        s = avant + (chr(10) + '    %s: {' + chr(10) + '    }') % a.langue + s[fin:]
        pos = s.index(entete) + len(entete)
        a_ecrire = dict(lot)

    lignes = "".join('\n        %s: %s,' % (k, json.dumps(v, ensure_ascii=False))
                     for k, v in a_ecrire.items())
    s = s[:pos] + lignes + s[pos:]
    io.open(INDEX, "w", encoding="utf-8", newline="\n").write(s)

    # --- La relecture, seul controle qui vaille ---------------------------
    apres_ecriture = relire(a.langue)
    ecarts = [k for k, v in lot.items() if apres_ecriture.get(k) != v]
    print("%d cles versees en %s ; le bloc en compte %d"
          % (len(lot), a.langue, len(apres_ecriture)))
    if ecarts:
        print("⚠️ %d ECARTS entre ce qui etait demande et ce qui est ecrit :" % len(ecarts))
        for k in ecarts[:10]:
            print("   %s\n     demande : %r\n     relu    : %r" % (k, lot[k], apres_ecriture.get(k)))
        sys.exit(1)
    print("relecture : les %d chaines sont identiques a ce qui etait demande." % len(lot))

if __name__ == "__main__":
    main()
