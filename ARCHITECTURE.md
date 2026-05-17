# Architecture Smart Firma

## Vue générale

```mermaid
flowchart LR
    subgraph Frontend["Frontend React / TypeScript"]
        Pages[Pages]
        Components[Components]
        Services[Services Axios]
        Context[AuthContext]
    end

    subgraph Backend["Backend Django REST"]
        Auth[authentication]
        Weather[weather]
        News[news]
        Analysis[analysis]
        Crops[crops]
        Chatbot[chatbot]
        Messaging[messaging]
    end

    subgraph Data["Données et modèles"]
        DB[(SQLite)]
        Media[(media/analysis_images)]
        PKL[(crop_model*.pkl)]
        H5[(plant_disease_cnn.h5)]
    end

    Pages --> Components
    Pages --> Services
    Context --> Services
    Services --> Auth
    Services --> Weather
    Services --> News
    Services --> Analysis
    Services --> Chatbot
    Services --> Messaging
    Pages --> Crops
    Auth --> DB
    Messaging --> DB
    Analysis --> DB
    Chatbot --> DB
    Analysis --> Media
    Analysis --> H5
    Crops --> PKL
```

## Backend

Le backend est un projet Django nommé `smartfirma`. Il expose une API JSON modulaire.

### Applications Django

| Application | Rôle |
|---|---|
| `authentication` | Utilisateur personnalisé, inscription, connexion, profil, liste admin |
| `messaging` | Messages reçus/envoyés, détail, suppression, compteur non lus |
| `weather` | Météo actuelle et prévisions via Open-Meteo/OpenWeatherMap |
| `news` | Actualités via NewsAPI |
| `analysis` | Upload image, CNN, historique d'analyse |
| `chatbot` | Chat OpenAI spécialisé agriculture tunisienne |
| `crops` | Recommandation culture par Random Forest |

## Frontend

Le frontend est une application React avec :

- `pages` : vues routées.
- `components` : composants partagés.
- `services` : appels API.
- `contexts` : gestion globale d'authentification.
- `styles` : CSS par domaine.

## Flux d'authentification

```mermaid
sequenceDiagram
    actor User
    participant React
    participant API as Django Auth API
    participant DB as SQLite

    User->>React: Saisit identifiants
    React->>API: POST /api/auth/login/
    API->>DB: authenticate(username, password)
    DB-->>API: User
    API-->>React: user + token
    React->>React: localStorage token/user
```

## Architecture ML

```mermaid
flowchart TD
    A[Localisation utilisateur] --> B[Geocodage Open-Meteo]
    B --> C[Meteo actuelle et pluie 3 jours]
    C --> D[Donnees sol locales]
    D --> E[Vecteur N P K temperature humidity ph rainfall]
    E --> F[Random Forest Tunisie]
    F --> G[Culture recommandee + alternatives]

    I[Image plante] --> J[Validation fichier]
    J --> K[Resize 224x224 RGB normalisation]
    K --> L[CNN Keras 38 classes]
    L --> M[Top 3 predictions + recommandations]
```

## DevOps

Aucun fichier Docker, pipeline CI/CD, Kubernetes ou monitoring n'a été détecté. L'exécution actuelle est locale :

```bash
cd backend
python manage.py runserver

cd frontend
npm start
```

