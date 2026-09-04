# Message aux testeurs — WhatsApp, brouillon du 4 septembre 2026

Trois versions du même message court : français, anglais, turc.

⚠️ **En conversation individuelle, jamais en groupe.** Un groupe WhatsApp
montre le numéro de téléphone de chacun à tous les autres — c'est pire qu'une
copie conforme par courriel.

**Deux questions, pas trois.** Sur WhatsApp, une liste de questions ne reçoit
pas de réponse. J'ai gardé celle à laquelle n'importe qui peut répondre, et celle
dont tu as vraiment besoin : qui est sur Android.

---

## Français

> Salut [prénom] 👋
>
> Petite nouvelle : ta progression dans Wortando ne se sauvegardait pas — un
> bug que j'ai trouvé et corrigé aujourd'hui. Si tu avais l'impression que ça
> ne suivait pas, tu avais raison. Rien n'est perdu.
>
> Deux questions rapides :
> 1. D'après toi, qu'est-ce qu'on devrait améliorer en premier ?
> 2. Tu as un téléphone Android ? (je prépare une version Play Store)
>
> Merci 🙏 Ton accès reste gratuit quoi qu'il arrive.

---

## English

> Hi [first name] 👋
>
> Quick news: your progress in Wortando wasn't being saved — a bug I found and
> fixed today. If you ever felt it wasn't keeping up, you were right. Nothing
> was lost.
>
> Two quick questions:
> 1. What do you think we should improve first?
> 2. Do you have an Android phone? (I'm preparing a Play Store version)
>
> Thanks 🙏 Your access stays free whatever happens.

---

## Türkçe

> Merhaba [ad] 👋
>
> Küçük bir haber: Wortando'daki ilerlemen kaydedilmiyordu — bugün bulup
> düzelttiğim bir hata. Bir şeylerin geride kaldığını hissettiysen haklıydın.
> Hiçbir şey kaybolmadı.
>
> İki kısa soru:
> 1. Sence ilk olarak neyi geliştirmeliyiz?
> 2. Android telefonun var mı? (Play Store sürümü hazırlıyorum)
>
> Teşekkürler 🙏 Erişimin ne olursa olsun ücretsiz kalacak.

⚠️ Le turc est de moi et n'a pas été relu par un locuteur natif, contrairement
aux traductions de l'app. Pour un message court le risque est faible ; à toi de
voir si tu préfères l'anglais avec cette personne.

---

## Ce que j'ai coupé, et pourquoi

- **La liste des nouveautés** (dictionnaire, C1, voix enregistrée, examens).
  Trop long pour WhatsApp, et ça noie la question qui compte. À garder pour une
  relance plus tard, ou pour ceux qui répondent.
- **La troisième question** (« y a-t-il eu un moment où tu as décroché ? »).
  Excellente au courriel, une de trop ici.
- **« Qu'as-tu ouvert une fois sans jamais y revenir ? »** — écartée : elle
  demande de se souvenir de ce qu'on n'a PAS fait, ce que personne ne sait
  faire. « Qu'est-ce qu'on devrait améliorer en premier » se répond aussi bien
  après deux séances qu'après deux mois. Le « en premier » fait le travail :
  il demande de choisir, donc il rapporte une chose précise plutôt qu'une
  liste polie ou un silence.

## Des réponses

- Chaque remarque va dans `journal-retours.md` — date, testeur, ce qui est dit,
  et plus tard le numéro de version qui y répond.
- Tenir à part **la liste de qui est sur Android**. Il en faut douze pour le
  test fermé du Play Store, et viser quatorze ou quinze : un seul désistement
  remet les quatorze jours à zéro.

---

## Réponse à Kirsty — 4 septembre 2026

Elle écrit : *« Let me know once it's compatible with Android too and I will
get it on Peters phone. »* Elle attend une compatibilité **qui existe déjà**.

⚠️ Si elle le croit, d'autres le croient aussi. À dire explicitement à tout le
monde, pas seulement à elle.

> Hi Kirsty 👋
>
> That's really kind of you, thank you. Two bits of news.
>
> **The plural now has its own speaker button** — you asked this morning, it's
> already in. Tap the small speaker next to the plural form and you'll hear it.
> Thank you for that one: it was a real gap and I hadn't seen it. If you don't
> see the button yet, close the app and open it again once.
>
> **And it already works on Android.** Wortando is a web app, so it opens in
> any browser, on any phone. Peter can even add it to his home screen and it
> behaves like a normal app, offline included. So no need to wait for me.
>
> Here is Peter's invitation code: **[CODE]**
> He just opens the link, taps "Create an account" and enters it. The code
> works once, and it's his.
>
> What's coming later is the Play Store version — same app, just distributed
> through Google. That's the one that needs a formal testing round, and I'll
> ask you then.
>
> Enjoy the weekend with it, and don't spare me 🙂

**À faire avant d'envoyer :**

1. **Générer le code** — ⚙️ Réglages → Administration → Tableau de bord →
   GÉNÉRER UN NOUVEAU CODE, puis remplacer `[CODE]` dans le message.
2. **Annoter le code** dans le tableau de bord (champ note à côté) : « Peter,
   via Kirsty ». Sinon, dans trois semaines, personne ne saura à qui il a servi.
3. **Joindre le lien** — https://jacquesagrenier-star.github.io/Deutsch-gemini/
4. **Noter Peter comme testeur ANDROID** dans `cle-testeurs.txt`. Il en faut
   douze pour le test fermé, l'app n'enregistre aucune information d'appareil,
   et cette liste ne se reconstitue pas toute seule. Peter est le premier
   confirmé.
