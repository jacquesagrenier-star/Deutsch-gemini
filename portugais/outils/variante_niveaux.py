# -*- coding: utf-8 -*-
"""Du portugais du Bresil au portugais d'Europe (A2-C1). SOURCE des regles.

Nos corpus allemand et espagnol portent, pour chaque mot, une traduction et
une phrase en portugais : celles de l'interface pt-BR, donc BRESILIENNES
(« Meu primo mora em Berlim », « Você me passa o sal? »). Le cours apprend le
portugais du PORTUGAL (decide par Jacques le 29 oct. 2026). Ce module :

  europeu(texte)      -> le texte converti (vocabulaire, orthographe, article
                         devant le possessif, gerondif « a + infinitif »,
                         pronom apres le verbe, mesoclise)
  bresilianismes(t)   -> ce qui reste de bresilien apres conversion ; une
                         phrase qui en garde est REJETEE (on prend une autre
                         phrase, ou aucune)
  BR_PT_VOCAB         -> la table des mots : elle servira aussi, a l'envers,
                         a une future variante bresilienne (voir PLAN-A2-C1.md)

Rien n'est deviné en silence : ce que la conversion ne sait pas faire
(« você » et sa conjugaison, « a gente », un « o » pronom), elle le refuse.
BROUILLON : a faire relire par un lusophone du Portugal.
"""
import re

# ------------------------------------------------------------------ le vocabulaire
# (bresilien, europeen). Des mots entiers, casse respectee. Les plus longs
# d'abord (« ponto de ônibus » avant « ônibus »).
BR_PT_VOCAB = [
    ("ponto de ônibus", "paragem de autocarro"), ("pontos de ônibus", "paragens de autocarro"),
    ("ponto do ônibus", "paragem do autocarro"),
    ("café da manhã", "pequeno-almoço"), ("cafés da manhã", "pequenos-almoços"),
    ("faixa de pedestres", "passadeira"), ("faixa de pedestre", "passadeira"),
    ("carteira de motorista", "carta de condução"), ("carteira de habilitação", "carta de condução"),
    ("fone de ouvido", "auscultadores"), ("fones de ouvido", "auscultadores"),
    ("vaso sanitário", "sanita"), ("caixa eletrônico", "multibanco"), ("caixas eletrônicos", "multibancos"),
    ("banheiro", "casa de banho"), ("banheiros", "casas de banho"),
    ("ônibus", "autocarro"), ("trem", "comboio"), ("trens", "comboios"),
    ("bonde", "elétrico"), ("bondes", "elétricos"), ("metrô", "metro"),
    ("celular", "telemóvel"), ("celulares", "telemóveis"),
    ("geladeira", "frigorífico"), ("geladeiras", "frigoríficos"),
    ("suco", "sumo"), ("sucos", "sumos"), ("sorvete", "gelado"), ("sorvetes", "gelados"),
    ("xícara", "chávena"), ("xícaras", "chávenas"), ("cardápio", "ementa"), ("cardápios", "ementas"),
    ("garçom", "empregado de mesa"), ("garçons", "empregados de mesa"), ("garçonete", "empregada de mesa"),
    ("açougue", "talho"), ("açougueiro", "talhante"), ("abacaxi", "ananás"), ("abacaxis", "ananases"),
    ("cachorro", "cão"), ("cachorros", "cães"), ("cachorrinho", "cãozinho"),
    ("caminhão", "camião"), ("caminhões", "camiões"), ("caminhoneiro", "camionista"),
    ("pedestre", "peão"), ("pedestres", "peões"), ("calçada", "passeio"), ("calçadas", "passeios"),
    ("freio", "travão"), ("freios", "travões"), ("frear", "travar"), ("carona", "boleia"),
    ("pedágio", "portagem"), ("estacionar", "estacionar"),
    ("torcedor", "adepto"), ("torcedores", "adeptos"), ("torcedora", "adepta"), ("torcida", "claque"),
    ("time", "equipa"), ("times", "equipas"), ("equipe", "equipa"), ("equipes", "equipas"),
    ("cadarço", "atacador"), ("cadarços", "atacadores"), ("camiseta", "t-shirt"), ("camisetas", "t-shirts"),
    ("terno", "fato"), ("ternos", "fatos"), ("tênis", "ténis"), ("calcinha", "cuecas"),
    ("xampu", "champô"), ("aeromoça", "hospedeira de bordo"), ("comissária de bordo", "hospedeira de bordo"),
    ("gramado", "relvado"),
    ("mouse", "rato"), ("usuário", "utilizador"), ("usuários", "utilizadores"), ("usuária", "utilizadora"),
    ("aluguel", "renda"), ("aluguéis", "rendas"), ("inquilino", "inquilino"),
    ("geléia", "compota"), ("geleia", "compota"), ("presunto", "fiambre"),
    ("grampeador", "agrafador"), ("durex", "fita-cola"), ("descarga", "autoclismo"),
    ("moça", "rapariga"), ("moças", "raparigas"), ("garoto", "miúdo"), ("garotos", "miúdos"),
    ("garota", "miúda"), ("garotas", "miúdas"), ("menino", "menino"),
    ("show", "concerto"), ("shows", "concertos"),
    ("lanchonete", "snack-bar"), ("sobremesa", "sobremesa"), 
    ("chiclete", "pastilha elástica"), ("biscoito", "bolacha"), ("biscoitos", "bolachas"),
    ("encanador", "canalizador"), ("encanamento", "canalização"),
    ("fila", "fila"), ("prefeitura", "câmara municipal"), ("prefeito", "presidente da câmara"),
    ("prefeita", "presidente da câmara"), ("cartório", "conservatória"), ("delegacia", "esquadra"),
    ("cafezinho", "café"), ("ótimo", "ótimo"),
    ("gostoso", "saboroso"), ("gostosa", "saborosa"), ("gostosos", "saborosos"), ("gostosas", "saborosas"),
    ("bacana", "fixe"), ("que legal", "que fixe"), ("tchau", "adeus"),
    ("bagunça", "confusão"), ("bagunçado", "desarrumado"), ("bagunçada", "desarrumada"),
    ("ficar sabendo", "ficar a saber"), ("esquentar", "aquecer"), ("esquenta", "aquece"),
    ("tomar banho", "tomar banho"), ("banheira", "banheira"), ("escova de dentes", "escova de dentes"),
    ("ônibus escolar", "autocarro escolar"), ("rodoviária", "estação rodoviária"),
    ("carro alugado", "carro alugado"), ("motorista", "motorista"), ("estádio", "estádio"),
    ("cueca", "cuecas"), ("sutiã", "soutien"), ("mamadeira", "biberão"), ("fralda", "fralda"),
    ("babá", "ama"), ("creche", "creche"), ("ensino médio", "ensino secundário"),
    ("ensino fundamental", "ensino básico"), ("colégio", "escola"), ("vestibular", "exame nacional"),
    ("faculdade", "faculdade"), ("nota fiscal", "fatura"), ("conta-corrente", "conta à ordem"),
    ("conta corrente", "conta à ordem"), ("CPF", "NIF"), ("carteira de identidade", "cartão de cidadão"),
    ("RG", "cartão de cidadão"), ("CEP", "código postal"), ("sobrenome", "apelido"), ("sobrenomes", "apelidos"),
    ("pegar o ônibus", "apanhar o autocarro"), ("pegar o trem", "apanhar o comboio"),
    ("pegou o ônibus", "apanhou o autocarro"), ("pegamos o trem", "apanhámos o comboio"),
    ("cômodo", "divisão"), ("cômodos", "divisões"), ("gramática", "gramática"),
    ("ônibus noturno", "autocarro noturno"), ("treinador", "treinador"), ("técnico", "técnico"),
    ("ficha", "ficha"), ("deletar", "apagar"),
    ("site", "site"), ("e-mail", "e-mail"), ("planilha", "folha de cálculo"),
    ("mouse", "rato"), ("tecla", "tecla"), ("notebook", "portátil"), ("laptop", "portátil"),
    ("injeção", "injeção"), ("remédio", "medicamento"), ("remédios", "medicamentos"),
    ("câmera", "câmara"), ("câmeras", "câmaras"), ("revisado", "revisto"), ("revisada", "revista"),
    ("revisados", "revistos"), ("revisadas", "revistas"), ("quando criança", "em criança"),
    ("na frente de", "em frente de"), ("na frente do", "em frente do"), ("na frente da", "em frente da"),
    ("passagens", "bilhetes"), ("esporte", "desporto"), ("esportes", "desportos"), ("esportivo", "desportivo"),
    ("esportiva", "desportiva"), ("esportivos", "desportivos"), ("esportivas", "desportivas"),
    ("esportista", "desportista"), ("esportistas", "desportistas"), ("goleiro", "guarda-redes"),
    ("gol", "golo"), ("gols", "golos"), ("vôlei", "voleibol"), ("basquete", "basquetebol"),
    ("bermuda", "calções"), ("sunga", "calções de banho"), ("maiô", "fato de banho"),
    ("senha", "palavra-passe"), ("senhas", "palavras-passe"), ("aplicativo", "aplicação"),
    ("aplicativos", "aplicações"), ("cadastro", "registo"), ("cadastrar", "registar"),
    ("controle remoto", "comando"), ("pasta de dente", "pasta de dentes"), ("fio dental", "fio dentário"),
    ("curativo", "penso"), ("pronto-socorro", "urgências"), ("aposentado", "reformado"),
    ("aposentada", "reformada"), ("aposentados", "reformados"), ("aposentadoria", "reforma"),
    ("aposentar", "reformar"), ("aposentou", "reformou"), ("rodovia", "autoestrada"),
    ("rodovias", "autoestradas"), ("posto de gasolina", "bomba de gasolina"), ("xerox", "fotocópia"),
    ("mamão", "papaia"), ("lixeira", "caixote do lixo"), ("lixeiras", "caixotes do lixo"),
    ("jogar fora", "deitar fora"), ("jogou fora", "deitou fora"), ("joguei fora", "deitei fora"),
    ("bobo", "parvo"), ("boba", "parva"), ("bobagem", "parvoíce"), ("xingar", "insultar"),
    ("freezer", "congelador"), ("liquidificador", "liquidificadora"), ("shopping", "centro comercial"),
    ("fazenda", "quinta"), ("fazendas", "quintas"), ("fazendeiro", "agricultor"),
    ("ingresso", "bilhete"), ("ingressos", "bilhetes"), ("oi", "olá"), ("Oi", "Olá"),
    ("bife", "bife"), ("aeromoças", "hospedeiras de bordo"), ("zagueiro", "defesa"),
    ("placar", "marcador"), ("técnico de futebol", "treinador"), ("conserto", "arranjo"),
    ("consertar", "arranjar"), ("consertou", "arranjou"), ("concertar", "arranjar"), ("Madri", "Madrid"), ("Moscou", "Moscovo"), ("Nova York", "Nova Iorque"), ("Teerã", "Teerão"),
]
# Le sens differe d'un pays a l'autre : on garde le mot, mais la phrase est
# rejetee (« apelido » = surnom au Bresil, nom de famille au Portugal...).
# Ceux-ci sont deja traites dans la table ; la liste sert au rapport.

# ------------------------------------------------------------------ l'orthographe
# Les voyelles fermees bresiliennes devant m ou n, ouvertes au Portugal :
# econômico -> económico, gênero -> género, bebê -> bebé.
ORTHO_LISTE = [
    ("bebê", "bebé"), ("bebês", "bebés"), ("nenê", "nené"), ("purê", "puré"), ("comitê", "comité"),
    ("judô", "judo"), ("caratê", "karaté"), ("crochê", "croché"), ("bidê", "bidé"), ("matinê", "matiné"),
    ("canapê", "canapé"), ("buquê", "ramo de flores"), ("robô", "robô"), ("tênis", "ténis"),
    ("pênis", "pénis"), ("Vênus", "Vénus"), ("bônus", "bónus"), ("ônus", "ónus"), ("tônus", "tónus"),
    ("fêmur", "fémur"), ("abdômen", "abdómen"), ("sêmen", "sémen"), ("Antônio", "António"),
    ("fato", "facto"), ("fatos", "factos"), ("contato", "contacto"), ("contatos", "contactos"),
    ("contatar", "contactar"), ("registro", "registo"), ("registros", "registos"),
    ("recepção", "receção"), ("recepcionista", "rececionista"), ("seção", "secção"), ("seções", "secções"),
    ("anistia", "amnistia"), ("úmido", "húmido"), ("úmida", "húmida"), ("umidade", "humidade"),
    ("excepcional", "excecional"), ("detectar", "detetar"), ("aspecto", "aspeto"), ("aspectos", "aspetos"),
    ("ação", "ação"), ("econômica", "económica"), ("gerência", "gerência"),
    ("Ônibus", "Autocarro"), ("time", "equipa"), ("facção", "fação"),
    ("planejar", "planear"), ("planejamento", "planeamento"), ("planejo", "planeio"), ("planejamos", "planeamos"),
    ("planejou", "planeou"), ("planejado", "planeado"), ("planejada", "planeada"),
    ("treinar", "treinar"), ("parabéns", "parabéns"), ("idéia", "ideia"),
]
# Garde le ê / ô fermes au Portugal aussi.
ORTHO_EXCEPTIONS = {"estômago", "estômagos", "fêmea", "fêmeas", "cômputo", "Estêvão", "êmbolo", "Ênio"}

VOYELLES = "aeiouáéíóúâêôãõà"


def _ouvrir_voyelle(mot):
    """econômico -> económico : ê/ô suivi de m/n + voyelle, avec encore deux
    syllabes apres (proparoxyton)."""
    if mot in ORTHO_EXCEPTIONS or mot.lower() in ORTHO_EXCEPTIONS:
        return mot
    for i, c in enumerate(mot):
        if c in "êôÊÔ" and i + 2 < len(mot) and mot[i + 1] in "mn" and mot[i + 2].lower() in VOYELLES:
            reste = mot[i + 1:]
            groupes = re.findall("[" + VOYELLES + "]+", reste.lower())
            if len(groupes) >= 2 or re.match(r"^[mn](i[ao]s?|e[ao]s?)$", reste.lower()):
                ouvert = {"ê": "é", "ô": "ó", "Ê": "É", "Ô": "Ó"}[c]
                return mot[:i] + ouvert + mot[i + 1:]
    return mot


_MOTIFS = {}


def _motifs(paires):
    cle = id(paires) if isinstance(paires, list) and len(paires) > 8 else tuple(paires)
    if cle not in _MOTIFS:
        _MOTIFS[cle] = [(re.compile(r"(?<![\w-])" + re.escape(a) + r"(?![\w-])", re.I), a.lower()[:3], b)
                        for a, b in sorted(paires, key=lambda p: -len(p[0])) if a != b]
    return _MOTIFS[cle]


def remplacer_mots(texte, paires):
    """Remplace des mots entiers (ou groupes de mots), casse du debut respectee."""
    bas = texte.lower()
    for motif, debut, b in _motifs(paires):
        if debut not in bas:
            continue

        def rep(m, b=b):
            s = m.group(0)
            if s.isupper() and len(s) > 1 and not b.isupper():
                return b.upper()
            if s[0].isupper():
                return b[0].upper() + b[1:]
            return b
        texte = motif.sub(rep, texte)
    return texte


# ------------------------------------------------------------------ la syntaxe
# Les mots qui attirent le pronom AVANT le verbe, au Portugal aussi.
ATTRACTEURS = set("""
não nunca jamais nem ninguém nada nenhum nenhuma que quem onde quando como porque porquê
embora enquanto já ainda sempre também só apenas bem mal talvez aqui lá ali cá tudo todos todas
alguém algo qualquer quanto quanta quantos quantas qual quais oxalá até mesmo se caso conforme
logo assim pouco muito tanto cada ambos ambas outro outra outros outras quase sequer
""".split())
CLITIQUES = ("me", "te", "se", "nos", "vos", "lhe", "lhes")
SUJETS = set("eu tu ele ela nós vós eles elas isso isto aquilo".split())
# Ce qui ne peut pas suivre un pronom complement : apres « se », c'est la
# conjonction (« não sei se ele vem »).
PAS_UN_VERBE = set("""eu tu ele ela nós vós eles elas você vocês o a os as um uma uns umas não já ainda
sempre também nunca isso isto aquilo me te se nos lhe lhes calhar""".split())
# Les verbes apres lesquels « se » est la conjonction « si » (savoir si...).
VERBES_SI = set("""sei sabe sabes sabemos sabem saber sabia perguntar pergunta perguntou perguntei
pergunto perguntamos ver vê vejo veja vemos verificar verifica duvido depende imagina imagino
decidir decide decidiu decidimos""".split())
MODAUX = set("""vou vais vai vamos vão ia iam pode podes podemos podem posso pôde podia quer queres
quero queremos querem queria deve deves devemos devem devia precisa precisas preciso precisamos
precisam tem tens tenho temos têm tinha começa começou começar acaba acabou acabar consegue consigo
conseguimos conseguiu tenta tentou tento costuma costumo costumamos gosta gosto gostamos prefere
prefiro sabe sei sabemos""".split())
FUTUR = re.compile(r"^(\w+r)(ei|ás|á|emos|eis|ão|ia|ias|íamos|íeis|iam)$")
# Les infinitifs connus, pour reconnaitre un futur (« levará » = levar + á) et
# ne pas couper un passe (« esperei » = esper + ei, pas esperar + ei).
INFINITIFS = set("far dir trar ser ter ir pôr".split())


def connaitre_infinitifs(liste):
    for v in liste:
        v = (v or "").strip().lower()
        if v.endswith("-se"):
            v = v[:-3]
        if re.match(r"^[a-zà-ú]+(ar|er|ir|or|ôr)$", v):
            INFINITIFS.add(v)


def _enclise(phrase):
    """Ele se chama -> Ele chama-se ; Me dá -> Dá-me ; se levará -> levar-se-á.
    Au Portugal, le pronom suit le verbe, sauf apres un « attracteur » (não,
    que, já, também...). Rend None si le cas est trop douteux."""
    mots = phrase.split(" ")
    i = 0
    while i < len(mots) - 1:
        cl = mots[i].lower().strip("¿¡\"«")
        if cl not in CLITIQUES:
            i += 1
            continue
        prec_brut = mots[i - 1] if i > 0 else ""
        precedent = prec_brut.lower().strip(",;:\"«»")
        debut = i == 0 or prec_brut[-1:] in ".!?"
        apres_ponct = debut or prec_brut[-1:] in ",;:—"
        verbe = mots[i + 1]
        v_nu = verbe.rstrip(".,;:!?»\"")
        fin = verbe[len(v_nu):]
        v_bas = v_nu.lower()
        # « se » ou « nos » qui ne precedent pas un verbe : conjonction, contraction
        if v_bas in PAS_UN_VERBE or not re.match(r"^[a-zà-ú]+$", v_bas):
            if cl in ("se", "nos"):
                i += 1
                continue
            return None
        if precedent in ATTRACTEURS:
            i += 1
            continue
        if cl == "nos" and not (precedent in SUJETS or re.search(r"(mos|ou|aram|eram|iram|am|em|ia|ava|ei|iu|eu)$", v_bas)):
            i += 1
            continue
        if cl == "se":
            si_conj = re.search(r"(r|res|rmos|rem|sse|sses|ssemos|ssem)$", v_bas) and (
                apres_ponct or precedent in ("e", "mas", "ou", "só", "que", "mesmo"))
            if si_conj or precedent in VERBES_SI:
                i += 1
                continue
            sujet_ou_nom = (precedent in SUJETS or debut or (i > 1 and mots[i - 2].lower() in DETERMINANTS)
                            or prec_brut[:1].isupper())
            modal = precedent in MODAUX and re.search(r"(ar|er|ir|or|ôr)$", v_bas)
            if not (sujet_ou_nom or modal):
                return None
        m = FUTUR.match(v_bas)
        base = m.group(1) if m else ""
        if m and base in INFINITIFS and len(v_nu) > 3:
            nouveau = v_nu[:len(base)] + "-" + cl + "-" + m.group(2)
        else:
            v2 = v_nu
            if cl == "nos" and v2.endswith("mos"):
                v2 = v2[:-1]
            # Pas de « o » ni « a » ici : les pronoms complements directs ne
            # sont pas deplaces (lo, no...), la phrase est refusee plus loin.
            nouveau = v2 + "-" + cl
        if debut:
            nouveau = nouveau[0].upper() + nouveau[1:]
        mots[i:i + 2] = [nouveau + fin]
        i += 1
    return " ".join(mots)


POSSESSIFS = set("meu minha meus minhas teu tua teus tuas seu sua seus suas nosso nossa nossos nossas".split())
DETERMINANTS = set("""o a os as um uma uns umas do da dos das no na nos nas ao à aos às pelo pela pelos pelas
este esta estes estas esse essa esses essas aquele aquela aqueles aquelas deste desta destes destas
desse dessa desses dessas daquele daquela neste nesta nesse nessa naquele naquela num numa dum duma
todo toda todos todas é são era foi ser sou és somos""".split())
FEM = set("minha minhas tua tuas sua suas nossa nossas".split())
PLUR = set("meus minhas teus tuas seus suas nossos nossas".split())


def _article(poss):
    p = poss.lower()
    return ("as" if p in FEM else "os") if p in PLUR else ("a" if p in FEM else "o")


CONTRACTIONS = {"de": {"o": "do", "a": "da", "os": "dos", "as": "das"},
                "em": {"o": "no", "a": "na", "os": "nos", "as": "nas"},
                "por": {"o": "pelo", "a": "pela", "os": "pelos", "as": "pelas"},
                "a": {"o": "ao", "os": "aos"}}


def _possessifs(phrase):
    """Meu primo -> O meu primo ; com minha mãe -> com a minha mãe ; de meu pai -> do meu pai."""
    mots = phrase.split(" ")
    sortie = []
    for i, m in enumerate(mots):
        nu = m.lower().strip("¿¡\"«(")
        if nu in POSSESSIFS and i + 1 < len(mots) and not m.rstrip()[-1:] in ".,;:!?":
            prec = sortie[-1].lower() if sortie else ""
            if prec in DETERMINANTS or prec in ("meu", "deus"):
                sortie.append(m)
                continue
            if (nu == "meu" and mots[i + 1].lower().strip(",.!?") in ("deus", "ver")) or (nu == "minha" and mots[i + 1].lower().startswith("nossa")):
                sortie.append(m)
                continue
            art = _article(nu)
            if prec in CONTRACTIONS and art in CONTRACTIONS[prec]:
                c = CONTRACTIONS[prec][art]
                if sortie[-1][0].isupper():
                    c = c[0].upper() + c[1:]
                sortie[-1] = c
                sortie.append(m)
                continue
            if not sortie or sortie[-1][-1:] in ".!?":
                sortie.append(art[0].upper() + art[1:])
                sortie.append(m[0].lower() + m[1:])
                continue
            sortie.append(art)
        sortie.append(m)
    return " ".join(sortie)


GERONDIF = re.compile(r"\b(est(?:ou|ás|á|amos|ão|ava|avas|ávamos|avam|eve|ive|ivemos|iveram|ar|ando|ado|ivesse|eja|ejam)|"
                      r"and(?:o|as|a|amos|am|ava|avam|ou)|fic(?:o|as|a|amos|am|ou|ava)|continu(?:o|as|a|amos|am|ou|ava)|"
                      r"pass(?:o|a|amos|am|ou|ei)) (\w+?)(ando|endo|indo|ondo)\b", re.I)


PAS_GERONDIF = set("quando lindo linda lindos lindas comando bando brando mando segundo fundo mundo".split())


def _gerondif(phrase):
    """estou fazendo -> estou a fazer (estar, andar, ficar, continuar, passar)."""
    def rep(m):
        aux, rad, term = m.group(1), m.group(2), m.group(3)
        if (rad + term).lower() in PAS_GERONDIF:
            return m.group(0)
        inf = rad + {"ando": "ar", "endo": "er", "indo": "ir", "ondo": "or"}[term.lower()]
        if inf.lower() == "por":
            inf = "pôr"
        return aux + " a " + inf
    return GERONDIF.sub(rep, phrase)


EXISTENTIEL = [
    (re.compile(r"^Tem (um|uma|uns|umas|muito|muita|muitos|muitas|vários|várias|alguém|algum|alguma|alguns|algumas|pouco|pouca|poucos|poucas|gente|mais|menos|\d+)\b"), r"Há \1"),
    (re.compile(r"\b(não|Não) tem (nada|ninguém|nenhum|nenhuma|mais|muito|muita|muitos|muitas|lugar|vaga|vagas)\b"), r"\1 há \2"),
    (re.compile(r"\b(Aqui|aqui|Lá|lá|Ali|ali) tem\b"), r"\1 há"),
    (re.compile(r"\bTinha (um|uma|muito|muita|muitos|muitas|vários|várias|alguém|pouca|poucos|gente)\b"), r"Havia \1"),
]
TER_QUE = re.compile(r"\b(tenho|tens|tem|temos|têm|tinha|tinhas|tínhamos|tinham|tive|teve|tivemos|tiveram|ter|terá|teria|teremos|tenha|tenhamos|tenham|tivesse) que\b", re.I)


PRECISAR = re.compile(r"\b(precis(?:o|as|a|amos|am|ava|avas|ávamos|avam|ou|ei|ámos|aram|ar|ará|aria|asse))\s+([a-zà-ú]+(?:ar|er|ir|ôr))\b", re.I)


def europeu(texte):
    """Le texte bresilien converti en portugais d'Europe, ou None si la
    conversion ne sait pas le faire proprement."""
    if not texte:
        return texte
    t = texte.strip()
    t = re.sub(r"\bpra\b", "para", t)
    t = re.sub(r"\bPra\b", "Para", t)
    t = remplacer_mots(t, ORTHO_LISTE)
    t = remplacer_mots(t, BR_PT_VOCAB)
    t = re.sub(r"[\wà-úÀ-Ú]+", lambda m: _ouvrir_voyelle(m.group(0)), t)
    for motif, rep in EXISTENTIEL:
        t = motif.sub(rep, t)
    t = TER_QUE.sub(lambda m: m.group(1) + " de", t)
    t = PRECISAR.sub(lambda m: m.group(1) + " de " + m.group(2), t)
    t = _gerondif(t)
    t = _possessifs(t)
    t = _enclise(t)
    return t


# ------------------------------------------------------------------ le controle
MARQUES_BR = [
    r"\bvocês?\b", r"\ba gente\b", r"\bcadê\b", r"\btá\b", r"\bné\b", r"\bcara\b(?! a)", r"\bgrana\b",
    r"\bmoleque", r"\bbeleza!", r"\bnossa!", r"\bvaleu\b", r"\bfala sério", r"\btipo assim",
    r"\b(eu|ele|ela|nós|eles|elas) (o|a|os|as) [a-zà-ú]+(ei|ou|aram|eu|iu|eram|iram|o|a|amos|emos|imos|am|em)\b",
    r"\bR\$", r"\btchau\b", r"\bpegar\b", r"\bpega\b", r"\bpegou\b", r"\bpeguei\b",
    r"\bdirigir\b", r"\bdirijo\b", r"\bdirige\b", r"\bdirigiu\b",
    r"\bbrasileir", r"\bBrasil\b", r"\bSão Paulo\b", r"\bRio\b", r"\breal\b", r"\bnota\b(?= \d)",
    r"\bsei lá\b", r"\bbatida\b", r"\bcolega de quarto\b", r"\bprédio\b(?=.*\bandar)",
    r"\bem casa de\b", r"\bgeladeira", r"\bônibus", r"\bmouse\b",
    r"\b[A-Za-zà-ú]+ndo\b(?= (a|o|um|uma)\b)",   # gerondif restant apres un verbe non auxiliaire
    r"\bpor favor me\b", r"^(Me|Te|Lhe|Lhes) ", r"\bjogue\b", r"\bjoga fora\b", r"\bpuxa\b",
    r"\bmoço\b", r"\bcaipira\b", r"\bcolega de apartamento\b",
    r"\bterminou de\b", r"\bacabou de\b(?=.*\bfalando)",
]
MARQUES_RE = [re.compile(m, 0 if re.search(r"[A-Z]", m) else re.I) for m in MARQUES_BR]

# Le gerondif est courant au Bresil ; au Portugal il vit (« chegando a casa »,
# « foi melhorando »), mais la forme progressive est « a + infinitif ». Un
# gerondif apres estar/andar/ficar qui aurait echappe est une faute.
GERONDIF_RESTANT = re.compile(r"\b(est\w+|and\w+|fic\w+|continu\w+) \w+(ando|endo|indo)\b", re.I)


def bresilianismes(t):
    if not t:
        return []
    trouves = [m.pattern for m in MARQUES_RE if m.search(t)]
    if GERONDIF_RESTANT.search(t):
        trouves.append("gerondif")
    return trouves


TUTOIEMENT_FR = re.compile(r"\b(ton|ta|tes|toi|tu|te|t')\b|\bt'", re.I)
VOUVOIEMENT_FR = re.compile(r"\b(votre|vos|vous|son|sa|ses|leur|leurs)\b", re.I)
SEU_TEU = [("seu", "teu"), ("sua", "tua"), ("seus", "teus"), ("suas", "tuas")]


def accorder_au_francais(pt, fr):
    """Le « seu » bresilien de « você » -> « teu » quand le francais tutoie
    (« Obrigado pelo seu apoio » / « Merci pour ton soutien »)."""
    if fr and TUTOIEMENT_FR.search(fr) and not VOUVOIEMENT_FR.search(fr):
        return remplacer_mots(pt, SEU_TEU)
    return pt


# Les mots qui CHANGENT DE GENRE d'un pays a l'autre (o cardápio -> a ementa) :
# une phrase qui en contient un est refusee (l'article et l'adjectif ne
# suivraient pas), et le nom prend le genre europeen ci-dessous.
GENRE_CHANGE = {
    "geladeira": "frigorífico", "calçada": "passeio", "time": "equipa", "aluguel": "renda",
    "banheiro": "casa de banho", "cardápio": "ementa", "pedágio": "portagem", "lixeira": "caixote do lixo",
    "aplicativo": "aplicação", "posto de gasolina": "bomba de gasolina", "xerox": "fotocópia",
    "mamão": "papaia", "bermuda": "calções", "sunga": "calções de banho", "pronto-socorro": "urgências",
    "liquidificador": "liquidificadora", "vaso sanitário": "sanita", "colégio": "escola",
    "carteira de identidade": "cartão de cidadão", "cômodo": "divisão", "mamadeira": "biberão",
    "carteira de motorista": "carta de condução", "fone de ouvido": "auscultadores", "calcinha": "cuecas",
    "cueca": "cuecas", "babá": "ama", "nota fiscal": "fatura", "maiô": "fato de banho",
}
GENRE_EUROPEEN = {
    "frigorífico": "o", "passeio": "o", "equipa": "a", "renda": "a", "casa de banho": "a", "ementa": "a",
    "portagem": "a", "caixote do lixo": "o", "aplicação": "a", "bomba de gasolina": "a", "fotocópia": "a",
    "papaia": "a", "calções": "os", "calções de banho": "os", "urgências": "as", "liquidificadora": "a",
    "sanita": "a", "escola": "a", "cartão de cidadão": "o", "divisão": "a", "biberão": "o",
    "carta de condução": "a", "auscultadores": "os", "cuecas": "as", "ama": "a", "fatura": "a",
    "fato de banho": "o",
}
_GENRE_RE = re.compile(r"(?<![\w-])(" + "|".join(re.escape(m) for m in sorted(GENRE_CHANGE, key=len, reverse=True))
                       + r")s?(?![\w-])", re.I)


def phrase_europeenne(texte):
    """(texte converti, None) ou (None, raison du rejet)."""
    if texte and _GENRE_RE.search(texte):
        return None, "genre change (%s)" % _GENRE_RE.search(texte).group(1)
    t = europeu(texte)
    if t is None:
        return None, "enclise douteuse"
    b = bresilianismes(t)
    if b:
        return None, ", ".join(b)
    return t, None


def mot_europeen(mot):
    """Un mot ou une glose (pas une phrase) : vocabulaire et orthographe seulement."""
    if not mot:
        return mot
    t = remplacer_mots(mot.strip(), ORTHO_LISTE)
    t = remplacer_mots(t, BR_PT_VOCAB)
    return re.sub(r"[\wà-úÀ-Ú]+", lambda m: _ouvrir_voyelle(m.group(0)), t)


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    essais = [
        "Meu primo mora em Berlim há anos.", "Você me passa o sal?", "O chefe já está sabendo.",
        "Ele se alimenta muito bem desde janeiro.", "Estou falando ao telefone com a minha mãe.",
        "Eu me assustei com o barulho.", "Ela se interessa muito por moda.", "O cachorro é fiel ao dono.",
        "O número de acidentes está caindo bastante.", "O trem chega às nove.", "Tem um café aqui perto.",
        "Não me diga!", "Se chover, ficamos em casa.", "Nós nos encontramos amanhã.",
        "Ele se levantará cedo.", "A reunião foi um fenômeno econômico.", "Temos que sair agora.",
        "Ela vai se casar em maio.", "Com meu pai e de minha mãe.", "O bebê dorme.",
    ]
    for e in essais:
        print("%-55s -> %s" % (e, phrase_europeenne(e)))
