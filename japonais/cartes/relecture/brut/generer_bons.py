"""Complete une reponse collee dont on n'a recopie que les lignes avec un avis.

    python generer_bons.py <reponse.txt> <premier> <dernier> <sortie.txt>

Les codes P<premier>..P<dernier> absents du fichier recoivent « NATUREL | OUI | »,
ce que le relecteur avait repondu pour eux. Refuse un code hors de l'intervalle.
"""
import re
import sys
from pathlib import Path

source, premier, dernier, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
avis = {}
for ligne in Path(source).read_text(encoding="utf-8").splitlines():
    m = re.match(r"P(\d{4}) \|", ligne)
    if not m:
        continue
    n = int(m.group(1))
    if not premier <= n <= dernier:
        sys.exit(f"code hors intervalle : {ligne[:40]}")
    avis[n] = ligne
lignes = [avis.get(n, f"P{n:04d} | NATUREL | OUI |") for n in range(premier, dernier + 1)]
Path(sortie).write_text("\n".join(lignes) + "\n", encoding="utf-8")
print(f"{len(lignes)} lignes, dont {len(avis)} avec un avis -> {sortie}")
