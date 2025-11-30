
def forward_chaining(facts, rules):
    new_facts = True
    inferred = []
    while new_facts:
        new_facts = False
        for rule in rules:
            # Si toutes les conditions sont dans les faits et la conclusion n'est pas encore connue
            if all(cond in facts for cond in rule["conditions"]) and rule["conclusion"] not in facts:
                facts.add(rule["conclusion"])
                inferred.append(rule)
                new_facts = True
    return inferred

def backward_chaining(goal, facts, rules)->bool:
    for rule in rules:
        if rule["conclusion"] == goal:
            # Vérifier si toutes les conditions sont présentes dans les faits
            if all(cond in facts for cond in rule["conditions"]):
                return True
            else:
                # Tenter de prouver chaque condition manquante
                for cond in rule["conditions"]:
                    if cond not in facts:
                        found= backward_chaining(cond, facts, rules)
                        if not found:
                            return False
                return True
    return False
