# Droits sur les vidéos OmniHuman — ce qui est vérifié, et ce qui ne l'est pas
### 12 septembre 2026

Wortando est un projet **commercial**, avec un dépôt de marque WORTANDO en
cours à l'EUIPO. Les vidéos de la série « Mark in Berlin » sont générées par
**OmniHuman 1.5** chez BytePlus. Ce fichier dit exactement ce qu'on sait de
nos droits sur ces vidéos, et ce qu'on ne sait pas.

## ✅ Vérifié dans les *Service Specific Terms*

**OmniHuman est nommément couvert.**

> *Vision AI means the visual- and image-related artificial intelligence
> processing services provided by BytePlus to Customer, including
> **OmniHuman**, DreamActor, Dreamina API, Avatar, Identity Verification…*

**Aucune obligation de filigrane pour Vision AI.** Le contraste est net et
il est signifiant : **Lumina**, **Kickart** et **Dramagic** ont chacun une
clause interdisant de retirer le filigrane invisible **et imposant un
filigrane visible** sur toute sortie diffusée à l'extérieur. La section
*Seed Speech and Vision AI* n'en contient aucune.

**BytePlus défend et indemnise** en cas de réclamation d'un tiers pour
atteinte à la propriété intellectuelle sur une sortie produite par leurs
propres modèles (§3.1), sous conditions de notification et de contrôle de la
défense.

## ⚠️ Deux réserves qui nous concernent directement

**L'indemnité exclut les marques.** §3.1(d) : elle ne joue pas

> *where the claim is related to a trademark-related right as a result of
> your and/or your Authorized Users' use of such Output in trade or commerce*

C'est précisément notre terrain — un produit commercial portant une marque en
cours de dépôt. Sur ce point-là, nous ne sommes pas couverts.

**Le « Data Authorization Agreement »** accorde à BytePlus une licence
*« unconditional, irrevocable, non-exclusive, royalty-free, sublicensable,
transferable, perpetual and worldwide »* sur les **Authorized Data**, avec
une procédure de retrait — et la mention que ce qui a été autorisé **avant**
le retrait ne peut pas être techniquement effacé. ⚠️ Ça ne parle **pas** de
la propriété de nos vidéos ; ça parle de l'usage de nos données pour
améliorer leurs modèles. À vérifier dans la console : est-ce actif par
défaut ?

## ❌ Ce qui n'a PAS pu être vérifié

**La clause qui dirait en toutes lettres que la sortie nous appartient.**
Un moteur de recherche cite *« BytePlus does not claim ownership of the
Output »* — mais la phrase venait des anciennes *Specific Terms for the
BytePlus Video Generation Model Services*, page qui **redirige aujourd'hui**
vers un document fusionné où elle est introuvable. ⚠️ **Ne pas citer cette
phrase comme acquise** tant que le support ne l'a pas confirmée.

**Et une phrase croisée sans pouvoir la rattacher au bon service** :
*« The Services provided to you are limited to enterprise usage. »* Si elle
couvre Vision AI, elle pèse sur le choix du type de compte.

## Le ticket

**I-2026091223400001**, ouvert le 12 septembre 2026 à 17 h 40, statut
*Processing*. Quatre questions : propriété des sorties, survie des droits
après résiliation, filigrane, et autorisation de données.

*(Le formulaire a tronqué la dernière ligne — « Thank y » au lieu de
« Thank you. ». Sans conséquence.)*

⚠️ **Tant que la réponse n'est pas arrivée, on monte et on regarde, mais on
ne diffuse pas publiquement.** La distinction est nette : le travail ne
demande pas cette certitude, la publication commerciale si.

## Le compte BytePlus

⚠️ **Deux choix irréversibles**, et leur doc le dit : *« the account type,
country selected cannot be changed after the account profile submitted »*.

- **Type** : prendre **Business**. Leur tableau des accès produits liste,
  pour un compte Personal, *« ModelArk, Seedream, Seedance, AI-Saving Plan,
  OneArt, ArkClaw »* — **OmniHuman n'y est pas** : il vit sous Vision AI.
  Business ne demande **aucune licence d'entreprise**, seulement une adresse
  complète, un téléphone vérifié et un *Organization Name* qui figure sur
  les factures.
- **Pays** : à vérifier avant de soumettre. Leur formulaire de contact
  proposait « Germany » par défaut.

## Les autres maillons de la chaîne

| | licence |
|---|---|
| **ElevenLabs** (les voix) | usage commercial couvert sur les forfaits payants, sans licence séparée |
| **Artlist** (images, SFX) | licence commerciale ; les fichiers téléchargés restent acquis même sans abonnement. ⚠️ Les SFX sont un **plan distinct** — vérifier ce que couvre « AI Creator » |
| **OmniHuman** | ce fichier |


---

# fal.ai — le même modèle, une autre porte
### 13 septembre 2026

Les crédits Artlist épuisés et le compte BytePlus bloqué, la question s'est
posée : **OmniHuman 1.5 ailleurs ?** Oui — **fal.ai**, à **0,16 $ la seconde**,
exactement le tarif BytePlus. Aussi sur Replicate (`bytedance/omni-human-1.5`)
et chez AIMLAPI.

**Courriel et carte.** Pas de type de compte irréversible, pas de pays
verrouillé, pas de licence commerciale, pas de « Individual ne se convertit pas
en Business ». Tout le nœud administratif du 13 septembre disparaît. Et c'est
une API : l'outillage Python du dépôt s'y branche plus facilement que sur une
console.

## ⚠️ Ce que ma première lecture a dit de faux

J'avais écrit ici — et poussé dans un commit — que fal était **plus faible que
BytePlus sur les droits**, sur trois points. Après lecture du texte intégral,
**deux des trois étaient faux.**

La cause est précise et se refera : j'avais des **citations de clauses sans la
section 3, les définitions**, et sans la section 7. Un contrat ne se lit pas par
extraits — le sens d'une clause vit dans un terme défini trente lignes plus
haut. C'est la même erreur que le champ `apparence` de Mark : lire la
description au lieu d'ouvrir la pièce.

## Ce que le texte dit vraiment

### 1. Les sorties : personne ne les réclame, et elles sont confidentielles

Il n'existe **aucune clause où fal accorde la propriété de l'Output** — §6(b) ne
parle que du Customer Input. Mais il n'en existe **aucune où fal la réclame**,
et deux clauses vont dans notre sens :

**§4(c)** — fal ne garantit pas que la sortie soit originale ou non
contrefaisante, *« or otherwise entitle Company to any intellectual property
rights in any Output Content »*. C'est fal qui écarte ses propres droits sur la
sortie.

**§7(a)** — et c'est la clause qui compte le plus, celle que j'avais manquée :

> *« Customer's Confidential Information includes Customer Input **and Output
> Content generated for Customer**. »*

Nos plans sont contractuellement **notre information confidentielle**. fal ne
peut s'en servir que pour exécuter le service, doit les protéger, et ne peut les
divulguer qu'à qui en a besoin — cinq ans après la fin du contrat. En pratique
c'est plus utile qu'une clause de propriété.

⚠️ **La limite honnête** : « rien n'empêche fal de générer une sortie identique
ou similaire pour un autre client » (§7(e)), et §4(c) prévient que les sorties
ne sont pas uniques entre usagers. Ce n'est pas une fuite — c'est la nature d'un
modèle génératif, et BytePlus dit la même chose.

### 2. L'entraînement sur nos données : j'avais tort

J'avais sonné l'alarme sur « Usage Data » (§6(c)) faute d'en avoir la
définition. Elle est à **§3(e)** :

> *« **anonymized or aggregated** data collected, computed, originated, or
> stored by Company resulting from the use or provision of the Services »*

Anonymisées ou agrégées. Ce sont des métriques d'usage, pas nos vidéos. Et §7
confirme par l'autre bout : les sorties sont de l'information confidentielle, et
la confidentialité **exclut** expressément les Usage Data — les deux catégories
sont disjointes. **Nos plans ne partent pas à l'entraînement.**

### 3. L'indemnité : ce point-là tient

C'est le vrai écart, et il reste.

| | BytePlus | fal |
|---|---|---|
| fournisseur → client | **défend et indemnise** contre les réclamations de PI visant les sorties (§3.1), **sauf** la marque en usage commercial | **rien** — aucune clause en ce sens |
| client → fournisseur | — | le client indemnise fal (§15) |

⚠️ Mais l'indemnité du §15 est **plus étroite** que je ne l'avais dit : elle
vise les réclamations contre le **Customer Input**, la violation des Terms, la
faute du client et ses End Users. Pas « tout ». Comme nos entrées sont nos
propres images de personnages, le risque réel est faible.

**Et surtout : la protection qu'on perd, on ne l'avait déjà pas.** BytePlus
excluait précisément les réclamations de **marque** — notre seul terrain de
risque, avec WORTANDO en cours de dépôt. Sur ce qui nous menace vraiment, les
deux offrent la même chose : rien.

## Quatre points qu'il faut connaître avant de signer

**⚠️ Les conditions de ByteDance peuvent revenir par la bande.** §14(b) : l'usage
des « Third-Party Materials » *« may be subject to additional terms »*. OmniHuman
est un modèle ByteDance hébergé par fal — passer par fal simplifie le **compte**,
pas nécessairement le **modèle**. §14(c) interdit par ailleurs d'utiliser les
sorties pour entraîner un concurrent du modèle, ce qui ne nous concerne pas.

**L'arbitrage se refuse, et ça expire.** §18(k) : **30 jours** après acceptation,
par courriel à `support@fal.ai`, avec nom complet, adresse postale et courriel,
et l'intention clairement exprimée. Ça ne coûte rien et garde le tribunal
ouvert. Sinon : arbitrage individuel AAA, droit californien, San Francisco
(§19) — c'est-à-dire, depuis Berlin ou le Québec, aucun recours praticable.
Et **un an** pour agir, passé ce délai la réclamation est éteinte (§18(h)).

**Le plafond de responsabilité est de 50 $**, ou le montant payé dans les douze
mois (§17(b)). À nos volumes, c'est symbolique. À retenir : si fal perd nos
données ou interrompt le service en plein montage, il n'y a rien à récupérer.

**Les crédits expirent** : 365 jours (90 pour les promotionnels), non
remboursables, non transférables (§9(a)). ⚠️ **N'acheter que ce qu'on brûlera
dans l'année.** Mesuré sur l'épisode 2 : **13 plans d'avatar, 52 secondes, soit 8,32 $**
— les six plans de décor sont des images fixes et ne passent pas par OmniHuman.
La provision se calcule en épisodes, pas en gros paquet « pour être tranquille ».

## Ce que j'en conclus

**fal est acceptable pour notre usage**, et l'était déjà avant que je le
noircisse. Les sorties sont traitées comme les nôtres et comme confidentielles,
l'entraînement ne les touche pas, il n'y a ni filigrane ni restriction
commerciale, et le blocage administratif disparaît.

Ce qu'on abandonne — la défense de BytePlus contre les réclamations de PI — ne
nous couvrait pas là où nous sommes exposés. **Le dépôt de marque reste notre
seule vraie protection, chez l'un comme chez l'autre.**

⚠️ **À faire dans les 30 jours de l'inscription** : le courriel d'exclusion de
l'arbitrage. C'est gratuit, c'est irréversible une fois le délai passé, et c'est
le genre de chose qu'on ne pense à regretter qu'au moment où elle sert.
