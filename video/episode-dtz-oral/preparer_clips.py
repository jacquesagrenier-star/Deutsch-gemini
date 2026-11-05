# -*- coding: utf-8 -*-
"""Les paniers des 23 clips de l'oral du DTZ, pour video/omnihuman.py --scene dtz-oral --modele kling. GRATUIT.

    python video/episode-dtz-oral/preparer_clips.py

Pour chaque replique « video » de scenes/dtz-oral.json :
  _a-televerser/planNN-<image>.jpg   l'image maitresse (anna-dtz recadree, ou mark-dtz), allegee en JPEG
  _a-televerser/planNN-pleine.mp3    la voix de audio/scenes/dtz-oral/, avec 0,25 s d'amorce et 1,3 s de queue :
                                     la queue est la marge dont la bouche a besoin pour se refermer (omnihuman.py)
  _essai-avatar/prompts/planNN.txt   le prompt, qui fait foi

LES PROMPTS SUIVENT verifier_prompt.py (relu avec --lecons et --avant-episode le 3 nov. 2026) :
  - un vrai verbe de parole, la camera verrouillee, le cadre tenu jusqu'a la derniere image ;
  - l'interlocuteur n'est JAMAIS nomme (interlocuteur-fantome) : ils parlent a l'objectif, c'est-a-dire a l'eleve ;
  - la poitrine decrite du debut a la fin (texte-incruste : Kling pose de faux sous-titres sur une poitrine vide) ;
  - les mains dites, et ce qu'elles tiennent : rien (objet-qui-se-materialise -- « Foto » est dans une replique) ;
  - UN GESTE PAR REPLIQUE, ecrit pour ce qu'elle dit, avec son amplitude, TENU jusqu'a la fin (geste-repete) ;
  - une intention apres la parole (fin-sans-intention).
"""
import io
import json
import os
import subprocess
import sys

from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
IMAGES = os.path.join(ICI, "01-images")
TEL = os.path.join(ICI, "_a-televerser")
PROMPTS = os.path.join(ICI, "_essai-avatar", "prompts")
VOIX = os.path.join(RACINE, "audio", "scenes", "dtz-oral")

# LES DEUX IMAGES SONT RECADREES SERRE, sans bandeau de table vide sous les mains (3 nov. 2026, essai payé 1,17 $) :
# sur mark-dtz.png entier, Kling a incruste une ligne de faux sous-titres sur la table vide du bas, de 1,5 s a la fin
# (texte_incruste.py : 186). Le cadre 9:16 s'arrete juste sous les mains : plus de place vide ou poser du texte, et
# le visage grossit (acquis « RECADRER une prise payee plutot que d'en racheter une »). Fenetres relevees a l'oeil
# sur les images 1536 x 2752.
CADRES = {"anna-dtz": (282, 140, 1282, 1918), "anna-dtz-sourire": (282, 140, 1282, 1918), "mark-dtz": (120, 380, 1256, 2400)}
# LES TROIS VERDICTS, ANNA SOURIANTE (4 nov. 2026, Jacques : « un peu plus souriante comme Marc », pour la video qui
# reste a faire ; accord « go », 1,80 $) : anna-dtz.png RETOUCHEE (plan 84), rien d'autre ne change. Les autres clips
# gardent anna-dtz.
SOURIANTE = {"a_ende_B1", "a_ende_A2", "a_ende_moins"}

POITRINE = {
    "anna": "Across her chest we see only the plain grey-blue cardigan, open, and the plain white blouse, from the first frame to the last.",
    "mark": "Across his chest we see only the plain dark green knit of his sweater, from the first frame to the last.",
}
DEBUT = {
    "anna": "The woman in the picture sits at the table and speaks German into the lens, in a calm, warm, clear voice, as an examiner who is kind and unhurried. Let her face follow the voice.",
    "mark": "The man in the picture sits at the table and speaks German into the lens, in a relaxed, friendly voice, as a fellow candidate planning something with a friend. Let his face follow the voice.",
}
FIN = {
    "anna": "Finally, when she has finished speaking, she listens without speaking and waits for the answer: she keeps looking into the lens, she blinks, she breathes, her face stays attentive.",
    "mark": "Finally, when he has finished speaking, he listens without speaking and waits for the answer: he keeps looking into the lens, he blinks, he breathes, still smiling.",
}
CAMERA = "The camera is locked on a tripod and stays there for the whole shot: the same lens, the same height, the same distance."
QUEUE = {
    "anna": "The framing holds to the very end: in the last frame she is the same size and in the same place in the picture as in the first.",
    "mark": "The framing holds to the very end: in the last frame he is the same size and in the same place in the picture as in the first.",
}

# Ce que fait chaque replique : le verbe de parole, puis le geste (une main dite immobile d'abord).
GESTES = {
    "a_bienvenue": "She greets and explains how the exam begins. Her hand nearer the left edge of the picture rests on the table for the whole shot. Only her other hand moves: on her last sentence it opens, palm up, a few centimetres above the table in front of her, as an invitation to begin, and it stays there, open and empty.",
    "a_danke_mark": "She thanks and invites. She gives one small nod, and her hand nearer the right edge of the picture slides a few centimetres forward on the table towards the lens, palm up, and stays there, offered.",
    "a_frage_familie": "She asks a question. Her head tilts a little to one side and her eyebrows lift with interest; her two hands stay folded on the table, empty, for the whole shot.",
    "a_frage_beruf": "She asks a question. Her gaze stays warm and steady; her hand nearer the right edge of the picture opens a little on the table, its empty fingers spreading apart, and stays open.",
    "a_frage_freizeit": "She asks a question with pleasure. Her smile grows until it reaches her eyes and her shoulders relax; her empty hands rest one over the other on the wood.",
    "a_frage_deutsch": "She asks a question. Her eyebrows rise and her chin lifts slightly, curious; her hands lie on the table, fingers interlaced, empty.",
    "a_fotos": "She explains the next task. Her hand nearer the left edge of the picture stays still on the table. Her other hand, open and empty, slides a few centimetres along the table towards the middle, in front of her, and rests flat there.",
    "a_ihr_foto": "She asks a short question and gives one small encouraging nod; her joined hands stay on the table, empty.",
    "a_erfahrung": "She asks about experiences. Her hand nearer the left edge of the picture stays flat on the table. Her other hand rises a few centimetres from the wood and turns from palm down to palm up, open, and stays open.",
    "a_planen": "She explains the last task. Her two hands come apart and each comes to rest flat on the table, palms down, a hand's width from each other, and they stay there.",
    "a_ende_B1": "She announces a good result. A wide, warm smile spreads over her face and she nods twice, slowly, pleased; her hands stay folded on the table.",
    "a_ende_A2": "She announces a result and encourages. Her hand nearer the left edge of the picture stays on the table. Her other hand lifts a few centimetres, and its thumb and index finger come close together, almost touching, and stay like that.",
    # 3 nov. 2026 : << leans back in her chair >> a fait RECULER la camera (le cadre s'elargit de moitie) ; le buste ne bouge plus.
    "a_ende_moins": "She announces a result and encourages. Her shoulders and her back stay where they are for the whole shot. Her hand nearer the left edge of the picture stays flat on the table; her other hand comes to rest gently on top of it, and she presses her lips together in a kind, encouraging smile.",
    "m_p1": "He makes a suggestion and asks for an opinion. His hand nearer the left edge of the picture stays on the table. Only his other hand moves: on his question it lifts a few centimetres, palm up and open towards the lens, and stays there.",
    "m_p2": "He asks a question and makes a suggestion. His hand nearer the right edge of the picture rests on the table; his other hand lifts its index finger a few centimetres from the wood, as for an idea, and holds it there.",
    "m_p3": "He offers two options. His two hands come apart and each opens palm up on the table, one on each side, as if holding the two options, and they stay open.",
    "m_p4": "He asks a question and makes an offer. His eyebrows rise, amused, and his smile widens with his mouth closed after the question; his hands stay joined on the table, empty.",
    "m_p5": "He asks who will do the task. His hand nearer the left edge of the picture stays still. His other hand, open and empty, moves a few centimetres along the table towards the lens, palm up, and stays there, offering.",
    "m_ok": "He agrees with enthusiasm: one big, happy nod, his smile widening; his empty hands stay loosely joined on the wood.",
    "m_ok2": "He agrees: a short, relaxed nod and a half-smile that reaches his eyes; his forearms stay lying on the table.",
    "m_nein": "He concedes good-naturedly: his head tilts to one side and both eyebrows lift, with a good-natured smile; his hands lie flat on the table, empty.",
    "m_nachfrage": "He asks what was meant. His eyes narrow a little and his eyebrows draw together, curious, and his face stays like that; his empty hands rest on the table.",
    # 3 nov. 2026 : << sits up straight >> a fait sauter le cadre a mi-prise (il se redresse, la camera le suit) ; le buste ne bouge plus.
    "m_ende": "He sums up happily and beams. His shoulders and his back stay where they are for the whole shot. His hand nearer the left edge of the picture stays on the table; his other hand lifts a few centimetres from the wood in a small thumbs-up, and holds it there.",
}


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), check=True)


def main():
    sc = json.load(io.open(os.path.join(RACINE, "scenes", "dtz-oral.json"), encoding="utf-8"))
    os.makedirs(TEL, exist_ok=True)
    os.makedirs(PROMPTS, exist_ok=True)

    maitres = {}
    for qui, nom in (("anna", "anna-dtz"), ("anna-sourire", "anna-dtz-sourire"), ("mark", "mark-dtz")):
        cadre = os.path.join(IMAGES, nom + "-cadre.png")
        Image.open(os.path.join(IMAGES, nom + ".png")).convert("RGB").crop(CADRES[nom]).resize((1080, 1920), Image.LANCZOS).save(cadre)
        maitres[qui] = (nom, cadre)

    manque = [p["id"] for p in sc["plans"] if p["video"] and p["id"] not in GESTES]
    if manque:
        sys.exit("  sans geste : %s" % ", ".join(manque))
    n = 0
    for p in sc["plans"]:
        if not p["video"]:
            continue
        qui, num = p["locuteur"], p["n"]
        nom, src = maitres["anna-sourire" if p["id"] in SOURIANTE else qui]
        jpg = os.path.join(TEL, "plan%02d-%s.jpg" % (num, nom))
        im = Image.open(src).convert("RGB")
        if im.width > 1080:
            im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
        im.save(jpg, quality=90)
        voix = os.path.join(VOIX, "%02d-%s.mp3" % (num, qui))
        ff("-f", "lavfi", "-t", "0.25", "-i", "anullsrc=r=44100:cl=mono", "-i", voix,
           "-f", "lavfi", "-t", "1.3", "-i", "anullsrc=r=44100:cl=mono",
           "-filter_complex", "[1:a]aresample=44100,aformat=channel_layouts=mono[v];[0:a][v][2:a]concat=n=3:v=0:a=1",
           "-c:a", "libmp3lame", "-b:a", "128k", os.path.join(TEL, "plan%02d-pleine.mp3" % num))
        # La queue d'apres-parole en DERNIER paragraphe, commencant par « Finally » : c'est ce que lit
        # verifier_prompt.py (PARA_FINAL), et ce qui garde le visage vivant pendant la queue de 1,3 s.
        debut, fin = DEBUT[qui], FIN[qui]
        if p["id"] in SOURIANTE:
            debut = debut.replace("as an examiner who is kind and unhurried. Let her face follow the voice.",
                                  "as an examiner who is kind and glad for the candidate. Let her face follow the voice, and between her sentences her warm, open smile comes back.")
            fin = fin.replace("her face stays attentive.", "she keeps her warm, open smile.")
        prompt = "\n\n".join([debut + " " + GESTES[p["id"]], POITRINE[qui], CAMERA + " " + QUEUE[qui], fin])
        io.open(os.path.join(PROMPTS, "plan%02d.txt" % num), "w", encoding="utf-8", newline="\n").write(prompt + "\n")
        n += 1
    print("%d paniers prets dans %s" % (n, os.path.relpath(TEL, RACINE)))


if __name__ == "__main__":
    main()
