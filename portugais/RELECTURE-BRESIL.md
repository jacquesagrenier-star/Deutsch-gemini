# Relire la variante du Brésil : la liste courte

Pour l'ancien étudiant brésilien de Jacques (décision du 30 oct. 2026). Tout
le portugais du Brésil de Wortando est **dérivé** du portugais du Portugal par
un programme (`portugais/outils/bresil.py`), puis complété à la main
(`portugais/outils/bresil_textes.py`). Ce qu'un Brésilien voit tout de suite et
qu'un programme ne voit pas, c'est ce qui compte ici.

**Où regarder** : dans l'app (compte admin), Réglages → Administration →
« PORTUGUÊS — ESSAI PORTUGAIS », puis Réglages → « Quel portugais ? » →
**Brésil**. Le même mot, la même carte, la même progression : seule la langue
change.

## Les dix points à juger

1. **Le pronom devant le verbe.** Le programme écrit « Me chamo Ana », « Eu me
   levanto às sete », « Se diz que vai chover », « Vou te ligar ». Est-ce
   naturel, ou trop familier pour un cours ? Faut-il écrire « Eu me chamo »
   plutôt que « Me chamo » en tête de phrase ?
2. **Tu ou você.** Les conjugaisons gardent les six personnes (eu, tu, ele/você,
   nós, eles/vocês ; vós caché), et beaucoup de phrases tutoient encore avec la
   forme du Portugal (« Moras aqui? », « Gostaste do filme? »). Faut-il tout
   passer à « você » + 3e personne ?
3. **L'article devant le possessif.** Il tombe seulement en tête de phrase
   (« Minha mãe mora no Rio ») ; ailleurs il reste (« com a minha mãe »). Juste ?
4. **Le gérondif.** « Estou lendo », « Ando estudando », « Continua chovendo »
   partout à la place de « estar a + infinitif ».
5. **Les mots changés** : 86 cartes de noms (trem, ônibus, café da manhã,
   banheiro, celular, geladeira, suco, xícara, cardápio, ponto, faixa de
   pedestres, abobrinha, grama, tela, sorvete…). La table complète est en tête
   de `bresil.py` (« NOMS »). Un mot qui sonne portugais du Portugal ?
6. **Les phrases où un nom a changé de genre** (a paragem → o ponto, o ecrã → a
   tela) : 60 phrases, listées à la fin de `portugais/outils/rapport_bresil.txt`.
   L'article suit ; l'adjectif d'après, non : à vérifier.
7. **Les 15 fiches de grammaire récrites** pour le Brésil (le pronom, estar +
   gérondif, tu / você / o senhor, les faux amis, la mésoclise, « Brésil ou
   Portugal ? »…), et les 4 séries d'exercices écrites pour elles.
8. **La prononciation** : 11 règles récrites (te / de en « tchi / dji », l final
   en « ou », r initial soufflé, voyelles pleines) et la prononciation figurée
   des nombres (« SÉ-tchi », « DÉÏS »). Pour l'accent de São Paulo : bon ?
9. **Les scènes** : les mots des zones (o trem, o bonde, a sacola, o abajur…).
10. **Ce qui reste du Portugal exprès** : l'action se passe encore à Lisbonne,
    avec des euros (la ville du Brésil est une question pour Jacques).

## Ce que la variante laisse de côté, et pourquoi

- **145 questions d'exercice** ne passent pas au Brésil : elles enseignent un
  usage du Portugal (« Au Portugal : … »), ou la conversion change la phrase
  là où se trouve le trou (« Estou ___ ler »). La liste est dans
  `rapport_bresil.txt`.
- **La voix** est celle du téléphone, en pt-BR (Luciana, Felipe, Francisca…).
  Aucune voix enregistrée.

## Comment corriger

Une correction de mot ou de règle va dans `bresil.py` (tables NOMS, MOTS,
VERBES) ; une explication, une fiche ou une série dans `bresil_textes.py`.
Puis `python portugais/outils/construire.py` refait `portugais/datos-br/`.
Jamais à la main dans `datos-br/` : le fichier serait écrasé au prochain passage.
