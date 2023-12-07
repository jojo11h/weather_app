# Weather App

Cette application météo utilise l'API OpenWeatherMap pour récupérer les données météorologiques d'une ville spécifiée et les affiche sous forme de message texte, génère un rapport au format PDF et envoie également les informations météorologiques par SMS à un numéro de téléphone spécifié.

## Fichiers Python

1. content_message.py
Ce fichier contient deux fonctions :

readfile(file): Lit le contenu d'un fichier JSON spécifié et retourne les données.
make_message(data): Prend les données météorologiques en entrée et crée un message formaté avec des informations telles que la ville, la température, le ciel, et la vitesse du vent.
2. generate_pdf.py
Ce script utilise les fonctions du fichier content_message.py pour générer un rapport météo au format PDF. Il extrait les données du fichier JSON, crée un fichier PDF avec les informations météorologiques formatées et l'ouvre automatiquement.

3. send_sms.py
Ce script utilise l'API Twilio pour envoyer un SMS avec les informations météorologiques à un numéro de téléphone spécifié. Il utilise les fonctions du fichier content_message.py pour obtenir les données et formater le message.

# Configuration

Avant d'exécuter ces scripts, assurez-vous d'avoir configuré les éléments suivants :

>[!IMPORTANT]
> - **API OpenWeatherMap** : Obtenez une clé API de OpenWeatherMap et configurez-la dans le fichier WeatherApp du fichier send_sms.py.
> - **API Twilio** : Créez un compte Twilio, configurez les variables d'environnement ACCOUNT_SID, AUTH_TOKEN, AUTHOR_PHONE et DEST_PHONE dans le fichier send_sms.py.
> - **Fichier .env** : Créez un fichier .env et configurez les variables ACCOUNT_SID, AUTH_TOKEN, AUTHOR_PHONE, DEST_PHONE et WEATHER_APP_KEY.

# Utilisation

Exécutez generate_pdf.py pour générer un rapport météo au format PDF.

Exécutez send_sms.py pour envoyer les informations météorologiques par SMS.

Les fonctions de ces scripts peuvent être intégrées dans d'autres projets ou applications selon vos besoins.

Note : Assurez-vous d'installer les bibliothèques requises en utilisant

```bash
 pip install -r requirements.txt.

```
