# Examen blanc telc Pflege : les 7 autres langues, ce qu'un locuteur natif devrait relire

14 nov. 2026. L'interface et les aides de l'examen (consignes, explications, critères, informations de la fiche)
sont écrites en français et en anglais, puis traduites depuis le français dans les sept autres langues d'interface :
355 textes par langue, sans relecture native.

- Fichiers : `visuel/prototype/telc/pflege/donnees/langues/interface.<l>.json` et
  `visuel/prototype/telc/pflege/donnees/modell-1/langues/<épreuve>.<l>.json`, des dictionnaires plats {clé : texte}.
- Ce qui manque : `python visuel/prototype/telc/pflege/outils/a_traduire.py` (le compte) ; `--sortie f.json --langue l`
  (les textes à traduire). Contrôle complet : `python tests/pflege_examen.py` (rien ne manque, les {x} sont intacts).
- L'allemand de l'examen n'est jamais traduit : textes, mots cités, noms des parties, AEDL, noms propres.
- Conventions reprises du telc A2·B1 (`retours/A-RELIRE-TELC-LANGUES.md`) : tutoiement de l'élève, lecteur neutre en
  uk, ru, pl, pt, ar ; l'apostrophe ʼ en ukrainien ; les cas allemands nommés en allemand ; le Brésil en portugais ;
  ی et ک persans.

## Pour toutes les langues

1. Les **termes du métier** n'ont été vérifiés par aucun soignant natif : « continent », « orienté (temps, lieu,
   personne) », « déambulateur », « hémocultures », « médecine du travail », « jardin ouvrier ».
2. Les **noms propres** restent en caractères latins (Elif, Jonas, Herr Brandt…), alors que les pages du telc A2·B1
   translittèrent en ru, uk, fa, ar : à harmoniser dans un sens ou dans l'autre.
3. Les **descripteurs des grilles** (`pf_desc_*`) : la gradation doit rester nette d'un cran à l'autre.

## Langue par langue

### Portugais du Brésil (pt)
- « simulado » (examen blanc), « gabarito » (corrigé), « prova oral » ; « Ouvir » sur les tuiles mais « compreensão
  oral » dans les textes.
- « plantão da manhã » (Frühdienst), « unidade » (service), « escala » (planning), « relatório de enfermagem ».
- « educadora em diabetes », « comissão de controle de infecção », « serviço de medicina do trabalho », « motorneiro
  de bonde », « horta comunitária » (jardin ouvrier : un Schrebergarten est privé), « relatório em texto corrido ».
- Les explications qui glosent un verbe allemand (n50, n51, n56) : « A glicemia se “misst” » est-il naturel ?

### Turc (tr)
- « bölüm » pour l'épreuve, « kısım » pour la partie : les manuels turcs du telc disent peut-être « Bölüm » pour Teil.
- « sınav görevlisi » pour l'examinateur (« sınav değerlendiricisi » ?).
- « kontinan (idrar ve dışkısını tutabiliyor) », « oryante », « yürüteç », « hobi bahçesi », « iş sağlığı birimi ».
- Critères : « Metin düzeni », « Dil doğruluğu », « Akıcılık » ; « bir basamak kaybettirir » (perdre un cran).
- « Plusquamperfekt », « genitif alan bir edat » parlent-ils à un apprenant turc ?

### Russe (ru)
- « отчёт о поступлении », « биографический отчёт », « лист анамнеза » / « биографическая анкета »,
  « сестринский пост », « служба производственной медицины ».
- « Говорение » pour l'épreuve orale, « языковые элементы » pour les Sprachbausteine.
- « контролирует мочеиспускание и стул (kontinent) » ; « ориентирован (во времени, месте, собственной личности) ».
- Descripteurs : « Речь идёт хорошо, с паузами и несколькими повторными попытками », « обходными путями ».

### Ukrainien (uk)
- « звіт про надходження (пацієнта) », « біографічний звіт », « анамнестична картка » ; « Таблиці оцінювання й
  результат » pour les grilles (« шкала », « критерії » ?), « Результат пробного іспиту ».
- « без нетримання (континентний) », « посіви крові на гемокультуру », « служба медицини праці », « сестринський
  пост », « консультантка з діабету ».
- Les explications qui glissent le verbe allemand après le verbe ukrainien (n51, n56) : lourd ?
- Formes neutres un peu sèches : « {m} хв », « Думка: {n} » (L'avis de {n}).

### Persan (fa)
- Noms des épreuves repris de l'app telc (شنیدن، خواندن، نوشتن، گفتن) ; « عناصر زبانی » ; « قسمت » pour l'épreuve,
  « بخش » pour la partie ; گفتن et آزمون شفاهی côte à côte.
- « ممتحن » ici, « ارزیاب » dans l'app telc A2·B1 : à harmoniser.
- دمانس، پروتز مفصل ران، واکر، بخش سالمندان، فرم شرح حال، « آگاه به زمان، مکان و شخص »، « کنترل ادرار و مدفوع
  دارد » : justes pour un public afghan aussi ?
- « باغچهٔ اجاره‌ای » (jardin ouvrier), « بازی ورق Skat » : une glose plus claire ?

### Arabe (ar)
- « تقرير القبول », « تقرير السيرة الحياتية » (et non « السيرة الذاتية », le CV) : usage en Syrie et en Tunisie ?
- Mois doubles « ديسمبر (كانون الأول) » ; « المشّاية », « مزرعتا دم », « المصحّة ».
- Termes de grammaire : « الماضي التام », « الـGenitiv (حالة الإضافة) », « حرف ربط », « الظرف ».
- « لا يعاني من السلس » (continent), « مدرك للزمان والمكان والأشخاص » (orienté).
- À l'écran : « وElif » (le و collé au nom latin), la règle des points réécrite en phrase.
- Impératif au masculin générique dans les consignes longues, comme `telc/langues/ar.json` ; « أنا مستعد(ة) ».

### Polonais (pl)
- Noms allemands laissés au nominatif ; à vérifier : « przy córce Herr Schulze jest… » (n21), « mierzy poziom cukru
  Frau Lehmann » (H2g2).
- Formes neutres : « Gotowe: do części ustnej », « Moja prezentacja (2A) była przeczytana, a nie wygłoszona »,
  « razem z Elif byłby powód do świętowania ».
- balkonik, edukatorka diabetologiczna, « kontroluje oddawanie moczu i stolca », endoproteza biodra, dyżurka
  pielęgniarek, medycyna pracy ; « Arkusz oceny », « Elementy językowe », « 75 ze 100 ».
