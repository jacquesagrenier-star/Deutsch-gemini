# Brouillon compact -> lot de corpus_langue.py (copie de .claude/russe/outils/lot.py,
# garde adaptee au cyrillique).
#   python lot.py <reste.txt> <fichier.json> <brouillon.txt> <lot.json>
# brouillon : une carte par ligne, « num|traduction|exemple[|perfekt|praeteritum|konj2][|kategorie] »
# La cle allemande vient du releve (« #12 der Vater [...] ») : on retire l'article.
import io, json, re, sys

reste, fichier, brouillon, sortie = sys.argv[1:5]
cles = {}
for l in io.open(reste, encoding="utf-8"):
    m = re.match(r"#(\d+) (.+?) \[", l)
    if m:
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
    # Un mot qui melange lettres latines et cyrilliques : « Мocква » avec un o
    # latin se lit pareil et ne se trouve plus par la recherche. L'oeil ne le
    # voit pas ; la machine, si.
    for v in vals:
        for mot in re.findall(r"[^\s\-—,.;:!?()«»“”„'/…]+", v):
            if re.search(r"[A-Za-zÄÖÜäöüß]", mot) and re.search(r"[Ѐ-ӿ]", mot):
                sys.exit("ligne %d : mot melangeant latin et cyrillique : %r" % (n, mot))
    # Une traduction ou un exemple sans une seule lettre cyrillique : une
    # ligne oubliee, restee en allemand ou en francais.
    for v in vals:
        if not re.search(r"[Ѐ-ӿ]", v):
            sys.exit("ligne %d : aucun mot russe dans %r" % (n, v))
    e[num] = [cles[num]] + vals
json.dump({"fichier": fichier, "e": e}, io.open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("%d cartes -> %s" % (len(e), sortie))
