# Les pages du telc dans sept langues : ce qu'un locuteur natif devrait relire

7 nov. 2026. Les pages de préparation au telc Deutsch A2·B1 (`visuel/prototype/telc/`) sont écrites en français et en
anglais. Elles ont été traduites depuis l'anglais, avec le français pour le sens, dans les sept autres langues
d'interface de l'allemand : 1 165 textes par langue, environ 81 000 caractères. Il n'y a pas encore eu de relecture
native.

- Les traductions sont dans `visuel/prototype/telc/langues/<langue>.json`, un objet { texte anglais : traduction }.
  On corrige le `.json`, puis `node visuel/prototype/telc/outils/langues.js construire <langue>` refait le `.js`.
- Le contrôle est `node tests/telc_langues.js` : rien ne manque, et les variables {n} et les balises sont intactes.
  Il ne juge pas la langue.
- L'allemand de l'examen n'est pas traduit : textes, mots cités, noms des parties, formules.

Vérifications déjà faites par la session des examens :

- le contrôle passe pour les 7 langues ;
- l'affichage a été essayé dans le navigateur, en tr, ru, pt et pl, sans reste de français ;
- le persan et l'arabe ont été vérifiés à l'écran, au format téléphone ;
- le portugais suit bien le **Brésil** : « você » partout, ônibus, celular, trem, et aucune forme du Portugal
  (autocarro, comboio, telemóvel, « estar a » + infinitif).

## Ce qui vaut pour plusieurs langues

1. **Le genre de l'élève** (pl, ar, pt, ru, uk). Le passé adressé à l'élève est au masculin (« Wybrałeś », « Jestem
   gotowy », « Estou pronto »). Les réponses modèles suivent le genre du français : vendeuse, puis infirmier, puis
   « je suis marié ». Faut-il des tournures neutres ou les deux formes ?
2. **Le vouvoiement d'Anna**, l'examinatrice, comme le Sie allemand. Le tutoiement de Mark, un ami, comme en français.
   À confirmer selon la langue : « Pan / Pani » est lourd en pl ; faut-il « حضرتك » ou le pluriel de politesse en ar
   pour un public syrien ?
3. **Les pluriels après un nombre** (uk, ru, pl, ar, fa). Pour rester juste avec n'importe quel nombre, les phrases
   ont été tournées en « Слов: {n} », « Liczba słów: {n} », « عدد الأسئلة: {n} ». C'est correct, mais un peu
   administratif. Restent en uk quelques « {n} питань », faux pour 1 et pour 2 à 4.
4. **Les noms des personnages secondaires**, translittérés en ar, fa, ru et uk (Mme Özdemir, M. Kaya, Frau Brandt…).
   Faut-il les garder en caractères latins, pour que l'élève les reconnaisse à l'écoute ?
5. **Les cas grammaticaux** (Akkusativ, Dativ…) sont laissés en allemand au milieu de la phrase. Ça peut se lire
   lourdement, surtout en ar.

## Langue par langue

### Turc (tr)
- Civilités : « Özdemir Hanım », « Kaya Bey », « Bay Garnier ».
- Termes : « hitap » (formule d'appel), « kapanış » (salutation finale), « hitap biçimi » (le registre du / Sie),
  « cevap anahtarı » (le corrigé), « deneme sınavı » (l'examen blanc). Un enseignant pourrait préférer « selamlama »,
  « üslup » ou « çözümler ».
- Certaines fins de phrase à compléter (« Hastalar reçetelerini… » + « Dr. Kaya’dan almalı. ») sont un peu raides en
  turc.
- Libellés avec la variable en fin de phrase, pour éviter un suffixe collé à la variable : « Örnek cevap {n} »,
  « … {f} / {f}. »

### Ukrainien (uk)
- « Пане Гарньє », « Марк Гарньє ».
- « Читання й письмо », « Слухання й нотатки » ; « лист » pour un courriel ; « звертання / прощальна формула ».
- « пробний іспит » (examen blanc), « Здати роботу » (rendre la copie).

### Persan (fa)
- L'oral : « گفتن » (comme dans l'app) ; « صحبت کردن » serait peut-être plus naturel.
- Termes : « ممتحن » (examinateur), « داوطلب » (candidat), « آزمون آزمایشی » (examen blanc), « جدول ارزیابی »
  (grille), « معیار » (critère). L'usage peut différer entre l'Iran et l'Afghanistan.
- Grammaire : « فعل جداشدنی » (verbe séparable), « جملهٔ وابسته » (subordonnée), « واژهٔ ربط » (connecteur).
- Le ton familier de Mark (« باشه », « هوم ») convient-il à un public afghan autant qu'iranien ?

### Arabe (ar)
- « امتحان تجريبي » (examen blanc), « تسليم الورقة » (rendre la copie), « التحية / الختام » (formules),
  « مستوى الخطاب » (le registre du / Sie), « الصحة اللغوية », « تنوّع اللغة » (critères).
- Quelques marques de direction invisibles (RLM) devant un mot allemand en début de proposition.

### Portugais du Brésil (pt)
- « secretária eletrônica » pour le répondeur : c'est la forme brésilienne, à garder (le chef, 7 nov.).
- « república » pour la colocation de Mark (WG) évoque plutôt une colocation d'étudiants.
- Le ton familier de Mark (« a gente », « Tá bom »).
- « Kiste » → « canteiro », « Keller » → « depósito no porão ».

### Polonais (pl)
- Les termes d'examen : « zasób środków językowych » (étendue de la langue), « forma » (le registre du / Sie),
  « Tabela » (la grille), « karta odpowiedzi » (la feuille de réponses). À comparer avec les termes officiels de telc
  en polonais.
- « Volkshochschule » → « uniwersytet ludowy ».

### Russe (ru)
- « Письмо » désigne à la fois l'épreuve d'écriture (comme dans l'app) et une lettre. « электронное письмо » a été
  mis là où c'était ambigu, mais « Раздел · Письмо » à côté de « письмо » peut gêner.
- « заключительная формула », « обращение », « стиль обращения », « таблица критериев ».
- Les phrases à compléter : chaque fin se raccorde-t-elle bien à son amorce ?
- Les institutions : « центр образования для взрослых (Volkshochschule) », « профессиональное училище », « квартира
  на несколько жильцов » (WG).

## Deux défauts d'affichage, en persan et en arabe

1. **La flèche du bouton retour « ‹ »** pointe vers la gauche, même en écriture de droite à gauche. Le bouton est bien
   placé à droite, mais il faudrait « › ». Le bouton vient de `visuel/prototype/dtz/commun.css` et `dtz.html`, communs
   avec le DTZ, et de `oral.html`.
2. **Les sous-titres qui mêlent allemand et persan** (« Lesen · 4 بخش · 45 دقیقه ») s'enchaînent dans un ordre peu
   naturel : l'algorithme bidirectionnel place le mot allemand du mauvais côté. Remède : isoler l'allemand dans un
   `<bdi>` ou un `<span dir="ltr">` là où ces sous-titres sont construits (les tuiles de l'accueil de commun.js, les
   en-têtes des parties).
