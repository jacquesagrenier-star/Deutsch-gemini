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
  // JAMAIS DEUX DOCUMENTS DU MEME GENRE DE SUITE (8 nov. 2026, Jacques : deux « Lis le mot de Katrin » de suite, au
  // contenu different, et il a cru revoir la meme carte). Une page marque ce qui fabrique un papier
  // (papierMot = Tirage.doc("mot", papierMot)) ; montrer() refuse, tant qu'il a le choix, une carte dont un papier est du
  // genre de la carte d'avant : le mot passe alors un peu plus loin, il n'est pas perdu. Sans autre choix, la carte passe.
  doc(genre, fabrique){ return (...a) => fabrique(...a).replace("<div", '<div data-doc="' + genre + '"'); },
  genres(z){ return z ? Array.from(z.querySelectorAll("[data-doc]")).map(e => e.dataset.doc) : []; },
  // docLibre : dernier passage avant le repli ; une question jamais vue vaut mieux que deux documents evites
  docLibre: false,
  docRepete(z){ return !Tirage.docLibre && Tirage.genres(z).some(g => Tirage.docAvant.includes(g)); },
  docPose(z){ Tirage.docAvant = Tirage.genres(z); if (!z) Tirage.docReportes = new Set(); },
  // le mot repousse revient des qu'une carte sans document libere la place : sinon ces mots s'accumulent a la fin,
  // et il ne reste plus que des documents du meme genre (demarches : 35 parties sur 100 avant ce retour anticipe)
  docReportes: new Set(),
  docReporte(w){ if (Tirage.docAvant.length) Tirage.docReportes.add(w); },
  ordreDocs(file, rang){
    const ids = file.map((_, i) => i).slice(rang), r = i => Tirage.docReportes.has(file[i]);
    return Tirage.docAvant.length ? ids : ids.filter(r).concat(ids.filter(i => !r(i)));
  },
  docAvant: [],
  // UNE REVISION PAR QUESTION (ligne 95 ; decision de Jacques du 13 nov. 2026 : « au moment ou on a une grande
  // reserve, autant pour les themes que pour les scenes, on devrait [avoir] une meme approche » -- celle des
  // cartes-phrases, ligne 84). Le mot reste choisi par sa carte (plan) ; c'est la QUESTION qui l'habille qui suit
  // maintenant sa propre revision, dans le moteur commun de index.html (type « t ») :
  //   - une question jamais posee passe d'abord ; puis une question due ; une question reussie attend 60 jours,
  //     puis 180, puis 365 (REVISION_JOURS de index.html) ; ratee, elle revient le lendemain ;
  //   - une question en attente ne se pose que si le mot n'en a plus d'autre (repli de la page, comme avant).
  // Les pages tirent leurs questions au hasard (EX[sorte](mot)) et refusent celles que vus.has() connait. Tirage.vus()
  // remplace ce Set : au debut d'une question il refuse tout ce qui n'est pas jamais pose, puis tout ce qui est en
  // attente, puis seulement ce qui a deja ete vu dans la partie (le comportement d'avant) -- par paliers comptes en
  // tirages, pour que le cout reste borne quand toute la reserve d'un mot a ete reussie. vus.add() (la question
  // retenue) remet les paliers a zero et note la question courante, que l'« exercice » envoie avec son verdict.
  // L'etat vient de l'app (message « questions ») ; hors de l'app, ou d'une app d'avant la ligne 95, il est vide et
  // vus() se comporte exactement comme un Set.
  PALIER_JAMAIS: 75,
  PALIER_DUE: 50,
  revisions: null,     // { etat: { id: [reussites, jour de l'echeance, jour vu] }, jour }
  courante: null,
  page(){ try{ return (location.pathname.split("/").pop() || "").replace(/\.html?$/, ""); }catch(e){ return ""; } },
  // le texte qui identifie une question : la page et sa cle (cleQuestion), hachee par l'app comme les phrases
  texteQuestion(cle){ return Tirage.page() + "|" + cle; },
  // le meme hachage que idRevision() de index.html
  idQuestion(texte){
    const s = String(texte || "").normalize("NFC").replace(/\s+/g, " ").trim();
    let h = 5381;
    for (let i = 0; i < s.length; i++) h = ((h * 33) ^ s.charCodeAt(i)) >>> 0;
    return h.toString(36) + s.length.toString(36);
  },
  // LA CLE DE REVISION : la cle de la page (cleQuestion) ET le mot vise (motQ, variable de chaque page). Certaines
  // sortes ont un enonce fixe (« Welcher Satz ist richtig? », une ecoute sans texte) : sans le mot, toutes leurs
  // questions auraient la meme cle, et en reussir une aurait ecarte la sorte entiere pour 60 jours.
  motDeLaQuestion(){
    try{
      const m = typeof motQ !== "undefined" ? motQ : null;
      if (!m) return "";
      if (Array.isArray(m)) return m.join(" ");
      if (typeof m === "object") return ((m.genre || "") + " " + (m.mot || "")).trim();
      return String(m);
    }catch(e){ return ""; }
  },
  cleRevision(k){ const m = Tirage.motDeLaQuestion(); return m ? k + "|" + m : k; },
  // la question tiree a l'instant (cle de la page, avec son mot)
  statut(cle){
    const r = Tirage.revisions;
    if (!r || !r.etat) return "jamais";
    const x = r.etat[Tirage.idQuestion(Tirage.texteQuestion(Tirage.cleRevision(cle)))];
    if (!x) return "jamais";
    return x[1] > r.jour ? "attente" : "due";
  },
  vus(){
    const base = new Set();
    let tirages = 0;
    return {
      has(k){
        if (base.has(k)) return true;
        if (!Tirage.revisions) return false;
        tirages++;
        const s = Tirage.statut(k);
        if (tirages <= Tirage.PALIER_JAMAIS) return s !== "jamais";
        if (tirages <= Tirage.PALIER_JAMAIS + Tirage.PALIER_DUE) return s === "attente";
        return false;
      },
      add(k){ base.add(k); tirages = 0; Tirage.courante = Tirage.cleRevision(k); return this; },
      delete(k){ return base.delete(k); },
      clear(){ base.clear(); tirages = 0; },
      values(){ return base.values(); },
      forEach(f){ base.forEach(f); },
      get size(){ return base.size; }
    };
  },
  // l'« exercice » d'une page : son verdict, et la question qu'il juge (l'app la note, type « t »)
  question(extra){
    const out = Object.assign({}, extra || {});
    if (Tirage.courante){
      out.rev = "t"; out.question = Tirage.texteQuestion(Tirage.courante);
      // la page garde sa copie a jour : une question jugee ne se repropose pas comme « jamais posee »
      if (Tirage.revisions && Tirage.revisions.etat){
        const id = Tirage.idQuestion(out.question), j = Tirage.revisions.jour, av = Tirage.revisions.etat[id];
        Tirage.revisions.etat[id] = out.juste === false ? [0, j + 1, j] : [(av ? av[0] : 0) + 1, j + 60, j];
      }
    }
    return out;
  },
  // l'etat des questions de ce type, demande a l'app ; null hors de l'app ou si elle ne repond pas
  demanderQuestions(type, attente){
    if (window.parent === window) return Promise.resolve(null);
    return new Promise(fin => {
      let fait = false;
      const finir = v => { if (fait) return; fait = true; window.removeEventListener("message", ecoute); fin(v); };
      const delai = setTimeout(() => finir(null), attente || 2000);
      function ecoute(ev){
        const d = ev.data;
        if (ev.source !== window.parent || !d || d.source !== "wortando-app" || d.type !== "questions") return;
        clearTimeout(delai);
        finir(d.etat && typeof d.etat === "object" && typeof d.jour === "number" ? {etat: d.etat, jour: d.jour} : null);
      }
      window.addEventListener("message", ecoute);
      try{ window.parent.postMessage({source: "wortando-scene", type: "questions", rev: type}, "*"); }
      catch(e){ clearTimeout(delai); finir(null); }
    });
  },
  // les mots du theme -> l'etat de chacun, dans le meme ordre ; null hors de l'app. L'etat des questions arrive
  // avec lui (Tirage.revisions) : une app d'avant la ligne 95 ne repond pas a « questions », on ne l'attend alors
  // que 300 ms apres les etats.
  demander(mots){
    if (window.parent === window) return Promise.resolve(null);
    const questions = Tirage.demanderQuestions("t", 2300).then(r => { Tirage.revisions = r; });
    return Tirage.demanderEtats(mots).then(etats =>
      Promise.race([questions, new Promise(r => setTimeout(r, 300))]).then(() => etats));
  },
  demanderEtats(mots){
    return new Promise(fin => {
      const delai = setTimeout(() => { window.removeEventListener("message", ecoute); fin(null); }, 2000);
      function ecoute(ev){
        const d = ev.data;
        if (ev.source !== window.parent || !d || d.source !== "wortando-app" || d.type !== "etats") return;
        clearTimeout(delai); window.removeEventListener("message", ecoute); fin(Array.isArray(d.etats) ? d.etats : null);
      }
      window.addEventListener("message", ecoute);
      // « sens » (3 nov.) : la traduction de l'entree voulue, pour un mot a deux entrees au corpus (rico : delicieux / riche)
      // « theme » (16 nov. 2026, themes des Soins) : l'id du theme de soins avec son niveau (soins_koerper_a2), pour que
      // l'app cherche d'abord la carte de SOINS (carteDeScene) ; absent des autres themes, il ne change rien pour eux
      try{ window.parent.postMessage({source: "wortando-scene", type: "etats", mots: mots.map(m => ({mot: m.mot, genre: m.genre || null, cat: m.cat || null, sens: m.sens || null, theme: m.theme || null}))}, "*"); }
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
