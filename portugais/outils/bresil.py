# -*- coding: utf-8 -*-
"""Du portugais du Portugal au portugais du BRESIL : la variante d'apprentissage.

Decide par Jacques le 30 oct. 2026 (« J'aimerais qu'on entre aussi l'aspect
portugais-Bresil. En apprentissage. »), sur le modele de l'anglais americain /
britannique : deux jeux de donnees complets, MEMES mots dans le MEME ordre,
portugais/datos (Portugal, la base) et portugais/datos-br (Bresil, la variante).

Les sources du cours sont ecrites en portugais d'Europe (l'A1 directement, les
niveaux A2-C1 convertis puis corriges a la main). La variante bresilienne est
donc DERIVEE de la sortie europeenne, par construire.py :

  brasileiro(texte)   -> le texte portugais converti (vocabulaire, orthographe,
                         estar a + infinitif -> gerondif, pronom devant le verbe,
                         « O meu carro » -> « Meu carro » en tete de phrase)
  construire(jeu)     -> (jeu_br, rapport) : tous les fichiers de datos/ en
                         version bresilienne

Ce qui n'est pas converti mais signale (rapport) : « tu » et sa conjugaison (le
Bresil dit surtout « voce » + 3e personne, mais « tu » vit au Sud et au Nord-Est),
les pronoms complements apres le verbe (« comprá-lo », correct a l'ecrit), et
toute phrase ou un nom a change de genre (l'adjectif qui suit n'est pas accorde).

Les explications en francais qui opposent le Portugal au Bresil sont reecrites a
la main dans bresil_textes.py ; une explication qui en parle encore sans
reecriture est signalee. Les questions d'exercice qui enseignent un usage du
Portugal (« Au Portugal : ... ») ne passent pas dans la variante.

BROUILLON : a faire relire par un lusophone du Bresil (l'ancien etudiant de Jacques).
"""
import copy, random, re

import bresil_textes as T

# ------------------------------------------------------------------ les noms
# « pt | pluriel | genre > br | pluriel | genre », puis des drapeaux :
#   !carte  le mot n'est change que sur sa carte (sens double dans une phrase)
#   !det    dans une phrase, seulement apres un determinant (o gelado, mais
#           « esta gelado » reste)
# Le genre change parfois (a paragem -> o ponto) : les determinants qui
# precedent sont accordes.
NOMS = """
divisão | divisões | a > cômodo | cômodos | o !carte
casa de banho | casas de banho | a > banheiro | banheiros | o
candeeiro de pé | candeeiros de pé | o > luminária de chão | luminárias de chão | a
candeeiro de rua | candeeiros de rua | o > poste de luz | postes de luz | o
penso rápido | pensos rápidos | o > curativo | curativos | o
candeeiro | candeeiros | o > abajur | abajures | o
frigorífico | frigoríficos | o > geladeira | geladeiras | a
lava-loiça | lava-loiças | o > pia | pias | a
máquina da loiça | máquinas da loiça | a > lava-louças | lava-louças | a
duche | duches | o > chuveiro | chuveiros | o
almofada | almofadas | a > travesseiro | travesseiros | o !carte
telemóvel | telemóveis | o > celular | celulares | o
comando | comandos | o > controle remoto | controles remotos | o !carte
rés-do-chão | — | o > térreo | — | o
bebé | bebés | o > bebê | bebês | o
rapariga | raparigas | a > moça | moças | a
apelido | apelidos | o > sobrenome | sobrenomes | o
pequeno-almoço | pequenos-almoços | o > café da manhã | cafés da manhã | o
sumo | sumos | o > suco | sucos | o
gelado | gelados | o > sorvete | sorvetes | o !det
sandes | sandes | a > sanduíche | sanduíches | o
chávena | chávenas | a > xícara | xícaras | a
empregado de mesa | empregados de mesa | o > garçom | garçons | o
empregada de mesa | empregadas de mesa | a > garçonete | garçonetes | a
fiambre | — | o > presunto | — | o
centro de saúde | centros de saúde | o > posto de saúde | postos de saúde | o
constipação | constipações | a > resfriado | resfriados | o
t-shirt | t-shirts | a > camiseta | camisetas | a
camisola | camisolas | a > suéter | suéteres | o !carte
saldos | — | os > liquidação | — | a !carte
calças de ganga | — | as > calça jeans | — | a !carte
autocarro | autocarros | o > ônibus | ônibus | o
paragem de autocarro | paragens de autocarro | a > ponto de ônibus | pontos de ônibus | o
paragem | paragens | a > ponto | pontos | o
metro | metros | o > metrô | metrôs | o !carte
comboio | comboios | o > trem | trens | o
elétrico | elétricos | o > bonde | bondes | o !det
bilhete | bilhetes | o > passagem | passagens | a !carte
passadeira | passadeiras | a > faixa de pedestres | faixas de pedestres | a
risca | riscas | a > listra | listras | a !carte
cãozinho | cãezinhos | o > cachorrinho | cachorrinhos | o
cão | cães | o > cachorro | cachorros | o
morada | moradas | a > endereço | endereços | o
ementa | ementas | a > cardápio | cardápios | o
dose | doses | a > porção | porções | a !carte
bica | bicas | a > cafezinho | cafezinhos | o
galão | galões | o > café com leite | cafés com leite | o
tosta mista | tostas mistas | a > misto-quente | mistos-quentes | o
saco de plástico | sacos de plástico | o > sacola plástica | sacolas plásticas | a
saco | sacos | o > sacola | sacolas | a !carte
talão | talões | o > recibo | recibos | o
montra | montras | a > vitrine | vitrines | a
empregado | empregados | o > vendedor | vendedores | o !carte
empregada | empregadas | a > vendedora | vendedoras | a !carte
talho | talhos | o > açougue | açougues | o
talhante | talhantes | o > açougueiro | açougueiros | o
mota | motas | a > moto | motos | a
camião | camiões | o > caminhão | caminhões | o
condutora | condutoras | a > motorista | motoristas | a
condutor | condutores | o > motorista | motoristas | o
carrinha | carrinhas | a > van | vans | a
ordenado | ordenados | o > salário | salários | o !det
desporto | desportos | o > esporte | esportes | o
equipa | equipas | a > equipe | equipes | a
ginásio | ginásios | o > academia | academias | a
fotografia | fotografias | a > foto | fotos | a !carte
pasta de dentes | pastas de dentes | a > pasta de dente | pastas de dente | a
champô | champôs | o > xampu | xampus | o
curgete | curgetes | a > abobrinha | abobrinhas | a
relvado | relvados | o > gramado | gramados | o
relva | relvas | a > grama | gramas | a
ecrã | ecrãs | o > tela | telas | a
utilizadora | utilizadoras | a > usuária | usuárias | a
utilizador | utilizadores | o > usuário | usuários | o
ficheiro | ficheiros | o > arquivo | arquivos | o
agrafador | agrafadores | o > grampeador | grampeadores | o
fita-cola | — | a > fita adesiva | — | a
esferográfica | esferográficas | a > caneta | canetas | a
pastilha elástica | pastilhas elásticas | a > chiclete | chicletes | o
rebuçado | rebuçados | o > bala | balas | a
ananás | ananases | o > abacaxi | abacaxis | o
pimento | pimentos | o > pimentão | pimentões | o
beringela | beringelas | a > berinjela | berinjelas | a
cebolinho | — | o > cebolinha | — | a
feijão-verde | — | o > vagem | vagens | a
alperce | alperces | o > damasco | damascos | o
espargo | espargos | o > aspargo | aspargos | o
tacho | tachos | o > panela | panelas | a
natas | — | as > creme de leite | — | o
estore | estores | o > persiana | persianas | a
alcatifa | alcatifas | a > carpete | carpetes | o
autoclismo | autoclismos | o > descarga | descargas | a
sanita | sanitas | a > vaso sanitário | vasos sanitários | o
esquentador | esquentadores | o > aquecedor | aquecedores | o
guarda-redes | guarda-redes | o > goleiro | goleiros | o
golo | golos | o > gol | gols | o
adepta | adeptas | a > torcedora | torcedoras | a
adepto | adeptos | o > torcedor | torcedores | o
hospedeira de bordo | hospedeiras de bordo | a > comissária de bordo | comissárias de bordo | a
carta de condução | cartas de condução | a > carteira de motorista | carteiras de motorista | a
travão | travões | o > freio | freios | o
peão | peões | o > pedestre | pedestres | o
portagem | portagens | a > pedágio | pedágios | o
boleia | boleias | a > carona | caronas | a
autoestrada | autoestradas | a > rodovia | rodovias | a
bomba de gasolina | bombas de gasolina | a > posto de gasolina | postos de gasolina | o
caixote do lixo | caixotes do lixo | o > lixeira | lixeiras | a
caixa multibanco | caixas multibanco | a > caixa eletrônico | caixas eletrônicos | o
multibanco | multibancos | o > caixa eletrônico | caixas eletrônicos | o
código postal | códigos postais | o > CEP | CEPs | o
cartão de cidadão | cartões de cidadão | o > carteira de identidade | carteiras de identidade | a
cartão de utente | cartões de utente | o > cartão do SUS | cartões do SUS | o
centro comercial | centros comerciais | o > shopping | shoppings | o
câmara municipal | câmaras municipais | a > prefeitura | prefeituras | a
presidente da câmara | presidentes da câmara | o > prefeito | prefeitos | o
esquadra | esquadras | a > delegacia | delegacias | a
conservatória | conservatórias | a > cartório | cartórios | o
urgências | — | as > pronto-socorro | — | o
papaia | papaias | a > mamão | mamões | o
liquidificadora | liquidificadoras | a > liquidificador | liquidificadores | o
propina | propinas | a > mensalidade | mensalidades | a
miúda | miúdas | a > garota | garotas | a
miúdo | miúdos | o > garoto | garotos | o
reformada | reformadas | a > aposentada | aposentadas | a
reformado | reformados | o > aposentado | aposentados | o
sítio | sítios | o > lugar | lugares | o
fato de banho | fatos de banho | o > maiô | maiôs | o
fato de treino | fatos de treino | o > agasalho | agasalhos | o
fato | fatos | o > terno | ternos | o
calções de banho | — | os > sunga | — | a
calções | — | os > bermuda | — | a
sapatilhas | — | as > tênis | — | os
peúgas | — | as > meias | — | as
soutien | soutiens | o > sutiã | sutiãs | o
biberão | biberões | o > mamadeira | mamadeiras | a
guiché | guichés | o > guichê | guichês | o
quadro de giz | quadros de giz | o > lousa | lousas | a
renda | rendas | a > aluguel | aluguéis | o !det
senhoria | senhorias | a > proprietária | proprietárias | a
senhorio | senhorios | o > proprietário | proprietários | o
penso | pensos | o > curativo | curativos | o !det
ligadura | ligaduras | a > atadura | ataduras | a
parque de estacionamento | parques de estacionamento | o > estacionamento | estacionamentos | o
loiça | — | a > louça | — | a
guitarra | guitarras | a > violão | violões | o
quinta | quintas | a > fazenda | fazendas | a !carte
secretária | secretárias | a > escrivaninha | escrivaninhas | a !carte
banca | bancas | a > barraca | barracas | a !carte
"""

# Une carte qui porte un de ces mots ne change que si sa traduction le confirme
# (« a quinta » est la ferme, pas jeudi ; « a secretária » le bureau-meuble).
CARTE_SI = {"quinta": "ferme", "secretária": "bureau", "banca": "étal", "empregado": "vendeu",
            "empregada": "vendeu", "saco": "sac", "fotografia": "photo", "dose": "portion"}


def _lire_noms():
    out = []
    for ligne in NOMS.strip().splitlines():
        ligne, _, drapeaux = ligne.partition("!")
        gauche, droite = ligne.split(">")
        pt, ptpl, ptg = [x.strip() for x in gauche.split("|")]
        br, brpl, brg = [x.strip() for x in droite.split("|")]
        out.append({"pt": pt, "ptpl": ptpl, "ptg": ptg, "br": br, "brpl": brpl, "brg": brg,
                    "drapeau": drapeaux.strip()})
    return out


NOMS_LUS = _lire_noms()
NOM_PAR_MOT = {n["pt"]: n for n in NOMS_LUS}

# ------------------------------------------------------------------ les autres mots
# Adjectifs, locutions, noms propres, orthographe : sans accord a faire.
MOTS = [
    # adjectifs
    ("cinzento", "cinza"), ("cinzenta", "cinza"), ("cinzentos", "cinza"), ("cinzentas", "cinza"),
    ("solarengo", "ensolarado"), ("solarenga", "ensolarada"), ("solarengos", "ensolarados"), ("solarengas", "ensolaradas"),
    ("canadiano", "canadense"), ("canadiana", "canadense"), ("canadianos", "canadenses"), ("canadianas", "canadenses"),
    ("constipado", "resfriado"), ("constipada", "resfriada"), ("constipados", "resfriados"), ("constipadas", "resfriadas"),
    ("fixe", "legal"), ("fixes", "legais"), ("desportivo", "esportivo"), ("desportiva", "esportiva"),
    ("desportivos", "esportivos"), ("desportivas", "esportivas"), ("desportista", "esportista"), ("desportistas", "esportistas"),
    # locutions
    ("se faz favor", "por favor"), ("Se faz favor", "Por favor"), ("faz favor", "por favor"), ("Faz favor", "Por favor"),
    ("festa de anos", "festa de aniversário"), ("festas de anos", "festas de aniversário"),
    ("faço anos", "faço aniversário"), ("fazes anos", "fazes aniversário"), ("faz anos", "faz aniversário"),
    ("fazer anos", "fazer aniversário"), ("fez anos", "fez aniversário"), ("fazemos anos", "fazemos aniversário"),
    ("Adeus", "Tchau"), ("em casa de", "na casa de"),
    ("calças de ganga", "calças jeans"), ("contrato de renda", "contrato de aluguel"),
    ("contratos de renda", "contratos de aluguel"), ("conta à ordem", "conta corrente"),
    ("contas à ordem", "contas correntes"), ("mais pequeno", "menor"), ("mais pequena", "menor"),
    ("mais pequenos", "menores"), ("mais pequenas", "menores"),
    ("de França", "da França"), ("em França", "na França"), ("De França", "Da França"), ("Em França", "Na França"), ("guitarra elétrica", "guitarra elétrica"),
    ("guitarras elétricas", "guitarras elétricas"),
    # noms propres
    ("Irão", "Irã"), ("Moscovo", "Moscou"), ("Teerão", "Teerã"), ("Nova Iorque", "Nova York"),
    ("Madrid", "Madri"), ("Amesterdão", "Amsterdã"), ("Vietname", "Vietnã"),
    # orthographe
    ("facto", "fato"), ("factos", "fatos"), ("de facto", "de fato"),
    ("contacto", "contato"), ("contactos", "contatos"), ("receção", "recepção"), ("receções", "recepções"),
    ("rececionista", "recepcionista"), ("rececionistas", "recepcionistas"), ("conceção", "concepção"),
    ("perceção", "percepção"), ("aspeto", "aspecto"), ("aspetos", "aspectos"),
    ("espetador", "espectador"), ("espetadores", "espectadores"), ("espetadora", "espectadora"),
    ("registo", "registro"), ("registos", "registros"), ("húmido", "úmido"), ("húmida", "úmida"),
    ("húmidos", "úmidos"), ("húmidas", "úmidas"), ("humidade", "umidade"), ("excecional", "excepcional"),
    ("excecionais", "excepcionais"), ("detetar", "detectar"), ("connosco", "conosco"),
    ("dezasseis", "dezesseis"), ("dezassete", "dezessete"), ("dezanove", "dezenove"),
    ("puré", "purê"), ("croché", "crochê"), ("comité", "comitê"), ("judo", "judô"), ("karaté", "caratê"),
    ("ténis", "tênis"), ("planeamento", "planejamento"), ("ótimo", "ótimo"),
]

# Les verbes qui changent : la forme europeenne -> la forme bresilienne, faite
# par echange du radical (conduz-o -> dirij-o). Chaque forme vue dans les
# cartes de ces verbes est convertie, dans les cartes et dans les phrases.
VERBES = {"perceber": ("perceb", "entend"), "conduzir": ("conduz", "dirig"), "registar": ("regist", "registr"),
          "planear": ("plane", "planej"), "magoar": ("mago", "machuc"), "magoar-se": ("mago", "machuc"),
          "apanhar": ("apanh", "peg")}
# « apanhar » n'est le « pegar » bresilien que devant un transport.
APANHAR_DEVANT = r"(?:o|a|um|uma)\s+(?:autocarro|comboio|metro|elétrico|táxi|avião|barco|ferry|ônibus|trem|metrô|bonde)"


def _graphie(radical, fin):
    """Le radical bresilien devant sa terminaison : peg + ei -> peguei,
    machuc + ei -> machuquei, dirig + o -> dirijo."""
    if not fin:
        return radical
    if fin[0] in "eéiê":
        if radical.endswith("c"):
            return radical[:-1] + "qu"
        if radical.endswith("g") and not radical.endswith("rig"):
            return radical[:-1] + "gu"
    if fin[0] in "aoáó" and radical.endswith("rig"):
        return radical[:-1] + "j"
    return radical


def forme_verbe(forme, pt, br):
    """conduzo -> dirijo ; planeio -> planejo ; apanhei -> peguei."""
    if not forme.lower().startswith(pt):
        return None
    reste = forme[len(pt):]
    if pt == "plane" and reste.startswith("i"):
        reste = reste[1:]                      # planeio -> planej-o
    if pt == "conduz" and reste == "":
        sortie = "dirige"
    else:
        sortie = _graphie(br, reste) + reste
    return sortie[0].upper() + sortie[1:] if forme[:1].isupper() else sortie


# Les terminaisons d'un verbe : une forme n'est convertie que si son reste en
# est une (« planeta » n'est pas une forme de planear).
FINALES = ("o as a amos ais am ei aste ou ámos amos astes aram ava avas ávamos áveis avam e es emos eis em "
           "ar ares armos ardes arem arei arás ará aremos areis arão aria arias aríamos aríeis ariam "
           "asse asses ássemos ásseis assem ando ado ada ados adas i este eu estes eram ia ias íamos íeis iam "
           "er eres ermos erem erei erás erá eremos erão eria erias eríamos eriam esse esses êssemos essem "
           "endo ido ida idos idas imos is iste iu istes iram ir ires irmos irem irei irás irá iremos irão "
           "iria irias iríamos iriam isse isses íssemos issem indo").split()
_FORME = re.compile(r"(?<![\w-])(" + "|".join(sorted({p for p, b in VERBES.values() if p != "apanh"}, key=len, reverse=True))
                    + r")(i?)(" + "|".join(sorted(FINALES, key=len, reverse=True)) + r")?(?![\wà-ú])", re.I)


def _formes_verbes(t):
    def rep(m):
        pt, i, fin = m.group(1), m.group(2), m.group(3) or ""
        if i and pt.lower() != "plane":
            return m.group(0)
        if not fin and pt.lower() != "conduz":
            return m.group(0)
        br = next(b for p, b in VERBES.values() if p == pt.lower())
        return forme_verbe(m.group(0), pt.lower(), br) or m.group(0)
    return _FORME.sub(rep, t)


# ------------------------------------------------------------------ les determinants
# Pour accorder ce qui precede un nom qui change de genre ou de nombre.
DET_SERIES = [
    ("o", "a", "os", "as"), ("um", "uma", "uns", "umas"), ("do", "da", "dos", "das"),
    ("no", "na", "nos", "nas"), ("ao", "à", "aos", "às"), ("pelo", "pela", "pelos", "pelas"),
    ("num", "numa", "nuns", "numas"), ("dum", "duma", "duns", "dumas"),
    ("este", "esta", "estes", "estas"), ("esse", "essa", "esses", "essas"),
    ("aquele", "aquela", "aqueles", "aquelas"), ("deste", "desta", "destes", "destas"),
    ("desse", "dessa", "desses", "dessas"), ("daquele", "daquela", "daqueles", "daquelas"),
    ("neste", "nesta", "nestes", "nestas"), ("nesse", "nessa", "nesses", "nessas"),
    ("naquele", "naquela", "naqueles", "naquelas"), ("meu", "minha", "meus", "minhas"),
    ("teu", "tua", "teus", "tuas"), ("seu", "sua", "seus", "suas"), ("nosso", "nossa", "nossos", "nossas"),
    ("outro", "outra", "outros", "outras"), ("novo", "nova", "novos", "novas"),
    ("primeiro", "primeira", "primeiros", "primeiras"), ("próximo", "próxima", "próximos", "próximas"),
    ("velho", "velha", "velhos", "velhas"), ("bom", "boa", "bons", "boas"), ("muito", "muita", "muitos", "muitas"),
    ("pouco", "pouca", "poucos", "poucas"), ("todo", "toda", "todos", "todas"),
    ("algum", "alguma", "alguns", "algumas"), ("nenhum", "nenhuma", "nenhuns", "nenhumas"),
]
DET = {}
for serie in DET_SERIES:
    for i, f in enumerate(serie):
        DET.setdefault(f, (serie, "m" if i in (0, 2) else "f", "s" if i < 2 else "p"))


def _genre_nombre(g, forme_pl):
    """(genre, nombre) d'une entree : g vaut o, a, os ou as."""
    return ("m" if g.startswith("o") else "f", "p" if forme_pl or len(g) == 2 else "s")


def _accorder(det, g, n):
    serie = DET[det.lower()][0]
    f = serie[(0 if g == "m" else 1) + (0 if n == "s" else 2)]
    return f[0].upper() + f[1:] if det[:1].isupper() else f


# ------------------------------------------------------------------ le motif unique
# Une seule passe, toutes les cles a la fois : sans cela, facto -> fato puis
# fato -> terno feraient « terno » d'un « facto ».
_CLES = {}


def _ajouter(cle, valeur):
    if cle and cle != "—" and cle not in _CLES:
        _CLES[cle] = valeur


for n in NOMS_LUS:
    if n["drapeau"] == "carte":
        continue
    _ajouter(n["pt"], ("nom", n, False))
    if n["ptpl"] not in ("—", n["pt"]):
        _ajouter(n["ptpl"], ("nom", n, True))
for a, b in MOTS:
    _ajouter(a, ("mot", b))

_DET_RE = "|".join(sorted((re.escape(d) for d in DET), key=len, reverse=True))


def _motif():
    cles = sorted(_CLES, key=len, reverse=True)
    return re.compile(r"(?<![\w-])((?:(?:" + _DET_RE + r")\s+){0,2})(" + "|".join(re.escape(c) for c in cles) + r")(?![\w-])",
                      re.I)


_MOTIF = [None]


def _remplacer(texte, alertes):
    if _MOTIF[0] is None:
        _MOTIF[0] = _motif()

    def rep(m):
        dets, mot = m.group(1), m.group(2)
        cle = mot if mot in _CLES else (mot.lower() if mot.lower() in _CLES else mot[0].lower() + mot[1:])
        val = _CLES.get(cle)
        if not val:
            return m.group(0)
        if val[0] == "mot":
            b = val[1]
            return dets + (b[0].upper() + b[1:] if mot[0].isupper() and not b[0].isupper() else b)
        n, pl = val[1], val[2]
        mots_det = dets.split()
        if n["drapeau"] == "det" and not mots_det:
            return m.group(0)
        br = n["brpl"] if pl and n["brpl"] != "—" else n["br"]
        g0, n0 = _genre_nombre(n["ptg"], pl)
        g1, n1 = _genre_nombre(n["brg"], pl and n["brpl"] != "—")
        if (g0, n0) != (g1, n1) and mots_det:
            mots_det = [_accorder(d, g1, n1) if d.lower() in DET else d for d in mots_det]
            alertes.add("genre")
        sortie = br[0].upper() + br[1:] if mot[0].isupper() and not mots_det else br
        return (" ".join(mots_det) + " " if mots_det else "") + sortie
    return _MOTIF[0].sub(rep, texte)


# ------------------------------------------------------------------ la syntaxe
CLITIQUES = "me|te|se|nos|lhe|lhes"
INFINITIFS = set()


def connaitre_infinitifs(verbes_json):
    for niveau in verbes_json.values():
        for v in niveau:
            inf = v.get("infinitif", "").replace("-se", "")
            if inf:
                INFINITIFS.add(inf)
    INFINITIFS.update(["ser", "ir", "ver", "ler", "ter", "vir", "pôr", "dar", "rir"])


def gerundio(inf):
    if inf == "pôr" or inf.endswith("por"):
        return inf[:-3] + "pondo" if inf != "pôr" else "pondo"
    return inf[:-2] + {"ar": "ando", "er": "endo", "ir": "indo"}.get(inf[-2:], inf[-2:])


ESTAR = (r"(?:est(?:ou|ás|á|amos|ão|ava|avas|ávamos|avam|ive|eve|ivemos|iveram|ar|arei|ará|aria|eja|ejam|ivesse|ivessem|ando|ado)"
         r"|and(?:o|as|a|amos|am|ava|avam|ei|ou|ar)|continu(?:o|as|a|amos|am|ou|ava|ar)|fic(?:o|as|a|amos|am|ou|ava|ar|ei|aram))")
_PROGRESSIF = re.compile(r"\b(" + ESTAR + r") a ([a-zà-ú]+)(?:-(" + CLITIQUES + r"))?\b", re.I)


def _progressif(t):
    """Estou a ler -> Estou lendo ; Está a vestir-se -> Está se vestindo."""
    def rep(m):
        aux, inf, cl = m.group(1), m.group(2), m.group(3)
        if inf.lower() not in INFINITIFS:
            return m.group(0)
        return aux + " " + (cl + " " if cl else "") + gerundio(inf.lower())
    return _PROGRESSIF.sub(rep, t)


_MESOCLISE = re.compile(r"\b([a-zà-ú]+r)-(" + CLITIQUES + r")-(ei|ás|á|emos|eis|ão|ia|ias|íamos|íeis|iam)\b", re.I)
_ENCLISE = re.compile(r"(?<![\w-])([A-Za-zà-úÀ-Ú]+)-(" + CLITIQUES + r")(?![\w-])(\s+[a-zà-ú]+)?")


def _proclise(t, garder_imperatif=False):
    """Chamo-me Ana -> Me chamo Ana ; vou-me deitar -> vou me deitar ;
    dar-te-ei -> te darei. Le Bresil met le petit pronom devant le verbe."""
    def meso(m):
        v, cl, fin = m.group(1), m.group(2), m.group(3)
        sortie = cl + " " + v.lower() + fin
        return sortie[0].upper() + sortie[1:] if v[:1].isupper() else sortie
    t = _MESOCLISE.sub(meso, t)
    if garder_imperatif:
        return t

    def encl(m):
        v, cl, suite = m.group(1), m.group(2), m.group(3) or ""
        if cl == "nos" and v.lower().endswith("mo"):
            v = v + "s"
        nu = suite.strip().lower()
        if nu and (nu in INFINITIFS or nu.replace("-", "") in INFINITIFS):
            return v + " " + cl + suite        # vou-me deitar -> vou me deitar
        haut = v[:1].isupper()
        sortie = cl + " " + (v[0].lower() + v[1:] if haut else v)
        if haut:
            sortie = sortie[0].upper() + sortie[1:]
        return sortie + suite
    return _ENCLISE.sub(encl, t)


_POSS_DEBUT = re.compile(r"(^|[.!?]\s+|—\s*|«\s*)(O|A|Os|As) (meu|minha|meus|minhas|teu|tua|teus|tuas|nosso|nossa|nossos|nossas)\b")


def _possessif(t):
    """« A minha mae chama-se Ana » -> « Minha mae... » : en tete de phrase, le
    Bresil laisse tomber l'article."""
    return _POSS_DEBUT.sub(lambda m: m.group(1) + m.group(3)[0].upper() + m.group(3)[1:], t)


# « Tenho de sair » -> « Tenho que sair » : la forme courante du Bresil.
_TER_DE = re.compile(r"\b(tenho|tens|tem|temos|têm|tinha|tinhas|tínhamos|tinham|tive|teve|tivemos|tiveram|ter|terá|teria|"
                     r"teremos|tenha|tenhamos|tenham|tivesse|Tenho|Tem|Temos|Têm|Tinha|Tive|Teve) de ([a-zà-ú]+)\b")
_FERME = re.compile(r"[éó](?=[mn][aeiouáéíóúâêôãõ])")
_ACEITE = re.compile(r"\b(foi|foram|é|são|ser|sido|está|estão|estava|tinha|tenho|tem|têm|tinham|era|eram|seria|será|fosse) aceite(s?)\b", re.I)


def brasileiro(texte, alertes=None, imperatif=False):
    """Le texte portugais du Portugal en portugais du Bresil."""
    if not texte or not isinstance(texte, str):
        return texte
    alertes = alertes if alertes is not None else set()
    t = re.sub(r"\b(apanh\w*)(?=\s+" + APANHAR_DEVANT + ")",
               lambda m: forme_verbe(m.group(1), "apanh", "peg") or m.group(1), texte, flags=re.I)
    t = re.sub(r"\b(tom\w+) (?:um )?duche\b", r"\1 banho", t)
    t = re.sub(r"\bdeit(o|as|a|amos|am|ei|ou|ar|ava|ámos) fora\b",
               lambda m: "jog" + ("u" if m.group(1) == "ei" else "") + m.group(1) + " fora", t)
    t = re.sub(r"\b(de|o|no|do|ao|pelo|O|No|Do|De) metro\b(?! (?:e|de altura|quadrado|cúbico|e meio))", r"\1 metrô", t)
    t = _formes_verbes(t)
    t = _remplacer(t, alertes)
    t = _ACEITE.sub(lambda m: m.group(1) + " aceito" + m.group(2), t)
    t = re.sub(r"(?<=[a-zà-ú])ámos\b", "amos", t)
    t = re.sub(r"[\wà-úÀ-Ú]+", lambda m: _FERME.sub(lambda v: {"é": "ê", "ó": "ô"}[v.group(0)], m.group(0))
               if len(m.group(0)) > 2 else m.group(0), t)
    t = _progressif(t)
    t = _TER_DE.sub(lambda m: m.group(1) + " que " + m.group(2) if m.group(2).lower() in INFINITIFS else m.group(0), t)
    t = _proclise(t, garder_imperatif=imperatif)
    t = _possessif(t)
    for motif, raison in MARQUES:
        if motif.search(t):
            alertes.add(raison)
    return t


# Ce qui reste du Portugal apres conversion : signale, pas corrige.
MARQUES = [(re.compile(r"(?<![\w-])tu(?![\w-])", re.I), "tu"),
           (re.compile(r"\b[a-zà-ú]+-(?:o|a|os|as|lo|la|los|las|no|na|nos|nas|mo|ma|to|ta|lho|lha)\b"), "enclise"),
           (re.compile(r"\b(?:est\w+|and\w+) a [a-zà-ú]+r\b"), "estar a")]


def dans_balises(texte, alertes=None):
    """Une explication en francais : seul le portugais en gras ou en italique
    (<b>, <i>, <em>) est converti."""
    if not texte:
        return texte
    return re.sub(r"(<(b|i|em)>)(.*?)(</\2>)", lambda m: m.group(1) + brasileiro(m.group(3), alertes) + m.group(4), texte)


# ------------------------------------------------------------------ les fichiers
CONTRASTE = re.compile(r"Brésil|brésilien|Portugal|portugais d.Europe|Lisbonne on|à Lisbonne,|À Lisbonne,")
PARENTHESE_PT = re.compile(r"\s*\((?:au Portugal|à Lisbonne|Portugal)\)")
# Une question qui enseigne l'usage du Portugal n'entre pas dans la variante.
QUESTION_PT = re.compile(r"(Au|au|Le) Portugal\s*[:,]|au Brésil|Le Brésil|brésilien|à Lisbonne on|PT\b")


class Rapport:
    def __init__(self):
        self.lignes = []
        self.compte = {}
        self.ecartees = []
        self.non_reecrits = []
        self.a_relire = []

    def noter(self, cle, n=1):
        self.compte[cle] = self.compte.get(cle, 0) + n


def _francais(texte, rap, ou):
    """Une explication en francais : sa reecriture bresilienne si elle oppose
    les deux pays, sinon le portugais de ses balises converti."""
    if not isinstance(texte, str):
        return texte
    r = T.reecriture(texte)
    if r is not None:
        rap.noter("explications reecrites")
        return r
    t = PARENTHESE_PT.sub("", texte)
    if CONTRASTE.search(t) and not T.contenu(t):
        rap.non_reecrits.append("%s : %s" % (ou, t[:120]))
    return dans_balises(t)


def _pt(texte, rap, ou, imperatif=False):
    if not isinstance(texte, str):
        return texte
    al = set()
    s = brasileiro(texte, al, imperatif)
    if s != texte:
        rap.noter("textes portugais convertis")
    if "genre" in al:
        rap.a_relire.append("genre change : " + s)
    for a in al - {"genre"}:
        rap.noter("signale : " + a)
    return s


def _carte_nom(m, rap):
    n = NOM_PAR_MOT.get(m.get("mot"))
    if n and (n["pt"] not in CARTE_SI or CARTE_SI[n["pt"]] in m.get("traduction", "")):
        m["mot"] = n["br"]
        m["genre"] = n["brg"]
        if "pluriel" in m:
            m["pluriel"] = n["brpl"]
        rap.noter("cartes de noms changees")
        if n["drapeau"] == "carte" and isinstance(m.get("exemple"), str):
            # Le mot a double sens est change dans la phrase de SA carte, ou
            # il a le sens de la carte (« O porco vive na quinta »).
            _CLES[n["pt"]] = ("nom", dict(n, drapeau=""), False)
            if n["ptpl"] not in ("—", n["pt"]):
                _CLES[n["ptpl"]] = ("nom", dict(n, drapeau=""), True)
            _MOTIF[0] = None
            try:
                m["exemple"] = _pt(m["exemple"], rap, "exemple")
            finally:
                _CLES.pop(n["pt"], None)
                _CLES.pop(n["ptpl"], None)
                _MOTIF[0] = None
            return m
    else:
        for cle in ("mot", "pluriel"):
            if isinstance(m.get(cle), str) and m[cle] != "—":
                m[cle] = _pt(m[cle], rap, "nom")
    m["exemple"] = _pt(m.get("exemple"), rap, "exemple")
    return m


def _themes(d, rap):
    for t in d["themes"]:
        t["nom_theme"] = _pt(t.get("nom_theme"), rap, "theme")
        for m in t["mots"]:
            _carte_nom(m, rap)
            if isinstance(m.get("exemple_fr"), str) and CONTRASTE.search(m["exemple_fr"]) and not T.contenu(m["exemple_fr"]):
                rap.non_reecrits.append("themes : " + m["exemple_fr"])
    return d


CHAMPS_VERBE = ["perfeito", "imperfeito", "futuro", "condicional", "conjuntivo", "conj_imperfeito", "conj_futuro",
                "mais_que_perfeito", "perfeito_composto"]


def _verbes(d, rap):
    for niveau in d.values():
        for v in niveau:
            avant = v.get("infinitif")
            # L'infinitif reste sous sa forme de dictionnaire : levantar-se.
            for cle in ("mot", "infinitif", "exemple", "participio", "gerundio"):
                if cle in v:
                    v[cle] = _pt(v[cle], rap, "verbe", imperatif=cle in ("mot", "infinitif"))
            if "praesens" in v:
                v["praesens"] = {k: _pt(f, rap, "verbe") for k, f in v["praesens"].items()}
            for cle in CHAMPS_VERBE:
                if isinstance(v.get(cle), list):
                    v[cle] = [_pt(f, rap, "verbe") for f in v[cle]]
            if isinstance(v.get("imperativo"), dict):
                v["imperativo"] = {k: _pt(f, rap, "verbe", imperatif=True) for k, f in v["imperativo"].items()}
            if v.get("infinitif") != avant:
                rap.noter("verbes changes")
    return d


def _adjectifs(d, rap):
    for niveau in d.values():
        for a in niveau:
            a["mot"] = _pt(a["mot"], rap, "adjectif")
            a["traduction"] = _francais(a["traduction"], rap, "adjectif")
            a["exemple"] = _pt(a.get("exemple"), rap, "adjectif")
            if isinstance(a.get("formes"), dict):
                a["formes"] = {k: _pt(f, rap, "adjectif") for k, f in a["formes"].items()}
    return d


def _simples(d, rap, nom):
    blocs = d.values() if isinstance(d, dict) else [d]
    for bloc in blocs:
        if not isinstance(bloc, list):
            continue
        for e in bloc:
            e["mot"] = _pt(e.get("mot"), rap, nom)
            e["exemple"] = _pt(e.get("exemple"), rap, nom)
            e["traduction"] = _francais(e.get("traduction"), rap, nom)
    return d


def _ligne_tableau(l, rap, ou):
    """Une ligne [portugais, francais ou {fr}] d'un tableau."""
    if not isinstance(l, list) or not l:
        return l
    out = [_pt(l[0], rap, ou) if isinstance(l[0], str) else l[0]]
    for x in l[1:]:
        if isinstance(x, dict) and "fr" in x:
            x = dict(x, fr=_francais(x["fr"], rap, ou))
        elif isinstance(x, str):
            x = _francais(x, rap, ou)
        out.append(x)
    return out


def _tableau(tab, rap, ou):
    if not isinstance(tab, dict):
        return tab
    tab = dict(tab)
    for cle in ("t", "a"):
        if isinstance(tab.get(cle), dict):
            tab[cle] = {k: _francais(v, rap, ou) for k, v in tab[cle].items()}
    if isinstance(tab.get("l"), list):
        tab["l"] = [_ligne_tableau(l, rap, ou) for l in tab["l"]]
    return tab


def _blocs_phrases(liste, rap, ou):
    out = []
    for b in liste or []:
        b = dict(b)
        for cle in ("p", "ex"):
            if cle in b:
                b[cle] = _pt(b[cle], rap, ou)
        if "v" in b:
            b["v"] = [_pt(x, rap, ou) for x in b["v"]]
        for cle in ("s", "exs"):
            if isinstance(b.get(cle), dict):
                b[cle] = {k: _francais(v, rap, ou) for k, v in b[cle].items()}
        if "l" in b and isinstance(b["l"], list):
            b["l"] = [dict(x, fr=_francais(x.get("fr"), rap, ou)) if isinstance(x, dict) else x for x in b["l"]]
        out.append(b)
    return out


def _dialogue(dl, rap, ou):
    if not isinstance(dl, dict):
        return dl
    dl = dict(dl)
    if isinstance(dl.get("t"), dict):
        dl["t"] = {k: _francais(v, rap, ou) for k, v in dl["t"].items()}
    dl["l"] = [dict(x, p=_pt(x.get("p"), rap, ou), s={k: _francais(v, rap, ou) for k, v in (x.get("s") or {}).items()})
               for x in dl.get("l", [])]
    return dl


def _escales(liste, rap, ou):
    for e in liste:
        if isinstance(e.get("s"), dict):
            e["s"] = {k: _francais(v, rap, ou) for k, v in e["s"].items()}
        if "mots" in e:
            e["mots"] = [_pt(m, rap, ou) for m in e["mots"]]
        if "tableau" in e:
            e["tableau"] = _tableau(e["tableau"], rap, ou)
        if "blocs" in e:
            e["blocs"] = _blocs_phrases(e["blocs"], rap, ou)
        if "phrases" in e:
            e["phrases"] = _blocs_phrases(e["phrases"], rap, ou)
        if "dialogue" in e:
            e["dialogue"] = _dialogue(e["dialogue"], rap, ou)
        if "cartes" in e:
            e["cartes"] = [_ligne_tableau(c, rap, ou) for c in e["cartes"]]
    return liste


def _a1_voyage(d, rap):
    for cle in ("escales", "installe", "suite"):
        if cle in d:
            d[cle] = _escales(d[cle], rap, "a1-voyage")
    return d


def _premiers_pas(d, rap):
    d["etapes"] = _escales(d.get("etapes", []), rap, "premiers-pas")
    return d


def _conjugaison(d, rap):
    for niveau in d.get("niveaux", {}).values():
        for e in niveau:
            for cle in ("t", "a"):
                if isinstance(e.get(cle), dict):
                    e[cle] = {k: _francais(v, rap, "conjugaison") for k, v in e[cle].items()}
            e["l"] = [_ligne_tableau(l, rap, "conjugaison") for l in e.get("l", [])]
    return d


def _reperes(d, rap):
    for r in d.get("reperes", []):
        for cle in ("t", "a"):
            if isinstance(r.get(cle), dict):
                r[cle] = {k: _francais(v, rap, "reperes") for k, v in r[cle].items()}
        if r.get("type") == "lettre":
            continue
        for cle in ("l", "x", "p"):
            if not isinstance(r.get(cle), list):
                continue
            lignes = []
            for l in r[cle]:
                if r.get("type") == "nombre" and cle == "l":
                    # [mot, chiffre, {fr: ce qu'on entend}] : la prononciation du Bresil.
                    mot = brasileiro(l[0])
                    l = [mot, l[1], {"fr": T.NOMBRES_BR.get(mot, "")}] + l[3:]
                    if not l[2]["fr"]:
                        rap.non_reecrits.append("nombre sans prononciation bresilienne : " + mot)
                elif r.get("type") in ("genre", "pluriel"):
                    l = [brasileiro(x) if isinstance(x, str) and i == 0 else x for i, x in enumerate(l)]
                else:
                    l = _ligne_tableau(l, rap, "reperes")
                lignes.append(l)
            r[cle] = lignes
    return d


def _grammaire(d, rap):
    textes = d.get("textes", {}).get("fr", {})
    for k, v in list(textes.items()):
        textes[k] = _francais(v, rap, "textes")
    for f in d.get("fiches", []):
        for cle in ("titre", "regle", "attention"):
            if cle in f:
                f[cle] = _francais(f[cle], rap, "fiche " + f.get("id", ""))
        f["resume"] = _pt(f.get("resume"), rap, "fiche") if "resume" in f else None
        # Le tableau d'une fiche : [portugais, francais, exemple portugais] ;
        # ses exemples : [portugais, francais].
        if isinstance(f.get("tableau"), list):
            f["tableau"] = [[_francais(x, rap, "fiche") if i == 1 else _pt(x, rap, "fiche") for i, x in enumerate(l)]
                            for l in f["tableau"]]
        if isinstance(f.get("exemples"), list):
            f["exemples"] = [_ligne_tableau(l, rap, "fiche " + f.get("id", "")) for l in f["exemples"]]
        if f.get("resume") is None:
            f.pop("resume", None)
        # Les fiches qui enseignent un usage du Portugal : leur version bresilienne.
        br = T.FICHES_BR.get(f.get("id"))
        if br:
            for cle in ("titre", "resume", "tableau", "exemples"):
                if cle in br:
                    f[cle] = br[cle]
            for i, ligne in br.get("lignes", {}).items():
                if i < len(f.get("tableau", [])):
                    f["tableau"][i] = ligne
            rap.noter("fiches reecrites pour le Bresil")
    for t in d.get("temps", []):
        for cle in ("titre", "texte"):
            if cle in t:
                t[cle] = _francais(t[cle], rap, "temps")
    for cle in [k for k in d if k not in ("textes", "fiches", "temps")]:
        pass
    return d


def _exercices(d, rap):
    for nom, serie in d.get("jeux", {}).items():
        gardees = []
        for q in serie:
            expl = PARENTHESE_PT.sub("", " ".join(str(q.get(k, "")) for k in ("explanation", "question")))
            if QUESTION_PT.search(expl) and not T.reecriture(q.get("explanation", "")):
                rap.ecartees.append("%s : %s" % (nom, q.get("question", "")))
                continue
            q2 = dict(q)
            al = set()
            trou = "XQX"
            question = q.get("question", "")
            juste = q.get("correct", "")
            conv_q = brasileiro(question.replace("___", trou), al)
            conv_j = brasileiro(juste, al) if juste else juste
            # La phrase complete convertie doit egaler la question convertie
            # completee : sinon la conversion traverse le trou (« Estou ___ ler »).
            if "___" in question and juste:
                pleine = brasileiro(question.replace("___", juste), al)
                if conv_q.replace(trou, conv_j) != pleine:
                    rap.ecartees.append("%s (conversion a travers le trou) : %s" % (nom, question))
                    continue
            q2["question"] = conv_q.replace(trou, "___")
            q2["question_en"] = q2["question"] if q.get("question_en") == question else _pt(q.get("question_en"), rap, nom)
            q2["correct"] = conv_j
            q2["correctEn"] = conv_j if q.get("correctEn") == juste else _pt(q.get("correctEn"), rap, nom)
            for cle in ("answers", "options", "optionsEn"):
                if isinstance(q.get(cle), list):
                    q2[cle] = [brasileiro(x, al) for x in q[cle]]
            for cle in ("explanation", "explanation_en"):
                if isinstance(q.get(cle), str):
                    q2[cle] = _francais(PARENTHESE_PT.sub("", q[cle]), rap, nom)
            opts = q2.get("options") or q2.get("answers") or []
            if opts and (len(set(o.lower() for o in opts)) < len(opts) or conv_j not in opts):
                rap.ecartees.append("%s (options confondues) : %s" % (nom, question))
                continue
            if al - {"genre"}:
                for a in al - {"genre"}:
                    rap.noter("signale : " + a)
            gardees.append(q2)
        d["jeux"][nom] = gardees
    for nom, (sujet, bloc) in T.SERIES_BR.items():
        if nom not in d["jeux"]:
            rap.non_reecrits.append("serie bresilienne sans serie europeenne : " + nom)
            continue
        qs = []
        for ligne in bloc.strip().splitlines():
            question, bonne, fausses, trad, expl = [c.strip() for c in ligne.split("|")][:5]
            options = [bonne] + [x.strip() for x in fausses.split("/")]
            random.Random(question).shuffle(options)
            qs.append({"topic": sujet, "question": question, "question_en": question,
                       "translation": trad, "translation_en": trad, "answers": [bonne], "correct": bonne,
                       "correctEn": bonne, "explanation": expl, "explanation_en": expl,
                       "options": options, "optionsEn": options})
        d["jeux"][nom] = qs
        rap.noter("series ecrites pour le Bresil")
    return d


def _prononciation(d, rap):
    rap.noter("prononciation remplacee")
    return T.prononciation_bresil()


def construire(jeu):
    """Le jeu de donnees europeen -> (jeu bresilien, rapport)."""
    connaitre_infinitifs(jeu.get("verbes.json", {}))
    _MOTIF[0] = None
    rap = Rapport()
    br = copy.deepcopy(jeu)
    faire = {"themes.json": _themes, "verbes.json": _verbes, "adjectifs.json": _adjectifs,
             "adverbes.json": lambda d, r: _simples(d, r, "adverbes"),
             "expressions.json": lambda d, r: _simples(d, r, "expressions"),
             "fonctionnels.json": lambda d, r: _simples(d, r, "fonctionnels"),
             "a1-voyage.json": _a1_voyage, "premiers-pas.json": _premiers_pas,
             "conjugaison.json": _conjugaison, "reperes.json": _reperes, "grammaire.json": _grammaire,
             "exercices.json": _exercices, "prononciation.json": _prononciation}
    for nom, f in faire.items():
        if nom in br:
            br[nom] = f(br[nom], rap)
    for nom in ("variantes-br.json", "synonymes.json"):
        br.pop(nom, None)
    return br, rap
