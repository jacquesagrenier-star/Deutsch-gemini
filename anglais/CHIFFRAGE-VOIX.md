# Vraies voix pour l'anglais : chiffrage (28 oct. 2026)

> **29 oct. 2026 : accordé pour A1-A2, en américain.** Jacques : « J'ai ajouté des crédits, donc fais les voix pour A1. Et A2. »
> - Le comparatif à l'aveugle est produit (1 350 crédits) : `audio/a_ecouter_voix/anglais_us/ECOUTER.html`.
> - Les 43 lectures en toutes lettres sont faites (`audio/lectures/en.json`, américain et britannique), contrôlées par `audio/lectures.py` et le vérificateur.
> - Le script est `audio/generer_en.py` : v2 seulement, A1-A2 seulement, et il refuse de tourner tant que la voix n'est pas choisie.
> - Pas de britannique ni de B1-C1 sans une nouvelle demande de Jacques.

Jacques : « la voix pour apprendre l'anglais est épouvantable ». Deux réponses :

1. **Tout de suite, sans dépense** : la voix du téléphone est mieux choisie. Elle ne prend plus que la variante choisie (en-US ou en-GB) et les meilleures voix de l'appareil, et ne prend jamais les voix fantaisie d'Apple ni les voix Eloquence (voir `scoreVoixAnglaise` dans `index.html`).
2. **Des voix enregistrées**, comme l'allemand (Aurora) et l'espagnol (Lolita et Monica) : ElevenLabs, modèle multilingual v2 (Flash interdit depuis le 12 oct.). Ce document les chiffre. **Rien n'est généré.**

## Ce qu'il faudrait faire dire

Tout est mesuré par `python anglais/outils/manifest_voix.py`, qui ne fait que rapporter : il n'écrit rien et ne dépense rien.

On compte les textes que l'app dit à voix haute en anglais, dédoublonnés, avec la **porteuse** des mots seuls (« Word: kitchen. », comptée dans le prix). Les traductions françaises restent à la voix du téléphone.

En modèle v2, **1 caractère = 1 crédit**.

| | textes | caractères = crédits, voix US | voix GB |
|---|---:|---:|---:|
| **A1 seul** | 4 711 | **89 919** | 89 986 |
| **A1-A2** | 10 180 | **207 016** | 207 104 |
| **A1-C1** | 25 332 | **574 743** | 574 837 |
| A1-C1, plus les exercices sans niveau (1 007) et les scènes (908) | 27 247 | **645 551** | 645 690 |

Détail par niveau (voix US) :

| | A1 | A2 | B1 | B2 | C1 |
|---|---:|---:|---:|---:|---:|
| textes | 4 711 | 5 469 | 7 529 | 3 574 | 4 049 |
| caractères | 89 919 | 117 097 | 171 639 | 90 740 | 105 348 |

- **Deux voix, deux fois le prix.** Les textes US et GB sont identiques à 96 % (26 341 en commun), mais chaque voix doit tout redire. Tout l'anglais en américain et en britannique coûte donc environ **1,29 million de crédits**.
- **En repère**, l'espagnol d'Espagne en demandait 520 302 avec une seule voix. Avec le plafond de 121 000 crédits par mois du forfait Creator noté dans `audio/manifest_es.py` :
  - l'A1 seul tient dans moins d'un mois ;
  - l'A1-A2 demande environ 1,7 mois par voix ;
  - tout l'anglais demande environ 5,3 mois par voix.
- **Marge** : compter 5 à 10 % de reprises (mots refusés par le découpage de la porteuse, prises à refaire).
- **Hors chiffrage** : la visite guidée, les épisodes et l'alphabet. L'alphabet est volontairement repoussé tant qu'il n'y a pas de voix.

## Avant toute génération

- **`audio/lectures/en.json`** : 144 textes américains contiennent des chiffres (« born in 1910 », « open until 6 pm »). Chacun doit avoir sa lecture en toutes lettres, écrite et relue à la main.
- Ajouter l'anglais à `audio/lectures.py` (`textes_en`) et au contrôle `verifier_lectures` du vérificateur.
- Un script `generer_en.py` sur le modèle de `audio/generer_es.py` : une voix par variante, les dossiers `audio/mp3/en-us/` et `audio/mp3/en-gb/`, la porteuse « Word: %s. », la normalisation, puis `audio/controler_sons.py`.
- Brancher l'app sur ces fichiers. Aujourd'hui, l'anglais passe toujours par la voix du téléphone.

## Choisir la voix : à l'aveugle, comme Aurora

Le comparatif est prêt mais n'est **pas produit**. Il coûterait environ 1 350 crédits en américain et 1 295 en britannique.

```
python anglais/outils/echantillons_voix.py --variante us              # le coût seul, sans rien produire
python anglais/outils/echantillons_voix.py --variante us --generer    # avec l'accord de Jacques
```

Le script passe par `audio/comparatif_voix.py`, tel quel :

- six textes de cours (un mot dans sa porteuse, un exemple, une question polie, une heure, un prix, une phrase longue) ;
- sonie égalisée, noms neutres VOIX-A, VOIX-B… ;
- une voix présentée deux fois, pour savoir si le verdict tient ;
- la clé rangée à part.

Les candidates sont des voix par défaut d'ElevenLabs, ouvertes à tout compte. Leurs identifiants ont été relevés sur les adresses d'écoute publiques et restent à confirmer dans l'interface, car la clé du projet ne sait pas lister les voix.

| américain (`audio/candidats_anglais_us.json`) | identifiant |
|---|---|
| Sarah, femme, jeune adulte, chaleureuse | `EXAVITQu4vr4xnSDxMaL` |
| Matilda, femme, alto professionnelle | `XrExE9yKIg1WjnnlVkGX` |
| Eric, homme, ténor posé | `cjVigY5qzO86Huf0OWal` |
| Brian, homme, voix grave de narration | `nPczCjzI2devNBz1zQrb` |

| britannique (`audio/candidats_anglais_gb.json`) | identifiant |
|---|---|
| Alice, femme, claire, faite pour l'e-learning | `Xb7hH8MSUJpSbSDYk0k2` |
| Lily, femme, veloutée, narration | `pFZP5JQG7iQjIQuC4Bku` |
| Daniel, homme, présentateur | `onwK4e9ZLuTAKqWW03F9` |
| George, homme, chaleureux | `JBFqnCBsd6RMkjVDRZzb` |

On peut ajouter à ces listes une voix de la Voice Library trouvée par Jacques, comme Aurora l'a été pour l'allemand.
