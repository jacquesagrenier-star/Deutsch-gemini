# Traduire les textes Soins : consignes

Pour qui traduit un fichier de `pflege/sources/traductions/<langue>/` (personne ou modèle).

## Ce qu'on remplit

Chaque fichier a la forme `{"cles": {"<chemin>": {"de": "<allemand>", "fr": "<français>", "<langue>": ""}}}`.
On remplit **seulement** la valeur `"<langue>"`, sans toucher aux autres clés ni aux chemins. Une entrée marquée
`"perime": true` a une traduction ancienne dont le français a changé : on la refait, puis on retire `"perime"`.

`noms.json` : les noms des personnages dans la langue. `""` = forme courante, `voc` = pour s'adresser à la
personne. Les langues à déclinaison (uk, ru, pl) **ajoutent les cas qu'elles emploient** (`gen`, `dat`, `acc`,
`ins`, `loc`) et peuvent en ajouter d'autres ; une forme employée dans une traduction (`{brandt:gen}`) doit exister
ici, le contrôle le vérifie. Écriture : les noms se translittèrent dans l'alphabet de la langue (uk, ru :
cyrillique ; ar, fa : écriture arabe), comme dans un roman traduit. Titres : « Herr / Frau » deviennent le titre
courant de la langue (M. / Mme, Mr / Mrs, Bay / Bayan, пан / пані, господин / госпожа, pan / pani, السيد / السيدة,
آقای / خانم, Sr. / Sra.). « Dr. Sommer » est une femme, « Dr. Neumann » un homme.

## Comment traduire

- **Traduire le sens de l'allemand**, le français servant de guide. Ce sont des aides pour un soignant qui apprend
  l'allemand : la traduction doit être naturelle dans sa langue, dans le registre de la scène (poli avec un
  patient : vous / Sie / siz / ви / вы / pan / o senhor ; entre collègues au « du » : tutoiement).
- **Les termes de soins sont ceux du métier dans la langue** (ce que le soignant a appris en formation), pas du mot
  à mot : *Pflegekraft* = le soignant du patient, *Kurve* = le dossier de soins, *bei Bedarf* = si besoin
  (prescription), *Visite* = la visite médicale, *Übergabe* = la relève / transmission, *Sturz* = chute,
  *Dekubitus* = escarre…
- **Une faute** (`faux` dans la source, le français dit souvent « (mal dit) » ou met la tournure fautive entre
  guillemets) : faire sentir l'erreur dans la traduction aussi, ou garder « (mal dit) » traduit.
- **Les aides** (`aide`) expliquent l'allemand : garder les mots allemands cités tels quels, entre les guillemets
  de la langue ; garder **exactement les mêmes balises `<b>…</b>`** que le français.
- **Les noms** restent des gabarits : `{elif}`, `{brandt}`, `{brandt:voc}`, `{sommer}`… On ne les écrit jamais en
  toutes lettres ; on garde **les mêmes noms** que le français (le contrôle compare). On peut changer la forme
  (`{brandt}` → `{brandt:voc}` pour s'adresser à lui, `{brandt:gen}` en russe) si elle est dans `noms.json`.
- **Turc** : jamais de suffixe collé après un gabarit (`{brandt}'ın`, `{elif}'e`) : il casserait si le nom change
  (harmonie vocalique). On met la forme fléchie dans `noms.json` (`gen` « Bay Brandt'ın », `dat` « Elif'e »,
  `acc`, `loc`, `abl`, `ins` « Elif'le »…) et on écrit `{brandt:gen}`. Le contrôle refuse `}'` en turc.
- Le français écrit parfois des formes propres au français (`{sommer:a}` = « à la docteure Sommer ») : dans les
  autres langues, prendre `{sommer}` ou la forme casuelle qui convient.
- Chiffres : on les garde en chiffres dans les traductions (elles ne sont pas lues à voix haute).
- Persan et arabe : pas de caractères de direction invisibles ; les mots allemands cités restent en lettres latines.
- Portugais : celui du **Brésil** (você / o senhor, a senhora).

## Ensuite

`python pflege/outils/textes.py construire` puis `python tests/pflege_dialogues.py` (ou `--partiel` tant que
toutes les langues ne sont pas faites). Le contrôle refuse : une traduction vide ou périmée, des `<b>` en nombre
différent, un nom absent ou en trop, une forme de nom inconnue.
