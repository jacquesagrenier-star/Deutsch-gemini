# -*- coding: utf-8 -*-
"""Cherche le FRANCAIS ECRIT EN DUR dans le HTML, hors de toute cle i18n.

⚠️ CE QUE LE VERIFICATEUR NE VOIT PAS. Il controle qu'une cle CITEE existe. Il
ne voit pas un element qui ne cite AUCUNE cle : pour lui ce texte n'est pas une
traduction manquante, c'est du decor. Or a l'ecran c'est du francais servi a un
lecteur turc, ukrainien, persan ou arabe.

Trouve le 15 septembre 2026 en montant l'essai RTL arabe : l'ecran de resultat
affichait « Très bien ! » en francais, et l'affichait ainsi depuis toujours
pour les cinq langues non francaises.

⚠️ IL FAUT SUIVRE L'IMBRICATION, PAS L'ELEMENT SEUL. Premiere version : une
expression reguliere par element -> 48 signalements, presque tous faux. Les
explications de grammaire portent data-i18n-html sur le PARENT ; leurs <em> et
<strong> internes n'ont evidemment pas d'attribut, et applyUiLang() remplace le
bloc entier. Un detecteur qui ne regarde pas les ancetres ne mesure rien.
"""
import io
import os
import re
import sys
from html.parser import HTMLParser

RACINE = r"C:\Users\jacqu\OneDrive\Desktop\Mes Projets\DeutschAI"
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MOTS = re.compile(r"\b(?:le|la|les|des|une?|du|au|aux|est|sont|pour|avec|dans|"
                  r"tes|ton|ta|tu|ce|cette|qui|que|sur|par|plus|tout|toute|"
                  r"sans|mais|bien|deja|encore|ici|vous|nous)\b", re.I)
ACCENTS = re.compile(r"[àâäéèêëîïôöùûüçœÀÂÄÉÈÊËÎÏÔÖÙÛÜÇŒ]")
VIDES = ("script", "style")


class Chasseur(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.pile = []          # (balise, protege, id)
        self.trouves = []
        self.ignore = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in VIDES:
            self.ignore += 1
        protege = any(k.startswith("data-i18n") for k in d)
        if self.pile:
            protege = protege or self.pile[-1][1]
        self.pile.append((tag, protege, d.get("id", "")))

    def handle_endtag(self, tag):
        if tag in VIDES and self.ignore:
            self.ignore -= 1
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i][0] == tag:
                del self.pile[i:]
                break

    def handle_data(self, texte):
        if self.ignore or not self.pile:
            return
        t = " ".join(texte.split())
        if len(t) < 4:
            return
        balise, protege, ident = self.pile[-1]
        if protege:
            return
        if not ACCENTS.search(t) and len(MOTS.findall(t)) < 2:
            return
        chemin = " > ".join(b for b, _, _ in self.pile[-3:])
        self.trouves.append((chemin, ident, t))


c = Chasseur()
c.feed(io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read())

print("  %d texte(s) francais qu'AUCUNE cle ne couvre\n" % len(c.trouves))
for chemin, ident, t in c.trouves:
    print("  %-34s id=%-20s %s" % (chemin, ident or "-", t[:76]))
