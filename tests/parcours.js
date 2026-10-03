// OU LES NOUVEAUX INSCRITS S'ARRETENT -- le pendant des etapes notees par
// l'app depuis la v678 (champ `parcoursJson` du document Firestore).
//
// Le 1er octobre 2026, la moitie des comptes avaient un compte et ZERO mot vu :
// ils decrochaient entre l'inscription et la premiere carte, sans qu'on sache
// ou. L'app date maintenant chaque etape une fois -- accueil vu, premiere carte
// affichee, premiere carte passee -- et ce script en fait le tableau. Depuis
// la v700 s'y ajoute la decouverte guidee : finie, ou passee a quelle etape.
//
//   node tests/parcours.js
//
// ⚠️ LECTURE SEULE, comme tests/retours.js et avec la meme cle : le compte
// `lecture-retour` ne porte que le role « Lecteur Cloud Datastore ». Aucune
// ecriture ici, et il ne faut pas en ajouter.
// ⚠️ PAS DE NOM A L'ECRAN : le depot est public et la sortie se colle
// volontiers dans une conversation. Un numero, la langue, les dates.

const path = require("path");
const OUTILS = process.env.WORTANDO_OUTILS || "C:/Users/jacqu/.wortando";
const FBA = path.join(OUTILS, "node_modules", "firebase-admin", "lib");
const { initializeApp, cert } = require(path.join(FBA, "app"));
const { getFirestore } = require(path.join(FBA, "firestore"));

const ETAPES = [["accueil", "accueil vu"], ["carte", "1re carte affichee"], ["reponse", "1re carte passee"]];

// LA DECOUVERTE GUIDEE (v700). L'app note `decouverte_debut`, puis
// `decouverte_etape1` a `decouverte_etape4` a mesure qu'on les atteint, et
// enfin `decouverte_finie` ou `decouverte_passee` -- avec, pour celle-ci,
// `decouverte_passee_etape2` (par exemple) : la question est A QUELLE ETAPE on
// la quitte. Une colonne la resume ; le bilan compte chaque issue.
const DEC_ETAPES = 4;
function decouverte(p){
    if(p.decouverte_finie) return "finie";
    for(let n = 1; n <= DEC_ETAPES; n++){
        if(p["decouverte_passee_etape" + n]) return "passee a " + n + "/" + DEC_ETAPES;
    }
    if(p.decouverte_passee) return "passee";
    for(let n = DEC_ETAPES; n >= 1; n--){
        if(p["decouverte_etape" + n]) return "arretee a " + n + "/" + DEC_ETAPES;
    }
    return p.decouverte_debut ? "commencee" : "—";
}

function jour(iso){ return iso ? String(iso).slice(0, 10) : "—"; }

async function main(){
    initializeApp({ credential: cert(require(path.join(OUTILS, "admin.json"))) });
    const snap = await getFirestore().collection("users").get();
    const lignes = [];
    for(const d of snap.docs){
        const x = d.data();
        let p = {};
        try{ p = JSON.parse(x.parcoursJson || "{}") || {}; }catch(e){}
        const cree = x.createdAt && x.createdAt.toDate ? x.createdAt.toDate().toISOString() : "";
        lignes.push({ cree, p, langue: x.langueInterface || "?", vus: x.vusCount || 0, suivi: !!x.parcoursJson });
    }
    lignes.sort((a, b) => (b.cree || "").localeCompare(a.cree || ""));

    console.log("compte  inscrit      langue  " + ETAPES.map(e => e[1].padEnd(19)).join("") + "mots vus  decouverte");
    lignes.forEach((l, i) => {
        const etapes = l.suivi ? ETAPES.map(e => jour(l.p[e[0]]).padEnd(19)).join("")
                               : "(n'a pas ouvert l'app depuis la v678)".padEnd(57);
        console.log(String(i + 1).padStart(6) + "  " + jour(l.cree).padEnd(11) + "  " + l.langue.padEnd(6) + "  " + etapes
                    + String(l.vus).padEnd(10) + decouverte(l.p));
    });

    const suivis = lignes.filter(l => l.suivi);
    console.log("\n" + suivis.length + " compte(s) suivi(s) sur " + lignes.length);
    for(const [cle, lib] of ETAPES){
        console.log("  " + lib.padEnd(20) + suivis.filter(l => l.p[cle]).length);
    }
    const vues = suivis.filter(l => l.p.decouverte_debut);
    if(vues.length){
        console.log("\ndecouverte guidee : " + vues.length + " commencee(s)");
        for(let n = 1; n <= DEC_ETAPES; n++){
            console.log(("  etape " + n + " atteinte").padEnd(22) + vues.filter(l => l.p["decouverte_etape" + n]).length);
        }
        console.log("  finie".padEnd(22) + vues.filter(l => l.p.decouverte_finie).length);
        console.log("  passee".padEnd(22) + vues.filter(l => l.p.decouverte_passee).length
                    + "  (" + [1, 2, 3, 4].map(n => n + "/" + DEC_ETAPES + " : "
                        + vues.filter(l => l.p["decouverte_passee_etape" + n]).length).join(", ") + ")");
    }
}

main().catch(e => { console.error(e.message || e); process.exit(1); });
