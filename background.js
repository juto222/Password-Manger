// background.js - Manipuler les données en arrière-plan

chrome.runtime.onInstalled.addListener(function() {
    console.log('Extension de gestion de mots de passe installée');
});

// Récupérer les mots de passe stockés
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'getPasswords') {
        chrome.storage.local.get('passwords', function(data) {
            sendResponse({passwords: data.passwords});
        });
        return true;  // Indiquer que la réponse est asynchrone
    }
});
