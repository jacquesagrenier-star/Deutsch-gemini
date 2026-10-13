# -*- coding: utf-8 -*-
"""La tuile « Prononciation » de l'espagnol : les regles de lecture.

    python tests/prononciation_es.py            # controle seul
    python tests/prononciation_es.py --ecrire   # ecrit espanol/datos/prononciation.json

Le pendant de tests/prononciation.py (allemand, v755). Demande de Jacques,
11 oct. 2026 : « le faire et pour un Francais qui apprend l'espagnol, et pour
un Anglais ». Les deux n'ont pas les memes pieges -- le francophone doit
prononcer le e final (noche) et oublier ses nasales (tengo) ; l'anglophone
doit garder les voyelles pures (no « go-w »), taire le h, ne pas reduire les
voyelles en « uh ». Chaque explication est donc ecrite POUR sa langue.

L'interface de l'espagnol existe en francais et en anglais : deux langues.

LA VARIANTE. Une regle change de texte selon l'Espagne ou l'Amerique latine :
c / z (« th » a Madrid, « s » a Mexico). Elle porte « variantes » ; l'app
montre celle de l'usager (VARIANTE_ESPAGNOL) et la voix qui va avec
(Lolita ou Monica). Les autres regles nomment la difference quand il y en a
une (ll a Buenos Aires, j plus doux au Mexique) dans un texte commun.

LES EXEMPLES sont des mots du corpus, deja dits par les DEUX voix, et absents
de variantes.json : un mot que l'Amerique latine remplace ne s'entendrait
pas tel qu'il est ecrit sur la carte.
"""
import hashlib, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
LANGUES = ("fr", "en", "pt")


def guillemets(t):
    """« x » -> “x” : l'anglais n'emploie pas les chevrons."""
    return re.sub(r"«\s*(.*?)\s*»", "“\\1”", t)


def L(fr, en):
    return {"fr": fr, "en": guillemets(en)}


# (id, graphie, api, court, explication, exemples[, variantes])
VOYELLES = [
 ("voyelles", "a · e · i · o · u", "[a e i o u]",
  L("cinq voyelles, toujours entières", "five pure vowels"),
  L("Cinq voyelles, toujours prononcées de la même façon et en entier : a, e (« é »), i, o, u (« ou »). Jamais muettes, jamais nasales.",
    "Five vowels, always pronounced the same way and in full: a « ah », e « eh », i « ee », o « oh », u « oo ». No gliding (o is not the « oh-w » of « go »), and never reduced to « uh »."),
  ["casa", "mesa", "libro"]),
 ("u", "u", "[u]",
  L("toujours « ou »", "always « oo »"),
  L("Le u se dit toujours « ou » : luna se dit « louna ». Jamais le « u » français.",
    "u is always « oo »: luna sounds like « loo-na », never « you »."),
  ["luna", "uva", "fruta"]),
 ("e-final", "-e", "[e]",
  L("le e final se prononce", "final e is pronounced"),
  L("Le e se prononce toujours, même à la fin du mot : noche se dit « notché », grande « grandé ». Le piège du francophone : le laisser muet.",
    "e is always pronounced, even at the end of a word: noche sounds like « no-cheh », grande like « grahn-deh ». It is never silent as in « come »."),
  ["noche", "leche", "grande"]),
 ("sans-nasale", "an · en · in · on · un", "[an] [en]",
  L("pas de nasales : la voyelle, puis le n", "the vowel, then a real n"),
  L("Pas de voyelles nasales : dans pan, también, cinco, on dit la voyelle PUIS le n, comme dans « Anne » : « pann », « tam-bién ». Jamais « pain » ni « tambien » à la française.",
    "Before n, the vowel stays pure and the n is fully pronounced: pan « pahn », también « tahm-byen ». Don't let the vowel turn into « uh »."),
  ["pan", "también", "cinco"]),
 ("diphtongues", "ue · ie", "[we] [je]",
  L("deux voyelles d'un seul coup", "two vowels in one beat"),
  L("Deux voyelles ensemble se disent d'un seul coup : bueno « boué-no », tiempo « tiém-po », nuevo « noué-vo ».",
    "Two vowels together are said in one beat: bueno « bweh-no », tiempo « tyem-po », nuevo « nweh-vo »."),
  ["bueno", "tiempo", "nuevo"]),
]

CONSONNES = [
 ("c-z", "ce · ci · z", "[θ] · [s]",
  L("selon la variante", "depends on the variety"),
  L("Devant e ou i, le c — et le z partout — se dit « th » en Espagne et « s » en Amérique latine.",
    "Before e or i, c — and z everywhere — is « th » in Spain and « s » in Latin America."),
  ["cielo", "zapato", "cerveza"],
  {"es": {
     "court": L("comme le « th » anglais", "« th » as in think"),
     "explication": L("En Espagne, devant e ou i, le c — et le z partout — se dit comme le « th » anglais de « think », la langue entre les dents : cielo « thiélo », zapato « thapato ». L'Amérique latine dit « s » : les deux sont corrects.",
                      "In Spain, before e or i, c — and z everywhere — is « th » as in « think », tongue between the teeth: cielo « thyeh-lo », zapato « tha-pa-to ». Latin America says « s »: both are correct.")},
   "latam": {
     "court": L("« s »", "« s »"),
     "explication": L("En Amérique latine, devant e ou i, le c — et le z partout — se dit « s » : cielo « siélo », zapato « sapato ». En Espagne on dit « th » : les deux sont corrects.",
                      "In Latin America, before e or i, c — and z everywhere — is « s »: cielo « syeh-lo », zapato « sa-pa-to ». Spain says « th »: both are correct.")}}),
 ("c-qu", "ca · co · cu · que · qui", "[k]",
  L("toujours « k »", "always « k »"),
  L("ca, co, cu se disent « ka, ko, kou ». Devant e et i, on écrit qu et le u ne s'entend pas : queso « késo », aquí « aki ».",
    "ca, co, cu are « ka, ko, koo ». Before e and i, Spanish writes qu and the u is silent: queso « keh-so », aquí « ah-kee »."),
  ["casa", "queso", "aquí"]),
 ("j", "j · ge · gi", "[x]",
  L("raclé au fond de la gorge", "a strong h, like Scottish loch"),
  L("Le j, et le g devant e ou i, est un raclement au fond de la gorge, comme un « r » français soufflé : jamón, gente. Au Mexique, il est plus doux, presque un « h » soufflé.",
    "j, and g before e or i, is a rasp in the throat like the « ch » of Scottish « loch » — a strong, breathy h: jamón, gente. In Mexico it is softer, close to an English h."),
  ["jamón", "ojo", "gente"]),
 ("g-gu", "ga · go · gu · gue · gui", "[g]",
  L("g dur ; gue, gui : u muet", "hard g; in gue, gui the u is silent"),
  L("ga, go, gu ont un g dur, comme « gare ». Devant e et i, on écrit gu et le u ne s'entend pas : guerra « guérra ». Le tréma le fait entendre : bilingüe « bi-lin-goué ».",
    "ga, go, gu have a hard g as in « go ». Before e and i, Spanish writes gu and the u is silent: guerra « geh-rra ». A diaeresis makes it heard: bilingüe « bee-leen-gweh »."),
  ["gato", "guerra", "bilingüe"]),
 ("ch", "ch", "[tʃ]",
  L("« tch »", "« ch » as in church"),
  L("ch se dit « tch » : noche « notché », ocho « otcho ». Jamais le « ch » français de « chat ».",
    "ch is « ch » as in « church »: noche « no-cheh », ocho « o-cho »."),
  ["noche", "ocho", "chico"]),
 ("ll-y", "ll · y", "[ʝ]",
  L("comme « y »", "« y » as in yes"),
  L("ll et y se disent comme le « y » de « yeux » : calle « caïé », playa « plaïa ». En Argentine et en Uruguay, on entend plutôt « ch » : calle « caché ».",
    "ll and y sound like « y » in « yes »: calle « ka-yeh », playa « pla-ya ». In Argentina and Uruguay you will hear « sh » instead: « ka-sheh »."),
  ["calle", "playa", "llave"]),
 ("n-tilde", "ñ", "[ɲ]",
  L("« gn »", "« ny » as in canyon"),
  L("ñ se dit « gn », comme dans « montagne » : niño « nigno », mañana « magnana ».",
    "ñ is « ny » as in « canyon »: niño « nee-nyo », mañana « ma-nya-na »."),
  ["niño", "mañana", "año"]),
 ("h", "h", "—",
  L("muet, comme en français", "always silent"),
  L("Le h ne se prononce jamais, exactement comme en français : hoy « oï », hermano « ermano ».",
    "h is always silent: hoy sounds like « oy », hermano like « er-ma-no ». Never breathe it as in « house »."),
  ["hoy", "hermano", "hora"]),
 ("r-rr", "r · rr", "[ɾ] · [r]",
  L("roulé, jamais dans la gorge", "tapped, or rolled"),
  L("Un r entre deux voyelles est un seul battement du bout de la langue (caro). En début de mot, ou écrit rr, il est roulé plusieurs fois (rojo, perro). Pas de « r » de gorge à la française : caro et carro ne veulent pas dire la même chose.",
    "A single r between vowels is one quick tap of the tongue, like the « tt » of American « butter » (caro). At the start of a word, or written rr, it is rolled (rojo, perro). Caro and carro are different words."),
  ["caro", "rojo", "perro"]),
 ("b-v", "b · v", "[b]",
  L("b et v : le même son", "b and v sound the same"),
  L("b et v se prononcent exactement pareil : un « b » en début de mot (vino « bino »), un b très doux, les lèvres à peine fermées, entre deux voyelles (uva).",
    "b and v sound exactly the same: a « b » at the start of a word (vino « bee-no »), and a very soft b, lips barely touching, between vowels (uva)."),
  ["vino", "beber", "uva"]),
 ("d", "d", "[ð]",
  L("doux entre deux voyelles", "soft between vowels"),
  L("Entre deux voyelles et en fin de mot, le d est très doux, presque le « th » anglais de « this » : cansado, nada, ciudad.",
    "Between vowels and at the end of a word, d is very soft, like « th » in « this »: cansado, nada, ciudad."),
  ["cansado", "nada", "ciudad"]),
 ("s", "s", "[s]",
  L("toujours « ss », jamais « z »", "always « s », never « z »"),
  L("Le s se dit toujours « ss », même entre deux voyelles : casa « cassa », rosa « rossa ». Le « z » français de « maison » n'existe pas en espagnol.",
    "s is always a hissing « s », never « z », even between vowels: casa « ka-sa », rosa « ro-sa »."),
  ["casa", "mesa", "rosa"]),
]

ACCENT = [
 ("accent", "á · é · í · ó · ú", "ˈ",
  L("une syllabe plus forte", "one stressed syllable"),
  L("Chaque mot a une syllabe plus forte. Mot terminé par une voyelle, n ou s : l'avant-dernière (casa, hablan). Autre consonne : la dernière (ciudad, hablar). Sinon, l'accent écrit la montre (café, médico, canción). Le piège du francophone : mettre la force à la fin, comme en français.",
    "Every word has one stressed syllable. Ending in a vowel, n or s: the second-to-last (casa, hablan). Any other consonant: the last (ciudad, hablar). Otherwise the written accent shows it (café, médico, canción)."),
  ["médico", "canción", "café", "ciudad"]),
]

# LE PORTUGAIS DU BRESIL (13 oct. 2026), ecrit CONTRE le portugais et non traduit
# du francais : le lusophone a deja les cinq voyelles pleines, le r roule
# (caro / carro) et le lh ~ ll ; ses pieges a lui sont le e et le o fermes ou
# nasalises, le s sonore entre voyelles (casa), le j et le ch a la francaise,
# le d et le t palatalises (dia -> « djia »), et le b / v distingues.
# Cle = id de la regle ; « c-z.es » et « c-z.latam » pour les variantes.
PT = {
 "voyelles": ("cinco vogais, sempre inteiras e abertas",
              "Cinco vogais, sempre pronunciadas do mesmo jeito e por inteiro: a, e, i, o, u. Nunca mudas, nunca nasais — e nunca o e e o o fechados do português: pelo se diz « pé-lo », com e aberto."),
 "u": ("sempre « u », nunca mudo",
       "O u se diz sempre « u » e sempre se ouve: luna, « lu-na ». Diferente do português, não há u mudo depois de q e g — em que e gue, só o u escrito com trema (ü) se pronuncia."),
 "e-final": ("o e final é um e aberto, nunca « i »",
             "O e se pronuncia sempre, e com som de é, mesmo no fim da palavra: noche se diz « nó-tchê », grande « gran-dê ». A armadilha do brasileiro: transformar esse e final em i (« nochi », « grandi »)."),
 "sans-nasale": ("sem nasais: a vogal, depois o n",
                 "Nada de vogais nasais: em pan, también, cinco, diz-se a vogal e DEPOIS o n, com a língua no céu da boca — « pann », « tam-bién ». Nunca o « pão » nem o « tambêm » do português."),
 "diphtongues": ("duas vogais de uma vez só",
                 "Duas vogais juntas se dizem de uma vez só: bueno « bué-no », tiempo « tiém-po », nuevo « nué-vo » — como em português « quase », « série »."),
 "c-z": ("depende da variante",
         "Antes de e ou i, o c — e o z em qualquer posição — se diz « th » na Espanha e « s » na América Latina."),
 "c-z.es": ("como o « th » inglês de « think »",
            "Na Espanha, antes de e ou i, o c — e o z em qualquer posição — se diz com a língua entre os dentes, como o « th » inglês de « think »: cielo « thié-lo », zapato « tha-pa-to ». A América Latina diz « s »: as duas formas são corretas."),
 "c-z.latam": ("« s »",
               "Na América Latina, antes de e ou i, o c — e o z em qualquer posição — se diz « s »: cielo « sié-lo », zapato « sa-pa-to ». Na Espanha diz-se « th »: as duas formas são corretas."),
 "c-qu": ("sempre « k »",
          "ca, co, cu se dizem « ka, ko, ku ». Antes de e e i escreve-se qu e o u não se ouve: queso « ké-so », aquí « a-ki » — como em português « quero », « aqui »."),
 "j": ("raspado no fundo da garganta",
       "O j, e o g antes de e ou i, é um raspar no fundo da garganta, como o rr carioca ou o r de « rato »: jamón, gente. Nunca o j do português (« já », « gente »). No México é mais suave, quase um h aspirado."),
 "g-gu": ("g duro; gue, gui: u mudo",
          "ga, go, gu têm g duro, como em « gato ». Antes de e e i escreve-se gu e o u não se ouve: guerra « gué-rra » — como em português. O trema o faz soar: bilingüe « bi-lin-güe »."),
 "ch": ("« tch »",
        "ch se diz « tch », como o « tch » de « tchau »: noche « nó-tchê », ocho « ó-tcho ». Nunca o ch do português (« chave »)."),
 "ll-y": ("como o « i » de « ioga »",
          "ll e y se dizem como o i de « ioga »: calle « ca-ie », playa « pla-ia ». Não é o lh do português. Na Argentina e no Uruguai ouve-se « ch » ou « j »: calle « ca-che »."),
 "n-tilde": ("« nh »",
             "ñ se diz como o nh do português, em « manhã »: niño « ni-nho », mañana « ma-nha-na »."),
 "h": ("mudo, como em português",
       "O h nunca se pronuncia, exatamente como em português: hoy « ói », hermano « er-ma-no »."),
 "r-rr": ("vibrado com a ponta da língua, nunca na garganta",
          "Um r entre duas vogais é uma só batida da ponta da língua, como o r de « caro » em português. No início da palavra, ou escrito rr, é vibrado várias vezes com a ponta da língua (rojo, perro) — nunca o rr de garganta do Rio ou o r aspirado: caro e carro não querem dizer a mesma coisa."),
 "b-v": ("b e v: o mesmo som",
         "b e v se pronunciam exatamente igual: um « b » no início da palavra (vino « bi-no »), um b muito suave, com os lábios mal fechados, entre duas vogais (uva). O v do português não existe em espanhol."),
 "d": ("suave entre vogais, nunca « dj »",
       "Entre duas vogais e no fim da palavra, o d é muito suave, quase o « th » inglês de « this »: cansado, nada, ciudad. E antes de i nunca vira « dj » como no Brasil: día se diz « di-a », não « djia »."),
 "s": ("sempre « ss », nunca « z »",
       "O s se diz sempre « ss », mesmo entre duas vogais: casa « ca-ssa », rosa « ró-ssa ». O s sonoro do português (« casa » com som de z) não existe em espanhol."),
 "accent": ("uma sílaba mais forte",
            "Cada palavra tem uma sílaba mais forte. Palavra terminada em vogal, n ou s: a penúltima (casa, hablan). Outra consoante: a última (ciudad, hablar). Senão, o acento escrito a mostra (café, médico, canción). As regras são parecidas com as do português; nos monossílabos, o acento serve para distinguir (más / mas, sí / si, él / el)."),
}

GROUPES = [("voyelles", VOYELLES), ("consonnes", CONSONNES), ("accent", ACCENT)]


def corpus():
    """mot espagnol -> son entree (ses traductions), du plus bas niveau au plus haut."""
    idx = {}
    def ch(n):
        return json.load(io.open(os.path.join(DATOS, n), encoding="utf-8"))
    for t in sorted(ch("temas.json")["themes"], key=lambda t: t.get("niveau", "")):
        for m in t["mots"]:
            idx.setdefault(m["mot"], m)
    for f, k in (("verbos.json", "infinitif"), ("adjetivos.json", "mot"), ("adverbios.json", "mot"),
                 ("expresiones.json", "mot"), ("funcionales.json", "mot")):
        d = ch(f)
        for n in sorted(d):
            for x in d[n]:
                idx.setdefault(x[k], x)
    return idx


def construire():
    idx = corpus()
    remplaces = set(json.load(io.open(os.path.join(DATOS, "variantes.json"), encoding="utf-8")).get("noms", {}))
    fautes, ids, out = [], set(), []
    for gid, regles in GROUPES:
        g = {"id": gid, "regles": []}
        for regle in regles:
            rid, graphie, api, court, expl, exemples = regle[:6]
            variantes = regle[6] if len(regle) > 6 else None
            # Le portugais vient de PT, ecrit contre le portugais (13 oct. 2026).
            if rid in PT:
                court = dict(court, pt=PT[rid][0])
                expl = dict(expl, pt=PT[rid][1])
            if variantes:
                variantes = {v: {"court": dict(t["court"], pt=PT[rid + "." + v][0]),
                                 "explication": dict(t["explication"], pt=PT[rid + "." + v][1])}
                             for v, t in variantes.items()}
            if rid in ids:
                fautes.append("id en double : " + rid)
            ids.add(rid)
            textes = [("court", court), ("explication", expl)]
            if variantes:
                for v, t in variantes.items():
                    textes += [("%s.court" % v, t["court"]), ("%s.explication" % v, t["explication"])]
            for nom, v in textes:
                manque = [l for l in LANGUES if not v.get(l)]
                if manque:
                    fautes.append("%s / %s : manque %s" % (rid, nom, manque))
            ex = []
            for mot in exemples:
                e = idx.get(mot)
                h = hashlib.sha1(mot.encode("utf-8")).hexdigest()[:16]
                if not e:
                    fautes.append("%s : « %s » absent du corpus (pas de traduction)" % (rid, mot))
                    continue
                if mot in remplaces:
                    fautes.append("%s : « %s » change en Amerique latine (variantes.json)" % (rid, mot))
                for voix in ("es-es", "es-419"):
                    if not os.path.exists(os.path.join(RACINE, "audio", "mp3", voix, h + ".mp3")):
                        fautes.append("%s : « %s » sans voix %s" % (rid, mot, voix))
                ex.append({"mot": mot, **{c: e[c] for c in ("traduction", "traduction_en", "traduction_pt") if e.get(c)}})
            if len(ex) < 2:
                fautes.append("%s : moins de deux exemples" % rid)
            r = {"id": rid, "graphie": graphie, "api": api, "court": court, "explication": expl, "exemples": ex}
            if variantes:
                r["variantes"] = variantes
            g["regles"].append(r)
        out.append(g)
    return {"_note": "Fichier DERIVE : python tests/prononciation_es.py --ecrire. Ne pas modifier a la main.",
            "groupes": out}, fautes


def main():
    d, fautes = construire()
    n = sum(len(g["regles"]) for g in d["groupes"])
    for f in fautes:
        print("  FAUTE :", f)
    print("%d regles, %d exemples, %d faute(s)" % (n, sum(len(r["exemples"]) for g in d["groupes"] for r in g["regles"]), len(fautes)))
    if fautes:
        sys.exit(1)
    chemin = os.path.join(DATOS, "prononciation.json")
    if "--ecrire" in sys.argv:
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print("ecrit :", chemin)
    elif os.path.exists(chemin):
        actuel = json.load(io.open(chemin, encoding="utf-8"))
        print("prononciation.json %s" % ("a jour" if actuel == d else "EN RETARD -- relancer avec --ecrire"))


if __name__ == "__main__":
    main()
