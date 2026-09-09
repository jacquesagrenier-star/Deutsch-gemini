# Veille — outils et méthodes de vidéo générée
### 9 septembre 2026, au soir d'une journée où presque rien n'a marché

Ce document répond à une question posée après huit heures d'échecs : **est-ce
qu'on s'y prend bien ?** Il rassemble ce qui s'écrit sur le web par les
praticiens, les éditeurs de blogs spécialisés et les documentations d'éditeurs.

**Trois niveaux de confiance, et je les signale à chaque fois :**

- **[mesuré]** — vérifié par nous, sur nos fichiers, aujourd'hui.
- **[éditeur]** — documentation officielle d'Artlist, ByteDance, ElevenLabs.
- **[blog]** — presse spécialisée et blogs commerciaux. Souvent justes, jamais
  vérifiables, et intéressés à vendre quelque chose. À traiter comme des
  hypothèses.

---

## 1. La leçon principale, et elle nous vise

> « **Accepting the first render is the single most common mistake in AI film
> dialogue**, and take selection is the cheapest fix available. » [blog]
>
> « Working in the other direction, **regenerating video until the mouth
> happens to match, burns credits and never fully locks**. » [blog]

C'est exactement ce qu'on a fait aujourd'hui : régénérer jusqu'à ce que la
bouche tombe juste. Nommé noir sur blanc comme la façon de brûler un budget
sans jamais verrouiller.

**La méthode qu'ils opposent est celle du cinéma depuis un siècle :**

> « **Lock picture first, conform audio to picture second, verify on consonants
> third.** » [blog]

Quand une réplique ne colle pas à l'image, on ne retourne pas le plan : on
refait le son pour qu'il colle. C'est l'ADR, le doublage. Il existe même un
outil professionnel dédié — Revoice Pro, dont la fonction *Audio Performance
Transfer* applique le minutage de la piste image à la voix enregistrée.

**Ce qu'on en a fait le soir même :** `audio/conformer.py` étire la voix
ElevenLabs pour qu'elle épouse la bouche du plan, sans toucher à la hauteur ni
au timbre. Le plan 11, que la mesure condamnait, a été sauvé sans un crédit.
**[mesuré]** — avec une réserve : à +25,7 % l'étirement détonne à côté des
plans non étirés. Il rattrape les quasi-réussites, pas les désastres.

---

## 2. Le paysage des modèles vidéo

| modèle | ce qu'il fait de mieux | prix indicatif |
|---|---|---|
| **Seedance 2.0** (ByteDance) | dialogue, lip-sync phonémique 8+ langues, multi-plans | 0,022 $/s en tier Fast [blog] ; **120 crédits/s chez Artlist en mode référence** [mesuré] |
| **Seedance 2.5** | 30 s en une passe, 50 références (30 img / 10 vid / 10 audio), 720p | mode référence non couvert par Unlimited [éditeur] |
| **Kling 3.0** (Kuaishou) | **recommandé pour les scènes de dialogue**, 4K/60 i/s, lip-sync multilingue | « le moins cher des cinq » [blog] — **à vérifier chez vous** |
| **Veo 3.1** (Google) | seul à générer du dialogue en 48 kHz ; décors, extérieurs, météo | 0,03–0,50 $/s en API [blog] |
| **Sora 2** (OpenAI) | audio synchronisé décrit au prompt | — |
| **Happy Horse 1.1** (Alibaba) | **conçu pour les têtes parlantes**, lip-sync 7 langues, open source | sur Artlist |
| **LTX-2.5** | **seul open source avec audio+vidéo en une passe** ; tourne en local | gratuit, 32 Go de VRAM (24 Go en quantifié) [blog] |

**Le point qui nous concerne le plus** [blog] :

> « Dialogue audio quality is **noticeably better in English than other
> languages**. For multilingual productions, **Kling 3.0's lip-sync pipeline
> outperforms** [Veo]. »
>
> « **Wide and medium shots hold up well** because the mouth is small in frame
> and small errors are invisible. **Tight close-ups are where you inspect frame
> by frame** — if your shot is a talking head at close range and the sync is
> not landing, you may need to **reframe wider** or take the speech out
> entirely. »

Nous faisons des gros plans en allemand. C'est le cas le plus difficile de
tous, sur la langue la moins bien servie. Ça explique beaucoup.

---

## 3. Les trois familles d'outils de bouche

Il faut les distinguer, parce qu'elles ne promettent pas la même chose et
qu'on les a confondues toute la journée.

**a) Les synchroniseurs — sync.so, Runway.**
Ils prennent VOTRE audio et repeignent les lèvres. Verrouillés sur votre onde,
zéro dérive possible. **Mais ils n'héritent pas de la mâchoire** : si le clip
source articule autre chose, ils ne peuvent pas la retimer. [mesuré] — c'est
le mur de la journée du 8 et de la matinée du 9.

> « Sync.so **leads on accuracy for real footage** » [blog]

**b) Les générateurs — Seedance, Kling, Veo.**
Ils construisent une vraie articulation, mâchoire comprise. Mais ils
**rejouent** le texte à leur tempo : l'audio de référence est un métronome, pas
une bande-son. [éditeur] :

> « The original audio acts as a **timing guide** for mouth movement, **not as a
> voice sample the model reproduces**. »

[mesuré] : décalage d'attaque de +0,35 s très régulier, et étirement sur les
répliques longues.

**c) Les avatars — Hedra Character-3, HeyGen, VEED Fabric.**
Ils prennent **une image fixe et un fichier audio** et fabriquent la vidéo à
partir du son. La voix est la vôtre, exactement. [blog] :

> « Hedra Character-3 [...] **reads the prosody of your audio** and matches it
> with micro-expressions [...] natural blinking, subtle head movement. »
> Prix : ~15 $/mois Basic, ~30 $ Creator, API à partir du plan Pro (~40 $).
>
> « VEED Fabric 1.0 [...] **0,08 $ par seconde** en 480p. »

**C'est la famille qu'on n'a jamais essayée**, et c'est celle qui résout
structurellement notre problème : la voix pédagogique reste intacte ET la
bouche est construite dessus. Le prix à payer, d'après les mêmes sources, est
un visage moins vivant qu'un plan généré — mais Hedra est justement loué pour
ses micro-expressions.

**Piste à tester en priorité demain**, et elle ne coûte pas de crédits Artlist.

---

## 4. Ce que les praticiens disent des pièges

Tout ceci est [blog], mais les mêmes points reviennent partout et **décrivent
exactement les échecs qu'on a vécus** — ce qui leur donne du poids.

**Sur la longueur des répliques**
> « Longer lines produce progressively mushier mouth movements. **Short
> sentences work much better — five to ten words per line is the sweet spot.** »
>
> « **12 words for a 10-second clip, 20 for 15 seconds.** »

[mesuré] chez nous : sous 2,2 s de parole, quatre prises sur cinq passent.
Au-dessus, zéro sur deux.

**Sur le silence**
> « **Don't remove every silence to the bone.** Leave natural short pauses
> (150–400 ms) between phrases — Seedance uses those micro-pauses as
> **anchors**. »

⚠️ Nos pistes de référence coupent le silence au millième. **À revoir.**

**Sur la sur-direction**
> « **Most bad lip sync comes from giving it too many performance notes, not
> too few.** Over-directed prompts divide attention among acting, lighting,
> camera motion, sound effects, and dialogue. Keep the visual brief compact,
> then specify speaker, language, exact line, tone, and pause. »

Nos prompts font huit paragraphes. [mesuré] : c'est en **décrivant** le cadrage
qu'on l'a fait dériver (15,9 dB) ; en se taisant, il est revenu (29,5 dB).

**Sur la dérive en cours de plan**
> « Lip movement and voice are tight at the start but **drift apart by the
> end**, most noticeable on multi-sentence dialogue. Insert **a written beat**
> (« She pauses, then continues: ») between sentences — Seedance uses written
> beats as **resync anchors**. »

À essayer sur le plan 13, qui est justement en deux phrases.

**Sur la méthode d'essai**
> « **Test a short clip first, then regenerate while changing only the audio,
> the source frame, or the prompt — not all three together.** »

On a changé trois choses à la fois plusieurs fois aujourd'hui.

---

## 5. Le montage — ce qui fait qu'un film généré sonne faux

**Couper plutôt qu'accélérer**
> « Most pacing problems in AI footage are solved by **trimming to the seconds
> where the action lands**, not by speeding the whole clip. »

**Ne pas tout resserrer**
> « **Removing every pause strips the edit of its rhythm.** Emotional beats,
> deliberate pauses before a key point, and natural breaths between sentences
> all serve the pacing. »

C'est ce que Jacques disait le 8 septembre — *« on n'est pas obligé d'ajouter
beaucoup, juste un petit peu »*.

**Les cuts en J et en L — la technique la plus utile pour nous**

Un **J-cut** fait arriver le son du plan suivant **avant** l'image ; un
**L-cut** laisse le son du plan précédent déborder **sur** l'image suivante.

> « Rather than cutting to each character when they say a line, **dialogue can
> overlap on the character listening before cutting to the character talking.**
> [...] Real conversations aren't perfectly sequential. Cutting strictly between
> speakers can feel robotic. »

**Pourquoi ça nous concerne directement** : notre épisode est un
champ-contrechamp de douze répliques, montées bout à bout, chacune séparée de
la suivante. C'est précisément la structure que les monteurs décrivent comme
« robotique ». Et un J-cut a un bénéfice secondaire énorme pour nous : **il
recouvre la queue d'un plan dont la bouche traîne**, puisque l'image passe au
plan suivant pendant que le son continue.

Autrement dit, une partie de nos défauts de bouche **se règlent au montage, pas
à la génération.**

**Le plan avant la dépense**
> « Creating a shot list with **specific duration targets before generating a
> single clip** — « establishing wide, 4 seconds », « character close-up, 3
> seconds » — forces you to think about pacing before committing resources. »

---

## 6. La cohérence des personnages, pour une série

Pertinent si Mark et Anna reviennent dans dix épisodes.

> « **30 à 50 images de référence**, étiquetées, pour entraîner un LoRA. [...]
> Une fois entraîné, il permet de générer le même personnage à travers
> différentes scènes avec une grande précision. »
>
> « Un court métrage documenté de 70 secondes a gardé deux personnages
> identiques dans toutes les scènes **avec des planches multi-angles tenues en
> contexte — sans LoRA, 750 $ au total**. »
>
> « Le LoRA l'emporte pour **un personnage phare récurrent sur des dizaines
> d'apparitions** dans un style verrouillé. »

Pour un épisode, les planches suffisent — c'est ce qu'on fait. Pour une série,
le LoRA devient rentable. À garder pour plus tard.

---

## 7. L'économie réelle

Le point le plus utile de toute la veille [blog] :

> « **The dominant cost driver is the iteration rate** (how many generations it
> takes to get a shot right), **not the per-second price.** »
>
> « Expect to generate **300–500 seconds of raw footage for a three-minute
> short**, often re-generating the same scene two or three times, resulting in
> **80–150 individual clips** for the final output. »
>
> « Realistic budgeting requires modeling shots per minute, seconds per shot,
> **attempts per shot**, and per-second cost, then **adding a 30 % exploration
> buffer**. »

[mesuré] chez nous : environ **1,4 génération par plan réussi** aujourd'hui —
ce qui est bon. Le problème n'était pas le taux d'essai, c'était que la
première moitié de la journée a été dépensée dans une chaîne à contre-emploi.

**Le routage multi-modèles**
> « Using a cheap model for bulk and draft content, and reserving premium
> models for hero shots, **typically saves 30–50 %**. »

Pour nous : les plans moyens (05, 06) où la bouche est petite pourraient
passer par un modèle bon marché ; seuls les gros plans (12, 13, 16, 17)
mériteraient le meilleur.

---

## 8. Ce que j'en tirerais pour Wortando

**Trois choses à vérifier demain, aucune ne coûte de crédits Artlist :**

1. **Le prix d'un clip Kling 3.0 de 7 secondes.** Recommandé pour le dialogue,
   annoncé comme le moins cher. Si c'est une fraction des 840 crédits de
   Seedance, tout change.
2. **Hedra Character-3**, essai gratuit. Il prend une image + votre mp3 et
   fabrique la bouche dessus. C'est la seule famille qui garde votre voix
   intacte ET construit la mâchoire.
3. **Le montage en J-cut** sur les cinq plans acquis. Gratuit, et ça pourrait
   masquer une partie des défauts de queue sans régénérer quoi que ce soit.

**Deux corrections à apporter à nos prompts :**

4. **Laisser des micro-pauses** dans les pistes de référence au lieu de couper
   le silence à l'os.
5. **Alléger les prompts.** Huit paragraphes, c'est ce que les praticiens
   désignent comme la première cause de mauvais lip-sync.

**Et une décision de scénario :**

6. **Le plan 13 doit être coupé en deux.** Sa réplique de 4,57 s est plus du
   double de ce qui passe, et aucune durée de clip ne le sauve.

---

## 9. Ce que je n'ai pas pu vérifier

- **Les prix chez vous.** Artlist facture selon votre formule ; je n'ai que les
  120 crédits/seconde relevés ce soir sur Seedance en mode référence.
- **La qualité réelle de Kling 3.0 et de Hedra en allemand.** Aucune source ne
  teste l'allemand ; les tests portent sur l'anglais, le mandarin, l'espagnol.
- **Les communautés elles-mêmes.** Reddit bloque la lecture automatisée, et les
  discussions Discord ne sont pas indexées. Tout ce qui est cité ici vient de
  blogs — dont plusieurs appartiennent à des éditeurs d'outils concurrents.
  **C'est la faiblesse principale de cette veille**, et elle mériterait une
  heure passée par un humain dans un forum.

---

*Sources principales : documentation Artlist (Seedance 2.0 Family, Seedance 2.5,
AI Toolkit FAQ, Artlist MCP), CrePal, Seedance.tv, MindStudio, Mirrorize,
Higgsfield, Atlas Cloud, LTX, StudioBinder, lipsync.com, Hedra, Percify,
ScreenWeaver, Magic Hour.*
