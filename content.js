// content.js - Intercepter les formulaires de connexion

document.addEventListener('submit', function(event) {
    const form = event.target;

    // Vérifier si le formulaire a des champs de nom d'utilisateur et mot de passe
    if (form.querySelector('[name="username"]') && form.querySelector('[name="password"]')) {
        const username = form.querySelector('[name="username"]').value;
        const password = form.querySelector('[name="password"]').value;
        const site = window.location.hostname;  // Récupérer le nom du site

        // Enregistrer les informations de connexion dans localStorage (à adapter pour plus de sécurité)
        const credentials = {
            site: site,
            username: username,
            password: password
        };

        // Utiliser Chrome Storage pour stocker les informations dans un espace sécurisé
        chrome.storage.local.get({passwords: []}, function(data) {
            let passwords = data.passwords;
            passwords.push(credentials);
            chrome.storage.local.set({passwords: passwords});
        });

        console.log(`Informations enregistrées pour ${site}: ${username}, ${password}`);
    }
}, true);
