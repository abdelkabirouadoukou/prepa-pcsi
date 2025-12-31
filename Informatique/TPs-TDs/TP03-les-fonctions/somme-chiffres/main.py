"""
TP03 - Les Fonctions: Somme des Chiffres
Calcul de la somme des chiffres d'un nombre.

Algorithme:
1. Extraire le dernier chiffre avec n % 10
2. Ajouter ce chiffre à la somme
3. Supprimer le dernier chiffre avec n // 10
4. Répéter jusqu'à n = 0
"""

def sommes_chiffres(n):
    """
    Calcule la somme des chiffres d'un nombre entier.
    
    Args:
        n (int): Un entier positif ou nul
    
    Returns:
        int: La somme de tous les chiffres de n
        
    Exemples:
        >>> sommes_chiffres(123)
        6  # 1 + 2 + 3
        >>> sommes_chiffres(9876)
        30  # 9 + 8 + 7 + 6
        >>> sommes_chiffres(1000)
        1  # 1 + 0 + 0 + 0
    
    Algorithme:
        - n % 10 donne le dernier chiffre
        - n // 10 supprime le dernier chiffre
    """
    s=0
    while n!=0:
        s+=n%10
        n=n//10
        
    return s

print(sommes_chiffres(239176924231))