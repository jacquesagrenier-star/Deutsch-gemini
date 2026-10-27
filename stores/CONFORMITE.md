# Conformité Google Play et App Store

26 octobre 2026. Ce qui pourrait nous faire refuser, ce qui est réglé, et les
réponses toutes prêtes pour les formulaires. **Source de vérité des données :
[confidentialite.html](../confidentialite.html)** ; si l'app change ce qu'elle
collecte, on corrige la politique ET ces réponses dans le même tour.

## 1. Fait le 26 oct. (v968)

- Politique de confidentialité à jour : micro et reconnaissance vocale (2.6),
  messages « Signaler un problème » et leur journal technique (2.5), profil
  d'apprentissage, rappel local, séance hors ligne, Cloudflare.
- Page publique de suppression du compte, sans l'app :
  **https://wortando.com/supprimer-compte** (exigée par Google).
- « Supprimer mon compte » efface aussi le japonais (`usersJa`, `resumesJa`) et
  la séance hors ligne avec les réponses en attente du compte.
- Phrases d'autorisation iPhone (micro, reconnaissance) rendues exactes :
  wortando-ios 82b18a1. ⚠️ **Une compilation iOS (n°11) est nécessaire avant
  la soumission à l'App Store** : la n°10 porte encore « Nothing is sent
  anywhere ». Android n'a pas changé. La reconnaissance n'est pas forcée sur
  l'appareil (un iPhone ancien perdrait le verdict de l'oral, argument 4.2).

## 2. À faire par Jacques dans les consoles

### Google Play Console
1. **Contenu de l'appli → Sécurité des données** : remplir avec le §3.
   Champ « URL de suppression du compte » : `https://wortando.com/supprimer-compte`.
2. **Accès à l'appli** : compte de démo avec mot de passe qui marche le jour de
   l'examen (en oct., celui du compte `+googleplay` avait été oublié).
3. **Avant la demande d'accès à la production** (vers le 6 nov.) : que les
   12 testeurs **ouvrent l'app Android plusieurs fois** pendant les 14 jours, et
   qu'au moins quelques-uns laissent un avis dans « Commentaires des
   testeurs ». Google pose des questions sur ce test et refuse souvent quand
   l'usage a été maigre. Garder des notes : ce qui a été corrigé grâce aux
   testeurs (le journal des retours en est plein).

### App Store Connect
0. **Lancer la compilation iOS n°11** (Codemagic, workflow ios-testflight, main) avant de soumettre.
1. **App Privacy** : remplir avec le §4.
2. **App Review Information** : compte de démo + mot de passe ; coller les notes
   de `wortando-ios/revision-apple/NOTES-REVISEUR.md`.
3. **iPad** : si l'app reste installable sur iPad, il faut des captures iPad
   13 pouces et une mise en page correcte ; sinon, la limiter à l'iPhone.
4. URL de confidentialité : `https://wortando.com/confidentialite`.

## 3. Google Play — Sécurité des données

Chiffrement en transit : **oui** (HTTPS partout). Suppression : **oui**, dans
l'app et par la page web. Données partagées avec des tiers : **non** (Firebase,
Cloudflare, Apple/Google pour la voix sont des sous-traitants, ce que Google ne
compte pas comme « partage »).

| Catégorie Google | Donnée | Collectée | Obligatoire | Finalités |
|---|---|---|---|---|
| Infos personnelles | Adresse e-mail | Oui | Oui | Fonctionnement, gestion du compte |
| Infos personnelles | Nom (prénom) | Oui | Oui | Fonctionnement (personnalisation) |
| Activité dans l'appli | Interactions (progression, séances, mots cherchés, profil d'apprentissage) | Oui | Oui | Fonctionnement, personnalisation, analyses |
| Activité dans l'appli | Autre contenu généré (messages « Signaler un problème ») | Oui | Non | Fonctionnement (correction de bugs) |
| Infos et performances de l'appli | Diagnostics (journal technique joint au signalement ; version, ouvertures) | Oui | Non | Analyses, correction de bugs |
| Identifiants de l'appareil | ID d'instance Analytics ; jeton de notification (web) | Oui | Non | Analyses ; notifications |
| Position | Approximative (pays/région via l'IP, Analytics) | Oui | Non | Analyses |
| Audio | Enregistrements vocaux | **Non collectée** : traitée sur l'appareil ou par le service de reconnaissance du système, jamais reçue par Wortando | — | — |

Publicité : **aucune**. Identifiant publicitaire : **non**.

## 4. Apple — App Privacy (étiquette)

Données « liées à l'utilisateur », **aucune** « utilisée pour le pistage » :

- **Coordonnées** : adresse e-mail, nom → Fonctionnalité de l'app.
- **Contenu utilisateur** : autre contenu (messages de signalement) → Fonctionnalité de l'app.
- **Utilisation** : interactions avec le produit → Analyse, Fonctionnalité de l'app, Personnalisation.
- **Diagnostics** : autres données de diagnostic → Fonctionnalité de l'app.
- **Identifiants** : ID d'appareil/instance (Analytics) → Analyse.
- **Localisation** : approximative → Analyse.
- **Audio** : *ne pas déclarer* si la reconnaissance se fait sur l'appareil ;
  si elle passe par les serveurs d'Apple, Apple le traite comme un service du
  système (pas une collecte par l'éditeur) — on ne la déclare pas, et la
  politique l'explique (2.6).

## 5. Risques restants, par ordre

1. **Google : accès à la production** refusé faute d'usage réel des testeurs (§2).
2. **Apple 4.2** (simple site emballé) : parades en place — rappel local,
   vibrations, reconnaissance vocale, séance hors ligne (module dans la
   compilation 10). Les citer dans les notes au réviseur.
3. **Inscription sur invitation** : passe à l'examen avec le compte de démo,
   mais une app publique où personne ne peut s'inscrire paraîtra inachevée →
   ouvrir l'inscription (échantillon gratuit / essai) avant la sortie publique.
4. **Abonnement (plus tard)** : Google Play Billing et achat intégré Apple
   obligatoires (RevenueCat) ; afficher prix, renouvellement automatique,
   conditions d'utilisation (EULA) et confidentialité sur l'écran d'achat ;
   bouton « Restaurer mes achats » ; aucun lien vers un paiement sur le site.
5. **Contenu généré par IA** (voix ElevenLabs, images, vidéos) : pas une
   fonction d'IA générative pour l'usager, donc pas de politique « IA » de
   Google à remplir ; droits commerciaux vérifiés (voir `video/DROITS-omnihuman.md`).
