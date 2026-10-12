# Brouillon compact -> lot de corpus_langue.py.
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
            mot = re.sub(r"^((der|die|das)(/(der|die|das))* )?(\(Pl\.\) )?", "", mot)
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
    # Un mot qui melange lettres latines et arabes : une faute de frappe
    # (« Grundzahلen ») que l'oeil ne voit pas dans une ligne RTL.
    for v in vals:
        for mot in re.findall(r"[^\s\-—،,.;:!?()«»“”'/]+", v):
            if re.search(r"[A-Za-zÄÖÜäöüß]", mot) and re.search(r"[؀-ۿ]", mot):
                sys.exit("ligne %d : mot melangeant latin et arabe : %r" % (n, mot))
    e[num] = [cles[num]] + vals
json.dump({"fichier": fichier, "e": e}, io.open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("%d cartes -> %s" % (len(e), sortie))
