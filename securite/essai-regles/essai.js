// Banc d'essai des regles corrigees, dans l'EMULATEUR local (projet fictif
// demo-wortando : rien ne part vers le vrai Firebase).
const fs = require("fs");
const path = require("path");
const { initializeTestEnvironment, assertSucceeds, assertFails } = require("@firebase/rules-unit-testing");
const { doc, setDoc, updateDoc, getDoc, getDocs, collection, deleteDoc, serverTimestamp, deleteField, Timestamp } = require("firebase/firestore");

const ADMIN_UID = "SOq5GGdxLsXGVaJWLiS3thtNGLE2";
// Les regles corrigees reconnaissent l'admin par son uid : l'adresse n'y joue
// aucun role. Pour comparer avec les regles EN LIGNE (qui la lisent), passer
// la vraie adresse par ADMIN_EMAIL.
const ADMIN_EMAIL = process.env.ADMIN_EMAIL || "admin@example.com";
const REGLES = process.env.REGLES || path.join(__dirname, "..", "firestore-corrige.rules");

let ok = 0, ko = 0;
async function cas(nom, attendu, fn){
    try{
        await (attendu ? assertSucceeds(fn()) : assertFails(fn()));
        ok++; console.log("  ok   " + nom);
    }catch(e){
        ko++; console.log("  ECHEC " + nom + " -- " + String(e.message || e).slice(0, 160));
    }
}

function resume(email, extra){
    return Object.assign({
        email, firstName: "Anna", masteredCount: 12, vusCount: 40, totalCount: 8000, streak: 3,
        retoursUsager: "", vocabDemandes: [], synonymesEcartes: "", langueInterface: "fr",
        appareil: "Android", versionNative: "19", updatedAt: serverTimestamp()
    }, extra || {});
}

(async () => {
    const env = await initializeTestEnvironment({
        projectId: "demo-wortando",
        firestore: { rules: fs.readFileSync(REGLES, "utf8"), host: "127.0.0.1", port: 8085 }
    });
    const anna = env.authenticatedContext("annaUid", { email: "anna@example.com" }).firestore();
    const bob = env.authenticatedContext("bobUid", { email: "bob@example.com" }).firestore();
    const admin = env.authenticatedContext(ADMIN_UID, { email: ADMIN_EMAIL }).firestore();
    const fauxAdmin = env.authenticatedContext("autreUid", { email: ADMIN_EMAIL }).firestore();
    const anonyme = env.unauthenticatedContext().firestore();

    console.log("RESUMES (ce que lit le tableau de bord)");
    for(const coll of ["resumes", "resumenesEs", "resumesEn", "resumesPt", "resumesJa"]){
        await env.clearFirestore();
        console.log(" " + coll);
        await cas("cree son resume normal", true, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com"), { merge: true }));
        await cas("le met a jour (merge)", true, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { vusCount: 41 }), { merge: true }));
        await cas("prenom a balise, court : accepte (l'app l'affiche en texte)", true, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { firstName: "<img src=x onerror=alert(1)>" }), { merge: true }));
        await cas("prenom de 61 caracteres : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { firstName: "a".repeat(61) }), { merge: true }));
        await cas("retours de 20 001 caracteres : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { retoursUsager: "a".repeat(20001) }), { merge: true }));
        await cas("retours de 20 000 caracteres : accepte", true, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { retoursUsager: "a".repeat(20000) }), { merge: true }));
        await cas("vusCount en texte : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { vusCount: "<b>9</b>" }), { merge: true }));
        await cas("appareil de 200 caracteres : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { appareil: "x".repeat(200) }), { merge: true }));
        await cas("151 mots demandes : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { vocabDemandes: Array(151).fill({ m: "x" }) }), { merge: true }));
        await cas("champ inconnu : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { html: "<script>" }), { merge: true }));
        await cas("s'ouvre un essai : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), { essais: ["anglais"] }, { merge: true }));
        await cas("s'ouvre les VHS : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), { vhsChaptersEnabled: true }, { merge: true }));
        await cas("s'offre l'acces a vie : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { accesAVie: true }), { merge: true }));
        await cas("s'offre 4 mois : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { accesJusqua: Timestamp.fromDate(new Date("2027-03-11")) }), { merge: true }));
        await cas("se fait passer pour une autre adresse : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), resume("marina@example.com"), { merge: true }));
        await cas("ecrit le resume de quelqu'un d'autre : refuse", false, () => setDoc(doc(bob, coll, "annaUid"), resume("bob@example.com"), { merge: true }));
        await cas("lit son propre resume : refuse (admin seul)", false, () => getDoc(doc(anna, coll, "annaUid")));
        await cas("l'admin lit la liste", true, () => getDocs(collection(admin, coll)));
        await cas("la meme adresse que l'admin sur un autre compte : refuse", false, () => getDocs(collection(fauxAdmin, coll)));
        await cas("l'admin ouvre un essai dans le resume", true, () => setDoc(doc(admin, coll, "annaUid"), { essais: ["anglais"], vhsChaptersEnabled: true }, { merge: true }));
        await cas("la personne sauvegarde ensuite normalement (essai deja la)", true, () => setDoc(doc(anna, coll, "annaUid"), resume("anna@example.com", { vusCount: 50 }), { merge: true }));
        await cas("l'admin reconstruit un resume", true, () => setDoc(doc(admin, coll, "bobUid"), resume("bob@example.com", { vhsChaptersEnabled: false, essais: [], updatedAt: null }), { merge: true }));
        await cas("la personne supprime son resume (suppression du compte)", true, () => deleteDoc(doc(anna, coll, "annaUid")));
        await cas("anonyme ecrit un resume : refuse", false, () => setDoc(doc(anonyme, coll, "annaUid"), resume("anna@example.com"), { merge: true }));
    }

    console.log("USERS (progression allemande et acces)");
    await env.clearFirestore();
    await cas("inscription : profil", true, () => setDoc(doc(anna, "users", "annaUid"), { email: "anna@example.com", firstName: "Anna", inviteCode: "ABCD2345", createdAt: serverTimestamp() }, { merge: true }));
    await cas("sauvegarde de la progression", true, () => setDoc(doc(anna, "users", "annaUid"), { progressJson: "{}", vusCount: 3, updatedAt: serverTimestamp(), dailyGoalTarget: null }, { merge: true }));
    await cas("jeton de notification", true, () => setDoc(doc(anna, "users", "annaUid"), { fcmToken: "t", fcmTokenUpdatedAt: serverTimestamp() }, { merge: true }));
    await cas("langue apprise", true, () => setDoc(doc(anna, "users", "annaUid"), { langueApprise: "es" }, { merge: true }));
    await cas("lit sa progression", true, () => getDoc(doc(anna, "users", "annaUid")));
    await cas("s'ouvre l'anglais : refuse", false, () => setDoc(doc(anna, "users", "annaUid"), { essais: ["anglais"] }, { merge: true }));
    await cas("s'ouvre les VHS : refuse", false, () => updateDoc(doc(anna, "users", "annaUid"), { vhsChaptersEnabled: true }));
    await cas("compte neuf cree avec un essai : refuse", false, () => setDoc(doc(bob, "users", "bobUid"), { email: "bob@example.com", essais: ["examens"] }));
    await cas("un autre lit ma progression : refuse", false, () => getDoc(doc(bob, "users", "annaUid")));
    await cas("un autre ecrit ma progression : refuse", false, () => setDoc(doc(bob, "users", "annaUid"), { progressJson: "{}" }, { merge: true }));
    await cas("l'admin ouvre l'anglais", true, () => updateDoc(doc(admin, "users", "annaUid"), { essais: ["anglais"] }));
    await cas("l'admin ouvre les VHS", true, () => updateDoc(doc(admin, "users", "annaUid"), { vhsChaptersEnabled: true }));
    await cas("l'admin touche a la progression : refuse", false, () => updateDoc(doc(admin, "users", "annaUid"), { progressJson: "x" }));
    await cas("la personne sauvegarde ensuite normalement (essai deja la)", true, () => setDoc(doc(anna, "users", "annaUid"), { progressJson: "{\"a\":1}", updatedAt: serverTimestamp() }, { merge: true }));
    await cas("l'admin lit la liste", true, () => getDocs(collection(admin, "users")));
    await cas("un testeur lit la liste : refuse", false, () => getDocs(collection(anna, "users")));
    await cas("la personne supprime son document", true, () => deleteDoc(doc(anna, "users", "annaUid")));

    console.log("USERS : L'ABONNEMENT (acces offerts, debut de l'essai)");
    await env.clearFirestore();
    const dans4mois = () => Timestamp.fromDate(new Date("2027-03-11"));
    const hier = () => Timestamp.fromDate(new Date("2026-11-10"));
    await cas("inscription : profil", true, () => setDoc(doc(anna, "users", "annaUid"), { email: "anna@example.com", firstName: "Anna", inviteCode: "ABCD2345", createdAt: serverTimestamp() }, { merge: true }));
    await cas("compte neuf cree avec l'acces a vie : refuse", false, () => setDoc(doc(bob, "users", "bobUid"), { email: "bob@example.com", accesAVie: true }));
    await cas("compte neuf cree avec 4 mois offerts : refuse", false, () => setDoc(doc(bob, "users", "bobUid"), { email: "bob@example.com", accesJusqua: dans4mois() }));
    await cas("s'offre l'acces a vie (merge) : refuse", false, () => setDoc(doc(anna, "users", "annaUid"), { accesAVie: true }, { merge: true }));
    await cas("s'offre l'acces a vie (update) : refuse", false, () => updateDoc(doc(anna, "users", "annaUid"), { accesAVie: true }));
    await cas("s'offre 4 mois : refuse", false, () => setDoc(doc(anna, "users", "annaUid"), { accesJusqua: dans4mois() }, { merge: true }));
    await cas("s'offre l'acces glisse dans une sauvegarde : refuse", false, () => setDoc(doc(anna, "users", "annaUid"), { progressJson: "{}", updatedAt: serverTimestamp(), accesAVie: true }, { merge: true }));
    await cas("debut de l'essai a une date du telephone : refuse", false, () => setDoc(doc(anna, "users", "annaUid"), { essaiDebut: hier() }, { merge: true }));
    await cas("debut de l'essai a l'heure du serveur, la premiere fois : accepte", true, () => setDoc(doc(anna, "users", "annaUid"), { essaiDebut: serverTimestamp() }, { merge: true }));
    await cas("debut de l'essai reecrit (heure du serveur) : refuse", false, () => setDoc(doc(anna, "users", "annaUid"), { essaiDebut: serverTimestamp() }, { merge: true }));
    await cas("debut de l'essai reecrit (date choisie) : refuse", false, () => updateDoc(doc(anna, "users", "annaUid"), { essaiDebut: dans4mois() }));
    await cas("debut de l'essai efface : refuse", false, () => updateDoc(doc(anna, "users", "annaUid"), { essaiDebut: deleteField() }));
    await cas("la sauvegarde ordinaire, essai en cours : acceptee", true, () => setDoc(doc(anna, "users", "annaUid"), { progressJson: "{\"b\":2}", vusCount: 9, updatedAt: serverTimestamp() }, { merge: true }));
    await cas("compte neuf cree avec le debut de l'essai (serveur) : accepte", true, () => setDoc(doc(bob, "users", "bobUid"), { email: "bob@example.com", essaiDebut: serverTimestamp() }, { merge: true }));
    await cas("compte neuf cree avec un debut d'essai choisi : refuse", false, () => setDoc(doc(anna, "users", "autreDoc"), { essaiDebut: hier() }));
    await cas("l'admin offre l'acces a vie", true, () => updateDoc(doc(admin, "users", "annaUid"), { accesAVie: true }));
    await cas("l'admin offre 4 mois", true, () => updateDoc(doc(admin, "users", "bobUid"), { accesJusqua: dans4mois() }));
    await cas("l'admin offre 4 mois en touchant la progression : refuse", false, () => updateDoc(doc(admin, "users", "bobUid"), { accesJusqua: dans4mois(), progressJson: "x" }));
    await cas("l'admin reecrit le debut de l'essai : refuse", false, () => updateDoc(doc(admin, "users", "annaUid"), { essaiDebut: serverTimestamp() }));
    await cas("la meme adresse que l'admin sur un autre compte offre l'acces : refuse", false, () => updateDoc(doc(fauxAdmin, "users", "annaUid"), { accesAVie: true }));
    await cas("apres l'acces offert, la sauvegarde ordinaire : acceptee", true, () => setDoc(doc(anna, "users", "annaUid"), { progressJson: "{\"c\":3}", updatedAt: serverTimestamp(), dailyGoalTarget: null }, { merge: true }));
    await cas("apres l'acces offert, le jeton de notification : accepte", true, () => setDoc(doc(anna, "users", "annaUid"), { fcmToken: null }, { merge: true }));
    await cas("apres les 4 mois offerts, la sauvegarde ordinaire : acceptee", true, () => setDoc(doc(bob, "users", "bobUid"), { progressJson: "{}", updatedAt: serverTimestamp() }, { merge: true }));

    // LE MODE SANS COMPTE (12 nov. 2026, refus d'Apple 5.1.1(v)) : un compte
    // Firebase Anonyme a un uid mais pas d'adresse dans son jeton.
    console.log("SANS COMPTE (Firebase Anonyme)");
    const sc = env.authenticatedContext("scUid", { firebase: { sign_in_provider: "anonymous" } }).firestore();
    await cas("sans compte : sa progression", true, () => setDoc(doc(sc, "users", "scUid"), { progressJson: "{}", vusCount: 2, updatedAt: serverTimestamp() }, { merge: true }));
    await cas("sans compte : lit sa progression", true, () => getDoc(doc(sc, "users", "scUid")));
    await cas("sans compte : la progression d'un autre : refuse", false, () => getDoc(doc(sc, "users", "annaUid")));
    await cas("sans compte : son resume, adresse vide", true, () => setDoc(doc(sc, "resumes", "scUid"), resume(""), { merge: true }));
    await cas("sans compte : son resume avec une adresse : refuse", false, () => setDoc(doc(sc, "resumes", "scUid"), resume("anna@example.com"), { merge: true }));
    await cas("sans compte : s'offre l'acces a vie : refuse", false, () => setDoc(doc(sc, "users", "scUid"), { accesAVie: true }, { merge: true }));
    await cas("avec une adresse, un resume a adresse vide : refuse", false, () => setDoc(doc(anna, "resumes", "annaUid"), resume(""), { merge: true }));
    // Le lien d'une adresse (linkWithCredential) : sa date, une fois, a l'heure du serveur.
    const relie = env.authenticatedContext("scUid", { email: "sc@example.com" }).firestore();
    await cas("lien : date du telephone : refuse", false, () => setDoc(doc(relie, "users", "scUid"), { email: "sc@example.com", adresseLieeLe: hier() }, { merge: true }));
    await cas("lien : heure du serveur, la premiere fois : accepte", true, () => setDoc(doc(relie, "users", "scUid"), { email: "sc@example.com", firstName: "Sam", inviteCode: "ABCD2345", adresseLieeLe: serverTimestamp() }, { merge: true }));
    await cas("lien : reecrit (heure du serveur) : refuse", false, () => setDoc(doc(relie, "users", "scUid"), { adresseLieeLe: serverTimestamp() }, { merge: true }));
    await cas("lien : reecrit (date choisie) : refuse", false, () => updateDoc(doc(relie, "users", "scUid"), { adresseLieeLe: hier() }));
    await cas("lien : efface : refuse", false, () => updateDoc(doc(relie, "users", "scUid"), { adresseLieeLe: deleteField() }));
    await cas("lien : compte neuf cree avec une date choisie : refuse", false, () => setDoc(doc(bob, "users", "bobAutre"), { adresseLieeLe: hier() }));
    await cas("lien : le resume prend l'adresse", true, () => setDoc(doc(relie, "resumes", "scUid"), resume("sc@example.com"), { merge: true }));
    await cas("lien : la sauvegarde ordinaire ensuite : acceptee", true, () => setDoc(doc(relie, "users", "scUid"), { progressJson: "{\"d\":4}", updatedAt: serverTimestamp() }, { merge: true }));
    await cas("se prolonge les 4 mois : refuse", false, () => updateDoc(doc(bob, "users", "bobUid"), { accesJusqua: Timestamp.fromDate(new Date("2030-01-01")) }));
    await cas("retire lui-meme son acces : refuse (admin seul)", false, () => updateDoc(doc(anna, "users", "annaUid"), { accesAVie: deleteField() }));
    await cas("un autre offre l'acces a quelqu'un : refuse", false, () => updateDoc(doc(bob, "users", "annaUid"), { accesAVie: true }));
    await cas("la personne supprime son document (suppression du compte)", true, () => deleteDoc(doc(anna, "users", "annaUid")));

    console.log("AUTRES LANGUES (progression)");
    for(const coll of ["usuariosEs", "usersEn", "usersPt", "usersJa"]){
        await cas(coll + " : sauvegarde", true, () => setDoc(doc(anna, coll, "annaUid"), { progressJson: "{}", updatedAt: serverTimestamp() }, { merge: true }));
        await cas(coll + " : s'offre l'acces a vie : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), { accesAVie: true }, { merge: true }));
        await cas(coll + " : s'offre 4 mois a la creation : refuse", false, () => setDoc(doc(bob, coll, "bobUid"), { accesJusqua: dans4mois() }));
        await cas(coll + " : s'ouvre un essai : refuse", false, () => setDoc(doc(anna, coll, "annaUid"), { essais: ["anglais"] }, { merge: true }));
        await cas(coll + " : un autre ecrit : refuse", false, () => setDoc(doc(bob, coll, "annaUid"), { progressJson: "{}" }, { merge: true }));
        await cas(coll + " : suppression", true, () => deleteDoc(doc(anna, coll, "annaUid")));
    }

    console.log("CODES D'INVITATION (inchanges)");
    await env.withSecurityRulesDisabled(async c => { await setDoc(doc(c.firestore(), "inviteCodes", "ABCD2345"), { used: false, note: "" }); });
    await cas("anonyme verifie un code", true, () => getDoc(doc(anonyme, "inviteCodes", "ABCD2345")));
    await cas("anonyme liste les codes : refuse", false, () => getDocs(collection(anonyme, "inviteCodes")));
    await cas("le nouvel inscrit consomme le code", true, () => updateDoc(doc(anna, "inviteCodes", "ABCD2345"), { used: true, usedAt: serverTimestamp(), usedBy: "annaUid" }));
    await cas("un second le reconsomme : refuse", false, () => updateDoc(doc(bob, "inviteCodes", "ABCD2345"), { used: true, usedAt: serverTimestamp(), usedBy: "bobUid" }));
    await cas("l'admin cree un code", true, () => setDoc(doc(admin, "inviteCodes", "ZZZZ2345"), { used: false, note: "", createdAt: serverTimestamp(), createdBy: ADMIN_EMAIL }));
    await cas("un testeur cree un code : refuse", false, () => setDoc(doc(anna, "inviteCodes", "YYYY2345"), { used: false }));
    await cas("collection inconnue : refuse", false, () => setDoc(doc(anna, "autre", "x"), { a: 1 }));

    await env.cleanup();
    console.log("\n" + ok + " ok, " + ko + " echec(s)");
    process.exit(ko ? 1 : 0);
})().catch(e => { console.error("PLANTE", e); process.exit(2); });
