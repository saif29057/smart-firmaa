# Documentation API Smart Firma

Base backend : `http://localhost:8000`

Base API frontend configurée : `http://localhost:8000/api`

## Authentification

Le frontend ajoute automatiquement :

```http
Authorization: Token <token>
```

## Endpoints

### Auth

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/api/auth/register/` | POST | Non | Inscription |
| `/api/auth/login/` | POST | Non | Connexion |
| `/api/auth/logout/` | POST | Oui | Déconnexion |
| `/api/auth/profile/` | GET | Oui | Profil |
| `/api/auth/profile/update/` | PUT | Oui | Mise à jour profil |
| `/api/auth/users/` | GET | Admin | Liste utilisateurs |

Exemple login :

```json
{
  "username": "user",
  "password": "password"
}
```

Réponse :

```json
{
  "user": {
    "id": 1,
    "username": "user",
    "email": "user@example.com",
    "role": "user"
  },
  "token": "..."
}
```

### Weather

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/api/weather/current/?city=Tunis` | GET | Oui | Météo actuelle |
| `/api/weather/forecast/?city=Tunis&days=5` | GET | Oui | Prévisions |

### News

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/api/news/?category=general&country=fr&page_size=20` | GET | Oui | Actualités |
| `/api/news/categories/` | GET | Oui | Catégories |

### Analysis

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/api/analysis/upload/` | POST | Oui | Upload image et diagnostic |
| `/api/analysis/history/` | GET | Oui | Historique |
| `/api/analysis/<analysis_id>/` | GET | Oui | Détail |

Contraintes image :

- champ multipart : `image`
- type MIME : `image/*`
- taille maximale : 10 MB

Réponse simplifiée :

```json
{
  "id": 1,
  "result": {
    "predictions": [],
    "top_prediction": {},
    "recommendations": {},
    "summary": "..."
  },
  "confidence": 0.98,
  "processing_time": 1.2
}
```

### Crops

Base directe hors préfixe `/api` : `http://localhost:8000/crops`

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/crops/predict_crop/?location=Tunis` | GET | Non dans le code | Recommandation automatique |
| `/crops/predict_crop/?location=Tunis&mode=manual&N=70&P=30&K=50&ph=6.5&temp=25&humidity=60` | GET | Non dans le code | Recommandation manuelle |
| `/crops/locations/` | GET | Non dans le code | Villes disponibles |

### Chatbot

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/api/chatbot/chat/` | POST | Oui | Envoyer question |
| `/api/chatbot/history/` | GET | Oui | Historique |
| `/api/chatbot/clear/` | DELETE | Oui | Effacer historique |

### Messaging

| Endpoint | Méthode | Auth | Description |
|---|---|---|---|
| `/api/messaging/inbox/` | GET | Oui | Boîte de réception |
| `/api/messaging/sent/` | GET | Oui | Messages envoyés |
| `/api/messaging/send/` | POST | Oui | Envoyer message |
| `/api/messaging/<message_id>/` | GET | Oui | Détail |
| `/api/messaging/<message_id>/delete/` | DELETE | Oui | Suppression |
| `/api/messaging/unread/count/` | GET | Oui | Nombre non lus |

## Gestion d'erreurs

| Code | Cas |
|---|---|
| 400 | données invalides |
| 401 | non authentifié |
| 403 | accès non autorisé |
| 500 | erreur serveur |
| 503 | modèle ou météo indisponible |

