# -*- coding: utf-8 -*-
# Traductions decalees, deuxieme vague (1er nov. 2026, apres le retour de Daria et les 34 du v1056).
# Trouvees par homonymes.py / doublons.py (une meme traduction en face de deux phrases differentes du
# meme mot) et par le rejeu git (rejouer.py : l'espagnol ll / y reecrit le 31 oct., pt et ar restes sur
# l'ancienne explication). Relues une a une. Chaque correction est reperee par (chemin, phrase ACTUELLE) :
# si la phrase a bouge entre-temps, rien n'est ecrit et le script le dit.
#   python corriger_decalees.py <racine du depot>
import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
RACINE = sys.argv[1]

# (fichier, fonction qui trouve l'objet, cle de controle, valeur attendue, {champ: nouvelle valeur})
def theme(d, tid, mot):
    for t in d["themes"]:
        if t["id"] == tid:
            r = [m for m in t["mots"] if m.get("mot") == mot]
            assert len(r) == 1, (tid, mot)
            return r[0]

def categorie(d, cat, mot):
    r = [m for m in d[cat] if m.get("mot") == mot]
    assert len(r) == 1, (cat, mot)
    return r[0]

def regle(d, rid):
    r = [x for g in d["groupes"] for x in g["regles"] if x.get("id") == rid]
    assert len(r) == 1, rid
    return r[0]

C = [
 # Le turc de berufe_a1 avait recu la phrase du meme mot dans arbeit_buero_a1 (ou universitaet_a1).
 ("themes.json", lambda d: theme(d, "berufe_a1", "Chef"), "exemple", "Mein Chef ist sehr streng.",
  {"exemple_tr": "Patronum çok sert."}),
 ("themes.json", lambda d: theme(d, "berufe_a1", "Kollege"), "exemple", "Mein Kollege sitzt neben mir.",
  {"exemple_tr": "İş arkadaşım yanımda oturuyor."}),
 ("themes.json", lambda d: theme(d, "berufe_a1", "Student"), "exemple", "Der Student lernt für die Prüfung.",
  {"exemple_tr": "Öğrenci sınava çalışıyor."}),
 # Le persan de la particule et de la preposition avait recu la phrase de la conjonction homonyme.
 ("funktionswort.json", lambda d: categorie(d, "partikeln", "denn"), "exemple", "Was machst du denn?",
  {"exemple_fa": "حالا چه کار می‌کنی؟"}),
 ("funktionswort.json", lambda d: categorie(d, "praepositionen", "während"), "exemple", "Während des Urlaubs lese ich viel.",
  {"exemple_fa": "در طول تعطیلات زیاد کتاب می‌خوانم."}),
]

# L'espagnol ll / y (portugais et arabe restes sur l'explication d'avant le 31 oct.) ne se corrige PAS
# ici : espanol/datos/prononciation.json est derive de tests/prononciation_es.py, corrige a la source.

ecrits = 0
for f in sorted(set(c[0] for c in C)):
    chemin = os.path.join(RACINE, f)
    s = open(chemin, encoding="utf-8").read()
    d = json.loads(s)
    forme = None
    for ind in (2, 1):
        if json.dumps(d, ensure_ascii=False, indent=ind) + ("\n" if s.endswith("\n") else "") == s:
            forme = ind
    assert forme, f + " : forme inattendue, rien ecrit"
    n = 0
    for fic, trouver, cle, attendu, champs in C:
        if fic != f:
            continue
        o = trouver(d)
        if o.get(cle) != attendu:
            print("  ⚠", f, ": la phrase a change, rien ecrit --", o.get(cle)); continue
        for k, v in champs.items():
            assert k in o, (f, k)
            if o[k] != v:
                print("  ", f, attendu, k, ":", o[k], "->", v)
                o[k] = v; n += 1
    if n:
        open(chemin, "w", encoding="utf-8", newline="").write(json.dumps(d, ensure_ascii=False, indent=forme) + ("\n" if s.endswith("\n") else ""))
    print(f, n, "champs corriges")
    ecrits += n
print(ecrits, "en tout")
