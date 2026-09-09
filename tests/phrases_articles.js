// Sort les phrases allemandes des exercices d'articles, en EVALUANT le code
// d'index.html au lieu de le relire a coups d'expressions regulieres -- meme
// procede que tests/i18n_dump.js, et pour la meme raison : ce qu'on obtient
// est exactement ce que le navigateur fabrique.
//
//     node tests/phrases_articles.js            une phrase par ligne
//     node tests/phrases_articles.js --json     avec le detail
//
// POURQUOI CE SCRIPT EXISTE. Ces 120 exercices sont FABRIQUES PAR LE CODE :
// ils ne sont pas dans exercices.json, donc audio/manifest.py ne les voyait
// pas, donc aucun mp3 n'a jamais ete genere pour eux -- et l'app retombait sur
// la voix de synthese du telephone. Signale par Jacques le 9 septembre 2026 :
// « c'est pas ta voix Aurora, c'est ta voix du iPhone ».
//
// Le manifeste appelle ce script plutot que de recopier les phrases : une
// donnee recopiee derive, celle-ci est LUE a la source a chaque fois.
const fs = require("fs"), path = require("path"), vm = require("vm");

const src = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");

// UNE SEULE TRANCHE CONTINUE, de la premiere constante du module jusqu'a la
// derniere serie assemblee. Le premier jet decoupait bloc par bloc et se
// trompait des qu'une constante tenait sur une ligne : le decoupage avalait la
// suivante, qui se retrouvait declaree deux fois. Une tranche ne peut pas se
// tromper de frontiere, et si le module bouge, le script s'arrete au lieu de
// sortir une liste incomplete.
const DEBUT = "const ARTICLE_FORMES = {";
const FIN = "const kasusArticleMix = construireExercicesArticlesMix(ARTICLES_MIX);";
const d = src.indexOf(DEBUT);
const f = src.indexOf(FIN);
if (d < 0 || f < 0 || f < d) {
    console.error("Le module des articles n'a pas les bornes attendues.");
    console.error("  debut trouve : " + (d >= 0) + ", fin trouvee : " + (f >= 0));
    process.exit(2);
}
const tranche = src.slice(d, f + FIN.length);

const ctx = {};
vm.createContext(ctx);
vm.runInContext(tranche, ctx);
vm.runInContext(
    "var TOUT = [].concat(kasusArticleNominativ, kasusArticleAkkusativ," +
    " kasusArticleDativ, kasusArticleGenitiv, kasusArticleMix);", ctx);

const tout = ctx.TOUT;
const sansAudio = tout.filter(e => !e.audioDe);
if (sansAudio.length) {
    console.error("ARRET : " + sansAudio.length + " exercice(s) sans audioDe.");
    console.error("   " + JSON.stringify(sansAudio[0].question));
    process.exit(1);
}
const avecParenthese = tout.filter(e => e.audioDe.indexOf("(") >= 0);
if (avecParenthese.length) {
    console.error("ARRET : " + avecParenthese.length + " phrase(s) contiennent encore");
    console.error("une indication entre parentheses : " + avecParenthese[0].audioDe);
    process.exit(1);
}

const phrases = [...new Set(tout.map(e => e.audioDe))].sort();
if (process.argv.includes("--json")) {
    process.stdout.write(JSON.stringify(
        { exercices: tout.length, phrases: phrases }, null, 1));
} else {
    process.stdout.write(phrases.join("\n") + "\n");
}
