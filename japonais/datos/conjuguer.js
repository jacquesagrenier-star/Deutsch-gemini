// Pont entre construire.py et le moteur de conjugaison : lit sur l'entrée
// standard une liste [{kanji, kana, classe}], écrit sur la sortie la liste des
// formes (null quand la classe n'est pas gérée). Rien n'est stocké à la main.
const C = require("../conjugaison/conjugaison.js");
let entree = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (d) => { entree += d; });
process.stdin.on("end", () => {
    const sortie = JSON.parse(entree).map(({ kanji, kana, classe }) => {
        const r = C.conjuguer(kanji, kana, classe);
        return r ? { formes: r.formes, erreur: null } : { formes: null, erreur: C.erreur(kanji, kana, classe) };
    });
    process.stdout.write(JSON.stringify(sortie));
});
