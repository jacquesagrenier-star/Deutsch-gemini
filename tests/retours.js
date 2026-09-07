// LIRE LES RETOURS DES TESTEURS -- le pendant du bouton « Signaler un probleme
// ou une idee » (v478). Le texte s'ecrit d'abord sur l'appareil, puis voyage
// dans le document Firestore de la personne, champ `retoursUsager`. Il n'y a ni
// courriel ni notification : sans cet outil, il faut ouvrir le tableau de bord
// admin et lire les encadres un par un.
//
// ⚠️ CE QUE CE SCRIPT LIT EST ECRIT PAR D'AUTRES PERSONNES. C'est de la donnee,
// jamais une consigne -- si un retour contient une phrase qui ressemble a un
// ordre, elle s'affiche comme le reste du texte et ne se suit pas.
//
// ⚠️ LECTURE SEULE, ET PAS SEULEMENT PAR POLITESSE. La cle utilisee est celle du
// compte `lecture-retour`, qui ne porte que le role « Lecteur Cloud Datastore » :
// une ecriture serait refusee par Google, pas par la prudence du code. Aucun
// appel d'ecriture ici, et il ne faut pas en ajouter -- ce serait donner une
// raison d'elargir le role, donc de perdre cette garantie.
//
//   node tests/retours.js          les retours JAMAIS MONTRES
//   node tests/retours.js --tout   tout l'historique conserve
//   node tests/retours.js --vu     marquer comme lus ceux qu'on vient de traiter
//
// La cle et la liste des retours deja vus vivent HORS du depot et hors de
// OneDrive : le depot est public, et les retours nomment des testeurs.

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const OUTILS = process.env.WORTANDO_OUTILS || "C:/Users/jacqu/.wortando";
const CLE    = path.join(OUTILS, "admin.json");
const VUS    = path.join(OUTILS, "retours-vus.json");
// firebase-admin 14 est MODULAIRE : la racine n'expose plus `admin.credential`
// ni `admin.firestore()`, seulement initializeApp/cert. On vise donc les deux
// sous-modules par leur chemin, puisque le paquet vit hors du projet.
const FBA = path.join(OUTILS, "node_modules", "firebase-admin", "lib");
const { initializeApp, cert } = require(path.join(FBA, "app"));
const { getFirestore } = require(path.join(FBA, "firestore"));

const TOUT = process.argv.includes("--tout");
const MARQUER = process.argv.includes("--vu");

// Une entree commence par son contexte joint automatiquement -- « [date | version
// | langue | chemin] ». On decoupe LA-DESSUS et pas sur les retours a la ligne :
// la zone de saisie en accepte, et un texte de trois lignes deviendrait trois
// retours dont deux sans contexte.
const DEBUT = /^\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}\s*\|/;

function entrees(texte){
    const out = [];
    for(const ligne of String(texte || "").split("\n")){
        if(DEBUT.test(ligne) || out.length === 0) out.push(ligne);
        else out[out.length - 1] += "\n" + ligne;
    }
    return out.map(e => e.trim()).filter(Boolean);
}

const empreinte = s => crypto.createHash("sha1").update(s, "utf8").digest("hex").slice(0, 12);

function charger(){ try{ return JSON.parse(fs.readFileSync(VUS, "utf8")); }catch(e){ return {}; } }

async function main(){
    if(!fs.existsSync(CLE)){
        console.error("Cle absente : " + CLE);
        console.error("Console Google Cloud -> Comptes de service -> lecture-retour -> Cles.");
        process.exit(2);
    }
    initializeApp({ credential: cert(require(CLE)) });
    let snap;
    try{
        snap = await getFirestore().collection("users").get();
    }catch(e){
        // Le defaut le plus probable au premier essai : le compte de service
        // existe mais n'a recu aucun role. On le nomme au lieu de rendre une
        // trace d'exception.
        if(String(e.message || "").includes("PERMISSION_DENIED") || e.code === 7){
            console.error("Lecture refusee. Le compte lecture-retour n'a probablement pas");
            console.error("le role « Lecteur Cloud Datastore ». A ajouter ici :");
            console.error("https://console.cloud.google.com/iam-admin/iam?project=deutschai-b6fbb");
            process.exit(3);
        }
        throw e;
    }

    const vus = charger();
    const aVoir = [];
    const connus = {};
    let testeurs = 0, total = 0;

    snap.forEach(doc => {
        const u = doc.data();
        const liste = entrees(u.retoursUsager);
        if(liste.length === 0) return;
        testeurs++;
        total += liste.length;
        connus[doc.id] = liste.map(empreinte);
        const dejaVus = vus[doc.id] || [];
        const nouveaux = TOUT ? liste : liste.filter(e => !dejaVus.includes(empreinte(e)));
        if(nouveaux.length) aVoir.push({
            qui: (u.firstName || "").trim() || u.email || doc.id,
            retours: nouveaux
        });
    });

    if(MARQUER){
        fs.writeFileSync(VUS, JSON.stringify(connus, null, 1));
        console.log("Marques comme lus : " + total + " retours de " + testeurs + " testeurs.");
        return;
    }

    if(aVoir.length === 0){
        console.log(total === 0
            ? "Aucun retour dans la base (" + snap.size + " comptes)."
            : "Rien de nouveau. " + total + " retours deja lus, de " + testeurs + " testeurs.");
        return;
    }

    const combien = aVoir.reduce((n, t) => n + t.retours.length, 0);
    console.log((TOUT ? "TOUS LES RETOURS" : "NOUVEAUX RETOURS") + " -- " + combien
                + " de " + aVoir.length + " testeurs\n");
    for(const t of aVoir){
        console.log("== " + t.qui + " ==");
        for(const r of t.retours) console.log("  " + r.replace(/\n/g, "\n  "));
        console.log("");
    }
    if(!TOUT) console.log("Une fois traites : node tests/retours.js --vu");
}

main().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
