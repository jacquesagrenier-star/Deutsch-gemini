# Traduire le vocabulaire des Soins en espagnol : consignes

Pour qui remplit un lot `pflege/sources/vocabulaire/es/lot_NN.json` (personne ou modèle). Décision de Jacques du
16 nov. 2026 : tout le contenu des Soins traduit dans la langue de l'apprenant, l'espagnol compris.

## Ce qu'on remplit

Chaque entrée (`items`) donne l'allemand (`mot`, `de_ex`, et pour une paire `patient`, `de_ex_patient`), le
français (`fr`, `fr_ex`…), l'anglais et le portugais comme guides. On remplit **seulement** les champs vides :

| champ | ce que c'est |
|---|---|
| `es_trad` | la traduction du MOT (ou, pour `titre du thème`, le titre du thème) |
| `es_ex` | la traduction de la phrase d'exemple `de_ex` |
| `es_trad_patient` | paire : la traduction du côté du PATIENT, au registre de tous les jours |
| `es_ex_patient` | paire : la traduction de `de_ex_patient` |

Sans toucher aux autres clés, ni à l'ordre, ni aux `id`. Puis `python pflege/outils/vocab_es.py verifier lot_NN`.

## Comment traduire

- **Le public** : des soignantes et des soignants d'Amérique latine (Mexique, Colombie, Pérou…) qui apprennent
  l'allemand pour travailler en Allemagne. **Espagnol neutre d'Amérique latine** ; avec un patient, **usted**
  (« ¿Le duele? », « Siéntese, por favor ») ; entre collègues, **tú**, comme le « du » allemand (mais « ustedes »
  au pluriel, jamais « vosotros » ni le voseo) ; l'apprenant est tutoyé, sans genre supposé.
- **Traduire le sens de l'allemand**, le français guidant. L'exemple traduit doit être naturel dans la bouche d'un
  soignant hispanophone.
- **Le terme du métier**, celui d'une formation d'enfermería en Amérique latine, jamais du mot à mot :
  *Dekubitus* = la úlcera por presión, *Übergabe* = la entrega de turno, *Visite* = la visita médica / el pase de
  visita, *Sturz* = la caída, *Pflegekraft* = el personal de enfermería, *bei Bedarf* = si es necesario, *Akte* /
  *Kurve* = el expediente, *Station* = el área (le service), *Stationsleitung* = la jefa de enfermería,
  *diensthabender Arzt* = el médico de guardia, *nüchtern* = en ayunas, *Blutzucker* = la glucosa (glucemia
  capilar)… Les mêmes termes que les dialogues des Soins (pflege/sources/traductions/es/), pour qu'un mot ne change
  pas d'une partie de l'app à l'autre. Quand l'Espagne et
  l'Amérique latine diffèrent, prendre l'Amérique latine (« el celular », « la computadora », « manejar »).
- **Les noms** : avec leur article (« la úlcera por presión », « el pañal »), comme le français.
- **Les termes propres au système allemand** (Pflegegrad, Vorsorgevollmacht, Medizinischer Dienst,
  Anerkennungsverfahren…) : le plus proche équivalent compréhensible, suivi d'une courte explication entre
  parenthèses, comme les autres langues (« el grado de dependencia (Pflegegrad, de uno a cinco) »).
- **Les paires** (`sorte` = `paire`) : `es_trad_patient` dans le registre de tous les jours (« el dolor de
  barriga »), `es_trad` dans le registre médical (« el dolor abdominal ») ; si l'espagnol n'a qu'un mot pour les
  deux, le garder et préciser entre parenthèses.
- **Les abréviations** (`mot` = « RR (= Blutdruck) ») : le sens, avec l'abréviation hispanophone du métier si elle
  existe (« la presión arterial (PA, TA) »).
- **Les noms de personnes** restent des gabarits entre accolades, exactement ceux de l'allemand : `{Herr Brandt}`,
  `{Frau Hoffmann}`, `{Elif}`… Jamais écrits en toutes lettres. Ils deviennent « el Sr. Brandt », « la Sra. Hoffmann »,
  « la Dra. Sommer » à la construction (la forme des dialogues) : la phrase doit donc accepter « el Sr. Brandt » à
  leur place (pas de « el {Herr Brandt} »). En tête de phrase, la majuscule est mise automatiquement.
- **Ponctuation espagnole** : « ¿ … ? », « ¡ … ! », guillemets « » ou “ ”.
- **Interdits** (refusés par l'importation) : le guillemet droit `"`, l'antislash, la barre `|`, un saut de ligne.
- **Aucun chiffre** dans une phrase d'exemple : les nombres en lettres, comme dans l'allemand.
- Les mots allemands cités dans une phrase (« Wir sagen „Vorlage“ ») restent en allemand.

## Ensuite

`python pflege/outils/vocab_es.py importer` recopie les champs remplis dans les sources (fin de chaque champ,
« | » puis l'espagnol), puis `python pflege/outils/construire.py`, `python tests/pflege.py` et
`python tests/pflege_vocabulaire.py`.

Avant l'importation, **un second avis** (méthode de la v1208) : le contraste mécanique
(`vocab_es.py verifier`), puis un autre modèle qui relit l'allemand, le français et l'espagnol et ne propose que ce
qui est sûr ; on n'applique que le sûr, le doute va à la relecture native.
