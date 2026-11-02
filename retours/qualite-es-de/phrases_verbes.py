# -*- coding: utf-8 -*-
"""Six phrases de verbes allemands qui enseignaient un AUTRE verbe, corrigees
avec l'accord de Jacques (2 nov. 2026, « Oui, corrige-les », transmis par le
chef d'orchestre). La voix de chaque phrase neuve est a refaire (Aurora, v2).

    python retours/qualite-es-de/phrases_verbes.py [--ecrire]

Quand le sens ne bouge pas (entsorgen, wirken, gucken), les traductions
restent ; sinon (lassen, luegen, blasen) elles sont reecrites dans les 9
langues. entsorgen vit aussi dans un chapitre de themes.json : meme phrase.
"""
import io
import json
import os
import sys

from commun import RACINE

PHRASES = [
    # (fichier verbe.json niveau, infinitif, temps, avant, apres, {langue: traduction} ou None, surlignage)
    ("B1", "entsorgen", "konjunktiv2", "Alte Batterien würde ich nie in den Hausmüll werfen.",
     "Alte Batterien würde ich nie im Hausmüll entsorgen.", None, None),
    ("B2", "wirken", "perfekt", "Seine Worte haben lange nachgewirkt.",
     "Seine Worte haben lange gewirkt.", None, None),
    ("B1", "gucken", "konjunktiv2", "Ich würde lieber ein Buch lesen als fernzugucken.",
     "Ich würde lieber ein Buch lesen als Fernsehen gucken.", None, None),
    ("A2", "lassen", "konjunktiv2", "Ich würde das nicht zulassen.",
     "Ich würde mein Auto zu Hause lassen.",
     {"fr": "Je laisserais ma voiture à la maison.", "en": "I would leave my car at home.",
      "tr": "Arabamı evde bırakırdım.", "uk": "Я залишив би машину вдома.",
      "fa": "ماشینم را در خانه می‌گذاشتم.", "ar": "كنت سأترك سيارتي في البيت.",
      "pt": "Eu deixaria meu carro em casa.", "pl": "Zostawiłbym samochód w domu.",
      "ru": "Я бы оставил машину дома."},
     'Ich würde <span class="hl-akkusativ">mein Auto</span> zu Hause lassen.'),
    ("A2", "lügen", "perfekt", "Sie hat mich nie angelogen.", "Sie hat nie gelogen.",
     {"fr": "Elle n'a jamais menti.", "en": "She has never lied.", "tr": "Hiç yalan söylemedi.",
      "uk": "Вона ніколи не брехала.", "fa": "او هرگز دروغ نگفته است.", "ar": "لم تكذب أبدًا.",
      "pt": "Ela nunca mentiu.", "pl": "Nigdy nie skłamała.", "ru": "Она никогда не лгала."}, None),
    ("B1", "blasen", "perfekt", "Der Wind hat das Laub weggeblasen.", "Der Wind hat stark geblasen.",
     {"fr": "Le vent a soufflé fort.", "en": "The wind blew hard.", "tr": "Rüzgâr sert esti.",
      "uk": "Вітер сильно дув.", "fa": "باد شدید وزیده است.", "ar": "هبّت الريح بقوة.",
      "pt": "O vento soprou forte.", "pl": "Wiatr mocno wiał.", "ru": "Ветер сильно дул."}, None),
]


def appliquer(v, temps, avant, apres, trad, hl, journal, ou):
    if v.get(temps) == apres:
        return
    if v.get(temps) != avant:
        raise SystemExit("REFUS %s : %r" % (ou, v.get(temps)))
    v[temps] = apres
    journal.append((ou + "." + temps, avant, apres))
    if trad:
        for l, t in trad.items():
            k = temps + "_" + l
            if k in v:
                journal.append((ou + "." + k, v[k], t))
                v[k] = t
    if temps + "Highlight" in v:
        nv = hl or apres
        journal.append((ou + "." + temps + "Highlight", v[temps + "Highlight"], nv))
        v[temps + "Highlight"] = nv


def main():
    j = []
    vb = json.load(io.open(os.path.join(RACINE, "verbe.json"), encoding="utf-8"))
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))
    for niv, inf, temps, av, ap, trad, hl in PHRASES:
        for i, v in enumerate(vb[niv]):
            if v["infinitif"] == inf:
                appliquer(v, temps, av, ap, trad, hl, j, "verbe.%s[%d]" % (niv, i))

        def chercher(o, ch):
            if isinstance(o, dict):
                if o.get("infinitif") == inf and o.get(temps) in (av, ap):
                    appliquer(o, temps, av, ap, trad, hl, j, "themes" + ch)
                for k, x in o.items():
                    chercher(x, ch + "." + k)
            elif isinstance(o, list):
                for i, x in enumerate(o):
                    chercher(x, "%s[%d]" % (ch, i))
        chercher(th, "")
    for ou, av, ap in j:
        print("%-60s %s" % (ou, ap))
    if "--ecrire" in sys.argv and j:
        for f, d in (("verbe.json", vb), ("themes.json", th)):
            with io.open(os.path.join(RACINE, f), "w", encoding="utf-8", newline="\n") as h:
                h.write(json.dumps(d, ensure_ascii=False, indent=2, separators=(",", ": ")) + "\n")
        print("ecrit.")


if __name__ == "__main__":
    main()
