# -*- coding: utf-8 -*-
"""L'ecran « S'entrainer par temps » de l'anglais, C1 : choisir le temps
dans un texte suivi, ou deux temps se disputent la place.
Format des questions : question | bonne | fausse / fausse | traduction | explication.
SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""

TEMPS = [
{
"id": "temps-tous", "titre": "Tous les temps — choisir le bon",
"texte": "Au C1, le temps ne se devine plus par un mot-repère : il dépend du point de vue (récit, bilan, projet), de ce qui est déjà vrai et de ce qui dure. Chaque question met deux temps proches en concurrence.<br><em>I've lived here for years. — I lived there for years. — I'd lived there for years.</em> (J'habite ici depuis des années. — J'y ai habité des années. — J'y habitais depuis des années.)",
"serie": "tempsTousEnExercises", "kicker": "Tous les temps",
"questions": """
I ___ here for six years, and I still love it. | have lived | lived / had lived | J'habite ici depuis six ans, et j'adore toujours autant. | La période continue : present perfect.
I ___ there for six years before I moved to Boston. | had lived | have lived / am living | J'y habitais depuis six ans quand j'ai déménagé à Boston. | Avant un autre passé : past perfect.
I ___ in Denver for six years; then I came back east. | lived | have lived / am living | J'ai vécu six ans à Denver, puis je suis revenu dans l'Est. | Période close du passé : past simple.
Hardly ___ sat down when the phone rang. | had I | I had / did I | À peine m'étais-je assis que le téléphone a sonné. | Hardly + inversion + past perfect.
No sooner ___ we left than it started to pour. | had | have / did | Nous étions à peine partis qu'il s'est mis à pleuvoir à verse. | No sooner had… than.
This is the third time you ___ late this week. | 've been | were / are | C'est la troisième fois que tu es en retard cette semaine. | This is the third time + present perfect.
That was the third time she ___ late that week. | had been | has been / was | C'était la troisième fois qu'elle était en retard cette semaine-là. | That was the… time + past perfect.
By the time the ambulance ___, a crowd had gathered. | arrived | had arrived / arrives | Le temps que l'ambulance arrive, une foule s'était rassemblée. | By the time + past simple.
I'll call you as soon as I ___ the results. | get | will get / got | Je t'appellerai dès que j'aurai les résultats. | As soon as + présent, pour le futur.
I'll lend you the book once I ___ it. | 've finished | will finish / finished | Je te prêterai le livre une fois que je l'aurai fini. | Once + present perfect (antériorité future).
It's high time we ___ home. | went | go / will go | Il est grand temps que nous rentrions. | It's high time + prétérit.
I'd rather you ___ anyone about this. | didn't tell | don't tell / won't tell | Je préférerais que tu n'en parles à personne. | I'd rather + sujet + prétérit.
If only I ___ to her before she left! | had spoken | spoke / would speak | Si seulement je lui avais parlé avant son départ ! | If only + past perfect : regret passé.
I wish you ___ making that noise. | would stop | stopped / will stop | J'aimerais que tu arrêtes de faire ce bruit. | I wish + would : agacement.
I wish I ___ taller. | were | would be / am | J'aimerais être plus grand. | I wish + prétérit (were) : regret présent.
She ___ for the company since 2019, and she's just been promoted. | has been working | worked / is working | Elle travaille pour l'entreprise depuis 2019, et elle vient d'être promue. | Depuis + continue : present perfect continuous.
The witness claimed she ___ the suspect before. | had never seen | has never seen / never sees | Le témoin a affirmé n'avoir jamais vu le suspect auparavant. | Discours rapporté : past perfect.
He'll be exhausted when he arrives — he ___ all night. | will have been driving | will drive / is driving | Il sera épuisé en arrivant : il aura roulé toute la nuit. | Durée jusqu'à un moment futur : will have been + -ing.
The moment I saw him, I knew something ___. | had happened | has happened / happens | Dès que je l'ai vu, j'ai su que quelque chose s'était passé. | Antériorité : past perfect.
According to the forecast, it ___ by the time we land. | will have stopped | stops / will stop yet | D'après la météo, ça se sera arrêté le temps que nous atterrissions. | Will have + participe.
We were going to call you, but we ___ your number. | had lost | have lost / lose | On allait t'appeler, mais on avait perdu ton numéro. | Cause antérieure : past perfect.
I ___ to call you, but I completely forgot. | was going | am going / will go | Je comptais t'appeler, mais j'ai complètement oublié. | Was going to : intention passée non réalisée.
The train ___ at 7:42, so don't be late. | leaves | will be leaving at / has left | Le train part à 7 h 42, alors ne sois pas en retard. | Horaire : present simple.
She ___ her thesis when her laptop crashed. | was finishing | had finished / finishes | Elle terminait sa thèse quand son ordinateur a planté. | Action en cours, interrompue.
By the end of the decade, she ___ three companies. | will have founded | founds / will found by | D'ici la fin de la décennie, elle aura fondé trois entreprises. | Will have + participe.
He ___ his job last year and has been traveling ever since. | quit | has quit / had quit | Il a quitté son emploi l'an dernier et voyage depuis. | Last year : past simple.
I ___ so much better since I started running. | 've been feeling | felt / feel since | Je me sens tellement mieux depuis que j'ai commencé à courir. | Since + proposition : present perfect continuous.
Little ___ that he was being watched. | did he know | he knew / knew he | Il était loin de se douter qu'on l'observait. | Little + inversion avec did.
Not until I got home ___ I had lost my wallet. | did I realize | I realized / had I realize | Ce n'est qu'en rentrant que je me suis rendu compte que j'avais perdu mon portefeuille. | Not until + inversion avec did.
Suppose you ___ the job — would you move to New York? | got | get / will get | Suppose que tu obtiennes le poste : déménagerais-tu à New York ? | Suppose + prétérit : hypothèse.
Had I known, I ___ differently. | would have acted | would act yesterday / acted | Si j'avais su, j'aurais agi autrement. | Had I known = If I had known.
Were she here, she ___ what to do. | would know | will know / knew | Si elle était là, elle saurait quoi faire. | Were she = If she were.
Should you need anything, ___ me. | call | called / would call | Si vous avez besoin de quoi que ce soit, appelez-moi. | Should you = If you should.
He talks as if he ___ everything. | knew | knows it / would know | Il parle comme s'il savait tout. | As if + prétérit : irréel.
She looked as though she ___ a ghost. | had seen | has seen / saw it | Elle avait l'air d'avoir vu un fantôme. | As though + past perfect.
It's the first time I ___ this dish. I love it! | 've tasted | tasted / taste | C'est la première fois que je goûte ce plat. Je l'adore ! | It's the first time + present perfect.
The house ___ for years before they finally sold it. | had been sitting empty | has sat empty / sat emptily | La maison était restée vide des années avant qu'ils la vendent enfin. | Had been + -ing : durée avant un passé.
When I ___ my coffee, I'll start. | 've had | will have / had had | Quand j'aurai bu mon café, je commencerai. | When + present perfect pour une antériorité future.
They ___ the bridge for three years now, and it still isn't finished. | have been repairing | repaired / are repairing for | Ils réparent le pont depuis trois ans, et il n'est toujours pas fini. | Durée jusqu'à maintenant : have been + -ing.
I ___ you were coming — I'd have made dinner. | didn't know | haven't known / don't know | Je ne savais pas que tu venais ; j'aurais préparé le souper. | Ignorance passée : past simple.
""",
},
]
