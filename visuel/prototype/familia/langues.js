// LA FAMILLE D'ANNA DANS LES SIX AUTRES LANGUES D'INTERFACE : turc, ukrainien, polonais, russe, persan, arabe
// (ligne 111, lot 2 de l'alignement des langues des themes, 15 nov. 2026 ; les captures Google Play montraient la
// glose seule sous la phrase d'Anna dans ces langues).
//
// LE CHEMIN NATIF : la page fabrique la phrase allemande (ou espagnole) avec ses morceaux ; on fabrique la traduction
// avec les MEMES choix (les memes personnes, le meme lien, le meme possessif, le meme groupe), comme TRADS.fr / en / pt
// dans familia.html. Ce fichier ajoute TRADS.tr, uk, pl, ru, fa, ar, avec la meme interface (rel, lien, possN,
// estPoss, estPossQ, estPoss3, groupe, lienPl, sontPoss, dit, disent, demande, combien, paire, soi, age, et).
//
// LE MOT JUSTE SELON L'ARBRE. Le francais dit « l'oncle » ; le turc, le persan et l'arabe disent de quel cote
// (amca / dayi, emu / dayi, 'amm / khal), et pour un oncle par alliance « le mari de la tante » (enishte, shohar-'ammeh,
// zawj al-'amma). Le russe et l'ukrainien distinguent le beau-pere de la femme et celui du mari (svekor / test'), et
// cinq beaux-freres et belles-soeurs. On ne les devine pas : lienFin(e, o) lit l'arbre (par quel parent passe le lien,
// le sexe du frere ou de la soeur) et chaque langue choisit son mot. Sans personne (les paires, « der Onkel → die
// Tante »), le mot general du corpus.
//
// Les noms : en cyrillique et declines en russe et en ukrainien (Анны, Анни), declines en polonais (Anny, Annę),
// avec le suffixe du turc (Anna'nın, Ben'e), en ecriture persane et arabe. Points a relire par un natif :
// retours/A-RELIRE-THEMES-<LG>.md.
function installerLanguesFamille(TRADS){

// ---------- l'arbre : le lien precis de o pour e ----------
function lienFin(e, o, k){
  if (Array.isArray(e) || relation(e, o) !== k) return {k, so: sexe(o)};
  const d = {k, so: sexe(o), se: sexe(e), precis: true};
  if (k === "grandparent"){ const p = parents(e).find(p => parents(p).includes(o)); d.cote = p ? sexe(p) : null; }
  else if (k === "oncle"){
    const p = parents(e).find(p => freres(p).includes(o) || (conjoint(o) && freres(p).includes(conjoint(o))));
    d.cote = p ? sexe(p) : null; d.alliance = p ? !freres(p).includes(o) : false;
  } else if (k === "neveu"){
    const q = parents(o).find(q => freres(e).includes(q) || (conjoint(e) && freres(conjoint(e)).includes(q)));
    d.par = q ? sexe(q) : null; d.alliance = q ? !freres(e).includes(q) : false;
  } else if (k === "cousin"){
    parents(e).forEach(pe => parents(o).forEach(po => { if (freres(pe).includes(po)){ d.cote = sexe(pe); d.par = sexe(po); } }));
  } else if (k === "beaufrere"){
    const s = freres(e).find(s => conjoint(s) === o);
    if (s){ d.via = "fratrie"; d.par = sexe(s); } else { d.via = "conjoint"; d.par = conjoint(e) ? sexe(conjoint(e)) : null; }
  }
  return d;
}
// les membres d'un groupe, regroupes par mot (dans l'ordre de l'arbre) : [{w, n}]
function parMot(langue, owner, g, k){
  const out = [];
  g.forEach(x => { const w = langue.mot(lienFin(owner, x, k)); const t = out.find(y => y.w.cle === w.cle); if (t) t.n++; else out.push({w, n: 1}); });
  return out;
}
const etListe = (a, et) => a.length > 1 ? a.slice(0, -1).join(", ") + et + a[a.length - 1] : a[0];

// les jetons : la page compose rel / possN / estPoss / groupe avant de savoir qui parle ; on rend la phrase a la fin
function jetons(L){
  return Object.assign(L, {
    rel: (k, s) => ({k, s}),
    possN: (forme, k, s) => ({forme, k, s}),
    estPoss: (o, pn) => ({t: "est", o, pn}),
    estPossQ: (o, pn) => ({t: "estQ", o, pn}),
    groupe: (k, g, forme) => ({k, g, forme}),
    sontPoss: (g, grp) => ({t: "sont", g, grp}),
    et: a => a
  });
}

// =====================================================================================================================
// LE RUSSE
// =====================================================================================================================
const RU_NOMS = {Heinz:["Хайнц","Хайнца","Хайнца"], Gisela:["Гизела","Гизелы","Гизелу"], Peter:["Петер","Петера","Петера"],
  Monika:["Моника","Моники","Монику"], Sabine:["Сабина","Сабины","Сабину"], Frank:["Франк","Франка","Франка"], Jan:["Ян","Яна","Яна"],
  Katrin:["Катрин","Катрин","Катрин"], Anna:["Анна","Анны","Анну"], Lena:["Лена","Лены","Лену"], Felix:["Феликс","Феликса","Феликса"],
  Sophie:["Софи","Софи","Софи"], Ben:["Бен","Бена","Бена"], Mia:["Мия","Мии","Мию"]};
// [nominatif, pluriel, apres 2-4, apres 5, genre]
const RU_M = (n, p, g2, g5, gr) => ({cle: n, n, p, g2, g5, gr});
const RU = {
  pere: RU_M("отец","отцы","отца","отцов","m"), mere: RU_M("мать","матери","матери","матерей","f"),
  fils: RU_M("сын","сыновья","сына","сыновей","m"), fille: RU_M("дочь","дочери","дочери","дочерей","f"),
  mari: RU_M("муж","мужья","мужа","мужей","m"), femme: RU_M("жена","жёны","жены","жён","f"),
  frere: RU_M("брат","братья","брата","братьев","m"), soeur: RU_M("сестра","сёстры","сестры","сестёр","f"),
  gp: RU_M("дедушка","дедушки","дедушки","дедушек","m"), gm: RU_M("бабушка","бабушки","бабушки","бабушек","f"),
  pf: RU_M("внук","внуки","внука","внуков","m"), pfl: RU_M("внучка","внучки","внучки","внучек","f"),
  oncle: RU_M("дядя","дяди","дяди","дядей","m"), tante: RU_M("тётя","тёти","тёти","тёть","f"),
  neveu: RU_M("племянник","племянники","племянника","племянников","m"), niece: RU_M("племянница","племянницы","племянницы","племянниц","f"),
  cousin: RU_M("двоюродный брат","двоюродные братья","двоюродных брата","двоюродных братьев","m"),
  cousine: RU_M("двоюродная сестра","двоюродные сёстры","двоюродные сестры","двоюродных сестёр","f"),
  svekor: RU_M("свёкор","свёкры","свёкра","свёкров","m"), svekrov: RU_M("свекровь","свекрови","свекрови","свекровей","f"),
  test: RU_M("тесть","тести","тестя","тестей","m"), tesha: RU_M("тёща","тёщи","тёщи","тёщ","f"),
  zyat: RU_M("зять","зятья","зятя","зятьёв","m"), nevestka: RU_M("невестка","невестки","невестки","невесток","f"),
  shurin: RU_M("шурин","шурья","шурина","шурьёв","m"), dever: RU_M("деверь","девери","деверя","деверей","m"),
  zolovka: RU_M("золовка","золовки","золовки","золовок","f"), svoyachenitsa: RU_M("свояченица","свояченицы","свояченицы","свояченец","f"),
  // sans personne : le mot general (les paires)
  g_bp: RU_M("тесть, свёкор","","","","m"), g_bm: RU_M("тёща, свекровь","","","","f"),
  g_bf: RU_M("шурин, деверь, зять","","","","m"), g_bs: RU_M("золовка, свояченица, невестка","","","","f")
};
function motRu(T, d){
  const f = d.so === "f";
  switch (d.k){
    case "parent": return f ? T.mere : T.pere;
    case "enfant": return f ? T.fille : T.fils;
    case "conjoint": return f ? T.femme : T.mari;
    case "frere": return f ? T.soeur : T.frere;
    case "grandparent": return f ? T.gm : T.gp;
    case "petitenfant": return f ? T.pfl : T.pf;
    case "oncle": return f ? T.tante : T.oncle;
    case "neveu": return f ? T.niece : T.neveu;
    case "cousin": return f ? T.cousine : T.cousin;
    case "beauparent": return !d.precis ? (f ? T.g_bm : T.g_bp) : d.se === "f" ? (f ? T.svekrov : T.svekor) : (f ? T.tesha : T.test);
    case "gendre": return f ? T.nevestka : T.zyat;
    case "beaufrere":
      if (!d.precis) return f ? T.g_bs : T.g_bf;
      if (d.via === "fratrie") return f ? T.nevestka : T.zyat;                 // la femme du frere, le mari de la soeur
      return f ? (d.par === "m" ? T.zolovka : T.svoyachenitsa) : (d.par === "f" ? T.shurin : T.dever);
  }
}
const RU_POSS = {je: ["мой","моя","мои"], tu: ["твой","твоя","твои"], nous: ["наш","наша","наши"]};
// les langues slaves de l'est : russe et ukrainien ont la meme phrase (« Петер — отец Анны »)
function slaveEst(o){
  const L = jetons({
    mot: d => o.mot(o.T, d),
    N: (x, c) => (o.noms[x] || [x, x, x])[c || 0],
    etN(a){ return etListe(a.map(x => L.N(x)), " " + o.et + " "); },
    // la liste des mots d'un groupe : « брат и сестра », « сёстры »
    liste(parts, poss){
      if (parts.length === 1 && parts[0].n > 1) return (poss ? poss[2] + " " : "") + parts[0].w.p;
      const mots = parts.map(x => x.n > 1 ? x.w.p : x.w.n);
      return (poss ? poss[2] + " " : "") + etListe(mots, " " + o.et + " ");
    },
    groupeDe(owner, g, k){ return k === "parent" ? null : parMot(L, owner, g, k); },
    rendu(tok, owner){
      if (tok.t === "sont"){
        const k = tok.grp.k, poss = o.poss[tok.grp.forme || "je"];
        return L.etN(tok.g) + " — " + (k === "parent" ? poss[2] + " " + o.parents : L.liste(parMot(L, owner, tok.g, k), poss));
      }
      const w = L.mot(lienFin(owner, tok.o, tok.pn.k)), p = o.poss[tok.pn.forme][w.gr === "f" ? 1 : 0];
      return L.N(tok.o) + " — " + p + " " + w.n + (tok.t === "estQ" ? "?" : "");
    },
    cite: s => "«" + s + "»" + (/[?!]$/.test(s) ? "" : "."),
    lien(oo, r, e){ return L.N(oo) + " — " + L.mot(lienFin(e, oo, r.k)).n + " " + (Array.isArray(e) ? etListe(e.map(x => L.N(x, 1)), " " + o.et + " ") : L.N(e, 1)) + "."; },
    lienPl(g, grp, e){ return L.etN(g) + " — " + (grp.k === "parent" ? o.parents : L.liste(parMot(L, e, g, grp.k))) + " " + L.N(e, 1) + "."; },
    dit: (s, tok) => L.N(s) + " " + o.dit + ": " + L.cite(L.rendu(tok, s)),
    disent: (a, b, tok) => L.N(a) + " " + o.et + " " + L.N(b) + " " + o.disent + ": " + L.cite(L.rendu(tok, a)),
    demande: (s, a, tok) => L.N(s) + " " + o.demande + " " + L.N(a, 2) + ": " + L.cite(L.rendu(tok, a)),
    estPoss3(oo, k, so, sp, e){ return L.N(oo) + " — " + o.poss3[sp === "f" ? 1 : 0] + " " + L.mot(e ? lienFin(e, oo, k) : {k, so}).n + "."; },
    compte(parts){
      return etListe(parts.map(x => x.n === 1 ? x.w.n : o.nombre(x.n, x.w.gr) + " " + (x.n < 5 ? x.w.g2 : x.w.g5)), " " + o.et + " ");
    },
    combien: {},
    paire: (k, s1, s2) => L.mot({k, so: s1}).n + " → " + L.mot({k, so: s2}).n,
    soi: (oo, age) => o.voici + " " + L.N(oo) + ". " + o.age(oo, age),
    age: (oo, age) => o.age(oo, age)
  });
  ["frere", "cousin", "neveu", "oncle"].forEach(k => { L.combien[k] = e => ["", g => (typeof o.chez === "function" ? o.chez(L.N(e, 1)) : o.chez + " " + L.N(e, 1)) + " " + L.compte(parMot(L, e, g, k)) + "."]; });
  L.combien.enfantCouple = (a, b) => ["", g => o.chezEux + " " + L.compte(parMot(L, a, g, "enfant")) + "."];
  L.combien.petitCouple = (a, b) => ["", g => o.chezEux + " " + L.compte(parMot(L, a, g, "petitenfant")) + "."];
  return L;
}
const ansRu = n => { const d = n % 10, c = n % 100; return (c >= 11 && c <= 14) ? "лет" : d === 1 ? "год" : (d >= 2 && d <= 4) ? "года" : "лет"; };
TRADS.ru = slaveEst({
  T: RU, mot: motRu, noms: RU_NOMS, et: "и", poss: RU_POSS, poss3: ["его", "её"], parents: "родители",
  dit: "говорит", disent: "говорят", demande: "спрашивает", chez: "У", chezEux: "У них",
  nombre: (n, gr) => n === 2 ? (gr === "f" ? "две" : "два") : ["", "", "", "три", "четыре", "пять"][n],
  voici: "Это", age: (x, a) => (sexe(x) === "f" ? "Ей" : "Ему") + " " + a + " " + ansRu(a) + "."
});

// =====================================================================================================================
// L'UKRAINIEN (l'apostrophe ukrainienne : ʼ, U+02BC)
// =====================================================================================================================
const UK_NOMS = {Heinz:["Гайнц","Гайнца","Гайнца"], Gisela:["Гізела","Гізели","Гізелу"], Peter:["Петер","Петера","Петера"],
  Monika:["Моніка","Моніки","Моніку"], Sabine:["Сабіна","Сабіни","Сабіну"], Frank:["Франк","Франка","Франка"], Jan:["Ян","Яна","Яна"],
  Katrin:["Катрін","Катрін","Катрін"], Anna:["Анна","Анни","Анну"], Lena:["Лена","Лени","Лену"], Felix:["Фелікс","Фелікса","Фелікса"],
  Sophie:["Софі","Софі","Софі"], Ben:["Бен","Бена","Бена"], Mia:["Мія","Мії","Мію"]};
// [nominatif, pluriel, apres 2-4 (le nominatif pluriel), apres 5, genre]
const UK = {
  pere: RU_M("батько","батьки","батьки","батьків","m"), mere: RU_M("мати","матері","матері","матерів","f"),
  fils: RU_M("син","сини","сини","синів","m"), fille: RU_M("дочка","дочки","дочки","дочок","f"),
  mari: RU_M("чоловік","чоловіки","чоловіки","чоловіків","m"), femme: RU_M("дружина","дружини","дружини","дружин","f"),
  frere: RU_M("брат","брати","брати","братів","m"), soeur: RU_M("сестра","сестри","сестри","сестер","f"),
  gp: RU_M("дідусь","дідусі","дідусі","дідусів","m"), gm: RU_M("бабуся","бабусі","бабусі","бабусь","f"),
  pf: RU_M("онук","онуки","онуки","онуків","m"), pfl: RU_M("онучка","онучки","онучки","онучок","f"),
  oncle: RU_M("дядько","дядьки","дядьки","дядьків","m"), tante: RU_M("тітка","тітки","тітки","тіток","f"),
  neveu: RU_M("племінник","племінники","племінники","племінників","m"), niece: RU_M("племінниця","племінниці","племінниці","племінниць","f"),
  cousin: RU_M("двоюрідний брат","двоюрідні брати","двоюрідні брати","двоюрідних братів","m"),
  cousine: RU_M("двоюрідна сестра","двоюрідні сестри","двоюрідні сестри","двоюрідних сестер","f"),
  svekor: RU_M("свекор","свекри","свекри","свекрів","m"), svekrov: RU_M("свекруха","свекрухи","свекрухи","свекрух","f"),
  test: RU_M("тесть","тесті","тесті","тестів","m"), tesha: RU_M("теща","тещі","тещі","тещ","f"),
  zyat: RU_M("зять","зяті","зяті","зятів","m"), nevestka: RU_M("невістка","невістки","невістки","невісток","f"),
  shurin: RU_M("шурин","шурини","шурини","шуринів","m"), dever: RU_M("дівер","дівери","дівери","діверів","m"),
  zolovka: RU_M("зовиця","зовиці","зовиці","зовиць","f"), svoyachenitsa: RU_M("своячка","своячки","своячки","своячок","f"),
  g_bp: RU_M("тесть, свекор","","","","m"), g_bm: RU_M("теща, свекруха","","","","f"),
  g_bf: RU_M("шурин, дівер, зять","","","","m"), g_bs: RU_M("зовиця, своячка, невістка","","","","f")
};
const ansUk = n => { const d = n % 10, c = n % 100; return (c >= 11 && c <= 14) ? "років" : d === 1 ? "рік" : (d >= 2 && d <= 4) ? "роки" : "років"; };
TRADS.uk = slaveEst({
  T: UK, mot: motRu, noms: UK_NOMS, et: "і", poss: {je: ["мій","моя","мої"], tu: ["твій","твоя","твої"], nous: ["наш","наша","наші"]},
  poss3: ["його", "її"], parents: "батьки", dit: "каже", disent: "кажуть", demande: "питає", chezEux: "У них",
  // « В Анни » : en debut de phrase, « в » devant une voyelle, « у » devant une consonne
  chez: nom => (/^[АЕЄИІЇОУ]/.test(nom) ? "В " : "У ") + nom,
  nombre: (n, gr) => n === 2 ? (gr === "f" ? "дві" : "два") : ["", "", "", "три", "чотири", "пʼять"][n],
  voici: "Це", age: (x, a) => (sexe(x) === "f" ? "Їй" : "Йому") + " " + a + " " + ansUk(a) + "."
});

// =====================================================================================================================
// LE POLONAIS : « Peter jest ojcem Anny » (byc + instrumental), « Anna ma brata i siostrę »
// =====================================================================================================================
const PL_NOMS = {Heinz:["Heinz","Heinza","Heinza"], Gisela:["Gisela","Giseli","Giselę"], Peter:["Peter","Petera","Petera"],
  Monika:["Monika","Moniki","Monikę"], Sabine:["Sabine","Sabine","Sabine"], Frank:["Frank","Franka","Franka"], Jan:["Jan","Jana","Jana"],
  Katrin:["Katrin","Katrin","Katrin"], Anna:["Anna","Anny","Annę"], Lena:["Lena","Leny","Lenę"], Felix:["Felix","Felixa","Felixa"],
  Sophie:["Sophie","Sophie","Sophie"], Ben:["Ben","Bena","Bena"], Mia:["Mia","Mii","Mię"]};
// [nominatif, instrumental, accusatif, instrumental pluriel, apres 2-4, apres 5, genre : mp (homme) ou f]
const PL_M = (n, i, a, ip, n2, n5, gr) => ({cle: n, n, i, a, ip, n2, n5, gr});
const PL = {
  pere: PL_M("ojciec","ojcem","ojca","ojcami","ojców","ojców","mp"), mere: PL_M("matka","matką","matkę","matkami","matki","matek","f"),
  fils: PL_M("syn","synem","syna","synami","synów","synów","mp"), fille: PL_M("córka","córką","córkę","córkami","córki","córek","f"),
  mari: PL_M("mąż","mężem","męża","mężami","mężów","mężów","mp"), femme: PL_M("żona","żoną","żonę","żonami","żony","żon","f"),
  frere: PL_M("brat","bratem","brata","braćmi","braci","braci","mp"), soeur: PL_M("siostra","siostrą","siostrę","siostrami","siostry","sióstr","f"),
  gp: PL_M("dziadek","dziadkiem","dziadka","dziadkami","dziadków","dziadków","mp"), gm: PL_M("babcia","babcią","babcię","babciami","babcie","babć","f"),
  pf: PL_M("wnuk","wnukiem","wnuka","wnukami","wnuków","wnuków","mp"), pfl: PL_M("wnuczka","wnuczką","wnuczkę","wnuczkami","wnuczki","wnuczek","f"),
  oncle: PL_M("wujek","wujkiem","wujka","wujkami","wujków","wujków","mp"), tante: PL_M("ciocia","ciocią","ciocię","ciociami","ciocie","cioć","f"),
  bratanek: PL_M("bratanek","bratankiem","bratanka","bratankami","bratanków","bratanków","mp"),
  bratanica: PL_M("bratanica","bratanicą","bratanicę","bratanicami","bratanice","bratanic","f"),
  siostrzeniec: PL_M("siostrzeniec","siostrzeńcem","siostrzeńca","siostrzeńcami","siostrzeńców","siostrzeńców","mp"),
  siostrzenica: PL_M("siostrzenica","siostrzenicą","siostrzenicę","siostrzenicami","siostrzenice","siostrzenic","f"),
  cousin: PL_M("kuzyn","kuzynem","kuzyna","kuzynami","kuzynów","kuzynów","mp"), cousine: PL_M("kuzynka","kuzynką","kuzynkę","kuzynkami","kuzynki","kuzynek","f"),
  tesc: PL_M("teść","teściem","teścia","teściami","teściów","teściów","mp"), tesciowa: PL_M("teściowa","teściową","teściową","teściowymi","teściowe","teściowych","f"),
  ziec: PL_M("zięć","zięciem","zięcia","zięciami","zięciów","zięciów","mp"), synowa: PL_M("synowa","synową","synową","synowymi","synowe","synowych","f"),
  szwagier: PL_M("szwagier","szwagrem","szwagra","szwagrami","szwagrów","szwagrów","mp"),
  szwagierka: PL_M("szwagierka","szwagierką","szwagierkę","szwagierkami","szwagierki","szwagierek","f"),
  g_bn: PL_M("bratanek, siostrzeniec","","","","","","mp"), g_bc: PL_M("bratanica, siostrzenica","","","","","","f")
};
function motPl(d){
  const f = d.so === "f";
  switch (d.k){
    case "parent": return f ? PL.mere : PL.pere;
    case "enfant": return f ? PL.fille : PL.fils;
    case "conjoint": return f ? PL.femme : PL.mari;
    case "frere": return f ? PL.soeur : PL.frere;
    case "grandparent": return f ? PL.gm : PL.gp;
    case "petitenfant": return f ? PL.pfl : PL.pf;
    case "oncle": return f ? PL.tante : PL.oncle;
    // le polonais dit l'enfant du frere (bratanek) ou de la soeur (siostrzeniec)
    case "neveu": return !d.precis || !d.par ? (f ? PL.g_bc : PL.g_bn) : d.par === "m" ? (f ? PL.bratanica : PL.bratanek) : (f ? PL.siostrzenica : PL.siostrzeniec);
    case "cousin": return f ? PL.cousine : PL.cousin;
    case "beauparent": return f ? PL.tesciowa : PL.tesc;
    case "gendre": return f ? PL.synowa : PL.ziec;
    case "beaufrere": return f ? PL.szwagierka : PL.szwagier;
  }
}
const PL_POSS = {je: ["moim","moją","moimi"], tu: ["twoim","twoją","twoimi"], nous: ["naszym","naszą","naszymi"]};
const ansPl = n => { const d = n % 10, c = n % 100; return n === 1 ? "rok" : (d >= 2 && d <= 4 && !(c >= 12 && c <= 14)) ? "lata" : "lat"; };
const PLs = jetons({
  mot: motPl,
  N: (x, c) => (PL_NOMS[x] || [x, x, x])[c || 0],
  etN: a => etListe(a.map(x => PLs.N(x)), " i "),
  // « bratem i siostrą », « siostrami », avec le possessif devant chaque mot : « moim bratem i moją siostrą »
  liste(parts, poss){
    if (parts.length === 1 && parts[0].n > 1) return (poss ? poss[2] + " " : "") + parts[0].w.ip;
    return etListe(parts.map(x => (poss ? (x.n > 1 ? poss[2] : poss[x.w.gr === "f" ? 1 : 0]) + " " : "") + (x.n > 1 ? x.w.ip : x.w.i)), " i ");
  },
  rendu(tok, owner){
    if (tok.t === "sont"){
      const k = tok.grp.k, poss = PL_POSS[tok.grp.forme || "je"];
      return PLs.etN(tok.g) + " są " + (k === "parent" ? poss[2] + " rodzicami" : PLs.liste(parMot(PLs, owner, tok.g, k), poss));
    }
    const w = PLs.mot(lienFin(owner, tok.o, tok.pn.k)), p = PL_POSS[tok.pn.forme][w.gr === "f" ? 1 : 0];
    return (tok.t === "estQ" ? "Czy " : "") + PLs.N(tok.o) + " jest " + p + " " + w.i + (tok.t === "estQ" ? "?" : "");
  },
  cite: s => "„" + s + "”" + (/[?!]$/.test(s) ? "" : "."),
  lien(o, r, e){ return PLs.N(o) + " jest " + PLs.mot(lienFin(e, o, r.k)).i + " " + (Array.isArray(e) ? etListe(e.map(x => PLs.N(x, 1)), " i ") : PLs.N(e, 1)) + "."; },
  lienPl(g, grp, e){ return PLs.etN(g) + " są " + (grp.k === "parent" ? "rodzicami" : PLs.liste(parMot(PLs, e, g, grp.k))) + " " + PLs.N(e, 1) + "."; },
  dit: (s, tok) => PLs.N(s) + " mówi: " + PLs.cite(PLs.rendu(tok, s)),
  disent: (a, b, tok) => PLs.N(a) + " i " + PLs.N(b) + " mówią: " + PLs.cite(PLs.rendu(tok, a)),
  demande: (s, a, tok) => PLs.N(s) + " pyta " + PLs.N(a, 2) + ": " + PLs.cite(PLs.rendu(tok, a)),
  estPoss3(o, k, so, sp, e){ return PLs.N(o) + " jest " + (sp === "f" ? "jej" : "jego") + " " + PLs.mot(e ? lienFin(e, o, k) : {k, so}).i + "."; },
  // « brata i siostrę », « dwie siostry », « dwóch wnuków i trzy wnuczki »
  compte(parts){
    const nb = (n, gr) => gr === "mp" ? ["", "", "dwóch", "trzech", "czterech", "pięciu"][n] : ["", "", "dwie", "trzy", "cztery", "pięć"][n];
    return etListe(parts.map(x => x.n === 1 ? x.w.a : nb(x.n, x.w.gr) + " " + (x.w.gr === "mp" || x.n >= 5 ? x.w.n5 : x.w.n2)), " i ");
  },
  combien: {},
  paire: (k, s1, s2) => PLs.mot({k, so: s1}).n + " → " + PLs.mot({k, so: s2}).n,
  soi: (o, age) => "To jest " + PLs.N(o) + ". Ma " + age + " " + ansPl(age) + ".",
  age: (o, age) => "Ma " + age + " " + ansPl(age) + "."
});
["frere", "cousin", "neveu", "oncle"].forEach(k => { PLs.combien[k] = e => ["", g => PLs.N(e) + " ma " + PLs.compte(parMot(PLs, e, g, k)) + "."]; });
PLs.combien.enfantCouple = (a, b) => ["", g => "Mają " + PLs.compte(parMot(PLs, a, g, "enfant")) + "."];
PLs.combien.petitCouple = (a, b) => ["", g => "Mają " + PLs.compte(parMot(PLs, a, g, "petitenfant")) + "."];
TRADS.pl = PLs;

// =====================================================================================================================
// LE TURC : « Peter, Anna'nın babası. », le cote de l'oncle et de la tante (amca / dayı, hala / teyze, enişte, yenge)
// =====================================================================================================================
// [genitif, datif]
const TR_NOMS = {Heinz:["Heinz'ın","Heinz'a"], Gisela:["Gisela'nın","Gisela'ya"], Peter:["Peter'in","Peter'e"], Monika:["Monika'nın","Monika'ya"],
  Sabine:["Sabine'nin","Sabine'ye"], Frank:["Frank'ın","Frank'a"], Jan:["Jan'ın","Jan'a"], Katrin:["Katrin'in","Katrin'e"],
  Anna:["Anna'nın","Anna'ya"], Lena:["Lena'nın","Lena'ya"], Felix:["Felix'in","Felix'e"], Sophie:["Sophie'nin","Sophie'ye"],
  Ben:["Ben'in","Ben'e"], Mia:["Mia'nın","Mia'ya"]};
const arriere = w => { const v = (w.match(/[aeıioöuü]/g) || ["e"]).pop(); return "aıou".includes(v); };
// [le mot, son possede (3e personne), mon, ton, notre]
const TR_M = (n, p3, p1, p2, p1p) => ({cle: n, n, p3, p1, p2, p1p});
const TRK = {
  baba: TR_M("baba","babası","babam","baban","babamız"), anne: TR_M("anne","annesi","annem","annen","annemiz"),
  ogul: TR_M("oğul","oğlu","oğlum","oğlun","oğlumuz"), kiz: TR_M("kız","kızı","kızım","kızın","kızımız"),
  koca: TR_M("koca","kocası","kocam","kocan","kocamız"), es: TR_M("eş","eşi","eşim","eşin","eşimiz"),
  ek: TR_M("erkek kardeş","erkek kardeşi","erkek kardeşim","erkek kardeşin","erkek kardeşimiz"),
  kk: TR_M("kız kardeş","kız kardeşi","kız kardeşim","kız kardeşin","kız kardeşimiz"),
  dede: TR_M("dede","dedesi","dedem","deden","dedemiz"),
  babaanne: TR_M("babaanne","babaannesi","babaannem","babaannen","babaannemiz"),
  anneanne: TR_M("anneanne","anneannesi","anneannem","anneannen","anneannemiz"),
  torun: TR_M("torun","torunu","torunum","torunun","torunumuz"),
  amca: TR_M("amca","amcası","amcam","amcan","amcamız"), dayi: TR_M("dayı","dayısı","dayım","dayın","dayımız"),
  hala: TR_M("hala","halası","halam","halan","halamız"), teyze: TR_M("teyze","teyzesi","teyzem","teyzen","teyzemiz"),
  eniste: TR_M("enişte","eniştesi","eniştem","enişten","eniştemiz"), yenge: TR_M("yenge","yengesi","yengem","yengen","yengemiz"),
  yegen: TR_M("yeğen","yeğeni","yeğenim","yeğenin","yeğenimiz"), kuzen: TR_M("kuzen","kuzeni","kuzenim","kuzenin","kuzenimiz"),
  kayinpeder: TR_M("kayınpeder","kayınpederi","kayınpederim","kayınpederin","kayınpederimiz"),
  kayinvalide: TR_M("kayınvalide","kayınvalidesi","kayınvalidem","kayınvaliden","kayınvalidemiz"),
  damat: TR_M("damat","damadı","damadım","damadın","damadımız"), gelin: TR_M("gelin","gelini","gelinim","gelinin","gelinimiz"),
  kayinbirader: TR_M("kayınbirader","kayınbiraderi","kayınbiraderim","kayınbiraderin","kayınbiraderimiz"),
  gorumce: TR_M("görümce","görümcesi","görümcem","görümcen","görümcemiz"), baldiz: TR_M("baldız","baldızı","baldızım","baldızın","baldızımız"),
  // sans personne (les paires)
  g_gm: TR_M("babaanne, anneanne"), g_et: TR_M("erkek torun"), g_kt: TR_M("kız torun"), g_on: TR_M("amca, dayı"), g_ta: TR_M("hala, teyze"),
  g_ey: TR_M("erkek yeğen"), g_ky: TR_M("kız yeğen"), g_ek: TR_M("kuzen (erkek)"), g_kk: TR_M("kuzen (kız)"),
  g_bf: TR_M("kayınbirader, enişte"), g_bs: TR_M("görümce, baldız, yenge")
};
function motTr(d){
  const f = d.so === "f", T = TRK;
  switch (d.k){
    case "parent": return f ? T.anne : T.baba;
    case "enfant": return f ? T.kiz : T.ogul;
    case "conjoint": return f ? T.es : T.koca;
    case "frere": return f ? T.kk : T.ek;
    case "grandparent": return !f ? T.dede : !d.precis || !d.cote ? T.g_gm : d.cote === "m" ? T.babaanne : T.anneanne;
    case "petitenfant": return d.precis ? T.torun : (f ? T.g_kt : T.g_et);
    case "oncle":
      if (!d.precis || !d.cote) return f ? T.g_ta : T.g_on;
      if (d.alliance) return f ? T.yenge : T.eniste;                         // la femme de l'oncle, le mari de la tante
      return d.cote === "m" ? (f ? T.hala : T.amca) : (f ? T.teyze : T.dayi);
    case "neveu": return d.precis ? T.yegen : (f ? T.g_ky : T.g_ey);
    case "cousin": return d.precis ? T.kuzen : (f ? T.g_kk : T.g_ek);
    case "beauparent": return f ? T.kayinvalide : T.kayinpeder;
    case "gendre": return f ? T.gelin : T.damat;
    case "beaufrere":
      if (!d.precis) return f ? T.g_bs : T.g_bf;
      if (d.via === "fratrie") return f ? T.yenge : T.eniste;                // la femme du frere, le mari de la soeur
      return f ? (d.par === "m" ? T.gorumce : T.baldiz) : T.kayinbirader;
  }
}
// le pluriel possede : kız kardeşleri, kuzenlerim
const plTr = (w, forme) => w.n + (arriere(w.n) ? "lar" : "ler") + ({p3: (arriere(w.n) ? "ı" : "i"), p1: (arriere(w.n) ? "ım" : "im")})[forme];
const qTr = w => { const v = (w.match(/[aeıioöuü]/g) || ["e"]).pop(); return "aı".includes(v) ? "mı" : "ei".includes(v) ? "mi" : "ou".includes(v) ? "mu" : "mü"; };
const TRs = jetons({
  mot: motTr,
  G: x => (TR_NOMS[x] || [x + "'in"])[0], D: x => (TR_NOMS[x] || [x, x + "'e"])[1],
  et: a => a,
  etN: a => etListe(a, " ve "),
  liste(parts, forme){
    return etListe(parts.map(x => x.n > 1 ? plTr(x.w, forme) : x.w[forme]), " ve ");
  },
  rendu(tok, owner){
    if (tok.t === "sont") return TRs.etN(tok.g) + " benim " + TRs.liste(parMot(TRs, owner, tok.g, tok.grp.k), "p1") + ".";
    const w = TRs.mot(lienFin(owner, tok.o, tok.pn.k));
    if (tok.t === "estQ") return tok.o + " senin " + w.p2 + " " + qTr(w.p2) + "?";
    return tok.o + (tok.pn.forme === "nous" ? " bizim " + w.p1p : " benim " + w.p1) + ".";
  },
  lien(o, r, e){ return o + ", " + (Array.isArray(e) ? etListe(e, " ve ").replace(/([^ ]+)$/, m => TRs.G(m)) : TRs.G(e)) + " " + TRs.mot(lienFin(e, o, r.k)).p3 + "."; },
  lienPl(g, grp, e){ return TRs.etN(g) + ", " + TRs.G(e) + " " + TRs.liste(parMot(TRs, e, g, grp.k), "p3") + "."; },
  dit: (s, tok) => s + " şöyle diyor: “" + TRs.rendu(tok, s) + "”",
  disent: (a, b, tok) => a + " ve " + b + " şöyle diyor: “" + TRs.rendu(tok, a) + "”",
  demande: (s, a, tok) => s + " " + TRs.D(a) + " soruyor: “" + TRs.rendu(tok, a) + "”",
  estPoss3(o, k, so, sp, e){ return o + " onun " + TRs.mot(e ? lienFin(e, o, k) : {k, so}).p3 + "."; },
  // « bir erkek kardeşi ve bir kız kardeşi », « iki kız kardeşi », « beş torunu »
  compte: parts => etListe(parts.map(x => ["", "bir", "iki", "üç", "dört", "beş"][x.n] + " " + x.w.p3), " ve "),
  combien: {},
  paire: (k, s1, s2) => TRs.mot({k, so: s1}).n + " → " + TRs.mot({k, so: s2}).n,
  soi: (o, age) => "Bu " + o + ". " + age + " yaşında.",
  age: (o, age) => age + " yaşında."
});
["frere", "cousin", "neveu", "oncle"].forEach(k => { TRs.combien[k] = e => ["", g => TRs.G(e) + " " + TRs.compte(parMot(TRs, e, g, k)) + " var."]; });
TRs.combien.enfantCouple = (a, b) => ["", g => "Onların " + TRs.compte(parMot(TRs, a, g, "enfant")) + " var."];
TRs.combien.petitCouple = (a, b) => ["", g => "Onların " + TRs.compte(parMot(TRs, a, g, "petitenfant")) + " var."];
TRADS.tr = TRs;

// =====================================================================================================================
// LE PERSAN : « پتر پدر آنا است. », l'ezafe ecrite seulement apres ا / و (ی) et apres le h muet (ٔ)
// =====================================================================================================================
const FA_NOMS = {Heinz:"هاینتس", Gisela:"گیزلا", Peter:"پتر", Monika:"مونیکا", Sabine:"زابینه", Frank:"فرانک", Jan:"یان", Katrin:"کاترین",
  Anna:"آنا", Lena:"لنا", Felix:"فلیکس", Sophie:"سوفی", Ben:"بن", Mia:"میا"};
const ezFa = w => /[اوآ]$/.test(w) ? w + "ی" : /ه$/.test(w) ? w + "ٔ" : w;
const plFa = w => w + "‌ها";
const FAM = n => ({cle: n, n});
function motFa(d){
  const f = d.so === "f", c = s => FAM(s);
  switch (d.k){
    case "parent": return c(f ? "مادر" : "پدر");
    case "enfant": return c(f ? "دختر" : "پسر");
    case "conjoint": return c(f ? "همسر" : "شوهر");
    case "frere": return c(f ? "خواهر" : "برادر");
    case "grandparent": return c(f ? "مادربزرگ" : "پدربزرگ");
    case "petitenfant": return c(d.precis ? "نوه" : f ? "نوه (دختر)" : "نوه (پسر)");
    case "oncle":
      if (!d.precis || !d.cote) return c(f ? "عمه، خاله" : "عمو، دایی");
      if (d.alliance) return c(d.cote === "m" ? (f ? "زن‌عمو" : "شوهرعمه") : (f ? "زن‌دایی" : "شوهرخاله"));
      return c(d.cote === "m" ? (f ? "عمه" : "عمو") : (f ? "خاله" : "دایی"));
    // l'enfant du frere ou de la soeur (de soi ou du conjoint), garcon ou fille : le meme mot
    case "neveu": return c(!d.precis || !d.par ? (f ? "برادرزاده، خواهرزاده (دختر)" : "برادرزاده، خواهرزاده (پسر)") : d.par === "m" ? "برادرزاده" : "خواهرزاده");
    case "cousin":
      if (!d.precis || !d.cote) return c(f ? "دخترعمو، دخترعمه، دختردایی، دخترخاله" : "پسرعمو، پسرعمه، پسردایی، پسرخاله");
      return c((f ? "دختر" : "پسر") + (d.cote === "m" ? (d.par === "m" ? "عمو" : "عمه") : (d.par === "m" ? "دایی" : "خاله")));
    case "beauparent": return c(!d.precis ? (f ? "مادرشوهر، مادرزن" : "پدرشوهر، پدرزن") : (f ? "مادر" : "پدر") + (d.se === "f" ? "شوهر" : "زن"));
    case "gendre": return c(f ? "عروس" : "داماد");
    case "beaufrere":
      if (!d.precis) return c(f ? "خواهرشوهر، خواهرزن، زن‌برادر" : "برادرزن، برادرشوهر، شوهرخواهر");
      if (d.via === "fratrie") return c(f ? "زن‌برادر" : "شوهرخواهر");
      return c((f ? "خواهر" : "برادر") + (d.par === "m" ? "شوهر" : "زن"));
  }
}
const FAs = jetons({
  mot: motFa,
  N: x => FA_NOMS[x] || x,
  etN: a => etListe(a.map(x => FAs.N(x)), " و "),
  // « برادر و خواهرِ آنا » : l'ezafe sur le dernier mot seulement ; « خواهرهای یان »
  liste: parts => ezFa(etListe(parts.map(x => x.n > 1 ? plFa(x.w.n) : x.w.n), " و ")),
  rendu(tok, owner){
    if (tok.t === "sont") return FAs.etN(tok.g) + " " + FAs.liste(parMot(FAs, owner, tok.g, tok.grp.k)) + " من هستند.";
    const w = FAs.mot(lienFin(owner, tok.o, tok.pn.k));
    if (tok.t === "estQ") return "آیا " + FAs.N(tok.o) + " " + ezFa(w.n) + " توست؟";
    return FAs.N(tok.o) + " " + ezFa(w.n) + (tok.pn.forme === "nous" ? " ما" : " من") + " است.";
  },
  lien(o, r, e){ return FAs.N(o) + " " + ezFa(FAs.mot(lienFin(e, o, r.k)).n) + " " + (Array.isArray(e) ? FAs.etN(e) : FAs.N(e)) + " است."; },
  lienPl(g, grp, e){ return FAs.etN(g) + " " + FAs.liste(parMot(FAs, e, g, grp.k)) + " " + FAs.N(e) + " هستند."; },
  dit: (s, tok) => FAs.N(s) + " می‌گوید: «" + FAs.rendu(tok, s) + "»",
  disent: (a, b, tok) => FAs.N(a) + " و " + FAs.N(b) + " می‌گویند: «" + FAs.rendu(tok, a) + "»",
  demande: (s, a, tok) => FAs.N(s) + " از " + FAs.N(a) + " می‌پرسد: «" + FAs.rendu(tok, a) + "»",
  estPoss3(o, k, so, sp, e){ return FAs.N(o) + " " + ezFa(FAs.mot(e ? lienFin(e, o, k) : {k, so}).n) + " اوست."; },
  compte: parts => etListe(parts.map(x => ["", "یک", "دو", "سه", "چهار", "پنج"][x.n] + " " + x.w.n), " و "),
  combien: {},
  paire: (k, s1, s2) => FAs.mot({k, so: s1}).n + " ← " + FAs.mot({k, so: s2}).n,
  soi: (o, age) => "این " + FAs.N(o) + " است. او " + age + " سال دارد.",
  age: (o, age) => "او " + age + " سال دارد."
});
["frere", "cousin", "neveu", "oncle"].forEach(k => { FAs.combien[k] = e => ["", g => FAs.N(e) + " " + FAs.compte(parMot(FAs, e, g, k)) + " دارد."]; });
FAs.combien.enfantCouple = (a, b) => ["", g => "آن‌ها " + FAs.compte(parMot(FAs, a, g, "enfant")) + " دارند."];
FAs.combien.petitCouple = (a, b) => ["", g => "آن‌ها " + FAs.compte(parMot(FAs, a, g, "petitenfant")) + " دارند."];
TRADS.fa = FAs;

// =====================================================================================================================
// L'ARABE : « بيتر هو والد آنا. », le cote de l'oncle (عم / خال), le cousin par ses deux parents (ابن العمة)
// =====================================================================================================================
const AR_NOMS = {Heinz:"هاينتس", Gisela:"غيزيلا", Peter:"بيتر", Monika:"مونيكا", Sabine:"زابينه", Frank:"فرانك", Jan:"يان", Katrin:"كاترين",
  Anna:"آنا", Lena:"لينا", Felix:"فيليكس", Sophie:"صوفي", Ben:"بن", Mia:"ميا"};
// le pronom affixe sur le dernier mot : عمة + ي -> عمتي ; أخ (seul) -> أخي, أخوك, أخونا, أخوه, أخوها
const AKH = {"ي": "أخي", "ك": "أخوك", "نا": "أخونا", "ه": "أخوه", "ها": "أخوها"};
const sufAr = (w, p) => w === "أخ" ? AKH[p] : /ة$/.test(w) ? w.slice(0, -1) + "ت" + p : w + p;
// un mot : sa tete (ابن, زوج, والد…) et son nom (عم, أخت…) ; c = a l'etat construit devant un prenom (أخو آنا) ;
// pour compter : s (un), d (deux), p (trois a cinq), gr (le genre du singulier, pour l'accord inverse du nombre) ;
// dc / pc : le duel et le pluriel construits (أختا يان, أخوات يان), auxquels on colle aussi le pronom (أختاي)
const AR_M = (h, t, s, d, p, gr, dc, pc, c) => ({cle: (h ? h + " " : "") + t, h, t, s, d, p, gr, dc, pc, c: c || null});
const AR = {
  walid: AR_M("", "والد", "والد", "والدان", "آباء", "m", "والدا", "آباء"), walida: AR_M("", "والدة", "والدة", "والدتان", "أمهات", "f", "والدتا", "أمهات"),
  ibn: AR_M("", "ابن", "ابن", "ابنان", "أبناء", "m", "ابنا", "أبناء"), ibna: AR_M("", "ابنة", "ابنة", "ابنتان", "بنات", "f", "ابنتا", "بنات"),
  zawj: AR_M("", "زوج", "زوج", "زوجان", "أزواج", "m", "زوجا", "أزواج"), zawja: AR_M("", "زوجة", "زوجة", "زوجتان", "زوجات", "f", "زوجتا", "زوجات"),
  akh: AR_M("", "أخ", "أخ", "أخوان", "إخوة", "m", "أخوا", "إخوة", "أخو"), ukht: AR_M("", "أخت", "أخت", "أختان", "أخوات", "f", "أختا", "أخوات"),
  jadd: AR_M("", "جد", "جد", "جدان", "أجداد", "m", "جدا", "أجداد"), jadda: AR_M("", "جدة", "جدة", "جدتان", "جدات", "f", "جدتا", "جدات"),
  hafid: AR_M("", "حفيد", "حفيد", "حفيدان", "أحفاد", "m", "حفيدا", "أحفاد"), hafida: AR_M("", "حفيدة", "حفيدة", "حفيدتان", "حفيدات", "f", "حفيدتا", "حفيدات"),
  amm: AR_M("", "عم", "عم", "عمان", "أعمام", "m", "عما", "أعمام"), amma: AR_M("", "عمة", "عمة", "عمتان", "عمات", "f", "عمتا", "عمات"),
  khal: AR_M("", "خال", "خال", "خالان", "أخوال", "m", "خالا", "أخوال"), khala: AR_M("", "خالة", "خالة", "خالتان", "خالات", "f", "خالتا", "خالات"),
  sihr: AR_M("", "صهر", "صهر", "صهران", "أصهار", "m", "صهرا", "أصهار"), kanna: AR_M("", "كنّة", "كنّة", "كنّتان", "كنّات", "f", "كنّتا", "كنّات")
};
// les mots composes : « ابن عم », « زوج عمة », « زوجة شقيق » (le duel et le pluriel portent sur la tete)
const TETE = {"ابن": ["ابنا", "أبناء", "m"], "ابنة": ["ابنتا", "بنات", "f"], "زوج": ["زوجا", "أزواج", "m"], "زوجة": ["زوجتا", "زوجات", "f"],
  "والد": ["والدا", "آباء", "m"], "والدة": ["والدتا", "أمهات", "f"], "شقيق": ["شقيقا", "أشقاء", "m"], "شقيقة": ["شقيقتا", "شقيقات", "f"]};
const ARc = (h, t) => AR_M(h, t, h + " " + t, TETE[h][0] + " " + t, TETE[h][1] + " " + t, TETE[h][2], TETE[h][0], TETE[h][1]);
const ARg = s => ({cle: s, h: "", t: s, s, gen: true});
function motAr(d){
  const f = d.so === "f", A = AR;
  switch (d.k){
    case "parent": return f ? A.walida : A.walid;
    case "enfant": return f ? A.ibna : A.ibn;
    case "conjoint": return f ? A.zawja : A.zawj;
    case "frere": return f ? A.ukht : A.akh;
    case "grandparent": return f ? A.jadda : A.jadd;
    case "petitenfant": return f ? A.hafida : A.hafid;
    case "oncle":
      if (!d.precis || !d.cote) return ARg(f ? "العمة، الخالة" : "العم، الخال");
      if (d.alliance) return ARc(f ? "زوجة" : "زوج", d.cote === "m" ? (f ? "عم" : "عمة") : (f ? "خال" : "خالة"));
      return d.cote === "m" ? (f ? A.amma : A.amm) : (f ? A.khala : A.khal);
    case "neveu":
      if (!d.precis || !d.par) return ARg(f ? "ابنة الأخ، ابنة الأخت" : "ابن الأخ، ابن الأخت");
      return ARc(f ? "ابنة" : "ابن", d.par === "m" ? "أخ" : "أخت");
    case "cousin":
      if (!d.precis || !d.cote) return ARg(f ? "ابنة العم، ابنة الخال" : "ابن العم، ابن الخال");
      return ARc(f ? "ابنة" : "ابن", d.cote === "m" ? (d.par === "m" ? "عم" : "عمة") : (d.par === "m" ? "خال" : "خالة"));
    case "beauparent": return !d.precis ? ARg(f ? "والدة الزوج أو الزوجة" : "والد الزوج أو الزوجة") : ARc(f ? "والدة" : "والد", d.se === "f" ? "زوج" : "زوجة");
    case "gendre": return f ? A.kanna : A.sihr;
    case "beaufrere":
      if (!d.precis) return ARg(f ? "زوجة الأخ، شقيقة الزوج أو الزوجة" : "زوج الأخت، شقيق الزوج أو الزوجة");
      if (d.via === "fratrie") return f ? ARc("زوجة", "أخ") : ARc("زوج", "أخت");
      return ARc(f ? "شقيقة" : "شقيق", d.par === "m" ? "زوج" : "زوجة");
  }
}
// devant un prenom : « أخو آنا », « ابن عم آنا » ; le compose garde son nom au genitif (« ابن أخ » -> « ابن شقيق » devant
// un prenom, pour ne pas ecrire « ابن أخي آنا »)
const consAr = (w, nom) => (w.h ? w.h + " " + (w.t === "أخ" ? "شقيق" : w.t) : (w.c || w.t)) + " " + nom;
const possAr = (w, p, chaqiq) => (w.h ? w.h + " " + (w.t === "أخ" ? (chaqiq ? "شقيق" + p : sufAr2(p)) : sufAr(w.t, p)) : sufAr(w.t, p));
// « ابن أخي », « ابن أخيك » : le nom au genitif apres la tete
const sufAr2 = p => ({"ي": "أخي", "ك": "أخيك", "نا": "أخينا", "ه": "أخيه", "ها": "أخيها"})[p];
const proAr = x => sexe(x) === "f" ? "هي" : "هو";
const ansAr = n => n === 1 ? "سنة واحدة" : n === 2 ? "سنتان" : (n >= 3 && n <= 10) ? n + " سنوات" : n + " سنة";
const ARs = jetons({
  mot: motAr,
  N: x => AR_NOMS[x] || x,
  etN: a => a.map(x => ARs.N(x)).reduce((s, x, i) => i ? s + " و" + x : x, ""),
  pro: g => g.length === 2 ? "هما" : g.every(x => sexe(x) === "f") ? "هن" : "هم",
  // « عمة آنا وزوج عمتها » : le premier mot devant le prenom, les suivants avec le pronom de celui-ci
  // (« أخي وأختي » quand c'est le possessif) ; deux du meme mot : le duel (« أختا يان », « أختاي »)
  liste(parts, apres){
    return parts.map((x, i) => {
      // deux ou trois du meme mot : le duel ou le pluriel, construit (la tete d'un compose : « ابنتا خال »)
      const w = x.n === 1 ? x.w : x.w.h ? Object.assign({}, x.w, {h: x.n === 2 ? x.w.dc : x.w.pc, c: null})
                                        : Object.assign({}, x.w, {t: x.n === 2 ? x.w.dc : x.w.pc, c: null});
      return i === 0 ? apres.premier(w) : apres.suite(w);
    }).reduce((s, x, i) => i ? s + " و" + x : x, "");
  },
  // dans une phrase qui a dit « ابن شقيق آنا », la suite dit « ابنة شقيقها » (et non « ابنة أخيها »)
  avecNom: (nom, suf) => ({premier: w => consAr(w, nom), suite: w => possAr(w, suf, true)}),
  avecSuf: suf => ({premier: w => possAr(w, suf), suite: w => possAr(w, suf)}),
  rendu(tok, owner){
    const suf = tok.t === "sont" ? "ي" : ({je: "ي", tu: "ك", nous: "نا"})[tok.pn.forme];
    if (tok.t === "sont") return ARs.etN(tok.g) + " " + ARs.pro(tok.g) + " " + (tok.grp.k === "parent" ? "والداي" : ARs.liste(parMot(ARs, owner, tok.g, tok.grp.k), ARs.avecSuf("ي"))) + ".";
    const w = ARs.mot(lienFin(owner, tok.o, tok.pn.k));
    if (tok.t === "estQ") return "هل " + ARs.N(tok.o) + " " + possAr(w, suf) + "؟";
    return ARs.N(tok.o) + " " + proAr(tok.o) + " " + possAr(w, suf) + ".";
  },
  lien(o, r, e){
    const nom = Array.isArray(e) ? ARs.etN(e) : ARs.N(e), w = ARs.mot(lienFin(e, o, r.k));
    return ARs.N(o) + " " + proAr(o) + " " + (w.gen ? w.t + " (" + nom + ")" : consAr(w, nom)) + ".";
  },
  lienPl(g, grp, e){
    const parts = parMot(ARs, e, g, grp.k), suf = sexe(e) === "f" ? "ها" : "ه";
    // les parents : « والدا آنا »
    if (grp.k === "parent") return ARs.etN(g) + " هما والدا " + ARs.N(e) + ".";
    return ARs.etN(g) + " " + ARs.pro(g) + " " + ARs.liste(parts, ARs.avecNom(ARs.N(e), suf)) + ".";
  },
  dit: (s, tok) => ARs.N(s) + (sexe(s) === "f" ? " تقول" : " يقول") + ": «" + ARs.rendu(tok, s) + "»",
  disent: (a, b, tok) => ARs.N(a) + " و" + ARs.N(b) + (sexe(a) === "f" && sexe(b) === "f" ? " تقولان" : " يقولان") + ": «" + ARs.rendu(tok, a) + "»",
  demande: (s, a, tok) => ARs.N(s) + (sexe(s) === "f" ? " تسأل " : " يسأل ") + ARs.N(a) + ": «" + ARs.rendu(tok, a) + "»",
  estPoss3(o, k, so, sp, e){ return ARs.N(o) + " " + proAr(o) + " " + possAr(ARs.mot(e ? lienFin(e, o, k) : {k, so}), sp === "f" ? "ها" : "ه") + "."; },
  // « أخ وأخت », « أختان », « ثلاث حفيدات » (le nombre prend le genre inverse du singulier)
  compte: parts => parts.map(x => x.n === 1 ? x.w.s : x.n === 2 ? x.w.d
                 : (x.w.gr === "f" ? ["", "", "", "ثلاث", "أربع", "خمس"] : ["", "", "", "ثلاثة", "أربعة", "خمسة"])[x.n] + " " + x.w.p)
                 .reduce((s, x, i) => i ? s + " و" + x : x, ""),
  combien: {},
  paire: (k, s1, s2) => { const g = (s) => { const w = ARs.mot({k, so: s}); return w.gen ? w.t : "ال" + w.t; }; return g(s1) + " ← " + g(s2); },
  soi: (o, age) => "هذه " + ARs.N(o) + ". عمرها " + ansAr(age) + ".",
  age: (o, age) => (sexe(o) === "f" ? "عمرها " : "عمره ") + ansAr(age) + "."
});
["frere", "cousin", "neveu", "oncle"].forEach(k => { ARs.combien[k] = e => ["", g => "لدى " + ARs.N(e) + " " + ARs.compte(parMot(ARs, e, g, k)) + "."]; });
ARs.combien.enfantCouple = (a, b) => ["", g => "لديهما " + ARs.compte(parMot(ARs, a, g, "enfant")) + "."];
ARs.combien.petitCouple = (a, b) => ["", g => "لديهما " + ARs.compte(parMot(ARs, a, g, "petitenfant")) + "."];
TRADS.ar = ARs;
}
