// LE TELC A2·B1 -- LA PARTIE « PARLER » (Sp) (6 nov. 2026, session « telc : Parler + examen blanc »).
//
// L'oral a sa propre page, oral.html : c'est le moteur de l'oral du DTZ (micro, video, juges, sections), qui ne
// partage ni le style ni l'ecran de commun.js. Ce module ne fait qu'inscrire la tuile « Sp » de l'accueil du bloc
// telc et ouvrir oral.html dans le meme cadre, avec les memes parametres (lang, nuit).
//   « depuis=telc » : le « ‹ » de la liste des sections de l'oral ramene a telc.html ;
//   ouverte directement sur l'oral (telc.html?partie=Sp, depuis le panneau de l'app : TELC.direct), sans
//   « depuis » : le « ‹ » de la liste ferme le cadre, comme les autres parties ouvertes de la meme facon.
// Le resultat de l'oral revient par le stockage : resultats.Sp de commun.js (wortando_telc_resultats) et l'etat de
// l'oral (wortando_telcOral, champ « resultat »). L'examen blanc (examen-blanc.js) passe lui aussi par oral.html.

"use strict";

textesTelc({
  fr: { sp_titre: "Parler", sp_sous: "Sprechen · à deux, environ 15 min" },
  en: { sp_titre: "Speaking", sp_sous: "Sprechen · in pairs, about 15 min" }
});

function urlOral(extra){
  const p = new URLSearchParams();
  ["apprendre", "lang", "nuit", "rapide"].forEach(k => { if (Q.get(k)) p.set(k, Q.get(k)); });
  for (const k in (extra || {})) p.set(k, extra[k]);
  return "oral.html?" + p.toString();
}

DTZ.partie({ id: "Sp", ordre: 70, titre: T("sp_titre"), sous: T("sp_sous"),
  ouvrir: () => { silence(); location.href = urlOral(TELC.direct ? {} : { depuis: "telc" }); } });
