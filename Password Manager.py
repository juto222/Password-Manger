import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import os

# Stockage des comptes
accounts = []
USERNAME = "a"
PASSWORD = "a"

# Charger les comptes depuis le fichier texte
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
                    accounts.append({"category": category, "site": site, "email": email, "password": password})

# Vérification des identifiants de login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Succès", "Connexion réussie !")
        unlock_manager()  # Débloque l'application principale
    else:
        messagebox.showerror("Erreur", "Identifiants incorrects.")

# Initialisation de l'application
root = tk.Tk()
root.title("Gestionnaire de Mots de Passe")
root.geometry("900x600")
root.config(bg="#1e1e2f")

load_accounts()

# Débloquer l'application après connexion
def unlock_manager():
    login_frame.pack_forget()  # Masquer l'écran de login
    sidebar.pack(side="left", fill="y")  # Afficher la barre latérale
    main_frame.pack(fill="both", expand=True)  # Afficher le contenu principal
    show_content("All")  # Charger les comptes

# Menu déroulant pour changer la langue dans la barre latérale
def toggle_language_menu():
    if language_menu.winfo_ismapped():  # Si le menu est déjà affiché, on le cache
        language_menu.pack_forget()
    else:  # Sinon, on l'affiche
        language_menu.pack(fill="x", pady=5)

# Barre latérale (masquée au départ)
sidebar = tk.Frame(root, bg="#2a2a40", width=200)

categories = ["All", "Bank Account", "Credit Card", "Computer Login", 
              "Entertainment", "Mail", "Secure Account", "Social Network", "Web Login"]
for category in categories:
    btn = tk.Button(sidebar, text=category, bg="#2a2a40", fg="white", relief="flat", anchor="w",
                    command=lambda cat=category: show_content(cat))
    btn.pack(fill="x", padx=10, pady=2)

# Ajout du bouton pour le menu déroulant de langue
lang_button = tk.Button(sidebar, text=" --> 🌐 Langue", bg="#2a2a40", fg="white", relief="flat", command=toggle_language_menu)
lang_button.pack(fill="x", padx=10, pady=10)

# Menu déroulant des langues
language_menu = tk.Frame(sidebar, bg="#2a2a40")
lang_fr = tk.Button(language_menu, text="Français", bg="#2a2a40", fg="white", relief="flat", command=lambda: switch_language("fr"))
lang_en = tk.Button(language_menu, text="English", bg="#2a2a40", fg="white", relief="flat", command=lambda: switch_language("en"))
lang_fr.pack(fill="x", pady=5)
lang_en.pack(fill="x", pady=5)

# Barre de navigation pour changer de langue
def switch_language(lang):
    if lang == "fr":
        messagebox.showinfo("Langue", "Langue changée en français.")
    elif lang == "en":
        messagebox.showinfo("Langue", "Language switched to English.")
    else:
        messagebox.showerror("Erreur", "Langue non reconnue.")


# Fonction pour afficher le contenu
def show_content(option):
    for widget in main_frame.winfo_children():
        widget.destroy()

    if language_menu == switch_language("fr"):
        tk.Label(main_frame, text=f"Comptes pour {option} :", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=10)
    else:
        tk.Label(main_frame, text=f"Account for {option} :", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=10)

    for index, account in enumerate(accounts):
        if option == "All" or account["category"] == option:
            frame = tk.Frame(main_frame, bg="#2a2a40", padx=10, pady=5)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=account["site"], bg="#2a2a40", fg="white", font=("Arial", 12, "bold")).pack(side="left")
            tk.Label(frame, text=account["email"], bg="#2a2a40", fg="white", font=("Arial", 10)).pack(side="left", padx=10)

            show_password_btn = tk.Button(frame, text="Afficher", bg="#444", fg="white", relief="flat",
                                          command=lambda idx=index: messagebox.showinfo("Mot de Passe", accounts[idx]["password"]))
            show_password_btn.pack(side="right", padx=5)


# Écran de login
login_frame = tk.Frame(root, bg="#1e1e2f")
login_frame.pack(fill="both", expand=True)

if language_menu == lang_fr:
    tk.Label(login_frame, text="Connexion", bg="#1e1e2f", fg="white", font=("Arial", 16, "bold")).pack(pady=20)
else:
    tk.Label(login_frame, text="Connexion", bg="#1e1e2f", fg="white", font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(login_frame, text="Nom d'utilisateur :", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=5)
username_entry = tk.Entry(login_frame, bg="#2a2a40", fg="white", relief="flat", width=30)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Mot de passe :", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(login_frame, bg="#2a2a40", fg="white", relief="flat", width=30, show="*")
password_entry.pack(pady=5)

tk.Button(login_frame, text="Se connecter", bg="#2a2a40", fg="white", command=login).pack(pady=20)


# Cadre principal (masqué au départ)
main_frame = tk.Frame(root, bg="#1e1e2f")



root.mainloop()
