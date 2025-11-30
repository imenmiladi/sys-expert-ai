from base_de_régles import rules
from chainage import forward_chaining, backward_chaining

# Saisie des symptômes
# exemple de saisie : moteur ne démarre pas, moteur cale, ralenti irrégulier
# resultat attendu pour chainage avant : batterie déchargée, allumage défectueux, démarrage complexe
# resultat attendu pour chainage arrière : si je veux verifier "démarrage complexe", il doit retourner True donc Diagnostic confirmé


user_input = input("Entrez les symptômes observés (séparés par une virgule) : ").lower().split(", ")
# Base de faits (initialement vide, remplie par l'utilisateur)
facts = set()
facts.update([symptom.strip() for symptom in user_input])

# Chaînage avant
forward_results = forward_chaining(facts, rules)
print("\n--- Diagnostics possibles (Forward Chaining) ---")
if forward_results:
    for rule in forward_results:
        print(f"- {rule['conclusion']}")
else:
    print("Aucun diagnostic trouvé.")

# Exemple de chaînage arrière pour tester un diagnostic particulier
goal = input("\nEntrez un diagnostic à vérifier (Backward Chaining) : ")
found= backward_chaining(goal, facts, rules)
if found:
    print(f"Diagnostic confirmé : {goal}")
else:
    print(f"Impossible de confirmer le diagnostic : {goal}")
