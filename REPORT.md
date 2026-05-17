# Rapport d'analyse du projet Smart Firma

## Synthèse

Smart Firma est une application web d'aide à la décision agricole orientée vers le contexte tunisien. Le projet est structuré en deux parties :

- `backend` : API Django REST Framework, base SQLite, modèles ML/DL et services externes.
- `frontend` : application React/TypeScript avec routes, pages, services Axios et contexte d'authentification.

Le projet contient deux modules IA :

- recommandation de cultures par Random Forest ;
- diagnostic de maladies végétales par CNN Keras.

## Technologies détectées

| Couche | Technologies |
|---|---|
| Frontend | React 19, TypeScript, React Router DOM, Axios, Lucide React, CSS |
| Backend | Python, Django 4.2.7, Django REST Framework, django-cors-headers |
| Authentification | DRF TokenAuthentication, SessionAuthentication, localStorage côté frontend |
| Base de données | SQLite |
| ML | Scikit-learn, RandomForestClassifier, Pandas, NumPy, Joblib |
| DL | TensorFlow 2.17, Keras, Pillow |
| APIs externes | Open-Meteo, OpenWeatherMap, NewsAPI, OpenAI API |

## Fonctionnalités détectées

- Inscription, connexion, déconnexion.
- Profil utilisateur.
- Dashboard utilisateur.
- Dashboard administrateur.
- Météo actuelle et prévisions.
- Actualités.
- Recommandation de cultures tunisiennes.
- Analyse d'image de plante.
- Recommandations agronomiques.
- Chatbot agricole.
- Messagerie interne.

## Machine Learning

Le dataset général `Crop_recommendation.csv` contient 2200 lignes et 22 classes. Le dataset tunisien `crop_recommendation_tunisia.csv` contient 1710 lignes et 11 cultures. Le modèle tunisien `crop_model_tunisia.pkl` est un Random Forest avec 200 arbres, profondeur maximale 15 et `min_samples_split=5`.

Métriques extraites :

| Modèle | CV moyenne | Ecart-type | Accuracy holdout |
|---|---:|---:|---:|
| `crop_model.pkl` | 0.9945 | 0.0034 | 0.9955 |
| `crop_model_tunisia.pkl` | 0.9444 | 0.0256 | 0.9561 |

Le modèle `plant_disease_cnn.h5` est un CNN Keras pour 38 classes, avec entrée 224x224x3, trois blocs Conv2D/MaxPooling, Dense 128, Dropout 0.5 et Dense softmax 38.

## Livrables générés

- `docs/rapport/main.tex`
- `docs/rapport/chapitre1.tex`
- `docs/rapport/chapitre2.tex`
- `docs/rapport/chapitre3.tex`
- `docs/rapport/conclusion.tex`
- `docs/rapport/annexes.tex`
- `docs/rapport/bibliographie.bib`
- `docs/rapport/diagrams/*.mmd`
- `ARCHITECTURE.md`
- `API_DOCUMENTATION.md`
- `SPRINTS.md`
- `UML_DESIGN.md`

## Limites observées

- Pas de Docker détecté.
- Pas de CI/CD détecté.
- Pas de Kubernetes ou monitoring détecté.
- SQLite utilisé en développement.
- Tests automatisés peu détaillés.
- Pas de rapport d'entraînement complet pour le CNN dans le workspace.
- Pas de JWT ni OAuth : le projet utilise DRF TokenAuthentication.

