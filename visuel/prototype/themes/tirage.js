// LE TIRAGE SUIT LES MOTS -- commun a tous les themes illustres (3 nov. 2026).
//
// Jacques : « l'important, c'est que [...] Tio [...] revienne assez souvent [...] jusqu'au moment ou on le maitrise,
// puis qu'apres ca, ca disparait » ; « on ne demandera plus de questions sur Tio. Avant 16 jours. » La reserve de
// questions (des centaines par theme) reste invisible : une partie choisit d'abord les MOTS a travailler, dans la
// progression commune aux cartes, puis habille chacun d'une question.
//
//   1. l'app donne l'etat de chaque mot du theme (message « etats » -> reponse « etats » de index.html, les memes
//      etats que les cartes : neuf, du, pas encore du) ;
//   2. l'ordre : les mots DUS (les plus en retard d'abord), puis ceux RATES RECEMMENT (une erreur les fait revenir
//      dans quelques minutes), puis des NOUVEAUX, dans une limite par partie, comme les cartes neuves de la seance ;
//   3. un mot pas encore du n'est JAMAIS demande ; un mot rate dans la partie y revient trois questions plus loin ;
//   4. plus rien a faire : la partie le dit (« Tout est revu pour aujourd'hui ») avec la prochaine echeance, et
//      ne repose pas des mots deja sus.
// Hors de l'app (la page ouverte seule, les controles), il n'y a pas d'etats : tous les mots sont neufs.
const Tirage = {
  // les mots du theme -> l'etat de chacun, dans le meme ordre ; null hors de l'app
  demander(mots){
    if (window.parent === window) return Promise.resolve(null);
    return new Promise(fin => {
      const delai = setTimeout(() => { window.removeEventListener("message", ecoute); fin(null); }, 2000);
      function ecoute(ev){
        const d = ev.data;
        if (ev.source !== window.parent || !d || d.source !== "wortando-app" || d.type !== "etats") return;
        clearTimeout(delai); window.removeEventListener("message", ecoute); fin(Array.isArray(d.etats) ? d.etats : null);
      }
      window.addEventListener("message", ecoute);
      // « sens » (3 nov.) : la traduction de l'entree voulue, pour un mot a deux entrees au corpus (rico : delicieux / riche)
      try{ window.parent.postMessage({source: "wortando-scene", type: "etats", mots: mots.map(m => ({mot: m.mot, genre: m.genre || null, cat: m.cat || null, sens: m.sens || null}))}, "*"); }
      catch(e){ clearTimeout(delai); fin(null); }
    });
  },
  // la file des mots d'une partie, et la prochaine echeance si elle est vide
  // etat : {e: "n"} neuf, {e: "d", due} du, {e: "f", due, h} pas encore du (h : reussites de suite), {e: "x"} hors jeu
  plan(mots, etats, nb, neufsMax){
    const maintenant = Date.now();
    const dus = [], rates = [], neufs = [];
    let prochaine = Infinity;
    mots.forEach((m, i) => {
      const s = etats ? (etats[i] || {e: "x"}) : {e: "n"};
      if (s.e === "d") dus.push([s.due || 0, m]);
      else if (s.e === "f" && !s.h && s.due - maintenant < 15 * 60000) rates.push([s.due, m]);   // rate il y a peu
      else if (s.e === "n") neufs.push(m);
      else if (s.e === "f" && s.due) prochaine = Math.min(prochaine, s.due);
    });
    dus.sort((a, b) => a[0] - b[0]); rates.sort((a, b) => a[0] - b[0]);
    const file = dus.map(x => x[1]).concat(rates.map(x => x[1]), melanger(neufs).slice(0, etats ? neufsMax : nb)).slice(0, nb);
    if (!file.length && rates.length) prochaine = Math.min(prochaine, rates[0][0]);
    return {file, prochaine: prochaine === Infinity ? null : prochaine};
  },
  // « ENCORE DES QUESTIONS » (Jacques, 3 nov. : « on pourrait toujours offrir des questions supplementaires ») :
  // c'est l'eleve qui choisit de continuer. Des mots DEJA VUS du theme, au hasard ; la repetition espacee n'en est
  // pas faussee : revisionDeScene() ne fait pas avancer un mot pas encore du, et une erreur le fait revenir plus tot.
  supplement(mots, etats, nb){
    const vus = mots.filter((m, i) => !etats || (etats[i] && (etats[i].e === "d" || etats[i].e === "f")));
    return melanger(vus).slice(0, nb);
  },
  // une erreur : le mot revient trois questions plus loin, sans depasser la longueur d'une partie
  remettre(file, rang, mot, nb){
    if (file.length >= nb) return;
    file.splice(Math.min(file.length, rang + 4), 0, mot);
  },
  // « Tout est revu pour aujourd'hui », et quand revenir
  revu(prochaine, langue){
    let quand = "";
    if (prochaine){
      try{ quand = new Date(prochaine).toLocaleString(langue, {weekday: "long", day: "numeric", month: "long", hour: "2-digit", minute: "2-digit"}); }
      catch(e){ quand = new Date(prochaine).toLocaleString(); }
    }
    return quand;
  }
};
const TIRAGE_TEXTES = {
  revu:      {fr:"Tout est revu pour aujourd'hui.", en:"Everything is reviewed for today.", tr:"Bugünlük her şey tekrar edildi.", uk:"На сьогодні все повторено.", fa:"برای امروز همه‌چیز مرور شد.", ar:"تمت مراجعة كل شيء لهذا اليوم.", pt:"Tudo revisado por hoje.", pl:"Na dziś wszystko powtórzone.", ru:"На сегодня всё повторено.", de:"Für heute ist alles wiederholt."},
  encore:    {fr:"Encore des questions", en:"More questions", tr:"Daha fazla soru", uk:"Ще запитання", fa:"پرسش‌های بیشتر", ar:"مزيد من الأسئلة", pt:"Mais perguntas", pl:"Więcej pytań", ru:"Ещё вопросы", de:"Weitere Fragen"},
  prochaine: {fr:"Prochaine révision : {d}", en:"Next review: {d}", tr:"Sonraki tekrar: {d}", uk:"Наступне повторення: {d}", fa:"مرور بعدی: {d}", ar:"المراجعة التالية: {d}", pt:"Próxima revisão: {d}", pl:"Następna powtórka: {d}", ru:"Следующее повторение: {d}", de:"Nächste Wiederholung: {d}"}
};
