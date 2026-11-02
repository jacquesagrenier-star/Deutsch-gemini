# -*- coding: utf-8 -*-
"""La passe visuelle : chaque ecran au telephone (375 x 812), de jour et de
nuit, dans les langues d'interface, mesure plutot que regarde.

    python retours/qualite-es-de/visuel.py --app de --langues fr,ar --themes light,dark --sortie v.json
    python retours/qualite-es-de/visuel.py --app es --captures retours/qualite-es-de/captures

Pour chaque ecran (les memes chemins que tests/francais_ailleurs.py : ecrans
ouverts par leur fonction, puis chaque tuile de « Tout le contenu »), on note :
  page_large   la page defile a l'horizontale (quelque chose depasse l'ecran)
  hors_ecran   un texte sort de l'ecran a gauche ou a droite
  coupe        un texte est rogne par son cadre (overflow cache, points de suspension)
  bouton       le texte d'un bouton deborde du bouton
  vide         l'ecran actif n'a presque pas de texte
  sens         ar / fa : un bloc de texte arabe ecrit de gauche a droite
  contraste    un texte sous le seuil WCAG AA (tests/audit-contraste.js)
Une capture est prise de chaque ecran qui a un signalement (--captures).

Rien ne part chez Firebase : comme le parcours, on ne se connecte pas.
"""
import argparse
import io
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "tests"))
import francais_ailleurs as FA  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

AUDIT = io.open(os.path.join(RACINE, "tests", "audit-contraste.js"), encoding="utf-8").read()

MESURE = r"""
(theme) => {
  const W = window.innerWidth, out = [];
  const actif = document.querySelector('.screen.active');
  const vis = el => { const r = el.getBoundingClientRect(); if(r.width < 1 || r.height < 1) return false;
    const cs = getComputedStyle(el); return cs.visibility !== 'hidden' && cs.display !== 'none' && parseFloat(cs.opacity) > 0.05; };
  // un ancetre qui defile a l'horizontale (ruban des scenes...) : le debordement y est voulu
  const defile = el => { for(let n = el.parentElement; n && n !== document.body; n = n.parentElement){
      const o = getComputedStyle(n).overflowX; if(o === 'auto' || o === 'scroll') return true; } return false; };
  const nom = el => (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '') || el.tagName.toLowerCase();
  const txt = el => (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80);
  if(document.documentElement.scrollWidth > W + 1)
    out.push({code: 'page_large', detail: document.documentElement.scrollWidth + ' px'});
  const portee = [...document.querySelectorAll('.screen.active, .modal.show, .modal-overlay.show, [role=dialog]')].filter(vis);
  const racines = portee.length ? portee : [document.body];
  const vus = new Set();
  for(const R of racines) for(const el of R.querySelectorAll('*')){
    if(!vis(el)) continue;
    const propre = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if(!propre) continue;
    const cs = getComputedStyle(el);
    const rng = document.createRange(); rng.selectNodeContents(el);
    const rr = rng.getBoundingClientRect(), r = el.getBoundingClientRect();
    if(!defile(el) && cs.position !== 'fixed' && (rr.right > W + 2 || rr.left < -2) && rr.width < W * 3){
      const k = 'h' + nom(el) + txt(el); if(!vus.has(k)){ vus.add(k); out.push({code: 'hors_ecran', el: nom(el), texte: txt(el), detail: Math.round(rr.left) + '..' + Math.round(rr.right)}); }
    }
    const cache = /hidden|clip/.test(cs.overflowX + cs.overflow);
    if(cache && el.scrollWidth > el.clientWidth + 2 && !defile(el)){
      const k = 'c' + nom(el) + txt(el); if(!vus.has(k)){ vus.add(k); out.push({code: 'coupe', el: nom(el), texte: txt(el), detail: el.scrollWidth + '>' + el.clientWidth + (cs.textOverflow === 'ellipsis' ? ' (…)' : '')}); }
    }
    if(cache && el.scrollHeight > el.clientHeight + 3 && cs.overflowY !== 'auto' && cs.overflowY !== 'scroll' && el.clientHeight > 0 && /-webkit-box|block|flex/.test(cs.display) && parseInt(cs.webkitLineClamp || 0) > 0){
      const k = 'v' + nom(el) + txt(el); if(!vus.has(k)){ vus.add(k); out.push({code: 'coupe', el: nom(el), texte: txt(el), detail: 'hauteur ' + el.scrollHeight + '>' + el.clientHeight}); }
    }
    const b = el.closest('button, .btn, [role=button]');
    if(b && b !== el && !defile(b)){
      const br = b.getBoundingClientRect();
      if(rr.right > br.right + 3 || rr.left < br.left - 3){
        const k = 'b' + nom(b) + txt(el); if(!vus.has(k)){ vus.add(k); out.push({code: 'bouton', el: nom(b), texte: txt(el), detail: Math.round(rr.left - br.left) + '/' + Math.round(br.right - rr.right)}); }
      }
    }
    if(document.documentElement.lang && /^(ar|fa)/.test(document.documentElement.lang) || document.documentElement.dir === 'rtl'){
      const t = el.textContent; const arabe = (t.match(/[؀-ۿ]/g) || []).length, latin = (t.match(/[A-Za-z]/g) || []).length;
      if(arabe > 8 && arabe > latin && cs.direction === 'ltr' && /block|flex|list-item/.test(cs.display)){
        const k = 's' + nom(el); if(!vus.has(k)){ vus.add(k); out.push({code: 'sens', el: nom(el), texte: txt(el)}); }
      }
    }
  }
  const lettres = actif ? (actif.innerText || '').replace(/\s+/g, '').length : 0;
  if(actif && lettres < 15) out.push({code: 'vide', detail: lettres + ' caracteres'});
  if(theme === 'dark' && window.auditContraste){
    for(const R of racines) for(const c of (window.auditContraste(R) || []).slice(0, 15))
      out.push({code: 'contraste', texte: (c.texte || '').slice(0, 60), detail: c.ratio + ' ' + (c.classe || '')});
  }
  return {ecran: actif ? actif.id : '(aucun)', dir: document.documentElement.dir || '', signalements: out};
}
"""


class Visuel(FA.Session):
    def __init__(self, nav, app, langue, theme, captures):
        self.theme, self.captures, self.mesures = theme, captures, {}
        self.langue = langue
        orig = nav.new_context

        def ctx375(**kw):
            kw["viewport"] = {"width": 375, "height": 812}
            kw["is_mobile"] = True
            kw["has_touch"] = True
            kw["device_scale_factor"] = 2
            kw["color_scheme"] = theme
            return orig(**kw)
        nav.new_context = ctx375
        try:
            super().__init__(nav, app, langue)
        finally:
            nav.new_context = orig
        self.page.evaluate("(t) => { try{ setAppTheme(t); }catch(e){} }", theme)
        self.page.evaluate(AUDIT)
        self.page.wait_for_timeout(300)

    def noter(self, chemin):
        ecran = super().noter(chemin)
        try:
            m = self.page.evaluate(MESURE, self.theme)
        except Exception as e:
            m = {"ecran": ecran, "signalements": [{"code": "erreur", "detail": str(e)[:150]}]}
        m["erreurs_js"] = self.releve[chemin]["erreurs"]
        self.mesures[chemin] = m
        bruit = [s for s in m["signalements"] if s["code"] != "contraste" or self.theme == "dark"]
        if self.captures and bruit:
            nom = re.sub(r"[^\w-]+", "_", "%s-%s-%s-%s" % (self.app, self.langue, self.theme, chemin))[:90]
            f = os.path.join(self.captures, nom + ".png")
            try:
                self.page.screenshot(path=f)
                m["capture"] = os.path.relpath(f, RACINE).replace(os.sep, "/")
            except Exception:
                pass
        return ecran


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", choices=["de", "es"], required=True)
    ap.add_argument("--langues", default="fr")
    ap.add_argument("--themes", default="light")
    ap.add_argument("--sortie")
    ap.add_argument("--captures")
    ap.add_argument("--port", type=int)
    ap.add_argument("--complet", action="store_true")
    a = ap.parse_args()
    if a.port:
        FA.PORT = a.port
    if a.captures:
        os.makedirs(a.captures, exist_ok=True)
    from playwright.sync_api import sync_playwright
    srv = FA.serveur()
    res = {}
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            for lg in a.langues.split(","):
                for th in a.themes.split(","):
                    print("%s %s %s..." % (a.app, lg, th), flush=True)
                    s = Visuel(nav, a.app, lg, th, a.captures)
                    s.visiter(FA.ECRANS, complet=a.complet)
                    res["%s|%s" % (lg, th)] = s.mesures
                    n = sum(len(m["signalements"]) for m in s.mesures.values())
                    print("   %d ecrans, %d signalements" % (len(s.mesures), n), flush=True)
                    s.ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    if a.sortie:
        json.dump(res, io.open(a.sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
