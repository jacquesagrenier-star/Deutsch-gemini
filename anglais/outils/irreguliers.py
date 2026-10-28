# -*- coding: utf-8 -*-
"""Les verbes irreguliers au-dela de l'A1. SOURCE : on corrige ici.

Meme forme que mots_a1.IRREGULIERS : base -> (preterit, participe), et la
forme britannique en troisieme position quand elle differe. niveaux.py les
ajoute a ceux de l'A1 APRES avoir construit l'A1 : l'A1 ne bouge pas.
Les verbes composes (overcome, undertake, withdraw...) sont listes en entier :
la regle ne devine pas que « become » suit « come ».
"""

IRREGULIERS = {
    "fall": ("fell", "fallen"), "befall": ("befell", "befallen"),
    "arise": ("arose", "arisen"), "awake": ("awoke", "awoken"), "bear": ("bore", "borne"),
    "beat": ("beat", "beaten"), "bend": ("bent", "bent"), "bet": ("bet", "bet"), "bind": ("bound", "bound"),
    "bite": ("bit", "bitten"), "bleed": ("bled", "bled"), "blow": ("blew", "blown"),
    "breed": ("bred", "bred"), "broadcast": ("broadcast", "broadcast"),
    "burn": ("burned", "burned", ("burned / burnt", "burned / burnt")), "burst": ("burst", "burst"),
    "cast": ("cast", "cast"), "catch": ("caught", "caught"), "cling": ("clung", "clung"),
    "creep": ("crept", "crept"), "deal": ("dealt", "dealt"), "dig": ("dug", "dug"),
    "dive": ("dove", "dived", ("dived", "dived")), "feed": ("fed", "fed"), "fight": ("fought", "fought"),
    "flee": ("fled", "fled"), "fling": ("flung", "flung"), "forbid": ("forbade", "forbidden"),
    "forecast": ("forecast", "forecast"), "foresee": ("foresaw", "foreseen"), "forgive": ("forgave", "forgiven"),
    "freeze": ("froze", "frozen"), "grind": ("ground", "ground"), "hang": ("hung", "hung"),
    "hide": ("hid", "hidden"), "hit": ("hit", "hit"), "hold": ("held", "held"),
    "kneel": ("knelt", "knelt"), "lay": ("laid", "laid"), "lead": ("led", "led"),
    "lean": ("leaned", "leaned", ("leaned / leant", "leaned / leant")), "leap": ("leaped", "leaped", ("leapt", "leapt")),
    "lend": ("lent", "lent"), "lie": ("lay", "lain"), "light": ("lit", "lit"),
    "mislead": ("misled", "misled"), "mistake": ("mistook", "mistaken"), "misunderstand": ("misunderstood", "misunderstood"),
    "overcome": ("overcame", "overcome"), "overdo": ("overdid", "overdone"), "overhear": ("overheard", "overheard"),
    "oversee": ("oversaw", "overseen"), "oversleep": ("overslept", "overslept"), "overtake": ("overtook", "overtaken"),
    "overthrow": ("overthrew", "overthrown"), "prove": ("proved", "proven", ("proved", "proved")),
    "quit": ("quit", "quit"), "rebuild": ("rebuilt", "rebuilt"), "redo": ("redid", "redone"),
    "rethink": ("rethought", "rethought"), "rewrite": ("rewrote", "rewritten"), "rid": ("rid", "rid"),
    "ring": ("rang", "rung"), "rise": ("rose", "risen"), "saw": ("sawed", "sawed", ("sawed", "sawn")),
    "seek": ("sought", "sought"), "set": ("set", "set"), "sew": ("sewed", "sewn"), "shake": ("shook", "shaken"),
    "shed": ("shed", "shed"), "shine": ("shone", "shone"), "shoot": ("shot", "shot"), "show": ("showed", "shown"),
    "shrink": ("shrank", "shrunk"), "shut": ("shut", "shut"), "sink": ("sank", "sunk"), "slide": ("slid", "slid"),
    "smell": ("smelled", "smelled", ("smelled / smelt", "smelled / smelt")), "sow": ("sowed", "sown"),
    "speed": ("sped", "sped"), "spill": ("spilled", "spilled", ("spilled / spilt", "spilled / spilt")),
    "spin": ("spun", "spun"), "spit": ("spit", "spit", ("spat", "spat")), "split": ("split", "split"),
    "spoil": ("spoiled", "spoiled", ("spoiled / spoilt", "spoiled / spoilt")), "spread": ("spread", "spread"),
    "spring": ("sprang", "sprung"), "steal": ("stole", "stolen"), "stick": ("stuck", "stuck"),
    "sting": ("stung", "stung"), "stink": ("stank", "stunk"), "stride": ("strode", "stridden"),
    "strike": ("struck", "struck"), "strive": ("strove", "striven"), "swear": ("swore", "sworn"),
    "sweep": ("swept", "swept"), "swell": ("swelled", "swollen"), "swing": ("swung", "swung"),
    "tear": ("tore", "torn"), "throw": ("threw", "thrown"), "thrust": ("thrust", "thrust"),
    "tread": ("trod", "trodden"), "undergo": ("underwent", "undergone"), "underline": ("underlined", "underlined"),
    "undertake": ("undertook", "undertaken"), "undo": ("undid", "undone"), "unwind": ("unwound", "unwound"),
    "uphold": ("upheld", "upheld"), "upset": ("upset", "upset"), "weave": ("wove", "woven"),
    "weep": ("wept", "wept"), "wet": ("wet", "wet"), "wind": ("wound", "wound"),
    "withdraw": ("withdrew", "withdrawn"), "withhold": ("withheld", "withheld"), "withstand": ("withstood", "withstood"),
    "wring": ("wrung", "wrung"), "outdo": ("outdid", "outdone"), "outgrow": ("outgrew", "outgrown"),
    "override": ("overrode", "overridden"), "overrun": ("overran", "overrun"), "overlook": ("overlooked", "overlooked"),
    "foretell": ("foretold", "foretold"), "inlay": ("inlaid", "inlaid"), "input": ("input", "input"),
    "broadcast": ("broadcast", "broadcast"), "outrun": ("outran", "outrun"), "outsell": ("outsold", "outsold"),
    "outshine": ("outshone", "outshone"), "overpay": ("overpaid", "overpaid"), "overspend": ("overspent", "overspent"),
    "overeat": ("overate", "overeaten"), "overfeed": ("overfed", "overfed"), "partake": ("partook", "partaken"),
    "proofread": ("proofread", "proofread"), "repay": ("repaid", "repaid"), "resell": ("resold", "resold"),
    "retell": ("retold", "retold"), "sublet": ("sublet", "sublet"), "upbring": ("upbrought", "upbrought"),
    "forsake": ("forsook", "forsaken"), "behold": ("beheld", "beheld"), "beset": ("beset", "beset"),
    "slay": ("slew", "slain"), "sling": ("slung", "slung"), "slit": ("slit", "slit"), "stave": ("staved", "staved"),
    "string": ("strung", "strung"), "dwell": ("dwelled", "dwelled", ("dwelt", "dwelt")),
    "kneel": ("knelt", "knelt"), "knit": ("knitted", "knitted"), "plead": ("pleaded", "pleaded"),
    "fit": ("fit", "fit", ("fitted", "fitted")), "forget": ("forgot", "forgotten"), "mean": ("meant", "meant"),
    "sell": ("sold", "sold"), "outweigh": ("outweighed", "outweighed"),
}

# Le -ing et le passe qui doublent la consonne finale, au-dela de l'A1.
DOUBLENT = {"admit", "commit", "omit", "permit", "submit", "transmit", "emit", "refer", "prefer", "confer",
            "defer", "infer", "transfer", "occur", "recur", "incur", "deter", "regret", "forget", "upset",
            "control", "patrol", "compel", "expel", "propel", "rebel", "repel", "excel", "equip", "ship",
            "drop", "grab", "rub", "scrub", "nod", "plug", "beg", "hug", "jog", "wrap", "trip", "slip", "step",
            "skip", "chop", "clap", "flip", "tap", "zip", "dip", "rob", "ban", "scan", "plan", "stir", "slam",
            "trim", "spin", "grin", "dig", "bet", "fit", "hit", "quit", "set", "split", "spit", "knit", "shut",
            "abet", "regret", "dim", "hum", "jam", "ram", "swap", "tip", "whip", "strip", "drag", "tag", "pat",
            "pet", "rot", "spot", "plot", "knot", "dot", "chat", "star", "scar", "bar", "mar", "jar", "omit",
            "wed", "pin", "sin", "win", "ship", "sip", "sob", "throb", "stab", "jab", "dab", "nab", "fan",
            "can", "span", "bag", "lag", "nag", "wag", "brag", "flag", "snag", "shrug", "tug", "mug", "dub",
            "hop", "mop", "pop", "shop", "top", "prop", "crop", "stop", "map", "nap", "rap", "snap", "strap",
            "trap", "sap", "cap", "lap", "trot", "blot", "jot", "slot", "trek", "wet", "net", "fret", "vet",
            "jet", "let", "get", "run", "sun", "stun", "gun", "shun", "begin", "skim", "swim", "slim", "rig",
            "forbid", "rid", "bid", "sit", "put", "cut", "hit", "outrun", "overrun", "upset", "beset", "sublet"}
# Seul le britannique double le l final apres une voyelle breve inaccentuee.
DOUBLENT_GB = {"travel", "cancel", "label", "model", "signal", "fuel", "quarrel", "level", "total", "equal",
               "marvel", "channel", "counsel", "dial", "duel", "funnel", "jewel", "libel", "panel", "pedal",
               "shovel", "tunnel", "worship", "kidnap"}
