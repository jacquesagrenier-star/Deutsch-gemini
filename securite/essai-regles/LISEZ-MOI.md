# Banc d'essai des règles Firestore

247 cas joués avec le SDK de l'app dans l'**émulateur local** (projet fictif
`demo-wortando` : rien ne part vers le vrai Firebase, rien ne coûte).
Il faut Java et la Firebase CLI, tous deux installés sur le PC.

```bash
cd securite/essai-regles
npm install
firebase emulators:exec --only firestore --project demo-wortando "node essai.js"
```

Sortie attendue : `247 ok, 0 echec(s)`. Pour éprouver un autre fichier de
règles (par exemple celles en ligne, pour comparer) :
`REGLES=../../firestore.rules ADMIN_EMAIL=<adresse de l admin> firebase emulators:exec ...` (le 11 nov. 2026,
celles en ligne donnaient 114 cas sur 241 autrement (le 12 nov.) ; `ADMIN_EMAIL` parce qu elles reconnaissent l admin a son adresse).

À relancer **à chaque changement des règles** et chaque fois que l'app écrit
un champ nouveau dans un résumé (il faut alors l'ajouter à `champsResume()`
dans les règles ET un cas ici).
