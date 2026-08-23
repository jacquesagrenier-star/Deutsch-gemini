// Service worker Firebase Cloud Messaging pour Wortando.
// Doit être servi depuis la racine de l'app (même dossier qu'index.html) --
// c'est ce fichier qui reçoit et affiche les notifications quand l'onglet
// n'est pas au premier plan (app fermée ou en arrière-plan).
//
// Utilise la variante "compat" du SDK Firebase : les service workers ne
// supportent pas nativement les imports ES module utilisés ailleurs dans
// index.html, `importScripts` est la méthode standard recommandée par
// Firebase pour ce fichier précis.

importScripts('https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.8.0/firebase-messaging-compat.js');

firebase.initializeApp({
    apiKey: "AIzaSyDK9aTVTxDWWrGSIuydHtjSvUTaEguu45U",
    authDomain: "deutschai-b6fbb.firebaseapp.com",
    projectId: "deutschai-b6fbb",
    storageBucket: "deutschai-b6fbb.firebasestorage.app",
    messagingSenderId: "915434419015",
    appId: "1:915434419015:web:bfd33c9e8ba5948af99262"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    const title = (payload.notification && payload.notification.title) || "Wortando";
    const options = {
        body: (payload.notification && payload.notification.body) || "",
        icon: "https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/branding/wortando-app-icon.png",
        badge: "https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/branding/wortando-app-icon.png"
    };
    self.registration.showNotification(title, options);
});
