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

## Ce qui est plus simple, et ce n'est pas rien

**Courriel et carte.** Pas de type de compte irréversible, pas de pays
verrouillé, pas de licence commerciale, pas de « Individual ne se convertit pas
en Business ». Tout le nœud administratif du 13 septembre disparaît.

Et c'est une API : l'outillage Python du dépôt s'y branche plus facilement que
sur une console.

## ⚠️ Mais sur les DROITS, c'est possiblement PLUS FAIBLE

Trois relevés, tirés des *Terms of Service* — pas des *API Services*, qui
régissent la revente à ses propres utilisateurs finaux et ne nous concernent
pas.

**1. La propriété des sorties n'est PAS confirmée.** La clause trouvée dit :

> *« Customer owns and retains all right, title, and interest in and to the
> **Customer Input**. »* (§6(b))

C'est l'**entrée** — ce qu'on téléverse — pas la **sortie**. Aucune clause
équivalente sur l'Output n'a été trouvée. ⚠️ **C'est exactement le trou qu'on
reprochait à BytePlus**, où la phrase *« BytePlus does not claim ownership of the
Output »* a disparu dans un document fusionné. Changer de porte ne le comble pas.

**2. L'entraînement sur nos données, sans retrait annoncé.**

> *« Company may generate, collect, store, use, transfer, and/or disclose to
> third parties Usage Data […] to design, develop, and offer Company products,
> services, and AI models. »* (§6(c))

Aucun mécanisme de retrait n'apparaît dans ces conditions. Chez BytePlus, le
*Data Authorization Agreement* en prévoyait un, même imparfait. ⚠️ Reste à
vérifier ce que « Usage Data » recouvre exactement : des métadonnées ou le
contenu. La définition change tout, et je ne l'ai pas.

**3. ET L'INDEMNITÉ EST INVERSÉE. C'est le point le plus important.**

| | BytePlus | fal |
|---|---|---|
| qui défend qui | **BytePlus défend et indemnise** le client contre les réclamations de PI visant les sorties de ses modèles (§3.1) | **le client indemnise fal** (§15) |
| exclusion | les réclamations de **marque** en usage commercial (§3.1(d)) | aucune clause trouvée où fal protège le client |

Chez BytePlus, nous étions couverts **sauf** sur la marque. Chez fal, il n'y a
pas de couverture à exclure — et c'est le client qui garantit fal contre les
réclamations visant ses entrées.

## Ce que j'en conclus, et ce qui reste à vérifier

**La complication qu'on évite est administrative ; la protection qu'on
abandonnerait est juridique.** Ce n'est pas un échange évident pour un produit
commercial portant une marque en cours de dépôt.

⚠️ **À lire soi-même avant de trancher** : les sections **4, 6 et 15** des
*Terms of Service*, et surtout les **définitions** de « Output Content »,
« Customer Input » et « Usage Data ». Mes relevés sont des citations, pas une
lecture complète du contrat.

**Ce qui ne change pas, quel que soit le fournisseur** : ni l'un ni l'autre ne
nous couvre sur le terrain de la marque. C'était déjà écrit plus haut pour
BytePlus, et c'est notre terrain.
