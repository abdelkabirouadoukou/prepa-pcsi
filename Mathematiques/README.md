# 📐 Mathématiques - PCSI

> Travaux pratiques et travaux dirigés de mathématiques pour la préparation aux concours PCSI.

---

## 📋 Navigation Rapide

| Domaine | Contenu | Statut |
|---------|---------|--------|
| **Algèbre** | Matrices, systèmes linéaires | 📝 À compléter |
| **Analyse** | Limites, dérivation, intégration | 📝 À compléter |
| **Géométrie** | Vecteurs, espaces | 📝 À compléter |
| **Probabilités** | Distributions, stats | 📝 À compléter |

---

## 📋 Contenu Pédagogique

### TPs-TDs (Travaux Pratiques & Travaux Dirigés)

Exercices et projets programmés en Python pour approfondir les concepts mathématiques :

#### **Algèbre Linéaire**
- Manipulation de vecteurs et matrices
- Résolution de systèmes linéaires (Gauss, décomposition LU)
- Calcul de déterminants et inverses
- Valeurs propres et vecteurs propres
- Diagonalisation et réduction de matrices

#### **Analyse Numérique**
- Résolution d'équations non linéaires (Newton-Raphson, dichotomie)
- Interpolation polynomiale (Lagrange, Newton)
- Intégration numérique (trapèzes, Simpson, quadrature)
- Résolution d'équations différentielles (Euler, Runge-Kutta)

#### **Algorithmes Avancés**
- Optimisation (gradient, méthode de Newton)
- Décompositions matricielles (QR, SVD, Cholesky)
- Approximation de fonctions
- Méthodes itératives pour systèmes linéaires

---

## 🎯 Objectifs Pédagogiques

✅ **Concepts Mathématiques**
- Maîtriser l'algèbre linéaire (fondation de toute science)
- Comprendre les erreurs numériques (arrondi, propagation)
- Choisir l'algorithme adapté au problème
- Analyser la stabilité et la convergence des méthodes

✅ **Programmation Mathématique**
- Implémenter sans bibliothèque (comprendre le fonctionnement)
- Utiliser numpy/scipy efficacement
- Tester et valider les résultats
- Optimiser pour la performance

✅ **Applications Pratiques**
- Résoudre des problèmes réels (physique, chimie, économie)
- Modéliser mathématiquement des situations
- Visualiser les résultats et les interpréter

---

## 📚 Concepts Clés PCSI

### 1. **Systèmes Linéaires**
```
AX = B
Où A est une matrice n×n, X et B sont des vecteurs
Méthodes : Gauss, Gauss-Jordan, LU, factorisation Cholesky
```

### 2. **Valeurs et Vecteurs Propres**
```
Av = λv
Utilité : Diagonalisation, analyse de stabilité, matrices de Markov
```

### 3. **Approximation et Interpolation**
```
Pourreau travers N points ?
→ Lagrange : polynôme passant exactement par les points
→ Moindres carrés : meilleure approximation au sens des erreurs
```

### 4. **Équations Différentielles Ordinaires (EDO)**
```
dy/dx = f(x, y) avec condition initiale y(x₀) = y₀
Méthodes numériques : Euler, Runge-Kutta ordre 2/4
Applications : Systèmes physiques, modèles démographiques
```

---

## 🛠️ Bibliothèques Essentielles

```python
import numpy as np          # Algèbre linéaire de base
from scipy.linalg import *  # Décompositions avancées
from scipy.optimize import * # Optimisation
from scipy.integrate import * # Intégration numérique
import matplotlib.pyplot as plt  # Visualisation
```

---

## 📋 Structure des Fichiers

```
Mathematiques/
├── README.md (ce fichier)
└── TPs-TDs/
    ├── [Algorithmes numériques]
    ├── [Calculs matriciels]
    ├── [Résolution de systèmes]
    └── [Optimisation]
```

---

## 💡 Conseils de Travail

### Pour les **Matrices**
1. Toujours vérifier les dimensions (n×m multiplié par m×p donne n×p)
2. Attention à l'ordre : AB ≠ BA en général
3. Visualiser avec `print(np.array(...))` avant de coder des algorithmes

### Pour les **EDO**
1. Commencer par une solution analytique connue pour valider
2. Comparer différentes méthodes (Euler vs RK4)
3. Vérifier la stabilité pour les équations raides

### Pour les **Systèmes Linéaires**
1. Éviter la division directe : ne JAMAIS faire `X = inv(A) @ B` (instable)
2. Utiliser `np.linalg.solve(A, B)` ou une décomposition LU
3. Tester avec des matrices mal conditionnées

### Pour le **Debugging**
```python
import numpy as np
A = np.array([[...], [...]])
print(f"Rang de A : {np.linalg.matrix_rank(A)}")
print(f"Nombre de condition : {np.linalg.cond(A)}")
print(f"Déterminant : {np.linalg.det(A)}")
```

---

## 📜 Ressources Complémentaires

- **Gilbert Strang** - Linear Algebra (fondamental)
- **Numerical Recipes** - Méthodes numériques classiques
- **Documentation scipy** - https://docs.scipy.org/
- **3Blue1Brown YouTube** - Visualisation intuitive de l'algèbre linéaire
- Suites et séries
- Probabilités et statistiques
- Analyse numérique
- Algèbre linéaire
- Analyse (limites, continuité, dérivabilité)
- Intégration
- Équations différentielles
- Géométrie

## 🎯 Compétences Développées

- ✅ Implémentation d'algorithmes mathématiques
- ✅ Manipulation de structures de données (matrices, vecteurs)
- ✅ Visualisation de fonctions et données
- ✅ Résolution numérique d'équations
- ✅ Programmation scientifique en Python

## 📖 Convention de Nommage

```
TPs-TDs/
├── TP01-nom-descriptif/
│   ├── main.py
│   └── README.md
├── TD01-nom-descriptif/
│   ├── exercice1.py
│   └── README.md
...
```

## 🚀 Utilisation

Chaque dossier contient :
1. Le code source Python (`.py`)
2. Un `README.md` avec l'énoncé et explications
3. Les données nécessaires (si applicable)

## 📦 Dépendances

```bash
pip install numpy matplotlib scipy sympy
```

---

**Dernière mise à jour :** Décembre 2025
