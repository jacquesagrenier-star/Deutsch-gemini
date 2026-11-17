# Le banc de « L'heure et les dates » : ce qu'il faut relire a la main

Fait par `node tests/heure_banc.js` (336 heures x 4 langues, 366 dates, l'agenda, 10 langues d'interface).

## Les cas pieges (107 / 107 justes)

- halb drei, a 2 h 30 : Es ist halb drei.
- halb drei, a 14 h 30 : Es ist halb drei.
- halb eins, a 0 h 30 : Es ist halb eins.
- halb eins, a 12 h 30 : Es ist halb eins.
- Viertel nach : Es ist Viertel nach zwei.
- Viertel vor : Es ist Viertel vor drei.
- Viertel vor eins : Es ist Viertel vor eins.
- fünf vor halb : Es ist fünf vor halb drei.
- fünf nach halb : Es ist fünf nach halb drei.
- zwanzig vor : Es ist zwanzig vor drei.
- kurz vor : Es ist kurz vor drei.
- kurz nach : Es ist kurz nach drei.
- ein Uhr : Es ist ein Uhr.
- zwölf Uhr a minuit : Es ist zwölf Uhr.
- officielle 14:30 : Es ist vierzehn Uhr dreißig.
- officielle 1:05 : Es ist ein Uhr fünf.
- officielle 21:00 : Es ist einundzwanzig Uhr.
- officielle 0:00 : Es ist null Uhr.
- officielle 23:45 : Es ist dreiundzwanzig Uhr fünfundvierzig.
- le moment, 19 h : Es ist sieben Uhr abends.
- le moment, 7 h : Es ist sieben Uhr morgens.
- es la una : Es la una.
- es la una y cuarto, 13 h 15 : Es la una y cuarto.
- es la una menos cuarto, 12 h 45 : Es la una menos cuarto.
- es la una menos cuarto, 0 h 45 : Es la una menos cuarto.
- son las dos y media : Son las dos y media.
- menos cuarto : Son las tres menos cuarto.
- menos veinticinco : Son las tres menos veinticinco.
- las doce a minuit : Son las doce.
- officielle 21:30, au feminin : Son las veintiuna treinta.
- officielle 14:05 : Son las catorce cero cinco.
- de la tarde : Son las dos y media de la tarde.
- de la mañana : Son las nueve de la mañana.
- del mediodía : Son las doce del mediodía.
- de la noche, minuit : Son las doce de la noche.
- a las / a la : a la una y media de la tarde
- 12:30 = twelve thirty p.m. : It's twelve thirty p.m.
- 0:30 = twelve thirty a.m. : It's twelve thirty a.m.
- 12:00 = noon : It's noon.
- 0:00 = midnight : It's midnight.
- 14:30 = two thirty p.m. : It's two thirty p.m.
- 6:45 numerique : It's six forty-five.
- 6:05 numerique : It's six oh five.
- 3:00 numerique : It's three o'clock.
- a quarter to (us) : It's a quarter to seven.
- quarter to (gb) : It's quarter to seven.
- half past : It's half past two.
- twenty-five past : It's twenty-five past two.
- almost (us) : It's almost three.
- nearly (gb) : It's nearly three.
- der erste Mai : Heute ist der erste Mai.
- der dritte Mai : Heute ist der dritte Mai.
- der siebte : Heute ist der siebte Juli.
- der achte : Heute ist der achte März.
- der zwanzigste (-ste) : Heute ist der zwanzigste Januar.
- der einunddreißigste : Heute ist der einunddreißigste Dezember.
- am dritten Mai (datif) : Ich habe am dritten Mai Geburtstag.
- am ersten : Ich habe am ersten Januar Geburtstag.
- el uno de mayo : Hoy es el uno de mayo.
- el tres de mayo : Hoy es el tres de mayo.
- el treinta y uno : Hoy es el treinta y uno de diciembre.
- el veintiuno : Mi cumpleaños es el veintiuno de marzo.
- May first : Today is May first.
- May third : Today is May third.
- the third of May : Today is the third of May.
- thirty-first : My birthday is on December thirty-first.
- twenty-second : twenty-second
- thirtieth : thirtieth
- 1st : 1st
- 2nd : 2nd
- 3rd : 3rd
- 11th : 11th
- 12th : 12th
- 13th : 13th
- 21st : 21st
- 22nd : 22nd
- 23rd : 23rd
- 31st : 31st
- 16 nov. 2026, lundi : 0
- 1er janv. 2027, vendredi : 4
- 29 fevr. 2028, mardi : 1
- um halb fünf nachmittags : Das Fußballtraining ist am Mittwoch um halb fünf nachmittags.
- el jueves a las diez : La cita con el médico es el jueves a las diez de la mañana.
- on Saturday at eight p.m. : The party is on Saturday at eight p.m.
- von neun bis halb elf : Von neun bis halb elf.
- de la una a las dos : De la una a las dos de la tarde.
- from eleven a.m. to one p.m. : From eleven a.m. to one p.m.
- fr : deux heures et demie : Il est deux heures et demie.
- fr : midi et quart : Il est midi et quart.
- fr : minuit et demi : Il est minuit et demi.
- fr : trois heures moins le quart : Il est trois heures moins le quart.
- fr : vingt et une heures : Il est vingt et une heures.
- fr : une heure du matin : Il est une heure du matin.
- fr : le 1er mai : Aujourd'hui, nous sommes le 1er mai.
- en : half past two : It's half past two.
- de : halb drei : Es ist halb drei.
- ru : во вторник : Во вторник в 9:00.
- pl : we wtorek : We wtorek o 9:00.
- uk : у середу : У середу о 9:00.
- tr : 9.00'da : Pazartesi saat 9.00'da.
- tr : 13.30'da : Konser saat 13.30'da başlıyor.
- tr : 20.00'de : Parti saat 20.00'de başlıyor.
- tr : 3 Mayıs'ta : Doğum günüm 3 Mayıs'ta.
- ru : была среда : Сегодня четверг. Вчера была среда.
- ru : было воскресенье : Сегодня понедельник. Вчера было воскресенье.
- pl : we wrześniu : Moje urodziny są we wrześniu.
- fa : chiffres persans : ساعت ۱۴:۳۰ است.

## Les heures charnieres, dans chaque langue et chaque lecture

### 0:00
- de : Es ist zwölf Uhr. · Es ist null Uhr. · Es ist zwölf Uhr nachts.
- es : Son las doce. · Son las cero horas. · Son las doce de la noche.
- us : It's twelve o'clock. · It's twelve o'clock. · It's midnight. · It's midnight.
- gb : It's twelve o'clock. · It's twelve o'clock. · It's midnight. · It's midnight.
- fr : Il est minuit. · Il est zéro heure. · Il est minuit.

### 0:30
- de : Es ist halb eins. · Es ist null Uhr dreißig. · Es ist halb eins nachts.
- es : Son las doce y media. · Son las cero treinta. · Son las doce y media de la noche.
- us : It's half past twelve. · It's twelve thirty. · It's twelve thirty a.m. · It's twelve thirty at night.
- gb : It's half past twelve. · It's twelve thirty. · It's twelve thirty a.m. · It's twelve thirty at night.
- fr : Il est minuit et demi. · Il est zéro heure trente. · Il est minuit et demi.

### 0:45
- de : Es ist Viertel vor eins. · Es ist null Uhr fünfundvierzig. · Es ist Viertel vor eins nachts.
- es : Es la una menos cuarto. · Son las cero cuarenta y cinco. · Es la una menos cuarto de la noche.
- us : It's a quarter to one. · It's twelve forty-five. · It's twelve forty-five a.m. · It's twelve forty-five at night.
- gb : It's quarter to one. · It's twelve forty-five. · It's twelve forty-five a.m. · It's twelve forty-five at night.
- fr : Il est une heure moins le quart. · Il est zéro heure quarante-cinq. · Il est une heure moins le quart.

### 1:00
- de : Es ist ein Uhr. · Es ist ein Uhr. · Es ist ein Uhr nachts.
- es : Es la una. · Es la una. · Es la una de la madrugada.
- us : It's one o'clock. · It's one o'clock. · It's one a.m. · It's one in the morning.
- gb : It's one o'clock. · It's one o'clock. · It's one a.m. · It's one in the morning.
- fr : Il est une heure. · Il est une heure. · Il est une heure du matin.

### 1:30
- de : Es ist halb zwei. · Es ist ein Uhr dreißig. · Es ist halb zwei nachts.
- es : Es la una y media. · Es la una treinta. · Es la una y media de la madrugada.
- us : It's half past one. · It's one thirty. · It's one thirty a.m. · It's one thirty in the morning.
- gb : It's half past one. · It's one thirty. · It's one thirty a.m. · It's one thirty in the morning.
- fr : Il est une heure et demie. · Il est une heure trente. · Il est une heure et demie du matin.

### 11:45
- de : Es ist Viertel vor zwölf. · Es ist elf Uhr fünfundvierzig. · Es ist Viertel vor zwölf vormittags.
- es : Son las doce menos cuarto. · Son las once cuarenta y cinco. · Son las doce menos cuarto de la mañana.
- us : It's a quarter to twelve. · It's eleven forty-five. · It's eleven forty-five a.m. · It's eleven forty-five in the morning.
- gb : It's quarter to twelve. · It's eleven forty-five. · It's eleven forty-five a.m. · It's eleven forty-five in the morning.
- fr : Il est midi moins le quart. · Il est onze heures quarante-cinq. · Il est midi moins le quart.

### 12:00
- de : Es ist zwölf Uhr. · Es ist zwölf Uhr. · Es ist zwölf Uhr mittags.
- es : Son las doce. · Son las doce horas. · Son las doce del mediodía.
- us : It's twelve o'clock. · It's twelve o'clock. · It's noon. · It's noon.
- gb : It's twelve o'clock. · It's twelve o'clock. · It's noon. · It's noon.
- fr : Il est midi. · Il est douze heures. · Il est midi.

### 12:15
- de : Es ist Viertel nach zwölf. · Es ist zwölf Uhr fünfzehn. · Es ist Viertel nach zwölf mittags.
- es : Son las doce y cuarto. · Son las doce quince. · Son las doce y cuarto del mediodía.
- us : It's a quarter past twelve. · It's twelve fifteen. · It's twelve fifteen p.m. · It's twelve fifteen in the afternoon.
- gb : It's quarter past twelve. · It's twelve fifteen. · It's twelve fifteen p.m. · It's twelve fifteen in the afternoon.
- fr : Il est midi et quart. · Il est douze heures quinze. · Il est midi et quart.

### 12:30
- de : Es ist halb eins. · Es ist zwölf Uhr dreißig. · Es ist halb eins mittags.
- es : Son las doce y media. · Son las doce treinta. · Son las doce y media del mediodía.
- us : It's half past twelve. · It's twelve thirty. · It's twelve thirty p.m. · It's twelve thirty in the afternoon.
- gb : It's half past twelve. · It's twelve thirty. · It's twelve thirty p.m. · It's twelve thirty in the afternoon.
- fr : Il est midi et demi. · Il est douze heures trente. · Il est midi et demi.

### 12:45
- de : Es ist Viertel vor eins. · Es ist zwölf Uhr fünfundvierzig. · Es ist Viertel vor eins mittags.
- es : Es la una menos cuarto. · Son las doce cuarenta y cinco. · Es la una menos cuarto del mediodía.
- us : It's a quarter to one. · It's twelve forty-five. · It's twelve forty-five p.m. · It's twelve forty-five in the afternoon.
- gb : It's quarter to one. · It's twelve forty-five. · It's twelve forty-five p.m. · It's twelve forty-five in the afternoon.
- fr : Il est une heure moins le quart. · Il est douze heures quarante-cinq. · Il est une heure moins le quart.

### 13:00
- de : Es ist ein Uhr. · Es ist dreizehn Uhr. · Es ist ein Uhr mittags.
- es : Es la una. · Son las trece horas. · Es la una de la tarde.
- us : It's one o'clock. · It's one o'clock. · It's one p.m. · It's one in the afternoon.
- gb : It's one o'clock. · It's one o'clock. · It's one p.m. · It's one in the afternoon.
- fr : Il est une heure. · Il est treize heures. · Il est une heure de l'après-midi.

### 14:30
- de : Es ist halb drei. · Es ist vierzehn Uhr dreißig. · Es ist halb drei nachmittags.
- es : Son las dos y media. · Son las catorce treinta. · Son las dos y media de la tarde.
- us : It's half past two. · It's two thirty. · It's two thirty p.m. · It's two thirty in the afternoon.
- gb : It's half past two. · It's two thirty. · It's two thirty p.m. · It's two thirty in the afternoon.
- fr : Il est deux heures et demie. · Il est quatorze heures trente. · Il est deux heures et demie de l'après-midi.

### 18:45
- de : Es ist Viertel vor sieben. · Es ist achtzehn Uhr fünfundvierzig. · Es ist Viertel vor sieben abends.
- es : Son las siete menos cuarto. · Son las dieciocho cuarenta y cinco. · Son las siete menos cuarto de la tarde.
- us : It's a quarter to seven. · It's six forty-five. · It's six forty-five p.m. · It's six forty-five in the evening.
- gb : It's quarter to seven. · It's six forty-five. · It's six forty-five p.m. · It's six forty-five in the evening.
- fr : Il est sept heures moins le quart. · Il est dix-huit heures quarante-cinq. · Il est sept heures moins le quart de l'après-midi.

### 23:30
- de : Es ist halb zwölf. · Es ist dreiundzwanzig Uhr dreißig. · Es ist halb zwölf nachts.
- es : Son las once y media. · Son las veintitrés treinta. · Son las once y media de la noche.
- us : It's half past eleven. · It's eleven thirty. · It's eleven thirty p.m. · It's eleven thirty at night.
- gb : It's half past eleven. · It's eleven thirty. · It's eleven thirty p.m. · It's eleven thirty at night.
- fr : Il est onze heures et demie. · Il est vingt-trois heures trente. · Il est onze heures et demie du soir.

### 23:58
- de : Es ist kurz vor zwölf. · Es ist dreiundzwanzig Uhr achtundfünfzig. · Es ist kurz vor zwölf nachts.
- es : Son las doce menos dos. · Son las veintitrés cincuenta y ocho. · Son las doce menos dos de la noche.
- us : It's almost twelve. · It's eleven fifty-eight. · It's eleven fifty-eight p.m. · It's eleven fifty-eight at night.
- gb : It's nearly twelve. · It's eleven fifty-eight. · It's eleven fifty-eight p.m. · It's eleven fifty-eight at night.
- fr : Il est minuit moins deux. · Il est vingt-trois heures cinquante-huit. · Il est minuit moins deux.

## Les dates charnieres

- 1/1 : Heute ist der erste Januar. · Hoy es el uno de enero. · Today is January first. · Today is the first of January. · Ich habe am ersten Januar Geburtstag. · Mi cumpleaños es el uno de enero. · My birthday is on January first. · My birthday is on the first of January.
- 28/2 : Heute ist der achtundzwanzigste Februar. · Hoy es el veintiocho de febrero. · Today is February twenty-eighth. · Today is the twenty-eighth of February. · Ich habe am achtundzwanzigsten Februar Geburtstag. · Mi cumpleaños es el veintiocho de febrero. · My birthday is on February twenty-eighth. · My birthday is on the twenty-eighth of February.
- 1/3 : Heute ist der erste März. · Hoy es el uno de marzo. · Today is March first. · Today is the first of March. · Ich habe am ersten März Geburtstag. · Mi cumpleaños es el uno de marzo. · My birthday is on March first. · My birthday is on the first of March.
- 3/5 : Heute ist der dritte Mai. · Hoy es el tres de mayo. · Today is May third. · Today is the third of May. · Ich habe am dritten Mai Geburtstag. · Mi cumpleaños es el tres de mayo. · My birthday is on May third. · My birthday is on the third of May.
- 7/7 : Heute ist der siebte Juli. · Hoy es el siete de julio. · Today is July seventh. · Today is the seventh of July. · Ich habe am siebten Juli Geburtstag. · Mi cumpleaños es el siete de julio. · My birthday is on July seventh. · My birthday is on the seventh of July.
- 8/8 : Heute ist der achte August. · Hoy es el ocho de agosto. · Today is August eighth. · Today is the eighth of August. · Ich habe am achten August Geburtstag. · Mi cumpleaños es el ocho de agosto. · My birthday is on August eighth. · My birthday is on the eighth of August.
- 21/9 : Heute ist der einundzwanzigste September. · Hoy es el veintiuno de septiembre. · Today is September twenty-first. · Today is the twenty-first of September. · Ich habe am einundzwanzigsten September Geburtstag. · Mi cumpleaños es el veintiuno de septiembre. · My birthday is on September twenty-first. · My birthday is on the twenty-first of September.
- 22/11 : Heute ist der zweiundzwanzigste November. · Hoy es el veintidós de noviembre. · Today is November twenty-second. · Today is the twenty-second of November. · Ich habe am zweiundzwanzigsten November Geburtstag. · Mi cumpleaños es el veintidós de noviembre. · My birthday is on November twenty-second. · My birthday is on the twenty-second of November.
- 23/12 : Heute ist der dreiundzwanzigste Dezember. · Hoy es el veintitrés de diciembre. · Today is December twenty-third. · Today is the twenty-third of December. · Ich habe am dreiundzwanzigsten Dezember Geburtstag. · Mi cumpleaños es el veintitrés de diciembre. · My birthday is on December twenty-third. · My birthday is on the twenty-third of December.
- 31/12 : Heute ist der einunddreißigste Dezember. · Hoy es el treinta y uno de diciembre. · Today is December thirty-first. · Today is the thirty-first of December. · Ich habe am einunddreißigsten Dezember Geburtstag. · Mi cumpleaños es el treinta y uno de diciembre. · My birthday is on December thirty-first. · My birthday is on the thirty-first of December.
