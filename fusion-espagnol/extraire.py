"""Decoupe une declaration `const NOM = <valeur>;` d'un fichier JavaScript, en
suivant les chaines, les gabarits et les commentaires : une accolade dans
une chaine ne compte pas."""


def fin_valeur(s, i):
    """i pointe sur le premier caractere de la valeur. Rend l'indice juste
    apres le « ; » qui la termine, au niveau zero."""
    prof = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c in "\"'":
            q = c; i += 1
            while s[i] != q:
                if s[i] == "\\":
                    i += 1
                i += 1
        elif c == "`":
            i += 1
            while s[i] != "`":
                if s[i] == "\\":
                    i += 1
                elif s[i] == "$" and s[i + 1] == "{":
                    # un gabarit imbrique : on compte ses accolades
                    i += 2; p = 1
                    while p:
                        if s[i] == "{": p += 1
                        elif s[i] == "}": p -= 1
                        i += 1
                    continue
                i += 1
        elif c == "/" and s[i + 1] == "/":
            i = s.index("\n", i)
            continue
        elif c == "/" and s[i + 1] == "*":
            i = s.index("*/", i) + 2
            continue
        elif c in "([{":
            prof += 1
        elif c in ")]}":
            prof -= 1
        elif c == ";" and prof == 0:
            return i + 1
        i += 1
    raise ValueError("fin introuvable")


def declaration(s, nom):
    """Rend (debut, fin, texte) de `const nom = ...;` ; exige une seule."""
    ancre = "const " + nom + " = "
    assert s.count(ancre) == 1, (nom, s.count(ancre))
    d = s.index(ancre)
    f = fin_valeur(s, d + len(ancre))
    return d, f, s[d:f]
