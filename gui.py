import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import requests

def load_passwords():
    """Charge la liste des mots de passe depuis le serveur Flask"""
    try:
        response = requests.get('http://localhost:5000/get_passwords')
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erreur", f"Impossible de connecter au serveur: {e}")
    return []

def save_password(site, username, password):
    """Envoie un nouveau mot de passe au serveur Flask"""
    try:
        response = requests.post('http://localhost:5000/save_password', 
                                json={
                                    'site': site,
                                    'username': username,
                                    'password': password
                                })
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erreur", f"Impossible de connecter au serveur: {e}")
        return False

def show_passwords(main_frame):
    """Affiche tous les mots de passe enregistrés"""
    # Effacer le contenu actuel
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    # Récupérer les mots de passe
    passwords = load_passwords()
    
    if not passwords:
        tk.Label(main_frame, text="Aucun mot de passe enregistré.").pack(pady=10)
        return
    
    # Créer un cadre défilant
    canvas = tk.Canvas(main_frame)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Afficher chaque mot de passe
    for i, entry in enumerate(passwords):
        frame = tk.Frame(scrollable_frame, bd=1, relief=tk.SOLID)
        frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(frame, text=f"Site: {entry['site']}").pack(anchor="w", padx=5)
        tk.Label(frame, text=f"Utilisateur: {entry['username']}").pack(anchor="w", padx=5)
        
        # Affichage du mot de passe caché
        password_var = tk.StringVar()
        password_var.set("Mot de passe: " + "•" * 8)
        password_label = tk.Label(frame, textvariable=password_var)
        password_label.pack(anchor="w", padx=5)
        
        button_frame = tk.Frame(frame)
        button_frame.pack(fill="x", pady=5)
        
        # Bouton pour afficher/masquer le mot de passe
        def toggle_password(entry=entry, password_var=password_var):
            if "•" in password_var.get():
                password_var.set(f"Mot de passe: {entry['password']}")
            else:
                password_var.set("Mot de passe: " + "•" * 8)
        
        tk.Button(button_frame, text="Afficher/Masquer", command=toggle_password).pack(side="left", padx=5)
        
        # Bouton pour supprimer l'entrée
        def delete_entry(site=entry['site'], username=entry['username']):
            if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cet identifiant ?"):
                # Récupérer les mots de passe actuels
                current_passwords = load_passwords()
                # Filtrer pour enlever l'identifiant
                new_passwords = [p for p in current_passwords 
                                if not (p['site'] == site and p['username'] == username)]
                
                # Enregistrer directement le fichier JSON
                try:
                    with open('passwords.json', 'w') as f:
                        json.dump(new_passwords, f, indent=4)
                    show_passwords(main_frame)  # Rafraîchir l'affichage
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible de supprimer l'identifiant: {e}")
        
        tk.Button(button_frame, text="Supprimer", command=delete_entry).pack(side="left", padx=5)

def add_password_window(main_frame):
    """Ouvre une fenêtre pour ajouter un nouveau mot de passe"""
    add_window = tk.Toplevel()
    add_window.title("Ajouter un mot de passe")
    add_window.geometry("300x200")
    
    tk.Label(add_window, text="Site:").pack(anchor="w", padx=10, pady=5)
    site_entry = tk.Entry(add_window, width=30)
    site_entry.pack(padx=10)
    
    tk.Label(add_window, text="Nom d'utilisateur:").pack(anchor="w", padx=10, pady=5)
    username_entry = tk.Entry(add_window, width=30)
    username_entry.pack(padx=10)
    
    tk.Label(add_window, text="Mot de passe:").pack(anchor="w", padx=10, pady=5)
    password_entry = tk.Entry(add_window, width=30, show="•")
    password_entry.pack(padx=10)
    
    def confirm():
        site = site_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        
        if not site or not username or not password:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
            return
        
        if save_password(site, username, password):
            messagebox.showinfo("Succès", "Mot de passe ajouté avec succès.")
            add_window.destroy()
            show_passwords(main_frame)  # Rafraîchir l'affichage
    
    tk.Button(add_window, text="Ajouter", command=confirm, bg="#357ab7", fg="white").pack(pady=15)

def main():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Gestionnaire de mots de passe")
    root.geometry("600x500")
    
    # Barre de menu supérieure
    menu_frame = tk.Frame(root, bg="#357ab7")
    menu_frame.pack(fill="x")
    
    tk.Label(menu_frame, text="Gestionnaire de mots de passe", font=("Arial", 16), 
             bg="#357ab7", fg="white").pack(side="left", padx=20, pady=10)
    
    # Cadre principal pour le contenu
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Barre de boutons
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(fill="x", side="bottom")
    
    tk.Button(button_frame, text="Ajouter un mot de passe", 
              command=lambda: add_password_window(main_frame),
              bg="#357ab7", fg="white").pack(side="left", padx=20, pady=10)
    
    tk.Button(button_frame, text="Actualiser", 
              command=lambda: show_passwords(main_frame),
              bg="#357ab7", fg="white").pack(side="left", padx=20, pady=10)
    
    # Afficher les mots de passe au démarrage
    show_passwords(main_frame)
    
    root.mainloop()

if __name__ == "__main__":
    main()
