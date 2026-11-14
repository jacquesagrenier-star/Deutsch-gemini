"""Theme 2 de l'annexe A : Grundpflege.

ON N'ECRIT PAS ICI : la source est pflege/sources/vocabulaire/t02_grundpflege.py (format compact, 9 langues),
que adaptateur.py presente au format de pflege/FORMAT-DONNEES.md, § 1. Puis
`python pflege/outils/construire.py` et `python tests/pflege.py`.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vocabulaire"))
from adaptateur import theme_soins  # noqa: E402

THEME, MOTS = theme_soins("t02_grundpflege")
