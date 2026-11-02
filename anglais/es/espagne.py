# -*- coding: utf-8 -*-
"""L'ESPAGNOL D'ESPAGNE, derive de l'espagnol d'Amerique latine (2 nov. 2026).

Decision de Jacques (2 nov. 2026, « On va faire les deux. Pour Amerique latine
et Espagne ») : deux espagnols d'interface pour l'anglais appris, au choix de
l'usager (Reglages -> Langue -> « ¿Qué español? »). L'Amerique latine est la
BASE complete (le defaut ; le palier 1, ecrit en espagnol neutre, l'est
devenu). L'Espagne n'est qu'une TABLE DE DIFFERENCES posee par-dessus, comme
I18N_PORTUGAIS_BRESIL pour le portugais : on ne traduit pas tout deux fois.

    python anglais/es/espagne.py controle    # chaque cle existe dans la base
    python anglais/es/espagne.py pose        # ecrit const I18N_ES_ESPAGNE dans index.html

INTERFACE : {cle d'I18N ou d'I18N_ANGLAIS : texte d'Espagne}. Ce qui differe :
le vocabulaire (ajustes, añadir, coger, la compra, estantería, ayuntamiento,
el tiempo, bricolaje), le passe recent au pretérito perfecto (« Has escrito »),
« Enhorabuena », « COMPROBAR ». Le tutoiement (tú) est le meme des deux cotes ;
l'interface ne s'adresse jamais a plusieurs personnes (pas de vosotros a poser).
"""
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
INDEX = os.path.join(RACINE, "index.html")

INTERFACE = {
    # Vocabulaire
    "settings_title": "Ajustes",
    "ecoute_reglages_title": "Ajustes",
    "reperes_reglages": "Los ajustes: tu idioma, tu nivel y todo lo demás.",
    "cp_micro_muet": "El micrófono no responde. Revisa que Wortando tenga permiso para usar el micrófono (Ajustes del teléfono) y vuelve a intentarlo.",
    "legende_seance": "Mi práctica de hoy — la cuenta de la izquierda es tu meta diaria, que puedes regular en los ajustes. La práctica te sirve lo que falta de ella: primero los repasos pendientes, luego las palabras nuevas si queda sitio.",
    "legende_objectif": "La barra «Hoy» — las tarjetas hechas desde esta mañana, sobre tu meta. Vuelve a cero cada día. El número buscado se cambia en los ajustes, y también da el tamaño de tu práctica.",
    "notif_denied": "Permiso denegado. Puedes autorizarlo en los ajustes de tu navegador.",
    "rappel_refuse": "Notificaciones rechazadas. Puedes autorizarlas en los ajustes de tu teléfono.",
    "abo_annulation": "Puedes cancelar en cualquier momento desde los ajustes de tu teléfono.",
    "parler_micro_refuse": "No se autorizó el micrófono. Puedes permitirlo en los ajustes del navegador.",
    "voice_none": "No hay ninguna voz instalada para este idioma en este dispositivo. Las frases se leerán con la voz predeterminada, es decir, con mal acento. Añádela en los ajustes de tu teléfono (Accesibilidad › Contenido hablado › Voces).",
    "voice_only_one": "Solo hay una voz instalada. Puedes añadir una mejorada en los ajustes de tu teléfono y luego volver a elegirla aquí.",
    "reglage_questions_desc": "Número de preguntas en la escena del día. Si la escena no tiene suficientes a tu nivel, añade las del nivel anterior, como repaso.",
    "myvocab_add_title": "Añadir a mis tarjetas",
    "myvocab_added": "«{mot}» añadida a tus tarjetas.",
    "myvocab_deja_cours": "«{mot}» ya es una tarjeta del curso — no hace falta añadirla.",
    "search_none_scope": "El curso cubre {n} tarjetas, del nivel {debut} al {fin}. Esta palabra está fuera del programa — mira la entrada del diccionario de arriba y toca el + para añadirla a tus tarjetas.",
    "vhs_kapitel_none_yet": "Todavía no se ha añadido ningún capítulo.",
    "seance_scene_buergeramt": "Mark en el ayuntamiento",
    "seance_scene_zug": "Mark coge el tren",
    "seance_scene_supermarkt": "Anna hace la compra",
    "seance_scene_heimwerken": "Mark monta una estantería",
    "op_scenes_hiver_d": "El invierno y el tiempo",
    "op_scenes_bricolage_d": "El bricolaje y las herramientas",
    "verify_button": "COMPROBAR",
    # Le passe recent : pretérito perfecto en Espagne
    "cp_tu_as_ecrit": "Has escrito:",
    "myvocab_full": "Has llegado a {n} palabras apartadas. Repásalas antes de añadir más.",
    "rappel_propose_texte": "¡Enhorabuena por este logro! ¿Quieres que Wortando te recuerde tu práctica cada día a las {h}, solo los días en que todavía no hayas alcanzado tu meta? La hora se cambia en los ajustes.",
}


def base():
    """L'interface d'Amerique latine, dans sa source : les lots (I18N.es et I18N_ANGLAIS.es)."""
    d = {}
    for c in sorted(glob.glob(os.path.join(ICI, "lots", "i18n-*.es.json"))) + [os.path.join(ICI, "lots", "surcharge-en.es.json")]:
        d.update(json.load(io.open(c, encoding="utf-8")))
    return d


def controler():
    b = base()
    fautes = []
    for k, v in INTERFACE.items():
        if k not in b:
            fautes.append("cle inconnue de la base : " + k)
        elif v == b[k]:
            fautes.append("identique a l'Amerique latine (inutile) : " + k)
        elif sorted(re.findall(r"\{\w+\}", v)) != sorted(re.findall(r"\{\w+\}", b[k])):
            fautes.append("marques differentes : " + k)
    print("Espagne : %d cles, %d faute(s)" % (len(INTERFACE), len(fautes)))
    for f in fautes:
        print("  FAUTE", f)
    return fautes


def poser():
    if controler():
        raise SystemExit("Des fautes : rien n'est ecrit.")
    html = io.open(INDEX, encoding="utf-8", newline="").read()
    lignes = ",\n".join("    %s: %s" % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in INTERFACE.items())
    bloc = ("const I18N_ES_ESPAGNE = {\n" + lignes + "\n};")
    m = re.search(r"const I18N_ES_ESPAGNE = \{\n.*?\n\};", html, re.S)
    if m:
        html = html[:m.start()] + bloc + html[m.end():]
    else:
        ancre = "if(LANGUE_APPRISE === \"en\"){\n    for(const l of Object.keys(I18N_ANGLAIS)) Object.assign(I18N[l], I18N_ANGLAIS[l]);"
        if html.count(ancre) != 1:
            raise SystemExit("ancre introuvable (fusion d'I18N_ANGLAIS)")
        entete = ("// L'ESPAGNOL D'ESPAGNE (2 nov. 2026) : derive de l'Amerique latine, la base\n"
                  "// d'I18N.es. Genere par anglais/es/espagne.py -- ne pas modifier a la main.\n")
        html = html.replace(ancre, entete + bloc + "\n" + ancre +
                            "\n    if(VARIANTE_INTERFACE_ES === \"es\") Object.assign(I18N.es, I18N_ES_ESPAGNE);")
    io.open(INDEX, "w", encoding="utf-8", newline="").write(html)
    print("Ecrit : const I18N_ES_ESPAGNE dans index.html")


if __name__ == "__main__":
    {"controle": controler, "pose": poser}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: print(__doc__))()
