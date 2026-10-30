"""Les candidats BRESILIENS de la mosaique portugaise (30 oct. 2026).

Decide par Jacques le 30 oct. 2026 : le portugais du Bresil entre en variante
(« J'aimerais qu'on entre aussi l'aspect portugais-Bresil. En apprentissage. »),
comme l'americain et le britannique pour l'anglais. La mosaique suit l'espagnol
(Espagne + Amerique latine) : des peintres du Portugal ET du Bresil, sur la meme
page de choix. Ceux du Portugal restent dans candidats.json (1-74, E1-E85) ;
ceux du Bresil vont dans candidats-bresil.json, numerotes B1... et BE1..., pour
que la premiere numerotation ne bouge pas.

REGLE DE DROIT, la meme que pour le Portugal : peintre MORT AVANT 1926, libre
partout (le Mexique protege 100 ans). Le Bresil protege 70 ans apres la mort,
compte a partir du 1er janvier suivant (loi 9.610/98, art. 41) : un peintre mort
en 1955 ou avant est libre au Bresil en 2026, comme en Europe. Ceux qui sont
morts entre 1926 et 1955 forment donc le groupe a decider (BE1...), oeuvres
d'avant 1931 seulement. Ce n'est pas un avis juridique, c'est une marge de prudence.

Peintres nes ailleurs mais faits bresiliens (Castagneto, Facchinetti, Taunay,
Grimm, Andersen, Brocos) : la peinture bresilienne du XIXe siecle leur doit
beaucoup, ils sont gardes. Les voyageurs de passage (Debret, Rugendas, Ender)
ne le sont pas.

Relancer : python portugais/mosaique/recolter_bresil.py
  ->  candidats-bresil.json + recolte-bresil.txt (vignettes dans le meme dossier brut).
"""
import re
import recolter

PEINTRES = [
    # morts avant 1926 : libres partout (B1...)
    ("Almeida Júnior", "Q569859", 25),
    ("Giovanni Battista Castagneto", "Q1401969", 15),
    ("Arthur Timótheo da Costa", "Q16494471", 12),
    ("Nicolau Facchinetti", "Q10336739", 10),
    ("Antônio Rafael Pinto Bandeira", "Q13384943", 10),
    ("Victor Meirelles", "Q727060", 8),
    ("Agostinho José da Mota", "Q14244088", 8),
    ("Pedro Américo", "Q540219", 6),       # surtout batailles et histoire
    ("Aurélio de Figueiredo", "Q9638354", 6),
    ("Antônio Firmino Monteiro", "Q8961727", 5),
    ("Abigail de Andrade", "Q8184049", 5),
    ("Félix Taunay", "Q3092622", 4),
    ("Georg Grimm", "Q833722", 6),
    ("Estêvão Silva", "Q1370813", 3),
    ("João Zeferino da Costa", "Q3187332", 3),
    ("Augusto Rodrigues Duarte", "Q13473237", 3),
    ("Manuel de Araújo Porto-Alegre", "Q1797092", 3),
    # morts entre 1926 et 1955 : a decider (BE1...)
    ("Eliseu Visconti", "Q2340277", 25),
    ("Antônio Parreiras", "Q612023", 20),
    ("Benedito Calixto", "Q3325858", 15),
    ("Belmiro de Almeida", "Q9653726", 10),
    ("Rodolfo Amoedo", "Q153845", 10),
    ("Oscar Pereira da Silva", "Q3357022", 8),
    ("Pedro Weingärtner", "Q634371", 8),
    ("Henrique Bernardelli", "Q9002927", 8),
    ("Pedro Alexandrino", "Q10347301", 6),
    ("Lucílio de Albuquerque", "Q6698662", 6),
    ("Alfredo Andersen", "Q4582950", 6),
    ("Bertha Worms", "Q16498026", 5),
    ("Décio Villares", "Q10269292", 4),
    ("Modesto Brocos", "Q10331431", 3),
    ("Antônio Garcia Bento", "Q10288297", 2),
]

# Une categorie qui n'existe pas rend une liste vide : sans danger.
CATEGORIES = {
    "Almeida Júnior": ["Paintings by Almeida Júnior"],
    "Giovanni Battista Castagneto": ["Paintings by Giovanni Battista Castagneto"],
    "Nicolau Facchinetti": ["Paintings by Nicolau Facchinetti"],
    "Georg Grimm": ["Paintings by Georg Grimm"],
    "Arthur Timótheo da Costa": ["Paintings by Arthur Timótheo da Costa"],
    "Antônio Parreiras": ["Paintings by Antônio Parreiras"],
    "Pedro Weingärtner": ["Paintings by Pedro Weingärtner"],
}

# Le filtre du Portugal, plus ce que l'histoire bresilienne ajoute :
# execution de Tiradentes, fusillades, naufrages, suicide, esclaves chaties.
EXCLUS = re.compile(recolter.EXCLUS.pattern + r"|esquartej|fuzila|execu[cç][aã]o|naufr[aá]g|suic[ií]d|"
                    r"castigo|chicot|açoit|a[cç]oite|enforc|tiradentes", re.I)

# Ecartes a l'oeil (numeros de la premiere recolte du 30 oct.).
EXCLUS_ID = {
    'c1baedc5e6fe5',  # B4    Almeida Júnior : doublon de O Violeiro
    'c7462bd4dd77c',  # B5    Almeida Júnior : doublon de O Violeiro
    'c83d41b6ae37f',  # B36   Almeida Júnior : doublon de O Violeiro
    'Q76517972',      # B6    Arthur Timótheo da Costa : etude de tetes
    'Q59826089',      # B7    Félix Taunay : dessin sur papier, avec la marge
    'Q59826256',      # B9    Félix Taunay : dessin sur papier, avec la marge
    'c3374cabe4600',  # B11   Almeida Júnior : doublon de Marinha, Guaruja
    'Q49870361',      # B22   Pedro Américo : allegorie aux figures nues
    'Q19860067',      # B29   Almeida Júnior : doublon de Ponte da Tabatinguera
    'Q130543818',     # B32   Arthur Timótheo da Costa : enfant deshabille
    'Q59824384',      # B35   Manuel de Araújo Porto-Alegre : illisible (sepia sombre)
    'Q43387023',      # B40   Victor Meirelles : bataille
    'Q111578002',     # B43   Agostinho José da Mota : ovale (et Rome)
    'Q59856705',      # B55   Nicolau Facchinetti : ovale
    'Q59856708',      # B63   Nicolau Facchinetti : ovale
    'Q76148718',      # B58   Arthur Timótheo da Costa : figure a terre, sujet trouble
    'Q111821694',     # B70   João Zeferino da Costa : charite, religieuse
    'c4a57e3c21f71',  # B73   Almeida Júnior : photo de salle de musee
    'Q19860023',      # B76   Almeida Júnior : doublon de Cena de familia
    'Q129263109',     # BE2   Antônio Parreiras : nu
    'Q62063579',      # BE14  Eliseu Visconti : plafond, allegorie
    'Q62064729',      # BE26  Eliseu Visconti : tranchees
    'Q62063584',      # BE27  Eliseu Visconti : lunette sepia avec son cadre
    'Q62063606',      # BE30  Eliseu Visconti : rideau de theatre, allegorie
    'Q62064795',      # BE32  Eliseu Visconti : plafond
    'Q62092665',      # BE33  Eliseu Visconti : nu
    'Q132197492',     # BE37  Benedito Calixto : religieux (saint Paul)
    'Q49868587',      # BE46  Antônio Parreiras : nu (Iracema)
    'Q129332642',     # BE49  Antônio Parreiras : arrestation
    'Q129307441',     # BE64  Antônio Parreiras : suicide (Fim de romance)
    'Q49844168',      # BE66  Rodolfo Amoedo : nu
    'Q129263119',     # BE71  Antônio Parreiras : nu
    'Q112052341',     # BE75  Pedro Weingärtner : nymphes nues
    'Q42571365',      # BE85  Rodolfo Amoedo : mort (O Ultimo Tamoio)
    'Q49844091',      # BE87  Rodolfo Amoedo : morte (Desdemona)
    'Q49843805',      # BE88  Rodolfo Amoedo : nus (Philoctete)
    'Q128710148',     # BE70  Antônio Parreiras : proces avant execution (Filipe dos Santos)
    'Q129307912',     # BE34  Antônio Parreiras : croquis
    # deuxieme passage (numeros de la deuxieme recolte)
    'Q130543810',     # B54   Arthur Timótheo da Costa : nu
    'c448fc2ca12ec',  # B71   Almeida Júnior : portrait posthume (la morte)
    'Q62064463',      # BE35  Eliseu Visconti : triptyque allegorique
    'Q129263092',     # BE68  Antônio Parreiras : nu
    'Q119361408',     # BE70  Antônio Parreiras : doublon de Fim de romance
    'Q56878623',      # BE73  Antônio Parreiras : nu
    # troisieme passage
    'Q129264045',     # BE74  Antônio Parreiras : bandeirante mourant (Cacador de esmeraldas)
}

SIGNATURES = r"Almeida|J[uú]nior|Castagneto|Timóteo|Timótheo|Facchinetti|Bandeira|Meirelles|Mota|" \
             r"Am[eé]rico|Figueiredo|Monteiro|Andrade|Taunay|Grimm|Zeferino|Duarte|Porto[- ]Alegre|" \
             r"Visconti|Parreiras|Calixto|Amoedo|Pereira da Silva|Weing[aä]rtner|Bernardelli|" \
             r"Alexandrino|Albuquerque|Andersen|Worms|Villares|Brocos|Bento"

if __name__ == "__main__":
    recolter.SIGNATURES = SIGNATURES
    recolter.main(PEINTRES, CATEGORIES, EXCLUS_ID, EXCLUS,
                  prefixes=(("libre", "B"), ("europe", "BE")),
                  sortie="candidats-bresil.json", recolte="recolte-bresil.txt")
