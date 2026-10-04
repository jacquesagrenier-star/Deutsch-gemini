# -*- coding: utf-8 -*-
"""Source des moyens mnémotechniques : modifier ici, puis relancer
`python japonais/kana/outils/mnemoniques_source.py` pour refaire mnemoniques.json.
Chaque ligne : (signe, romaji, français, anglais). Le son-clé est entre ** **."""
import json

M = [
# hiragana
("あ","a","Une **a**raignée accrochée à une croix : la grosse boucle en bas, c'est son ventre.","An **a**ntenna on two crossed sticks, its cable tangled into a big loop underneath."),
("い","i","Deux **i** sans leurs points, penchés l'un vers l'autre, qui se racontent un secret : « **hi** hi ».","Two strands of spaghetti being **ea**ten; the one on the right is already shorter."),
("う","u","Un petit chapeau sur une grande oreille : on tend l'oreille, « **ou** ça ? ».","Someone doubled over, hat on their head, groaning '**oo**f'."),
("え","e","Un patineur avec un bonnet (le petit trait) qui fait un zigzag sur la glace : quelle **é**légance !","An **e**lf in a little hat dancing a zigzag on one leg."),
("お","o","Un jongleur qui laisse échapper sa balle (le point en haut à droite) : « **Oh** ! »","A golfer mid-swing, the ball (the dot) flying off: '**Oh**!'"),
("か","ka","Un **ca**nard qui lève l'aile en crochet et lâche un petit « coin » (le trait à droite).","A **ka**rate chop: a raised arm with a little spark beside the blow."),
("き","ki","Une vieille clé : deux barres pour les dents, l'anneau en bas. Elle traîne sur la table : elle est à **qui** ?","A s**ki** lift: two cables crossing the pole, the chair swinging below."),
("く","ku","Le bec ouvert d'un **cou**cou qui sort de son horloge.","The open beak of a **coo**ing pigeon."),
("け","ke","Une **que**ue de billard (le trait de gauche) posée contre une table, vue de profil.","A **ke**g on its side: a post on the left, a tap dripping on the right."),
("こ","ko","Deux **co**tons-tiges posés l'un au-dessus de l'autre.","Two **co**-workers asleep on bunk beds, one above the other."),
("さ","sa","Une épée plantée dans un **sa**c : la lame en biais, le sac arrondi en dessous.","A **sa**w stuck through a plank, its curved handle hanging below."),
("し","shi","La queue d'un **chi**en vue de profil : elle descend, puis remonte en remuant.","A fishing hook: '**She** caught one!'"),
("す","su","Une **sou**ris suspendue à une barre par sa queue, qui a fait un nœud au milieu.","**Sou**p slurped through a straw with a loop in it."),
("せ","se","Une grande bouche ouverte avec une seule dent : « **C'est** bon ! »","A wide mouth with one tall fang: a vampire's **se**t of teeth."),
("そ","so","Un **saut** à l'élastique : un zigzag en haut, puis la grande chute en courbe.","A zigzag of **sew**ing thread, ending in a curl."),
("た","ta","Un « t » et un « a » collés l'un à l'autre : **t** + **a** = **ta**.","A 't' and an 'a' squeezed together: **t** + **a** = **ta**."),
("ち","chi","Quelqu'un qui lève son verre, le bras plié, et trinque : « **Tchi**n ! »","A **chee**rleader with one arm up, body curving forward."),
("つ","tsu","Une grosse vague qui roule vers la droite : un **tsu**nami.","A big wave rolling sideways: a **tsu**nami."),
("て","te","Un **té** de golf tordu par un coup trop fort.","A **te**nt pole that buckled: a T with a bent stem."),
("と","to","Un petit clou planté dans une **to**mate (la courbe en dessous).","A **toa**d (the curve) with a twig landed on its head."),
("な","na","Un **na**vigateur près du mât (la croix) qui fait un nœud à sa voile, un point d'exclamation au-dessus de la tête.","A **na**ughty kid (the dot) next to a cross, tying a knot in his shoelace."),
("に","ni","Un **ni**d posé contre un tronc : le tronc à gauche, deux brindilles à droite.","A **nee**dle (the left stroke) next to two loose threads."),
("ぬ","nu","Des **nou**illes enroulées autour de baguettes ; la petite boucle, c'est la nouille qui pend.","A tangled phone cord with a loop at the end: time for a **new** one."),
("ね","ne","Un **nez** qui coule : la goutte forme une boucle au bout.","A **ne**rvous snake that coiled its tail into a loop."),
("の","no","Le panneau d'interdiction, un cercle barré : « **Non** ! »","A '**No**' sign: a circle with a slash through it."),
("は","ha","Quelqu'un qui se tient les côtes en riant : « **Ha** ha ! » — lui à gauche, sa bouche ouverte à droite.","A **ha**t stand: a tall pole on the left, a hat with a loop on the right."),
("ひ","hi","Un grand sourire en coin : « **Hi** hi hi ! »","A smug grin: '**He** he he!'"),
("ふ","fu","Un visage aux joues gonflées qui souffle « **fou** » sur une bougie.","A **foo**tballer juggling: the ball on top, a foot kicking on each side."),
("へ","he","Le toit pointu d'une maison : « **Hé**, il pleut ! »","A **he**ad peeking over a hill."),
("ほ","ho","Le Père Noël à côté de sa porte (le trait de gauche), avec son sapin à deux branches et une boule : « **Ho** ho ho ! »","A **ho**se reel: a post with the hose wound into a coil."),
("ま","ma","Une **ma**man en tablier : deux barres pour les bras, la boucle pour le nœud dans le dos.","A **ma**st with two sails and a coil of rope at its foot."),
("み","mi","Un ruban de cadeau noué en boucle, avec la ficelle qui file à droite : un cadeau pour **Mi**mi.","It looks like the number 21: '**Me** at 21.'"),
("む","mu","Une vache qui meugle « **mou** » : la boucle est son museau, le point sa corne.","A cow going '**moo**': a looped snout and one horn (the dot)."),
("め","me","Un œil en amande — et justement, « œil » se dit **me** en japonais. **Mé**fie-toi de lui !","An eye with its pupil — the Japanese word for eye is '**me**' (as in 'met')."),
("も","mo","Un hameçon avec deux vers enfilés : **mo**rdez, les poissons !","A fishing hook with two worms: '**Mo**re bait!'"),
("や","ya","Un **ya**k vu de profil : sa corne recourbée, une patte, et la queue.","A slingshot about to fire: '**Ya**hoo!'"),
("ゆ","yu","Un poisson qui fait demi-tour dans son bocal : « **You**pi ! »","A fish making a **U**-turn in its bowl."),
("よ","yo","Un **yo**-yo qui pend au bout de sa ficelle.","A **yo**ga pose: one leg looped around the body."),
("ら","ra","Un **ra**t assis sur sa queue, avec une petite oreille dressée.","A **ra**bbit sitting with one ear up."),
("り","ri","Deux **ri**deaux : un court à gauche, un long à droite.","A **ree**f: two pillars of coral, the right one taller."),
("る","ru","Une route en zigzag qui finit sur une **rou**e (la boucle).","A **rou**te that zigzags and ends in a roundabout."),
("れ","re","Un danseur, une jambe levée vers l'arrière : il **ré**pète son pas.","Someone kicking a leg out as they **re**treat."),
("ろ","ro","Comme る, mais la **ro**ute ne se referme pas : pas de rond-point.","A bent oar from a **row**ing boat: like る, but it never closes into a loop."),
("わ","wa","Un chien assis, une patte tendue, le dos rond : « **Oua**f ! »","A swan on the **wa**ter, its neck bent round."),
("を","wo","Un plongeur qui saute du tremplin la tête la première : « **Oh** ! »","A runner tripping over a hurdle: '**Oh**, no!'"),
("ん","n","Une lettre **n** écrite à toute vitesse.","A lowercase **n** scribbled in a hurry."),
# katakana
("ア","a","Une **ha**che, lame en haut à droite, manche qui descend à gauche. « **A**ïe ! »","An **a**xe: the blade at the top right, the handle sweeping down."),
("イ","i","Une flèche plantée dans un piquet : « **I**ci ! »","An **ea**gle perched on a branch."),
("ウ","u","Une chouette (le point est sa tête) perchée sur son nid : « **Hou** hou ! »","Like う with a roof added: someone sheltering, '**Oo**h, it's raining.'"),
("エ","e","Une poutre d'**é**chafaudage en forme de I.","An **e**levator shaft seen from the side: floor, shaft, floor."),
("オ","o","Un bonhomme qui ouvre les bras, une jambe en l'air : « **Oh** ! »","An **o**pera singer with arms flung wide."),
("カ","ka","Le même **ca**nard que か, mais muet : plus de petit trait.","The same **ka**rate chop as か — no spark this time: you missed."),
("キ","ki","Comme き sans l'anneau : la clé a perdu son anneau, à **qui** est-elle ?","The s**ki** lift of き, with the chair gone."),
("ク","ku","Le bec d'un **cou**cou vu de côté, sous un petit toit.","A **coo**kie with a corner bitten off."),
("ケ","ke","Une **que**ue de billard qui tape dans la bande du haut.","A **ke**tchup bottle tipped over, its cap on the left."),
("コ","ko","Le **co**in d'une pièce : deux murs qui se rejoignent.","The **co**rner of a box."),
("サ","sa","Une barrière à deux poteaux, dont un qui penche : on **sa**ute par-dessus.","A **sa**ddle thrown over a fence."),
("シ","shi","Un visage de profil qui sourit vers le ciel : deux yeux à gauche, un sourire qui monte. « **Chi**c ! »","**She** smiles up at the sky: two eyes on the left, a smile rising from below."),
("ス","su","Quelqu'un qui court, une jambe en arrière : il a **sou**tiré un bonbon.","A **su**perhero mid-stride."),
("セ","se","La bouche à une dent de せ, en plus anguleuse : « **C'est** dur ! »","A squarer version of せ: the vampire's **se**t of teeth again."),
("ソ","so","Deux gouttes qui tombent d'en haut : il pleut à **seau**x.","A needle and thread **sew**ing downward from the top."),
("タ","ta","Comme ク, avec une **ta**che au milieu.","A **ta**co with filling inside (the middle stroke)."),
("チ","chi","Un verre à pied avec un chapeau penché dessus : « **Tchi**n ! »","A **chee**rleader in a hat, arms out, legs swinging left."),
("ツ","tsu","Un **tsu**nami vu de face : deux gouttes en haut, la vague qui s'abat depuis la droite.","A **tsu**nami crashing down from the top right."),
("テ","te","Une antenne de **té**lé sur un toit.","A **te**levision aerial on a roof."),
("ト","to","Un poteau indicateur avec une seule flèche : « **To**ut droit ! »","A **to**tem pole with one arm sticking out."),
("ナ","na","Une épée plantée de travers : « Pas comme ça, **Na**poléon ! »","A **na**il hammered in crooked."),
("ニ","ni","Deux traits, comme le kanji 二 qui veut dire « deux » et se lit justement **ni**.","Two lines, just like the kanji 二, 'two', which is read **ni**."),
("ヌ","nu","Des baguettes qui pincent une **nou**ille (le petit trait).","Chopsticks pinching a **noo**dle."),
("ネ","ne","Un épouvantail : une tête, des bras, un bâton… et un **nez** (le dernier point).","A **ne**cktie hanging on a peg."),
("ノ","no","Un seul trait, comme un « **Non** » qu'on barre d'un coup.","A single slash: '**No**!'"),
("ハ","ha","Deux traits qui s'écartent comme une bouche qui éclate de rire : « **Ha** ! »","Two strands of **ha**ir falling apart."),
("ヒ","hi","Quelqu'un assis par terre qui pouffe : « **Hi** hi ! »","A **he**-man doing sit-ups."),
("フ","fu","Un **fou**lard plié qui flotte au vent.","A **foo**t seen from the side."),
("ヘ","he","Comme へ : le toit d'une maison, « **Hé** ! »","Same as へ: a **he**ad over a hill."),
("ホ","ho","Un sapin de Noël avec deux petites boules : « **Ho** ho ho ! »","A Christmas tree with two baubles: '**Ho** ho ho!'"),
("マ","ma","Le bec d'une **ma**man oiseau qui tend la becquée (le petit trait).","A **ma**ma bird's beak with a crumb of food."),
("ミ","mi","Trois **mi**ettes alignées.","Three scratch marks: the cat says '**me**ow'."),
("ム","mu","Le nez d'une vache vu de face : « **Meuh** ».","A cow's nose, seen head-on: '**moo**'."),
("メ","me","Une croix sur une carte au trésor : « **Mé**moire, c'est ici ! »","An X marks the spot: '**Me**et me here.'"),
("モ","mo","Le même hameçon que も, mais tout raidi : **mo**rdez quand même !","The same hook as も, straightened out: we need **mo**re bait."),
("ヤ","ya","Un **ya**k vu de profil, la corne levée vers le ciel.","A **ya**k's horn pointing up at the sky."),
("ユ","yu","Un banc de musculation avec ses haltères : « **You**pi, fini ! »","A **U**-turn sign turned on its side."),
("ヨ","yo","Un peigne à trois dents : le rappeur se recoiffe, « **Yo** ! »","A backwards E: '**Yo**, that's backwards!'"),
("ラ","ra","Un **ra**dar posé sur un toit.","A **ra**bbit's ear folded over."),
("リ","ri","Comme り : deux **ri**deaux, le court et le long.","The coral **ree**f of り, drawn with a ruler."),
("ル","ru","Les deux racines d'un arbre, dont une qui **rou**le vers la droite.","Two **roo**ts of a tree, one curling to the right."),
("レ","re","Une jambe qui part toute seule sous le marteau du médecin : un **ré**flexe.","A leg jerking forward: a **re**flex."),
("ロ","ro","La tête carrée d'un **ro**bot.","A square **ro**bot head."),
("ワ","wa","Un bol renversé : « **Oua**h, toute la soupe ! »","A **wa**ter jug tipped over."),
("ヲ","wo","Une chaise qui bascule en arrière : « **Oh** ! »","A bucket tipping over: '**Whoa**!'"),
("ン","n","Un point à gauche et un trait qui remonte, comme un « **hein** ? » qui monte à la fin d'une question.","One eye winking and a smile rising from the bottom left: '**N**ice!'"),
]

assert len(M) == 92, len(M)
assert len({m[0] for m in M}) == 92
doc = {
    "description": "Brouillon de moyens mnémotechniques visuels, un par signe de base. Le français et l'anglais sont écrits séparément : chacun relie la forme du signe à un son de sa propre langue. Le son-clé est entre ** **.",
    "statut": "brouillon à relire",
    "mnemoniques": [
        {"signe": s, "ecriture": "hiragana" if "぀" <= s <= "ゟ" else "katakana",
         "romaji": "o" if r == "wo" else r, "fr": fr, "en": en, "statut": "brouillon à relire"}
        for s, r, fr, en in M
    ],
}
import os
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mnemoniques.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("ok", len(M))
