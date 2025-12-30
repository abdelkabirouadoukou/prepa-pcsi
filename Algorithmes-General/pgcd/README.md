# Fonction PGCD (Plus Grand Commun Diviseur)

## Description

Cette fonction calcule le Plus Grand Commun Diviseur (PGCD) de deux nombres entiers en utilisant l'algorithme d'Euclide, avec gestion complète des cas particuliers.

## Code

```python
"""
    Fonction PGCD (Plus Grand Commun Diviseur)
    by Abdelkabir
"""

def pgcd(a, b):
    a, b = abs(a), abs(b)  # Conversion en valeur absolues

    # Cas particulier : PGCD(0, 0) n'est pas défini mathématiquement
    if a == 0 and b == 0:
        return "PGCD(0, 0) n'est pas défini"

    # Cas : si l'un des deux est 0
    if b == 0:
        return a
    if a == 0:
        return b

    # Algorithme d'Euclide
    while a%b!= 0:
        a, b=b, a%b
    return b

print(pgcd(3,2))  # output will be 1
print(pgcd(0,0))  # output will be "PGCD(0, 0) n'est pas défini"
```

## Utilisation

```python
# Exemples d'utilisation
print(pgcd(3, 2))    # Affiche : 1
print(pgcd(12, 8))   # Affiche : 4
print(pgcd(-15, 10)) # Affiche : 5
print(pgcd(0, 5))    # Affiche : 5
print(pgcd(0, 0))    # Affiche : "PGCD(0, 0) n'est pas défini"
```

## Fonctionnalités

Cette implémentation robuste gère tous les cas possibles :

### 1. Nombres négatifs

- Utilise `abs()` pour convertir automatiquement en valeurs absolues
- Fonctionne avec tous les nombres entiers relatifs (ℤ)

### 2. Cas avec zéro

- **PGCD(a, 0) = a** : Si un nombre est 0, le PGCD est l'autre nombre
- **PGCD(0, 0)** : Retourne un message explicatif car mathématiquement non défini

### 3. Algorithme d'Euclide

- Implémentation classique et efficace
- Échange itératif des variables jusqu'à ce que le reste soit 0

## Comment ça fonctionne

1. **Préparation** : Conversion en valeurs absolues avec `abs()`
2. **Vérifications** :
   - Si les deux nombres sont 0 → message d'erreur
   - Si un seul est 0 → retourne l'autre nombre
3. **Algorithme d'Euclide** :
   - Divise `a` par `b`
   - Remplace `a` par `b` et `b` par le reste
   - Répète jusqu'à ce que le reste soit 0

## Exemples complets

```python
# Cas normaux
print(pgcd(48, 18))   # Résultat : 6
print(pgcd(17, 13))   # Résultat : 1 (nombres premiers entre eux)

# Avec nombres négatifs
print(pgcd(-24, 36))  # Résultat : 12
print(pgcd(-15, -25)) # Résultat : 5

# Cas avec zéro
print(pgcd(42, 0))    # Résultat : 42
print(pgcd(0, 17))    # Résultat : 17
print(pgcd(0, 0))     # Résultat : "PGCD(0, 0) n'est pas défini"

# Cas identiques
print(pgcd(7, 7))     # Résultat : 7
```

## Domaine de définition

- **Entrée** : Tous les nombres entiers relatifs (ℤ)
- **Sortie** : Nombre entier positif ou message d'erreur pour PGCD(0,0)

## Avantages de cette implémentation

✅ **Robuste** : Gère tous les cas particuliers  
✅ **Universelle** : Fonctionne avec les nombres négatifs  
✅ **Claire** : Messages explicites pour les cas non définis  
✅ **Efficace** : Utilise l'algorithme d'Euclide optimisé  
✅ **Documentée** : Code bien commenté et explicatif
