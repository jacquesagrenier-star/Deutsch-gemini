// LE TELC A2·B1 -- LA TUILE « PARLER » (6 nov. 2026, session « telc : Parler + examen blanc »).
//
// L'oral a sa propre page, parler.html : c'est le moteur de l'oral du DTZ (micro, video, juges, sections), qui ne
// partage ni le style ni l'ecran de commun.js. Ce module ne fait qu'inscrire sa tuile dans l'accueil du bloc telc
// (commun.js, PROFIL.tuiles : « Sp ») et l'ouvrir dans le meme cadre, en gardant la langue et le mode nuit.
// « depuis=telc » : le « ‹ » de la liste des sections de l'oral ramene ici.

"use strict";

Object.assign(TXT, { sp_titre: "Parler", sp_sous: "Sprechen · à deux, 15 min" });
if (LANGUE === "en") Object.assign(TXT, { sp_titre: "Speaking", sp_sous: "Sprechen · in pairs, 15 min" });

function urlParler(extra){
  const p = new URLSearchParams();
  ["apprendre", "lang", "nuit", "rapide"].forEach(k => { if (Q.get(k)) p.set(k, Q.get(k)); });
  for (const k in (extra || {})) p.set(k, extra[k]);
  return "parler.html?" + p.toString();
}

// Ouverte directement sur l'oral (?partie=Sp, depuis le panneau du bloc telc de l'app) : sans « depuis », le « ‹ » de
// la liste ferme le cadre, comme les Sprachbausteine ouvertes de la meme facon.
DTZ.partie({ id: "Sp", ordre: 70, titre: T("sp_titre"), sous: T("sp_sous"),
  ouvrir: () => { silence(); location.href = urlParler(Q.get("partie") === "Sp" ? {} : { depuis: "telc" }); } });
