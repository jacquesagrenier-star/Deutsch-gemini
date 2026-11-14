// LE BAREME DU TELC DEUTSCH B1·B2 PFLEGE (14 nov. 2026, session pflege-examen). Relevé dans le test modèle
// officiel (pflege/FORMAT-TELC-PFLEGE.md, « Les seuils ») ; aucun texte du telc n'est repris ici.
//
// Fichier PUR : aucune dépendance, aucun accès à la page. La page le charge avant pflege-examen.js ; le contrôle
// tests/pflege_examen.py le fait tourner sous node (module.exports en bas) pour tester chaque seuil.
//
//   Écoute + lecture + éléments de langue (59)   B2 43-59   B1 27-42   sous B1 0-26
//   Écrit (20)                                   B2 15-20   B1 7-14    sous B1 0-6
//   Oral (100)                                   B2 75-100  B1 35-74,5 sous B1 0-34,5
//
// Le certificat : L'ORAL DÉCIDE. Sans B1 à l'oral, aucun certificat.
//   B2 : B2 à l'oral, B2 dans l'une des deux parties écrites, au moins B1 dans l'autre.
//   B1 : B1 ou B2 à l'oral, au moins B1 dans l'une des deux parties écrites ; l'autre peut être sous B1, mais
//        garde un plancher : 19 points sur 59, ou 4 points sur 20 à l'écrit.
// Ces règles redonnent exactement les 13 cas du B1 et les 3 cas du B2 du tableau officiel (le contrôle les
// énumère tous).
"use strict";

const PF_BAREME = (() => {
  const niveauHLS = p => p >= 43 ? "b2" : p >= 27 ? "b1" : "unter";
  const niveauSchreiben = p => p >= 15 ? "b2" : p >= 7 ? "b1" : "unter";
  const niveauSprechen = p => p >= 75 ? "b2" : p >= 35 ? "b1" : "unter";
  const PLANCHER_HLS = 19, PLANCHER_SCHREIBEN = 4;

  // les crans de chaque critère, du meilleur au plus bas : B2 « gut erfüllt », B2 « erfüllt », B1 « gut erfüllt »,
  // B1 « erfüllt », A2, 0
  const CRANS = {
    5: [5, 4, 3, 2, 1, 0],
    10: [10, 8, 6, 4, 2, 0],
    15: [15, 12, 9, 6, 3, 0],
    20: [20, 16, 12, 8, 4, 0]
  };
  const STUFEN = ["B2+", "B2", "B1+", "B1", "A2", "0"];

  // l'écrit : quatre critères sur 5 ; un contenu à 0 met tout l'écrit à 0
  const CRITERES_SCHREIBEN = { inhalt: 5, gestaltung: 5, korrektheit: 5, wortschatz: 5 };
  // l'oral : la tâche (50) partie par partie, la langue (50) sur l'ensemble
  const CRITERES_SPRECHEN = { t1a: 5, t1b: 5, t2a: 15, t2b: 5, t3: 20, aussprache: 15, fluessigkeit: 10, korrektheit: 10, wortschatz: 15 };
  // un exposé lu en entier ne dépasse pas A2 : le cran A2 de la partie 2A
  const PLAFOND_ABGELESEN = 3;   // cran A2 sur 15 (CRANS[15][4])

  function borner(sur, v){
    const crans = CRANS[sur];
    v = Number(v) || 0;
    // la valeur autorisée la plus proche, sans dépasser : un cran officiel seulement
    for (const c of crans) if (v >= c) return c;
    return 0;
  }
  function punkteSchreiben(g){
    g = g || {};
    if (!borner(5, g.inhalt)) return 0;
    let n = 0;
    for (const k in CRITERES_SCHREIBEN) n += borner(CRITERES_SCHREIBEN[k], g[k]);
    return n;
  }
  function punkteSprechen(g){
    g = g || {};
    let n = 0;
    for (const k in CRITERES_SPRECHEN){
      let v = borner(CRITERES_SPRECHEN[k], g[k]);
      if (k === "t2a" && g.abgelesen) v = Math.min(v, PLAFOND_ABGELESEN);
      n += v;
    }
    return n;
  }

  // LE CONTENU DE L'ÉCRIT, calculé sur la fiche (notre règle, d'après les exemples corrigés du manuel : trois
  // informations oubliées font perdre un cran). Aucune information reprise : 0, et l'écrit entier tombe à 0.
  function inhaltPunkte(total, reprises){
    if (!total || reprises <= 0) return 0;
    const oubliees = Math.max(0, total - reprises);
    return Math.max(1, 5 - Math.floor(oubliees / 3));
  }

  function zertifikat(r){
    // r = {hls: points sur 59, schreiben: points sur 20, sprechen: points sur 100}
    const sp = niveauSprechen(r.sprechen), h = niveauHLS(r.hls), s = niveauSchreiben(r.schreiben);
    if (sp === "unter") return null;
    const auMoinsB1 = n => n === "b1" || n === "b2";
    if (sp === "b2" && ((h === "b2" && auMoinsB1(s)) || (s === "b2" && auMoinsB1(h)))) return "b2";
    const plancherH = r.hls >= PLANCHER_HLS, plancherS = r.schreiben >= PLANCHER_SCHREIBEN;
    if ((auMoinsB1(h) && plancherS) || (auMoinsB1(s) && plancherH)) return "b1";
    return null;
  }
  function resultat(r){
    return {
      hls: niveauHLS(r.hls), schreiben: niveauSchreiben(r.schreiben), sprechen: niveauSprechen(r.sprechen),
      zertifikat: zertifikat(r)
    };
  }

  return { niveauHLS, niveauSchreiben, niveauSprechen, zertifikat, resultat, punkteSchreiben, punkteSprechen,
           inhaltPunkte, borner, CRANS, STUFEN, CRITERES_SCHREIBEN, CRITERES_SPRECHEN, PLAFOND_ABGELESEN,
           PLANCHER_HLS, PLANCHER_SCHREIBEN };
})();

if (typeof module !== "undefined" && module.exports) module.exports = PF_BAREME;
