const { chromium } = require(process.env.PLAYWRIGHT || "playwright");
const dir = process.argv[2];
const CAS = [
  ["affiche, droite", 72, 35, "poster"], ["squelette du milieu, jambes", 60, 35, "poster"],
  ["poumon", 59.9, 28.1, "lunge"], ["cotes (gauche)", 50.4, 27.9, "rippe"],
  ["colonne", 69.4, 28.6, "wirbelsaeule"], ["os (femur)", 68, 32.8, "knochen"],
  ["tete de Mark, centre", 49.8, 33.5, "(rien)"], ["tete de Mark, bord droit", 54.8, 32.5, "?"],
  ["squelette gauche, crane", 46.5, 24.5, "?"],
];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 375, height: 1200 } });
  const err = []; p.on("pageerror", e => err.push(e.message));
  await p.goto("file://" + dir + "/index.html?scene=arztpraxis");
  await p.waitForTimeout(500);
  const r = await p.evaluate(() => { const r = document.getElementById("scene").getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; });
  await p.mouse.click(r[0] + r[2] * 0.70, r[1] + r[3] * 0.25);
  await p.waitForTimeout(800);
  if (!(await p.$(".gros-plan"))) { console.log("gros plan pas ouvert"); process.exit(1); }
  await p.evaluate(() => { const v = window.toucher; window.toucher = (id, pt) => { window.__t.push(id); return v(id, pt); }; });
  for (const [nom, x, y, att] of CAS) {
    const g = await p.evaluate(() => { window.__t = []; const r = document.querySelector(".gros-plan").getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; });
    await p.mouse.click(g[0] + (x - 43) / 34 * g[2], g[1] + (y - 14.3) / 34 * g[3]);
    await p.waitForTimeout(60);
    const id = await p.evaluate(() => window.__t[0] || "(rien)");
    console.log("  " + nom.padEnd(28) + " -> " + id + (att === "?" ? "" : id === att ? "   ok" : "   FAUX (attendu " + att + ")"));
  }
  // capture : l'anneau de das Poster
  const g = await p.evaluate(() => { const r = document.querySelector(".gros-plan").getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; });
  await p.mouse.click(g[0] + (72 - 43) / 34 * g[2], g[1] + (35 - 14.3) / 34 * g[3]);
  await p.waitForTimeout(400);
  await p.screenshot({ path: process.argv[3], clip: { x: g[0], y: g[1], width: g[2], height: g[3] } });
  if (err.length) console.log("  erreurs JS : " + err.join(" | "));
  await b.close();
})();
