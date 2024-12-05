import tkinter as tk
from tkinter import messagebox
import os


# Données utilisateurs et comptes
accounts = []
USERNAME = "a"
PASSWORD = "a"


# Charger les comptes existants
def load_accounts():
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as f:
            for line in f:
                parts = line.strip().split(", ")
                if len(parts) == 4:
                    category = parts[0].split(": ")[1]
                    site = parts[1].split(": ")[1]
                    email = parts[2].split(": ")[1]
                    password = parts[3].split(": ")[1]
                    accounts.append({
                        "Catégorie": category,
                        "Site": site,
                        "Email": email,
                        "Password": password
                    })



def add_account():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="Ajouter un compte", bg="#2a2a40", fg="white", font=("Arial", 14)).pack(pady=10)

    selected_categories = tk.StringVar()

    dropdown = tk.OptionMenu(main_frame, selected_categories, *categories, command=add_account)
    dropdown.pack(pady=20)


    selected_categories.set(categories[0])

    tk.Label(main_frame, text="Site:", bg="#2a2a40", fg="white").pack(pady=5)
    site_entry = tk.Entry(main_frame, bg="#1e1e2f", fg="white", width=30)
    site_entry.pack(pady=5)

    tk.Label(main_frame, text="Email:", bg="#2a2a40", fg="white").pack(pady=5)
    email_entry = tk.Entry(main_frame, bg="#1e1e2f", fg="white", width=30)
    email_entry.pack(pady=5)

    tk.Label(main_frame, text="Mot de passe:", bg="#2a2a40", fg="white").pack(pady=5)
    password_entry = tk.Entry(main_frame, bg="#1e1e2f", fg="white", width=30, show="*")
    password_entry.pack(pady=5)

    # Ajouter un bouton pour valider l'ajout
    def save_new_account():
        category = selected_categories.get()
        site = site_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if not category or not site or not email or not password:
            messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")
            return

        # Sauvegarde dans la liste des comptes
        accounts.append({
            "Catégorie": category,
            "Site": site,
            "Email": email,
            "Password": password
        })

        # Sauvegarde dans le fichier
        with open("accounts.txt", "a") as f:
            f.write(f"Catégorie: {category}, Site: {site}, Email: {email}, Password: {password}\n")

        messagebox.showinfo("Succès", "Compte ajouté avec succès !")
        show_content("Tous les comptes")  # Retour à la liste des comptes

    tk.Button(main_frame, text="Ajouter", bg="#2a2a40", fg="white", command=save_new_account).pack(pady=10)

    # Bouton pour annuler et revenir à l'accueil
    tk.Button(main_frame, text="Annuler", bg="#2a2a40", fg="white",
              command=lambda: show_content("Accueil")).pack(pady=5)


# Fonction de connexion
def login():
    id = id_entry.get()
    mdp = mdp_entry.get()

    if id == USERNAME and mdp == PASSWORD:
        messagebox.showinfo("Connexion réussie", "Bienvenue dans le gestionnaire de mots de passe !")
        unlock_manager()
    else:
        messagebox.showerror("Erreur", "Identifiants de connexion incorrects.")


# Déverrouiller l'accès principal
def unlock_manager():
    login_frame.pack_forget()
    sidebar.pack(side="left", fill="y")
    main_frame.pack(fill="both", expand=True)
    show_content("Accueil")  # Afficher un contenu par défaut


# Afficher le contenu selon l'option
def show_content(option):
    for widget in main_frame.winfo_children():
        widget.destroy()

    if option == "Accueil":
        tk.Label(main_frame, text="Bienvenue dans le gestionnaire de mots de passe !",
                 bg="#2a2a40", fg="white", font=("Arial", 14)).pack(pady=20)
    elif option == "Tous les comptes":
        tk.Label(main_frame, text="Liste de tous les comptes enregistrés :", bg="#2a2a40", fg="white").pack(pady=10)
        for account in accounts:
            tk.Label(main_frame, text=f"{account['Catégorie']} - {account['Site']} - {account['Email']}",
                     bg="#2a2a40", fg="white").pack(anchor="w", padx=20)
    elif option == "Ajouter un compte":
        add_account()
    else:
        tk.Label(main_frame, text=f"Contenu pour {option}", bg="#2a2a40", fg="white").pack(pady=20)


# Interface utilisateur
root = tk.Tk()
root.title("Gestionnaire de Mots de Passe")
root.geometry("900x600")
root.config(bg="#1e1e2f")

load_accounts()

# Sidebar
sidebar = tk.Frame(root, bg="#1e1e2f", width=200)
tk.Label(sidebar, text="Menu", bg="#1e1e2f", fg="white", font=("Arial", 14, "bold")).pack(pady=10)
categories = ["Accueil", "Tous les comptes","Site Web", "Carte Bancaire","Jeux Vidéo", "Professionel","Temporaire","Ajouter un compte", "Paramètres"]
for category in categories:
    btn = tk.Button(sidebar, text=category, bg="#2a2a40", fg="white", relief="flat",
                    command=lambda cat=category: show_content(cat))
    btn.pack(fill="x", padx=10, pady=5)

# Écran de connexion
login_frame = tk.Frame(root, bg="#1e1e2f")
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Connexion", bg="#1e1e2f", fg="white", font=("Arial", 16, "bold")).pack(pady=20)
tk.Label(login_frame, text="Username:", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=5)
id_entry = tk.Entry(login_frame, bg="#2a2a40", fg="white", relief="flat", width=30)
id_entry.pack(pady=5)

tk.Label(login_frame, text="Password:", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=5)
mdp_entry = tk.Entry(login_frame, bg="#2a2a40", fg="white", relief="flat", width=30, show="•")
mdp_entry.pack(pady=5)

tk.Button(login_frame, text="Login", bg="#2a2a40", fg="white", command=login).pack(pady=20)

tk.Label(login_frame, text="Copyright Julien", bg="#2a2a40", fg="white").pack(side="bottom")

# Contenu principal
main_frame = tk.Frame(root, bg="#2a2a40")

root.mainloop()
