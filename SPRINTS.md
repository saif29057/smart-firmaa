# Plan SCRUM Smart Firma

## Rôles

| Rôle | Responsabilité |
|---|---|
| Product Owner | Priorisation des besoins agricoles |
| Scrum Master | Suivi de la démarche et blocages |
| Développeur frontend | Pages React, composants, services Axios |
| Développeur backend | APIs Django, modèles, serializers, permissions |
| Data/ML engineer | Datasets, Random Forest, CNN, déploiement ML |
| Utilisateur final | Validation métier |

## Product Backlog

| ID | User Story | Priorité | Sprint |
|---|---|---|---|
| US1 | En tant que visiteur, je veux créer un compte. | Haute | S1 |
| US2 | En tant qu'utilisateur, je veux me connecter. | Haute | S1 |
| US3 | En tant qu'utilisateur, je veux consulter mon dashboard. | Haute | S1 |
| US4 | En tant qu'utilisateur, je veux consulter la météo. | Haute | S2 |
| US5 | En tant qu'utilisateur, je veux consulter des actualités. | Moyenne | S2 |
| US6 | En tant qu'agriculteur, je veux recommander une culture. | Très haute | S2 |
| US7 | En tant qu'agriculteur, je veux personnaliser les valeurs NPK/pH. | Haute | S3 |
| US8 | En tant qu'utilisateur, je veux analyser une image de plante. | Très haute | S3 |
| US9 | En tant qu'utilisateur, je veux recevoir des recommandations de traitement. | Très haute | S3 |
| US10 | En tant qu'utilisateur, je veux discuter avec un chatbot agricole. | Moyenne | S4 |
| US11 | En tant qu'utilisateur, je veux échanger des messages. | Moyenne | S4 |
| US12 | En tant qu'administrateur, je veux consulter un dashboard admin. | Moyenne | S4 |

## Sprint 1 : socle applicatif

Objectif : créer la base technique du projet.

Livrables :

- Django project `smartfirma`
- React app
- `authentication`
- routes frontend
- dashboard utilisateur/admin

APIs :

- `/api/auth/register/`
- `/api/auth/login/`
- `/api/auth/logout/`
- `/api/auth/profile/`
- `/api/auth/users/`

## Sprint 2 : services agricoles

Objectif : intégrer météo, actualités et première recommandation.

Livrables :

- page météo
- service météo
- service news
- module `crops`
- composant `RecommendationForm`

APIs :

- `/api/weather/current/`
- `/api/weather/forecast/`
- `/api/news/`
- `/api/news/categories/`
- `/crops/predict_crop/`
- `/crops/locations/`

## Sprint 3 : IA et diagnostic

Objectif : intégrer ML/DL.

Livrables :

- modèle `crop_model_tunisia.pkl`
- modèle `plant_disease_cnn.h5`
- page `Analysis`
- recommandations agronomiques
- historique d'analyse

APIs :

- `/api/analysis/upload/`
- `/api/analysis/history/`
- `/api/analysis/<id>/`

## Sprint 4 : communication et consolidation

Objectif : finaliser l'expérience utilisateur.

Livrables :

- chatbot agricole
- messagerie interne
- dashboard admin
- documentation technique

APIs :

- `/api/chatbot/chat/`
- `/api/chatbot/history/`
- `/api/chatbot/clear/`
- `/api/messaging/inbox/`
- `/api/messaging/sent/`
- `/api/messaging/send/`
- `/api/messaging/unread/count/`

