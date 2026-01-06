#!/usr/bin/env python3
"""
Script de lancement pour exécuter la fonction topServeurVote
"""
from dotenv import load_dotenv
import os
from src.excalia_autovote.main import topServeurVote

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

if __name__ == "__main__":
    # Récupérer le pseudo depuis les variables d'environnement
    pseudo = os.getenv("PSEUDO", "Wallans")
    
    print(f"Démarrage du vote pour le pseudo: {pseudo}")
    
    try:
        topServeurVote(pseudo)
        print("Vote terminé avec succès !")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        raise

