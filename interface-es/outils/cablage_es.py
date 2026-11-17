# -*- coding: utf-8 -*-
"""Branche l'espagnol, 10e langue d'interface de l'ALLEMAND appris, dans le code de l'app.

    python interface-es/outils/cablage_es.py [--ecrire]

Sans --ecrire, rien n'est ecrit : on verifie seulement que chaque remplacement
trouve exactement ce qu'il attend (un motif qui ne se trouve pas, ou qui se
trouve deux fois, arrete tout).

Modele : russe/outils/cablage_ru.py. Decision de Jacques du 15 nov. 2026
(decisions/DECISIONS.md) ; plan accorde par le chef d'orchestre le meme jour.

⚠️ « es » EST DEJA UN CODE DU MOTEUR, DANS DEUX SENS
    - la langue APPRISE (LANGUE_APPRISE === "es", I18N_ESPAGNOL, wortandoEs_) :
      on n'y touche pas ; aucun de ces tests ne lit getUiLang() ;
    - la langue d'interface de l'ANGLAIS appris (2 nov. 2026, anglais/es/) :
      SUFFIXE_LANGUE, RANGS_CARTE, DRAPEAUX_LANGUE, LANGUE_TAG, I18N.es existent
      deja. Ce script ETEND ce deuxieme sens a l'allemand appris, sans le
      modifier pour l'anglais (le repli de l'anglais reste es -> fr).

L'ESSAI ADMIN. Tant que l'espagnol n'est pas complet, il n'entre dans UI_LANGS
de l'allemand que si l'admin l'a ouvert SUR L'APPAREIL (Reglages ->
Administration -> « ESPAÑOL — ESSAI INTERFACE »), cle locale
deutschAI_essaiInterfaceEs. Sans elle, rien ne change : un telephone regle en
espagnol s'ouvre toujours en anglais (langueDuTelephone).

Variante : Amerique latine neutre (champEs(), VARIANTE_INTERFACE_ES par defaut
« latam ») ; « ¿Qué español? » reste cache pour l'allemand appris
(data-seulement-en).
"""
import io
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Les libelles des categories d'adverbes et d'expressions (comme cablage_ru.py).
CATS = {
    "Zeit": "Zeit \\u2014 tiempo",
    "Ort/Richtung": "Ort/Richtung \\u2014 lugar, direcci\\u00f3n",
    "H\\u00e4ufigkeit": "H\\u00e4ufigkeit \\u2014 frecuencia",
    "Art und Weise": "Art und Weise \\u2014 modo",
    "Grad/Menge": "Grad/Menge \\u2014 grado, cantidad",
    "Grund/Folge": "Grund/Folge \\u2014 causa, consecuencia",
    "Verbindung/Logik": "Verbindung/Logik \\u2014 conexi\\u00f3n l\\u00f3gica",
    "Frageadverbien": "Frageadverbien \\u2014 palabras interrogativas",
    "Nuance/Ton": "Nuance/Ton \\u2014 actitud",
    "Begrüßung/Small Talk": "Begrüßung \\u2014 saludar, platicar",
    "Meinung/Zustimmung": "Meinung \\u2014 dar tu opini\\u00f3n",
    "Gefühle/Reaktionen": "Gefühle \\u2014 sentimientos, reacciones",
    "Alltag/Organisation": "Alltag \\u2014 la vida diaria",
    "Diskussion/Nuance": "Diskussion \\u2014 matizar, argumentar",
    "Feste Verbindungen": "Feste Verbindungen \\u2014 verbo + sustantivo",
}


class Fichier:
    def __init__(self, chemin):
        self.chemin = chemin
        self.src = io.open(chemin, encoding="utf-8", newline="").read()
        self.nl = "\r\n" if "\r\n" in self.src else "\n"

    def _nl(self, s):
        return s.replace("\n", self.nl) if self.nl != "\n" else s

    def r(self, avant, apres, n=1):
        avant, apres = self._nl(avant), self._nl(apres)
        c = self.src.count(avant)
        if c != n:
            sys.exit("%s : ATTENDU %d, TROUVE %d : %r"
                     % (os.path.basename(self.chemin), n, c, avant[:120]))
        self.src = self.src.replace(avant, apres)

    def sub(self, motif, rempl, n=1, flags=0):
        nouveau, c = re.subn(motif, rempl, self.src, flags=flags)
        if c != n:
            sys.exit("%s : ATTENDU %d, TROUVE %d : %s"
                     % (os.path.basename(self.chemin), n, c, motif[:120]))
        self.src = nouveau

    def ecrire(self):
        io.open(self.chemin, "w", encoding="utf-8", newline="").write(self.src)


def index_html(f):
    if "CLE_ESSAI_INTERFACE_ES" in f.src:
        sys.exit("l'espagnol de l'allemand est DEJA cable : rien n'a ete touche")

    # 1. L'essai admin, puis UI_LANGS de l'allemand.
    f.r('const UI_LANGS = LANGUE_APPRISE === "es" ? ["fr", "en", "pt", "ar", "de"]\n',
        '// L\'ESPAGNOL, LANGUE D\'INTERFACE DE L\'ALLEMAND (15 nov. 2026, decision de Jacques,\n'
        '// interface-es/PLAN.md) : en ESSAI tant qu\'il n\'est pas complet. Il n\'entre dans\n'
        '// UI_LANGS que si l\'admin l\'a ouvert sur l\'appareil (Reglages -> Administration),\n'
        '// sinon un telephone regle en espagnol s\'ouvrirait en espagnol (langueDuTelephone).\n'
        'const CLE_ESSAI_INTERFACE_ES = PREFIXE_STOCKAGE + "essaiInterfaceEs";\n'
        'const ESSAI_INTERFACE_ES = LANGUE_APPRISE === "de" && (() => {\n'
        '    try{ return localStorage.getItem(CLE_ESSAI_INTERFACE_ES) === "1"; }catch(e){ return false; }\n'
        '})();\n'
        'const UI_LANGS = LANGUE_APPRISE === "es" ? ["fr", "en", "pt", "ar", "de"]\n')
    f.r('               : ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"];\nconst DEFAULT_UI_LANG',
        '               // L\'espagnol (Amerique latine), 10e langue de l\'allemand : sous essai (ci-dessus).\n'
        '               : ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"].concat(ESSAI_INTERFACE_ES ? ["es"] : []);\n'
        'const DEFAULT_UI_LANG')

    # 2. Le repli : es -> fr pour l'anglais appris (jamais par la langue apprise),
    #    es -> en -> fr pour l'allemand, comme les huit autres.
    f.r('                       es: ["es", "fr"] };',
        '                       // L\'allemand appris (15 nov. 2026) : es -> en -> fr, comme les autres.\n'
        '                       es: LANGUE_APPRISE === "en" ? ["es", "fr"] : ["es", "en", "fr"] };')

    # 3. Les cinq tuples de cartes : les rangs es (apres ceux de « de », vides).
    f.r(': LANGUE_APPRISE === "en" ? ["", "", champEs(',
        ': (LANGUE_APPRISE === "en" || LANGUE_APPRISE === "de") ? ["", "", champEs(', 2)
    f.r(': LANGUE_APPRISE === "en" ? ["", "", "", champEs(',
        ': (LANGUE_APPRISE === "en" || LANGUE_APPRISE === "de") ? ["", "", "", champEs(', 3)

    # 4. Le chargeur des verbes : la carte et ses trois temps.
    f.r('                    ...(LANGUE_APPRISE === "en" ? { traduction_es: champEs(v, "traduction"), exemple_es: champEs(v, "exemple") } : {}),\n',
        '                    ...(LANGUE_APPRISE === "en" ? { traduction_es: champEs(v, "traduction"), exemple_es: champEs(v, "exemple") } : {}),\n'
        '                    // L\'espagnol, langue d\'interface de l\'allemand (15 nov. 2026) : la carte et ses trois temps.\n'
        '                    ...(LANGUE_APPRISE === "de" ? { traduction_es: champEs(v, "traduction"), exemple_es: champEs(v, "exemple"),\n'
        '                        praeteritum_es: v.praeteritum_es || "", perfekt_es: v.perfekt_es || "", konjunktiv2_es: v.konjunktiv2_es || "" } : {}),\n')

    # 5. Premiers pas : les rangs es aussi pour l'allemand.
    f.r('                   ...(LANGUE_APPRISE === "en" ? { es: [36, 37, 38] } : {}) };',
        '                   // et de l\'allemand (15 nov. 2026).\n'
        '                   ...((LANGUE_APPRISE === "en" || LANGUE_APPRISE === "de") ? { es: [36, 37, 38] } : {}) };')

    # 6. La phrase d'essai de la voix de l'interface.
    f.r('        ...(LANGUE_APPRISE === "en" ? { es: "¡Buenos días! Aprendo un poco de inglés todos los días." } : {}),\n',
        '        ...(LANGUE_APPRISE === "en" ? { es: "¡Buenos días! Aprendo un poco de inglés todos los días." }\n'
        '            : LANGUE_APPRISE === "de" ? { es: "¡Buenos días! Aprendo un poco de alemán todos los días." } : {}),\n')

    # 7. Le quiz des articles : la traduction et l'explication en espagnol.
    f.r('["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"].concat(LANGUE_APPRISE === "de" ? [] : ["de"]).forEach(code => {',
        '["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"].concat(LANGUE_APPRISE === "de" ? ["es"] : ["de"]).forEach(code => {')

    # 8. La recherche.
    f.r('de: w[0], fr: w[3], en: w[4], tr: w[12], uk: w[15], fa: w[17], pt: w[19], ar: w[21], pl: w[23], ru: w[25], alt: w[8]',
        'de: w[0], fr: w[3], en: w[4], tr: w[12], uk: w[15], fa: w[17], pt: w[19], ar: w[21], pl: w[23], ru: w[25], es: w[29], alt: w[8]')
    f.r('pl: v.traduction_pl, ru: v.traduction_ru\n',
        'pl: v.traduction_pl, ru: v.traduction_ru, es: v.traduction_es\n', 3)
    f.r('pl: a[21], ru: a[23]\n', 'pl: a[21], ru: a[23], es: a[27]\n', 2)
    for cle, rang in (("praep", 35), ("adverbien", 36), ("konjunktionen", 35), ("partikeln", 35),
                      ("kasusverben", 35), ("redewendungen", 36)):
        f.sub(r"(\[\w+Theme, 'search_kind_\w+', 'search_src_\w+', '%s'(?:, \d+){7})\]" % cle,
              lambda m, r=rang: m.group(1) + ", %d]" % r)
    f.r('pl: w[cfg[9]], ru: w[cfg[10]]\n', 'pl: w[cfg[9]], ru: w[cfg[10]], es: w[cfg[11]]\n')

    # 9. Ecoute, phrases a construire, examens : les champs copies.
    f.r('correctPl: correct, correctRu: correct,', 'correctPl: correct, correctRu: correct, correctEs: correct,', 2)
    f.r('optionsPl: options, optionsRu: options,', 'optionsPl: options, optionsRu: options, optionsEs: options,', 3)
    f.r('correctPl: bonne, correctRu: bonne,', 'correctPl: bonne, correctRu: bonne, correctEs: bonne,')
    f.r('explanation_pl: ph.de, explanation_ru: ph.de', 'explanation_pl: ph.de, explanation_ru: ph.de, explanation_es: ph.de')
    f.r('pl: w[r.pl], ru: w[r.ru], de: w[r.de] });', 'pl: w[r.pl], ru: w[r.ru], de: w[r.de], es: w[r.es] });', 2)
    f.r('ru: v[base + "_ru"], de: v[base + "_de"] });', 'ru: v[base + "_ru"], de: v[base + "_de"], es: v[base + "_es"] });')
    f.r('ru: v.exemple_ru, de: v.exemple_de }', 'ru: v.exemple_ru, de: v.exemple_de, es: v.exemple_es }', 2)

    # 10. Les libelles des categories.
    nl = f.nl
    lignes = f.src.split(nl)
    vus = {}
    for i, l in enumerate(lignes):
        m = re.match(r'^    "([^"]+)":\s*\{ fr: ', l)
        if m and m.group(1) in CATS:
            if " es: " in l:
                sys.exit("deja es : " + m.group(1))
            coeur = l.rstrip()
            fin = "," if coeur.endswith("},") else ""
            coeur = coeur[:-2] if fin else coeur[:-1]
            lignes[i] = coeur.rstrip() + ', es: "' + CATS[m.group(1)] + '" }' + fin
            vus[m.group(1)] = vus.get(m.group(1), 0) + 1
    if set(CATS) - set(vus) or any(n != 1 for n in vus.values()):
        sys.exit("categories : manquantes %s, en double %s"
                 % (set(CATS) - set(vus), [k for k, n in vus.items() if n != 1]))
    f.src = nl.join(lignes)

    # 11. Les boutons « Español » des deux choisisseurs : montres pour l'allemand
    #     quand l'essai est ouvert (caches dans la page par defaut).
    f.r('function adapterChoixALaLangueApprise(){\n',
        'function adapterChoixALaLangueApprise(){\n'
        '    // L\'espagnol, langue d\'interface de l\'allemand (essai, 15 nov. 2026).\n'
        '    if(LANGUE_APPRISE === "de"){\n'
        '        document.querySelectorAll(\'.setup-choice[onclick*="selectUiLangChoice(\\\'es\\\')"]\').forEach(btn => {\n'
        '            btn.classList.toggle("hidden", !UI_LANGS.includes("es"));\n'
        '        });\n'
        '    }\n')

    # 12. L'entree de l'essai dans la carte Administration.
    f.r('        <button class="secondary" onclick="ouvrirEssaiPortugais()">PORTUGUÊS — ESSAI PORTUGAIS →</button>\n',
        '        <button class="secondary" onclick="ouvrirEssaiPortugais()">PORTUGUÊS — ESSAI PORTUGAIS →</button>\n'
        '        <!-- L\'espagnol, langue d\'interface de l\'allemand (essai, 15 nov. 2026) : ouvre ou ferme\n'
        '             l\'essai SUR CET APPAREIL (cle locale), puis recharge. Allemand appris seulement. -->\n'
        '        <div class="spacer hidden" id="essaiInterfaceEsEspace"></div>\n'
        '        <button class="secondary hidden" id="essaiInterfaceEsBtn" onclick="basculerEssaiInterfaceEs()">ESPAÑOL — ESSAI INTERFACE →</button>\n')
    f.r('    majEntreeEssaiAnglais();\n    try{ majCartePlacement(); }catch(e){}',
        '    majEntreeEssaiAnglais();\n    majEntreeEssaiInterfaceEs();\n    try{ majCartePlacement(); }catch(e){}')
    f.r('function majEntreeEssaiAnglais(){\n',
        '// L\'ESSAI DE L\'ESPAGNOL, LANGUE D\'INTERFACE DE L\'ALLEMAND (15 nov. 2026). Le bouton dit\n'
        '// ce qu\'il fera ; fermer l\'essai remet l\'interface en francais si elle etait en espagnol.\n'
        'function majEntreeEssaiInterfaceEs(){\n'
        '    const b = document.getElementById("essaiInterfaceEsBtn");\n'
        '    const e = document.getElementById("essaiInterfaceEsEspace");\n'
        '    const voir = LANGUE_APPRISE === "de" && isAdminUser();\n'
        '    if(b){\n'
        '        b.classList.toggle("hidden", !voir);\n'
        '        b.textContent = ESSAI_INTERFACE_ES ? "ESPAÑOL — FERMER L\'ESSAI INTERFACE" : "ESPAÑOL — ESSAI INTERFACE →";\n'
        '    }\n'
        '    if(e) e.classList.toggle("hidden", !voir);\n'
        '}\n'
        'function basculerEssaiInterfaceEs(){\n'
        '    if(LANGUE_APPRISE !== "de" || !isAdminUser()) return;\n'
        '    try{\n'
        '        if(ESSAI_INTERFACE_ES){\n'
        '            localStorage.removeItem(CLE_ESSAI_INTERFACE_ES);\n'
        '            if(getUiLang() === "es") localStorage.setItem(UI_LANG_KEY, "fr");\n'
        '        } else {\n'
        '            localStorage.setItem(CLE_ESSAI_INTERFACE_ES, "1");\n'
        '            localStorage.setItem(UI_LANG_KEY, "es");\n'
        '        }\n'
        '    }catch(e){}\n'
        '    location.reload();\n'
        '}\n\n'
        'function majEntreeEssaiAnglais(){\n')


def main():
    f = Fichier(os.path.join(RACINE, "index.html"))
    index_html(f)
    print("ok : cablage espagnol pret")
    if "--ecrire" in sys.argv:
        f.ecrire()
        print("ecrit")


if __name__ == "__main__":
    main()
