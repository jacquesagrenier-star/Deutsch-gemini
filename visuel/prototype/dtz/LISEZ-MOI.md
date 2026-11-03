# Le DTZ avec Mark et Anna

La préparation au DTZ de Wortando (allemand), décidée par Jacques le 3 nov. 2026 : une **répétition**. Mark aide
l'élève à préparer l'examen, Anna joue l'examinatrice, et l'élève répond pour lui-même. On reprend le **format** du DTZ (Prüfungshandbuch du Goethe-Institut et de telc, 2009), **jamais son
contenu** : tous les textes et les sons sont les nôtres.

Deux sessions s'en partagent le travail. Celle-ci fait Écouter (Hören), Lire (Lesen) et l'examen blanc qui les
regroupe. La session « Préparation au DTZ avec Mark et Anna » fait l'oral et l'écrit.

## Les fichiers

| fichier | rôle |
|---|---|
| `dtz.html` | la page : le style et le squelette ; elle s'ouvre comme un thème illustré (`sceneCadre`, `postMessage`) |
| `commun.js` | ce qui sert à toutes les épreuves : voix, minuterie, panneau, tirage, verdict global, et l'accueil construit à partir des inscriptions (`DTZ.partie()`, `DTZ.examen()`, `DTZ.charger()`, `DTZ.surRetour()`) |
| `hoeren-lesen.js` | Écouter et Lire : l'entraînement, l'examen blanc, la feuille de réponses, le verdict sur 45 et le corrigé |
| `sprechen-schreiben.js` | Parler et Écrire (session de l'oral et de l'écrit) |
| `donnees/hoeren.json` | les séries de Hören : 20 items en 4 Teile, les voix, les consignes |
| `donnees/lesen.json` | les séries de Lesen : 25 items en 5 Teile |
| `outils/relecture.py` | refait `RELECTURE-DE.md`, le fichier destiné au germanophone (sans l'app) ; les sections de l'oral et de l'écrit viennent de `outils/relecture_oral.py` |
| `RELECTURE-DE.md` | **dérivé** : on ne le corrige jamais à la main, on corrige les JSON puis on relance le script |
| `../tests/dtz.py` | le contrôle : format du DTZ (nombre d'items, numéros, exemples), réponses valables, feuille non devinable, mots clés présents dans le corpus |

## Les commandes

```
python tests/dtz.py --mots
python visuel/prototype/dtz/outils/relecture.py
```

La page s'essaie servie par HTTP (pas en `file://`, à cause du `fetch` des JSON) :
`visuel/prototype/dtz/dtz.html?rapide=1` raccourcit les pauses de l'examen, pour les essais seulement.

## Les règles

- **Séries 1-3 : examen blanc seulement.** Les suivantes tournent en entraînement. Tant qu'il n'existe qu'une
  série (la maquette), elle sert aux deux.
- **`bon` donne l'indice de la bonne réponse à sa place** (a, b ou c), comme sur la feuille d'examen. Le contrôle
  refuse qu'une lettre porte plus de la moitié des bonnes réponses d'une série.
- **Les documents de Lesen sont mis en page en HTML, jamais en image** : un texte dans une image ne se relit
  pas, ne se corrige pas et ne s'agrandit pas. Les images ne servent qu'aux photos.
- **Les mots clés** (`mots`) entrent dans la répétition espacée de l'app, sous la forme que lit `carteDeScene()` :
  un nom avec son genre, un verbe à l'infinitif, un adjectif. Rien d'autre.
- **La voix** : en attendant les enregistrements (ElevenLabs multilingual v2, qui demandent l'accord de Jacques),
  c'est la voix du téléphone. Les nombres s'écrivent en chiffres, et la voix en recevra la lecture en lettres
  (`audio/lectures/de.json`).
- **Mark s'appelle Mark Gagnon** dans les documents et habite Gartenstraße 12. Ce nom est proposé et n'est pas
  encore validé par Jacques. Les textes d'Écouter et Lire viennent de sa vie à Berlin (son répondeur, son
  courrier) : il ne passe pas le DTZ, il aide l'élève à le préparer.
