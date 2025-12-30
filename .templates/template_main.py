"""
Template - Code Principal pour TP/TD
=====================================

Nom du TP/TD: [Nom]
Date: [Date]
Auteur: Abdelkabir
Matière: [Mathématiques / Physique / Chimie / SI]

Description:
-----------
[Description brève du programme]

Utilisation:
-----------
python main.py

"""

# ============================================================================
# IMPORTS
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional

# ============================================================================
# CONSTANTES
# ============================================================================

# Définir les constantes ici
CONSTANTE_1 = 0
CONSTANTE_2 = 0

# ============================================================================
# FONCTIONS PRINCIPALES
# ============================================================================

def fonction_principale():
    """
    Description de la fonction principale.
    
    Args:
        param1: Description du paramètre 1
        param2: Description du paramètre 2
    
    Returns:
        Description du retour
        
    Examples:
        >>> fonction_principale()
        Résultat attendu
    """
    pass


def fonction_auxiliaire(param1: float, param2: float) -> float:
    """
    Description de la fonction auxiliaire.
    
    Args:
        param1: Description du paramètre 1
        param2: Description du paramètre 2
    
    Returns:
        Description du retour
    """
    pass

# ============================================================================
# VISUALISATION
# ============================================================================

def afficher_resultats(data: np.ndarray):
    """
    Affiche les résultats sous forme de graphique.
    
    Args:
        data: Données à afficher
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title("Titre du graphique")
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.grid(True)
    plt.show()

# ============================================================================
# MAIN
# ============================================================================

def main():
    """
    Fonction principale du programme.
    """
    print("=" * 60)
    print("TP/TD: [Nom]")
    print("=" * 60)
    
    # Votre code ici
    
    print("\n" + "=" * 60)
    print("Fin du programme")
    print("=" * 60)


if __name__ == "__main__":
    main()
