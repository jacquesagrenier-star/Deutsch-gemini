# -*- coding: utf-8 -*-
"""Les phrases allemandes que la relecture complete a trouvees fautives, et qui
touchent une voix enregistree. Accord de Jacques le 2 nov. 2026 : « Oui,
jusqu'a 5 000 » (credits, decisions/DECISIONS.md).

    python retours/qualite-es-de/phrases_relecture.py           # montre
    python retours/qualite-es-de/phrases_relecture.py --ecrire  # applique

Deux parties :
  1. le « Perfekt » au passif Präteritum (« Die Formel wurde … hergeleitet »)
     de 86 verbes, refait mecaniquement en « ist … worden » ; le sens ne
     change pas, les traductions (deja au passe compose) restent ;
  2. les phrases isolees, chacune avec ses traductions quand le sens change.
Chaque remplacement verifie le texte actuel : si le fichier a change, refus.
Les voix : voix_relecture.py, sur la difference du manifeste.
"""
import io
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
JOURNAL = os.path.join(ICI, "corrections-phrases-voix.json")
L9 = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]


def tr(champ, valeurs):
    """{champ_fr: …, champ_en: …} depuis une liste dans l'ordre de L9."""
    return {"%s_%s" % (champ, l): v for l, v in zip(L9, valeurs)}


# (fichier, chemin, {champ: (avant, apres)}) -- avant=None : on ne le verifie
# pas (traduction recrite en entier, l'ancienne est au journal).
ISOLEES = [
    ("themes.json", "obst_gemuese_a1.mots[5]", {
        "exemple": ("Die Zwiebel macht mich weinen.", "Die Zwiebel bringt mich zum Weinen.")}),
    ("themes.json", "politik_gesellschaft_b1.mots[55]", {
        "exemple": ("Die EU-Bürgerin braucht für die Reise keinen Visum.",
                    "Die EU-Bürgerin braucht für die Reise kein Visum.")}),
    ("themes.json", "vhs_kapitel16_b1.mots[11]", {
        "exemple": ("Die EU-Bürgerin braucht für die Reise keinen Visum.",
                    "Die EU-Bürgerin braucht für die Reise kein Visum.")}),
    ("themes.json", "politik_gesellschaft_b1.mots[58]", {
        "pluriel": ("—", "Geburtsurkunden")}),
    ("themes.json", "vhs_kapitel8_b1.verben[1]", {
        "konjunktiv2": ("Ohne Handy würde ich mir den Alltag kaum vorstellen.",
                        "Ohne Handy könnte ich mir den Alltag kaum vorstellen.")}),
    ("themes.json", "vhs_kapitel16_b1.verben[3]", dict(
        {"perfekt": ("Sie hat die deutsche Staatsbürgerschaft seit einem Jahr besessen.",
                     "Sie hat die deutsche Staatsbürgerschaft ein Jahr lang besessen.")},
        **{k: (None, v) for k, v in tr("perfekt", [
            "Elle a eu la nationalité allemande pendant un an.",
            "She held German citizenship for a year.",
            "Bir yıl boyunca Alman vatandaşlığına sahip oldu.",
            "Вона рік мала німецьке громадянство.",
            "او یک سال شهروندی آلمان را داشت.",
            "حملت الجنسية الألمانية لمدة سنة.",
            "Ela teve a cidadania alemã durante um ano.",
            "Przez rok miała niemieckie obywatelstwo.",
            "Год у неё было немецкое гражданство.",
        ]).items()})),
    ("verbe.json", "A2[166]", dict(
        {"praeteritum": ("Sie deckte das Kind mit einer Decke zu.",
                         "Sie deckte den Tisch für vier Personen.")},
        **{k: (None, v) for k, v in tr("praeteritum", [
            "Elle a mis la table pour quatre personnes.",
            "She set the table for four people.",
            "Dört kişilik sofra kurdu.",
            "Вона накрила стіл на чотирьох.",
            "او میز را برای چهار نفر چید.",
            "أعدّت المائدة لأربعة أشخاص.",
            "Ela pôs a mesa para quatro pessoas.",
            "Nakryła stół dla czterech osób.",
            "Она накрыла стол на четверых.",
        ]).items()})),
    ("verbe.json", "A2[167]", dict(
        {"praeteritum": ("Wir steckten eine Stunde im Aufzug fest.",
                         "Der Schlüssel steckte noch im Schloss.")},
        **{k: (None, v) for k, v in tr("praeteritum", [
            "La clé était encore dans la serrure.",
            "The key was still in the lock.",
            "Anahtar hâlâ kilitteydi.",
            "Ключ ще стирчав у замку.",
            "کلید هنوز توی قفل بود.",
            "كان المفتاح لا يزال في القفل.",
            "A chave ainda estava na fechadura.",
            "Klucz wciąż tkwił w zamku.",
            "Ключ всё ещё торчал в замке.",
        ]).items()})),
    ("verbe.json", "B1[118]", {
        "praesens.ihr": ("übersehet", "überseht"),
        "imperativ.ihr": ("Übersehet!", "Überseht!")}),
    # erschrecken : les quatre phrases sont au verbe faible transitif
    # (effrayer) ; la traduction et les formes du verbe fort intransitif
    # (avoir peur, du erschrickst) ne collaient pas. On suit les phrases.
    ("verbe.json", "B1[152]", {
        "traduction": ("avoir peur, être effrayé", "effrayer, faire peur à"),
        "traduction_en": ("to be frightened", "to scare, to frighten"),
        "praesens.du": ("erschrickst", "erschreckst"),
        "praesens.er_sie_es": ("erschrickt", "erschreckt"),
        "imperativ.du": ("Erschrick!", "Erschreck!")}),
    ("verbe.json", "B1[176]", {
        "praeteritum": ("Sie losten die Startreihenfolge aus.",
                        "Sie losten um die Startreihenfolge.")}),
    ("verbe.json", "B1[212]", dict(
        {"konjunktiv2": ("Ohne Wind würde niemand die Segel blasen sehen.",
                         "Bei Kälte würde ich mir in die Hände blasen.")},
        **{k: (None, v) for k, v in tr("konjunktiv2", [
            "Par grand froid, je soufflerais dans mes mains.",
            "In the cold I would blow on my hands.",
            "Soğukta ellerime üflerdim.",
            "На морозі я б дмухав собі на руки.",
            "در سرما به دست‌هایم ها می‌کردم.",
            "في البرد كنت سأنفخ في يديّ.",
            "No frio, eu sopraria nas mãos.",
            "Na mrozie chuchałbym w dłonie.",
            "На холоде я бы дул на руки.",
        ]).items()})),
    ("verbe.json", "B1[403]", dict(
        {"konjunktiv2": ("Ohne Hilfe würde ich das nicht schaffen zu pflegen.",
                         "Ohne Hilfe würde ich es nicht schaffen, sie zu pflegen.")},
        **{k: (None, v) for k, v in tr("konjunktiv2", [
            "Sans aide, je n'arriverais pas à la soigner.",
            "Without help I wouldn't manage to care for her.",
            "Yardım olmadan ona bakmayı başaramazdım.",
            "Без допомоги я б не впорався з доглядом за нею.",
            "بدون کمک نمی‌توانستم از او مراقبت کنم.",
            "من دون مساعدة لما استطعت أن أعتني بها.",
            "Sem ajuda, eu não conseguiria cuidar dela.",
            "Bez pomocy nie dałbym rady się nią opiekować.",
            "Без помощи я бы не справился с уходом за ней.",
        ]).items()})),
    ("verbe.json", "B1[426]", {
        "konjunktiv2": ("Bei gutem Wetter würde ich eine Wanderung vorhaben.",
                        "Bei gutem Wetter hätte ich eine Wanderung vor.")}),
    ("verbe.json", "B1[433]", dict(
        {"exemple": ("Der Winter geht langsam zu Ende.", "Die Tür geht nicht zu.")},
        **{k: (None, v) for k, v in tr("exemple", [
            "La porte ne ferme pas.",
            "The door won't close.",
            "Kapı kapanmıyor.",
            "Двері не зачиняються.",
            "در بسته نمی‌شود.",
            "الباب لا يُغلق.",
            "A porta não fecha.",
            "Drzwi się nie domykają.",
            "Дверь не закрывается.",
        ]).items()})),
    ("verbe.json", "B1[471]", {
        "praeteritum": ("Das Paar schied im letzten Jahr.",
                        "Das Paar ließ sich im letzten Jahr scheiden.")}),
    # krankmelden : « ich melde mich krank » ; le drapeau n'affiche qu'une
    # pastille, il ne change ni l'infinitif ni une voix
    ("verbe.json", "B1[513]", {"reflexiv": (False, True)}),
    ("verbe.json", "C1[13]", dict(
        {"perfekt": ("Den Widerstand hatte niemand einkalkuliert.",
                     "Den Widerstand hat niemand einkalkuliert.")},
        **{k: (None, v) for k, v in tr("perfekt", [
            "Personne n'a prévu la résistance.",
            "Nobody factored in the resistance.",
            "Direnci kimse hesaba katmadı.",
            "Опору ніхто не врахував наперед.",
            "کسی آن مقاومت را در محاسبه نگنجانده است.",
            "لم يحسب أحد حساب المعارضة.",
            "Ninguém contou com a resistência.",
            "Nikt nie wziął pod uwagę oporu.",
            "Сопротивления никто не предусмотрел.",
        ]).items()})),
    ("verbe.json", "C1[82]", {
        "praeteritum": ("Man archivierte die Fotos nach Jahren.",
                        "Man archivierte die Fotos nach Jahren geordnet.")}),
    # « Perfekt » qui n'en etaient pas : passif d'etat (ist / war … -t) et
    # hochfahren intransitif conjugue avec haben (lot 3 de la relecture)
    ("verbe.json", "C1[23]", {
        "perfekt": ("Das Projekt ist finanziell abgesichert.",
                    "Das Projekt ist finanziell abgesichert worden."),
        "perfekt_fr": (None, "Le projet a été sécurisé financièrement."),
        "perfekt_en": (None, "The project has been financially secured."),
        "perfekt_tr": (None, "Proje mali açıdan güvenceye alındı."),
        "perfekt_uk": (None, "Проєкт фінансово убезпечили."),
        "perfekt_ar": (None, "تمّ تأمين المشروع ماليًّا."),
        "perfekt_pt": (None, "O projeto foi garantido financeiramente."),
        "perfekt_pl": (None, "Projekt został zabezpieczony finansowo."),
        "perfekt_ru": (None, "Проект был финансово обеспечен.")}),
    ("verbe.json", "C1[45]", {
        "perfekt": ("Der Vorgang ist urkundlich bezeugt.",
                    "Der Vorgang ist urkundlich bezeugt worden."),
        "perfekt_fr": (None, "Le fait a été attesté par un document."),
        "perfekt_en": (None, "The event has been documented in records."),
        "perfekt_tr": (None, "Olay resmî belgeyle kanıtlandı."),
        "perfekt_ar": (None, "تمّ توثيق الواقعة بالمستندات."),
        "perfekt_pt": (None, "O fato foi documentado em registros."),
        "perfekt_pl": (None, "To zdarzenie zostało poświadczone w dokumentach.")}),
    ("verbe.json", "C1[89]", {
        "perfekt": ("Das Kapitel ist fein untergliedert.",
                    "Das Kapitel ist fein untergliedert worden."),
        "perfekt_fr": (None, "Le chapitre a été subdivisé avec finesse."),
        "perfekt_en": (None, "The chapter has been finely subdivided."),
        "perfekt_tr": (None, "Bölüm ince ince alt bölümlere ayrıldı."),
        "perfekt_ar": (None, "قُسِّم الفصل بدقّة."),
        "perfekt_pt": (None, "O capítulo foi bem subdividido."),
        "perfekt_pl": (None, "Rozdział został drobiazgowo podzielony."),
        "perfekt_ru": (None, "Глава была подробно разбита на разделы.")}),
    ("verbe.json", "C1[115]", {
        "perfekt": ("Der Beitrag war sauber recherchiert.",
                    "Der Beitrag ist sauber recherchiert worden."),
        "perfekt_fr": (None, "L'article a été solidement documenté."),
        "perfekt_en": (None, "The piece has been properly researched."),
        "perfekt_tr": (None, "Yazı düzgün biçimde araştırıldı."),
        "perfekt_uk": (None, "Матеріал ретельно опрацювали."),
        "perfekt_fa": (None, "آن مطلب با دقت تحقیق شده است."),
        "perfekt_ar": (None, "دُرِس التقرير بعناية."),
        "perfekt_pl": (None, "Materiał został rzetelnie przygotowany.")}),
    ("verbe.json", "C1[171]", dict(
        {"perfekt": ("Der Rechner hat lange hochgefahren.",
                     "Der Rechner ist sehr langsam hochgefahren.")},
        **{k: (None, v) for k, v in tr("perfekt", [
            "L'ordinateur a démarré très lentement.",
            "The computer booted up very slowly.",
            "Bilgisayar çok yavaş açıldı.",
            "Комп'ютер завантажувався дуже повільно.",
            "آن رایانه خیلی کند بالا آمد.",
            "أقلع الحاسوب ببطء شديد.",
            "O computador ligou muito devagar.",
            "Komputer uruchamiał się bardzo wolno.",
            "Компьютер загружался очень медленно.",
        ]).items()})),
    ("verbe.json", "C1[75]", {
        "perfekt": ("Der Einbruch war vorgetäuscht.",
                    "Der Einbruch ist vorgetäuscht worden."),
        "perfekt_fr": (None, "Le cambriolage a été simulé."),
        "perfekt_tr": (None, "Hırsızlık yalandan sahnelendi."),
        "perfekt_fa": (None, "آن دستبرد ساختگی بوده است."),
        "perfekt_ar": (None, "تمّ افتعال السطو.")}),
    ("adjectif.json", "C1[111]", {
        "exemple": ("In dieser Stelle ist sie deutlich unterfordert.",
                    "In dieser Position ist sie deutlich unterfordert.")}),
]

PASSIF = re.compile(r"\b(wurden?)\b")


def perfekt(phrase):
    """« X wurde … gemacht. » -> « X ist … gemacht worden. »"""
    assert phrase.endswith(".") and phrase.count(".") == 1 and "," not in phrase, phrase
    p = PASSIF.sub(lambda m: "sind" if m.group(1) == "wurden" else "ist", phrase, count=1)
    return p[:-1] + " worden."


def noeud(doc, fichier, chemin):
    if fichier == "themes.json":
        tid, reste = chemin.split(".", 1)
        o = next(t for t in doc["themes"] if t["id"] == tid)
        for m in re.finditer(r"(\w+)\[(\d+)\]", reste):
            o = o[m.group(1)][int(m.group(2))]
        return o
    m = re.fullmatch(r"(\w+)\[(\d+)\]", chemin)
    return doc[m.group(1)][int(m.group(2))]


def main():
    ecrire = "--ecrire" in sys.argv
    docs = {f: json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))
            for f in ("themes.json", "verbe.json", "adjectif.json")}
    journal, refus = [], 0

    def poser(f, ch, champ, avant, apres):
        nonlocal refus
        o = noeud(docs[f], f, ch)
        cles = champ.split(".")
        for c in cles[:-1]:
            o = o[c]
        k = cles[-1]
        if o.get(k) == apres:
            return
        if avant is not None and o.get(k) != avant:
            print("REFUS %s %s %s : actuel %r" % (f, ch, champ, o.get(k)))
            refus += 1
            return
        if ("%sHighlight" % k) in o:
            print("REFUS %s %s %s : un surlignage existe, a refaire a la main" % (f, ch, champ))
            refus += 1
            return
        journal.append({"fichier": f, "chemin": ch, "champ": champ, "avant": o.get(k), "apres": apres})
        o[k] = apres

    for niv, liste in docs["verbe.json"].items():
        if not isinstance(liste, list):
            continue
        for i, e in enumerate(liste):
            p = e.get("perfekt") or ""
            if PASSIF.search(p) and "worden" not in p:
                poser("verbe.json", "%s[%d]" % (niv, i), "perfekt", p, perfekt(p))
    for f, ch, champs in ISOLEES:
        for champ, (avant, apres) in champs.items():
            poser(f, ch, champ, avant, apres)

    for j in journal:
        print("%-13s %-34s %-16s %s\n%66s -> %s" % (j["fichier"], j["chemin"], j["champ"],
                                                   j["avant"], "", j["apres"]))
    print("\n%d changements, %d refus" % (len(journal), refus))
    if not ecrire or refus:
        return
    sys.argv = sys.argv[:1]
    from verdicts import format_de
    for f, d in docs.items():
        ind, sep, fin = format_de(f)
        io.open(os.path.join(RACINE, f), "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=ind, separators=sep) + fin)
    ancien = json.load(io.open(JOURNAL, encoding="utf-8")) if os.path.exists(JOURNAL) else []
    json.dump(ancien + journal, io.open(JOURNAL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ecrit.")


if __name__ == "__main__":
    main()
