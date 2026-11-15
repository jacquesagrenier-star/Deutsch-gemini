# -*- coding: utf-8 -*-
"""Theme 12 — Patientensprache und Fachsprache (plan du 15 nov., § C 1 : « comprendre le patient,
parler au medecin »).

Des PAIRES, une seule sorte : ce que dit le patient (« das Bauchweh ») et ce que dit ou ecrit le
service (« die Abdominalschmerzen »), dans les deux sens. Constructeur P de commun.py :

  P(niveau, patient, service,
    trad_patient,  trad_service,     9 champs : fr | en | tr | uk | fa | ar | pt | pl | ru
    ex_patient,    ex_service)      10 champs : de | fr | en | tr | uk | fa | ar | pt | pl | ru

- les deux cotes s'ecrivent avec leur article, ou tels qu'on les dit (« groß machen », « Mir ist schlecht. ») ;
- la traduction du patient est dans le REGISTRE DE TOUS LES JOURS de la langue (« le mal au ventre »),
  celle du service dans le REGISTRE MEDICAL (« les douleurs abdominales ») ; si la langue n'a qu'un mot,
  on le precise entre parentheses ;
- ex_patient : ce que dit le patient, a l'oral, a la premiere personne le plus souvent ;
  ex_service : la meme chose dans la transmission, la relève ou le dossier, ou, dans l'autre sens,
  l'explication donnee au patient avec ses mots a lui ;
- relire=True sur tout terme medical (⚕️).
"""
from commun import P

THEME = {
    "cle": "sprache",
    "numero": 12,
    "nom_theme": "Patientensprache und Fachsprache",
    "titre": "comprendre le patient, parler au médecin | understanding patients, talking to doctors | hastayı anlamak, doktorla konuşmak | розуміти пацієнта, говорити з лікарем | فهمیدن بیمار، صحبت با پزشک | فهم المريض والتحدّث إلى الطبيب | entender o paciente, falar com o médico | rozumieć pacjenta, rozmawiać z lekarzem | понимать пациента, говорить с врачом",
}

MOTS = [
    P("B1", "das Bauchweh", "die Abdominalschmerzen",
      "le mal au ventre | stomach ache, tummy ache | karın ağrısı | біль у животі | دل‌درد | وجع البطن | a dor de barriga | ból brzucha | боль в животе",
      "les douleurs abdominales | abdominal pain | abdominal ağrı | абдомінальний біль | درد شکمی | آلام البطن | as dores abdominais | bóle w jamie brzusznej | абдоминальные боли",
      "Ich hab so Bauchweh, schon seit heute früh. | J'ai tellement mal au ventre, depuis ce matin. | I've got such a stomach ache, since this morning. | Sabahtan beri karnım çok ağrıyor. | У мене так болить живіт, ще з самого ранку. | از صبح دلم خیلی درد می‌کند. | بطني يوجعني كثيرًا منذ الصباح. | Estou com muita dor de barriga, desde cedo. | Strasznie boli mnie brzuch, już od rana. | У меня так болит живот, ещё с утра.",
      "{Herr Schulze} klagt seit dem Morgen über Abdominalschmerzen. | {Herr Schulze} se plaint de douleurs abdominales depuis le matin. | {Herr Schulze} has been complaining of abdominal pain since this morning. | {Herr Schulze} sabahtan beri abdominal ağrıdan yakınıyor. | {Herr Schulze} з ранку скаржиться на абдомінальний біль. | {Herr Schulze} از صبح از درد شکمی شکایت دارد. | يشكو {Herr Schulze} من آلام في البطن منذ الصباح. | {Herr Schulze} se queixa de dores abdominais desde a manhã. | {Herr Schulze} od rana skarży się na bóle w jamie brzusznej. | {Herr Schulze} с утра жалуется на абдоминальные боли.",
      relire=True, note="À l'oral, beaucoup disent simplement « Bauchschmerzen » ; « Abdominalschmerzen » est la forme écrite du dossier."),
    P("B1", "die Windel", "die Inkontinenzvorlage",
      "la couche | nappy, diaper | bez (çocuk bezi) | підгузок | پوشک | الحفّاض | a fralda | pielucha | подгузник",
      "la protection pour incontinence | incontinence pad | inkontinans pedi | урологічна прокладка | پد بی‌اختیاری | فوطة سلس البول | o absorvente para incontinência | wkład urologiczny | урологическая прокладка",
      "Ich will keine Windel, ich bin doch kein Baby! | Je ne veux pas de couche, je ne suis pas un bébé ! | I don't want a nappy, I'm not a baby! | Bez istemiyorum, ben bebek değilim ki! | Я не хочу підгузок, я ж не немовля! | پوشک نمی‌خواهم، من که بچه نیستم! | لا أريد حفّاضًا، لستُ طفلًا! | Não quero fralda, eu não sou bebê! | Nie chcę pieluchy, przecież nie jestem dzieckiem! | Я не хочу подгузник, я же не ребёнок!",
      "Wir sagen „Vorlage“, nicht „Windel“: Das Wort schützt die Würde der Bewohnerin. | On dit « protection », pas « couche » : le mot protège la dignité de la résidente. | We say “pad”, not “nappy”: the word protects the resident's dignity. | „Bez“ değil „ped“ diyoruz: bu kelime sakinin onurunu korur. | Ми кажемо «прокладка», а не «підгузок»: це слово береже гідність мешканки. | ما می‌گوییم «پد»، نه «پوشک»: این کلمه از شأن ساکن محافظت می‌کند. | نقول «فوطة» لا «حفّاض»: فالكلمة تحفظ كرامة المقيمة. | Dizemos “absorvente”, não “fralda”: a palavra preserva a dignidade da moradora. | Mówimy „wkład”, a nie „pielucha”: to słowo chroni godność mieszkanki. | Мы говорим «прокладка», а не «подгузник»: это слово бережёт достоинство жительницы."),
    P("B2", "die Wassertabletten", "die Diuretika",
      "les cachets pour éliminer l'eau | water pills | idrar söktürücü haplar | сечогінні таблетки | قرص ادرار | حبوب إدرار البول | os remédios para tirar o líquido | tabletki moczopędne | мочегонные таблетки",
      "les diurétiques | diuretics | diüretikler | діуретики | داروهای مُدِر | مدرّات البول | os diuréticos | leki moczopędne (diuretyki) | диуретики",
      "Die Wassertabletten nehme ich lieber erst nach dem Frühstück. | Les cachets pour l'eau, je préfère les prendre après le petit-déjeuner. | I'd rather take the water pills after breakfast. | İdrar söktürücü hapları kahvaltıdan sonra almayı tercih ediyorum. | Сечогінні таблетки я краще випʼю після сніданку. | قرص ادرارم را ترجیح می‌دهم بعد از صبحانه بخورم. | أفضّل أن آخذ حبوب الماء بعد الفطور. | Os remédios para tirar o líquido eu prefiro tomar depois do café da manhã. | Tabletki moczopędne wolę brać dopiero po śniadaniu. | Мочегонные таблетки я лучше выпью после завтрака.",
      "Die Diuretika werden morgens gegeben, damit der Patient nachts nicht so oft aufstehen muss. | On donne les diurétiques le matin pour que le patient n'ait pas à se lever si souvent la nuit. | Diuretics are given in the morning so that the patient doesn't have to get up so often at night. | Diüretikler sabah verilir, böylece hasta gece o kadar sık kalkmak zorunda kalmaz. | Діуретики дають зранку, щоб пацієнтові не доводилося так часто вставати вночі. | داروهای مُدِر را صبح می‌دهند تا بیمار شب‌ها مجبور نباشد زیاد بلند شود. | تُعطى مدرّات البول صباحًا حتى لا يضطر المريض إلى النهوض كثيرًا في الليل. | Os diuréticos são dados de manhã para o paciente não ter que se levantar tanto à noite. | Leki moczopędne podaje się rano, żeby pacjent nie musiał tak często wstawać w nocy. | Диуретики дают утром, чтобы пациенту не приходилось так часто вставать ночью.",
      relire=True, note="L'heure de prise suit la prescription ; le matin est l'usage courant."),
]

LECTURES = {}
