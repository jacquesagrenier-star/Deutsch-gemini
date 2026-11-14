// Le calcul du certificat de l'examen blanc telc Deutsch B1·B2 Pflege (certificatSoins dans index.html),
// contre le tableau officiel du test modele (pflege/FORMAT-TELC-PFLEGE.md, « Les seuils »).
// Usage : node tests/pflege_certificat.js [index.html]
const fs=require('fs'); const src=fs.readFileSync(process.argv[2]||require('path').join(__dirname,'..','index.html'),'utf8');
const a=src.indexOf('function niveauPartielSoins'); const b=src.indexOf('function lireExamensSoins');
eval(src.slice(a,b));
const cas=[[59,20,100,'B2'],[43,7,75,'B2'],[42,15,75,'B2'],[42,14,75,'B1'],[43,3,75,'aucun'],[43,4,75,'B1'],[18,15,80,'aucun'],[19,7,80,'B1'],[50,18,74.5,'B1'],[50,18,34.5,'aucun'],[26,6,90,'aucun'],[27,0,40,'aucun'],[27,4,40,'B1']];
let ok=0; for(const [h,s,o,att] of cas){const r=certificatSoins({hls:h,schreiben:s,sprechen:o}); if(r===att) ok++; else console.log('ECART',h,s,o,'attendu',att,'obtenu',r);} console.log(ok+'/'+cas.length+' cas justes'); if(ok!==cas.length) process.exit(1);
