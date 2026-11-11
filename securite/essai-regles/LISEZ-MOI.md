# Banc d'essai des règles Firestore

146 cas joués avec le SDK de l'app dans l'**émulateur local** (projet fictif
`demo-wortando` : rien ne part vers le vrai Firebase, rien ne coûte).
Il faut Java et la Firebase CLI, tous deux installés sur le PC.

```bash
cd securite/essai-regles
npm install
firebase emulators:exec --only firestore --project demo-wortando "node essai.js"
```

Sortie attendue : `146 ok, 0 echec(s)`. Pour éprouver un autre fichier de
règles (par exemple celles en ligne, pour comparer) :
`REGLES=../../firestore.rules firebase emulators:exec ...` (le 11 nov. 2026,
celles en ligne laissaient passer 53 attaques).

À relancer **à chaque changement des règles** et chaque fois que l'app écrit
un champ nouveau dans un résumé (il faut alors l'ajouter à `champsResume()`
dans les règles ET un cas ici).
