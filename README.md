# Excalia AutoVote

Script d'automatisation de vote pour le serveur Minecraft Excalia sur :

- [top-serveurs.net](https://top-serveurs.net).

## 📋 Description

Ce projet permet d'automatiser le processus de vote pour le serveur Excalia. Le script utilise SeleniumBase avec undetected-chromedriver pour :

- Ouvrir automatiquement la page de vote
- Gérer le pop-up d'autorisation
- Résoudre le captcha (avec interaction manuelle)
- Valider le vote

## 🚀 Installation

### Prérequis

- Python >= 3.13
- Poetry (gestionnaire de dépendances)

### ⚙️ Étapes d'installation et de configuration

1. **Cloner le dépôt** (ou télécharger le projet)

2. **Installer les dépendances avec Poetry :**

   ```bash
   poetry install
   ```

3. **Créer le fichier `.env`** à la racine du projet :

   ```bash
   cp .env.example .env
   ```

   ⚠️ **Important :** Changer _votre_pseudo_ par votre réel pseudo.

## 🎯 Utilisation

### Lancement simple

Pour lancer le vote avec les paramètres du fichier `.env` :

```bash
poetry run python run.py
```

Ou si vous êtes dans l'environnement virtuel Poetry :

```bash
python run.py
```

## 🔧 Fonctionnalités

- ✅ Ouverture automatique du navigateur avec undetected-chromedriver
- ✅ Gestion automatique du pop-up d'autorisation
- ✅ Résolution du captcha (nécessite une interaction manuelle)
- ✅ Validation automatique du vote
- ✅ Configuration via variables d'environnement

## 📁 Structure du projet

```
excalia-autovote/
├── src/
│   └── excalia_autovote/
│       ├── __init__.py
│       └── main.py          # Fonction principale
├── tests/
├── run.py                    # Script de lancement
├── .env                      # Configuration (non versionné)
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## 📝 Dépendances

- `seleniumbase` (>=4.45.8,<5.0.0) : Automatisation du navigateur
- `python-dotenv` (>=1.0.0,<2.0.0) : Gestion des variables d'environnement

## 👤 Auteur

**Wallans**  
Email : timothe.vaquie1@gmail.com

## 📄 Licence

Ce projet est fourni tel quel, sans garantie.
