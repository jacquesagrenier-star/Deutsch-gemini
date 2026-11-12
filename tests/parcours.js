// OU LES NOUVEAUX INSCRITS S'ARRETENT -- le pendant des etapes notees par
// l'app depuis la v678 (champ `parcoursJson` du document Firestore).
//
// Le 1er octobre 2026, la moitie des comptes avaient un compte et ZERO mot vu :
// ils decrochaient entre l'inscription et la premiere carte, sans qu'on sache
// ou. L'app date maintenant chaque etape une fois -- accueil vu, premiere carte
// affichee, premiere carte passee -- et ce script en fait le tableau. Depuis
// la v700 s'y ajoute la decouverte guidee : finie, ou passee a quelle etape.
// Depuis la v712, la seance du jour : ou l'on decroche dans le paquet.
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

const ETAPES = [["accueil", "accueil vu"], ["carte", "1re carte affichee"], ["reponse", "1re carte passee"]];

// LA DECOUVERTE GUIDEE (v700). L'app note `decouverte_debut`, puis
// `decouverte_etape1` a `decouverte_etape5` a mesure qu'on les atteint (la 5,
// la seance du jour, depuis la v702), et
// enfin `decouverte_finie` ou `decouverte_passee` -- avec, pour celle-ci,
// `decouverte_passee_etape2` (par exemple) : la question est A QUELLE ETAPE on
// la quitte. Une colonne la resume ; le bilan compte chaque issue.
// v806 (15 oct. 2026) : SIX etapes -- la scene a toucher est la 5, la seance
// passe a la 6. Un compte qui a vu la visite avant la v806 n'a pas pu atteindre
// la 6 : chez lui « etape 5 » veut dire la seance.
const DEC_ETAPES = 6;
// 12 nov. 2026 : `decouverte_perdue` -- la visite quittee par un autre ecran (showScreen la referme et rend ses blocs).
function decouverte(p){
    if(p.decouverte_finie) return "finie";
    if(p.decouverte_perdue) return "perdue (autre ecran)";
    // 0 = quittee des l'introduction (v701), avant toute carte.
    for(let n = 0; n <= DEC_ETAPES; n++){
        if(p["decouverte_passee_etape" + n]) return "passee a " + n + "/" + DEC_ETAPES;
    }
    if(p.decouverte_passee) return "passee";
    for(let n = DEC_ETAPES; n >= 1; n--){
        if(p["decouverte_etape" + n]) return "arretee a " + n + "/" + DEC_ETAPES;
    }
    return p.decouverte_debut ? "commencee" : "—";
}

function jour(iso){ return iso ? String(iso).slice(0, 10) : "—"; }

// LA SEANCE DU JOUR (v712). Champ `seancesJson` : une liste
// { d: ouverture, n: cartes prevues, p: passees, f: 1 si finie }, sept jours
// au plus. Relue ici sur SEPT JOURS A PARTIR DE MAINTENANT : un telephone qui
// n'a pas synchronise depuis longtemps garde des seances plus vieilles.
const SEANCES_JOURS = 7;
function seancesRecentes(json, maintenant){
    let l = [];
    try{ l = JSON.parse(json || "[]"); }catch(e){}
    if(!Array.isArray(l)) return [];
    const limite = maintenant - SEANCES_JOURS * 86400000;
    return l.filter(s => s && s.d && Date.parse(s.d) >= limite && s.n > 0)
            .sort((a, b) => String(a.d).localeCompare(String(b.d)));
}

// Une colonne : « 3 : 20/20 ✓, 7/20, 0/20 ».
function colonneSeances(l){
    if(!l.length) return "—";
    return l.length + " : " + l.map(s => s.p + "/" + s.n + (s.f ? " \u2713" : "")).join(", ");
}

// Ou les seances non finies s'arretent, en part du paquet.
const TRANCHES = [["a 0 carte", s => s.p === 0], ["avant 1/4", s => s.p > 0 && s.p < s.n / 4],
                  ["de 1/4 a 1/2", s => s.p >= s.n / 4 && s.p < s.n / 2],
                  ["de 1/2 a 3/4", s => s.p >= s.n / 2 && s.p < 3 * s.n / 4],
                  ["apres 3/4", s => s.p >= 3 * s.n / 4]];
function bilanSeances(listes){
    const toutes = [].concat.apply([], listes);
    const lignes = [];
    lignes.push("seance du jour, " + SEANCES_JOURS + " derniers jours : " + toutes.length + " ouverte(s) par "
                + listes.filter(l => l.length).length + " compte(s)");
    if(!toutes.length) return lignes;
    const finies = toutes.filter(s => s.f);
    const lachees = toutes.filter(s => !s.f);
    lignes.push("  finies".padEnd(22) + finies.length);
    lignes.push("  non finies".padEnd(22) + lachees.length);
    for(const [lib, test] of TRANCHES){
        lignes.push(("    " + lib).padEnd(22) + lachees.filter(test).length);
    }
    const parts = lachees.map(s => s.p / s.n).sort((a, b) => a - b);
    if(parts.length){
        lignes.push("  mediane des non finies : " + Math.round(100 * parts[Math.floor(parts.length / 2)]) + " % du paquet");
    }
    lignes.push.apply(lignes, arretsParActivite(toutes));
    return lignes;
}

// LE BILAN PAR VERSION (lot de l'evaluation, 6 nov. 2026, champs proposes par la session des maquettes).
// Chaque seance porte depuis ce lot :
//   v la version a l'ouverture ; q "f" (la fin) ou "r" (« ‹ »), absent = fermee sans l'un ni l'autre ;
//   o 1 si une seance etait deja finie ce jour-la (avant la v1143 : l'objectif du jour atteint) ; i les fenetres et bulles montrees pendant la seance ;
//   e / er les mots rates proposes a la fin et ceux refaits ; t la duree en secondes ; a l'activite a l'ecran
//   quand on s'arrete (« carte », « ecoute », « parler », « gram », « scene », « reprise »...).
// Les seances d'avant le lot n'ont pas `v` : elles forment le groupe « avant ».
// ⚠️ Une douzaine de comptes donnent quelques dizaines de seances par semaine : assez pour voir un grand
// ecart (moitie moins d'abandons), pas un petit. Deux ou trois semaines avant de conclure.
function mediane(l){
    if(!l.length) return null;
    const x = l.slice().sort((a, b) => a - b);
    return x[Math.floor(x.length / 2)];
}
function pc(n, total){ return total ? Math.round(100 * n / total) + " %" : "—"; }
function arretsParActivite(toutes){
    const lignes = [];
    const groupes = {};
    toutes.forEach(s => { const g = s.v ? "v" + s.v : "avant"; (groupes[g] = groupes[g] || []).push(s); });
    const noms = Object.keys(groupes).sort((a, b) => a === "avant" ? -1 : b === "avant" ? 1 : a.localeCompare(b));
    lignes.push("  par version :");
    noms.forEach(g => {
        const l = groupes[g];
        const finies = l.filter(s => s.f || s.q === "f").length;
        const retour = l.filter(s => !s.f && s.q === "r").length;
        const fermees = l.filter(s => !s.f && !s.q).length;
        const lachees = l.filter(s => !s.f);
        const m = mediane(lachees.map(s => s.p / s.n));
        let ligne = ("    " + g).padEnd(12) + String(l.length).padStart(3) + " seance(s) : finies " + pc(finies, l.length);
        if(g !== "avant") ligne += ", « ‹ » " + pc(retour, l.length) + ", fermees " + pc(fermees, l.length);
        else ligne += ", non finies " + pc(lachees.length, l.length);
        if(m !== null) ligne += " ; mediane des non finies " + Math.round(100 * m) + " % du paquet";
        lignes.push(ligne);
        if(g === "avant") return;
        const obj = lachees.filter(s => s.o).length;
        if(lachees.length) lignes.push("      non finies, une seance deja finie ce jour-la : " + obj + " sur " + lachees.length);
        const mi = mediane(l.map(s => s.i || 0)), mt = mediane(l.filter(s => s.t).map(s => s.t));
        lignes.push("      fenetres et bulles par seance (mediane) : " + (mi === null ? "—" : mi)
                    + " ; duree mediane : " + (mt === null ? "—" : Math.round(mt / 60) + " min"));
        const e = l.reduce((x, s) => x + (s.e || 0), 0), er = l.reduce((x, s) => x + (s.er || 0), 0);
        if(e) lignes.push("      mots rates proposes a la fin : " + e + ", refaits : " + er);
        const parA = {};
        lachees.filter(s => s.a).forEach(s => { parA[s.a] = (parA[s.a] || 0) + 1; });
        const cles = Object.keys(parA).sort((x, y) => parA[y] - parA[x]);
        if(cles.length) lignes.push("      ou l'on s'arrete : " + cles.map(k => k + " " + parA[k]).join(", "));
    });
    return lignes;
}

// LES OUVERTURES DE TUILES (harmonisation des exercices, 7 nov. 2026). Champ `tuilesJson` : { "AAAA-MM-JJ" :
// { data-orbid : nombre } }, quatorze jours au plus. Des nombres seulement : quelle tuile de Tout le contenu sert le
// plus, sur sept jours, et combien de comptes l'ont ouverte.
function tuilesRecentes(json, maintenant){
    let v = {};
    try{ v = JSON.parse(json || "{}") || {}; }catch(e){}
    if(!v || typeof v !== "object" || Array.isArray(v)) return {};
    const limite = new Date(maintenant - SEANCES_JOURS * 86400000).toISOString().slice(0, 10);
    const total = {};
    Object.keys(v).forEach(jour => {
        if(!/^\d{4}-\d{2}-\d{2}$/.test(jour) || jour < limite || !v[jour] || typeof v[jour] !== "object") return;
        Object.keys(v[jour]).forEach(id => { total[id] = (total[id] || 0) + (Number(v[jour][id]) || 0); });
    });
    return total;
}
function bilanTuiles(listes){
    const total = {}, comptes = {};
    listes.forEach(t => Object.keys(t).forEach(id => {
        if(!t[id]) return;
        total[id] = (total[id] || 0) + t[id];
        comptes[id] = (comptes[id] || 0) + 1;
    }));
    const ids = Object.keys(total).sort((a, b) => total[b] - total[a]);
    const lignes = ["tuiles ouvertes, " + SEANCES_JOURS + " derniers jours : " + ids.length + " tuile(s), "
                    + listes.filter(t => Object.keys(t).length).length + " compte(s)"];
    ids.forEach(id => lignes.push(("  " + id).padEnd(26) + String(total[id]).padStart(5) + "  (" + comptes[id] + " compte(s))"));
    return lignes;
}

async function main(){
    const { initializeApp, cert } = require(path.join(FBA, "app"));
    const { getFirestore } = require(path.join(FBA, "firestore"));
    initializeApp({ credential: cert(require(path.join(OUTILS, "admin.json"))) });
    // Les deux langues (v735) : la progression espagnole vit dans usuariosEs.
    const db = getFirestore();
    // v1054 : et les essais (anglais, portugais, japonais) -- Nicole, passee a
    // l'anglais, n'apparaissait plus nulle part.
    let docs = [];
    for(const [coll, marque] of [["users", ""], ["usuariosEs", "es "], ["usersEn", "en "], ["usersPt", "pt "], ["usersJa", "ja "]]){
        docs = docs.concat((await db.collection(coll).get()).docs.map(d => [d, marque]));
    }
    // Sans compte (12 nov. 2026) : un compte qui n'a pas d'adresse dans users.
    const avecAdresse = new Set(docs.filter(([d, m]) => m === "" && d.data().email).map(([d]) => d.id));
    const maintenant = Date.now();
    const lignes = [];
    for(const [d, marque] of docs){
        const x = d.data();
        if(!avecAdresse.has(d.id)) x.langueInterface = (x.langueInterface || "?") + " sans compte";
        let p = {};
        try{ p = JSON.parse(x.parcoursJson || "{}") || {}; }catch(e){}
        const cree = x.createdAt && x.createdAt.toDate ? x.createdAt.toDate().toISOString() : "";
        lignes.push({ cree, p, langue: marque + (x.langueInterface || "?"), vus: x.vusCount || 0, suivi: !!x.parcoursJson,
                      seances: seancesRecentes(x.seancesJson, maintenant), tuiles: tuilesRecentes(x.tuilesJson, maintenant) });
    }
    lignes.sort((a, b) => (b.cree || "").localeCompare(a.cree || ""));

    console.log("compte  inscrit      langue  " + ETAPES.map(e => e[1].padEnd(19)).join("") + "mots vus  " + "decouverte".padEnd(18) + "seances 7 j");
    lignes.forEach((l, i) => {
        const etapes = l.suivi ? ETAPES.map(e => jour(l.p[e[0]]).padEnd(19)).join("")
                               : "(n'a pas ouvert l'app depuis la v678)".padEnd(57);
        console.log(String(i + 1).padStart(6) + "  " + jour(l.cree).padEnd(11) + "  " + l.langue.padEnd(6) + "  " + etapes
                    + String(l.vus).padEnd(10) + decouverte(l.p).padEnd(18) + colonneSeances(l.seances));
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
        console.log("  perdue".padEnd(22) + vues.filter(l => l.p.decouverte_perdue).length);
        console.log("  passee".padEnd(22) + vues.filter(l => l.p.decouverte_passee).length
                    + "  (" + [0, 1, 2, 3, 4, 5].map(n => n + "/" + DEC_ETAPES + " : "
                        + vues.filter(l => l.p["decouverte_passee_etape" + n]).length).join(", ") + ")");
    }
    console.log("\n" + bilanSeances(lignes.map(l => l.seances)).join("\n"));
    console.log("\n" + bilanTuiles(lignes.map(l => l.tuiles)).join("\n"));
}

// Les fonctions de lecture s'essaient sans cle ni reseau (voir le test de la v712).
module.exports = { seancesRecentes, colonneSeances, bilanSeances, tuilesRecentes, bilanTuiles };
if(require.main === module){
    main().catch(e => { console.error(e.message || e); process.exit(1); });
}
