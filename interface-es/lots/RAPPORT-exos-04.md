# Rapport — exos-04 (15 nov. 2026)

## Chiffres

- Source : `interface-es/sources/exos-04.json`, 140 exercices. Rendu : `interface-es/lots/exos-04.es.json`, 140 exercices.
  - `kasusReconnaissanceExercises#15` à `#49` (35) : `question`, `translation`, `hint`, `explanation`.
  - `relativReconNomAkk#0` à `#51` (52) : `translation`, `hint`, `explanation`.
  - `relativReconDativ#0` à `#49` (50) : `translation`, `hint`, `explanation`.
  - `relativReconMixed#0` à `#2` (3) : `translation`, `hint`, `explanation`.
- Contrôle `exos.py controle` : **140 exercices, 0 faute, 0 avis**.
- Les 140 traductions sont écrites à la main, d'après la phrase allemande (Perfekt → pretérito). Les consignes, indices et explications, qui suivent sept gabarits dans la source, sont rendus gabarit par gabarit, formes allemandes recopiées de la source ; la consigne et l'indice des cas reprennent mot pour mot ceux d'exos-03 (« ¿En qué caso está «…»? », le test lo / le).
- Le « -- » de la source devient « — » dans les indices et les explications des relatives.

## Explications réécrites contre l'espagnol

- `kasusReconnaissanceExercises#15` à `#49`, l'**indice** : celui d'exos-03 (les questions « ¿qué? / ¿a quién? (lo, la) — ¿a quién le…? (le) »), parce que « à qui ? » ne sépare pas l'Akkusativ du Dativ en espagnol (« veo a Juan »).
- `kasusReconnaissanceExercises#17`, `#23` : objet direct de personne, que l'espagnol introduit par « a » (« Visitamos a nuestros abuelos », « Llamo a mi amigo ») ; l'explication ajoute « (en español: «los visitamos») », « «lo llamo» ».
- `kasusReconnaissanceExercises#26`, `#29`, `#30`, `#31`, `#35`, `#36` : « répond à à qui ? » devient « responde a «¿a quién le doy?» — es el objeto indirecto (en español: «le doy») ».
- `kasusReconnaissanceExercises#27` (helfen), `#32` (folgen), `#34` (vertrauen) : le vrai piège pour un hispanophone, que la source ne dit pas — l'espagnol y met un objet direct ou « en » : « aunque en español se diga «la ayuda» / «lo seguimos» / «confiar en» ».
- `kasusReconnaissanceExercises#28` (danken), `#33` (gefallen), `#37` (antworten) : là l'espagnol aide — « como en «le damos las gracias» / «le gusta» / «le responde» ».
- `kasusReconnaissanceExercises#38` à `#48` : la possession avec les mots espagnols (« el carro DE mi hermano », « el color DEL cielo »).
- `relativReconDativ#0`, `#7`, `#11`, `#14`, `#20`, `#22`, `#43` (helfen), `#1`, `#8`, `#13`, `#17`, `#23`, `#26`, `#38`, `#39`, `#46`, `#48` (vertrauen), `#2`, `#21`, `#24`, `#40`, `#42` (gratulieren), `#4`, `#15` (begegnen), `#6`, `#19`, `#37`, `#44` (zuhören) — 28 explications : ajout de « y «helfen» pide Dativ », parce que la traduction espagnole (« al que ayudé », « en quien confío », « al que felicité », « con el que me encuentro », « al que escuché ») ne laisse pas deviner un datif. Les relatives au pluriel de ces mêmes verbes (`#28` à `#34`, `#41`, `#47`) gardent l'explication « denen (no «den») » de la source, sans cet ajout.

## Doutes (9)

1. L'ajout « y «…» pide Dativ » sur 28 explications de `relativReconDativ` : plus long que la source ; à retirer si on veut l'explication nue.
2. Les explications des relatives disent « «Der Film» es masculino », « «Das Auto» es neutro » alors que la traduction dit « la película », « el carro » : le genre est celui du mot allemand cité, sans « en alemán ». Concerne surtout `relativReconNomAkk#22`, `#27`, `#31`, `#35`, `#36`, `#38`, `#14` (das Mädchen), `relativReconDativ#18`, `#23`, `relativReconMixed#0`.
3. *Lehrer / Lehrerin* → « profesor / profesora » partout (`kasus#28`, `NomAkk#1`, `#25`, `Dativ#16`, `#33`) : rien ne dit primaire ou lycée.
4. *Junge* → « niño » (`NomAkk#2`, `Dativ#6`) ; *Mädchen* → « niña » (`NomAkk#14`, assise à la fenêtre) mais « muchacha » (`Dativ#23`, « ma meilleure amie »).
5. `relativReconNomAkk#31`, `relativReconDativ#13` : « im dritten Stock » → « en el tercer piso » ; l'étage allemand ne compte pas le rez-de-chaussée, ce serait le « cuarto piso » de bien des pays d'Amérique.
6. `relativReconDativ#18` : *die Katze* → « el gato » (générique), alors que l'explication dit « femenino ».
7. `relativReconDativ#38` / `#39` : *das Unternehmen* → « la empresa », *die Firma* → « la compañía », pour ne pas rendre deux fois le même mot.
8. `relativReconDativ#44` : « erzählte spannende Reisen » rendu mot à mot (« contó viajes apasionantes ») ; l'allemand lui-même est inhabituel (on raconte *von Reisen*).
9. `relativReconNomAkk#15` : « feiert lange » → « celebra por mucho tiempo ».

## À trancher (mots où l'Amérique latine hésite)

- `relativReconNomAkk#6`, `relativReconMixed#1` : *Kellner* → « mesero » (Mexique, Colombie ; le Cône Sud dit « mozo », « camarero » est d'Espagne).
- `kasus#44`, `relativReconNomAkk#23`, `#51` : *Kuchen* et *Torte* → « pastel » (Mexique ; la Colombie dit « torta » ou « ponqué » ; « torta » est un sandwich au Mexique).
- `relativReconNomAkk#24` : *Pullover* → « suéter » (ou « saco », « buzo », « chompa » selon le pays).
- `relativReconNomAkk#29` : *Jacke* → « chaqueta » (Mexique : « chamarra »).
- `relativReconNomAkk#31` : *mieten* → « rentar » (consignes ; la Colombie dit « arrendar », le Cône Sud « alquilar »).

## Sources fautives ou bancales

- `relativReconDativ#44` : « Die Gästin » est un mot rare et discuté (le Duden l'admet, l'usage dit « der Gast » pour une femme aussi), et « spannende Reisen erzählen » n'est pas idiomatique. À faire relire par la germanophone.
- `relativReconNomAkk#15` : le français « L'équipe qui gagne aujourd'hui fête longtemps » est bancal, l'allemand se tient.
- `relativReconDativ#10` : le français dit « m'a remercié », l'allemand « hat sich bedankt » sans « bei mir » ; l'espagnol suit l'allemand (« dio las gracias »).
- `relativReconDativ#19` : « hatte einen schlechten Tag » (Präteritum) rendu en français par « a eu » ; sans conséquence, « tuvo un mal día ».
- `relativReconDativ#30` : « freuen sich sehr » (présent) ; le français « sont très contents » convient, l'espagnol dit « se alegran mucho ».
- Aucune traduction française ne contredit l'allemand sur le sens.
