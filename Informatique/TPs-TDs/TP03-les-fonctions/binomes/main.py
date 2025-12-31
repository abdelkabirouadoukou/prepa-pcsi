"""
TP03 - Les Fonctions: Coefficients Binomiaux
Exercices sur la factorielle, les produits et les coefficients binomiaux.
"""

# q1
def factorielle(n):
    """
    Calcule la factorielle de n de manière récursive.
    
    Args:
        n (int): Un entier positif ou nul
    
    Returns:
        int: n! = n × (n-1) × ... × 2 × 1
        
    Exemples:
        >>> factorielle(0)
        1
        >>> factorielle(5)
        120
    """
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

print(factorielle(3))

# q2
def produit(n,k):
    """
    Calcule le produit de k termes consécutifs décroissants à partir de n.
    Produit(n,k) = n × (n-1) × (n-2) × ... × (n-k+1)
    
    Args:
        n (int): Nombre de départ
        k (int): Nombre de termes à multiplier
    
    Returns:
        int: Le produit des k premiers termes
        
    Exemples:
        >>> produit(5, 3)
        60  # 5 × 4 × 3
        >>> produit(10, 2)
        90  # 10 × 9
    
    Note:
        Peut aussi être calculé avec: factorielle(n) / factorielle(n-k)
    """
    if k == 0:
        return 1
    else:
        return n*produit(n-1, k-1)
    # ou bien on peut utilise factorielle(n) / factorielle(n-k)

# q3
def binom(n,k):
    """
    Calcule le coefficient binomial C(n,k).
    C(n,k) = n! / (k! × (n-k)!) = nombre de combinaisons de k éléments parmi n.
    
    Args:
        n (int): Nombre total d'éléments
        k (int): Nombre d'éléments à choisir
    
    Returns:
        float or str: Le coefficient binomial, ou "Non" si k > n
        
    Exemples:
        >>> binom(5, 2)
        10.0
        >>> binom(10, 3)
        120.0
        >>> binom(3, 5)
        'Non'
    
    Note:
        Formule alternative: factorielle(n) / (factorielle(k) × factorielle(n-k))
    """
    if k>n:
        return "Non"
    else:
        return produit(n,k)/factorielle(k) # ou bien factorielle(n)/factorielle(k)*factorielle(n-k)
    

