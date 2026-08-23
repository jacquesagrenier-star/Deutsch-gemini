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

        const goalMetToday = data.dailyActivityDate === today
            && typeof data.dailyActivityToday === "number"
            && typeof data.dailyGoalTarget === "number"
            && data.dailyActivityToday >= data.dailyGoalTarget;

        if(goalMetToday) return; // déjà atteint aujourd'hui, pas de rappel

        const message = {
            token,
            notification: {
                title: "Wortando",
                body: "Tu n'as pas encore atteint ton objectif du jour — quelques minutes suffisent !"
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
