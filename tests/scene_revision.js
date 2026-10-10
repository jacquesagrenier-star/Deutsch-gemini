// UNE REPONSE DANS LA SCENE = UNE REVISION DU MOT (branche scenes-revision).
//
//   node tests/scene_revision.js
//
// Une page headless joue le role de l'app : elle porte le VRAI code d'index.html
// qui recoit la scene et ecrit la progression (le gestionnaire de messages,
// carteDeScene, revisionDeScene, getWordState/setWordState, l'echelle de la
// repetition espacee), extrait par nom de fonction, et le vrai corpus. Elle
// ouvre le VRAI prototype de scene dans son cadre, en seance, et l'eleve y
// repond -- on touche la bonne zone, ou une mauvaise, dans la scene elle-meme.
//
// Ce qui est remplace par un bouchon, et seulement ca : Firebase, l'ecriture
// differee sur disque, l'objectif du jour, la navigation entre ecrans.
//
// Playwright : celui installe globalement (npm root -g), Chromium de
// PLAYWRIGHT_BROWSERS_PATH. Sur le PC : npm i -g playwright une fois.
const fs = require("fs");
const http = require("http");
const path = require("path");
const { execSync } = require("child_process");

let chromium;
try { ({ chromium } = require("playwright")); }
catch (e) {
  const g = execSync("npm root -g").toString().trim();
  ({ chromium } = require(path.join(g, "playwright")));
}

const RACINE = path.join(__dirname, "..");
const src = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");

// Une fonction de premier niveau : de « function nom( » a la premiere ligne
// « } » en colonne 0.
function fonction(nom) {
  const i = src.indexOf("\nfunction " + nom + "(");
  if (i < 0) throw new Error("fonction introuvable : " + nom);
  const j = src.indexOf("\n}", i + 1);
  return src.slice(i + 1, j + 2);
}
function constante(nom) {
  const m = src.match(new RegExp("\\n(const " + nom + " = [^\\n]*;)"));
  if (!m) throw new Error("constante introuvable : " + nom);
  return m[1];
}
function bloc(debut, fin) {
  const i = src.indexOf(debut);
  if (i < 0) throw new Error("bloc introuvable : " + debut);
  return src.slice(i, src.indexOf(fin, i) + fin.length);
}

const CODE_APP = [
  constante("SRS_DAILY_LADDER_DAYS"), constante("SRS_PALIERS"),
  constante("SRS_ENCORE_MINUTES"), constante("SRS_PREMIERE_MINUTES"),
  constante("SRS_ENTRETIEN_JOURS"), constante("PLAFOND_NEUFS"), constante("NEUFS_KEY"),
  "let progressCache = null;",
  bloc("const CLES_STABLES = {", "\n};"),
  ...["getProgress", "progressKey", "prefixeLangue", "cleMot", "getWordState",
      "setWordState", "estNeuf", "etatNeufsDuJour", "ecrireNeufsDuJour",
      "noterMotNeuf", "joursEntretien", "programmerEcheance", "programmerMaitrise",
      "estChapitreVhs", "themesComptes", "baseScenes", "ouvrirSceneSeance",
      "carteDeScene", "revisionDeScene"].map(fonction),
  'let sceneOuverteDepuis = "seance";',
  bloc('window.addEventListener("message", (e) => {', "\n});")
].join("\n\n");

// Le corpus, mis dans la forme que l'app lui donne au chargement (les champs
// que ces fonctions lisent : le mot en case 0, le genre en case 1).
function corpus() {
  const lire = f => JSON.parse(fs.readFileSync(path.join(RACINE, f), "utf8"));
  const grouped = {}, order = [];
  for (const t of lire("themes.json").themes) {
    const base = t.id.replace(/_(a1|a2|b1|b2|c1)$/i, "");
    if (!grouped[base]) { grouped[base] = { id: base, levels: {} }; order.push(base); }
    grouped[base].levels[t.niveau] = { id: t.id, words: t.mots.map(w => [w.mot, w.genre]) };
  }
  const verbes = [], adjectifs = [];
  const v = lire("verbe.json"), a = lire("adjectif.json");
  for (const n of Object.keys(v)) v[n].forEach(x => verbes.push({ infinitif: x.infinitif, niveau: n }));
  for (const n of Object.keys(a)) a[n].forEach(x => adjectifs.push([x.mot, x.traduction, x.exemple, n]));
  return { themes: order.map(id => grouped[id]), verbes, adjectifs };
}

const PAGE = `<!doctype html><meta charset="utf-8"><title>banc</title>
<iframe id="sceneCadre" style="width:420px;height:800px"></iframe>
<script>
const STORAGE_KEY = "deutschAI_progress";
const LANGUE_ENSEIGNEE = { code: "de" };
const ADRESSE_DEFINITIVE = "";
let progressDirectionOverride = null;
const C = ${JSON.stringify(corpus())};
let themes = C.themes;
const verbeTheme = { id: "verben", words: C.verbes };
const adjektiveTheme = { id: "adjektive", words: C.adjectifs };
// Les bouchons
const journal = [];
function saveProgress(p){ progressCache = p; localStorage.setItem(STORAGE_KEY, JSON.stringify(p)); }
function getTodayStr(){ return "2026-10-10"; }
function getLearningDirection(){ return "de"; }
function accesComplet(){ return true; }
function filtrerGratuit(items){ return items; }
function recordDailyActivity(){ journal.push("objectif"); return 0; }
function logMasteryEvent(){ journal.push("maitrise"); }
function showScreen(s){ journal.push("ecran:" + s); }
function sceneDuJour(){ return window.SCENE_DU_JOUR; }
function niveauSeance(){ return window.NIVEAU; }
function ouvrirSeanceDuJour(){ journal.push("cartes"); }
function ouvrirChoixSeance(){ journal.push("choix"); }
function openAdminDashboard(){ journal.push("admin"); }
${CODE_APP}
</script>`;

const TYPES = { ".html": "text/html", ".js": "text/javascript", ".json": "application/json",
                ".webp": "image/webp", ".png": "image/png" };
const serveur = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split("?")[0]);
  if (u === "/banc.html") { res.writeHead(200, { "content-type": "text/html" }); return res.end(PAGE); }
  const f = path.join(RACINE, u);
  if (!f.startsWith(RACINE) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});

let ko = 0;
const ok = (n, v) => { console.log("  " + (v ? "OK   " : "ECHEC") + "  " + n); if (!v) ko++; };

// Ce que la progression contient d'autre AVANT la scene : des mots deja
// travailles, qui ne doivent pas bouger d'un octet.
const DEJA = {
  "familie_a1": { "0": { mastered: false, due: 1, reviews: 3, srsHits: 2, srsDailyStreak: 1 },
                  "1": { mastered: true, due: 9e12, reviews: 5, srsHits: 4, entretiens: 1 } },
  "verben": { "sein": { mastered: false, due: 2, reviews: 1, srsHits: 1 } }
};

async function ouvrir(page, scene, niveau, depuis) {
  await page.goto(base + "/banc.html");
  await page.evaluate(([s, n, d, deja]) => {
    localStorage.clear();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(deja));
    progressCache = null;
    window.SCENE_DU_JOUR = { nom: s }; window.NIVEAU = n;
    ouvrirSceneSeance();
    sceneOuverteDepuis = d;
  }, [scene, niveau, depuis, DEJA]);
  const cadre = page.frame({ url: /visuel\/prototype\/index\.html/ }) ||
                (await (await page.waitForSelector("#sceneCadre")).contentFrame());
  await cadre.waitForFunction(() => typeof attenteToucher !== "undefined" && document.querySelector("#carte .question"));
  return cadre;
}
const progression = page => page.evaluate(() => JSON.parse(JSON.stringify(getProgress())));
const attendre = ms => new Promise(r => setTimeout(r, ms));

let base;
(async () => {
  await new Promise(r => serveur.listen(0, "127.0.0.1", r));
  base = "http://127.0.0.1:" + serveur.address().port;
  const nav = await chromium.launch();
  const page = await nav.newPage();
  page.on("pageerror", e => { console.log("  erreur de page : " + e.message); ko++; });

  // ---------------------------------------------------------------------
  console.log("\nUNE SEANCE A1 : TROIS « TROUVE ! », JUSTE, FAUX, JUSTE");
  let cadre = await ouvrir(page, "klassenzimmer", "A1", "seance");
  const avant = await progression(page);
  const reponses = [];
  for (const juste of [true, false, true]) {
    const r = await cadre.evaluate(j => {
      const cible = attenteToucher;
      const proprio = proprietaire(cible);
      const aLui = z => !proprio || racine(z) === proprio;
      const bonnes = zonesDe(cible).filter(id => aLui(P[id]));
      // Une mauvaise zone : une qui ne porte la cible ni elle ni son support.
      const fausse = S.points.find(p => !touche(p, cible) && !(proprio && estPersonne(racine(p)) && racine(p) !== proprio));
      toucher(j ? bonnes[0] : fausse.id);
      const r = { cible, theme: A_TROUVER.find(t => t.mot === cible).theme, juste: j };
      document.getElementById("suite").click();
      return r;
    }, juste);
    reponses.push(r);
  }
  await attendre(300);
  const apres = await progression(page);
  console.log("  mots demandes : " + reponses.map(r => r.cible + (r.juste ? " (juste)" : " (faux)")).join(", "));
  const changes = [];
  for (const k of new Set([...Object.keys(avant), ...Object.keys(apres)]))
    for (const i of new Set([...Object.keys(avant[k] || {}), ...Object.keys(apres[k] || {})]))
      if (JSON.stringify((avant[k] || {})[i]) !== JSON.stringify((apres[k] || {})[i])) changes.push(k + "#" + i);
  ok("exactement trois mots ont change (" + changes.join(", ") + ")", changes.length === 3);
  const etats = await page.evaluate(rs => rs.map(r => {
    const it = carteDeScene({ mot: r.cible, theme: r.theme });
    return { it: it && (it.themeId + "#" + cleMot(it.themeId, it.index)), mot: it && it.word[0], st: getWordState(it.themeId, it.index) };
  }), reponses);
  ok("ce sont les trois mots de la scene", etats.every(e => changes.includes(e.it)));
  etats.forEach((e, n) => {
    const st = e.st, dans = (st.due - Date.now()) / 60000;
    if (reponses[n].juste)
      ok(e.mot + " juste -> une pastille, revient dans ~10 min (comme « Je savais »)",
         st.srsHits === 1 && st.reviews === 1 && !st.mastered && dans > 9 && dans <= 10);
    else
      ok(e.mot + " faux -> pastilles a zero, revient dans ~2 min (comme « Encore »)",
         st.srsHits === 0 && st.reviews === 1 && dans > 1 && dans <= 2);
  });
  ok("les mots deja travailles n'ont pas bouge",
     JSON.stringify(apres.familie_a1) === JSON.stringify(avant.familie_a1)
     && JSON.stringify(apres.verben) === JSON.stringify(avant.verben));
  const neufs = await page.evaluate(() => etatNeufsDuJour().n);
  ok("trois mots neufs comptes dans la dose du jour", neufs === 3);
  ok("aucune fin de scene envoyee avant la fin", !(await page.evaluate(() => journal.includes("cartes"))));
  // La fin : « vers les cartes » ramene a la seance.
  await cadre.evaluate(() => document.getElementById("encore").click());
  await attendre(200);
  ok("« fini » enchaine sur les cartes", await page.evaluate(() => journal.includes("cartes")));

  // ---------------------------------------------------------------------
  console.log("\nUN MOT PAS ENCORE ECHU, JUSTE : IL NE BOUGE PAS ; FAUX : IL RETOMBE");
  cadre = await ouvrir(page, "klassenzimmer", "A1", "seance");
  const cible = await cadre.evaluate(() => attenteToucher);
  const r2 = await page.evaluate(m => {
    const it = carteDeScene({ mot: m });
    const st = getWordState(it.themeId, it.index);
    Object.assign(st, { srsHits: 2, srsDailyStreak: 2, due: Date.now() + 3 * 86400000, reviews: 2 });
    setWordState(it.themeId, it.index, st);
    return { id: it.themeId, i: it.index, avant: JSON.stringify(st) };
  }, cible);
  await cadre.evaluate(() => { const c = attenteToucher, p = proprietaire(c);
    toucher(zonesDe(c).filter(id => !p || racine(P[id]) === p)[0]); });
  await attendre(200);
  ok("juste a trois jours de l'echeance : rien n'est ecrit",
     await page.evaluate(r => JSON.stringify(getWordState(r.id, r.i)) === r.avant, r2));
  await page.evaluate(m => revisionDeScene({ mot: m, juste: false }), cible);
  ok("faux : l'echelle repart de zero",
     await page.evaluate(r => { const s = getWordState(r.id, r.i); return s.srsHits === 0 && s.srsDailyStreak === 0 && s.reviews === 3; }, r2));

  // ---------------------------------------------------------------------
  console.log("\nLA QUATRIEME REUSSITE MAITRISE LE MOT, COMME UNE CARTE");
  const r3 = await page.evaluate(() => {
    const it = carteDeScene({ mot: "stehen", cat: "verbe" });
    setWordState(it.themeId, it.index, { srsHits: 3, srsDailyStreak: 2, due: Date.now() - 1, reviews: 3 });
    journal.length = 0;
    revisionDeScene({ mot: "stehen", cat: "verbe", juste: true });
    const s = getWordState(it.themeId, it.index);
    return { key: it.themeId + "#" + cleMot(it.themeId, it.index), s, jours: (s.due - Date.now()) / 86400000, journal: journal.slice() };
  });
  ok("stehen (verbe, cle stable « " + r3.key + " ») maitrise, entretien a 16 j",
     r3.key === "verben#stehen" && r3.s.mastered && r3.s.srsHits === 4 && r3.s.entretiens === 1
     && r3.jours > 15.9 && r3.jours <= 16 && r3.journal.includes("maitrise"));

  // ---------------------------------------------------------------------
  console.log("\nLES QUESTIONS B1 : SEULES CELLES QUI PORTENT UN MOT COMPTENT");
  cadre = await ouvrir(page, "klassenzimmer", "B1", "seance");
  const avantB1 = await progression(page);
  const qs = [];
  for (let n = 0; n < 3; n++) {
    const q = await cadre.evaluate(() => {
      const q = COUCHES[niveau].ordre[i];
      if (q._trouve) { const c = attenteToucher, p = proprietaire(c);
        toucher(zonesDe(c).filter(id => !p || racine(P[id]) === p)[0]);
        document.getElementById("suite").click(); return { trouve: q._trouve.mot }; }
      const k = [...document.querySelectorAll("#bas .choix")].findIndex(b => b.textContent === q.c[0]);
      document.querySelectorAll("#bas .choix")[k].click();
      document.querySelector("#bas .suite").click();
      return { q: q.q, revise: q.revise ? q.revise.mot : null };
    });
    qs.push(q);
  }
  await attendre(300);
  const apresB1 = await progression(page);
  const attendus = qs.map(q => q.revise || q.trouve).filter(Boolean);
  qs.forEach(q => console.log("    " + (q.q || "Trouve ! " + q.trouve) + "  ->  " + (q.revise || q.trouve || "(aucun mot)")));
  let nb = 0;
  for (const k of Object.keys(apresB1))
    for (const i of Object.keys(apresB1[k]))
      if (JSON.stringify((avantB1[k] || {})[i]) !== JSON.stringify(apresB1[k][i])) nb++;
  // Deux questions peuvent travailler le meme verbe : la seconde reussite,
  // non echue, n'ecrit rien.
  ok("autant de mots changes que de mots distincts portes (" + new Set(attendus).size + ")",
     nb === new Set(attendus).size);

  // ---------------------------------------------------------------------
  console.log("\nDEPUIS LE TABLEAU DE BORD, RIEN NE S'ECRIT");
  cadre = await ouvrir(page, "klassenzimmer", "A1", "admin");
  const avantA = await progression(page);
  await cadre.evaluate(() => { const c = attenteToucher, p = proprietaire(c);
    toucher(zonesDe(c).filter(id => !p || racine(P[id]) === p)[0]); });
  await attendre(200);
  ok("une reponse juste ne change pas la progression",
     JSON.stringify(await progression(page)) === JSON.stringify(avantA));

  // ---------------------------------------------------------------------
  console.log("\nHORS SEANCE (?seance absent), LA SCENE N'ENVOIE RIEN");
  await page.goto(base + "/banc.html");
  const envoyes = await page.evaluate(async () => {
    const recus = [];
    addEventListener("message", e => { if (e.data && e.data.type === "reponse") recus.push(e.data); });
    const f = document.getElementById("sceneCadre");
    f.src = baseScenes() + "index.html?scene=klassenzimmer";
    await new Promise(r => f.onload = r);
    const w = f.contentWindow;
    w.modeA1 = "trouver"; w.eval("modeA1 = 'trouver'; demarrer();");
    w.eval("toucher(zonesDe(attenteToucher)[0])");
    await new Promise(r => setTimeout(r, 200));
    return recus.length;
  });
  ok("aucun message « reponse »", envoyes === 0);

  // ---------------------------------------------------------------------
  console.log("\nCHAQUE MOT QU'UNE SCENE PEUT ENVOYER SE RETROUVE DANS LE CORPUS");
  const envois = [];
  for (const f of fs.readdirSync(path.join(RACINE, "visuel/prototype")).filter(f => /^scene-.*\.js$/.test(f))) {
    const window = {};
    eval(fs.readFileSync(path.join(RACINE, "visuel/prototype", f), "utf8"));
    const S = window.SCENE;
    for (const p of S.points) for (const m of [p, ...p.aussi])
      envois.push({ scene: f, mot: m.mot, genre: m.genre, theme: m.theme, cat: "nom" });
    for (const c of Object.values(S.couches || {})) for (const q of c.qs || [])
      if (q.revise) envois.push(Object.assign({ scene: f, cat: "nom" }, q.revise));
  }
  const perdus = await page.evaluate(es => es.filter(e => !carteDeScene(e)).map(e => e.scene + " : " + e.mot), envois);
  ok(envois.length + " envois possibles, tous retrouves" + (perdus.length ? " -- perdus : " + perdus.join(", ") : ""),
     perdus.length === 0);

  await nav.close();
  serveur.close();
  console.log(ko ? "\n" + ko + " ECHEC(S)" : "\nOK : tout passe.");
  process.exit(ko ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
