# -*- coding: utf-8 -*-
"""La premiere colonne des tableaux de grammaire de l'espagnol, par langue.

Jusqu'au 1er nov. 2026, une quinzaine de libelles de cette colonne etaient des
chaines francaises (« vosotros (Espagne) », « tú (négatif) », « l'heure »,
« concéder »), affichees telles quelles en anglais, en portugais et en arabe.
abrirGramatica() passe deja chaque cellule par texteDeFiche() : un objet
{fr, en, pt, ar} suffit. Le francais ne change pas.

    python espanol/ar/colonne_fiches.py
"""
import io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CIBLE = os.path.join(RACINE, "espanol", "datos", "grammaire.json")

LIBELLES = {
    "vosotros (Espagne)": ("vosotros (Spain)", "vosotros (Espanha)", "vosotros (إسبانيا)"),
    "-ma (grec)": ("-ma (Greek)", "-ma (grego)", "-ma (أصل يوناني)"),
    "a (personnel)": ("personal a", "a (pessoal)", "a (قبل الشخص)"),
    "ajouter": ("adding", "acrescentar", "الإضافة"),
    "cause": ("cause", "causa", "السبب"),
    "concéder": ("conceding", "concessão", "الاستدراك"),
    "condition": ("condition", "condição", "الشرط"),
    "conséquence": ("consequence", "consequência", "النتيجة"),
    "opposer": ("contrasting", "oposição", "المقابلة"),
    "organiser": ("ordering", "organizar", "الترتيب"),
    "estar + gérondif": ("estar + gerund", "estar + gerúndio", "estar + gerundio"),
    "seguir + gérondif": ("seguir + gerund", "seguir + gerúndio", "seguir + gerundio"),
    "irréguliers": ("irregulars", "irregulares", "الأفعال الشاذة"),
    "l'heure": ("the time", "as horas", "الساعة"),
    "tú (négatif)": ("tú (negative)", "tú (negativo)", "tú (النفي)"),
    "tú irréguliers": ("tú irregulars", "tú irregulares", "tú: الأفعال الشاذة"),
}

# Le fichier est en CRLF : le garder tel quel, sinon chaque ligne changerait.
crlf = b"\r\n" in open(CIBLE, "rb").read(200)
texte = io.open(CIBLE, encoding="utf-8").read()
d = json.loads(texte)
n = 0
for f in d["fiches"]:
    for ligne in f.get("tableau", []):
        if isinstance(ligne[0], str) and ligne[0] in LIBELLES:
            en, pt, ar = LIBELLES[ligne[0]]
            ligne[0] = {"fr": ligne[0], "en": en, "pt": pt, "ar": ar}
            n += 1
indent = 1 if texte.startswith("{\n \"") else 2
with io.open(CIBLE, "w", encoding="utf-8", newline="\r\n" if crlf else "\n") as f:
    json.dump(d, f, ensure_ascii=False, indent=indent)
    if texte.endswith("\n"):
        f.write("\n")
print("%d cellules traduites" % n)
