# À relire : les textes du lecteur de conversations, pour les dialogues des Soins (15 nov. 2026)

Le lecteur des conversations (`visuel/prototype/conversation.html`) joue depuis le 15 nov. les dialogues des Soins
(`?soins=1`). Il ne parlait que français, anglais et arabe ; les Soins ont neuf langues d'interface. Les textes
ci-dessous ont été écrits par Claude (session architecture de Wortando Pflege), sans relecture native. Ils ne
s'affichent que dans les Soins (essai « soins », admin et comptes ouverts un à un).

Où : `UI_SOINS` dans `conversation.html`, juste avant la fonction `u()`.

Points à vérifier par un natif, langue par langue :

- **Le lecteur au neutre** (règle des lots 89 et 90). L'app ne dit jamais « je n'ai rien entendu » au masculin : « Ничего
  не слышно », « Нічого не чути », « Nic nie słychać », « Hiçbir şey duyulmadı », « چیزی شنیده نشد », « Não deu para ouvir
  nada ». « Tu as dit : … » devient une forme sans genre (« Почуто », « Услышано », « Usłyszane », « Duyulan », « شنیده
  شد ») ; en portugais « Ouvimos ».
- **« Bravo »** : « Чудова робота! » (uk) et « Отличная работа! » (ru) plutôt que « Молодець! » / « Молодец! », pour la
  même raison.
- **Le nom de la section** : « Bakım » (tr), « Догляд » (uk), « Уход » (ru), « Opieka » (pl), « Cuidados » (pt),
  « پرستاری » (fa), « الرعاية » (ar). À aligner sur le nom que la tuile Soins portera dans ces langues.
- **« moments »** (le nombre de nœuds d'un dialogue) : « an » (tr), « моментів » / « моментов », « momentów »,
  « momentos », « لحظه ». Les pluriels slaves sont figés au génitif pluriel ; à revoir si le nombre tombe à 2-4.
- **Le persan** s'affiche de droite à gauche, comme l'arabe (la flèche de retour devient « › »).

Rien d'autre n'a changé dans le lecteur pour les conversations de Premiers pas (fr, en, ar).
