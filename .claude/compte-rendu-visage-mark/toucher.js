// node toucher.js <dossier du prototype> : touche des points du visage de Mark
// dans le gros plan, comme un doigt, et dit quelle partie repond.
const { chromium } = require(process.env.PLAYWRIGHT || "playwright");
const dir = process.argv[2];
const CAS = [
  ["front, centre", 49.8, 33.5, "stirn"], ["front, haut", 49.6, 33.15, "stirn"],
  ["front, gauche", 47.2, 33.8, "stirn"], ["front, droite", 52.3, 33.8, "stirn"],
  ["oreille D, haut", 54.6, 35.0, "ohr-r"], ["oreille D, milieu", 54.35, 35.4, "ohr-r"],
  ["oreille D, lobe", 54.25, 35.95, "ohr-r"], ["oreille G", 44.9, 36.0, "ohr-l"],
  ["oeil D, iris", 51.6, 35.17, "auge-r"], ["oeil D, coin int.", 51.15, 35.17, "auge-r"],
  ["oeil D, coin ext.", 52.35, 35.17, "auge-r"], ["oeil G, iris", 47.8, 35.17, "auge-l"],
  ["sourcil D, int.", 51.1, 34.8, "augenbraue-r"], ["sourcil D, ext.", 52.6, 34.8, "augenbraue-r"],
  ["joue D", 53.3, 36.6, "wange-r"],
  ["menton, centre", 50, 38.5, "kinn"], ["menton, bas", 50, 38.85, "kinn"], ["menton, cote", 49.0, 38.6, "kinn"],
  ["cou, haut", 50, 39.5, "hals"], ["cou, milieu", 49.8, 40.3, "hals"],
  ["cheveux, haut", 49.8, 31.0, "haar"], ["cheveux, milieu", 49.8, 32.3, "haar"],
  ["cheveux, gauche", 46.0, 32.0, "haar"], ["cheveux, droite", 53.5, 32.0, "haar"],
  ["nez", 50, 36.2, "nase"], ["bouche", 50, 37.3, "zahn"],
];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 375, height: +(process.argv[3] || 812) } });
  const erreurs = []; p.on("pageerror", e => erreurs.push(e.message));
  await p.goto("file://" + dir + "/index.html?scene=arztpraxis");
  await p.waitForTimeout(500);
  // ouvrir le gros plan en touchant le visage dans la scene
  const r = await p.evaluate(() => { const r = document.getElementById("scene").getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; });
  await p.mouse.click(r[0] + r[2] * 0.50, r[1] + r[3] * 0.36);
  await p.waitForTimeout(800);
  if (!(await p.$(".gros-plan"))) { console.log("gros plan pas ouvert"); process.exit(1); }
  await p.evaluate(() => { window.__t = []; const v = window.toucher; window.toucher = (id, pt) => { window.__t.push(id); return v(id, pt); }; });
  let ok = 0;
  for (const [nom, x, y, attendu] of CAS) {
    const id = await p.evaluate(([x, y]) => {
      window.__t = [];
      const el = document.querySelector(".gros-plan"), r = el.getBoundingClientRect(), [cx, cy, w, h] = [43, 28, 13.6, 13.6];
      return [r.left + (x - cx) / w * r.width, r.top + (y - cy) / h * r.height];
    }, [x, y]).then(async ([X, Y]) => { await p.mouse.click(X, Y); await p.waitForTimeout(60); return p.evaluate(() => window.__t[0] || "(rien)"); });
    const bon = id === attendu; ok += bon;
    console.log((bon ? "  ok   " : "  FAUX ") + nom.padEnd(20) + " -> " + id + (bon ? "" : "   (attendu " + attendu + ")"));
  }
  console.log(`  ${ok}/${CAS.length}` + (erreurs.length ? "   erreurs JS : " + erreurs.join(" | ") : ""));
  await b.close();
})();
