"""
TP03 - Les Fonctions: Nombres Amis
Exercices sur les diviseurs et les nombres amicaux.

Deux nombres x et y sont amis si:
- somme(diviseurs_stricts(x)) = y
- somme(diviseurs_stricts(y)) = x

Exemple: 220 et 284 sont des nombres amis.
"""

def divStrict(x):
    """
    Affiche tous les diviseurs stricts de x (tous les diviseurs sauf x lui-même).
    
    Args:
        x (int): Un entier strictement positif
    
    Returns:
        None: Affiche les diviseurs dans l'ordre décroissant
        
    Exemple:
        >>> divStrict(30)
        15
        10
        6
        5
        3
        2
        1
    """
    i = x - 1
    while i > 0:
        if x % i == 0:
            print(i)
        i = i - 1



def somDivStrict(x):
    """
    Calcule la somme de tous les diviseurs stricts de x.
    
    Args:
        x (int): Un entier strictement positif
    
    Returns:
        int: La somme des diviseurs stricts de x
        
    Exemples:
        >>> somDivStrict(6)
        6  # 1 + 2 + 3 (nombre parfait)
        >>> somDivStrict(30)
        42  # 1 + 2 + 3 + 5 + 6 + 10 + 15
        >>> somDivStrict(220)
        284  # 220 et 284 sont des nombres amis
        >>> somDivStrict(284)
        220
    """
    som = 0
    for i in range(1,x):
        if x%i==0:
            som+=i
    return som

print(somDivStrict(30))

