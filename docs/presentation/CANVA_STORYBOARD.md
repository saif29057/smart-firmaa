# Storyboard Canva - Soutenance Smart Firma

Ce document contient une présentation prête à recréer dans Canva. Format recommandé : 16:9.

## Slide 1 - Page de garde

**Titre :** Smart Firma, une plateforme intelligente pour l'aide à la décision agricole  
**Sous-titre :** Backend Django REST, frontend React/TypeScript, Random Forest et CNN  
**Éléments visuels :** fond agricole, palette vert/brun/or, mention PFE 2025-2026.

## Slide 2 - Plan

1. Contexte et problématique  
2. Solution proposée  
3. Besoins fonctionnels et non fonctionnels  
4. Architecture et UML  
5. Réalisation par sprints  
6. Machine Learning / Deep Learning  
7. Sécurité, limites et perspectives  
8. Conclusion

## Slide 3 - Contexte

**Message clé :** L'agriculture tunisienne nécessite des outils numériques capables de centraliser les décisions techniques.

- Variabilité climatique.
- Stress hydrique.
- Risques phytosanitaires.
- Informations dispersées entre météo, diagnostic et conseil.

## Slide 4 - Problématique

**Question centrale :**  
Comment concevoir une plateforme web intelligente capable d'assister un agriculteur tunisien dans le diagnostic des maladies, la recommandation des cultures et l'accès aux services agricoles numériques fiables ?

## Slide 5 - Solution proposée

**Message clé :** Smart Firma regroupe les services agricoles essentiels dans une architecture web modulaire.

Flux :

Utilisateur → Interface React → API Django REST → Données, services externes et modèles IA

Modules :

- Météo agricole
- Recommandation culture
- Diagnostic image
- Chatbot agricole
- Messagerie
- Dashboard

## Slide 6 - Besoins fonctionnels

| Domaine | Besoins |
|---|---|
| Authentification | inscription, connexion, profil, rôle |
| Agriculture | météo, recommandation, diagnostic, conseils |
| Communication | messagerie, chatbot |
| Administration | dashboard admin, utilisateurs |

## Slide 7 - Besoins non fonctionnels

- Sécurité : TokenAuthentication, permissions, validation.
- Performance : chargement paresseux du CNN, cache LRU.
- Maintenabilité : apps Django séparées, services Axios.
- Traçabilité : AnalysisLog, ChatMessage.

## Slide 8 - Architecture globale

Créer un schéma à 3 colonnes :

1. Frontend React
   - Pages
   - Services Axios
   - AuthContext

2. Backend Django REST
   - authentication
   - weather
   - news
   - crops
   - analysis
   - chatbot
   - messaging

3. Données et services
   - SQLite
   - fichiers media
   - modèles PKL/H5
   - Open-Meteo, NewsAPI, OpenAI

## Slide 9 - Cas d'utilisation

Acteurs :

- Visiteur : s'inscrire, se connecter.
- Utilisateur : météo, recommandation, analyse image, chatbot, messages.
- Administrateur : dashboard admin, liste utilisateurs, supervision.

## Slide 10 - Base de données

Entités :

- User
- Message
- AnalysisLog
- ChatMessage

Relations :

- User 1..N Message envoyé
- User 1..N Message reçu
- User 1..N AnalysisLog
- User 1..N ChatMessage

## Slide 11 - SCRUM

| Sprint | Objectif | Livrables |
|---|---|---|
| S1 | Socle applicatif | Django, React, Auth, Dashboards |
| S2 | Services agricoles | Météo, News, Recommandation |
| S3 | IA et diagnostic | Random Forest, CNN, Upload image |
| S4 | Consolidation | Chatbot, Messagerie, Documentation |

## Slide 12 - Réalisation frontend

Interfaces :

- Home
- Login/Register
- Dashboard utilisateur
- Dashboard admin
- Weather
- RecommendationPage
- Analysis
- Chatbot

## Slide 13 - Réalisation backend

Applications Django :

- authentication
- messaging
- weather
- news
- analysis
- chatbot
- crops

Endpoints clés :

- `/api/auth/login/`
- `/api/analysis/upload/`
- `/api/chatbot/chat/`
- `/crops/predict_crop/`

## Slide 14 - Machine Learning / CRISP-DM

Phases appliquées :

- Business understanding : aider le choix de culture.
- Data understanding : NPK, météo, pH, rainfall.
- Data preparation : séparation features/label.
- Modeling : Random Forest.
- Evaluation : cross-validation et holdout accuracy.
- Deployment : API `/crops/predict_crop/`.

## Slide 15 - Deep Learning

Pipeline :

Image plante → validation → resize 224x224 RGB → normalisation → CNN Keras → top-3 prédictions → recommandations

Architecture :

- Conv2D 32/64/128
- MaxPooling
- Dense 128
- Dropout 0.5
- Softmax 38 classes

## Slide 16 - Résultats

| Modèle | Résultat |
|---|---:|
| Random Forest général | 99.55 % holdout |
| Random Forest Tunisie | 95.61 % holdout |
| Cross-validation Tunisie | 94.44 % moyenne |

Autres résultats :

- APIs REST fonctionnelles.
- Interfaces spécialisées.
- Historique des analyses.
- Chatbot agricole intégré.

## Slide 17 - Sécurité et limites

Sécurité :

- TokenAuthentication.
- IsAuthenticated / IsAdminUser.
- Validation image.
- CORS configuré.

Limites :

- Pas de Docker.
- Pas de CI/CD.
- SQLite en développement.
- Pas de JWT/OAuth.
- Tests à renforcer.
- Dataset tunisien synthétique.

## Slide 18 - Conclusion

**Message clé :** Smart Firma démontre comment une architecture web moderne peut intégrer l'IA pour améliorer la décision agricole.

Résultats :

- Plateforme modulaire.
- ML/DL intégrés.
- Services agricoles centralisés.

Perspectives :

- PostgreSQL.
- Docker et CI/CD.
- Données terrain.
- Transfert learning.
- Monitoring.

