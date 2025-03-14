# Serveur Flask (app.py)
from flask import Flask, request, jsonify
import json
from flask_cors import CORS  # Pour permettre les requêtes cross-origin

app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Chargement des mots de passe existants
def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Sauvegarde des mots de passe
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

@app.route('/save_password', methods=['POST'])
def save_password():
    data = request.get_json()
    site = data.get('site')
    username = data.get('username')
    password = data.get('password')

    if not site or not username or not password:
        return jsonify({'error': 'Données manquantes'}), 400

    # Charger les mots de passe existants
    passwords = load_passwords()

    # Vérifier si cet identifiant existe déjà
    for existing in passwords:
        if existing['site'] == site and existing['username'] == username:
            existing['password'] = password  # Mettre à jour le mot de passe existant
            save_passwords(passwords)
            return jsonify({'message': 'Mot de passe mis à jour avec succès'})

    # Ajouter le nouveau mot de passe
    passwords.append({
        'site': site,
        'username': username,
        'password': password
    })

    # Sauvegarder les mots de passe
    save_passwords(passwords)

    return jsonify({'message': 'Mot de passe enregistré avec succès'})

@app.route('/get_passwords', methods=['GET'])
def get_passwords():
    passwords = load_passwords()
    return jsonify(passwords)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)