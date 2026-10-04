# -*- coding: utf-8 -*-
"""
Fabrique oracles/jmdict-courants.json : les verbes et adjectifs « courants » de JMdict,
avec leur classe, pour l'essai à grande échelle de tests.js.

Source : JMdict (EDRDG), licence CC BY-SA 4.0 — https://www.edrdg.org/edrdg/licence.html
Copie utilisée : la base SQLite du paquet PyPI jamdict-data 1.5 (JMdict 1.08, 2021).
La liste produite est une donnée dérivée de JMdict : même licence, même attribution.

« Courant » = au moins une graphie ou une lecture porte une marque de priorité
news1, ichi1, spec1, spec2 ou gai1 (la définition des entrées (P) de JMdict).

  pip download --no-deps jamdict-data==1.5 ; tar xzf ... ; xz -dk .../jamdict.db.xz
  python3 oracles/extraire_jmdict.py chemin/vers/jamdict.db
"""
import io
import json
import os
import sqlite3
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PRIO = ('news1', 'ichi1', 'spec1', 'spec2', 'gai1')

# jamdict range les classes sous leur description ; on revient au code JMdict.
CODES = {
    'Ichidan verb': 'v1',
    'Ichidan verb - kureru special class': 'v1-s',
    "Godan verb with 'u' ending": 'v5u',
    "Godan verb with 'ku' ending": 'v5k',
    "Godan verb with 'gu' ending": 'v5g',
    "Godan verb with 'su' ending": 'v5s',
    "Godan verb with 'tsu' ending": 'v5t',
    "Godan verb with 'nu' ending": 'v5n',
    "Godan verb with 'bu' ending": 'v5b',
    "Godan verb with 'mu' ending": 'v5m',
    "Godan verb with 'ru' ending": 'v5r',
    "Godan verb with 'ru' ending (irregular verb)": 'v5r-i',
    'Godan verb - Iku/Yuku special class': 'v5k-s',
    "Godan verb with 'u' ending (special class)": 'v5u-s',
    'Godan verb - -aru special class': 'v5aru',
    "Godan verb with 'uru' ending (old class of 'eru')": 'v5uru',
    'Kuru verb - special class': 'vk',
    'suru verb - included': 'vs-i',
    'suru verb - special class': 'vs-s',
    'noun or participle which takes the aux. verb suru': 'vs',
    'su verb - precursor to the modern suru': 'vs-c',
    'Ichidan verb - zuru verb (alternative form of -jiru verbs)': 'vz',
    'irregular nu verb': 'vn',
    'irregular ru verb, plain form ends with -ri': 'vr',
    'verb unspecified': 'v-unspec',
    'adjective (keiyoushi)': 'adj-i',
    'adjective (keiyoushi) - yoi/ii class': 'adj-ix',
    'adjectival nouns or quasi-adjectives (keiyodoshi)': 'adj-na',
    "'taru' adjective": 'adj-t',
    "'ku' adjective (archaic)": 'adj-ku',
    "'shiku' adjective (archaic)": 'adj-shiku',
    'archaic/formal form of na-adjective': 'adj-nari',
    'auxiliary adjective': 'aux-adj',
    'auxiliary verb': 'aux-v',
}


def code(description):
    if description in CODES:
        return CODES[description]
    if description.startswith('Nidan verb'):
        return 'v2'
    if description.startswith('Yodan verb'):
        return 'v4'
    return None


def main(chemin):
    c = sqlite3.connect(chemin)
    sortie, vus = [], set()
    for (idseq,) in c.execute('SELECT idseq FROM Entry ORDER BY idseq'):
        classes = []
        for (desc,) in c.execute('SELECT p.text FROM pos p JOIN Sense s ON p.sid = s.ID WHERE s.idseq = ?', (idseq,)):
            cd = code(desc)
            if cd and cd not in classes:
                classes.append(cd)
        if not classes:
            continue
        kanjis = c.execute('SELECT ID, text FROM Kanji WHERE idseq = ? ORDER BY ID', (idseq,)).fetchall()
        kanas = c.execute('SELECT ID, text, nokanji FROM Kana WHERE idseq = ? ORDER BY ID', (idseq,)).fetchall()
        prio_k = {kid for kid, in c.execute('SELECT kid FROM KJP WHERE kid IN (%s) AND text IN (%s)' % (
            ','.join(str(k[0]) for k in kanjis) or '0', ','.join("'%s'" % p for p in PRIO)))}
        prio_r = {kid for kid, in c.execute('SELECT kid FROM KNP WHERE kid IN (%s) AND text IN (%s)' % (
            ','.join(str(k[0]) for k in kanas) or '0', ','.join("'%s'" % p for p in PRIO)))}
        if not prio_k and not prio_r:
            continue
        # Graphies irrégulières, archaïques ou rares : écartées.
        mauvais_k = {kid for kid, in c.execute("SELECT kid FROM KJI WHERE text != ''")}
        mauvais_r = {kid for kid, in c.execute("SELECT kid FROM KNI WHERE text != ''")}
        kanji = next((t for i, t in kanjis if i in prio_k and i not in mauvais_k), None)
        if kanji is None and kanjis and not prio_r:
            continue
        lecture = None
        for i, t, nokanji in kanas:
            if i in mauvais_r or (kanji and nokanji):
                continue
            restr = [r for r, in c.execute('SELECT text FROM KNR WHERE kid = ?', (i,))]
            if kanji and restr and kanji not in restr:
                continue
            if i in prio_r or lecture is None:
                lecture = t
                if i in prio_r:
                    break
        if lecture is None:
            continue
        for cl in classes:
            cle = (kanji, lecture, cl)
            if cle not in vus:
                vus.add(cle)
                sortie.append([kanji, lecture, cl])
    with io.open(os.path.join(ICI, 'jmdict-courants.json'), 'w', encoding='utf-8') as f:
        f.write('[\n' + ',\n'.join(json.dumps(x, ensure_ascii=False) for x in sortie) + '\n]\n')
    print(len(sortie), 'entrées')


if __name__ == '__main__':
    main(sys.argv[1])
