import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

main = tk.Tk()
main.title("Password Manager")
main.geometry("1000x900")
main.config(bg="#357ab7")

def ajt():
    ajouter = Toplevel(main)
    ajouter.geometry("400x400")
    ajouter.title("Créer un compte")
    ajouter.config(bg="#357ab7")

    label = tk.Label(ajouter, bg="#357ab7", text="Formulaire de création de compte", font=("Arial", 14))
    label.pack(pady=20)

    # Site
    site = tk.Label(ajouter, bg="#357ab7", text="Site : ")
    site.pack(pady=10)
    site_entry = tk.Entry(ajouter)
    site_entry.pack(pady=10)

    # User
    username = tk.Label(ajouter, bg="#357ab7", text="Nom d'utilisateur ou email:")
    username.pack()
    username_entry = tk.Entry(ajouter)
    username_entry.pack(pady=10)

    # Mdp
    password = tk.Label(ajouter,bg="#357ab7", text="Mot de passe:")
    password.pack()
    password_entry = tk.Entry(ajouter, show="*")
    password_entry.pack(pady=10)

    def confirmer():

        if not password_entry or not username_entry or not site_entry:
            messagebox.showwarning("Vous n'avez pas rempli tout les champs")
        else: 
            user = username_entry.get()
            sitee = site_entry.get()
            mdp = password_entry.get()
            ajouter.destroy()

    # Bouton pour soumettre
    submit_button = tk.Button(ajouter, bg="#357ab7", text="Créer", command=confirmer)
    submit_button.pack(pady=10)




sidebar = tk.Frame(main, bg="darkblue", width=200, height=900) 
sidebar.pack(side="left", fill="y")

# Contenu principal
main_content = tk.Frame(main, bg="#357ab7", width=800, height=900) 
main_content.pack(side="right", fill="both", expand=True)

# Bouton sidebar
create = tk.Button(sidebar, text="Créer un compte", command=ajt)
create.pack(pady=10) 

# Lancement de l'interface
main.mainloop()
