# Brouillon compact -> lot de corpus_langue.py.
#   python lot.py <reste.txt> <fichier.json> <brouillon.txt> <lot.json>
# brouillon : une carte par ligne, « num|traduction|exemple[|perfekt|praeteritum|konj2][|kategorie] »
# La cle allemande vient du releve (« #12 der Vater [...] ») : on retire l'article.
import io, json, re, sys

reste, fichier, brouillon, sortie = sys.argv[1:5]
cles, exemples, dernier = {}, {}, None
for l in io.open(reste, encoding="utf-8"):
    e = re.match(r"    (?:exem|perf|prae|konj): (.*)", l)
    if e and dernier:
        exemples[dernier] = exemples.get(dernier, "") + " " + e.group(1)
    m = re.match(r"#(\d+) (.+?) \[", l)
    if m:
        dernier = m.group(1)
        mot = m.group(2)
        if fichier == "themes.json":
            mot = re.sub(r"^(der|die|das) ", "", mot)
        cles[m.group(1)] = mot
e = {}
for n, l in enumerate(io.open(brouillon, encoding="utf-8"), 1):
    l = l.rstrip("\n")
    if not l.strip() or l.startswith("#"):
        continue
    parts = l.split("|")
    num = parts[0].strip()
    if num not in cles:
        sys.exit("ligne %d : numero %s absent du releve" % (n, num))
    if num in e:
        sys.exit("ligne %d : numero %s en double" % (n, num))
    vals = [p.strip() for p in parts[1:]]
    if any(not v for v in vals) or any(ord(c) < 32 for v in vals for c in v):
        sys.exit("ligne %d : champ vide ou caractere de controle" % n)
    # Garde du polonais (l'arabe avait « lettres latines et arabes mêlées ») :
    # 1. aucune lettre cyrillique ni arabe (copie d'une autre colonne) ;
    # 2. aucune lettre propre a l'allemand (ä ö ü ß) dans un mot que l'exemple
    #    allemand de la carte ne contient pas : c'est un mot allemand oublie
    #    dans la traduction (« Kaffee » au lieu de « kawa ») -- un nom propre
    #    (Müller, Köln) figure dans l'exemple et passe ;
    # 3. l'exemple polonais n'est pas l'exemple allemand recopie.
    de = exemples.get(num, "")
    for v in vals:
        if re.search(r"[\u0400-\u04FF\u0600-\u06FF]", v):
            sys.exit("ligne %d : lettre cyrillique ou arabe : %r" % (n, v))
        for mot in re.findall(r"[^\s\-—,.;:!?()„”'/…]+", v):
            if re.search(r"[äöüßÄÖÜ]", mot) and mot not in de:
                sys.exit("ligne %d : mot allemand dans le polonais : %r" % (n, mot))
    if len(vals) > 1 and de and vals[1].strip() == de.strip():
        sys.exit("ligne %d : exemple recopie de l'allemand" % n)
    e[num] = [cles[num]] + vals
json.dump({"fichier": fichier, "e": e}, io.open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("%d cartes -> %s" % (len(e), sortie))
