# -*- coding: utf-8 -*-
"""Le plan des trente episodes : un theme de l'app par episode.

    python scenes/serie.py          ->  scenes/serie.html

L'IDEE, ET POURQUOI ELLE CHANGE L'ECONOMIE DE LA SERIE
    Chaque episode s'appuie sur un theme qui EXISTE DEJA dans themes.json.
    Son vocabulaire est donc dans les cartes avant d'etre dans la video :
    l'apprenant reconnait au lieu de decouvrir, et tests/lexique.py passe par
    construction au lieu d'exiger un ajout a chaque fois.

    On n'ecrit plus un episode puis son lexique. On prend un lexique qui
    existe et on lui ecrit une situation.

LA REGLE DE COMPREHENSIBILITE
    Un texte se comprend quand il est fait de connu plus un peu de neuf.
    L'episode 1 l'a verifie sans le chercher : 26 mots de lexique, dont 22
    deja etudies. C'est ce rapport-la qu'il faut tenir, pas l'inverse.

L'ARC, ET POURQUOI IL EST CHRONOLOGIQUE
    Mark arrive, s'installe, travaille, vit. Les demarches viennent dans
    l'ordre ou la vie les impose -- l'Anmeldung avant le bail, le bail avant
    le compte en banque. Un apprenant qui arrive vraiment en Allemagne suit
    la meme sequence, et peut donc regarder la serie comme un mode d'emploi.

    Le passage du Sie au du (episode 20) est le sommet. Tout ce qui precede
    le prepare, tout ce qui suit en vit. Voir _arc dans personnages.json.
"""
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# n, titre allemand, titre francais, theme, niveau, situation, ce que MARK doit
# savoir dire (c'est le programme oral), presence d'Anna
EPISODES = [
 (1,"Ankunft in Berlin","Arrivée à Berlin","reisen_urlaub","A2",
  "Il atterrit, cherche ses bagages, demande son chemin au guichet.",
  "Demander où se trouve quelque chose, dire d'où l'on vient et pourquoi on est là.",
  "Elle est l'employée du guichet. Premiere rencontre."),
 (2,"Beim Bürgeramt","Au Bürgeramt","stadt_gebaeude","A2",
  "La declaration de domicile obligatoire. Le rendez-vous, le formulaire, la file.",
  "Prendre un rendez-vous, remplir un formulaire, epeler son nom et son adresse.",
  None),
 (3,"Die Wohnungsbesichtigung","La visite d'appartement","wohnen","A2",
  "Il visite un appartement avec une agente. Les pieces, le loyer, les charges.",
  "Poser des questions sur un logement, comprendre un prix, dire ce qu'on cherche.",
  None),
 (4,"Der Umzug","Le déménagement","moebel_haushalt","A2",
  "Il emmenage. Les meubles, les cartons, ce qui manque.",
  "Nommer les meubles, dire ce dont on a besoin, demander de l'aide.",
  None),
 (5,"Im Supermarkt","Au supermarché","einkaufen_geld","A2",
  "Les courses du premier soir. Et il la reconnait dans une allee, hors de son uniforme.",
  "Demander un produit, comprendre un prix, payer.",
  "LES RETROUVAILLES. Hors uniforme, en garde-robe quotidien. Il hesite avant d'oser."),
 (6,"Auf dem Wochenmarkt","Au marché","obst_gemuese","A2",
  "Le marche du samedi. Les fruits, les legumes, les quantites.",
  "Demander une quantite, choisir, comparer.",
  "Ils s'y croisent une seconde fois. Le quartier commence a les reunir."),
 (7,"Das Konto bei der Bank","Le compte en banque","einkaufen_geld","B1",
  "Ouvrir un compte. Les papiers, la carte, les frais.",
  "Expliquer ce qu'on veut ouvrir, comprendre des conditions, poser une question d'argent.",
  None),
 (8,"Der Handyvertrag","Le forfait de téléphone","medien_technologie","A2",
  "Un contrat de telephone. Les options, la duree, ce qu'on ne comprend pas.",
  "Demander des explications, dire qu'on n'a pas compris, refuser poliment.",
  None),
 (9,"Beim Arzt anmelden","S'inscrire chez le médecin","gesundheit","A2",
  "Trouver un medecin traitant, s'inscrire, la carte d'assurance.",
  "Prendre rendez-vous, dire de quoi on souffre, comprendre une consigne.",
  None),
 (10,"Im Restaurant","Au restaurant","essen_trinken","A2",
  "Un premier repas au restaurant. La carte, la commande, l'addition.",
  "Commander, demander une recommandation, payer et laisser un pourboire.",
  "Leur premier repas ensemble. Ils se vouvoient encore, et ca commence a peser."),
 (11,"Kleidung kaufen","Acheter des vêtements","kleidung","A2",
  "L'hiver arrive. Les tailles, les couleurs, l'essayage.",
  "Demander une taille, dire ce qui va ou pas, echanger un article.",
  None),
 (12,"Kochen für Gäste","Cuisiner pour des invités","kueche_kochen","A2",
  "Il cuisine pour la premiere fois chez lui.",
  "Suivre une recette, nommer les ustensiles, inviter quelqu'un.",
  "Elle est invitee. Premiere scene hors d'un lieu public."),
 (13,"Mit der S-Bahn durch Berlin","Berlin en S-Bahn","verkehr","A2",
  "Un trajet qui tourne mal : retard, correspondance, mauvaise direction.",
  "Lire un horaire, demander une correspondance, signaler un probleme.",
  None),
 (14,"Die Nachbarn","Les voisins","wohnen","B1",
  "La cage d'escalier, les regles de l'immeuble, le bruit du dimanche.",
  "Se presenter a un voisin, s'excuser, demander un service.",
  None),
 (15,"Das Wetter und die Jahreszeiten","Le temps et les saisons","wetter","A2",
  "Le premier hiver berlinois. Le froid, la neige, les jours courts.",
  "Parler du temps, dire comment on se sent, faire des projets selon la meteo.",
  None),
 (16,"Der erste Arbeitstag","Le premier jour de travail","arbeit_buero","B1",
  "Le bureau, les collegues, ce qu'on n'ose pas demander.",
  "Se presenter a une equipe, poser une question a un collegue, dire ce qu'on sait faire.",
  None),
 (17,"Termine und Absprachen","Rendez-vous et accords","arbeit_buero","B1",
  "Organiser une reunion, deplacer un rendez-vous, se mettre d'accord.",
  "Proposer une date, refuser, negocier un delai.",
  None),
 (18,"Ein Bewerbungsgespräch","Un entretien d'embauche","berufe","B1",
  "Un entretien pour un meilleur poste.",
  "Parler de son parcours, expliquer une motivation, poser des questions sur un poste.",
  None),
 (19,"Der Sprachkurs","Le cours de langue","schule","B1",
  "Il s'inscrit a un cours du soir. La classe, les exercices, les autres.",
  "S'inscrire, demander une explication, parler de ses difficultes.",
  None),
 (20,"Sie oder du?","Sie ou du ?","gefuehle_charakter","B1",
  "LE SOMMET DE LA SERIE. Le passage du vouvoiement au tutoiement se propose, "
  "s'accepte, et a un moment precis.",
  "Proposer le tutoiement, accepter, parler de ce qu'on ressent.",
  "L'episode est le sien autant que le sien. Ne pas le depenser trop tot."),
 (21,"Sport im Verein","Le sport au club","sport","B1",
  "Il s'inscrit dans un club. Les horaires, les regles, l'equipe.",
  "S'inscrire a une activite, comprendre des regles, encourager quelqu'un.",
  None),
 (22,"Ein Konzert","Un concert","musik_kunst","B1",
  "Les billets, la salle, ce qu'on en dit apres.",
  "Acheter des billets, donner son avis, decrire une impression.",
  "Ils y vont ensemble. Ils se tutoient depuis l'episode 20."),
 (23,"Am Wochenende","Le week-end","freizeit_hobbys","B1",
  "Ce qu'on fait de son temps libre a Berlin.",
  "Proposer une activite, accepter ou refuser, raconter son week-end.",
  None),
 (24,"Beim Arzt","Chez le médecin","koerperteile","A2",
  "Une vraie consultation. Ou on a mal, depuis quand, ce qu'on prend.",
  "Decrire une douleur, situer sur le corps, comprendre une ordonnance.",
  None),
 (25,"Ein Fest bei Freunden","Une fête chez des amis","feste_feiertage","B1",
  "Un anniversaire. Les cadeaux, les toasts, la petite gene sociale.",
  "Feliciter, offrir, remercier, prendre conge.",
  "Elle le presente a ses amis. Il n'est plus un nouvel arrivant."),
 (26,"Im Grünen","Au vert","natur","A2",
  "Une sortie hors de la ville. Le lac, la foret, le silence.",
  "Decrire un paysage, proposer une excursion, parler de ce qu'on aime.",
  None),
 (27,"Umwelt und Alltag","L'environnement au quotidien","umwelt","B1",
  "Le tri, la consigne, le velo plutot que la voiture.",
  "Expliquer un geste, poser une question pratique, defendre une habitude.",
  None),
 (28,"Die Familie am Telefon","La famille au téléphone","familie","A2",
  "Montreal appelle. Ce qu'on raconte et ce qu'on tait.",
  "Parler de sa famille, raconter sa semaine, rassurer quelqu'un.",
  None),
 (29,"Ein schwieriges Gespräch","Une conversation difficile","gefuehle_charakter","B1",
  "Un desaccord. Dire ce qui ne va pas sans blesser.",
  "Exprimer un desaccord, s'excuser, expliquer un sentiment.",
  "C'est avec elle. La serie a gagne le droit d'avoir une scene comme celle-la."),
 (30,"Ein Jahr in Berlin","Un an à Berlin","zeit_kalender","B1",
  "Un an jour pour jour apres l'episode 1. Le meme aeroport, un autre homme.",
  "Raconter une annee, comparer avant et apres, dire ce qu'on a appris.",
  "Boucle avec l'episode 1. Le meme comptoir, et cette fois c'est lui qui renseigne quelqu'un."),
]


def themes_dispo():
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]
    d = {}
    for t in th:
        base = re.sub(r"_(a1|a2|b1|b2|c1)$", "", t["id"])
        d.setdefault(base, {"nom": t["nom_theme"], "niv": {}})
        d[base]["niv"][t["niveau"]] = len(t["mots"])
    return d


def html(dispo):
    e = lambda s: str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    o = ["""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Wortando &mdash; le plan des 30 &eacute;pisodes</title><style>
:root{color-scheme:light}
body{margin:0;background:#F2EEE2;color:#1C2430;
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:60rem;margin:0 auto;padding:2rem 1.25rem 5rem}
h1{font-size:1.7rem;margin:0 0 .25rem}
.sous{color:#6b6558;margin:0 0 2rem}
.note{background:#fff;border:1px solid #e2dcc9;border-radius:10px;padding:1rem 1.25rem;margin-bottom:2.5rem}
h2.bloc{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:#6b6558;
 margin:2.5rem 0 .75rem;border-bottom:1px solid #d8d1bd;padding-bottom:.3rem}
article{background:#fff;border:1px solid #e2dcc9;border-radius:10px;padding:1rem 1.15rem;margin-bottom:.9rem}
article.fait{border-color:#7a9a5b;background:#f6faf2}
article.sommet{border-color:#E8A23A;background:#fdf7ec}
.tete{display:flex;gap:.6rem;align-items:baseline;flex-wrap:wrap;margin-bottom:.5rem}
.num{font:600 1.05rem ui-monospace,Menlo,Consolas,monospace;color:#6b6558}
.de{font-size:1.1rem;font-weight:600}
.fr{color:#6b6558}
.tag{font-size:.72rem;background:#eae4d3;color:#5a5446;border-radius:4px;padding:.1rem .45rem}
.tag.n{background:#1C2430;color:#e8e4d8}
p{margin:.35rem 0}
.lab{font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:#6b6558}
.anna{border-left:3px solid #E8A23A;padding-left:.7rem;margin-top:.6rem}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) body{background:#15181d;color:#e8e4d8}
:root:not([data-theme="light"]) article,:root:not([data-theme="light"]) .note{background:#1e232a;border-color:#2e353f}
:root:not([data-theme="light"]) .fr,:root:not([data-theme="light"]) .sous,
:root:not([data-theme="light"]) .lab,:root:not([data-theme="light"]) h2.bloc{color:#9aa3ae}
:root:not([data-theme="light"]) .tag{background:#2e353f;color:#c9d1da}
:root:not([data-theme="light"]) article.fait{background:#1b2620;border-color:#4a6b3a}
:root:not([data-theme="light"]) article.sommet{background:#2a2318;border-color:#8a6a2a}}
</style></head><body><main>"""]
    o.append("<h1>Le plan des 30 épisodes</h1>")
    o.append('<p class="sous">Un thème de l\'app par épisode &middot; ~90 s chacun &middot; '
             'généré par <code>scenes/serie.py</code></p>')
    o.append("""<div class="note"><p><b>Le principe.</b> Chaque épisode s'appuie sur un thème
qui existe <b>déjà</b> dans <code>themes.json</code>. Son vocabulaire est donc dans les cartes
avant d'être dans la vidéo : l'apprenant <b>reconnaît</b> au lieu de découvrir.</p>
<p><b>Ce que ça change.</b> On n'écrit plus un épisode puis son lexique. On prend un lexique qui
existe et on lui écrit une situation. <code>tests/lexique.py</code> passe par construction.</p>
<p><b>Les répliques de Mark sont le programme.</b> Ce sont les phrases que l'apprenant devra
savoir produire — l'oral du DTZ et du B1. Celles d'Anna et des employés sont ce qu'il doit
savoir comprendre.</p></div>""")

    blocs = [(1, 9, "L'installation &mdash; les démarches d'un nouvel arrivant"),
             (10, 15, "Le quotidien &mdash; vivre dans le quartier"),
             (16, 20, "Le travail, et le basculement"),
             (21, 30, "La vie &mdash; une année complète")]
    for d0, d1, titre in blocs:
        o.append('<h2 class="bloc">%s &nbsp;·&nbsp; épisodes %d à %d</h2>' % (titre, d0, d1))
        for n, de, fr, th, niv, sit, mark, anna in EPISODES:
            if not (d0 <= n <= d1):
                continue
            info = dispo.get(th)
            mots = info["niv"].get(niv, 0) if info else 0
            nom = info["nom"] if info else "THEME INTROUVABLE"
            cls = " class=\"fait\"" if n == 1 else (" class=\"sommet\"" if n == 20 else "")
            o.append("<article%s>" % cls)
            o.append('<div class="tete"><span class="num">%02d</span>'
                     '<span class="de">%s</span><span class="fr">%s</span>'
                     '<span class="tag n">%s</span><span class="tag">%s &middot; %d mots</span>%s</div>'
                     % (n, e(de), e(fr), niv, e(nom), mots,
                        '<span class="tag">TOURNÉ</span>' if n == 1 else ''))
            o.append("<p>%s</p>" % e(sit))
            o.append('<p><span class="lab">Mark doit savoir</span><br>%s</p>' % e(mark))
            if anna:
                o.append('<div class="anna"><span class="lab">Anna</span><br>%s</div>' % e(anna))
            o.append("</article>")
    o.append("</main></body></html>")
    return "\n".join(o)


def main():
    dispo = themes_dispo()
    perdus = [(n, th) for n, _, _, th, _, _, _, _ in EPISODES if th not in dispo]
    if perdus:
        sys.exit("  THEMES INTROUVABLES : %s" % perdus)
    maigres = [(n, th, niv, dispo[th]["niv"].get(niv, 0))
               for n, _, _, th, niv, _, _, _ in EPISODES if dispo[th]["niv"].get(niv, 0) < 10]
    if maigres:
        print("  ATTENTION, moins de 10 mots disponibles :")
        for n, th, niv, c in maigres:
            print("     episode %02d  %s %s  %d mots" % (n, th, niv, c))
    out = os.path.join(RACINE, "scenes", "serie.html")
    io.open(out, "w", encoding="utf-8", newline="").write(html(dispo))
    themes = {th for _, _, _, th, _, _, _, _ in EPISODES}
    print("  %d episodes, %d themes distincts, tous presents dans themes.json"
          % (len(EPISODES), len(themes)))
    print("  ->  scenes/serie.html")


if __name__ == "__main__":
    main()
