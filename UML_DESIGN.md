# UML Design Smart Firma

## Cas d'utilisation global

```mermaid
flowchart LR
    Visiteur((Visiteur))
    Utilisateur((Utilisateur authentifie))
    Admin((Administrateur))

    UC1[S'inscrire]
    UC2[Se connecter]
    UC3[Consulter tableau de bord]
    UC4[Consulter meteo]
    UC5[Recommander culture]
    UC6[Analyser image plante]
    UC7[Utiliser chatbot]
    UC8[Gerer messages]
    UC9[Consulter utilisateurs]

    Visiteur --> UC1
    Visiteur --> UC2
    Utilisateur --> UC3
    Utilisateur --> UC4
    Utilisateur --> UC5
    Utilisateur --> UC6
    Utilisateur --> UC7
    Utilisateur --> UC8
    Admin --> UC9
    Admin --> UC8
```

## Diagramme de classes

```mermaid
classDiagram
    class User {
      +int id
      +string username
      +string email
      +string first_name
      +string last_name
      +string role
      +string phone
      +image avatar
      +datetime created_at
      +datetime updated_at
    }

    class Message {
      +int id
      +User sender
      +User recipient
      +string subject
      +text content
      +boolean is_read
      +datetime created_at
      +datetime updated_at
    }

    class AnalysisLog {
      +int id
      +User user
      +image image
      +json result
      +float confidence
      +float processing_time
      +datetime created_at
    }

    class ChatMessage {
      +int id
      +User user
      +text message
      +text response
      +datetime created_at
    }

    User "1" --> "*" Message : sent_messages
    User "1" --> "*" Message : received_messages
    User "1" --> "*" AnalysisLog
    User "1" --> "*" ChatMessage
```

## Séquence : recommandation de culture

```mermaid
sequenceDiagram
    actor U as Utilisateur
    participant F as RecommendationForm
    participant C as Crops API
    participant M as Open-Meteo
    participant RF as RandomForest

    U->>F: Saisir localisation
    F->>C: GET /crops/predict_crop/
    C->>M: Geocodage + meteo
    M-->>C: temperature, humidite, pluie
    C->>C: Charger donnees sol
    C->>RF: predict(features)
    RF-->>C: culture + probabilites
    C-->>F: JSON recommandation
    F-->>U: Afficher culture et conseils
```

## Séquence : analyse de maladie

```mermaid
sequenceDiagram
    actor U as Utilisateur
    participant F as Analysis.tsx
    participant A as Analysis API
    participant CNN as CNN Keras
    participant DB as SQLite

    U->>F: Selection image
    F->>A: POST multipart image
    A->>A: Valider type et taille
    A->>DB: Creer AnalysisLog
    A->>A: Preprocess 224x224 RGB
    A->>CNN: predict()
    CNN-->>A: Top classes
    A->>DB: Sauvegarder resultats
    A-->>F: Diagnostic JSON
    F-->>U: Resultat + recommandations
```

## Activité : authentification

```mermaid
flowchart TD
    A[Debut] --> B[Saisie username/password]
    B --> C[POST /api/auth/login]
    C --> D{Identifiants valides ?}
    D -- Non --> E[Afficher erreur]
    D -- Oui --> F[Retour user + token]
    F --> G[Stocker localStorage]
    G --> H{Role admin ?}
    H -- Oui --> I[Dashboard admin]
    H -- Non --> J[Dashboard utilisateur]
```

## Composants

```mermaid
flowchart LR
    subgraph React
        Pages[Pages]
        Navbar[Navbar/Footer]
        AuthContext[AuthContext]
        Axios[Services Axios]
    end
    subgraph Django
        Auth[authentication]
        Weather[weather]
        News[news]
        Crops[crops]
        Analysis[analysis]
        Chatbot[chatbot]
        Messaging[messaging]
    end
    Pages --> Axios
    AuthContext --> Axios
    Axios --> Auth
    Axios --> Weather
    Axios --> News
    Axios --> Analysis
    Axios --> Chatbot
    Axios --> Messaging
    Pages --> Crops
```

