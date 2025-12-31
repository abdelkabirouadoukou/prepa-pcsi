# TP03 - Les Fonctions

## 📝 Description
Ce TP explore les concepts fondamentaux des fonctions en Python, notamment la récursivité, les calculs mathématiques et les algorithmes sur les nombres.

## 🎯 Objectifs d'apprentissage
- Maîtriser la récursivité en Python
- Comprendre les fonctions mathématiques (factorielle, coefficients binomiaux)
- Manipuler les nombres et leurs propriétés (diviseurs, chiffres)
- Appliquer les concepts de boucles et conditions dans les fonctions

## 📂 Exercices

### 1. Binômes (`binomes/`)
**Concepts**: Récursivité, factorielle, coefficients binomiaux

**Fonctions implémentées**:
- `factorielle(n)`: Calcule n! de manière récursive
- `produit(n, k)`: Calcule le produit n × (n-1) × ... × (n-k+1)
- `binom(n, k)`: Calcule le coefficient binomial C(n,k) = n! / (k! × (n-k)!)

**Exemples**:
```python
factorielle(5)  # 120
produit(5, 3)   # 60 (5 × 4 × 3)
binom(5, 2)     # 10
```

### 2. Nombres Amis (`nombers-amis/`)
**Concepts**: Diviseurs, somme de diviseurs, nombres amicaux

**Fonctions implémentées**:
- `divStrict(x)`: Affiche tous les diviseurs stricts de x (diviseurs < x)
- `somDivStrict(x)`: Calcule la somme des diviseurs stricts de x

**Théorie**: Deux nombres x et y sont **amis** si:
- somme(diviseurs_stricts(x)) = y
- somme(diviseurs_stricts(y)) = x

**Exemples**:
```python
divStrict(30)      # Affiche: 15, 10, 6, 5, 3, 2, 1
somDivStrict(30)   # Retourne: 42 (15+10+6+5+3+2+1)
```

**Paire de nombres amis classique**: 220 et 284
- somDivStrict(220) = 284
- somDivStrict(284) = 220

### 3. Somme des Chiffres (`somme-chiffres/`)
**Concepts**: Manipulation de chiffres, division entière, modulo

**Fonction implémentée**:
- `sommes_chiffres(n)`: Calcule la somme des chiffres d'un nombre

**Algorithme**:
1. Extraire le dernier chiffre avec `n % 10`
2. Ajouter ce chiffre à la somme
3. Supprimer le dernier chiffre avec `n // 10`
4. Répéter jusqu'à n = 0

**Exemples**:
```python
sommes_chiffres(123)    # 6 (1+2+3)
sommes_chiffres(9876)   # 30 (9+8+7+6)
```

## 🔧 Utilisation

Pour tester un exercice:
```bash
# Depuis le dossier TP03-les-fonctions
python binomes/main.py
python nombers-amis/main.py
python somme-chiffres/main.py
```

## 💡 Concepts clés

### Récursivité
Une fonction qui s'appelle elle-même. Nécessite:
- **Cas de base**: condition d'arrêt
- **Cas récursif**: appel de la fonction avec paramètres modifiés

### Diviseurs stricts
Pour un nombre x, les diviseurs stricts sont tous les diviseurs de x sauf x lui-même.

### Division entière et modulo
- `n // 10`: Supprime le dernier chiffre
- `n % 10`: Extrait le dernier chiffre

## 📚 Références
- Factorielle: n! = n × (n-1) × ... × 2 × 1
- Coefficient binomial: C(n,k) = n! / (k! × (n-k)!)
- Nombres amis: Concept introduit par les Pythagoriciens

## ✅ Tests suggérés

### Binômes
- `factorielle(0)` → 1
- `factorielle(5)` → 120
- `binom(10, 2)` → 45

### Nombres amis
- `somDivStrict(6)` → 6 (nombre parfait: 1+2+3)
- `somDivStrict(220)` → 284
- `somDivStrict(284)` → 220

### Somme chiffres
- `sommes_chiffres(0)` → 0
- `sommes_chiffres(1234567890)` → 45

---
**Auteur**: PCSI - Ibn Taimiya CPGE  
**Date**: 2024-2025
