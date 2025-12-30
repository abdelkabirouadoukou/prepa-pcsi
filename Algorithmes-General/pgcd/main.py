"""
    Fonction PGCD (Plus Grand Commun Diviseur)
    by Abdelkabir
"""

def pgcd(a, b):
    a, b = abs(a), abs(b)  # Conversion en valeur absolues
    
    # Cas particulier : PGCD(0, 0) n’est pas défini mathématiquement
    if a == 0 and b == 0:
        return "PGCD(0, 0) n'est pas défini"
    
    # Cas : si l’un des deux est 0
    if b == 0:
        return a
    if a == 0:
        return b

    # Algorithme d'Euclide
    while a%b!= 0:
        a, b=b, a%b
    return b

print(pgcd(3,2))  # output will be 1
print(pgcd(0,0))  # output will be 
