// CE QUE CHAQUE APPAREIL A VU DE SES VERSIONS -- le pendant du journal que
// l'app tient depuis la v684 (champ `journalVersionJson` du document
// Firestore, voir noterVersion() dans index.html).
//
// Ne le 2 octobre 2026 : l'app TestFlight restait en v681 apres fermeture et
// reouverture, alors que le site servait la v683. Ce script dit, pour chaque
// ouverture, si la page venait du cache, si l'app se savait installee, et ce
// que la verification de version a vu et fait.
//
//   node tests/versions.js          les comptes qui ont un journal
//   node tests/versions.js --admin  seulement le compte administrateur
//
// v1054 : TOUTES LES LANGUES (chacune a sa collection) et LES FINS DE PAGE
// (`journalFinsJson`, voir surveillerFinsDePage() dans index.html) : une page
// de l'app native morte sans prevenir, au premier plan ou en arriere-plan.
//
// ⚠️ LECTURE SEULE, comme tests/retours.js et avec la meme cle : le compte
// `lecture-retour` ne porte que le role « Lecteur Cloud Datastore ». Aucune
// ecriture ici, et il ne faut pas en ajouter.
// ⚠️ PAS DE NOM A L'ECRAN : le depot est public et la sortie se colle
// volontiers dans une conversation. Un numero de compte, les dates.

const path = require("path");
const OUTILS = process.env.WORTANDO_OUTILS || "C:/Users/jacqu/.wortando";
const FBA = path.join(OUTILS, "node_modules", "firebase-admin", "lib");
const { initializeApp, cert } = require(path.join(FBA, "app"));
const { getFirestore } = require(path.join(FBA, "firestore"));

const ADMIN = "jacques.a.grenier@gmail.com";

function ligne(e){
    const heure = String(e.t || "").replace("T", " ").slice(0, 19);
    if(e.quoi === "ouverture"){
        return `${heure}  v${e.app}  ouverture   ${e.cache ? "CACHE " : "reseau"}  ${e.natif ? "app native" : "navigateur"}`
             + `  nav=${e.navigation}${e.recherche ? "  " + e.recherche : ""}${e.sw ? "  sw" : ""}`;
    }
    if(e.quoi === "fin"){
        return `${heure}  v${e.app}  FIN ${e.genre === "premier plan" ? "AU PREMIER PLAN" : "en arriere-plan"}`
             + `  (page v${e.appAvant}, ecran ${e.ecran}, langue ${e.langue}, vivante ${e.vie} s,`
             + ` dernier signe ${String(e.dernierPouls || "").slice(11, 19)}, ${e.silence} s avant cette ouverture,`
             + ` ${e.dom} elements${e.tas != null ? ", tas " + e.tas + " Mo" : ""})`;
    }
    return `${heure}  v${e.app}  verification  ${e.resultat}${e.publiee ? "  (en ligne : v" + e.publiee + ")" : ""}`
         + `${e.erreur ? "  " + e.erreur : ""}`;
}

async function main(){
    initializeApp({ credential: cert(require(path.join(OUTILS, "admin.json"))) });
    const seulAdmin = process.argv.includes("--admin");
    const COLLECTIONS = { users: "de", usuariosEs: "es", usersEn: "en", usersJa: "ja", usersPt: "pt" };
    let n = 0;
    for(const [col, langue] of Object.entries(COLLECTIONS)){
        const snap = await getFirestore().collection(col).get();
        snap.docs.forEach((d, i) => {
            const x = d.data();
            if(seulAdmin && String(x.email || "").toLowerCase() !== ADMIN) return;
            let journal = [];
            try{ journal = JSON.parse(x.journalVersionJson || "[]") || []; }catch(e){}
            try{ journal = journal.concat(JSON.parse(x.journalFinsJson || "[]") || []); }catch(e){}
            if(!journal.length) return;
            journal.sort((a, b) => (String(a.t) < String(b.t) ? -1 : 1));
            n++;
            const quand = x.updatedAt && x.updatedAt.toDate ? x.updatedAt.toDate().toISOString().slice(0, 16) : "?";
            console.log(`
[${langue}] compte ${i + 1}${String(x.email || "").toLowerCase() === ADMIN ? " (admin)" : ""} -- derniere sauvegarde ${quand}`);
            journal.forEach(e => console.log("  " + ligne(e)));
        });
    }
    if(!n) console.log("Aucun journal de version : aucun appareil n'a encore sauvegarde depuis la v684.");
}

main().catch(e => { console.error(e.message || e); process.exit(1); });
