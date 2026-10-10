# L'espagnol dans le même moteur que l'allemand

Décidé par Jacques le 10 octobre 2026 : « mettre l'espagnol solide, dans un seul
moteur avec l'allemand. S'il y a un risque de cassure, on est mieux de le régler
tout de suite. »

## D'où on part

- L'app espagnole (`espanol/`) est **générée** depuis l'app allemande par
  `fork.py` (dépôt `wortando-espanol`) : plus de cent remplacements de texte,
  et environ 20 000 lignes de Python autour (conversion des données,
  conjugaison, grammaire). Elle n'a ni compte, ni sauvegarde dans le cloud,
  et sa porte se passe par des codes à part.
- L'app allemande a **déjà** la base d'un moteur à plusieurs langues
  (« restructuration multilingue », septembre 2026) : la table
  `LANGUE_ENSEIGNEE`, `urlDonnees()`, les exercices et la grammaire sortis en
  données, et la progression rangée par langue apprise (v394 ; l'allemand
  sans préfixe, **volontairement**, pour ne rien faire perdre aux testeurs).
- Les données espagnoles sont **déjà** au format allemand
  (`contenido/a_formato_aleman.py`).

## La règle qui protège l'allemand

**À chaque étape, l'app allemande doit rester identique pour ses testeurs.** On
ne le vérifie pas à l'œil : un parcours automatique (navigateur sans tête,
Playwright) ouvre chaque tuile et chaque option du panneau, et relève le texte
visible et les erreurs de la console. On le fait tourner une fois **avant**
de toucher quoi que ce soit (la référence), puis après chaque étape : une
seule différence en allemand arrête l'étape.

Le même parcours sur l'app espagnole actuelle donne la référence espagnole :
le moteur, réglé sur l'espagnol, doit s'en approcher étape après étape,
jusqu'à pouvoir la remplacer.

Tant que le moteur n'a pas rattrapé la référence espagnole, **`espanol/` reste
servi tel quel** : les testeurs d'espagnol ne voient rien bouger.

## Les étapes

0. **Le filet.** Le parcours automatique et les deux références (allemand en
   v727, espagnol en v39). Rien n'est encore touché dans l'app.
   ✅ **Fait le 10 oct. 2026** : `fusion-espagnol/parcours.py`, références dans
   `fusion-espagnol/references/`. Allemand : 104 chemins, 0 erreur ;
   espagnol : 51 chemins (le fork cache la moitié des tuiles), 21 fichiers
   absents tolérés (`synonymes.json`, `grammaire.json`, `frequence.json`
   demandés dans `espanol/datos/`), invisibles à l'écran. Étalonné : deux
   passages sur la même version → 0 écart (heure et hasard figés) ; un seul
   « ? » ajouté dans un libellé → 1 écart, au bon chemin.
   Après chaque étape :
   `python fusion-espagnol/parcours.py --app de --sortie releve.json` puis
   `python fusion-espagnol/parcours.py --comparer fusion-espagnol/references/de-v729.json releve.json`
   → **0 écart exigé**. Le parcours prend environ six minutes.
   Relevé en passant dans l'espagnol actuel : une explication dit « c'est ici
   que **l'anglais** n'aide pas » même en interface française (écrite pour
   des anglophones), et une option du panneau des adverbes n'a pas de titre — ⚠️ corrigé à l'étape 4 : ce n'est pas un défaut, c'est une option CACHÉE (le parcours ouvre aussi les options cachées, d'où un nom vide).
1. **Choisir la langue apprise au démarrage.** Une table de langues `{de, es}`
   au lieu d'une seule `LANGUE_ENSEIGNEE` ; la langue vient de l'adresse
   (`?apprendre=es`), puis du réglage. Données espagnoles lues dans
   `espanol/datos/`. Stockage local sous le préfixe `wortandoEs_` (celui du
   fork : la progression des testeurs d'espagnol actuels est conservée).
   ✅ **Fait en v728 (10 oct. 2026)** : `LANGUE_ALLEMAND` / `LANGUE_ESPAGNOL`,
   `LANGUE_APPRISE` lue dans `?apprendre=es` seulement (pas encore de
   réglage : personne n'y arrive par hasard), `PREFIXE_STOCKAGE` sur les 50
   clés (sauf le journal de gel, écrit par le `<head>`), `urlDonnees()` avec
   table de renvoi et sans repli sur l'allemand, et **aucun nuage en
   espagnol** (`syncProgressToCloud` et `restoreProgressFromCloud` sortent
   tout de suite) jusqu'à l'étape 6. Allemand : 0 écart sur 104 chemins.
   Moteur en espagnol : 104 chemins, aucune exception, les données
   espagnoles chargées (130 thèmes) ; 44 fichiers allemands absents
   demandés (grammaire, synonymes, examen, fréquence) — l'objet des
   étapes 2 à 5. Le réglage Espagne / Amérique latine passe à l'étape 2,
   avec les mots qui changent.
   ⚠️ Appris en route : le remplacement global des clés a aussi touché la
   ligne qui DÉFINIT le préfixe (erreur d'initialisation au chargement).
   Les deux vérificateurs disaient « aucun problème » ; c'est le parcours
   qui l'a vue. Ne jamais publier une étape sans lui.
   Défaut existant noté pour l'étape 2 : les noms de thèmes espagnols
   s'affichent en anglais sous une interface française (déjà dans le fork).

2. **Les libellés.** Les remplacements de texte du fork deviennent une couche
   de traductions par langue apprise, en données, par-dessus l'interface.
   ✅ **Fait en v729 (10 oct. 2026)**. Mesuré d'abord, pas recopié : l'app
   espagnole v39 a été générée sur l'allemand **v722** ; leurs dictionnaires
   comparés clé par clé donnent **77 clés par langue** (60 modifiées,
   17 ajoutées), 9 Ko. Versées par-dessus `I18N` en mode espagnol seulement
   (`I18N_ESPAGNOL`), avant tout affichage : pas de clignotement « Apprends
   l'allemand ». Les 14 clés `_xxx_` (anciens libellés allemands gardés par la
   grammaire du fork) attendent l'étape 4. La version **française** du fork
   était à moitié anglaise (« Subjunctive », « Two pasts », « Direction: EN →
   ES ») : remise en français. En espagnol, l'interface ne propose que le
   français et l'anglais (`UI_LANGS`), le choix « Qu'est-ce que tu apprends ? »
   montre 🇪🇸 Espagnol / 🇩🇪 Allemand et ramène à l'allemand, la page
   s'appelle « Wortando Español ». Allemand : 0 écart.
   **L'inventaire complet des 168 autres différences** (hors dictionnaire) est
   dans `fusion-espagnol/inventaire.txt` : c'est la liste de travail des
   étapes 3 à 7.
   ⚠️ Le réglage Espagne / Amérique latine n'est PAS fait : il dépend des mots
   qui changent (étape 3, avec le contenu).
   Noté : le dictionnaire espagnol n'a que la paire **espagnol-anglais**
   (`espanol/dicc/es-en`, `en-es`) ; un espagnol-français manque.

3. **Ce qui n'existe qu'en allemand** (examens Goethe/DTZ, cas, scènes, voix
   d'Aurora, dictionnaire, fréquence, synonymes, marques régionales) : un
   drapeau par fonction dans la table de langue, au lieu d'un remplacement
   dans le fork.
   ✅ **Premier morceau fait en v730 (10 oct. 2026) : les cartes.**
   `data-apprendre` sur `<html>` dès le `<head>` ; les règles CSS du fork qui
   cachaient une trentaine d'exercices allemands ne valent plus qu'en
   espagnol (`html[data-apprendre="es"] …`). Articles (`ARTICLES_GENRE`,
   `articlePluriel()` : los/las), quiz des articles (el/la), personnes de
   conjugaison (`PERSONNES_CONJUGAISON`), les trois temps espagnols au verso
   (`blocTempsEspagnol`, aides en français ET en anglais — le fork ne les
   avait qu'en anglais), pastilles de registre et de construction.
   Le vérificateur lit maintenant `I18N_ESPAGNOL` et exige chaque clé en
   français et en anglais : il a trouvé un oubli du fork (en français, le
   panneau « Ser vs estar » gardait « der · den · dem · ein · kein »).
   **Le parcours retourne maintenant les cartes** (verso, temps cachés d'un
   verbe) et ouvre une carte de verbe et une d'adjectif : 123 chemins.
   Nouvelle référence allemande : `references/de-v729.json`, prise sur la
   version d'AVANT ce morceau ; après : 0 écart, carte de *sein* comprise.
   ✅ **Deuxième morceau fait en v731 : le contenu écrit dans le code.**
   Six listes en double (`praepTheme`, `partikelnTheme`, `konjunktionenTheme`,
   `ADVERB_CATEGORIES`, `ADVERB_CATEGORY_OPTIONS`, `REDEWENDUNG_CATEGORIES`) :
   l'allemande inchangée, l'espagnole de fork.py en mode espagnol, découpées
   par un extracteur qui suit chaînes et commentaires. Le panneau des
   expressions et ses groupes (dont `ausdrueckeModismos`, espagnol seulement),
   les titres des paquets, le radar sans branche des cas. La voix : « de »
   veut dire la langue apprise, `voicesForLang()` le traduit (es-*), le choix
   des réglages et la voix des cartes restent la même. Le dictionnaire
   (`dicc/`, paire espagnol-anglais). Sans objet en espagnol : visite guidée,
   essai des scènes, schéma des prépositions, crédits Aurora/fréquence/
   examens, tuile d'examen. Le vérificateur a trouvé les 11 options
   espagnoles du panneau sans `section` (défaut du fork) : rangées sous
   « mots ». Allemand : 0 écart sur 123 chemins.
   ✅ **Troisième morceau fait en v732 : les deux espagnols.** « Quel
   espagnol ? » (🇪🇸 Espagne / 🌎 Amérique latine), au premier lancement et
   dans les réglages, caché en allemand. `VARIANTE_ESPAGNOL`, rangée sous
   `wortandoEs_variante` ; changer recharge la page. En Amérique latine :
   *vosotros* caché partout dans les conjugaisons, « ellos/ustedes », voix
   es-MX si le téléphone en a une. `espanol/datos/variantes.json` : 17 noms
   sûrs (coche/carro, ordenador/computadora, móvil/celular, zumo/jugo,
   patata/papa, piso/departamento, billete/boleto, camarero/mesero,
   gafas/lentes…) ; en Espagne la carte cite l'autre mot en note, en Amérique
   latine elle prend le mot, l'article, le pluriel et l'exemple d'ici, et
   cite le mot d'Espagne. Vérifié dans le navigateur dans les deux modes.
   **Reste, et à soumettre à Jacques :**
   - trois noms écartés faute de forme commune en Amérique latine : *tarta*
     (pastel, torta, pay), *tortilla* (un autre plat), *zapatilla* ;
   - les **verbes** qui changent (*conducir/manejar*, *coger/tomar*,
     *aparcar/estacionar*, *enfadarse/enojarse*, *alquilar/rentar*) : pas
     encore de note, il faut le même mécanisme côté verbes ;
   - les **exercices** (`ejercicios.json`) gardent *vosotros* et les mots
     d'Espagne en mode Amérique latine ;
   - **aucune voix enregistrée** pour l'espagnol : deux corpus à chiffrer.

4. **La grammaire espagnole** (7 écrans de `gramatica_es.py`) en données,
   comme `grammaire.json` pour l'allemand.
   ✅ **Fait en v733 (10 oct. 2026).** `espanol/datos/grammaire.json`, au
   format de l'allemand : 41 textes d'écrans (temps, adverbes, expressions)
   versés dans `I18N` au chargement, plus **les sept fiches** (`fiches`),
   ouvertes par `abrirGramatica(id)` sur l'écran `gramaticaES`. Le fork ne les
   avait qu'en anglais, écrites pour des anglophones (« English gives you
   nothing to go on ») : la version **française est réécrite pour des
   francophones** — le français aide pour les deux passés, le subjonctif et
   la place des pronoms, et piège pour le genre (el color, la leche) et pour
   *cuando llegue* (« quand j'arriverai »). Les comparaisons avec l'anglais
   sont retirées des textes français des écrans. En espagnol, les tuiles de
   grammaire passent par `FICHE_PAR_TUILE` (dans `openOrbPanel`, donc les
   « Retour » aussi). La fiche de l'accord était **injoignable** dans le
   fork (option renommée puis cachée par une autre règle) : rendue, depuis
   le panneau des adjectifs. Allemand : 0 écart. Espagnol : 67 chemins, plus
   aucun `grammaire.json` introuvable.
   ⚠️ **À faire relire** : les fiches françaises sont de moi, comme les
   textes que le fork avait écrits ; elles méritent la relecture croisée
   (autre modèle, puis un hispanophone).
   Restent cachés en espagnol, à finir : les écrans d'explication des
   adverbes et des expressions (textes espagnols écrits, mais leurs boutons
   mènent à des exercices allemands et leurs libellés manquent).

5. **Les verbes** : les temps espagnols, la conjugaison, l'affichage.
6. **Les comptes.** L'espagnol passe par Firebase comme l'allemand : connexion,
   sauvegarde dans le cloud, codes d'invitation du tableau admin, bouton
   « Signaler un problème », suivi du parcours. Sa progression rangée à part
   dans Firestore (sinon elle écraserait celle de l'allemand : mêmes noms de
   champs). Une règle Firestore à ajouter dans la console : texte fourni.
   Les testeurs actuels gardent leur progression locale, versée dans leur
   compte à la première connexion.
7. **La bascule.** Quand le parcours espagnol du moteur égale la référence :
   `espanol/` devient une simple redirection vers le moteur réglé sur
   l'espagnol, et `fork.py` prend sa retraite.

Chaque étape est publiée seule, avec ses deux vérificateurs et le parcours
allemand identique à la référence.

## Les deux espagnols, dès le lancement

Décidé par Jacques le 10 octobre 2026 : **Espagne ET Amérique latine au
lancement**, au choix de l'apprenant.

- **Une question au premier lancement**, sur le même écran que « Qu'est-ce que
  tu apprends ? » : espagnol d'Espagne ou d'Amérique latine. Modifiable dans
  les réglages. La variante est un réglage du moteur (étape 1), pas une
  troisième langue : même progression, même compte.
- **La base des données est l'Espagne** : le vocabulaire actuel dit *coche*,
  *ordenador*, *zumo*, *móvil*, et chaque verbe a sa forme *vosotros*. La
  variante latino-américaine **retire** (cache *vosotros*) et **remplace**
  (les mots étiquetés), elle n'ajoute pas de personne de conjugaison.
- **Chaque mot qui change porte les deux formes**, et la carte affiche l'autre
  en note : « En Espagne : *coche* » / « En Amérique latine : *carro* », comme
  les marques (A) et (CH) de l'allemand. Repérage et vérification : quelques
  centaines de mots.
- **Deux voix.** L'espagnol n'a aujourd'hui **aucune** voix enregistrée (la
  synthèse du téléphone lit tout) : les deux corpus sont à enregistrer chez
  ElevenLabs. Mesurer le nombre de textes et le coût **avant** de dépenser,
  et le soumettre à Jacques.
- ⚠️ Le DELE et le SIELE acceptent **toutes** les variantes cultivées : ce
  n'est pas un argument pour l'Espagne (Gemini et moi l'avions dit à tort).

## Après

- Interface allemande pour l'espagnol (« allemand vers espagnol ») : un
  dictionnaire d'interface `de` à écrire. Aujourd'hui l'espagnol se lit en
  français ou en anglais.
- Le japonais suivra le même chemin : des données et une ligne dans la table
  des langues, plus un fork.
