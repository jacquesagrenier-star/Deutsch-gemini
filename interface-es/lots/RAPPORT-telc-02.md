# Rapport — telc-02 (pages d'entraînement telc A2·B1, interface espagnole)

## Chiffres

- Source : `interface-es/sources/telc-02.json`, 726 textes (Lesen 291, oral 263, Schreiben 106, Sprachbausteine 66).
  Lot : `interface-es/lots/telc-02.es.json`, **726 clés sur 726**.
- Contrôle `textes.py controle` : **0 FAUTE**, 10 avis, tous de l'allemand cité (`du`, `Du`, `des` dans « Hast du … », « du vertrittst », « des Fahrpreises ») : rien à corriger.
- Les numéros ci-dessous sont le rang de l'entrée dans la source (0 à 725).

## Choix constants (alignés sur telc-01)

- Gardés en allemand : les noms des parties, Volkshochschule, Frau Becker / Frau Krüger, Repair-Café, Zweite Chance, WG, tous les mots et phrases cités ; les exemples entre parenthèses (weil, denn, deshalb…).
- courriel → correo ; examen blanc → simulacro de examen ; compétences → habilidades ; Retour → Volver ; Parler → Hablar ; piège → trampa ; annonce → anuncio ; formule d'appel / salutation → saludo / despedida ; heures « 18:00 » ; cave → sótano ; eau brune → agua café ; salle de cours → salón (de clases).
- Tutoiement dans toute l'interface et les explications. **Usted** pour les répliques d'Anna l'examinatrice (599-605, 611-614, 620, 626, 632-635, 642-643), « ustedes » quand elle s'adresse aux deux candidats ; Mark tutoie.
- Amérique latine : carro, celular, boleto, rentar / la renta, apartamento, autobús, manejar, jugo, pastel, estacionamiento, cobija, bocina (enceinte), papás.
- Citations allemandes entre « … » sans espace avant « ? » ni « ! ».

## Sources fautives ou divergentes

- n° 54 : le français ajoute « et c'était déjà le cas » (la sauna), absent de l'anglais. J'ai suivi le français (« y ya era así »).
- n° 117-120 : le français met « Les ordonnances » en tête de la question et des pronoms dans les options ; l'anglais dit « Patients should… » / « collect their prescriptions… ». J'ai suivi la construction anglaise (la clé), pour que chaque option se lise seule.
- n° 176 : le français écrit la citation allemande avec une espace avant les deux-points (« Volkshochschule : im Hotel ») ; rendu sans espace, comme l'anglais.
- n° 178 : le français dit « si les deux premières sont gratuites », l'anglais « if two are free » ; suivi l'anglais, plus proche de l'allemand cité.
- n° 236 : le français cite « im Preis … enthalten », l'anglais coupe à « im Preis » ; gardé la citation française, plus complète.
- n° 276-277 : français « Aujourd'hui, au magasin, viennent… / aussi des gens… », anglais « The shop's customers today include… / people who… » ; suivi l'anglais.
- n° 543 : français « Contenu (partie I) », anglais « Content (criterion I) » ; le n° 545 parle aussi de « partie I » en français et de « criterion I » en anglais. J'ai mis **criterio I** aux deux (telc-01 dit aussi « criterio II »).
- n° 652-653 : les modèles 1B changent de genre d'une réponse à l'autre dans le français (vendeuse, puis infirmier ; « marié ») ; gardé tel quel (vendedora, enfermero, casado).

## Doutes

- n° 516 : « Je suis prêt » → **« Ya estoy »** (sans genre ; « Estoy listo » supposerait un homme).
- n° 579 : « te présenter seul » → « presentarte por tu cuenta » (sans genre). De même 578 « Bravo d'être allé jusqu'au bout » → « ¡Bravo por llegar hasta el final! ».
- n° 317, 343, 650-651, 709, 714, 717 : phrases modèles à la 1re personne, masculin comme le français (enfermo, casado, solo).
- n° 349 : « Ich wünsche Ihnen eine schöne Zeit! » → « ¡Le deseo que la pase muy bien! » (usted singulier ; « Ihnen » peut aussi être pluriel).
- n° 469 : « ton coach » → « tu coach » (courant en Amérique latine ; sinon « tu entrenador »).
- n° 572, 695, 721 : compromis → « punto medio » (« compromiso » veut d'abord dire engagement).
- n° 609 : « Tu veux dire quoi ? » → « ¿Qué quieres decir? ».
- n° 704 : « Tandempartner » → « un compañero de intercambio de idiomas ».
- n° 677 : « belegte Brötchen » → « panes rellenos » (voir À trancher).
- n° 299, 326 : « 2e place » → « 2.ª posición ».

## À trancher (l'Amérique latine hésite)

- n° 452 : barbecue (l'événement) → **una parrillada** (telc-01 dit « la parrilla » pour l'appareil ; Mexique : « una carne asada »).
- n° 16, 233-234, 268, 281, 663-664, 687-688 : gâteau → **pastel** (Colombie : torta, ponqué) ; « Torten mit Sahne » → « pasteles con crema ».
- n° 55-58, 66, 215, 220 : piscine / bassin → **piscina** partout (Mexique : alberca) ; le bassin pour enfants est « una piscina para niños pequeños ».
- n° 3, 7 : eau brune → agua café (comme telc-01).
- n° 35, 37, 640, 709 : loyer → **la renta** (Colombie : el arriendo) ; louer → rentar.
- n° 48 : WG → « apartamento compartido » ; « appartement d'une pièce » → « apartamento de un solo ambiente ».
- n° 143, 146, 636, 693-694, 697 : parking → **estacionamiento** (Colombie : parqueadero).
- n° 162-166 : bac (Kiste du jardin sur le toit) → **cajón** ; jardin → **huerto**.
- n° 177-193 : enlèvement des encombrants → **la recolección** ; déchetterie → « centro de reciclaje » ; s'inscrire → registrarse.
- n° 263 : sac (Tasche) → **bolsa** (Colombie : bolso, maleta) ; bureau des objets trouvés → « oficina de objetos perdidos ».
- n° 264 : entrepôt → **bodega** (aussi « almacén »).
- n° 284-285 : soupe populaire → **comedor comunitario**.
- n° 397 : gérance (Hausverwaltung) → « la administración de su edificio ».
- n° 408 : Volkshochschule → « centro de educación para adultos (Volkshochschule) ».
- n° 430 : abonnement au club de sport → **membresía** del gimnasio.
- n° 600, 644, 649 : stage → **unas prácticas** (Colombie : una pasantía).
- n° 618 : enceinte → **bocina** (Colombie : parlante).
- n° 622, 672-673 : camionnette → **camioneta** (aussi « furgoneta », plutôt d'Espagne).
- n° 333, 675 : couverture → **cobija** (aussi « manta »).
- n° 654-655 : « juego fútbol » sans « al » (usage américain).
