# Somme des Chiffres

## 📚 Description
Calculer la somme des chiffres d'un nombre entier.

Exemple: `somme_chiffres(123)` → `1 + 2 + 3 = 6`

## 🎯 Objectifs
- Comprendre les boucles et les itérations
- Manipuler les nombres (modulo, division)
- Implémenter des fonctions avec valeur de retour
- Analyser un problème en étapes

## 🔍 Approches

### Approche 1: Division entière (itérative)
```python
while nombre > 0:
    somme += nombre % 10  # Prendre le dernier chiffre
    nombre //= 10        # Enlever le dernier chiffre
```

### Approche 2: Conversion chaîne (Pythonic)
```python
return sum(int(chiffre) for chiffre in str(nombre))
```

### Approche 3: Récursion
```python
if nombre == 0:
    return 0
return (nombre % 10) + somme_chiffres(nombre // 10)
```

## 💡 Concepts
- Opérateurs modulo (%) et division entière (//)
- Boucles while
- Récursion
- Comprehensions Python

