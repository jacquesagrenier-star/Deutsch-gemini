# Divergences de la relecture croisee (allemand)

Produit par `python tests/relecture.py --rapport`. **Aucune correction appliquee.** Cette application est en service, avec des testeurs : ce qui remonte ici s'examine, ne s'applique pas en bloc.

Le genre et le pluriel ne figurent pas : `tests/contraste.py` les a deja tranches contre WikDict.

## frase_peu_naturelle (2)

- **Ellbogen** — champ `exemple`
  - suggestion : "Mein Ellbogen ist an der Tür angeschlagen." sonne comme une traduction littérale (le coude comme sujet d'un état passif). Un locuteur natif dirait plutôt : « Ich habe mir den Ellbogen an der Tür angeschlagen. » (construction réfléchie, comme pour Handgelenk/Knie dans le même thème).
- **Ratenzahlung** — champ `exemple`
  - suggestion : "Sie zahlt den Kühlschrank in Ratenzahlung." est redondant (« payer … en paiement-échelonné »). Formulation naturelle : « Sie zahlt den Kühlschrank in Raten. » ou « Sie bezahlt den Kühlschrank per Ratenzahlung. »

## « Fachkraft » est un nom comptable au singulier (une personne qualifiée), mais la traduction « main-d'œuvre qualifiée » est un collectif non comptable en français (on ne dit pas « une main-d'œuvre »). Ça ne colle pas avec la traduction anglaise, correcte et comptable, « skilled worker ». Un apprenant risque de mal utiliser le mot au singulier. (1)

- **Fachkraft** — champ `traduction`
  - suggestion : traduction : « travailleur qualifié » ou « professionnel qualifié » (garder « main-d'œuvre qualifiée » comme équivalent possible seulement au pluriel/collectif, ex. dans l'exemple avec Fachkräften)

## La phrase française inverse « prise » et « fiche » par rapport à l'allemand. « Zieh den Stecker aus der Steckdose » veut dire retirer la fiche (mâle) de la prise (murale) — c'est bien ce que dit exemple_en (« Pull the plug out of the outlet ») et ce que confirme le champ traduction du mot lui-même (« fiche, prise (mâle) »). Mais exemple_fr dit « Débranche la prise de la fiche murale », soit l'inverse : on ne débranche pas une prise d'une fiche, on débranche une fiche d'une prise. (1)

- **Stecker** — champ `exemple_fr`
  - suggestion : Débranche la fiche de la prise murale.

## Le champ traduction donne « réutilisation », mais la phrase d'exemple traduit le même mot par « recyclage » (« Le recyclage du plastique aide l'environnement »), tout comme traduction_en donne « recycling, reuse » et exemple_en dit « recycling ». Les deux champs français se contredisent sur un même mot dans la même fiche. Or Wiederverwertung correspond en allemand au retraitement de matière (recyclage), distinct de Wiederverwendung (réemploi simple sans transformation) — c'est donc le champ traduction qui est imprécis, pas l'exemple. (1)

- **Wiederverwertung** — champ `traduction`
  - suggestion : recyclage, valorisation
