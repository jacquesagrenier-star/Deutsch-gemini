// LA POIGNEE DE MAIN DES PAGES EN CADRE (ligne 86 de la file, 13 nov. 2026).
//
// Les themes illustres, les conversations, le telc, le DTZ et les scenes sont des pages
// statiques : servies telles quelles, elles s'ouvriraient sans compte a qui en connait
// l'adresse. La garde d'acces vit dans l'app (index.html : pageOuverte(), aux portes de
// ces pages) ; ici, la page verifie seulement qu'elle a ete ouverte PAR L'APP :
//   - dans le cadre de l'app (meme origine), la page lit window.parent : accesComplet()
//     vrai, ou le chemin que chargerCadre() vient d'ouvrir (window.cadreAutorise) ;
//   - seule (lien partage, adresse tapee) : « Ouvre Wortando pour continuer ».
// Limite assumee : cela arrete le lien partage et l'usage ordinaire, pas une personne
// technique (les donnees restent des fichiers publics). Decision du chef du 13 nov. :
// une vraie barriere serveur seulement si des abus sont constates.
//
// ⚠️ DEUX CAS, UN SEUL INTERRUPTEUR QUI COMPTE.
//  - DANS LE CADRE DE L'APP, la page suit l'app elle-meme : parent.accesComplet() rend
//    toujours vrai tant que ACCES.actif vaut false (et lit l'apercu « Version gratuite » de
//    l'admin). L'app ne peut donc jamais etre payante avec des pages restees ouvertes.
//    (ACCES est un const d'index.html : il n'est pas sur window, accesComplet() si.)
//  - SEULE (lien partage) : ACTIF ci-dessous, faute d'app a interroger. Il passe a true le
//    meme jour que ACCES.actif (node tests/essai.js verifie qu'ils s'accordent).
// Une page SEULE n'est jamais bloquee en local (localhost, 127.0.0.1) : les controles l'ouvrent ainsi.
(function(){
    var ACTIF = false;
    var local = true;
    try{
        var h = location.hostname;
        local = location.protocol !== "https:" || h === "localhost" || h === "127.0.0.1" || h === "[::1]" || /\.localhost$|\.test$/.test(h);
    }catch(e){}

    var parent = null, lisible = false;
    try{ if(window.parent && window.parent !== window){ parent = window.parent; lisible = typeof parent.accesComplet === "function"; } }catch(e){ lisible = false; }
    // Un cadre d'une autre origine ne peut pas etre interroge : on ne bloque pas ce qu'on ne sait pas juger.
    if(parent && !lisible) return;

    var payante = false;
    if(parent){
        try{
            if(parent.accesComplet()) return;
            var autorise = String(parent.cadreAutorise || "");
            var ici = location.pathname;
            if(autorise && (ici === autorise || (autorise.charAt(autorise.length - 1) === "/" && ici.indexOf(autorise) === 0))) return;
            payante = true;
        }catch(e){ return; }
    } else if(!ACTIF || local){
        return;
    }

    var lang = "fr";
    try{ lang = (new URLSearchParams(location.search).get("lang") || navigator.language || "fr").slice(0, 2).toLowerCase(); }catch(e){}
    var T = {
        fr: { titre: "Ouvre Wortando pour continuer", texte: "Cette page fait partie de l'app Wortando.", bouton: "Ouvrir Wortando",
              payant: "Cette page fait partie de l'abonnement.", voir: "Voir l'abonnement" },
        en: { titre: "Open Wortando to continue", texte: "This page is part of the Wortando app.", bouton: "Open Wortando",
              payant: "This page is part of the subscription.", voir: "See the subscription" },
        de: { titre: "Öffne Wortando, um weiterzumachen", texte: "Diese Seite gehört zur App Wortando.", bouton: "Wortando öffnen",
              payant: "Diese Seite gehört zum Abo.", voir: "Zum Abo" },
        es: { titre: "Abre Wortando para continuar", texte: "Esta página forma parte de la app Wortando.", bouton: "Abrir Wortando",
              payant: "Esta página forma parte de la suscripción.", voir: "Ver la suscripción" }
    };
    var x = T[lang] || T.en;

    function poser(){
        if(document.getElementById("accesVoile")) return;
        var v = document.createElement("div");
        v.id = "accesVoile";
        v.setAttribute("role", "dialog");
        v.setAttribute("aria-modal", "true");
        v.style.cssText = "position:fixed; inset:0; z-index:2147483647; display:flex; align-items:center; justify-content:center;"
            + " padding:24px; background:#F7F3EA; color:#1C2430; font-family:system-ui,-apple-system,'Segoe UI',sans-serif; text-align:center;";
        var boite = document.createElement("div");
        boite.style.cssText = "max-width:340px;";
        var marque = document.createElement("div");
        marque.textContent = "Wortando";
        marque.style.cssText = "font-weight:800; font-size:22px; letter-spacing:.5px; margin-bottom:18px;";
        var h1 = document.createElement("h1");
        h1.textContent = payante ? x.payant : x.titre;
        h1.style.cssText = "font-size:20px; line-height:1.3; margin:0 0 20px;";
        boite.appendChild(marque); boite.appendChild(h1);
        if(!payante){
            var p = document.createElement("p");
            p.textContent = x.texte;
            p.style.cssText = "margin:-10px 0 20px; color:#4C566B; font-size:15px;";
            boite.appendChild(p);
        }
        var b = document.createElement(payante ? "button" : "a");
        b.textContent = payante ? x.voir : x.bouton;
        b.style.cssText = "display:inline-block; padding:12px 22px; border-radius:999px; border:0; background:#1C2430; color:#fff;"
            + " font-weight:700; font-size:15px; text-decoration:none; cursor:pointer;";
        if(payante){
            b.type = "button";
            b.addEventListener("click", function(){ try{ parent.ouvrirAbonnement(); }catch(e){} });
        } else {
            b.href = location.origin + "/";
        }
        boite.appendChild(b);
        v.appendChild(boite);
        document.body.appendChild(v);
        try{ document.documentElement.style.overflow = "hidden"; }catch(e){}
    }
    if(document.body) poser(); else document.addEventListener("DOMContentLoaded", poser);
})();
