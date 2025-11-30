import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from chainage import forward_chaining, backward_chaining
from base_de_régles import rules


def run_diagnosis():
    selected_symptoms = [symptom for symptom, var in check_vars.items() if var.get()]
    if not selected_symptoms:
        messagebox.showwarning("Attention", "Veuillez sélectionner au moins un symptôme !")
        return
    
    facts = set(selected_symptoms)
    
    if chainage_var.get() == "avant":
        # Chaînage avant
        inferred_rules = forward_chaining(facts, rules)
        result_text = "=== Chaînage avant ===\n"
        if inferred_rules:
            for rule in inferred_rules:
                result_text += f"- {rule['conclusion']} (à partir de : {', '.join(rule['conditions'])})\n"
        else:
            result_text += "Aucun diagnostic ne peut être déduit avec les symptômes sélectionnés."
        result_text += "\nFaits finaux : " + ", ".join(facts)
        
    else:
        # Chaînage arrière
        goal = backward_combo.get()
        if not goal:
            messagebox.showwarning("Attention", "Veuillez sélectionner un diagnostic à vérifier !")
            return
        found= backward_chaining(goal, facts, rules)
        result_text = "=== Chaînage arrière ===\n"
        if found:
            result_text += f"Diagnostic confirmé : {goal}"
        else:
            result_text += f"Impossible de confirmer le diagnostic : {goal}"
        result_text += "\nFaits utilisés : " + ", ".join(facts)
    
    # Afficher le résultat
    result_box.config(state='normal')
    result_box.delete('1.0', tk.END)
    result_box.insert(tk.END, result_text)
    result_box.config(state='disabled')

def reset_all():
    for var in check_vars.values():
        var.set(False)
    backward_combo.set("")
    chainage_var.set("avant")
    result_box.config(state='normal')
    result_box.delete('1.0', tk.END)
    result_box.config(state='disabled')

def update_ui(*args):
    if chainage_var.get() == "avant":
        backward_combo.config(state="disabled")
    else:
        backward_combo.config(state="readonly")

# -------------------------
# Interface graphique
# -------------------------
root = tk.Tk()
root.title("Système Expert : Détection de pannes de véhicules")
root.geometry("900x750")
root.configure(bg="#e6f2ff")

# Titre
tk.Label(root, text="Système Expert : Détection de pannes de véhicules",
         font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=15)

# Cadre choix chaînage
chainage_frame = tk.LabelFrame(root, text="Type de chaînage", font=("Helvetica", 14, "bold"),
                               padx=15, pady=10, bg="#e6f2ff", fg="#003366")
chainage_frame.pack(padx=20, pady=10, fill="x")

chainage_var = tk.StringVar(value="avant")
tk.Radiobutton(chainage_frame, text="Chaînage avant", variable=chainage_var, value="avant",
               font=("Helvetica", 12), bg="#e6f2ff", command=update_ui).pack(side="left", padx=20)
tk.Radiobutton(chainage_frame, text="Chaînage arrière", variable=chainage_var, value="arriere",
               font=("Helvetica", 12), bg="#e6f2ff", command=update_ui).pack(side="left", padx=20)

# Cadre symptômes
symptoms_frame = tk.LabelFrame(root, text="Sélectionnez les symptômes observés",
                               font=("Helvetica", 14, "bold"), padx=15, pady=10, bg="#e6f2ff", fg="#003366")
symptoms_frame.pack(padx=20, pady=10, fill="x")

symptoms_list = [
    "moteur ne démarre pas",
    "moteur cale",
    "ralenti irrégulier",
    "voyant moteur allumé",
    "fumée noire",
    "fumée bleue",
    "fuite d’huile",
    "freins mous",
    "bruit lors du freinage"
]

check_vars = {}
for symptom in symptoms_list:
    var = tk.BooleanVar()
    tk.Checkbutton(symptoms_frame, text=symptom, variable=var, font=("Helvetica", 12), bg="#e6f2ff").pack(anchor="w", padx=10)
    check_vars[symptom] = var

# Cadre chaînage arrière
backward_frame = tk.LabelFrame(root, text="Chaînage arrière : Vérifier un diagnostic",
                               font=("Helvetica", 14, "bold"), padx=15, pady=10, bg="#e6f2ff", fg="#003366")
backward_frame.pack(padx=20, pady=10, fill="x")

diagnostics_list = [rule["conclusion"] for rule in rules]
backward_combo = ttk.Combobox(backward_frame, values=diagnostics_list,
                              font=("Helvetica", 12), state="disabled", width=50)
backward_combo.pack(side="left", padx=10, pady=5)

# Boutons
buttons_frame = tk.Frame(root, bg="#e6f2ff")
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Lancer le diagnostic", command=run_diagnosis,
          font=("Helvetica", 12), bg="#4CAF50", fg="white", width=20).grid(row=0, column=0, padx=10)
tk.Button(buttons_frame, text="Réinitialiser", command=reset_all,
          font=("Helvetica", 12), bg="#f44336", fg="white", width=20).grid(row=0, column=1, padx=10)

# Zone de résultats scrollable
result_frame = tk.LabelFrame(root, text="Résultats", font=("Helvetica", 14, "bold"),
                             padx=15, pady=10, bg="#e6f2ff", fg="#003366")
result_frame.pack(padx=20, pady=10, fill="both", expand=True)

result_box = scrolledtext.ScrolledText(result_frame, font=("Helvetica", 12),
                                       state='disabled', wrap=tk.WORD, bg="#f2faff")
result_box.pack(fill="both", expand=True)

root.mainloop()
