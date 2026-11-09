# -*- coding: utf-8 -*-
"""Les paniers des 35 clips de l'oral du telc, pour video/omnihuman.py --scene telc-oral --modele kling. GRATUIT.

    python video/episode-telc-oral/preparer_clips.py

Memes images, memes phrases de cadre et memes regles que l'oral du DTZ (video/episode-dtz-oral/preparer_clips.py) :
un vrai verbe de parole, la camera verrouillee, l'interlocuteur jamais nomme, la poitrine decrite, les mains dites et
vides (les repliques nomment un buste de salade, des fleurs, un livre, un telephone : objet-qui-se-materialise), UN
geste par replique tenu jusqu'a la fin, le buste qui ne bouge pas, jamais de geste vers un bord du cadre.
"""
import io
import json
import os
import subprocess
import sys

from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
IMAGES = os.path.join(RACINE, "video", "episode-dtz-oral", "01-images")
TEL = os.path.join(ICI, "_a-televerser")
PROMPTS = os.path.join(ICI, "_essai-avatar", "prompts")
VOIX = os.path.join(RACINE, "audio", "scenes", "telc-oral")

MAITRES = {"anna": "anna-dtz", "mark": "mark-dtz"}

POITRINE = {
    "anna": "Across her chest we see only the plain grey-blue cardigan, open, and the plain white blouse, from the first frame to the last.",
    "mark": "Across his chest we see only the plain dark green knit of his sweater, from the first frame to the last.",
}
DEBUT = {
    "anna": "The woman in the picture sits at the table and speaks German into the lens, in a calm, warm, clear voice, as an examiner who is kind and unhurried. Let her face follow the voice.",
    "mark": "The man in the picture sits at the table and speaks German into the lens, in a relaxed, friendly voice, as a fellow candidate planning something with a friend. Let his face follow the voice.",
    "contre": "The man in the picture sits at the table and speaks German into the lens, in a relaxed, friendly voice, as a fellow candidate who sees the matter differently and enjoys the discussion. Let his face follow the voice.",
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

# Le verbe de parole, puis UN geste. Toutes differentes : geste-repete.
GESTES = {
    # Anna : les consignes
    "t_plan_fest": "She explains a task with pleasure. Her hand nearer the right edge of the picture stays flat on the table. Her other hand turns over on the wood, palm up, its empty fingers relaxed, and stays like that.",
    "t_plan_umzug": "She explains a task. Her head tilts a little to one side and stays there, her gaze warm; her two empty hands lie side by side on the table, fingers together.",
    # 8 nov. 2026 : << lifts its index finger and holds it there >>, tenu 17 s, donne une maitresse d'ecole : un doigt leve ne se tient pas sur une replique longue.
    "t_plan_geschenk": "She explains a task and smiles at the idea. Her two empty hands lie joined on the table, her thumbs side by side, and her warm smile comes back between her sentences.",
    "t_avis_auto": "She explains the last task and asks a question. Her two empty hands lie flat on the table, a hand's width apart, and her eyebrows lift when she asks the question, and stay lifted a moment.",
    "t_avis_lernen": "She explains the last task and asks a question. Her hand nearer the left edge of the picture stays flat on the table; her other hand comes to rest on the wood with its thumb against its index finger, empty.",
    "t_avis_land": "She explains the last task and asks a question. Her empty hands rest one over the other on the wood, and a soft smile stays in her eyes.",
    "t_a_los": "She invites someone to begin. She gives one short nod, and her empty hand nearer the right edge of the picture opens on the table, palm up, and stays open.",
    "t_avis_buero": "She explains the last task and asks a question. Her chin lifts slightly, curious; her empty hand nearer the right edge of the picture rests on the wrist of her other hand on the table.",
    "t_avis_handy": "She explains the last task and asks a question. Her eyebrows draw a little closer, thoughtful; her two empty hands lie on the table with the fingers loosely interlaced.",
    # Mark : planifier une fete
    "t_fest_1": "He makes a suggestion and asks for an opinion. His hand nearer the left edge of the picture stays on the table; his other hand rises a few centimetres, palm down and empty, and stays level above the wood.",
    "t_fest_2": "He asks where and offers two places. His head tilts a little to one side and stays there, curious; his empty hands stay loosely joined on the wood.",
    "t_fest_3": "He asks a question and offers to help. His hand nearer the left edge of the picture stays on the table; the open fingers of his other hand come to rest against the middle of his chest, empty, and stay there.",
    "t_fest_4": "He asks a question and makes an offer. His smile widens until his eyes narrow with amusement; his forearms lie on the table, his hands apart and empty.",
    "t_fest_5": "He asks a question and makes a gentle suggestion. His two empty hands come together a few centimetres above the table, fingertips touching, and stay there.",
    # Mark : aider a demenager
    "t_umzug_1": "He asks when and makes a suggestion. His eyebrows rise on the question; one empty hand rests closed on the table and the other rests on top of it.",
    # 8 nov. 2026 : << slide apart ... until each is under one of his shoulders >> a fait monter les deux mains aux epaules : ne jamais accrocher une main a une partie du haut du corps.
    "t_umzug_2": "He names a problem and makes a suggestion. His eyebrows rise as he names the problem; his two empty hands lie flat on the table, a forearm's length apart, and they stay there.",
    "t_umzug_3": "He asks a question and says what he will bring. His hand nearer the right edge of the picture stays on the table; his other hand lifts a few centimetres, loosely closed and empty, and holds there.",
    "t_umzug_4": "He jokes and makes a suggestion. A broad, amused smile stays on his face between his sentences; his two empty hands lie flat on the table, close together.",
    "t_umzug_5": "He asks a question and makes a warm suggestion. His chin lifts a little and a happy half-smile reaches his eyes; his forearms lie crossed on the table, his hands empty.",
    # Mark : un cadeau
    "t_geschenk_1": "He asks a question and suggests an idea. His eyebrows rise with the idea at the end; his empty hands lie one over the other on the wood.",
    "t_geschenk_2": "He asks how much and proposes an amount. His hand nearer the right edge of the picture stays on the table; his other hand lifts a few centimetres with its five empty fingers spread, and holds there.",
    "t_geschenk_3": "He asks where and offers two ways. His two empty hands turn palm up on the table, the one nearer the left edge of the picture a little higher than the other, and they stay like that.",
    "t_geschenk_4": "He asks when and makes a suggestion. His eyes narrow a little as he thinks, then his smile returns; his hands stay joined, the two thumbs resting side by side, empty.",
    "t_geschenk_5": "He asks who will do the task. His hand nearer the left edge of the picture slides a few centimetres along the table towards the lens, palm down and empty, and stays there.",
    # Mark : l'avis contraire
    "t_auto_gegenA": "He disagrees kindly and asks for a reaction. A half-smile stays on his face. His hand nearer the left edge of the picture stays flat on the table; his other hand turns palm up on the wood, open and empty, and stays open.",
    "t_auto_gegenB": "He disagrees kindly and asks for a reaction. His two empty hands rise a few centimetres together, palms facing each other a small distance apart, and they stay there.",
    "t_lernen_gegenA": "He disagrees cheerfully and asks for a reaction. His hand nearer the right edge of the picture stays on the table; his other hand lifts its index finger a few centimetres from the wood and holds it there.",
    "t_lernen_gegenB": "He disagrees kindly and asks for a reaction. He shakes his head once, slowly, at the start, then his eyes stay warm; his empty hands stay with the fingers interlaced on the table.",
    "t_land_gegenA": "He disagrees happily and asks for a reaction. His shoulders stay low and relaxed, and a warm smile grows through the sentences; his empty hands rest one over the other on the wood.",
    "t_land_gegenB": "He disagrees kindly and asks for a reaction. His eyebrows draw together a little; his hand nearer the left edge of the picture stays flat on the table and the empty fingers of his other hand spread apart on the wood.",
    "t_buero_gegenA": "He disagrees kindly and asks for a reaction. He nods twice, slowly, as he talks about his own days; his forearms lie side by side on the table, his hands empty.",
    "t_buero_gegenB": "He disagrees kindly and asks for a reaction. His hand nearer the left edge of the picture stays on the table; his other hand slides a few centimetres towards the middle of the table, palm down and empty, and rests flat there.",
    "t_handy_gegenA": "He disagrees seriously and asks for a reaction. His face stays thoughtful, his eyebrows together; his two empty hands stay joined, fingers interlaced, the two thumbs resting side by side on top, on the table.",
    "t_handy_gegenB": "He disagrees kindly and asks for a reaction. His eyebrows lift, his gaze steady; his two empty hands lie open on the table, palms up, close together.",
    "t_m_schluss": "He concedes with good humour. One small nod and a smile with his mouth closed after his sentence; one empty hand rests over the other on the table.",
}


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), check=True)


def main():
    sc = json.load(io.open(os.path.join(RACINE, "scenes", "telc-oral.json"), encoding="utf-8"))
    os.makedirs(TEL, exist_ok=True)
    os.makedirs(PROMPTS, exist_ok=True)
    manque = [p["id"] for p in sc["plans"] if p["id"] not in GESTES]
    if manque:
        sys.exit("  sans geste : %s" % ", ".join(manque))
    n = 0
    for p in sc["plans"]:
        qui, num = p["locuteur"], p["n"]
        nom = MAITRES[qui]
        jpg = os.path.join(TEL, "plan%02d-%s.jpg" % (num, nom))
        im = Image.open(os.path.join(IMAGES, nom + "-cadre.png")).convert("RGB")
        if im.width > 1080:
            im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
        im.save(jpg, quality=90)
        voix = os.path.join(VOIX, "%02d-%s.mp3" % (num, qui))
        if os.path.exists(voix):
            ff("-f", "lavfi", "-t", "0.25", "-i", "anullsrc=r=44100:cl=mono", "-i", voix,
               "-f", "lavfi", "-t", "1.3", "-i", "anullsrc=r=44100:cl=mono",
               "-filter_complex", "[1:a]aresample=44100,aformat=channel_layouts=mono[v];[0:a][v][2:a]concat=n=3:v=0:a=1",
               "-c:a", "libmp3lame", "-b:a", "128k", os.path.join(TEL, "plan%02d-pleine.mp3" % num))
        debut = DEBUT["contre" if "_gegen" in p["id"] else qui]
        prompt = "\n\n".join([debut + " " + GESTES[p["id"]], POITRINE[qui], CAMERA + " " + QUEUE[qui], FIN[qui]])
        io.open(os.path.join(PROMPTS, "plan%02d.txt" % num), "w", encoding="utf-8", newline="\n").write(prompt + "\n")
        n += 1
    print("%d paniers prets dans %s" % (n, os.path.relpath(TEL, RACINE)))


if __name__ == "__main__":
    main()
