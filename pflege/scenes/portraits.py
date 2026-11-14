# -*- coding: utf-8 -*-
"""Les portraits maîtres des soignants (personnages validés par Jacques le 14 nov. 2026).

    python pflege/scenes/portraits.py            # écrit pflege/scenes/portrait-<id>.prompt.txt
    python pflege/outils/generer_scene.py portrait-elif --ref soins-aufnahme --format 3:4 --payer

UNE IMAGE MAÎTRESSE PAR SOIGNANT, comme Herr Brandt et Frau Lehmann : en pied, de face à trois
quarts, fond de studio gris clair uni, tenue de service, aucune écriture (pas de badge nominatif).
Toute image où il revient le reçoit en référence (verifier_prompt : personne-sans-reference), y
compris celles de la session de l'examen blanc. Les traits ci-dessous sont DÉCIDÉS ICI (la fiche
pflege/PERSONNAGES.md ne donne que l'âge, le pays et le poste) : un trait changé après la première
image demande de refaire l'image, et toutes celles qui la prennent en référence.

LA RÉFÉRENCE DE STYLE est une photo AVEC des personnes (soins-aufnahme) : sans photo de référence,
le modèle a rendu deux scènes sur cinq en illustration dessinée (14 nov.).

LES TENUES SUIVENT LE LIEU, pour qu'on reconnaisse d'un coup d'œil qui travaille où :
  - Klinikum am Kanal (Elif, Yusuf, Jonas, Frau Hoffmann) : tunique et pantalon blancs ;
    Frau Hoffmann, cadre, un gilet bleu marine par-dessus ;
  - Dr. Sommer : blouse blanche ouverte sur un chemisier bleu clair, stéthoscope ;
  - Haus Lindenhof (Arun, Olena) : polo vert sauge et pantalon bleu marine ;
  - soins à domicile (Amira) : polo bleu marine, pantalon gris foncé, veste polaire bleu marine.

LE FOULARD : Amira seulement (décision de Jacques du 14 nov., « Amira seulement ») — sobre, uni, bleu
marine, compatible avec la tenue de soins à domicile. Elif n'en porte pas.

OLENA REFAITE (retour de Jacques du 14 nov.) : la première ressemblait trop à Anna
(visuel/prototype/descripcion/Anna.webp : fine, cheveux châtain clair tirés en arrière). Visage rond et
large, pommettes marquées, rides d'expression, carré blond doré lâché aux épaules, silhouette plus forte.
"""
import io
import os

ICI = os.path.dirname(os.path.abspath(__file__))

TETE = (
    "A real photograph, taken with a good phone camera and looking exactly like a phone photograph, of one "
    "{qui} standing in a plain photographic studio, in a tall vertical picture, the whole person in view from the "
    "top of the head to the shoes, with a band of plain background above the head and below the feet, "
    "everything in sharp focus. Natural colours, soft even daylight from the front left. The textures of real "
    "cotton, skin and hair, with the true depth and the slight lens perspective of a photograph.\n\n"
    "The reference picture is a real phone photograph taken in the same hospital: use it for the photographic "
    "look only (the same true-to-life rendering, the same natural colours and fine detail, nothing drawn or "
    "painted). Its room and its people do not appear here.\n\n"
    "THE BACKGROUND is a plain seamless light-grey studio wall that curves into a light-grey floor, with a soft "
    "shadow under the shoes. The picture carries no writing, numbers, print, symbol or logo anywhere: the "
    "clothes have no name badge, no embroidery and no brand.\n\n"
)
PIED = (
    "\n\nThe person stands upright and relaxed, the body turned a little to the left of the picture and the "
    "face turned towards the camera, both arms relaxed at the sides, both hands empty and fully in view, the "
    "two feet flat on the floor a little apart. The expression is natural and friendly, caught as if the "
    "photographer had just said something kind; the eyes look just past the camera."
)

SOIGNANTS = {
    "elif": ("young woman of twenty-nine from Turkey, a nurse",
             "SHE is of medium height and slim, with olive skin, warm dark-brown eyes, straight dark eyebrows, a small "
             "straight nose and an open, cheerful smile. Her long dark-brown hair is tied back in a low ponytail, a few "
             "loose strands at her temples. Small round silver stud earrings. She wears a plain white short-sleeved "
             "nurse's tunic with a V-neck and two lower pockets, plain white trousers, and white closed nursing shoes. "
             "A black ballpoint pen is clipped to the breast pocket, and a slim black wristwatch is on her wrist."),
    "amira": ("young woman of twenty-six from Tunisia, a home-care nurse",
              "SHE is of medium height, with light-brown skin, dark-brown eyes, full dark eyebrows, a round face and a "
              "bright, energetic smile. She wears a plain navy-blue jersey headscarf, neatly wrapped around her head and "
              "pinned under the chin, covering her hair and neck and tucked into the collar of her fleece, simple and "
              "practical for work, with no pattern. She wears a plain navy-blue polo shirt, dark-grey trousers, a zipped navy-blue fleece jacket left open, and black trainers."),
    "arun": ("man of thirty-one from Kerala in India, a nurse in a care home",
             "HE is of medium height and build, with dark-brown skin, short neat black hair parted on the side, dark eyes "
             "behind thin black-framed glasses, a short neat black moustache and a gentle, patient smile. He wears a "
             "plain sage-green short-sleeved polo shirt, navy-blue trousers and black closed shoes."),
    "yusuf": ("man of thirty-four from Syria, a nurse who works night shifts",
              "HE is tall and broad-shouldered, with light olive skin, short black hair, a short well-trimmed black beard, "
              "dark eyes and a calm, kind, slightly tired look. He wears a plain white short-sleeved nurse's tunic, plain "
              "white trousers and white closed shoes."),
    "olena": ("woman of forty-four from Ukraine, a nurse in a care home",
              "SHE is of medium height with a solid, sturdy build, broad shoulders and a full figure. Her face is round "
              "and wide, with high, marked cheekbones, a broad short nose, light-blue eyes, fine expression lines at the "
              "corners of the eyes and across the forehead, and a broad, warm, motherly smile. Her hair is dark golden "
              "blonde, cut in a straight blunt bob that hangs loose and touches her shoulders, with a side parting; it "
              "is not tied back. She wears a plain sage-green short-sleeved polo shirt, navy-blue trousers and black "
              "closed shoes."),
    "jonas": ("German man of thirty-eight, a senior nurse who trains new colleagues",
              "HE is tall and lean, with fair skin, short sandy-blond hair, light stubble, blue eyes and an amused, "
              "friendly grin. He wears a plain white short-sleeved nurse's tunic, plain white trousers and white trainers; "
              "a pair of trauma scissors and a black pen sit in the breast pocket."),
    "hoffmann": ("German woman of fifty-two, the head nurse of a hospital ward",
                 "SHE is of medium height, with fair skin, a short grey-blonde bob, rectangular dark-framed glasses, a "
                 "composed, attentive face and a small, fair smile. She wears a plain white nurse's tunic and white "
                 "trousers, with a plain navy-blue knitted cardigan open over the tunic, and white closed shoes."),
    "sommer": ("German woman of forty, a hospital doctor",
               "SHE is slim and of medium height, with fair skin and light freckles, short dark-brown hair in a pixie cut, "
               "hazel eyes and a bright, direct smile. She wears a white doctor's coat, open, over a plain pale-blue "
               "blouse, dark-grey trousers and dark-grey trainers; a black stethoscope hangs around her neck."),
}

if __name__ == "__main__":
    for i, (qui, corps) in SOIGNANTS.items():
        io.open(os.path.join(ICI, "portrait-%s.prompt.txt" % i), "w", encoding="utf-8").write(
            TETE.format(qui=qui) + corps + PIED + "\n")
    print("%d prompts : %s" % (len(SOIGNANTS), ", ".join(SOIGNANTS)))
