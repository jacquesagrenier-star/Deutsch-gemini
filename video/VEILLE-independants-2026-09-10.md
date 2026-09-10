# Veille — les sources qui n'ont rien à vendre
### 10 septembre 2026

La veille du 9 septembre disait elle-même où était sa faiblesse : *« tout ce
qui est cité ici vient de blogs — dont plusieurs appartiennent à des éditeurs
d'outils concurrents »*. Demande de Jacques : chercher des blogues indépendants
de ceux qui font la promotion d'un outil, et des articles de spécialistes.

Ce document ne rassemble que des sources **qui ne vendent pas d'outil de
génération vidéo** : un organisme de normalisation, la recherche universitaire
en traduction audiovisuelle, la littérature d'évaluation en vision par
ordinateur, et le journal d'un syndicat de monteurs.

**Ce qui en sort de plus utile n'est pas une liste d'outils : ce sont trois
chiffres et une liste de phonèmes.** Nous n'avions ni l'un ni l'autre.

---

## 1. Enfin des seuils : la recommandation UIT-R BT.1359-1

L'Union internationale des télécommunications est l'organisme de normalisation
des télécoms. Elle n'a rien à vendre, et elle a mesuré exactement notre
question sur des sujets parlants — des présentateurs de journal télévisé,
c'est-à-dire nos plans.

| | son en AVANCE sur l'image | son en RETARD sur l'image |
|---|---|---|
| **seuil de détection** | +45 ms | −125 ms |
| **seuil d'acceptabilité** | +90 ms | −185 ms |

> « The visual cues of lip movement are easy to match with speech and hence
> lip-sync error detection has very low thresholds of +45 ms to −125 ms. »

### Ce que ça nous dit, et qu'on ne pouvait pas deviner

**a) Notre décalage mesuré est hors norme d'un facteur 3 à 8.** Le 9 septembre,
on a relevé sur Seedance un « décalage d'attaque de +0,35 s très régulier ».
C'est **350 ms** : près de huit fois le seuil de détection dans un sens, encore
deux fois le seuil d'*acceptabilité* dans l'autre. Ce n'était pas une question
d'appréciation — c'était mesurablement raté, et on n'avait aucun barème pour le
dire.

**b) La tolérance n'est pas symétrique, et c'est la règle de montage la plus
directement applicable.** L'oreille pardonne **presque trois fois plus** un son
en retard qu'un son en avance : 125 ms contre 45 ms. Autrement dit, **dans le
doute, la voix doit arriver un peu TARD, jamais tôt.**

⚠️ **À vérifier dans nos fichiers, et c'est une vraie question ouverte :** le
signe de notre « +0,35 s ». On a noté l'amplitude sans jamais noter la
direction, parce qu'on n'avait pas de raison de croire qu'elle changeait
quelque chose. Elle change tout : le même écart est trois fois plus grave d'un
côté que de l'autre. La mesure est à refaire, une fois, en notant le sens.

**c) On a enfin un critère de réussite.** Après conformation, le résidu doit
tomber dans +45 / −125 ms. Ce n'est plus « ça a l'air bon » : c'est un test qui
passe ou qui échoue.

---

## 2. La recherche en doublage : trois synchronies, pas une

C'est la découverte qui reconfigure le problème. La traduction audiovisuelle
est un champ universitaire, et il distingue depuis longtemps trois choses que
nous confondions sous le mot « lip-sync » :

- **L'isochronie** — la durée des répliques et des silences correspond.
- **La synchronie cinétique** — les gestes ne contredisent pas les mots.
- **La synchronie labiale** — les lèvres correspondent aux sons.

Et voici le classement, qui n'est pas celui qu'on croyait :

> « **Isochrony, the lack of which is the foremost noticeable indicator of a
> poorly dubbed product**, addresses the matching of the time between the ST
> and TT speech phrases and pauses. »

**La durée passe avant la bouche.** Le défaut le plus visible d'un doublage
raté n'est pas une lèvre mal formée : c'est une réplique qui ne dure pas ce
qu'elle devrait. Or c'est précisément ce que `conformer.py` corrige déjà — et
c'était rangé chez nous comme un pis-aller, en attendant de « vraiment » régler
la bouche. C'est l'inverse : c'est le levier principal.

### Et la synchronie labiale ne porte que sur une petite liste

> « In dubbing, particularly in the case of close-ups, the [...] dialogue must
> coincide with the screen actor's lip movements — **especially in the case of
> bilabial consonants, labio-dental consonants and open vowels.** »
>
> « Research into lip synchrony focuses on **rounded and protruded vowels**
> since lip rounding is a visibly marked feature, **which cannot be neglected
> especially in close-ups.** »

Traduit pour nos plans allemands, il y a **quatre familles à vérifier**, et
tout le reste est invisible :

| famille | en allemand | pourquoi ça se voit |
|---|---|---|
| bilabiales | **p, b, m** | les lèvres se ferment complètement |
| labio-dentales | **f, v, w** | la lèvre inférieure touche les dents |
| voyelles ouvertes | **a, ä** | la mâchoire descend |
| voyelles arrondies/projetées | **u, o, ü, ö** | les lèvres s'avancent |

**Ce que ça change concrètement :** on ne juge plus « la réplique est-elle
synchrone », question à laquelle on répondait à l'œil et en se contredisant.
On repère les p/b/m/f/w et les ü/ö/u de la ligne, et on ne vérifie qu'eux.
C'est un contrôle fini, reproductible, et qui tient en quelques images.

**Et une mauvaise nouvelle honnête pour l'allemand.** La recherche désigne les
voyelles arrondies et projetées comme le trait le plus visible en gros plan.
L'allemand en est chargé — *ü, ö, u* sont partout, et ce sont les sons que
l'anglais ne fournit presque pas aux modèles à l'entraînement. Le blog qui
affirmait le 9 septembre que « German syncs with a steady beat » ne se trompe
peut-être pas sur le rythme, mais il ne dit rien du seul trait qui compte en
gros plan — et sur celui-là, l'allemand est *plus* exposé que l'anglais, pas
moins.

---

## 3. La métrique que le domaine utilise vraiment : SyncNet

Toute la littérature d'évaluation des « têtes parlantes » se juge sur deux
nombres tirés d'un même réseau, SyncNet :

- **LSE-D** (*Lip-Sync Error – Distance*) : la distance entre la bouche
  produite et l'audio. Plus bas, mieux c'est.
- **LSE-C** (*Lip-Sync Error – Confidence*) : la confiance de l'appariement.
  Plus haut, mieux c'est.

L'échelle est publiée : **LSE-D de 6 à 8 correspond à l'état de l'art** dans
les grandes évaluations. C'est un barème, pas une impression.

**Pourquoi ça nous concerne directement.** Le 9 septembre, un commit portait ce
titre : *« Quatrième fois que cette mesure se trompe, et c'est écrit dans le
fichier »*. Notre mesure maison (un écart en dB) s'est trompée quatre fois, et
une mesure non étalonnée n'arbitre rien — elle a déjà préféré une prise
rejetée à l'œil. SyncNet est gratuit, tourne en local, et **son échelle est
étalonnée par des milliers de comparaisons publiées.** C'est le remplacement
évident.

⚠️ **Sa limite, dite par la littérature elle-même :** SyncNet n'est pas
invariant à la translation — un visage décalé dans le cadre change le score.
**Donc il compare deux prises du MÊME plan, jamais deux cadrages différents.**
Pour nous c'est exactement l'usage voulu (choisir entre des prises), mais ça
interdit de s'en servir pour classer les plans entre eux.

---

## 4. Le journal des monteurs : ce que la profession fait, sans rien vendre

*CineMontage* est le journal du syndicat des monteurs de cinéma américains
(Motion Picture Editors Guild). Ses auteurs sont des monteurs ; il ne vend pas
de logiciel.

**Sur l'outillage de conformation.** La profession a des outils dédiés
(Matchbox, ReConform de Nuendo, mfChangeNote) qui comparent deux versions et
produisent un rapport des différences. Et un mixeur y met en garde contre la
conformation automatique lancée sans relecture, en une phrase qu'on ferait bien
de garder : *« You've been warned; now, here's your magic wand, Harry. »*

**Sur le doublage par IA, l'usage réel est le nôtre.** D'après l'article,
Amazon s'y intéresse pour les **territoires où le doublage traditionnel n'est
pas rentable** — c'est-à-dire exactement notre économie : un contenu qui ne
justifie pas un studio, mais qui doit exister dans la langue.

**Sur la voix, une confirmation qui vient d'un praticien, pas d'un éditeur.**
Un monteur son y qualifie Respeecher et **ElevenLabs** de *« gold standard for
synthetic dialogue »*. Notre choix de voix n'est donc pas un pari.

**Et un signal sur ce qui ne disparaît pas.** Le syndicat étudie la création
d'une classification *« Vubbing Editor »* sous la catégorie Monteur son. La
profession qui adopte ces outils est en train d'écrire une fiche de poste pour
la passe humaine — pas de la supprimer.

---

## 5. Ce que je referais, à la lumière de ces sources seules

1. **Refaire la mesure de décalage en notant le SIGNE**, une fois, sur les
   prises acquises. C'est cinq minutes et ça décide d'une règle de montage.
2. **Adopter +45 / −125 ms comme critère de réussite** de `conformer.py`, à la
   place du jugement à l'œil. Et **laisser la voix arriver plutôt tard.**
3. **Vérifier la bouche uniquement sur p/b/m, f/v/w, a/ä et u/o/ü/ö.** Le reste
   n'est pas visible, et le vérifier nous a coûté des journées.
4. **Remplacer notre mesure en dB par SyncNet (LSE-D/LSE-C)**, avec sa règle
   d'emploi : comparer des prises du même plan, jamais des cadrages différents.
5. **Traiter l'isochronie comme le levier principal, pas comme un pis-aller.**
   `conformer.py` corrige ce que la recherche désigne comme le défaut le plus
   visible d'un doublage raté.

---

## 6. Ce que ces sources ne donnent pas

- **Rien sur l'allemand mesuré.** Aucune de ces sources ne teste l'allemand.
  Ce qu'on en déduit ici (les voyelles arrondies exposent l'allemand en gros
  plan) est un **raisonnement à partir de la phonétique**, pas une mesure.
- **Rien sur le seuil d'audibilité d'un étirement.** La recherche sur la parole
  étirée porte sur l'**intelligibilité** — on comprend encore — pas sur le
  moment où l'oreille entend que c'est étiré. Notre +25,7 % du plan 11 reste
  donc jugé par une seule oreille, la nôtre, et ce jugement (« ça détonne à
  côté des plans non étirés ») demeure la meilleure information disponible.
- **Rien de numérique chez les monteurs.** Les articles d'ADR de *CineMontage*
  sont des récits de métier, pas des fiches techniques : belle matière, aucun
  chiffre. Les chiffres, dans cette veille, viennent tous de l'UIT et de la
  recherche universitaire.

---

*Sources : Recommandation UIT-R BT.1359-1 (Union internationale des
télécommunications) ; recherche en traduction audiovisuelle sur la synchronie
en doublage (Chaume, Fodor ; travaux sur la synchronie labiale des voyelles
arrondies) ; littérature d'évaluation LSE-D / LSE-C issue de SyncNet ;
CineMontage, journal de la Motion Picture Editors Guild ; TV Tech.*
