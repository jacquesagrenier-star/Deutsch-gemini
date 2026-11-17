# Rapport : feuilles de conjugaison (A2 à C1) en espagnol d'Amérique latine

Lot : `interface-es/lots/dicts-conjugaison.es.json` (source `interface-es/sources/dicts-conjugaison.json`).

## Chiffres

- 336 textes rendus sur 336, dans l'ordre de la source : 42 feuilles (A2 12, B1 12, B2 10, C1 8),
  chacune 1 titre, 6 gloses ou phrases, 1 explication.
- Contrôle `dicts_langue.py controle conjugaison.json` : **0 faute, 4 avis**. Les 4 avis sont le
  pronom allemand « du » cité dans une explication (A2/9/a, A2/10/a, B1/0/a, B1/9/a) : voulus.
- Rien n'a été posé (`pose` non lancé).

## Choix d'ensemble

- **Perfekt → pretérito** partout (cociné, compraste, Ya pagué), y compris dans les feuilles
  « Le passé avec haben / sein » : c'est ce que dit un Mexicain. La forme composée n'est gardée
  que dans B2/0/l/2 (« Ha sido construido (ya está hecho) »), où la feuille oppose wurde gebaut
  et ist gebaut worden.
- **ihr → ustedes**, **Sie → usted** ; quand la feuille distingue les deux, une parenthèse le dit :
  « usted vivió (formal) », « ¡Vengan con nosotros! (a varios, de tú) », « ¡Pase! (formal) ».
- Les gloses de 1re et 2e personne sont sans pronom (cociné, compraste) ; la 3e personne et
  ustedes le gardent (él · ella trabajó, ustedes aprendieron), faute de quoi la forme est ambiguë.
- Passif : « se » ou « están + gérondif » quand c'est ce qu'on dit (Aquí se habla alemán, Están
  poniendo la mesa), pasiva avec ser quand la feuille montre la forme (Fue construido en 1990,
  Él fue operado, Tiene que ser construido).
- Les explications qui comparaient au **français** sont adaptées à l'espagnol (voir « Sources »).

## Doutes (clés précises)

- `/niveaux/A2/0/l/*`, `/niveaux/A2/1/l/*`, `/niveaux/A2/2/l/*` : pretérito simple (cociné, comí,
  fui) et non « he cocinado ». À confirmer : un apprenant pourrait mieux voir haben + participe
  avec « he cocinado », mais ce n'est pas l'usage en Amérique latine.
- `/niveaux/A2/0/l/5/1`, `/niveaux/A2/1/l/5/1`, `/niveaux/B1/1/l/5/1` : « sie · Sie » rendu
  « ellos … · usted … (formal) » ; Sie peut aussi être ustedes, non écrit pour rester court.
- `/niveaux/A2/1/l/1/1` : « bebiste » plutôt que « tomaste » (plus mexicain), pour ne pas se
  confondre avec la ligne 5 de la même feuille (genommen → tomaron).
- `/niveaux/A2/2/l/5/1` : « ellos se convirtieron (en…) » pour sie sind geworden ; « llegaron a
  ser » ou « se volvieron » possibles.
- `/niveaux/A2/5/l/0/1` : « Ya pagué. » (les consignes citent « Ya he comido » ; le Mexique dit
  « Ya pagué »).
- `/niveaux/A2/5/l/4/1` : « ¿Olvidaron la palabra? (ustedes) », parenthèse ajoutée pour marquer ihr.
- `/niveaux/A2/7/t` et `/niveaux/A2/7/l/0/1`, `/l/1/1`, `/l/3/1` : war rendu par « estaba » (lieu,
  état) ; le titre dit « Yo estaba, yo tenía » et laisse « era » de côté.
- `/niveaux/A2/8/l/3/1` : « No teníamos permitido fumar. » (durften nicht) ; « No nos dejaban
  fumar » plus parlé.
- `/niveaux/A2/10/t`, `/l/2/1`, `/l/3/1`, `/niveaux/B2/6/l/0/1`, `/l/4/1` : werden sans équivalent
  unique : « volverse, llegar a ser » en titre, « él se hace médico », « ella se hizo médica ».
- `/niveaux/B1/7/l/2/1` : « ¿Abriría usted la ventana? » garde le würde ; « ¿Podría abrir la
  ventana? » serait plus courant.
- `/niveaux/B1/7/l/5/1` : « ¿Podría interrumpir un momento? » (évite lo / la pour stören).
- `/niveaux/B1/8/l/*` : futur simple (Te llamaré, Mañana lloverá) pour montrer la forme, et
  « ir a » pour deux lignes comme le français ; un Mexicain dirait partout « voy a ».
- `/niveaux/B1/9/l/0/1`, `/l/1/1` : « Mando reparar mi carro. », « Vas a que te corten el pelo. »
  (faire faire n'a pas de tournure unique en espagnol).
- `/niveaux/B2/0/l/0/1` : « El puente se está construyendo. » ; les lignes suivantes passent au
  masculin (die Brücke → el puente), comme le français.
- `/niveaux/B2/1/l/3/1`, `/niveaux/C1/6/l/5/1` : « las tabletas » (Tabletten) ; « pastillas » ou
  « comprimidos » selon le pays — à faire relire par un soignant.
- `/niveaux/B2/6/l/3/1`, `/niveaux/C1/4/l/2/1` : supposition rendue par « debe de… » (« ha de
  estar enfermo » est mexicain, moins neutre).
- `/niveaux/B2/7/l/3/1` : « habría (de «hay») » pour es gäbe, précision ajoutée car « habría »
  seul se lit aussi comme auxiliaire.
- `/niveaux/B2/8/l/3/1` : « un huevo cocido » (« huevo duro » ailleurs).
- `/niveaux/C1/0/l/*`, `/niveaux/C1/2/l/*` : le verbe introducteur allemand est au présent (Er
  sagt), donc « Él dice que está enfermo » et non « dijo que estaba » ; le passé n'apparaît que
  là où l'allemand dit sagten / fragte (C1/1/l/1, C1/1/l/5, C1/3/l/4, C1/3/l/5).
- `/niveaux/C1/0/l/5/1`, `/niveaux/C1/2/l/5/1` : la distance du Konjunktiv I seul rendue par
  « Según él, … » et « Según dicen, … » plutôt que par le conditionnel de presse (« habría sido
  vendida »).
- `/niveaux/C1/3/l/3/1` : « Él dice que yo espere. » (ordre rapporté) ; « que debo esperar » possible.
- `/niveaux/C1/7/l/2/1` : « tener consideración con » pour Rücksicht nehmen auf.

## Sources fautives ou propres au français

- `/niveaux/A2/6/a` : le français dit « même quand le français dit "je me suis" » ; sans objet en
  espagnol (haber partout), retiré comme dans l'anglais.
- `/niveaux/B1/1/a` : « Le français a deux temps (j'allais, j'allai) » → « El español tiene dos
  tiempos (iba, fui) » ; l'anglais avait supprimé la phrase.
- `/niveaux/B1/10/a` : « souvent sans rapport avec le français » → « no es la que esperarías en
  español ».
- `/niveaux/B1/11/a` : « Le français dit souvent "on" » → « El español dice a menudo «se» ».
- `/niveaux/C1/4/a` : « comme le futur antérieur français » → « como el futuro perfecto del español ».
- `/niveaux/C1/6/a` : « Là où le français met une relative » → « Donde el español pone… ».
- `/niveaux/A2/5/l/1/1` : le français (« Tu as compris ? ») omet *das* ; l'espagnol suit
  l'allemand (« ¿Entendiste eso? »).
- `/niveaux/A2/7/l/4/1` : le français met un passé composé (« Vous avez eu de la chance ») dans
  une feuille d'imparfaits ; gardé (« Ustedes tuvieron suerte »), c'est le sens.
- `/niveaux/B1/11/l/2/1` : le français (« La porte ouvre à huit heures ») n'est pas un passif ;
  l'espagnol dit « La puerta se abre a las ocho ».
- Aucune faute relevée dans l'allemand.

## À trancher

- Pretérito simple ou « he + participio » dans les trois feuilles du Perfekt A2 (voir doutes).
- « tabletas / pastillas », « huevo cocido / duro » : mots qui varient d'un pays à l'autre.
