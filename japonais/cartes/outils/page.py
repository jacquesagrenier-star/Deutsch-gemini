"""Écrit a-relire.html : une page autonome (hors ligne) pour que Jacques relise les cartes.

Les réponses sont gardées dans localStorage à chaque clic et à chaque frappe, et un
bouton les exporte en JSON (un autre les réimporte). La page prévient avant de se
fermer si des réponses n'ont pas été exportées.
"""
import json

ORDRE = {"FAUX": 0, "A_REMPLACER": 1, "A_AMELIORER": 2, "BON": 3, None: 4}


def carte(f, phrases):
    fr = f["gloses"]["fr"]
    p = None
    if f["phrases"]:
        ph = phrases[f["phrases"][0]]["texte"]
        p = [ph["ja"]["v"], ph["fr"]["v"], ph["en"]["v"]]
    return {
        "id": f["id"],
        "f": f["furigana"]["v"],
        "fs": f["furigana"]["statut"],
        "kana": f["ecritures"]["kana"]["v"],
        "ro": f["ecritures"]["romaji"]["v"],
        "cl": f["classe"]["v"],
        "fr": fr["affichee"]["v"],
        "src": fr["affichee"]["src"],
        "note": fr["affichee"].get("note"),
        "au": [a["v"] for a in fr["autres"]],
        "en": f["gloses"]["en"]["affichee"]["v"],
        "enj": f["_en_jmdict"],
        "frj": f["_fr_jmdict"],
        "p": p,
        "np": f.get("note_phrases"),
        "vm": f["verdict_machine"],
        "r": f["raison"],
    }


def ecrire(chemin, pour_page):
    donnees = {}
    for niv, (fiches, phrases) in pour_page.items():
        l = [carte(f, phrases) for f in fiches]
        l.sort(key=lambda c: ORDRE.get(c["vm"], 4))
        donnees[niv] = l
    js = json.dumps(donnees, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    with open(chemin, "w", encoding="utf-8") as fh:
        fh.write(GABARIT.replace("/*DONNEES*/null", js))


GABARIT = r"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cartes japonais à relire</title>
<!-- Généré par japonais/cartes/outils/construire.py : ne pas modifier à la main. -->
<style>
:root{--encre:#1C2430;--papier:#FBF8F2;--ambre:#E8A23A;--trait:#d9d2c3;--doux:#5b6470;--carte:#fff;--rouge:#b3261e;--vert:#2e7d32;--bleu:#1f5fa8}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--encre:#ECE7DD;--papier:#171C24;--trait:#3a4250;--doux:#a7afba;--carte:#1f2530;--rouge:#ef8a80;--vert:#81c784;--bleu:#8ab4f8}}
:root[data-theme="dark"]{--encre:#ECE7DD;--papier:#171C24;--trait:#3a4250;--doux:#a7afba;--carte:#1f2530;--rouge:#ef8a80;--vert:#81c784;--bleu:#8ab4f8}
*{box-sizing:border-box}
body{margin:0;padding:16px;background:var(--papier);color:var(--encre);font:16px/1.5 Georgia,"Times New Roman",serif}
main{max-width:860px;margin:0 auto}
h1{font-size:1.45rem;margin:0 0 .25rem}
.intro{color:var(--doux);margin:0 0 1rem}
.barre{position:sticky;top:0;background:var(--papier);padding:8px 0;border-bottom:1px solid var(--trait);z-index:2;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
button,select,input[type=search]{font:inherit;font-size:.9rem;padding:5px 10px;border:1px solid var(--trait);background:var(--carte);color:var(--encre);border-radius:6px;cursor:pointer}
button.on{background:var(--encre);color:var(--papier);border-color:var(--encre)}
.alerte{background:#fdecea;color:#7a1610;border:1px solid #e9a39d;padding:8px 12px;border-radius:6px;margin:8px 0;display:none}
.compte{color:var(--doux);font-size:.9rem;margin-left:auto}
article{background:var(--carte);border:1px solid var(--trait);border-radius:10px;padding:14px 16px;margin:12px 0;display:grid;grid-template-columns:minmax(150px,220px) 1fr;gap:16px}
.recto{text-align:center;align-self:center}
.mot{font-size:2.4rem;line-height:1.9;font-family:"Noto Serif JP","Hiragino Mincho ProN","Yu Mincho",serif}
.mot rt{font-size:.42em;color:var(--doux)}
.ro{color:var(--doux);font-style:italic}
.verso p{margin:.15rem 0}
.fr{font-size:1.25rem;font-weight:bold}
.petit{color:var(--doux);font-size:.85rem}
.ja{font-family:"Noto Serif JP","Hiragino Mincho ProN","Yu Mincho",serif}
.tag{display:inline-block;font-size:.75rem;padding:1px 7px;border-radius:10px;border:1px solid currentColor;margin-right:4px}
.v-FAUX{color:var(--rouge)}.v-A_REMPLACER{color:#c25e00}.v-A_AMELIORER{color:var(--bleu)}.v-BON{color:var(--vert)}
.choix{display:flex;flex-wrap:wrap;gap:6px;margin-top:.5rem}
.choix button.on.FAUX{background:var(--rouge);border-color:var(--rouge)}
.choix button.on.A_REMPLACER{background:#c25e00;border-color:#c25e00}
.choix button.on.A_AMELIORER{background:var(--bleu);border-color:var(--bleu)}
.choix button.on.BON{background:var(--vert);border-color:var(--vert)}
textarea{width:100%;font:inherit;font-size:.95rem;margin-top:6px;border:1px solid var(--trait);border-radius:6px;background:var(--papier);color:var(--encre);padding:6px}
.pages{display:flex;flex-wrap:wrap;gap:4px;margin:12px 0}
@media (max-width:560px){article{grid-template-columns:1fr}.mot{font-size:2rem}}
</style>
</head>
<body>
<main>
<h1>Cartes de vocabulaire japonais à relire</h1>
<p class="intro">Brouillon machine : rien n'est vérifié. Chaque carte porte le verdict de la machine sur ce que JMdict proposait en français (coloré) et sa raison. À vous de dire le vôtre et, si besoin, d'écrire la bonne traduction. Vos réponses sont gardées dans ce navigateur à chaque clic ; <b>exportez-les régulièrement</b> (bouton « Exporter ») : c'est ce fichier qui me revient.</p>
<div class="alerte" id="alerte"></div>
<div class="barre">
  <span id="niveaux"></span>
  <select id="filtre" aria-label="Filtre">
    <option value="prio">FAUX et À REMPLACER d'abord</option>
    <option value="FAUX">FAUX seulement</option>
    <option value="A_REMPLACER">À REMPLACER seulement</option>
    <option value="A_AMELIORER">À AMÉLIORER seulement</option>
    <option value="BON">BON seulement</option>
    <option value="tout">Toutes les cartes</option>
    <option value="nonrelu">Pas encore relues</option>
    <option value="relu">Déjà relues</option>
  </select>
  <input type="search" id="cherche" placeholder="Chercher (japonais, français…)">
  <button id="exporter">Exporter</button>
  <button id="importer">Importer</button>
  <input type="file" id="fichier" accept=".json,application/json" hidden>
  <span class="compte" id="compte"></span>
</div>
<div class="pages" id="pages-haut"></div>
<div id="liste"></div>
<div class="pages" id="pages-bas"></div>
</main>
<script>
const DONNEES = /*DONNEES*/null;
const CLE = "wortando-ja-cartes-relecture-v1";
const PAR_PAGE = 40;
const NOMS = {FAUX:"FAUX", A_REMPLACER:"À REMPLACER", A_AMELIORER:"À AMÉLIORER", BON:"BON"};
let reponses = {}, stockageOk = true, nonExporte = 0;
let niveau = Object.keys(DONNEES)[0], page = 0;

function alerte(t){const a=document.getElementById("alerte");a.textContent=t;a.style.display=t?"block":"none";}
try{
  const brut = localStorage.getItem(CLE);
  if (brut) reponses = JSON.parse(brut) || {};
  localStorage.setItem(CLE + "-test", "1"); localStorage.removeItem(CLE + "-test");
}catch(e){
  stockageOk = false;
  alerte("Ce navigateur ne garde pas les réponses (navigation privée ou stockage bloqué). Exportez avant de fermer la page, sinon elles seront perdues.");
}
try{ nonExporte = Number(localStorage.getItem(CLE + "-nonexporte") || 0); }catch(e){}

function sauver(){
  nonExporte++;
  if (!stockageOk) return;
  try{
    localStorage.setItem(CLE, JSON.stringify(reponses));
    localStorage.setItem(CLE + "-nonexporte", String(nonExporte));
  }catch(e){
    stockageOk = false;
    alerte("L'enregistrement a échoué (" + e.name + "). Exportez maintenant pour ne rien perdre.");
  }
}
window.addEventListener("beforeunload", e => { if (nonExporte > 0) { e.preventDefault(); e.returnValue = ""; } });

function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}
function ruby(b){return b.map(([t,l])=>l?`<ruby>${esc(t)}<rt>${esc(l)}</rt></ruby>`:esc(t)).join("");}

function visibles(){
  const f = document.getElementById("filtre").value;
  const q = document.getElementById("cherche").value.trim().toLowerCase();
  return DONNEES[niveau].filter(c=>{
    if (f==="prio" && !(c.vm==="FAUX"||c.vm==="A_REMPLACER")) return false;
    if (NOMS[f] && c.vm!==f) return false;
    if (f==="nonrelu" && reponses[c.id] && reponses[c.id].v) return false;
    if (f==="relu" && !(reponses[c.id] && reponses[c.id].v)) return false;
    if (q){
      const t = (c.f.map(b=>b[0]).join("")+" "+c.kana+" "+c.ro+" "+c.fr+" "+c.au.join(" ")+" "+c.en+" "+c.id).toLowerCase();
      if (!t.includes(q)) return false;
    }
    return true;
  });
}

function rendre(){
  const l = visibles();
  const nPages = Math.max(1, Math.ceil(l.length / PAR_PAGE));
  if (page >= nPages) page = nPages - 1;
  const morceau = l.slice(page*PAR_PAGE, (page+1)*PAR_PAGE);
  document.getElementById("liste").innerHTML = morceau.map(c=>{
    const r = reponses[c.id] || {};
    const btn = Object.keys(NOMS).map(v=>`<button class="${v}${r.v===v?" on":""}" data-id="${c.id}" data-v="${v}">${NOMS[v]}</button>`).join("");
    const phrase = c.p ? `<p class="ja" lang="ja">${esc(c.p[0])}</p><p>${esc(c.p[1])}</p><p class="petit">${esc(c.p[2])}</p>`
                       : `<p class="petit">Pas de phrase retenue${c.np?" : "+esc(c.np):""}.</p>`;
    const vm = c.vm ? `<span class="tag v-${c.vm}">machine : ${NOMS[c.vm]}</span>` : `<span class="tag">pas encore jugé</span>`;
    return `<article id="${c.id}">
  <div class="recto"><div class="mot" lang="ja">${ruby(c.f)}</div><div class="ro">${esc(c.ro)}</div>
    ${c.fs!=="brouillon"?'<div class="petit">furigana à vérifier</div>':""}</div>
  <div class="verso">
    <p class="fr">${esc(c.fr||"—")}</p>
    ${c.au.length?`<p>Aussi : ${esc(c.au.join(" ; "))}</p>`:""}
    ${c.note?`<p class="petit">Note : ${esc(c.note)}</p>`:""}
    ${phrase}
    <p class="petit">Anglais JMdict : ${esc(c.enj.join(" | "))}</p>
    <p class="petit">Français JMdict (en vrac) : ${esc(c.frj.join(" ; ")||"aucun")}</p>
    <p class="petit">${vm} ${esc(c.r||"")} · ${c.src==="wortando"?"traduction écrite par la machine":"traduction tirée de JMdict"} · ${esc(c.cl||"")} · ${esc(c.id)}</p>
    <div class="choix">${btn}</div>
    <textarea data-id="${c.id}" rows="1" placeholder="Correction ou remarque (facultatif)">${esc(r.c||"")}</textarea>
  </div></article>`;
  }).join("") || "<p>Aucune carte pour ce filtre.</p>";
  const pg = Array.from({length:nPages},(_,i)=>`<button class="${i===page?"on":""}" data-page="${i}">${i+1}</button>`).join("");
  document.getElementById("pages-haut").innerHTML = nPages>1?pg:"";
  document.getElementById("pages-bas").innerHTML = nPages>1?pg:"";
  compter(l.length);
}

function compter(n){
  const tous = DONNEES[niveau], relus = tous.filter(c=>reponses[c.id]&&reponses[c.id].v).length;
  document.getElementById("compte").textContent = `${n} carte(s) affichée(s) · ${relus}/${tous.length} relues en ${niveau}` + (nonExporte?` · ${nonExporte} changement(s) non exporté(s)`:"");
}

function niveaux(){
  document.getElementById("niveaux").innerHTML = Object.keys(DONNEES).map(n=>`<button class="${n===niveau?"on":""}" data-niveau="${n}">${n} (${DONNEES[n].length})</button>`).join(" ");
}

document.addEventListener("click", e=>{
  const b = e.target.closest("button"); if (!b) return;
  if (b.dataset.niveau){ niveau=b.dataset.niveau; page=0; niveaux(); rendre(); return; }
  if (b.dataset.page){ page=Number(b.dataset.page); rendre(); window.scrollTo(0,0); return; }
  if (b.dataset.id){
    const r = reponses[b.dataset.id] || (reponses[b.dataset.id] = {});
    r.v = r.v===b.dataset.v ? null : b.dataset.v; r.t = new Date().toISOString();
    sauver();
    b.parentNode.querySelectorAll("button").forEach(x=>x.classList.toggle("on", x.dataset.v===r.v));
    compter(visibles().length);
  }
});
document.addEventListener("input", e=>{
  const t = e.target;
  if (t.tagName==="TEXTAREA" && t.dataset.id){
    const r = reponses[t.dataset.id] || (reponses[t.dataset.id] = {});
    r.c = t.value; r.t = new Date().toISOString(); sauver(); compter(visibles().length);
  }
});
document.getElementById("filtre").addEventListener("change", ()=>{page=0;rendre();});
document.getElementById("cherche").addEventListener("input", ()=>{page=0;rendre();});
document.getElementById("exporter").addEventListener("click", ()=>{
  const sortie = {page:"japonais/cartes/a-relire.html", exporte_le:new Date().toISOString(), reponses:{}};
  for (const [id,r] of Object.entries(reponses)) if (r.v || (r.c && r.c.trim())) sortie.reponses[id] = r;
  const blob = new Blob([JSON.stringify(sortie,null,1)], {type:"application/json"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "relecture-cartes-japonais-" + new Date().toISOString().slice(0,10) + ".json";
  document.body.appendChild(a); a.click(); a.remove();
  nonExporte = 0; try{ localStorage.setItem(CLE + "-nonexporte", "0"); }catch(e){}
  compter(visibles().length);
});
document.getElementById("importer").addEventListener("click", ()=>document.getElementById("fichier").click());
document.getElementById("fichier").addEventListener("change", e=>{
  const f = e.target.files[0]; if (!f) return;
  f.text().then(t=>{
    const d = JSON.parse(t), recu = d.reponses || {};
    let n = 0;
    for (const [id,r] of Object.entries(recu)){
      const ici = reponses[id];
      if (!ici || !ici.t || (r.t && r.t > ici.t)){ reponses[id] = r; n++; }
    }
    sauver(); rendre(); alerte(n + " réponse(s) importée(s) (les plus récentes gardées).");
  }).catch(err=>alerte("Import impossible : " + err.message));
});
niveaux(); rendre(); compter(visibles().length);
</script>
</body>
</html>
"""
