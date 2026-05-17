# Captures d'écran à insérer dans le rapport

Place les captures au format PNG dans ce dossier avec les noms suivants :

| Fichier | Interface attendue |
|---|---|
| `01_accueil.png` | Page d'accueil Smart Firma |
| `02_login.png` | Page de connexion |
| `03_register.png` | Page d'inscription |
| `04_dashboard_utilisateur.png` | Tableau de bord utilisateur |
| `05_dashboard_admin.png` | Tableau de bord administrateur |
| `06_meteo.png` | Page météo agricole |
| `07_recommandation_formulaire.png` | Formulaire de recommandation |
| `08_recommandation_resultat.png` | Résultat de recommandation |
| `09_analyse_upload.png` | Upload d'image plante |
| `10_analyse_resultat.png` | Résultat diagnostic maladie |
| `11_chatbot.png` | Chatbot agricole |
| `12_messagerie.png` | Messagerie interne ou écran associé |

Le rapport compile même si les images sont absentes : un cadre de remplacement sera affiché automatiquement.

Pour créer les captures :

1. Lance le backend :
   ```powershell
   cd D:\smart_firma\backend
   python manage.py runserver
   ```
2. Lance le frontend :
   ```powershell
   cd D:\smart_firma\frontend
   npm start
   ```
3. Ouvre `http://localhost:3000`.
4. Fais les captures avec `Win + Shift + S`.
5. Enregistre chaque image dans `D:\smart_firma\docs\rapport\figures`.

