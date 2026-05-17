# Dashboard Admin Django Modernisé - Smart Firma

## Installation

### 1. Installer les nouvelles dépendances

```bash
cd backend
pip install django-admin-interface==0.27.0 django-colorfield==0.11.0
```

Ou utiliser le requirements.txt mis à jour:

```bash
pip install -r requirements.txt
```

### 2. Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Créer un superutilisateur (si pas déjà fait)

```bash
python manage.py createsuperuser
```

### 4. Lancer le serveur

```bash
python manage.py runserver
```

### 5. Accéder au dashboard admin

Ouvrez votre navigateur sur: `http://localhost:8000/admin/`

## Nouvelles fonctionnalités

### Interface moderne avec django-admin-interface

- **Thème bleu personnalisé**: Interface moderne avec palette de couleurs cohérente
- **Design responsive**: Adapté aux mobiles et tablettes
- **Améliorations UX**: Meilleure expérience utilisateur avec modals, tri, recherche

### Dashboard personnalisé avec statistiques

Le dashboard affiche en temps réel:
- **Utilisateurs**: Total et utilisateurs actifs
- **Analyses**: Total et analyses du jour
- **Messages**: Total et messages non lus
- **Chatbot**: Total et conversations du jour
- **Cultures**: Recommandations effectuées
- **Confiance moyenne**: Pourcentage de confiance des analyses IA

### Admin utilisateurs modernisé (authentication/admin.py)

- **list_display**: username, email, first_name, last_name, role, phone, is_active, created_at
- **list_filter**: role, is_active, is_staff, created_at
- **search_fields**: username, email, first_name, last_name, phone
- **fieldsets personnalisés**: Informations personnelles, Rôle et permissions, Avatar, Dates
- **date_hierarchy**: Navigation par date de création

### Admin analyses modernisé (analysis/admin.py)

- **Thumbnails images**: Aperçu des images dans la liste
- **Diagnostic affiché**: Plante et maladie détectée
- **Confiance en pourcentage**: Format lisible
- **Aperçu image grand**: Dans le détail de l'analyse
- **Permissions restreintes**: Pas d'ajout/modification (lecture seule)

### Admin messages modernisé (messaging/admin.py)

- **Badges de statut**: Lu (vert) / Non lu (rouge)
- **Preview sujet**: Sujet tronqué si trop long
- **Filtres avancés**: is_read, created_at, sender, recipient
- **Recherche**: subject, content, usernames

### Activité récente

Le dashboard affiche les 4 dernières activités:
- Dernière analyse effectuée
- Dernier utilisateur inscrit
- Dernier message envoyé
- Dernière conversation chatbot

## Configuration

### Personnalisation du thème (settings.py)

```python
# Django Admin Interface Configuration
ADMIN_INTERFACE_TITLE = 'Smart Firma Admin'
ADMIN_INTERFACE_NAME = 'Smart Firma'
ADMIN_INTERFACE_INDEX_TITLE = 'Tableau de bord'
ADMIN_INTERFACE_THEME_COLOR = '#2563eb'  # Bleu principal
ADMIN_INTERFACE_THEME_BACKGROUND_COLOR = '#f8fafc'
ADMIN_INTERFACE_THEME_HEADER_COLOR = '#1e40af'
ADMIN_INTERFACE_THEME_BUTTON_COLOR = '#3b82f6'
ADMIN_INTERFACE_THEME_BUTTON_OK_COLOR = '#22c55e'
ADMIN_INTERFACE_THEME_BUTTON_CANCEL_COLOR = '#ef4444'
```

### Modifier les couleurs

Pour changer le thème, modifiez les codes hexadécimaux dans `settings.py`:
- `THEME_COLOR`: Couleur principale
- `THEME_BACKGROUND_COLOR`: Couleur de fond
- `THEME_HEADER_COLOR`: Couleur de l'en-tête
- `THEME_BUTTON_COLOR`: Couleur des boutons
- `THEME_BUTTON_OK_COLOR`: Couleur bouton OK (vert)
- `THEME_BUTTON_CANCEL_COLOR`: Couleur bouton Annuler (rouge)

## Fichiers modifiés

1. **requirements.txt**: Ajout de django-admin-interface et django-colorfield
2. **smartfirma/settings.py**: Configuration de django-admin-interface et templates
3. **smartfirma/urls.py**: Utilisation de smartfirma_admin au lieu de admin.site
4. **smartfirma/admin.py**: Admin site personnalisé avec statistiques
5. **smartfirma/templates/admin/index.html**: Template dashboard personnalisé
6. **authentication/admin.py**: Admin User modernisé
7. **analysis/admin.py**: Admin AnalysisLog modernisé
8. **messaging/admin.py**: Admin Message modernisé

## Avantages

- **Interface moderne**: Design professionnel et cohérent
- **Statistiques en temps réel**: Vue d'ensemble de l'activité
- **UX améliorée**: Recherche, filtres, tri, thumbnails
- **Personnalisable**: Facile à adapter aux besoins
- **Responsive**: Fonctionne sur tous les appareils

## Dépannage

### Problème: Les statistiques ne s'affichent pas

Vérifiez que:
- Les modèles sont correctement enregistrés dans `smartfirma/admin.py`
- Les migrations sont appliquées
- L'admin personnalisé est utilisé dans `urls.py`

### Problème: Le thème ne s'applique pas

Vérifiez que:
- `admin_interface` et `colorfield` sont dans `INSTALLED_APPS`
- Les dépendances sont installées
- Les migrations sont appliquées

### Problème: Les images ne s'affichent pas

Vérifiez que:
- `MEDIA_URL` et `MEDIA_ROOT` sont correctement configurés
- Le serveur sert les fichiers media en mode DEBUG
- Les permissions sur le dossier media sont correctes

## Support

Pour toute question ou problème, consultez la documentation de django-admin-interface:
https://django-admin-interface.readthedocs.io/
