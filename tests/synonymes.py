# -*- coding: utf-8 -*-
"""Genere synonymes.json -- les voisins de sens DEJA DANS LE COURS.

REGLE DE BASE : deux mots allemands sont voisins s'ils partagent une traduction
en francais ET en anglais. Le francais seul rapproche fliegen et stehlen
(« voler »), haben et kriegen (« avoir ») ; l'anglais les separe.

CE QUI EST ECARTE ENSUITE est morphologique, jamais semantique -- une regle sur
la FORME ne se trompe pas, une regle sur le sens si. Premiere version du
programme : j'avais mis un doute sur « niveaux eloignes » et il signalait
angenehm/wohltuend, schweigsam/wortkarg, reserviert/zurueckhaltend. C'est
exactement l'enrichissement demande : un mot A2 qui ouvre sur son voisin C1.
Regle retiree.

Les quatre exclusions automatiques :
  1. feminin      Journalist / Journalistin   -- pas un synonyme, une forme
  2. reflechi     anmelden / sich anmelden    -- le meme verbe
  3. pluriel      Nudel / Nudeln              -- le meme mot
  4. prefixe      anrufen / rufen             -- le prefixe CHANGE le sens

La 4e est la plus importante et la moins evidente. « anrufen » n'est pas un
synonyme de « rufen » : on telephone, on ne crie pas. La traduction partagee
(« appeler ») est un accident du francais. On perd au passage quelques vraies
paires (anbieten/bieten), et c'est le bon cote ou se tromper : une carte qui
manque ne dit rien de faux.
"""
import json, re, unicodedata, collections, io

PREFIXES = ('ab', 'an', 'auf', 'aus', 'be', 'bei', 'durch', 'ein', 'ent', 'er',
            'her', 'hin', 'los', 'mit', 'nach', 'um', 'unter', 'ver', 'vor',
            'weg', 'zer', 'zu', 'zurück', 'zusammen', 'über')

# Paires ecartees A LA MAIN, apres lecture. Chacune passait les regles de forme
# et disait pourtant quelque chose de faux. La raison est ecrite : sans elle,
# la ligne se fait supprimer par le suivant qui la trouvera arbitraire.
A_ECARTER = {
    ('alter', 'zeitalter'):    "l'age d'une personne n'est pas une epoque",
    ('ehefrau', 'frau'):       "toute femme n'est pas une epouse",
    ('ehemann', 'mann'):       "tout homme n'est pas un mari",
    ('maß', 'maßnahme'):       "une mesure-grandeur n'est pas une mesure-action",
    ('speicher', 'speicherung'): "l'endroit n'est pas l'action de ranger",
    ('stand', 'zustand'):      "Stand est un etal, un rang, un niveau -- trop de sens",
    ('stand', 'staat'):        "faux couple sur « etat » : l'Etat et l'etat",
    ('lager', 'lagerbestand'): "Lager est aussi un camp et un entrepot",
    ('kuchen', 'torte'):       "une Torte n'est pas un Kuchen, un patissier corrigerait",
    ('tor', 'ziel'):           "Tor est une porte avant d'etre un but",
    ('reichen', 'zuspielen'):  "passer un ballon n'est pas tendre ni suffire",
    ('motiv', 'thema'):        "un motif n'est pas un sujet",
    ('machen', 'treiben'):     "treiben ne remplace pas machen (Sport treiben)",
    ('treiben', 'tun'):        "meme raison",
    ('zünder', 'zündholz'):    "un detonateur n'est pas une allumette",
}

def norm(s):
    s = (s or '').lower().strip()
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r"^(le |la |les |l'|un |une |des |to |the |se |s')", '', s)
    s = re.sub(r'\([^)]*\)', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def sens(t):
    return {norm(x) for x in re.split(r'[;,/]|\bou\b', t or '') if len(norm(x)) > 1}

mots = {}
def ajouter(de, fr, en, type_, niveau):
    if not de or not fr or not en:
        return
    # Une carte d'antonymes porte les deux mots dans le meme champ --
    # « angstlich/mutig ». Ce n'est pas un mot, ca ne peut pas etre un voisin.
    if '/' in de or ',' in de or '(' in de:
        return
    c = de.lower()
    if c in mots:
        mots[c][1] |= fr; mots[c][2] |= en
        return
    mots[c] = [de, fr, en, type_, niveau]

for t in json.load(io.open('themes.json', encoding='utf-8'))['themes']:
    for m in t.get('mots', []):
        ajouter(m.get('mot'), sens(m.get('traduction')), sens(m.get('traduction_en')), 'nom', t.get('niveau'))
def pv(o):
    if isinstance(o, dict):
        if 'infinitif' in o:
            ajouter(o['infinitif'], sens(o.get('traduction')), sens(o.get('traduction_en')), 'verbe', o.get('niveau'))
        else:
            for x in o.values(): pv(x)
    elif isinstance(o, list):
        for x in o: pv(x)
pv(json.load(io.open('verbe.json', encoding='utf-8')))
for niveau, liste in json.load(io.open('adjectif.json', encoding='utf-8')).items():
    for a in liste:
        ajouter(a.get('mot'), sens(a.get('traduction')), sens(a.get('traduction_en')), 'adjectif', niveau)

print('cartes distinctes :', len(mots), dict(collections.Counter(v[3] for v in mots.values())))

index_fr = collections.defaultdict(list)
for c, v in mots.items():
    for s in v[1]:
        index_fr[s].append(c)

brutes = {}
rejet_en = 0
for s, liste in index_fr.items():
    if len(liste) < 2 or len(liste) > 10:
        continue
    for x in range(len(liste)):
        for y in range(x + 1, len(liste)):
            a, b = sorted((liste[x], liste[y]))
            if mots[a][3] != mots[b][3]:
                continue
            com = mots[a][2] & mots[b][2]
            if com:
                p = brutes.setdefault((a, b), {'fr': set(), 'en': set()})
                p['fr'].add(s); p['en'] |= com
            else:
                rejet_en += 1
print('paires partageant un sens fr ET en :', len(brutes), '| rejetees par l anglais :', rejet_en)

def motif_exclusion(a, b):
    A, B = mots[a], mots[b]
    court, long_ = (a, b) if len(a) <= len(b) else (b, a)
    if long_ == court + 'in' or long_ == court + 'innen':
        return 'féminin'
    if long_ == 'sich ' + court:
        return 'réfléchi'
    if A[3] == 'nom' and long_ in (court + 'n', court + 'en', court + 'e', court + 's'):
        return 'pluriel'
    if A[3] == 'verbe':
        for p in PREFIXES:
            if long_ == p + court:
                return 'préfixe (' + p + '-)'
    return None

exclues = collections.defaultdict(list)
restantes = {}
for (a, b), info in brutes.items():
    m = motif_exclusion(a, b)
    if (a, b) in A_ECARTER or (b, a) in A_ECARTER:
        m = 'à la main'
    if m:
        exclues[m.split(' (')[0]].append((a, b, m))
    else:
        restantes[(a, b)] = info
print('exclues automatiquement :', sum(len(v) for v in exclues.values()),
      dict((k, len(v)) for k, v in exclues.items()))
print('paires retenues :', len(restantes))

# ce qui reste a regarder a l'oeil : les noms composes (un mot contient l'autre)
composes = [(a, b, i) for (a, b), i in restantes.items()
            if mots[a][3] == 'nom' and (a in b or b in a)]
print('noms composés à trancher à l\'œil :', len(composes))

voisins = collections.defaultdict(set)
for (a, b) in restantes:
    voisins[mots[a][0]].add(mots[b][0])
    voisins[mots[b][0]].add(mots[a][0])

donnees = {
 "_note": ("Voisins de sens deja presents dans le cours. Une paire n'y figure que si "
           "les deux mots partagent une traduction en francais ET en anglais : sur le "
           "francais seul, « voler » reunirait fliegen et stehlen. Sont ecartes "
           "automatiquement les feminins (Journalistin), les reflechis (sich anmelden), "
           "les pluriels (Nudeln) et les verbes a prefixe (anrufen / rufen), qui ne sont "
           "pas des synonymes mais des formes. Genere par tests/synonymes.py puis relu : "
           "pour retirer une paire, enlever le mot des deux listes."),
 "voisins": {k: sorted(v)[:3] for k, v in sorted(voisins.items())}
}
io.open('synonymes.json', 'w', encoding='utf-8', newline='').write(
    json.dumps(donnees, ensure_ascii=False, separators=(',', ':')))
print('synonymes.json :', len(donnees['voisins']), 'cartes,',
      sum(len(v) for v in donnees['voisins'].values()), 'liens')

with io.open('synonymes-a-relire.txt', 'w', encoding='utf-8', newline='') as f:
    f.write('NOMS COMPOSES A TRANCHER (%d)\n' % len(composes))
    f.write('Un mot contient l\'autre. Parfois deux noms du meme objet (Anwalt /\n')
    f.write('Rechtsanwalt), parfois un genre et son espece (Frau / Ehefrau) -- et la,\n')
    f.write('le lien est faux : toute Frau n\'est pas une Ehefrau.\n')
    f.write('=' * 70 + '\n')
    for a, b, i in sorted(composes, key=lambda x: mots[x[0]][0]):
        f.write('  %-22s %-22s  %-26s %s / %s\n' % (
            mots[a][0], mots[b][0], ', '.join(sorted(i['fr']))[:26],
            mots[a][4] or '?', mots[b][4] or '?'))
    f.write('\n\nEXCLUES AUTOMATIQUEMENT (%d)\n' % sum(len(v) for v in exclues.values()))
    f.write('=' * 70 + '\n')
    for m, liste in sorted(exclues.items(), key=lambda kv: -len(kv[1])):
        f.write('\n### %s (%d)\n' % (m, len(liste)))
        for a, b, detail in sorted(liste)[:200]:
            f.write('  %-24s %s\n' % (mots[a][0], mots[b][0]))
print('synonymes-a-relire.txt ecrit')
