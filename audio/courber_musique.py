# -*- coding: utf-8 -*-
"""Graver une courbe de niveau dans une musique, pour un episode precis.

    python audio/courber_musique.py --dans audio/musique/last-tram-prenzlauer-berg.mp3 --sortie audio/musique/last-tram-episode3.mp3 --duree 67.26 --montee 22.8,27.2,0.9 --montee 63.4,66.2,1.0

POURQUOI UNE PISTE DERIVEE ET NON DES OPTIONS DE LIGNE DE COMMANDE.

Jacques, 23 septembre 2026 : << tu peux mettre la musique un peu plus forte, et
peut-etre la monter un peu lorsque la cycliste passe, et une montee et une
descente a la fin ? >>

Le NIVEAU se regle dans ambiance.py, au troisieme champ de --musique. La
COURBE, non : une automation ecrite dans une ligne de commande ne se relit pas,
ne se verifie pas, et se reperd au premier remontage. Elle se grave donc une
fois dans un fichier, sous un nom qui dit a quel episode il appartient.

⚠️ OU PLACER LES MONTEES NE SE DEVINE PAS : CA SE MESURE. Une musique qui monte
   sur une narration allemande coute de la comprehension a quelqu'un qui
   decode la langue -- c'est le cours qu'on abime, pas juste le mixage. Les
   montees vont donc la ou AUCUN mot n'est dit, et cette liste se lit dans
   _montage-avatar/_plans.json, pas de memoire.

   Pour l'episode 3, mesure le 23 sept. : le plan 07 (23,39 -> 26,68) est
   declare MUET, et le plan 18 n'a que 2,77 s de narration sur 6,12 -- donc
   ~3,3 s sans un mot a la toute fin, la chute avec les bras en l'air. Ce sont
   exactement les deux endroits que Jacques avait choisis a l'oreille.

⚠️ ET LA DESCENTE FINALE EXISTE DEJA. ambiance.py applique un fondu de sortie
   de 1,5 s. Une montee qui tiendrait jusqu'a la fin se battrait avec lui : la
   courbe redescend donc a 1,0 AVANT que le fondu commence, et les deux
   s'enchainent au lieu de se contrarier.
"""
import argparse
import math
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    p = argparse.ArgumentParser(
        description="Graver une courbe de niveau dans une musique.")
    p.add_argument("--dans", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--duree", type=float, required=True,
                   help="la duree de l'episode, pour tailler la piste")
    p.add_argument("--montee", action="append", default=[],
                   help="DEBUT,FIN,GAIN[,RAMPE_IN[,RAMPE_OUT]] -- gain en "
                        "facteur d'amplitude ajoute au-dessus de 1,0 "
                        "(0.9 ~ +5,6 dB). Repetable.")
    p.add_argument("--rampe", type=float, default=0.8,
                   help="rampe par defaut, si la montee n'en precise pas")
    p.add_argument("--essai", action="store_true")
    a = p.parse_args()

    def chemin(c):
        return c if os.path.isabs(c) else os.path.join(RACINE, c)

    dans = chemin(a.dans)
    if not os.path.exists(dans):
        sys.exit("  introuvable : %s" % dans)

    termes = ["1"]
    for m in a.montee:
        ch = m.split(",")
        if len(ch) < 3 or len(ch) > 5:
            sys.exit("  --montee veut DEBUT,FIN,GAIN[,RAMPE_IN[,RAMPE_OUT]] : %s" % m)
        try:
            t0, t1, gain = float(ch[0]), float(ch[1]), float(ch[2])
        except ValueError:
            sys.exit("  --montee : trois nombres au moins (%s)" % m)
        if t1 <= t0:
            sys.exit("  --montee : la fin doit suivre le debut (%s)" % m)
        # ⚠️ LES DEUX RAMPES SE REGLENT SEPAREMENT, ET CE N'EST PAS UN LUXE.
        #    23 sept. 2026 : Jacques voulait la montee AVANT que la cycliste
        #    croise Mark, << comme pour preparer tout ca >>. La narration du
        #    plan 06 finit a 22,14 s et celle du plan 08 commence a 26,68 :
        #    il faut donc monter LENTEMENT dans le silence qui precede, et
        #    redescendre VITE avant que Mark parle. Une rampe symetrique
        #    obligeait a choisir entre les deux, et laissait la musique haute
        #    sous << Warum klingeln alle? >>.
        r_in = float(ch[3]) if len(ch) >= 4 else a.rampe
        r_out = float(ch[4]) if len(ch) == 5 else r_in
        marge = (t1 - t0) / 2.0
        r_in, r_out = min(r_in, marge), min(r_out, marge)
        # Deux rampes qui se multiplient : une qui monte, une qui descend.
        # clip() borne a [0,1], donc le terme vaut gain au plateau et 0 ailleurs.
        termes.append("%.3f*clip((t-%.3f)/%.3f,0,1)*clip((%.3f-t)/%.3f,0,1)"
                      % (gain, t0, r_in, t1, r_out))
        print("  montee : %6.2f -> %6.2f s   x%.2f au plateau  (+%.1f dB)   "
              "rampes %.2f / %.2f s   plateau %.2f -> %.2f"
              % (t0, t1, 1.0 + gain, 20.0 * math.log10(1.0 + gain),
                 r_in, r_out, t0 + r_in, t1 - r_out))
    expr = "+".join(termes)

    sortie = chemin(a.sortie)
    print("  duree  : %.2f s" % a.duree)
    print("  courbe : %s" % expr)
    if a.essai:
        print("\n  (essai -- rien n'a ete ecrit)")
        return

    # ⚠️ LES VIRGULES DE L'EXPRESSION DOIVENT ETRE ECHAPPEES. Dans un
    #    filtergraph, la virgule separe les filtres : clip(x,0,1) ecrit tel
    #    quel fait echouer ffmpeg avec un code de sortie qui n'explique rien.
    #    Mesure le 23 sept. 2026, un rendu perdu a le comprendre.
    echappe = expr.replace(",", "\\,")
    subprocess.run([
        "ffmpeg", "-loglevel", "error", "-y", "-i", dans,
        "-af", "atrim=0:%.3f,volume=%s:eval=frame" % (a.duree, echappe),
        "-c:a", "libmp3lame", "-b:a", "192k", sortie], check=True)
    print("\n  -> %s  (%.0f ko)" % (sortie, os.path.getsize(sortie) / 1024.0))


if __name__ == "__main__":
    main()
