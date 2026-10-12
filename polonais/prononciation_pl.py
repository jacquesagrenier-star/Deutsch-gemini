# -*- coding: utf-8 -*-
"""Les regles de prononciation pour le POLONAIS, pretes a poser dans tests/prononciation.py.

Ecrit CONTRE le polonais, pas traduit du francais : sch = sz, sp/st initiaux =
szp/szt, ch dur = le ch de « dach », ch doux = le ch de « Chiny », z = c, ei =
aj, eu = oj, et les pieges propres au Polonais : le r roule, l'absence de
longueur vocalique, les ti / di / si que le polonais adoucit. Bonne nouvelle a
dire : l'assourdissement final (Kind = « kint ») est le meme qu'en polonais.
Non relu par un natif.

POSE (phase 2, apres la fusion de l'arabe, une etape mecanique) dans
tests/prononciation.py :
  1. ajouter "pl" a LANGUES ;
  2. coller le dictionnaire PL ci-dessous a cote de PT ;
  3. dans construire(), a cote de « if rid in PT: », ajouter :
         if rid in PL:
             court = dict(court, pl=PL[rid][0])
             expl = dict(expl, pl=PL[rid][1])
  4. ajouter "traduction_pl" aux traductions recopiees dans les exemples ;
  5. python tests/prononciation.py --ecrire.

    python polonais/prononciation_pl.py     # controle : memes regles que PT, textes propres
"""
import io, os, re, sys

PL = {
 "u-trema": ("„i” z zaokrąglonymi ustami",
             "Polski nie ma tego dźwięku: powiedz „i” i, nie ruszając językiem, zaokrąglij usta jak do „u” albo do gwizdania: müde, Tür."),
 "o-trema": ("„e” z zaokrąglonymi ustami",
             "Tego dźwięku też nie ma w polskim: powiedz „e” jak w „ten” i, nie ruszając językiem, zaokrąglij usta jak do „o”."),
 "a-trema": ("jak polskie „e”",
             "ä wymawia się jak polskie „e” w „ten” czy „sen”: Käse, Mädchen."),
 "u": ("jak polskie „u”",
       "Niemieckie u to polskie „u” (albo „ó”): gut czyta się „gut”, Buch „buch”. Łatwe — trudny jest dopiero ü."),
 "ei": ("„aj”, jak w „kraj”",
        "ei czyta się „aj”, jak w „kraj”: Wein to „wajn”, klein „klajn”. Nigdy „ej”."),
 "ie": ("długie „i”",
        "ie to długie „i”, a e jest nieme: Liebe to „liibe”. Uwaga: przed i spółgłoski zostają twarde — die to „di”, Kino to „kino”, a nie „dzi” czy „ki” zmiękczone jak w polskim „siedem”."),
 "eu": ("„oj”, jak w „bój”",
        "eu i äu czyta się „oj”: heute to „hojte”, neu „noj”, Häuser „hojzer”."),
 "au": ("„au”, jak w „auto”",
        "au czyta się jak w polskim „auto”: Haus to „haus”, Frau „frau”. Nie wymawiaj go jak „ał”."),
 "longueur": ("samogłoska długa albo krótka",
              "Samogłoska jest długa przed h albo gdy jest podwojona (Tee, Sohn), a krótka przed podwójną spółgłoską (Bett, kommen). W polskim długość samogłosek nie istnieje; w niemieckim zmienia słowo: Staat / Stadt."),
 "sch": ("jak polskie „sz”",
         "sch to dokładnie polskie „sz”: Schule to „szule”, Tisch „tisz”."),
 "sp-st": ("„szp”, „szt” na początku słowa",
           "Na początku słowa (albo jego części) sp i st czyta się „szp” i „szt”: Straße to „sztrase”, sprechen „szprechen”, Bleistift „blajsztift”. W środku i na końcu słowa zostaje zwykłe s: Fenster, ist."),
 "ch-doux": ("jak „ch” w „Chiny”",
             "Po e, i, ä, ö, ü, ei, eu, l, n i r ch jest miękkie, z językiem przy podniebieniu — jak polskie „ch” w „Chiny” albo „chichot”: ich, Milch, leicht. Nie wymawiaj go twardo jak w „dach”."),
 "ch-dur": ("jak polskie „ch” w „dach”",
            "Po a, o, u i au ch jest twarde, z tyłu gardła — dokładnie jak polskie „ch” w „dach” czy „chata”: Nacht, Buch, Bauch."),
 "z": ("polskie „c”",
       "z (i tz) czyta się zawsze jak polskie „c”: Zeit to „cajt”, Katze „kace”, zehn „cen”. Nigdy jak polskie „z”."),
 "v": ("prawie zawsze „f”",
       "v czyta się prawie zawsze „f”: Vater to „fater”, viel „fil”. Kilka słów obcego pochodzenia zachowuje „w” (Vase, Klavier)."),
 "w": ("polskie „w”",
       "w to polskie „w”: Wasser to „waser”, wo „wo”. Bez niespodzianek."),
 "s": ("„z” przed samogłoską",
       "Przed samogłoską s czyta się jak polskie „z”: Sonne to „zone”, Hose „hoze”, sieben „ziben”. I nie zmiękczaj go: sie to twarde „zi”, a nie polskie „się”."),
 "eszett": ("ostre „s”",
            "ß i ss to ostre „s”, jak w „sam”. ß stoi po samogłosce długiej (groß), ss po krótkiej (essen)."),
 "j": ("polskie „j”",
       "j to polskie „j”: Jahr to „jar”, jung „jung”. Łatwe."),
 "h": ("lekki wydech na początku, nieme po samogłosce",
       "Na początku słowa albo sylaby h to lekki wydech, dużo słabszy niż polskie „h” czy „ch”: Hund, Haus. Po samogłosce się go nie wymawia, tylko wydłuża samogłoskę: gehen, Uhr."),
 "r": ("z tyłu gardła, nie toczone",
       "Niemieckie r robi się z tyłu gardła, jak przy płukaniu gardła — nie toczy się go czubkiem języka jak polskie „r”: rot, Brot. Toczone r zostanie zrozumiane, ale od razu zdradza akcent."),
 "pf": ("p + f naraz",
        "pf czyta się jako p i f za jednym razem; słychać oba: Apfel, Kopf, Pferd."),
 "er-final": ("lekkie „a”",
              "Na końcu słowa -er czyta się jak lekkie „a”, bez „r”: Vater ≈ „fata”, Mutter ≈ „muta”, besser ≈ „besa”."),
 "ig-final": ("„-ich” z miękkim ch",
              "Na końcu słowa -ig czyta się „-ich”, z miękkim ch jak w „Chiny”: richtig, billig, wenig."),
 "b-d-g-final": ("„p”, „t”, „k”",
                 "Na końcu słowa b, d i g tracą dźwięczność i brzmią jak p, t, k: Kind ≈ „kint”, Tag ≈ „tak”, gelb ≈ „gelp”. Tu polski ci pomaga: to dokładnie to samo co w „chleb” czy „ogród”."),
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = io.open(os.path.join(racine, "tests", "prononciation.py"), encoding="utf-8").read()
    ids = re.findall(r'^ \("([a-z0-9-]+)", "', src, re.M)
    fautes = []
    if set(ids) != set(PL):
        fautes.append("regles : manque %s, en trop %s" % (sorted(set(ids) - set(PL)), sorted(set(PL) - set(ids))))
    for rid, (court, expl) in PL.items():
        for t in (court, expl):
            if not t.strip() or "«" in t or "»" in t or re.search("[Ѐ-ӿ؀-ۿ]", t):
                fautes.append("%s : texte refuse %r" % (rid, t))
    for f in fautes:
        print("  FAUTE :", f)
    print("%d regles polonaises sur %d, %d faute(s)" % (len(PL), len(ids), len(fautes)))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
