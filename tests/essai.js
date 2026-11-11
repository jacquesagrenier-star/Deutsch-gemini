// L'essai de 7 jours gere par l'app (modele B, decide le 11 nov. 2026) :
// les jours 1, 5, 7, 8 et 30, le testeur gratuit a vie, le testeur des
// magasins (4 mois offerts), l'abonne, l'horloge du telephone reculee, et
// l'inertie tant que ACCES.actif vaut false.
//
//   node tests/essai.js
//
// Aucun navigateur, aucun verrou : la logique vit entre deux marques dans
// index.html (« ESSAI : LOGIQUE PURE (debut) » ... « (fin) »), sans DOM ni
// stockage. On l'extrait et on l'execute dans un bac a sable.
// Le fuseau est fixe (Europe/Berlin) pour que l'heure du rappel du jour 5 ne
// depende pas de la machine.

process.env.TZ = process.env.TZ || "Europe/Berlin";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const RACINE = path.join(__dirname, "..");
const source = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");
const DEBUT = "// ---- ESSAI : LOGIQUE PURE (debut) ----";
const FIN = "// ---- ESSAI : LOGIQUE PURE (fin) ----";
const a = source.indexOf(DEBUT), b = source.indexOf(FIN);
if(a < 0 || b < a){ console.error("ECHEC : les marques de la logique de l'essai sont introuvables dans index.html"); process.exit(1); }
const ctx = {};
vm.createContext(ctx);
vm.runInContext(source.slice(a, b) + "\n;this.E = { JOUR_MS, ESSAI_JOURS, ESSAI_RAPPEL_JOUR, etatEssaiPur, momentRappelEssai, dateEnMs };", ctx);
const E = ctx.E;

let ok = 0, ko = 0;
const fautes = [];
function verifier(cond, msg){ if(cond) ok++; else { ko++; fautes.push(msg); } }
function egal(x, y, msg){ verifier(x === y, msg + " -- attendu " + JSON.stringify(y) + ", obtenu " + JSON.stringify(x)); }

const J = E.JOUR_MS, H = 3600000;
// Un compte cree le mardi 1er decembre 2026 a 10 h (heure de Berlin).
const CREE = new Date(2026, 11, 1, 10, 0, 0).getTime();
const LANCEMENT = new Date(2026, 10, 20, 0, 0, 0).getTime();   // sortie fictive le 20 nov.
const base = { actif: true, admin: false, accesAVie: false, lancementMs: LANCEMENT, creeMs: CREE };
const au = (jour, heures) => CREE + (jour - 1) * J + (heures || 2) * H;   // « jour N », quelques heures apres l'heure de creation
const etat = (extra) => E.etatEssaiPur(Object.assign({}, base, extra));

// ---------- 0. Inerte avant la sortie ----------
egal(E.etatEssaiPur({ actif: false, creeMs: CREE, maintenantMs: au(30) }).etat, "ouvert", "ACCES.actif false : ouvert, meme au jour 30");
egal(E.etatEssaiPur({ actif: false, admin: true }).etat, "ouvert", "ACCES.actif false : ouvert pour l'admin aussi");
egal(E.etatEssaiPur(null).etat, "ouvert", "sans parametre : ouvert");

// ---------- 1. Les jours de l'essai ----------
{
    const r = etat({ maintenantMs: au(1) });
    egal(r.etat, "essai", "jour 1 : essai");
    egal(r.jour, 1, "jour 1 : numero du jour");
    egal(r.restants, 7, "jour 1 : encore 7 jours");
    egal(r.fin, CREE + 7 * J, "jour 1 : fin = creation + 7 jours");
}
{
    const r = etat({ maintenantMs: CREE + 60000 });
    egal(r.etat, "essai", "une minute apres l'inscription : essai");
    egal(r.restants, 7, "une minute apres l'inscription : encore 7 jours");
}
{
    const r = etat({ maintenantMs: au(5) });
    egal(r.etat, "essai", "jour 5 : essai");
    egal(r.jour, 5, "jour 5 : numero du jour");
    egal(r.restants, 3, "jour 5 : encore 3 jours (5, 6, 7)");
    verifier(r.jour >= E.ESSAI_RAPPEL_JOUR, "jour 5 : la bulle du rappel est due");
}
{
    const r = etat({ maintenantMs: au(4, 23) });
    verifier(r.jour < E.ESSAI_RAPPEL_JOUR, "jour 4 : pas encore de rappel (jour " + r.jour + ")");
}
{
    const r = etat({ maintenantMs: au(7) });
    egal(r.etat, "essai", "jour 7 : encore l'essai");
    egal(r.jour, 7, "jour 7 : numero du jour");
    egal(r.restants, 1, "jour 7 : dernier jour (le compteur dit « dernier jour »)");
}
{
    const r = etat({ maintenantMs: CREE + 7 * J - 1 });
    egal(r.etat, "essai", "la derniere milliseconde du 7e jour : essai");
}
{
    const r = etat({ maintenantMs: CREE + 7 * J });
    egal(r.etat, "gratuit", "la premiere milliseconde du 8e jour : gratuit");
}
{
    const r = etat({ maintenantMs: au(8) });
    egal(r.etat, "gratuit", "jour 8 : version gratuite (l'ecran d'abonnement s'ouvre une fois)");
    egal(r.jour, 8, "jour 8 : numero du jour");
    egal(r.restants, 0, "jour 8 : plus aucun jour d'essai");
    verifier(!!r.fin, "jour 8 : la fin est connue (condition de l'ecran du 8e jour)");
}
{
    const r = etat({ maintenantMs: au(30) });
    egal(r.etat, "gratuit", "jour 30 : version gratuite");
    egal(r.jour, 30, "jour 30 : numero du jour");
}

// ---------- 2. L'horloge du telephone ne prolonge pas l'essai ----------
{
    // Au jour 9, la personne recule l'heure de son telephone au jour 2 : le
    // jeton Firebase emis il y a une heure (heure du serveur) fait plancher.
    const r = etat({ maintenantMs: au(2), plancherServeurMs: au(9) - H });
    egal(r.etat, "gratuit", "horloge reculee au jour 2, serveur au jour 9 : gratuit");
}
{
    const r = etat({ maintenantMs: au(3), plancherServeurMs: au(1) });
    egal(r.restants, 5, "plancher plus ancien que l'horloge : l'horloge compte (jour 3, encore 5 jours)");
}
{
    // `essaiDebut` reecrit plus tard dans le compte ne recule pas le debut.
    const r = etat({ maintenantMs: au(9), debutCompteMs: au(6) });
    egal(r.etat, "gratuit", "essaiDebut reecrit au jour 6 : le debut reste la creation (gratuit au jour 9)");
    // Et s'il est plus ancien que creationTime, c'est lui qui compte.
    const r2 = etat({ maintenantMs: au(6), debutCompteMs: CREE - 2 * J });
    egal(r2.etat, "gratuit", "essaiDebut plus ancien que la creation : le plus tot des deux (gratuit au jour 6)");
}
{
    const r = E.etatEssaiPur({ actif: true, maintenantMs: au(3) });
    egal(r.etat, "essai", "compte pas encore connu : essai (rien ne se ferme sur une inconnue)");
}

// ---------- 3. Le testeur gratuit a vie ----------
egal(etat({ creeMs: LANCEMENT - J, maintenantMs: au(30) }).etat, "testeur", "compte cree la veille de la sortie : testeur a vie, meme au jour 30");
egal(etat({ accesAVie: true, maintenantMs: au(30) }).etat, "testeur", "drapeau accesAVie : testeur a vie au jour 30");
egal(etat({ admin: true, maintenantMs: au(30) }).etat, "testeur", "l'admin : toujours tout");
egal(etat({ creeMs: LANCEMENT, maintenantMs: LANCEMENT + 30 * J }).etat, "gratuit", "compte cree le jour meme de la sortie : pas testeur (essai puis gratuit)");

// ---------- 4. Le testeur des magasins : 4 mois offerts ----------
{
    const jusqua = E.dateEnMs("2027-04-01");
    verifier(jusqua === new Date(2027, 3, 1, 23, 59, 59, 999).getTime(), "accesJusqua « 2027-04-01 » vaut jusqu'a la fin de ce jour");
    egal(etat({ maintenantMs: au(30), offertJusquaMs: jusqua }).etat, "offert", "4 mois offerts, jour 30 : acces complet");
    egal(etat({ maintenantMs: au(110), offertJusquaMs: jusqua }).etat, "offert", "4 mois offerts, jour 110 (21 mars) : acces complet");
    egal(etat({ maintenantMs: new Date(2027, 3, 2, 9).getTime(), offertJusquaMs: jusqua }).etat, "gratuit", "4 mois offerts, le lendemain de la date : version gratuite");
    egal(etat({ maintenantMs: new Date(2027, 3, 2, 9).getTime(), plancherServeurMs: 0, offertJusquaMs: jusqua }).etat, "gratuit", "4 mois offerts expires : gratuit");
    egal(etat({ maintenantMs: new Date(2026, 11, 20).getTime(), plancherServeurMs: new Date(2027, 3, 5).getTime(), offertJusquaMs: jusqua }).etat, "gratuit", "4 mois offerts : l'horloge reculee ne les prolonge pas non plus");
    const ts = { toMillis: () => 1800000000000 };
    egal(E.dateEnMs(ts), 1800000000000, "accesJusqua en Timestamp Firestore");
    egal(E.dateEnMs("pas une date"), null, "accesJusqua illisible : ignore");
    egal(E.dateEnMs(""), null, "accesJusqua vide : ignore");
    egal(E.dateEnMs(undefined), null, "accesJusqua absent : ignore");
}

// ---------- 5. L'abonne ----------
egal(etat({ maintenantMs: au(30), abonne: true }).etat, "abonne", "abonne au jour 30 : acces complet");
egal(etat({ maintenantMs: au(3), abonne: true }).etat, "abonne", "abonne pendant l'essai : abonne (plus de compte a rebours)");

// ---------- 6. Le moment du rappel du jour 5 ----------
{
    const quand = E.momentRappelEssai(CREE, "19:00");
    const d = new Date(quand);
    egal(d.getDate(), 5, "rappel : le 5 decembre (5e jour d'un compte cree le 1er a 10 h)");
    egal(d.getHours(), 19, "rappel : a 19 h");
    const r = etat({ maintenantMs: quand });
    egal(r.jour, 5, "rappel : il tombe bien au jour 5");
    egal(r.restants, 3, "rappel : il reste 3 jours a ce moment-la");
}
{
    // Compte cree a 22 h : le 5e jour commence le 5 a 22 h ; le rappel de 19 h
    // du 5 serait encore le 4e jour -> le 6 a 19 h.
    const tard = new Date(2026, 11, 1, 22, 0).getTime();
    const d = new Date(E.momentRappelEssai(tard, "19:00"));
    egal(d.getDate(), 6, "compte cree a 22 h : rappel le 6 a 19 h (jamais avant le 5e jour)");
    verifier(E.momentRappelEssai(tard, "19:00") < tard + 7 * J, "compte cree a 22 h : rappel avant la fin de l'essai");
}
{
    const d = new Date(E.momentRappelEssai(CREE, "07:30"));
    egal(d.getHours() + ":" + d.getMinutes(), "7:30", "rappel a l'heure du rappel quotidien (07:30)");
    egal(new Date(E.momentRappelEssai(CREE, "n'importe quoi")).getHours(), 19, "heure illisible : 19 h");
    egal(E.momentRappelEssai(null, "19:00"), null, "debut inconnu : pas de rappel");
}

// ---------- 7. Le code autour de la logique ----------
// Les gardes que la logique pure ne peut pas voir : relues dans le source.
const extrait = (debut, n) => { const i = source.indexOf(debut); return i < 0 ? "" : source.slice(i, i + (n || 1500)); };
verifier(/const ACCES = \{ actif: false,/.test(source), "ACCES.actif vaut toujours false dans index.html (a ne passer a true que le jour de la sortie)");
verifier(/cleAndroid: "",/.test(source) && /cleIos: "",/.test(source), "les cles RevenueCat sont vides (a remplir par les cles PUBLIQUES le moment venu)");
verifier(!/sk_[A-Za-z0-9]{10,}/.test(source), "aucune cle secrete RevenueCat (sk_…) dans index.html");
verifier(/function achatsPermis\(\)\{ return ACCES\.actif \|\| isAdminUser\(\); \}/.test(source), "les achats restent reserves a l'admin avant la sortie");
verifier(extrait("function majApresChangementAcces(){", 200).indexOf("if(!ACCES.actif && !apercuEssaiJour()) return;") >= 0, "majApresChangementAcces ne fait rien avant la sortie");
verifier(extrait("function majAccesAccueil(){", 200).indexOf("if(!ACCES.actif && !apercuEssaiJour()) return;") >= 0, "ni rappel ni ecran du 8e jour avant la sortie");
verifier(extrait("async function programmerRappelEssai(){", 400).indexOf("if(!ACCES.actif || apercuEssaiJour()) return;") >= 0, "aucune notification d'essai avant la sortie, ni pour une simulation");
verifier(extrait("function lireAccesDuCompte(d, user){", 600).indexOf("if(ACCES.actif && user && !d.essaiDebut") >= 0, "essaiDebut n'est ecrit qu'apres la sortie");
verifier(extrait("function apercuEssaiJour(){", 120).indexOf("if(!isAdminUser()) return 0;") >= 0, "la simulation de l'essai est reservee a l'admin");
// Les mots deja rencontres restent en revision (decide le 2 oct., v694).
verifier(/function filtrerGratuit\(items\)\{[\s\S]{0,200}!estNeuf\(getWordState\(it\.themeId, it\.index\)\)/.test(source), "version gratuite : les mots deja rencontres pendant l'essai restent en revision");

// ---------- 8. Les textes ----------
const CLES = ["essai_compteur", "essai_compteur_dernier", "essai_rappel_titre", "essai_rappel_titre_dernier", "essai_rappel_texte",
    "essai_rappel_ok", "essai_rappel_voir", "essai_notif_titre", "essai_notif_texte", "abo_jour8", "abo_jour8_texte",
    "abo_essai_jusqua", "abo_sous_titre_choisir", "abo_fin_titre", "abo_fin_sous_titre", "abo_gratuit_continuer",
    "gratuit_bienvenue", "abo_sabonner", "abo_merci", "abo_achat_echec", "abo_restaure", "abo_restaure_rien",
    "abo_actif_titre", "abo_actif_texte", "abo_gerer", "abo_web_texte", "abo_web_deja", "abo_maj_app"];
CLES.forEach(k => {
    const n = (source.match(new RegExp("^        " + k + ": \"", "gm")) || []).length;
    egal(n, 11, "la cle " + k + " existe dans les 11 langues d'interface");
});

console.log("Essai de 7 jours : " + ok + " verifications passees, " + ko + " en echec.");
if(ko){ fautes.forEach(f => console.log("  ECHEC : " + f)); process.exit(1); }
