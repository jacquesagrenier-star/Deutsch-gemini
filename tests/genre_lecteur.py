# -*- coding: utf-8 -*-
"""Le lecteur n'a pas de genre (lot 89, 13 nov. 2026) : en polonais, russe et ukrainien, l'app ne
s'adresse jamais a la personne qui apprend au masculin seul (« pomyliłeś », « ты ошибся », « ти помилився »).

Ces trois langues accordent le passe et l'adjectif au genre de « tu ». Une consigne, un bilan, une
etiquette dite par le lecteur (« Ce que j'ai entendu »), une replique de Mark ou d'Anna adressee au
candidat ne savent pas qui lit : on y prend une tournure neutre (present, impersonnel, nom), ou la forme
double deja employee par l'interface polonaise (« pomyliłeś/aś »).

Ce qui reste juste : ce que dit Mark de lui-meme (« Я бы сказал », « я провёл », « Mógłbym »), les
reponses modeles qui suivent le genre de l'allemand (Krankenpfleger -> медбрат), les tiers (« он сказал »).
Le detecteur ne lit pas le sens : il SIGNALE, et ce qui est juste malgre lui s'ecrit dans
tests/genre_lecteur_acceptes.txt avec sa raison.

    python tests/genre_lecteur.py            controle des fichiers du lot (telc/langues, index.html) ; code 1
                                             s'il reste un signalement non accepte
    python tests/genre_lecteur.py --tout     tous les fichiers servis (mesure, ne compte pas pour le code)
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "publication"))
ACCEPTES = os.path.join(RACINE, "tests", "genre_lecteur_acceptes.txt")
PERIMETRE = ["index.html"] + ["visuel/prototype/telc/langues/%s.json" % lg for lg in ("pl", "ru", "uk")]

CYR = "а-яА-ЯіїєґІЇЄҐёЁʼ'"
W = "[" + CYR + "]"
# Forme double deja ecrite : « видел(а) », « бачив(-ла) », « написав(ла) » -- neutre, pas un defaut.
DOUBLE = r"(?!\(|\s*\(\s*-?\s*(?:а|ла|лася|лась|ась|ася)\s*\))"

# Passes qui n'en sont pas (noms, adverbes) : ils finissent comme un passe masculin.
NON_VERBES = {
    "смысл", "глагол", "раздел", "бокал", "пол", "стол", "зал", "сигнал", "материал", "балл", "уровень",
    "текстов", "слов", "мысл", "фестивал", "интервал", "журнал", "канал", "вокзал", "штрафов", "пунктов",
    "балів", "пунктів", "разів", "слів", "батьків", "текстів", "листів", "днів", "років", "уроків", "учнів",
    "колів", "вів", "лев", "нав", "готов", "здоров", "часів", "речень", "правил", "питань", "відповідей",
    "варіантів", "завдань", "хвилин", "кроків", "вправ", "прикладів", "дієслів", "іменників", "звуків",
    "людей", "друзів", "колег", "предметів", "місяців", "тижнів", "етапів", "рівнів", "кольорів", "дітей",
    "голосів", "островів", "фактів", "символів", "знаків", "номерів", "пасажирів", "зошитів", "лікарів",
    "ти", "тобі", "тебе", "сам", "лекторів", "відтінків", "абзаців", "аркушів", "склад",
}

REGLES = {
    "pl": [
        re.compile(r"\b\w+(łeś|łbyś)\b(?!\s*(/|\(|-)\s*-?\w*aś)", re.I),
        re.compile(r"\b(jesteś|byłeś|będziesz|czujesz się|zostałeś)\s+(sam|gotowy|gotów|pewny|pewien|zadowolony|"
                   r"zmęczony|chory|zdrowy|ciekawy|przygotowany|dumny|smutny|szczęśliwy|zajęty|wolny)\b"
                   r"(?!\s*\(\s*-?\s*a\s*\)|\s*/\s*-?\w*a\b)", re.I),
    ],
    "ru": [
        re.compile(r"\b(ты|тебе|тебя)\b(?:(?!\b(он|она|оно|они|я|мы|кто)\b)[^.!?…:;])*?\b(" + W + r"{2,}(?:л|лся|ёл))\b" + DOUBLE, re.I),
        re.compile(r"\b(" + W + r"{2,}(?:л|лся|ёл))\b" + DOUBLE + r"\s+(?:бы\s+)?ты\b", re.I),
        re.compile(r"\b(ты|будь)\s+(?:бы\s+)?(сам|готов|уверен|прав|должен|рад|согласен|один|внимателен|осторожен|"
                   r"способен|свободен|доволен|знаком)\b" + DOUBLE, re.I),
    ],
    "uk": [
        re.compile(r"\b(ти|тобі|тебе)\b(?:(?!\b(він|вона|воно|вони|я|ми|хто)\b)[^.!?…:;])*?\b(" + W + r"{2,}(?:в|вся))\b" + DOUBLE, re.I),
        re.compile(r"\b(" + W + r"{2,}(?:в|вся))\b" + DOUBLE + r"\s+(?:би?\s+)?ти\b", re.I),
        re.compile(r"\b(ти|будь)\s+(?:би?\s+)?(сам|готовий|впевнений|правий|повинен|радий|згоден|один|уважний|"
                   r"обережний|вільний|задоволений|знайомий)\b" + DOUBLE, re.I),
        re.compile(r"\b(Молодець|Добре|Браво),?\s+що\s+(" + W + r"+(?:в|вся))\b" + DOUBLE, re.I),
    ],
}


def langue(texte):
    if re.search("[ąćęłńśźż]", texte, re.I):
        return "pl"
    if re.search("[іїєґ]", texte, re.I):
        return "uk"
    if re.search("[ыэъё]", texte, re.I):
        return "ru"
    if re.search("[а-я]", texte, re.I):
        return "ru/uk"
    return None


def signalements(texte):
    """[(langue, forme)] des formes masculines adressees au lecteur dans un texte."""
    lg = langue(texte)
    if not lg:
        return []
    trouves = []
    for l in (["ru", "uk"] if lg == "ru/uk" else [lg]):
        for regle in REGLES[l]:
            for m in regle.finditer(texte):
                mots = [g for g in m.groups() if g]
                dernier = mots[-1].lower() if mots else m.group(0).lower()
                if dernier in NON_VERBES or dernier.split()[-1] in NON_VERBES:
                    continue
                trouves.append((l, m.group(0)))
    return trouves


def chaines_json(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from chaines_json(v)
    elif isinstance(o, list):
        for v in o:
            yield from chaines_json(v)


LITTERAL = re.compile(r'"((?:[^"\\\n]|\\.)*)"|\'((?:[^\'\\\n]|\\.)*)\'|`((?:[^`\\]|\\.)*)`')


def chaines(f):
    texte = io.open(os.path.join(RACINE, f), encoding="utf-8").read()
    if f.endswith(".json"):
        try:
            return list(chaines_json(json.loads(texte)))
        except ValueError:
            return []
    return [next(g for g in m.groups() if g is not None) for m in LITTERAL.finditer(texte)]


def acceptes():
    if not os.path.exists(ACCEPTES):
        return set()
    lignes = io.open(ACCEPTES, encoding="utf-8").read().splitlines()
    return {l.split(" | ")[0].strip() for l in lignes if l.strip() and not l.startswith("#")}


def relever(fichiers):
    """[(fichier, texte, [(langue, forme)])]."""
    res = []
    for f in fichiers:
        for c in chaines(f):
            s = signalements(c)
            if s:
                res.append((f, c, s))
    return res


def main():
    if "--tout" in sys.argv:
        import construire_site
        import subprocess
        suivis = subprocess.run(["git", "ls-files", "-z"], cwd=RACINE, capture_output=True).stdout.decode("utf-8")
        fichiers = [f for f in suivis.split("\0") if f.endswith((".json", ".js", ".html")) and construire_site.publie(f)
                    and re.search("[а-яąćęłńśźż]", io.open(os.path.join(RACINE, f), encoding="utf-8", errors="replace").read(), re.I)]
    else:
        fichiers = PERIMETRE
    ok = acceptes()
    restes = [(f, c, s) for f, c, s in relever(fichiers) if c.strip() not in ok]
    par_fichier = {}
    for f, c, s in restes:
        par_fichier.setdefault(f, []).append((c, s))
        print("%s | %s | %s" % (f, " / ".join(x[1] for x in s), c[:150].replace("\n", " ")))
    print("\n%d texte(s) au masculin pour le lecteur (hors acceptes, %d acceptes)" % (len(restes), len(ok)))
    for f, l in sorted(par_fichier.items(), key=lambda x: -len(x[1])):
        print("   %4d  %s" % (len(l), f))
    return 1 if restes and "--tout" not in sys.argv else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
