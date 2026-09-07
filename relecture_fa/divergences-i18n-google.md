# Ecarts de sens sur l'interface -- google

Produit par `python tests/contraste_i18n.py --langue fa --moteur google`. **Aucune correction appliquee.**

Le fa de l'interface a ete retraduit EN FRANCAIS, puis compare au francais d'origine. Le moteur ne voit jamais ce francais : il ne peut donc pas l'inventer.

**Ce n'est pas une liste de fautes.** Un moteur traduit, il ne juge pas : une formulation differente est souvent aussi juste. Et il ne voit RIEN du registre -- tutoiement, langue ecrite ou parlee -- qui reste a un relecteur humain.

220 cles examinees -- celles d'au moins 30 signes, en deca un aller-retour ne prouve rien --, 17 ecarts francs (proximite < 0.42).

### `op_verben_o5_d`  (proximite 0.05)

| | |
|---|---|
| francais d'origine | Un seul verbe en français, deux en allemand |
| fa     ecrit | دانستن یک چیز، یا شناختن کسی؟ |
| retraduit | Savoir quelque chose, ou connaître quelqu'un ? |

### `rel_intro`  (proximite 0.08)

| | |
|---|---|
| francais d'origine | L'app propose maintenant, au verso des cartes, les mots du cours qui disent à peu près la même chose. Ces paires ont été trouvées <strong>automatiquement</strong> : deux mots sont retenus s'ils partagent une traduction en français et en anglais.<br><br>La machine ne sait pas tout. <strong>Touche « pas un synonyme » sur les paires qui ne vont pas</strong> — inutile de marquer les bonnes, seules les mauvaises comptent. Tes réponses sont gardées au fur et à mesure. |
| fa     ecrit | برنامه اکنون در پشت کارت‌ها واژه‌هایی از درس را نشان می‌دهد که کمابیش یک چیز می‌گویند. این جفت‌ها <strong>خودکار</strong> پیدا شده‌اند: دو واژه وقتی نگه داشته می‌شوند که ترجمه‌ای مشترک در فرانسوی و انگلیسی داشته باشند.<br><br>ماشین همه‌چیز را نمی‌داند. <strong>روی جفت‌هایی که جور نیستند «مترادف نیست» را لمس کن</strong> — نشان کردن جفت‌های درست لازم نیست، تنها نادرست‌ها به کار می‌آیند. پاسخ‌های تو در همان لحظه نگه داشته می‌شوند. |
| retraduit | L'application affiche désormais au verso des cartes des mots de la leçon qui ont un sens plus ou moins identique. Ces paires sont détectées automatiquement : deux mots sont enregistrés lorsqu'ils ont une traduction commune en français et en anglais. L'application n'est pas infaillible. Touchez « Pas synonyme » sur les paires qui ne correspondent pas. Inutile de cocher les paires correctes, seules les paires incorrectes seront prises en compte. Vos réponses sont enregistrées instantanément. |

### `parler_desc`  (proximite 0.08)

| | |
|---|---|
| francais d'origine | Le modèle, puis toi, l'un après l'autre. C'est de s'entendre qui fait entendre l'écart — l'écouter en répétant ne suffit pas. Rien n'est noté et rien n'est envoyé : l'enregistrement reste sur l'appareil et disparaît à la phrase suivante. |
| fa     ecrit | اول الگو، سپس تو، یکی پس از دیگری. این شنیدنِ خود است که فاصله را آشکار می‌کند — شنیدن هنگام تکرار بس نیست. هیچ نمره‌ای داده نمی‌شود و هیچ چیز فرستاده نمی‌شود: ضبط روی دستگاه می‌ماند و با جملهٔ بعدی از میان می‌رود. |
| retraduit | D'abord le motif, puis vous, l'un après l'autre. C'est en s'écoutant soi-même que l'on perçoit la distance ; entendre ne suffit pas lorsqu'on répète. Aucun score n'est attribué, rien n'est transmis : l'enregistrement reste sur l'appareil et disparaît à la phrase suivante. |

### `tuiles_menu_desc`  (proximite 0.09)

| | |
|---|---|
| francais d'origine | On te donne la phrase en français et les mots allemands en vrac. Touche-les dans le bon ordre — pas de clavier. Le banc contient un ou deux mots en trop, choisis dans la même famille que ceux de la phrase : c'est là que se joue l'exercice. |
| fa     ecrit | جمله را به زبان خودت می‌بینی و واژه‌های آلمانی را درهم. آن‌ها را به ترتیب درست لمس کن — بدون صفحه‌کلید. روی نیمکت یکی دو واژهٔ اضافی هست، برگزیده از همان خانوادهٔ واژه‌های جمله: تمرین دقیقاً همین‌جاست. |
| retraduit | Vous voyez la phrase dans votre langue et les mots allemands mélangés. Touchez-les dans le bon ordre – sans clavier. Un ou deux mots supplémentaires, appartenant à la même famille que la phrase, sont posés sur le banc : l’exercice est là. |

### `next_badge_progress`  (proximite 0.10)

| | |
|---|---|
| francais d'origine | {current} sur {threshold} {unit} |
| fa     ecrit | {current} از {threshold} {unit} |
| retraduit | {actuel} à partir de {seuil} {unité} |

### `ecoute_menu_desc`  (proximite 0.12)

| | |
|---|---|
| francais d'origine | Une séance mains libres : l'app dit le mot, laisse un silence pour que tu le répètes à voix haute, puis lit la phrase d'exemple. Garde l'écran allumé — la voix se tait si le téléphone se verrouille. |
| fa     ecrit | نشستی بدون دست: برنامه واژه را می‌گوید، سکوتی می‌گذارد تا آن را بلند تکرار کنی، سپس جملهٔ نمونه را می‌خواند. صفحه را روشن نگه دار — اگر تلفن قفل شود، صدا خاموش می‌شود. |
| retraduit | Session mains libres : l’application prononce le mot, fait une pause pour vous laisser le répéter à voix haute, puis lit la phrase d’exemple. Laissez l’écran allumé ; si le téléphone est verrouillé, le son sera coupé. |

### `carte_dire_desc`  (proximite 0.15)

| | |
|---|---|
| francais d'origine | Au verso d'une carte, l'allemand se dit tout seul. Choisis ce que tu veux entendre. Ce que tu retires reste affiché, et son haut-parleur fonctionne toujours — tu peux l'écouter quand tu le décides. |
| fa     ecrit | در پشت کارت، آلمانی خودش خوانده می‌شود. انتخاب کن چه چیزی را می‌خواهی بشنوی. آنچه برداری همچنان روی صفحه می‌ماند و دکمهٔ بلندگویش کار می‌کند — هر وقت خواستی می‌توانی آن را بشنوی. |
| retraduit | Au verso de la carte, le texte allemand est affiché. Choisissez ce que vous souhaitez écouter. Votre sélection reste affichée à l'écran et le bouton du haut-parleur est fonctionnel : vous pouvez l'écouter quand vous le souhaitez. |

### `myvocab_vide_explication`  (proximite 0.17)

| | |
|---|---|
| francais d'origine | <strong>Mon vocabulaire est encore vide.</strong><br>C'est ta réserve personnelle : les mots que tu rencontres ailleurs — en cours, dans un texte, dans une conversation — et qui ne sont pas dans l'app.<br><br>Cherche-en un ci-dessus, puis touche le <strong>+</strong> à côté du résultat du dictionnaire. Il deviendra une carte à réviser comme les autres. |
| fa     ecrit | <strong>واژگان من هنوز خالی است.</strong><br>این ذخیرهٔ شخصی توست: واژه‌هایی که جای دیگری با آن‌ها روبه‌رو می‌شوی — سر کلاس، در یک متن، در یک گفت‌وگو — و در برنامه نیستند.<br><br>یکی از آن‌ها را بالا جست‌وجو کن، سپس <strong>+</strong> کنار نتیجهٔ فرهنگ واژگان را لمس کن. آن واژه هم مانند بقیه به کارتی برای مرور تبدیل می‌شود. |
| retraduit | <strong>Mon vocabulaire est encore vide.</strong><br>Voici votre lexique personnel : les mots que vous rencontrez ailleurs (en cours, dans un SMS, dans une conversation) et qui ne figurent pas dans l’application.<br><br>Recherchez-en un ci-dessus, puis appuyez sur le <strong>+</strong> à côté du résultat. Ce mot devient alors une fiche de révision, comme les autres. |

### `op_konjunktionen_o10_d`  (proximite 0.20)

| | |
|---|---|
| francais d'origine | Un seul « quand » en français — deux mots en allemand |
| fa     ecrit | زمان، یا پرسش؟ |
| retraduit | L'heure, ou une question ? |

### `op_konjunktionen_o9_d`  (proximite 0.24)

| | |
|---|---|
| francais d'origine | Un seul « si » en français — deux mots en allemand |
| fa     ecrit | شرط، یا پرسش غیرمستقیم؟ |
| retraduit | Condition ou question indirecte ? |

### `op_konjunktionen_o11_d`  (proximite 0.25)

| | |
|---|---|
| francais d'origine | Un seul « mais » en français — et deux conditions à vérifier |
| fa     ecrit | پس از جملهٔ منفی، پیونددهندهٔ دیگری لازم است |
| retraduit | Après une phrase négative, un autre mot de liaison est nécessaire. |

### `op_praep_sub`  (proximite 0.37)

| | |
|---|---|
| francais d'origine | Cas fixe & Wechselpräpositionen |
| fa     ecrit | حالت ثابت و Wechselpräpositionen |
| retraduit | prépositions fixes et variables |

### `op_konjunktionen_o2_t`  (proximite 0.39)

| | |
|---|---|
| francais d'origine | Coordination ou subordination ? |
| fa     ecrit | هم‌پایه یا وابسته؟ |
| retraduit | Pair ou dépendant ? |

### `srs_aide_intro`  (proximite 0.40)

| | |
|---|---|
| francais d'origine | Tu réponds une seule chose — si le mot t'est revenu. C'est l'app qui en déduit la date. |
| fa     ecrit | تو فقط یک چیز پاسخ می‌دهی — اینکه واژه به یادت آمد یا نه. برنامه از همان، فاصلهٔ مرور بعدی را درمی‌آورد. |
| retraduit | Vous n'avez qu'à répondre à une seule question : si vous vous souvenez du mot ou non. Le programme calcule ensuite l'intervalle de révision suivant. |

### `streak_freeze_earned`  (proximite 0.41)

| | |
|---|---|
| francais d'origine | Gel de série gagné ! Il protégera ta série un jour où tu en manques un. |
| fa     ecrit | انجماد زنجیره به دست آوردی! روزی که یک روز را از دست بدهی، از زنجیره‌ات محافظت می‌کند. |
| retraduit | Vous avez gagné le gel de chaîne ! Le jour où vous manquez une journée, votre chaîne est protégée. |

### `op_konjunktionen_o12_d`  (proximite 0.41)

| | |
|---|---|
| francais d'origine | Ce qui passe devant pousse le verbe — et le sujet derrière |
| fa     ecrit | آنچه جلو می‌آید فعل را می‌راند — و نهاد را پشت آن |
| retraduit | Ce qui est mis en avant détermine l'action — et l'entité qui la contrôle. |

### `carte_phrase_non`  (proximite 0.42)

| | |
|---|---|
| francais d'origine | Non — mot et pluriel seulement |
| fa     ecrit | نه — تنها واژه و جمع |
| retraduit | Non — seulement le mot et le pluriel |

