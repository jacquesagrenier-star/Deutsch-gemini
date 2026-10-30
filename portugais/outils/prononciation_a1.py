# -*- coding: utf-8 -*-
"""Prononcer le portugais du Portugal : les regles, pour un francophone, au
format de espanol/datos/prononciation.json. SOURCE : on corrige ici, puis
python portugais/outils/construire.py.

La prononciation decrite est celle de Lisbonne (la norme europeenne). Ce qui
la separe le plus du Bresil : les voyelles atones avalees, le s final en
« ch », le o final en « ou ». Chaque regle : id, graphie, api, court,
explication, exemples (mot | sens).
"""

GROUPES = [
("voyelles", [
 {"id": "e-avale", "graphie": "e (sans accent)", "api": "[ɨ] · muet",
  "court": "le e sans accent s'avale",
  "explication": "C'est le trait le plus frappant du Portugal : un e sans accent se réduit à presque rien, un « e » très bref, souvent muet. telefone se dit « t'l'FON' », pequeno « p'KÉ-nou », noite « NOÏT' ». C'est pour cela que le portugais d'Europe semble « manger » les mots.",
  "exemples": "telefone | le téléphone\npequeno | petit\nnoite | la nuit\nsete | sept\nleite | le lait\ndesculpe | excusez-moi"},
 {"id": "o-final", "graphie": "o (sans accent)", "api": "[u]",
  "court": "le o sans accent se dit « ou »",
  "explication": "En fin de mot, et souvent ailleurs quand il n'est pas accentué, le o se dit « ou » : obrigado « o-bri-GA-dou », carro « KA-rrou », Porto « POR-tou ». Accentué, il redevient o : avó (o ouvert), avô (o fermé).",
  "exemples": "obrigado | merci\ncarro | la voiture\nPorto | Porto\nfilho | le fils\ncomo | comment\npouco | peu"},
 {"id": "a-ouvert-ferme", "graphie": "a · á · â", "api": "[a] · [ɐ]",
  "court": "deux a : ouvert et sourd",
  "explication": "Le a accentué est ouvert, comme en français : casa « KA-za », chá. Sans accent, il devient un a sourd, plus fermé, presque un « e » de « le » : a casa, para. L'accent aigu (á) marque le a ouvert, le circonflexe (â) le a fermé : câmara.",
  "exemples": "casa | la maison\nchá | le thé\npara | pour\ncama | le lit\nmás | mauvaises\ncâmara | la mairie"},
 {"id": "nasales", "graphie": "ão · ã · õe · em · im · om · um", "api": "[ɐ̃w̃] · [ɐ̃] · [õj̃]",
  "court": "pão, mãe, põe : les nasales",
  "explication": "Le tilde (~) rend la voyelle nasale : ã comme « an » bref, ão comme « an » qui glisse vers « ou » (pão, não, mão), õe comme « on » qui glisse vers « i » (põe, lições). Une voyelle devant m ou n en fin de syllabe est nasale aussi : bem « bâïñ », sim, bom, um.",
  "exemples": "pão | le pain\nnão | non\nmãe | la mère\npõe | il met\nbem | bien\nsim | oui\num | un"},
 {"id": "ei-ou", "graphie": "ei · ou", "api": "[ɐj] · [o]",
  "court": "leite « lâïte », pouco « pôcou »",
  "explication": "À Lisbonne, ei se dit presque « âï » : leite « LÂÏT' », primeiro, dinheiro. Et ou se réduit à un o fermé : pouco « PÔ-kou », outro, ouvir.",
  "exemples": "leite | le lait\nprimeiro | premier\ndinheiro | l'argent\npouco | peu\noutro | autre\nouvir | écouter"},
]),
("consonnes", [
 {"id": "s-final", "graphie": "s · z (fin de syllabe)", "api": "[ʃ] · [ʒ]",
  "court": "dois « doïch », Lisboa « lijboa »",
  "explication": "En fin de mot ou devant une consonne, s (et z final) se dit « ch » : dois « DOÏCH », três, mais, feliz, escola « ch'KOLA ». Devant une consonne sonore (b, d, g, l, m, n, v), il devient « j » : Lisboa « lij-BOA », mesmo. C'est l'accent chuintant du Portugal.",
  "exemples": "dois | deux\ntrês | trois\nmais | plus\nescola | l'école\nLisboa | Lisbonne\nfeliz | heureux"},
 {"id": "s-z", "graphie": "s · ss · z · ç", "api": "[z] · [s]",
  "court": "casa « kaza », massa « massa »",
  "explication": "Entre deux voyelles, un s seul se dit « z » : casa, mesa, rosa. Pour le son « s » entre voyelles, on double : massa, passar. Le ç (avant a, o, u) et le c (avant e, i) se disent « s » : praça, cidade. Le z en début de syllabe : zero, fazer.",
  "exemples": "casa | la maison\nmesa | la table\npassar | passer\npraça | la place\ncidade | la ville\nfazer | faire"},
 {"id": "lh-nh", "graphie": "lh · nh", "api": "[ʎ] · [ɲ]",
  "court": "filho « fillou », vinho « vignou »",
  "explication": "lh se dit comme le « ill » de famille : filho, trabalho, olhar. nh se dit comme le « gn » de montagne : vinho, amanhã, senhor. Ils ne se séparent jamais en deux sons.",
  "exemples": "filho | le fils\ntrabalho | le travail\nolho | l'œil\nvinho | le vin\namanhã | demain\nsenhor | monsieur"},
 {"id": "ch-j-x", "graphie": "ch · j · g (e, i) · x", "api": "[ʃ] · [ʒ]",
  "court": "chave, já, gelado : comme en français",
  "explication": "ch se dit « ch » (chave, chá), j et g devant e ou i se disent « j » (já, gelado, hoje). Le x est capricieux : le plus souvent « ch » (caixa, baixo, peixe), parfois « z » (exame), « ks » (táxi) ou « s » (próximo). Il s'apprend avec le mot.",
  "exemples": "chave | la clé\njá | déjà\nhoje | aujourd'hui\ngelado | la glace\ncaixa | la caisse\ntáxi | le taxi\npróximo | prochain"},
 {"id": "r", "graphie": "r · rr", "api": "[ɾ] · [ʁ]",
  "court": "caro ≠ carro : deux r",
  "explication": "Entre deux voyelles, un r seul est battu, un petit coup de langue : caro, para, hora. En début de mot, après n ou l, et quand il est doublé (rr), il se dit au fond de la gorge, comme le r français : rua, carro, Henrique. Caro (cher) et carro (voiture) ne se confondent pas.",
  "exemples": "caro | cher\ncarro | la voiture\nhora | l'heure\nrua | la rue\nrio | le fleuve\nterra | la terre"},
 {"id": "h-muet", "graphie": "h", "api": "—",
  "court": "hoje, hotel : le h ne se dit pas",
  "explication": "Le h ne se prononce jamais en début de mot : hoje « OJ' », hotel « o-TÈL », homem. Il ne vit que dans ch, lh et nh. Há (il y a) et à (à la) se disent donc pareil.",
  "exemples": "hoje | aujourd'hui\nhotel | l'hôtel\nhomem | l'homme\nhora | l'heure\nhá | il y a"},
 {"id": "l-final", "graphie": "l (fin de syllabe)", "api": "[ɫ]",
  "court": "Portugal, sol : un l sombre",
  "explication": "En fin de syllabe, le l se dit au fond de la bouche, un l « sombre » proche du l anglais de « ball » : Portugal, sol, azul, mil. Au Brésil, il se change en « ou » ; au Portugal, il reste un l.",
  "exemples": "Portugal | le Portugal\nsol | le soleil\nazul | bleu\nmil | mille\nhotel | l'hôtel"},
]),
("accent", [
 {"id": "accent-tonique", "graphie": "´ · ^ · ~", "api": "ˈ",
  "court": "où tombe l'accent",
  "explication": "Sans accent écrit, un mot qui finit par a, e, o (et leur pluriel en -s) ou par -em, -am est accentué sur l'avant-dernière syllabe : CA-sa, ca-SA-co, FA-lam. Sinon, sur la dernière : ho-TEL, fa-LAR, a-ZUL. Un accent écrit montre la syllabe forte, contre la règle : CÉ-u, a-VÓ, MÚ-si-ca. Le tilde (ã, õ) marque aussi la syllabe forte.",
  "exemples": "casaco | la veste\nfalam | ils parlent\nhotel | l'hôtel\nfalar | parler\nmúsica | la musique\navó | la grand-mère\navô | le grand-père"},
]),
]

TITRES = {
    "pron_kicker": "Prononcer le portugais",
    "pron_intro": "Le portugais du Portugal s'écrit presque comme il se lit… à condition de savoir que les voyelles sans accent s'effacent et que le s final se dit « ch ». Ces règles couvrent ce qui surprend le plus un francophone. Touche un mot pour l'entendre.",
    "pron_voyelles": "Les voyelles",
    "pron_consonnes": "Les consonnes",
    "pron_accent": "L'accent tonique",
}
