import tkinter as tk
from tkinter import messagebox
import os


accounts = []
USERNAME = "a"
PASSWORD = "a"


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
                    accounts.append({"Catégorie": category, "     Site": site, "     Email": email, "     Password": password})




def login():
    id = id_entry.get()
    mdp = mdp_entry.get()

    if id == USERNAME and mdp == PASSWORD:
        messagebox.showinfo("gg, bro")
        unlock_manager()
    else:
        messagebox.showerror("Identifiants de connexion faux")

def unlock_manager():
    login_frame.pack_forget() 
    main_frame.pack(fill="both", expand=True)  
    sidebar.pack(side="left", fill="y")


root = tk.Tk()
root.title("Gestionnaire de Mots de Passe")
root.geometry("900x600")
root.config(bg="#1e1e2f")

load_accounts()

sidebar = tk.Frame(root, bg="#1e1e2f", width=200)

cate_fr = ["Tous", "Compte Bancaire", "Mail", "Site Web", "Réseaux Sociaux"]
cate_en = ["All", "Account Bank", "Mail", "Web Site", "Social Media"]



login_frame = tk.Frame(root, bg="#1e1e2f")
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Connexion", bg="#1e1e2f", fg="white", font=("Arial", 16, "bold")).pack(pady=20)
tk.Label(login_frame, text="Username:", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=5)
id_entry = tk.Entry(login_frame, bg="#2a2a40", fg="white", relief="flat", width=30)
id_entry.pack(pady=5)

tk.Label(login_frame, text="Password :", bg="#1e1e2f", fg="white", font=("Arial", 12)).pack(pady=5)
mdp_entry = tk.Entry(login_frame, bg="#2a2a40", fg="white", relief="flat", width=30, show="•")
mdp_entry.pack(pady=5)

tk.Button(login_frame, text="Login", bg="#2a2a40", fg="white", command=login).pack(pady=20)

tk.Label(login_frame, text="Copyright Julien", bg="#2a2a40", fg="white").pack(side="bottom")



main_frame = tk.Frame(root, bg="#2a2a40")

root.mainloop()
