# Rapport : étapes, repères, prononciation (espagnol d'Amérique latine, 15 nov. 2026)

## Ce qui est fait

| Lot | Fichier | Textes | Contrôle |
|---|---|---|---|
| Étapes A2-C1 et lignes « Tu sais… » | `etapes.es.json` | 161 sur 161 | s'analyse, 161 clés copiées de la source, aucune ligne « Tu sais… » de plus de 60 signes |
| Repères | `dicts-reperes.es.json` | 57 sur 57 | `dicts_langue.py controle reperes.json` : 0 faute, 1 avis (« gris », identique au français, juste) |
| Prononciation | `prononciation.es.json` | 25 règles sur 25, `[court, explication]` | s'analyse, mêmes identifiants et même ordre que la source |

`tests/etapes_construire.py` n'a pas été lancé : il lit `etapes/traductions/es.json`, où je n'écris pas.

## Choix à connaître

### Étapes
- Amorces : « Ahora ya sabes… » et « Esta semana aprendiste a… ». Toutes les lignes sont à l'infinitif, en minuscules, sans point, et se lisent après les deux.
- **« Quand j'étais petit »** → « En mi infancia » / « contar cómo era tu infancia » : tournure sans genre, au lieu de « Cuando era niño » (masculin).
- « Réussir mon A2 / B1 / C1 » → « Aprobar mi A2… ».
- « « Tu aurais dû » » → « «Deberías haber…» » (avec points de suspension, comme le portugais).
- « rapporter » (C1, discours indirect) → « contar lo que dijo alguien », puis « transmitir… » pour les deux lignes suivantes.
- Vocabulaire d'Amérique : boleto, apartamento, llenar un formulario, reportar un robo, hablar del clima, pasatiempos, tomar el tren.

### Repères
- Astuce de l'alphabet **réécrite** : E, I, U se disent comme en espagnol, donc l'astuce française ne servait à rien. Elle signale C « tse », G « gue », H « ha », J « yot », V « fau », W « ve », Z « tset ».
- Genre : l'astuce de `das` commence par « das es el neutro, un tercer género que el español no tiene » ; celle de `die` note que -ion et -tät répondent à « -ión » et « -dad », féminins aussi en espagnol.
- Couleurs : un seul mot par couleur (café, anaranjado, rosado, morado), le premier des deux mots retenus dans les cartes du corpus (« café, marrón », etc.).

### Prononciation
- Tout est réécrit sur les sons de l'espagnol, d'après les repères fournis. Ajouts de mon cru, à relire :
  - `sp-st` : « sin «e» de apoyo delante: no «eshport» » (l'hispanophone ajoute un e devant s + consonne) ;
  - `s` : « pon la mano en la garganta: debe vibrar » ;
  - `w` : « no es la «b» de «vaca» ni la «u» de «web» » ;
  - `au` : « nada que cambiar » (identique à « auto »).

## Doutes précis (à trancher)

1. **« faire tes démarches à la mairie »** → « en el ayuntamiento » : mot du Mexique ; la Colombie dit « la alcaldía », d'autres pays « la municipalidad ». Aucun mot n'est commun à toute l'Amérique.
2. **« Chez le médecin »** → « En el médico » : courant ; « Con el doctor » ou « En el consultorio » sont possibles.
3. **braun → « café »** : mot du Mexique et de la Colombie, mais il se lit aussi « le café » ; « marrón » est compris partout. De même « rosado » (le Mexique dit « rosa ») et « anaranjado » (« naranja »).
4. **`ch-dur`** : « como la «j» de «jamón» dicha con fuerza ». En Colombie et aux Caraïbes, la « j » est un simple souffle, d'où « dicha con fuerza » ; un Mexicain n'a rien à changer.
5. **`a-trema`** : « parecida a la «e» de «perro» ». L'espagnol n'a qu'un « e » ; l'ouverture devant « rr » est réelle mais peu consciente. On peut couper la comparaison.
6. **`s`** : j'ai écarté la comparaison avec « mismo » (le s sonore n'y existe pas dans tous les accents) au profit du bourdonnement « zzz ».
7. **`v`** : Vase, Klavier « suenan como la w alemana », plutôt que « gardent le v », parce que le « v » espagnol se dit « b ».
8. **« Parler soutenu »** → « Hablar en registro formal » : « registro culto » serait plus exact mais moins simple.

## Sources fautives ou à signaler

- **Prononciation** : les repères de la consigne citent le « -e final faible, jamais muet », mais aucune des 25 règles ne le porte. Rien n'a été ajouté. Une règle neuve serait à créer dans toutes les langues.
- **Prononciation, `eu`** : le français écrit heute « hoïte » ; j'ai pris träumen « troimen » comme second exemple, pour montrer aussi « äu » et éviter le h soufflé dans une transcription.
- **Repères, `/reperes/0/a`** : « dreizehn = trois-dix » rendu « tres-diez » comme demandé. L'espagnol dit l'inverse (« dieci-séis » = dix-et-six), ce que l'astuce ne dit pas, faute de place.
- Aucune faute relevée dans l'allemand des trois sources.
