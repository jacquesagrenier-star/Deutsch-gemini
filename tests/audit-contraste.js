// L'AUDIT DU CONTRASTE (v875, 18 oct. 2026) -- a coller dans la console de la
// page (ou dans l'outil javascript du navigateur), APRES setAppTheme("dark").
//
// Ne le jour ou Jacques a retrouve un texte presque invisible en mode nuit
// (« Qu'est-ce que tu apprends ? ») alors qu'il croyait le mode nuit corrige :
// les correctifs au cas par cas laissaient toujours le suivant. Ce script mesure
// le contraste de CHAQUE texte visible contre le fond reellement peint derriere
// lui (fonds semi-transparents composes, jusqu'au premier fond opaque) et
// renvoie ceux qui passent sous le seuil WCAG AA : 4,5:1, ou 3:1 pour un grand
// texte (24 px, ou 18,66 px en gras). Un fond image (scene, vignette) est
// ignore : on ne sait pas mesurer derriere une photo.
//
// Usage :
//   auditContraste(document.getElementById("settings"))  -> [{ratio, classe, texte, couleur, fond}]
// Parcours conseilles : reglages (tous les <details> ouverts), une seance carte
// par carte (recto ET verso, flipCard()), Premiers pas, A1 voyage (bloc,
// dialogue, jalon), le carnet, chaque panneau openOrbPanel(...) et ce qu'il
// ouvre, puis la meme chose avec ?apprendre=es. Les correctifs vivent dans
// index.html, bloc « v875 : L'AUDIT COMPLET DU MODE NUIT ».
window.auditContraste = function(racine){
    const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p = m[1].split(",").map(x => parseFloat(x)); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
    const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
    const melange = (h, b) => ({ r: h.r * h.a + b.r * (1 - h.a), g: h.g * h.a + b.g * (1 - h.a), b: h.b * h.a + b.b * (1 - h.a), a: 1 });
    const fond = el => {
        const pile = []; let n = el;
        while(n && n.nodeType === 1){
            const cs = getComputedStyle(n), c = parse(cs.backgroundColor);
            if(cs.backgroundImage && cs.backgroundImage !== "none" && !cs.backgroundImage.includes("gradient")) return null;
            if(c && c.a > 0){ pile.push(c); if(c.a >= 1) break; }
            n = n.parentElement;
        }
        let b = pile.length && pile[pile.length - 1].a >= 1 ? pile.pop() : parse(getComputedStyle(document.body).backgroundColor);
        for(let i = pile.length - 1; i >= 0; i--) b = melange(pile[i], b);
        return b;
    };
    const res = [], vus = new Set();
    (racine || document.body).querySelectorAll("*").forEach(el => {
        if(!Array.from(el.childNodes).some(n => n.nodeType === 3 && n.textContent.trim().length > 1)) return;
        const r = el.getBoundingClientRect(); if(r.width < 2 || r.height < 2) return;
        const cs = getComputedStyle(el); if(cs.visibility === "hidden" || cs.display === "none") return;
        let o = 1, n = el; while(n && n.nodeType === 1){ o *= parseFloat(getComputedStyle(n).opacity); n = n.parentElement; }
        if(o < 0.5 || el.closest(".hidden,[hidden]")) return;
        const c = parse(cs.color), bg = fond(el); if(!c || !bg) return;
        const cc = c.a < 1 ? melange(c, bg) : c;
        const L1 = lum(cc), L2 = lum(bg), ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
        const taille = parseFloat(cs.fontSize), gras = parseInt(cs.fontWeight) >= 700;
        const seuil = (taille >= 24 || (taille >= 18.66 && gras)) ? 3 : 4.5;
        if(ratio >= seuil) return;
        const cle = (el.className || el.tagName) + "|" + el.textContent.trim().slice(0, 30);
        if(vus.has(cle)) return; vus.add(cle);
        res.push({ ratio: Math.round(ratio * 100) / 100, classe: (typeof el.className === "string" ? el.className : "") || el.tagName.toLowerCase(),
                   id: el.id || "", texte: el.textContent.trim().slice(0, 40), couleur: cs.color,
                   fond: "rgb(" + Math.round(bg.r) + "," + Math.round(bg.g) + "," + Math.round(bg.b) + ")" });
    });
    return res.sort((a, b) => a.ratio - b.ratio);
};
