# -*- coding: utf-8 -*-
"""Fabrique la feuille de production d'une scene : les 19 plans, deux prompts
chacun, prets a coller dans Artlist.

    python scenes/production.py --scene 01-ankunft-berlin

POURQUOI UN SCRIPT ET PAS UN DOCUMENT ECRIT A LA MAIN
    Les repliques allemandes viennent de scenes/<scene>.json. Si une phrase
    change -- et elles changeront, c'est un cours de langue -- la feuille se
    refait en une commande au lieu d'etre recopiee, avec le risque de recopier
    de travers. Le texte allemand ne doit exister qu'a un seul endroit.

CE QUE LE SCRIPT APPORTE, LUI
    La mise en scene : le cadrage de chaque plan et l'action de chaque
    replique. C'est du travail d'auteur, il vit ici, dans MISE_EN_SCENE.

LES DEUX PROMPTS, ET POURQUOI ILS SONT SEPARES
    Framing  -- l'image fixe. Elle porte le cadrage, le decor, la lumiere, la
                place du personnage. C'est elle qui tient l'identite.
    Directing -- l'animation. Elle ne decrit QUE le mouvement.

    Redecrire la composition dans le prompt d'animation lui laisse moins de
    place pour l'action, et le modele finit par n'avoir rien a animer. Verifie
    le 8 septembre 2026 : le prompt d'image utilise pour la video a produit un
    plan sans geste, ou le modele a invente un zoom faute d'instruction.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Ce qui ne change pas d'un plan a l'autre.
# --------------------------------------------------------------------------
ANNA_POSE = ("She is placed LEFT of centre and looks toward the RIGHT of frame "
             "and slightly upward, with open space in front of her gaze. She "
             "stands at an OPEN information desk in an airport arrivals hall - "
             "no glass partition, no booth, no screen. The pale desk crosses "
             "the lower third of the frame, close to the camera, with a dark "
             "tablet and a few leaflets on it. One of her hands rests on the "
             "desk beside them.")

MARK_POSE = ("He is placed RIGHT of centre and looks toward the LEFT of frame "
             "and slightly downward, with open space in front of his gaze. He "
             "stands in front of an information desk in an airport arrivals "
             "hall, the pale edge of the desk crossing the lower left corner. "
             "He wears a dark technical shell jacket over a plain dark t-shirt, "
             "slightly rumpled from travelling. The handle of a suitcase is "
             "visible at the very bottom of the frame.")

FOND = ("Soft, even light on the face. Behind, the open depth of the hall - "
        "warm interior lighting, distant travellers - thrown STRONGLY out of "
        "focus, heavy bokeh. No bright window behind the head, no vertical "
        "pillar close to the head.")

EPAULE = ("In the lower {coin} corner, only a soft dark blurred shape suggests "
          "the other person's shoulder. No second face.")

FIN_IMAGE = "Natural skin texture, realistic lighting, photorealistic, no stylization."

FIXE = "Locked-off camera. No zoom, no push-in, no camera movement of any kind."
ZOOM = "A very slow, subtle push-in throughout the shot, ending on the face."

# --------------------------------------------------------------------------
# LES TROIS TAILLES DE PLAN, ET POURQUOI ELLES CHANGENT EN COURS DE SCENE.
#
# Douze repliques au meme cadrage donnent un diaporama de tetes parlantes. Le
# cinema fait varier la taille des plans -- c'est ce qui evite la monotonie
# d'un dialogue, bien plus que des mouvements de camera ajoutes au hasard.
#
# Ici la progression raconte quelque chose : ils commencent a distance,
# etrangers et vouvoyes, et finissent proches. LE CADRAGE SUIT LA RELATION.
#
#   plans 5-6    moyen        deux inconnus, la distance polie
#   plans 8-11   moyen serre  la conversation s'installe
#   plans 12-13  serre        le coeur pratique de la scene
#   plans 15-16  moyen serre  on respire, echange bref
#   plans 17-18  serre        l'adieu, le moment le plus chaleureux
# --------------------------------------------------------------------------
TAILLES = {
    "moyen": ("Medium shot, from the waist up, the figure occupying about half "
              "the frame height."),
    "moyen serre": ("Medium close shot, chest up, the face filling the upper "
                    "third of the frame."),
    "serre": ("Close shot, head and shoulders, the face filling the upper half "
              "of the frame."),
}

# --------------------------------------------------------------------------
# LA MISE EN SCENE, plan par plan. C'est le coeur du fichier.
#   cadre  -- ce qui s'ajoute a la pose type, pour l'image fixe
#   action -- le prompt d'animation. QUE du mouvement.
#   zoom   -- True seulement la ou le moment le merite (voir _lisez_moi)
# --------------------------------------------------------------------------
MISE_EN_SCENE = {
    1: dict(cadre="Vertical 9:16. Seen from inside the terminal, through a tall "
                  "glass wall: an aircraft on the apron at dusk, ground vehicles "
                  "around it, warm low sun. No people in the foreground. The "
                  "glass reflects the interior faintly.",
            action="Almost still. The faintest drift of the camera. Ground "
                   "vehicles move slowly in the distance, light shifts on the "
                   "glass. Nothing dramatic."),

    2: dict(cadre="Vertical 9:16. Wide shot of a busy airport arrivals hall, "
                  "warm evening light. Small in the frame and seen FROM BEHIND, "
                  "a young man in a dark technical shell jacket walks in pulling "
                  "two suitcases. His face is not visible. Travellers pass in "
                  "soft focus.",
            action="He walks slowly away from the camera into the hall, pulling "
                   "the two suitcases. Travellers cross the frame around him. "
                   "The camera stays still."),

    3: dict(cadre="Vertical 9:16. A baggage carousel turning, suitcases going "
                  "round, seen close and slightly from above. Warm terminal "
                  "light, the hall behind thrown out of focus. No faces.",
            action="The carousel turns steadily, suitcases sliding past the "
                   "camera. A hand reaches in at the edge of frame and lifts one "
                   "away. The camera stays still."),

    4: dict(cadre="Vertical 9:16. A young man in a dark technical shell jacket, "
                  "seen from BEHIND and slightly to the side, standing still in "
                  "the hall and looking up at the overhead signs. His face is "
                  "not visible. Two suitcases beside him. Signs and travellers "
                  "softly out of focus.",
            action="He turns his head slowly, scanning the overhead signs, then "
                   "settles on one direction. His shoulders shift as he decides. "
                   "The camera stays still."),

    5: dict(pose="mark", coin="left", taille="moyen",
            action="He leans in very slightly and asks his question, polite and "
                   "a little tired from the flight. His eyebrows lift on the "
                   "question and stay up as he waits. One small open-hand "
                   "gesture of enquiry, close to his body."),

    6: dict(pose="anna", coin="right", taille="moyen",
            action="She answers immediately, without hesitating. A small open "
                   "hand indicates a direction just past him, low and close to "
                   "her body, then returns to the desk. Her head tilts slightly "
                   "as she asks her own question in return."),

    7: dict(cadre="Vertical 9:16. Close on a baggage carousel, the number FOUR "
                  "on a sign above it out of focus in the upper frame. Suitcases "
                  "turn past the camera. Warm terminal light. No faces.",
            action="The suitcases turn steadily past the camera, one after "
                   "another. The camera stays still."),

    8: dict(pose="mark", coin="left", taille="moyen serre",
            action="He answers simply, a small settling of the shoulders. On the "
                   "second half a quiet pride comes into his face, and the "
                   "beginning of a smile. He holds her eye throughout."),

    9: dict(pose="anna", coin="right", taille="moyen serre",
            action="Her face opens with genuine warmth and she gives a small "
                   "welcoming nod. Then curiosity: her eyebrows lift and her "
                   "head tilts a little as she asks."),

    10: dict(pose="mark", coin="left", taille="moyen serre",
             action="He nods once and answers, the smile widening. A small lift "
                    "of the chin - confidence with a trace of nervousness under "
                    "it. He holds her eye."),

    11: dict(pose="anna", coin="right", taille="moyen serre",
             action="She becomes practical. A small precise gesture of one hand, "
                    "kept close to her body, as she names the office. Her "
                    "eyebrows lift at the end to check he has followed."),

    12: dict(pose="mark", coin="left", taille="serre",
             action="He glances briefly away, orienting himself in the hall, "
                    "then back to her as he asks. A slight forward lean on the "
                    "question."),

    13: dict(pose="anna", coin="right", taille="serre", zoom=True,
             action="EARLY in the shot, while the framing is still wide, she "
                    "lifts one hand and indicates DOWN and to her LEFT - away "
                    "from him, into the depth of the hall behind her - a small "
                    "precise gesture, not a broad sweep. Her eyes follow her "
                    "hand briefly, then return to him and stay there as the "
                    "camera closes in. A small nod at the end."),

    14: dict(cadre="Vertical 9:16. A ticket machine standing in a lower "
                   "concourse of an airport, screen lit, seen straight on from a "
                   "few steps away. The hall around it warm and softly out of "
                   "focus, a few travellers passing.",
             action="A traveller crosses the frame in front of the machine and "
                    "walks on. The lit screen flickers gently. The camera stays "
                    "still."),

    15: dict(pose="mark", coin="left", taille="moyen serre",
             action="A short simple question. His head tilts slightly, eyebrows "
                    "raised, waiting. Nothing else moves."),

    16: dict(pose="anna", coin="right", taille="moyen serre",
             action="She answers precisely, factually. A tiny nod on the number. "
                    "Her hand stays on the desk."),

    17: dict(pose="mark", coin="left", taille="serre",
             action="Warm and genuine. A small nod of thanks, his shoulders "
                    "loosening now that he knows where to go. A real smile at "
                    "the end."),

    18: dict(pose="anna", coin="right", taille="serre", zoom=True,
             action="The warmest moment of the scene. She answers easily, and as "
                    "the camera closes in a real smile reaches her eyes. A small "
                    "nod of farewell at the end. She keeps looking at him after "
                    "she has finished speaking."),

    19: dict(cadre="Vertical 9:16. The terminal exit at night, seen from inside: "
                   "dark glass doors, city lights and headlights beyond, wet "
                   "tarmac reflecting them. A figure in silhouette walks out, "
                   "small in the frame, face not visible.",
             action="The figure walks out through the doors and away into the "
                    "night. Headlights pass beyond the glass. The camera stays "
                    "still."),
}


def image_prompt(p, m):
    """Le prompt de Framing. Pour un plan de decor, le cadre est ecrit en
    entier ; pour une replique, on assemble la pose type et le fond."""
    if "cadre" in m:
        return m["cadre"] + "\n\n" + FIN_IMAGE
    qui = "@Anna" if m["pose"] == "anna" else "@Mark"
    tete = "Vertical 9:16. %s of %s." % (TAILLES[m["taille"]].rstrip("."), qui)
    pose = ANNA_POSE if m["pose"] == "anna" else MARK_POSE
    return "\n\n".join([tete, pose, FOND, EPAULE.format(coin=m["coin"]), FIN_IMAGE])


def video_prompt(m):
    """Le prompt de Directing. Le mouvement de camera d'abord, l'action ensuite."""
    return (ZOOM if m.get("zoom") else FIXE) + "\n\n" + m["action"]


def html(d, scene):
    e = lambda s: (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    o = []
    o.append("""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Production &mdash; %s</title><style>
:root{color-scheme:light}
body{margin:0;background:#F2EEE2;color:#1C2430;
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:56rem;margin:0 auto;padding:2rem 1.25rem 5rem}
h1{font-size:1.6rem;margin:0 0 .25rem}
.sous{color:#6b6558;margin:0 0 2rem}
.regles{background:#fff;border:1px solid #e2dcc9;border-radius:10px;
 padding:1rem 1.25rem;margin-bottom:2.5rem}
.regles h2{font-size:1rem;margin:0 0 .6rem;text-transform:uppercase;
 letter-spacing:.05em;color:#6b6558}
.regles ul{margin:0;padding-left:1.1rem}.regles li{margin:.25rem 0}
article{background:#fff;border:1px solid #e2dcc9;border-radius:10px;
 padding:1.1rem 1.25rem;margin-bottom:1.5rem}
article.fait{border-color:#7a9a5b;background:#f6faf2}
h2.plan{font-size:1.15rem;margin:0 0 .1rem}
.meta{color:#6b6558;font-size:.85rem;margin:0 0 .8rem}
.de{font-size:1.05rem;margin:.2rem 0}
.fr{color:#6b6558;margin:0 0 1rem}
h3{font-size:.75rem;text-transform:uppercase;letter-spacing:.07em;
 color:#6b6558;margin:1.1rem 0 .35rem}
pre{background:#1C2430;color:#e8e4d8;border-radius:8px;padding:.85rem 1rem;
 overflow-x:auto;white-space:pre-wrap;font:13px/1.5 ui-monospace,Menlo,Consolas,monospace;margin:0}
.reglage{font:13px ui-monospace,Menlo,Consolas,monospace;color:#6b6558;margin:.4rem 0 0}
.badge{display:inline-block;background:#E8A23A;color:#1C2430;border-radius:4px;
 padding:.05rem .4rem;font-size:.72rem;font-weight:600;vertical-align:.1em}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) body{background:#15181d;color:#e8e4d8}
:root:not([data-theme="light"]) article,:root:not([data-theme="light"]) .regles{background:#1e232a;border-color:#2e353f}
:root:not([data-theme="light"]) .fr,:root:not([data-theme="light"]) .meta,
:root:not([data-theme="light"]) .sous,:root:not([data-theme="light"]) h3,
:root:not([data-theme="light"]) .reglage,:root:not([data-theme="light"]) .regles h2{color:#9aa3ae}
:root:not([data-theme="light"]) article.fait{background:#1b2620;border-color:#4a6b3a}}
</style></head><body><main>""" % e(scene))

    o.append("<h1>Feuille de production &mdash; %s</h1>" % e(scene))
    o.append('<p class="sous">%d plans &middot; %d s de video &middot; '
             'genere par <code>scenes/production.py</code></p>'
             % (len(d["plans"]), sum(p["duree"] for p in d["plans"])))

    o.append("""<div class="regles"><h2>La marche a suivre</h2><ul>
<li><b>Deux etapes par plan.</b> D'abord <b>Framing</b> (l'image fixe), puis
<b>Directing</b> (l'animation), avec l'image en <b>Start Frame</b>.</li>
<li><b>Images :</b> 9:16 &middot; 1K &middot; 4 images &mdash; 130 credits les quatre.
Le 2K est inutile : la video plafonne a 720p.</li>
<li><b>Video :</b> Seedance 2.0 Mini &middot; 9:16 &middot; 720p &middot; audio
<b>coupe</b> &middot; duree du plan.</li>
<li><b>N'attachez que les visages qui doivent etre reconnaissables.</b>
<code>@Anna</code>, <code>@Mark</code>. Une personne vue de dos ne s'attache pas :
l'attacher inviterait le modele a lui montrer le visage.</li>
<li><b>En Directing, aucun personnage attache.</b> Ils sont deja dans l'image.</li>
<li><b>Regard :</b> Mark vers la GAUCHE, Anna vers la DROITE. C'est ce qui donne
l'impression qu'ils se regardent.</li>
<li><b>Un seul visage ancre par plan.</b> L'autre n'est qu'une epaule floue.</li>
<li><b>Telechargez chaque prise gardee tout de suite</b> &mdash; Artlist peut
effacer sans preavis (voir <code>video/PROVENANCE.txt</code>).</li>
<li>Puis <code>python video/rapatrier.py --plan N</code> : son coupe, prise classee.</li>
</ul></div>""")

    for p in d["plans"]:
        m = MISE_EN_SCENE.get(p["n"])
        if not m:
            continue
        fait = ' class="fait"' if p["n"] == 13 else ""
        o.append("<article%s>" % fait)
        badge = ' <span class="badge">FAIT</span>' if p["n"] == 13 else ""
        o.append('<h2 class="plan">Plan %02d &mdash; %s%s</h2>' % (p["n"], e(p["locuteur"]), badge))
        o.append('<p class="meta">%s &middot; %s s &middot; audio %s s%s</p>'
                 % (e(p["type"]), p["duree"], p.get("duree_audio", "?"),
                    (" &middot; " + m["taille"] if "taille" in m else "")
                    + (" &middot; rapprochement" if m.get("zoom") else "")))
        if p.get("de"):
            o.append('<p class="de">%s</p><p class="fr">%s</p>' % (e(p["de"]), e(p.get("fr", ""))))
        o.append("<h3>1. Framing &mdash; l'image de depart</h3>")
        o.append("<pre>%s</pre>" % e(image_prompt(p, m)))
        o.append("<h3>2. Directing &mdash; l'animation</h3>")
        o.append("<pre>%s</pre>" % e(video_prompt(m)))
        o.append('<p class="reglage">Seedance 2.0 Mini &middot; 9:16 &middot; 720p &middot; %s sec &middot; audio coupe</p>'
                 % p["duree"])
        o.append("</article>")

    o.append("</main></body></html>")
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    a = ap.parse_args()
    src = os.path.join(RACINE, "scenes", a.scene + ".json")
    if not os.path.exists(src):
        sys.exit("  Introuvable : %s" % src)
    d = json.load(io.open(src, encoding="utf-8"))
    manquants = [p["n"] for p in d["plans"] if p["n"] not in MISE_EN_SCENE]
    if manquants:
        print("  ATTENTION, plans sans mise en scene : %s" % manquants)
    out = os.path.join(RACINE, "scenes", "production-%s.html" % a.scene.split("-")[0])
    io.open(out, "w", encoding="utf-8", newline="").write(html(d, a.scene))
    print("  %d plans  ->  scenes/%s" % (len(d["plans"]), os.path.basename(out)))


if __name__ == "__main__":
    main()
