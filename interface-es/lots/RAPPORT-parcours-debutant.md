# Rapport : parcours débutant en espagnol (15 nov. 2026)

## Ce qui est fait

| Source | Textes | Lot | Contrôle |
|---|---|---|---|
| `sources/dicts-premiers-pas.json` | 666 (626 couples allemand/français distincts) | `lots/dicts-premiers-pas.es.json` | 0 faute, 2 avis |
| `sources/dicts-a1-voyage.json` | 646 (644 distincts) | `lots/dicts-a1-voyage.es.json` | 0 faute, 8 avis |

Total : **1 312 textes**, toutes les clés, dans l'ordre de la source. Rien n'a été posé
(`dicts_langue.py pose` non lancé), aucun fichier touché hors de `interface-es/lots/`.

Les avis, tous regardés, aucun à corriger :

- Premiers pas : `/etapes/1/cartes/0/1` (« un café ») et `/etapes/5/cartes/4/1` (« un kilo de… »)
  sont identiques au français parce que l'espagnol s'écrit pareil.
- A1 voyage : huit « du francais ? ('du') » dans les notes de tableau — c'est le pronom
  **allemand** *du* cité entre guillemets (« du isst », « du wartest »…).

Contrôle de cohérence de mon côté : un même couple (allemand, français) reçoit partout le même
espagnol ; un même français n'a deux espagnols qu'une fois, exprès (voir « Was darf's sein? »).

## Partis pris (valables pour les deux fichiers)

- **Gloses de tableau** avec le pronom sujet (« yo me quedo », « tú tienes »), *ihr* → « ustedes … »
  sans parenthèse (le « à plusieurs » du français devient inutile), *Sie* → « usted … (formal) ».
  *sein* → « yo soy / estoy », etc.
- *möchten* → « quisiera » ; *Ich hätte gern* → « Quisiera » aussi.
- *Haben Sie…?* → « ¿Tiene…? » (usted, au singulier, pour rester fidèle à *Sie* ; en boutique
  l'Amérique dit aussi « ¿Tienen…? »).
- *Entschuldigung* devant une question → « Disculpe, … » ; seul → « perdón, disculpe ».
- *Wie geht's?* → « ¿Qué tal? » (l'allemand ne tranche pas entre *du* et *Sie*).
- Vocabulaire : el boleto (transport), la entrada (musée, concert), el celular, la computadora,
  el autobús, el jugo, la papa, la ducha, el baño (*Toilette*), la estación (*Bahnhof*), el andén
  (*Gleis*), la cuenta, el menú (*Speisekarte*), la reservación, la renta, la cobija, la curita,
  el mesero.
- Les mots et phrases allemands cités restent allemands ; « : » et « ? » sans espace ; guillemets «…».

## Sources fautives ou gênantes pour un hispanophone

Je n'ai trouvé aucune phrase française qui contredise l'allemand. En revanche, plusieurs textes
**allemands** sont écrits pour un francophone du Canada ; je les ai traduits tels quels, la
correction relève de la source :

- `premiers-pas /etapes/7/cartes/6/3` — *Wie sagt man « merci » auf Deutsch?* : le mot cité est
  français. Rendu « ¿Cómo se dice «merci» en alemán? ». Un hispanophone attendrait « gracias »,
  mais il faudrait changer la phrase allemande (et sa voix).
- `premiers-pas /etapes/7/cartes/3/1`, `/3/3`, `/etapes/7/phrases/2/s`, `/2/l/0`, `/2/l/1` —
  *Sprechen Sie Englisch · Französisch?* : rendu « ¿Habla usted inglés · francés? ». Un
  hispanophone demanderait *Spanisch*.
- *Ich komme aus Kanada* (premiers pas `/etapes/0/…`, A1 voyage `/escales/8/…`, `/escales/9/…`),
  *nach Frankreich*, *Mein Name ist Dupont* (`/escales/0/dialogue/l/3/s`) : gardés (Canadá,
  Francia, Dupont).
- `a1-voyage /escales/5/tableau/a` : le français écrit « Kann ich… ? » avec une espace avant
  « ? » dans une citation allemande ; écrit « Kann ich…? » en espagnol.
- `a1-voyage /escales/2/blocs/2`, `/escales/3/blocs/*`, etc. : l'ordre des variantes (`vs`) ne
  suit pas toujours l'exemple (`exs`) — sans effet sur la traduction, signalé au cas où.

## Doutes (clés précises)

- `premiers-pas /etapes/0/cartes/1/1`, `/2/1`, `/3/1`, `/4/1` — l'espagnol n'a que deux saluts pour
  quatre allemands. Rendu : *Guten Morgen* « buenos días (por la mañana) », *Guten Tag* « buenos
  días, buenas tardes (de día) », *Guten Abend* « buenas noches (al llegar) », *Gute Nacht*
  « buenas noches (al ir a dormir) ». Dans les phrases, *Guten Tag* = « Buenos días » et
  *Guten Abend* = « Buenas noches » ; du coup `/etapes/0/phrases/1/s` et son leurre `/l/0`
  restent distincts, mais `/etapes/0/cartes/1/3` et `/2/3` (Morgen / Tag) donnent le même salut.
- `premiers-pas /etapes/0/cartes/22/1` — *tschüss · auf Wiedersehen* → « chao · adiós ».
- `premiers-pas /etapes/0/cartes/12/1` — *freut mich* → « mucho gusto » (le français distinguait
  enchanté · enchantée ; l'espagnol n'en a pas besoin).
- `premiers-pas /etapes/1/tableau/l/5/1` — « un · una (einen delante de un masculino) » suit le
  français, qui simplifie (einen = masculin à l'accusatif).
- `premiers-pas /etapes/6/cartes/9/3`, `/10/3`, `/13/3` et leurres ; `a1-voyage /escales/1/blocs/2/*`,
  `/escales/6/tableau/a` — « Estoy enfermo », « Estoy resfriado », « Soy alérgico » : au masculin,
  comme le français ; l'allemand ne tranche pas. Les gloses de carte donnent les deux genres.
- `premiers-pas /etapes/7/cartes/17/3`, `/phrases/6/*` — « Berlín es muy bonito » (masculin ;
  « bonita » se défend aussi, par *la ciudad*).
- `a1-voyage /escales/7/tableau/l/*` — *ich habe verloren* glosé au **pretérito** (« yo perdí »),
  selon la consigne Perfekt → pretérito. La note `/escales/7/tableau/a` explique « haben + participe » :
  la glose ne montre donc pas la structure (« he perdido » la montrerait).
- `a1-voyage /escales/7/blocs/3/s` — *Ich habe … verpasst* → « Perdí … (se me fue) » : l'espagnol
  dit « perder el tren », même verbe que *verlieren* (`/escales/7/blocs/0/s` « Perdí … »). La
  parenthèse distingue les deux modèles ; les exemples (`Perdí el tren`) restent naturels.
- `a1-voyage /escales/1/blocs/3/s` — *Noch …, bitte.* → « Otro · otra …, por favor. » (l'accord
  oblige à donner les deux).
- `a1-voyage /installe/0/blocs/2/s` — *Ist die Wohnung …?* → « ¿El apartamento es / está …? »
  (amueblado prend *estar*, luminoso et tranquilo prennent *ser*).
- `a1-voyage /escales/10/blocs/1/*` — *Heute ist es …* → « Hoy hace … » (sol, viento, mucho calor)
  pour qu'un seul modèle couvre les trois variantes.
- `a1-voyage /escales/10/blocs/3/vs/1` — « se baigner » → « ¿Se puede entrar al agua aquí? »
  (pour ne pas répéter « nadar » ni casser le modèle « ¿Se puede … aquí? »).
- `a1-voyage /escales/2/dialogue/l/0/s` et `/escales/11/dialogue/l/0/s` — *Was darf's sein?* :
  « ¿Qué va a llevar? » à la boulangerie, « ¿Qué desea? » au musée (même français, deux lieux).
- `a1-voyage /suite/5/tableau/t` et `/a` — *spielen* : titre « Jugar, tocar », et la note précise
  « (jugar) … (tocar) », ajout utile en espagnol où ce sont deux verbes ; les gloses disent « yo juego ».
- `a1-voyage /installe/1/tableau/*` — *müssen* → « tener que » (titre et gloses), plus naturel
  que « deber » et cohérent avec « Tengo que llenar un formulario ».
- `a1-voyage /escales/9/tableau/a`, `/dialogue/l/2/s` — *Woher kommst du?* → « ¿De dónde vienes? »
  (pour coller au tableau *kommen aus* ; « ¿De dónde eres? » serait plus courant).

## À trancher

Mots où le Mexique et la Colombie ne disent pas la même chose (j'ai écrit la forme la plus
largement comprise) :

1. **el ascensor** (*Aufzug*) — Mexique : *elevador*. `premiers-pas /etapes/4/cartes/5/*`,
   `/phrases/5/l/1`, `/phrases/7/*` ; `a1-voyage /escales/0/blocs/3/*`, `/installe/0/blocs/4/*`.
2. **derecho** (*geradeaus*) — « Siga derecho », glose « derecho (de frente) » ; risque de
   confusion avec « a la derecha » pour un vrai débutant (« todo recto » est d'Espagne).
   `premiers-pas /etapes/2/cartes/10/*`, `/phrases/1/l/1`, `/phrases/2/*`, `/phrases/6/l/1` ;
   `a1-voyage /escales/3/blocs/4/vs/0`, `/escales/3/dialogue/l/2/s`.
3. **la taquilla** (*Schalter*, guichet de gare) — ou *la ventanilla*. `premiers-pas
   /etapes/3/cartes/11/*`, `/phrases/7/s` ; `a1-voyage /escales/4/dialogue/t`.
4. **un panecillo** (*Brötchen*) — Mexique : *bolillo* ; Colombie : *pan*. `premiers-pas
   /etapes/1/cartes/6/*`.
5. **una camiseta** (*T-Shirt*) — Mexique : *playera*. `premiers-pas /etapes/5/cartes/17/*`.
6. **la chaqueta** (*Jacke*) — Mexique : *chamarra*. `a1-voyage /escales/5/blocs/1/vs/2`,
   `/blocs/3/*`, `/dialogue/l/1/s`, `/escales/10/blocs/4/vs/2`.
7. **el bolso** (*Tasche*, pour le distinguer de *la bolsa* = *Tüte*) — Mexique : *bolsa*.
   `a1-voyage /escales/7/blocs/0/vs/2`, `/blocs/1/vs/0`, `/dialogue/l/1/s`, `/l/4/s`.
8. **la estampilla** (*Briefmarke*) — Mexique : *timbre*. `a1-voyage /escales/8/blocs/1/*`.
9. **el estacionamiento** (parking) — Colombie : *parqueadero*. `a1-voyage /escales/0/blocs/1/vs/2`.
10. **el ayuntamiento** (mairie, *Rathaus*) — Colombie : *alcaldía*. `a1-voyage /escales/3/blocs/0/vs/1`.
11. **un pedazo de pastel** (*ein Stück Kuchen*) — Colombie : *torta*. `a1-voyage /escales/2/tableau/a`.
12. **una parrillada** (barbecue) — Mexique : *carne asada* ; Colombie : *asado*. `a1-voyage
    /escales/10/blocs/3/vs/2`.
13. **la computadora portátil** (*Laptop*) — Mexique : *laptop* ; Colombie : *portátil*.
    `a1-voyage /escales/8/blocs/3/vs/1`.
14. **la renta / los gastos / el depósito** (*Miete, Nebenkosten, Kaution*) — Colombie : *arriendo*.
    `a1-voyage /installe/0/tableau/a`, `/blocs/1/*`, `/dialogue/l/3/s` ; et « contrato de
    arrendamiento » (*Mietvertrag*) `/installe/1/blocs/2/*`.
15. **la estación de policía** (*Polizeistation*) — choisi aussi parce qu'il est féminin comme le
    modèle « ¿Dónde está la … más cercana? ». `a1-voyage /escales/7/blocs/4/*`, `/dialogue/t`.
16. **el check-out** gardé en anglais, comme l'allemand (`premiers-pas /etapes/4/cartes/18/*`) ;
    autre choix : « ¿A qué hora hay que dejar la habitación? ».
17. **Les quatre saluts** (voir Doutes) : garder « buenas noches » pour *Guten Abend*, ou
    « buenas tardes » comme le dit une partie de l'Amérique latine en fin de journée ?
18. **Les textes allemands faits pour un francophone** (« merci », *Französisch*, *Kanada*,
    *Dupont*, *nach Frankreich*) : les laisser, ou écrire une variante allemande pour
    hispanophones (ce qui touche l'allemand et ses voix) ?
19. **Le genre par défaut** des phrases à la première personne (« Estoy enfermo », « Soy
    alérgico ») : masculin comme le français, ou une forme double ?
