// Exerce le VRAI code de la v519, extrait d'index.html -- pas une copie.
// Les deux morceaux (le magasin et la fusion du nuage) sont evalues ENSEMBLE,
// comme dans index.html ou ils vivent dans le meme <script> : les evaluer
// separement leur donnerait deux portees, ce que le fichier livre n'a pas.
const fs = require("fs");
const src = fs.readFileSync("index.html", "utf8");

function bloc(debut, fin) {
  const i = src.indexOf(debut);
  if (i < 0) throw new Error("introuvable : " + debut);
  const j = src.indexOf(fin, i);
  if (j < 0) throw new Error("fin introuvable apres : " + debut);
  return src.slice(i, j);
}

const magasin = {};
globalThis.localStorage = {
  getItem: k => (k in magasin ? magasin[k] : null),
  setItem: (k, v) => { magasin[k] = String(v); },
  removeItem: k => { delete magasin[k]; }
};
globalThis.scheduleCloudSync = () => {};
var exerciseJeuNom = null;

const MAGASIN = bloc('const GRAMMAIRE_KEY = "deutschAI_grammaire_v1";',
                     "function showResults()");
const FUSION = bloc("            const distant = JSON.parse(data.grammaire",
                    "        }catch(e){}");

eval(MAGASIN + "\nglobalThis.noterSerieGrammaire = noterSerieGrammaire;"
   + "\nglobalThis.lireGrammaire = lireGrammaire;"
   + "\nglobalThis.etatJeu = etatJeu;"
   // `catch(e){}` VIDE, exactement comme index.html : une enveloppe qui
   // relance l'exception testerait mon banc d'essai, pas le code livre.
   + "\nglobalThis.fusionnerDuNuage = function(data){ try{\n" + FUSION + "\n}catch(e){} };");

function ligne(n, v) { console.log("  " + (v ? "OK   " : "ECHEC") + "  " + n); return v; }
let ko = 0;
const ok = (n, v) => { if (!ligne(n, v)) ko++; };

console.log("\nUNE SERIE PARFAITE");
exerciseJeuNom = "perfektExercises";
noterSerieGrammaire(100, 10, 10);
let e = etatJeu("perfektExercises");
ok("1 serie comptee", e.series === 1);
ok("sansFaute a 1", e.sansFaute === 1);
ok("meilleur a 100", e.meilleur === 100);
ok("totaux 10/10", e.questions === 10 && e.justes === 10);

console.log("\nUNE SERIE MOINS BONNE : le meilleur ne redescend pas");
noterSerieGrammaire(70, 7, 10);
e = etatJeu("perfektExercises");
ok("2 series", e.series === 2);
ok("sansFaute reste a 1", e.sansFaute === 1);
ok("meilleur reste 100", e.meilleur === 100);
ok("dernierPct suit la derniere, pas la meilleure", e.dernierPct === 70);
ok("totaux cumules 17/20", e.questions === 20 && e.justes === 17);

console.log("\nCE QUI NE DOIT RIEN ECRIRE");
const avant = JSON.stringify(lireGrammaire());
exerciseJeuNom = null;
noterSerieGrammaire(100, 5, 5);
ok("serie construite a la volee (nom null) : ignoree",
   JSON.stringify(lireGrammaire()) === avant);
exerciseJeuNom = "perfektExercises";
noterSerieGrammaire(0, 0, 0);
ok("serie vide (total 0) : ignoree, pas de division par zero",
   JSON.stringify(lireGrammaire()) === avant);

console.log("\nUN JEU JAMAIS JOUE");
ok("etatJeu renvoie null", etatJeu("konjunktiv2Exercises") === null);

console.log("\nSTOCKAGE ILLISIBLE (navigateur prive, quota, JSON casse)");
magasin["deutschAI_grammaire_v1"] = "{ceci n'est pas du JSON";
ok("lireGrammaire ne jette pas et rend un objet vide",
   JSON.stringify(lireGrammaire()) === "{}");

console.log("\nFUSION AU RETOUR DU NUAGE");
magasin["deutschAI_grammaire_v1"] = JSON.stringify({
  perfektExercises: { series: 2, dernier: 1000, meilleur: 100, questions: 20,
                      justes: 17, sansFaute: 1, dernierPct: 70 }
});
fusionnerDuNuage({ grammaire: JSON.stringify({
  perfektExercises: { series: 5, dernier: 9000, meilleur: 90, questions: 50,
                      justes: 45, sansFaute: 3, dernierPct: 90 },
  relativOrderExercises: { series: 1, dernier: 500, meilleur: 60, questions: 10,
                           justes: 6, sansFaute: 0, dernierPct: 60 }
}) });
e = etatJeu("perfektExercises");
ok("series : le maximum des deux", e.series === 5);
ok("sansFaute : le maximum des deux", e.sansFaute === 3);
ok("meilleur : le maximum, meme si le distant est plus bas", e.meilleur === 100);
ok("dernierPct : celui de la serie la PLUS RECENTE (distant)", e.dernierPct === 90);
ok("un jeu absent en local arrive du nuage",
   etatJeu("relativOrderExercises").series === 1);

console.log("\nFUSION INVERSE : le local est plus recent");
magasin["deutschAI_grammaire_v1"] = JSON.stringify({
  perfektExercises: { series: 9, dernier: 99000, meilleur: 100, questions: 90,
                      justes: 80, sansFaute: 4, dernierPct: 55 }
});
fusionnerDuNuage({ grammaire: JSON.stringify({
  perfektExercises: { series: 5, dernier: 9000, meilleur: 90, questions: 50,
                      justes: 45, sansFaute: 3, dernierPct: 90 }
}) });
ok("dernierPct garde le local, plus recent que le distant",
   etatJeu("perfektExercises").dernierPct === 55);
ok("aucune serie perdue", etatJeu("perfektExercises").series === 9);

console.log("\nNUAGE VIDE OU ABSENT");
const intact = JSON.stringify(lireGrammaire());
fusionnerDuNuage({});
ok("aucun champ grammaire : rien n'est touche",
   JSON.stringify(lireGrammaire()) === intact);
fusionnerDuNuage({ grammaire: "pas du JSON" });
ok("champ illisible : rien n'est touche, aucune exception",
   JSON.stringify(lireGrammaire()) === intact);

console.log(ko ? "\n" + ko + " ECHEC(S)\n" : "\nTout passe.\n");
process.exit(ko ? 1 : 0);
