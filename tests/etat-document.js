// -*- coding: utf-8 -*-
// De quoi a l'air le document Firestore d'un testeur, sans lire son contenu.
//
//     node tests/etat-document.js
//     node tests/etat-document.js --qui jacques
//
// POURQUOI CE CONTROLE EXISTE
//     Le 14 septembre 2026, Jacques a envoye TROIS retours et un seul est
//     arrive. Le chemin est : bouton -> localStorage -> prochaine sauvegarde
//     nuage -> Firestore. Deux coupures possibles, et elles se reparent
//     differemment :
//
//       a) le texte n'a jamais atteint localStorage -- l'app a gele et la page
//          s'est rechargee avant l'envoi. C'est le defaut que le commentaire du
//          brouillon decrit deja dans index.html.
//       b) localStorage l'a bien pris, mais la sauvegarde nuage a echoue. C'est
//          le plafond des 40 000 entrees d'index, repare en v577-v578 -- ou
//          autre chose.
//
//     On ne peut pas lire le localStorage de son telephone d'ici. Mais on peut
//     regarder le document : sa taille, sa date, sa version, et le nombre de
//     retours qu'il porte. Si le document est frais et ne porte qu'un retour,
//     c'est (a). S'il est vieux ou absent, c'est (b).
//
// ⚠️ IL NE LIT AUCUN TEXTE DE RETOUR, seulement des tailles et des dates.
//    Le contenu se lit avec tests/retours.js, qui est fait pour ca.
//
// La cle vit hors du depot, comme pour retours.js : le depot est public.

const fs = require("fs");
const path = require("path");

// Meme resolution que tests/retours.js : le paquet vit HORS du projet, et
// firebase-admin 14 est modulaire -- la racine n'expose plus admin.firestore().
const OUTILS = process.env.WORTANDO_OUTILS || "C:/Users/jacqu/.wortando";
const CLE = path.join(OUTILS, "admin.json");
const FBA = path.join(OUTILS, "node_modules", "firebase-admin", "lib");

const { initializeApp, cert } = require(path.join(FBA, "app"));
const { getFirestore } = require(path.join(FBA, "firestore"));

function taille(o) {
    // Une approximation honnete du poids d'un document : la serialisation JSON.
    // Firestore compte autrement, mais l'ordre de grandeur suffit a voir si
    // l'on approche du 1 Mio.
    try { return JSON.stringify(o).length; } catch (e) { return -1; }
}

function champs(o, profondeur) {
    // Le nombre d'entrees d'index est ce qui a fait echouer les sauvegardes en
    // silence : Firestore indexe CHAQUE champ, y compris au fond des objets.
    if (profondeur > 20 || o === null || typeof o !== "object") return 1;
    let n = 0;
    for (const k of Object.keys(o)) n += 1 + champs(o[k], profondeur + 1);
    return n;
}

(async () => {
    const filtre = (process.argv.includes("--qui")
                    ? process.argv[process.argv.indexOf("--qui") + 1] : "") || "";
    if (!fs.existsSync(CLE)) {
        console.log("  Cle absente : " + CLE);
        process.exit(1);
    }
    initializeApp({ credential: cert(require(CLE)) });
    const snap = await getFirestore().collection("users").get();

    const lignes = [];
    snap.forEach(doc => {
        const d = doc.data() || {};
        const qui = d.email || doc.id;
        if (filtre && !String(qui).toLowerCase().includes(filtre.toLowerCase())) return;
        const r = String(d.retoursUsager || "");
        // Un retour = une ligne qui COMMENCE par « [date... ». C'est la meme
        // regle que retours.js, et elle existe parce qu'un texte colle peut
        // imiter un en-tete : index.html desamorce en ajoutant un espace.
        const n = (r.match(/^\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/gm) || []).length;
        lignes.push({
            qui: qui,
            version: d.appVersion || d.version || "?",
            // updatedAt est un Timestamp Firestore : sans .toDate() la
            // colonne affiche « [object Object] » et ne sert a rien -- or
            // c'est ELLE qui dit si la personne a rouvert l'app depuis le
            // correctif.
            maj: (d.updatedAt && d.updatedAt.toDate)
                 ? d.updatedAt.toDate().toISOString().slice(0, 16)
                 : "jamais",
            // ⚠️ LE DIAGNOSTIC TIENT DANS CES DEUX CHAMPS.
            //   progress (objet)     ancien format, un champ par mot : des
            //                        dizaines de milliers d'entrees d'index,
            //                        donc des sauvegardes qui echouent.
            //   progressJson (texte) format v577 : UNE chaine, index a deux
            //                        chiffres.
            // Le correctif ne s'applique qu'a la PROCHAINE SAUVEGARDE REUSSIE
            // de la personne. Tant qu'elle n'a pas rouvert l'app, son document
            // reste bloque dans l'ancien format -- et tout ce qu'elle apprend
            // entre-temps se perd.
            vieux: !!(d.progress && typeof d.progress === "object"),
            neuf: (typeof d.progressJson === "string"),
            octets: taille(d),
            index: champs(d, 0),
            retours: n,
            coupe: r.indexOf("[COUPE]") >= 0,
            taille_retours: r.length
        });
    });

    if (!lignes.length) { console.log("  Aucun document."); return; }
    lignes.sort((a, b) => b.octets - a.octets);

    console.log("");
    console.log("  " + "document".padEnd(30) + "version".padEnd(9)
                + "poids".padStart(9) + "index".padStart(8)
                + "retours".padStart(9) + "  format".padEnd(10)
                + "derniere sauvegarde");
    console.log("  " + "-".repeat(92));
    for (const l of lignes) {
        console.log("  " + String(l.qui).slice(0, 29).padEnd(30)
            + String(l.version).padEnd(9)
            + (Math.round(l.octets / 1024) + " ko").padStart(9)
            + String(l.index).padStart(8)
            + (l.retours + (l.coupe ? "+C" : "")).padStart(9)
            + (l.neuf ? "  v577" : l.vieux ? "  ANCIEN" : "  -").padEnd(10)
            + String(l.maj));
        if (l.index > 32000) {
            console.log("      ⚠️  " + l.index + " entrees d'index : le plafond "
                        + "Firestore est a 40 000, et il fait echouer les "
                        + "sauvegardes EN SILENCE.");
        }
        if (l.octets > 700000) {
            console.log("      ⚠️  document proche du plafond de 1 Mio.");
        }
        if (l.taille_retours > 3600) {
            console.log("      ⚠️  champ retours a " + l.taille_retours
                        + " caracteres sur 4 000 : les plus anciens vont "
                        + "commencer a tomber.");
        }
    }
    console.log("");
    const bloques = lignes.filter(l => l.index > 40000);
    if (bloques.length) {
        console.log("  \u26a0\ufe0f  " + bloques.length + " document(s) AU-DESSUS DU "
                    + "PLAFOND : leurs sauvegardes echouent en silence, et");
        console.log("      tout ce que ces personnes apprennent se perd a la "
                    + "reconnexion. Le correctif v577");
        console.log("      existe, mais il ne s'applique qu'a leur prochaine "
                    + "ouverture de l'application.");
        console.log("");
    }
    console.log("  Le CONTENU des retours se lit avec : node tests/retours.js");
})().catch(e => { console.error("  " + e.message); process.exit(1); });
