
# Base de règles (conditions → diagnostic)
rules = [
    {"conditions": ["moteur ne démarre pas"], "conclusion": "batterie déchargée"},
    {"conditions": ["moteur cale", "ralenti irrégulier"], "conclusion": "allumage défectueux"},
    {"conditions": ["voyant moteur allumé"], "conclusion": "capteur défectueux"},
    {"conditions": ["fumée noire"], "conclusion": "injection carburant"},
    {"conditions": ["fumée bleue"], "conclusion": "joint de culasse"},
    {"conditions": ["fuite d’huile"], "conclusion": "fuite moteur"},
    {"conditions": ["freins mous", "bruit lors du freinage"], "conclusion": "freins usés"},
    {"conditions": ["batterie déchargée", "moteur cale"], "conclusion": "démarrage complexe"},
    {"conditions": ["allumage défectueux", "injection carburant"], "conclusion": "moteur instable"},
    {"conditions": ["joint de culasse", "fumée noire"], "conclusion": "moteur endommagé"},
    {"conditions": ["capteur défectueux", "voyant moteur allumé"], "conclusion": "diagnostic électronique"},
    {"conditions": ["moteur instable", "moteur endommagé"], "conclusion": "panne critique"},
    {"conditions": ["démarrage complexe", "moteur instable"], "conclusion": "intervention urgente"},
    {"conditions": ["fuite moteur", "moteur endommagé"], "conclusion": "intervention mécanique"},
    {"conditions": ["freins usés", "moteur instable"], "conclusion": "intervention sécurité"}
]
