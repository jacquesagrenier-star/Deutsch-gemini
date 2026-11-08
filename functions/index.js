// Cloud Function planifiée pour Wortando : envoie un rappel push une fois par
// jour à chaque utilisateur qui a activé les notifications ET qui n'a pas
// encore atteint son objectif quotidien.
//
// NÉCESSITE le plan Firebase Blaze (Cloud Functions planifiées / Cloud
// Scheduler ne fonctionnent pas sur le plan Spark gratuit). Déploiement :
//   cd functions && npm install
//   firebase deploy --only functions
//
// dailyActivityToday/dailyActivityDate/dailyGoalTarget/fcmToken sont écrits
// côté client par syncProgressToCloud() dans index.html.

const { onSchedule } = require("firebase-functions/v2/scheduler");
const { logger } = require("firebase-functions");
const admin = require("firebase-admin");

admin.initializeApp();
const db = admin.firestore();
const messaging = admin.messaging();

// Ajuste l'heure/le fuseau au besoin -- 19h heure de l'Est par défaut.
const SCHEDULE = "0 19 * * *";
const TIMEZONE = "America/Toronto";

function getTodayStr(tz){
    // Format YYYY-MM-DD dans le fuseau donné, pour matcher le format produit
    // par getTodayStr() côté client (index.html).
    const parts = new Intl.DateTimeFormat("en-CA", {
        timeZone: tz,
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
    }).formatToParts(new Date());
    const map = {};
    parts.forEach(p => { map[p.type] = p.value; });
    return `${map.year}-${map.month}-${map.day}`;
}

exports.dailyGoalReminder = onSchedule({ schedule: SCHEDULE, timeZone: TIMEZONE }, async () => {
    const today = getTodayStr(TIMEZONE);
    const snapshot = await db.collection("users").where("fcmToken", "!=", null).get();

    if(snapshot.empty){
        logger.info("Aucun utilisateur avec un token de notification actif.");
        return;
    }

    const staleTokenDocs = [];
    const sends = [];

    snapshot.forEach(docSnap => {
        const data = docSnap.data();
        const token = data.fcmToken;
        if(!token) return;

        // La séance légère pour tous (décision du 8 nov. 2026 ; préparé le 6 nov., À DÉPLOYER PAR JACQUES) :
        // plus d'objectif chiffré. Le client écrit seanceFinieDate (le jour où la
        // séance-leçon est finie) et seancePartiesDate / seancePartiesFaites / seancePartiesTotal
        // (où l'on s'est arrêté). On ne relance pas quelqu'un qui a fini sa séance du jour.
        const seanceFinie = data.seanceFinieDate === today;

        // L'ancienne règle reste vraie pour les comptes qui ont encore l'objectif « N / 20 »
        // (tout le monde tant que la séance légère est en essai admin) : déployer cette version
        // avant la mise en service ne change rien pour eux.
        const goalMetToday = data.dailyActivityDate === today
            && typeof data.dailyActivityToday === "number"
            && typeof data.dailyGoalTarget === "number"
            && data.dailyActivityToday >= data.dailyGoalTarget;

        if(seanceFinie || goalMetToday) return; // fait aujourd'hui, pas de rappel

        const enCours = data.seancePartiesDate === today
            && typeof data.seancePartiesFaites === "number" && data.seancePartiesFaites > 0
            && typeof data.seancePartiesTotal === "number" && data.seancePartiesTotal > data.seancePartiesFaites;
        const seanceLegere = typeof data.seanceFinieDate === "string" || typeof data.seancePartiesDate === "string";
        const body = enCours
            ? `Tu as fait ${data.seancePartiesFaites} partie${data.seancePartiesFaites > 1 ? "s" : ""} sur ${data.seancePartiesTotal} de ta séance : tu reprends là où tu t'es arrêté.`
            : seanceLegere
                ? "Ta séance du jour t'attend : environ 15 minutes."
                : "Tu n'as pas encore atteint ton objectif du jour — quelques minutes suffisent !";

        const message = {
            token,
            notification: {
                title: "Wortando",
                body
            }
        };

        sends.push(
            messaging.send(message).catch(err => {
                logger.warn(`Échec d'envoi pour ${docSnap.id} :`, err.code || err.message);
                // Token expiré/désinstallé : on le retire pour ne plus réessayer en vain.
                if(err.code === "messaging/registration-token-not-registered"
                    || err.code === "messaging/invalid-registration-token"){
                    staleTokenDocs.push(docSnap.id);
                }
            })
        );
    });

    await Promise.all(sends);

    await Promise.all(staleTokenDocs.map(uid =>
        db.collection("users").doc(uid).set({ fcmToken: null }, { merge: true }).catch(() => {})
    ));

    logger.info(`Rappels envoyés : ${sends.length}, tokens périmés nettoyés : ${staleTokenDocs.length}.`);
});
