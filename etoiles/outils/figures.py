# -*- coding: utf-8 -*-
"""Les constellations de la seance legere : une etoile par etape, dans l'ordre des etapes, et le dessin usuel.
Ce fichier ne porte AUCUNE mesure : positions, magnitudes, couleurs et distances viennent de SIMBAD
(etoiles/sources/), relues par construire.py. Choix des figures : maquette de la seance legere, 6 nov. 2026
(decision d9d9dbd : Grande Ourse, Gemeaux et Orion pour l'A1)."""

# Notre nom de l'etoile -> la designation que SIMBAD reconnait. L'ordre est celui des deux relevés de sources/.
DESIGNATIONS = [
 ("Dubhe", "alf UMa"), ("Merak", "bet UMa"), ("Phecda", "gam UMa"), ("Megrez", "del UMa"), ("Alioth", "eps UMa"),
 ("Mizar", "zet UMa"), ("Alcor", "80 UMa"), ("Alkaid", "eta UMa"),
 ("Castor", "alf Gem"), ("Pollux", "bet Gem"), ("tau Gem", "tau Gem"), ("iota Gem", "iot Gem"), ("kappa Gem", "kap Gem"),
 ("Mebsuta", "eps Gem"), ("Tejat", "mu. Gem"), ("Propus", "eta Gem"), ("Wasat", "del Gem"), ("Mekbuda", "zet Gem"),
 ("Alhena", "gam Gem"), ("Alzirr", "ksi Gem"),
 ("Meissa", "lam Ori"), ("Betelgeuse", "alf Ori"), ("Bellatrix", "gam Ori"), ("Mintaka", "del Ori"), ("Alnilam", "eps Ori"),
 ("Alnitak", "zet Ori"), ("Hatysa", "iot Ori"), ("Saiph", "kap Ori"), ("Rigel", "bet Ori"), ("Tabit", "pi.03 Ori"),
 ("Vega", "alf Lyr"), ("eps Lyr", "eps01 Lyr"), ("zeta Lyr", "zet01 Lyr"), ("delta Lyr", "del02 Lyr"), ("Sulafat", "gam Lyr"),
 ("Sheliak", "bet Lyr"),
 ("Deneb", "alf Cyg"), ("Sadr", "gam Cyg"), ("Fawaris", "del Cyg"), ("Gienah", "eps Cyg"), ("eta Cyg", "eta Cyg"),
 ("Albireo", "bet01 Cyg"),
 ("Sham", "alf Sge"), ("beta Sge", "bet Sge"), ("delta Sge", "del Sge"), ("gamma Sge", "gam Sge"),
 ("Alcyone", "eta Tau"), ("Atlas", "27 Tau"), ("Electra", "17 Tau"), ("Maia", "20 Tau"), ("Merope", "23 Tau"), ("Taygeta", "19 Tau"),
 ("Aldebaran", "alf Tau"), ("theta2 Tau", "tet02 Tau"), ("Prima Hyadum", "gam Tau"), ("delta1 Tau", "del01 Tau"),
 ("Ain", "eps Tau"), ("Tianguan", "zet Tau"),
 ("theta CrB", "tet CrB"), ("Nusakan", "bet CrB"), ("Alphecca", "alf CrB"), ("gamma CrB", "gam CrB"), ("delta CrB", "del CrB"),
 ("eps CrB", "eps CrB"),
 ("Capella", "alf Aur"), ("Menkalinan", "bet Aur"), ("Mahasim", "tet Aur"), ("Elnath", "bet Tau"), ("Hassaleh", "iot Aur"),
 ("Almaaz", "eps Aur"),
 ("Caph", "bet Cas"), ("Schedar", "alf Cas"), ("Navi", "gam Cas"), ("Ruchbah", "del Cas"), ("Segin", "eps Cas"),
 ("Alderamin", "alf Cep"), ("Alfirk", "bet Cep"), ("Errai", "gam Cep"), ("iota Cep", "iot Cep"), ("zeta Cep", "zet Cep"),
 ("Gienah Corvi", "gam Crv"), ("Algorab", "del Crv"), ("Kraz", "bet Crv"), ("Minkar", "eps Crv"),
 ("Sualocin", "alf Del"), ("Rotanev", "bet Del"), ("gamma Del", "gam02 Del"), ("delta Del", "del Del"), ("Aldulfin", "eps Del"),
 ("Markab", "alf Peg"), ("Scheat", "bet Peg"), ("Alpheratz", "alf And"), ("Algenib", "gam Peg"),
 ("Acrux", "alf01 Cru"), ("Mimosa", "bet Cru"), ("Gacrux", "gam Cru"), ("delta Cru", "del Cru"), ("Ginan", "eps Cru"),
]

# SIMBAD ne donne pas de magnitude V pour ces quatre identifiants (etoiles doubles, mesurees par composante) :
# la valeur usuelle du systeme, sans couleur (B-V inconnu, l'etoile garde la teinte de base).
V_USUELLE = {"Mizar": 2.23, "eps Lyr": 4.7, "gamma CrB": 3.84, "Errai": 3.21}

# Les noms de la figure. fr, de et es : maquette du 6 nov. ; les autres langues d'interface pour les trois
# figures de l'A1, l'anglais pour toutes. Une langue absente retombe sur l'anglais (a completer avant la
# mise en service pour tous).
FIGURES = {
 "ourse": dict(et=["Dubhe", "Merak", "Phecda", "Megrez", "Alioth", "Mizar", "Alcor", "Alkaid"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 7)],
   noms=dict(fr="la Grande Ourse", de="der Große Wagen", es="el Carro", en="the Big Dipper", pt="a Ursa Maior",
             tr="Büyük Ayı", pl="Wielki Wóz", ru="Большой Ковш", uk="Великий Віз", ar="الدب الأكبر", fa="دب اکبر")),
 "gemeaux": dict(et=["Castor", "tau Gem", "Mebsuta", "Tejat", "Propus", "iota Gem", "Pollux", "kappa Gem", "Wasat", "Mekbuda",
                     "Alhena", "Alzirr"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7), (6, 8), (8, 9), (9, 10), (10, 11)],
   noms=dict(fr="les Gémeaux", de="die Zwillinge", es="Géminis", en="Gemini", pt="Gêmeos", tr="İkizler", pl="Bliźnięta",
             ru="Близнецы", uk="Близнята", ar="التوأمان", fa="دوپیکر")),
 "orion": dict(et=["Meissa", "Betelgeuse", "Bellatrix", "Mintaka", "Alnilam", "Alnitak", "Hatysa", "Saiph", "Rigel", "Tabit"],
   tr=[(0, 1), (0, 2), (1, 5), (2, 3), (3, 4), (4, 5), (5, 7), (3, 8), (4, 6), (2, 9)],
   noms=dict(fr="Orion", de="Orion", es="Orión", en="Orion", pt="Órion", tr="Avcı", pl="Orion", ru="Орион", uk="Оріон",
             ar="الجبار", fa="شکارچی")),
 "lyre": dict(et=["Vega", "eps Lyr", "zeta Lyr", "delta Lyr", "Sulafat", "Sheliak"],
   tr=[(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2)],
   noms=dict(fr="la Lyre", de="die Leier", es="la Lira", en="Lyra")),
 "cygne": dict(et=["Deneb", "Sadr", "Fawaris", "Gienah", "eta Cyg", "Albireo"],
   tr=[(0, 1), (1, 2), (1, 3), (1, 4), (4, 5)],
   noms=dict(fr="le Cygne", de="der Schwan", es="el Cisne", en="Cygnus")),
 "fleche": dict(et=["Sham", "beta Sge", "delta Sge", "gamma Sge"],
   tr=[(0, 2), (1, 2), (2, 3)],
   noms=dict(fr="la Flèche", de="der Pfeil", es="la Flecha", en="Sagitta")),
 "pleiades": dict(et=["Alcyone", "Atlas", "Merope", "Electra", "Taygeta", "Maia"],
   tr=[(1, 0), (0, 2), (2, 3), (3, 4), (4, 5), (5, 0)],
   noms=dict(fr="les Pléiades", de="das Siebengestirn", es="las Siete Cabrillas", en="the Pleiades")),
 "couronne": dict(et=["theta CrB", "Nusakan", "Alphecca", "gamma CrB", "delta CrB", "eps CrB"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
   noms=dict(fr="la Couronne boréale", de="die Nördliche Krone", es="la Corona Boreal", en="Corona Borealis")),
 "cocher": dict(et=["Capella", "Menkalinan", "Mahasim", "Elnath", "Hassaleh", "Almaaz"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 5)],
   noms=dict(fr="le Cocher", de="der Fuhrmann", es="el Cochero", en="Auriga")),
 "cassiopee": dict(et=["Caph", "Schedar", "Navi", "Ruchbah", "Segin"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 4)],
   noms=dict(fr="Cassiopée", de="das Himmels-W", es="Casiopea", en="Cassiopeia")),
 "cephee": dict(et=["Alderamin", "Alfirk", "Errai", "iota Cep", "zeta Cep"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)],
   noms=dict(fr="Céphée", de="Kepheus", es="Cefeo", en="Cepheus")),
 "corbeau": dict(et=["Gienah Corvi", "Algorab", "Kraz", "Minkar"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 0)],
   noms=dict(fr="le Corbeau", de="der Rabe", es="el Cuervo", en="Corvus")),
 "dauphin": dict(et=["Sualocin", "gamma Del", "delta Del", "Rotanev", "Aldulfin"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)],
   noms=dict(fr="le Dauphin", de="der Delfin", es="el Delfín", en="Delphinus")),
 "pegase": dict(et=["Markab", "Scheat", "Alpheratz", "Algenib"],
   tr=[(0, 1), (1, 2), (2, 3), (3, 0)],
   noms=dict(fr="le Grand Carré de Pégase", de="das Herbstviereck", es="el Cuadrado de Pegaso", en="the Great Square of Pegasus")),
 "croix": dict(et=["Gacrux", "Acrux", "Mimosa", "delta Cru", "Ginan"],
   tr=[(0, 1), (2, 3)],
   noms=dict(fr="la Croix du Sud", de="das Kreuz des Südens", es="la Cruz del Sur", en="the Southern Cross")),
}

# Les groupes d'etapes de l'app qui ont deja leur figure (A1 voyage : les 12 escales, puis la suite de 10 etapes).
# Les groupes A2-C1 (etapes.json) les recevront quand l'app suivra leurs etapes.
GROUPES = {"a1_escales": "gemeaux", "a1_suite": "orion", "premiers_pas": "ourse"}

# La phrase de la distance, par langue d'interface (cles d'Intl.PluralRules ; « environ » pour une distance arrondie).
TEXTES_DISTANCE = {
    "fr": {"other": "à {n} années-lumière", "environ": "à environ {n} années-lumière"},
    "en": {"other": "{n} light-years away", "environ": "about {n} light-years away"},
    "de": {"other": "{n} Lichtjahre entfernt", "environ": "etwa {n} Lichtjahre entfernt"},
    "pt": {"other": "a {n} anos-luz", "environ": "a cerca de {n} anos-luz"},
    "tr": {"other": "{n} ışık yılı uzakta", "environ": "yaklaşık {n} ışık yılı uzakta"},
    "pl": {"one": "{n} rok świetlny stąd", "few": "{n} lata świetlne stąd", "many": "{n} lat świetlnych stąd",
           "other": "{n} lat świetlnych stąd", "environ": "około {n} lat świetlnych stąd"},
    "ru": {"one": "{n} световой год от Земли", "few": "{n} световых года от Земли", "many": "{n} световых лет от Земли",
           "other": "{n} световых лет от Земли", "environ": "около {n} световых лет от Земли"},
    "uk": {"one": "{n} світловий рік від Землі", "few": "{n} світлові роки від Землі", "many": "{n} світлових років від Землі",
           "other": "{n} світлових років від Землі", "environ": "близько {n} світлових років від Землі"},
    "ar": {"few": "على بعد {n} سنوات ضوئية", "many": "على بعد {n} سنةً ضوئية", "other": "على بعد {n} سنة ضوئية",
           "environ": "على بعد نحو {n} سنة ضوئية"},
    "fa": {"other": "در فاصلهٔ {n} سال نوری", "environ": "در فاصلهٔ حدود {n} سال نوری"},
}
