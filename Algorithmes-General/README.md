# 💻 Algorithmes Généraux & Problem Solving

Collection d'algorithmes fondamentaux, structures de données et exercices de résolution de problèmes essentiels pour tout informaticien.

---

## 📋 Contenu Pédagogique

### 1. **Algorithmes Mathématiques**

#### **PGCD (Plus Grand Commun Diviseur)**
- **Algorithme d'Euclide** : Très efficace même pour grands nombres
- **Formule** : pgcd(a,b) = pgcd(b, a mod b) jusqu'à b = 0
- **Complexité** : O(log(min(a,b)))
- **Applications** : Simplification de fractions, cryptographie RSA

#### **PPCM (Plus Petit Commun Multiple)**
- **Relation** : ppcm(a,b) = (a × b) / pgcd(a,b)
- **Applications** : Problèmes de synchronisation, calculs d'orbites

#### **Crible d'Eratosthène**
- **Objectif** : Trouver tous les nombres premiers jusqu'à N
- **Idée** : Éliminer progressivement les multiples de chaque nombre
- **Complexité** : O(N log log N)
- **Cas d'usage** : Générer listes de nombres premiers, cryptographie

#### **Test de Primalité**
- **Déterministe** : Vérifier la divisibilité jusqu'à $\sqrt{N}$
- **Probabiliste** : Miller-Rabin (rapide pour très grands nombres)
- **Applications** : Génération de clés cryptographiques

#### **Exponentiation Rapide**
- **Problème** : Calculer $a^b \mod n$ efficacement
- **Méthode naïve** : O(b) multiplications → intrégnable pour b grand
- **Exponentiation binaire** : O(log b) multiplications
- **Applications** : Cryptographie RSA, modélo exponentiel

---

### 2. **Structures de Données**

#### **Listes et Tableaux**
- Accès O(1), insertion/suppression O(n) au milieu

#### **Piles (Stacks)**
- LIFO (Last In First Out)
- Utilisation : Appels de fonction, parsing, déséquilibrage de parenthéses

#### **Files (Queues)**
- FIFO (First In First Out)
- Utilisation : BFS, imprimantes, ordonnancement

#### **Arbres**
- **Binaires de recherche (BST)** : Recherche/insertion O(log n)
- **Arbres équilibrés (AVL, Red-Black)** : Garantissent balancement
- **Tas (Heaps)** : Tri par tas, file de priorité

#### **Graphes**
- **Représentations** : Matrice d'adjacence vs liste d'adjacence
- **Parcours** : DFS, BFS
- **Shortest path** : Dijkstra, A*
- **Applications** : Réseaux, social graphs, jeux vidéo

---

### 3. **Problem Solving Exercises**

#### **Niveaux d'Apprentissage**

**Niveau 1 - Basique** :
- Find Missing Number : Trouver l'entier manquant dans [1..n]
- Frequency Count : Compter les occurrences d'éléments
- Move Zeros : Déplacer tous les zéros à la fin

**Niveau 2 - Intermédiaire** :
- Merge Two Lists : Fusionner deux listes triées
- Rotate List : Rotation circulaire d'une liste
- Second Largest Element : Trouver le deuxième plus grand
- Sum of List Using Recursion : Somme récursive

**Niveau 3 - Avancé** :
- Two Sum : Trouver deux nombres dont la somme = target
- Longest Substring Without Repeating : Plus longue sous-chaîne sans répétition
- Pile de crépes : Tri par inversion de bajo-listes

#### **Stratégies de Résolution**
1. **Brute force** : Solution naïve d'abord, puis optimiser
2. **Two pointers** : Démarrer des deux extrémités
3. **Sliding window** : Fenêtre glissante sur un tableau
4. **Hash maps** : Accélérer les recherches O(n) → O(1)
5. **Divide and conquer** : Diviser le problème en sous-problèmes
6. **Dynamic programming** : Mémorisation des résultats

---

## 🎯 Objectifs PCSI

✅ **Algorithmes Fondamentaux**
- Implémenter des algorithmes de base sans bibliothèque
- Analyser la complexité (temps et espace)
- Optimiser pour des cas limites et grands volumes de données

✅ **Efficacité**
- Préférer O(log n) à O(n), O(n) à O(n²), O(n log n) à O(n²)
- Comprendre l'impact pratique : O(n²) sur n=10⁶ = catastrophe!

✅ **Thinking Algorithmique**
- Avant de coder, penser à la structure
- Diviser un gros problème en petits sous-problèmes
- Vérifier avec des cas de test simples
- Gérer les cas limites (liste vide, un seul élément, etc.)

---

## 📁 Structure des Fichiers

```
Algorithmes-General/
├── README.md (ce fichier)
├── pgcd/
│   ├── main.py (Euclide, PGCD)
│   └── README.md
└── Problem-Solving/
    ├── README.md
    ├── find-missing-number/
    ├── frequency-count/
    ├── merge-two-lists/
    ├── move-zeros/
    ├── rotate-list/
    ├── second-largest-element/
    │   ├── main.py
    │   └── README.md
    └── Sum of List Using Recursion/
        ├── main.py
        └── README.md
```

---

## 💡 Conseils Pratiques

### Lors de la Résolution

1. **Complexité d'Abord** : Demandez-vous : "Quelle est la meilleure complexité possible ?"
2. **Trade-off Espace/Temps** : Utiliser plus de mémoire pour aller plus vite
3. **Cas Limites** : Liste/string vide, un seul élément, tous identiques
4. **Test** : Écrivez les tests AVANT le code (TDD)

### Optimisation

```python
# ❌ O(n²) - Naïf
for i in range(n):
    for j in range(n):
        if arr[i] + arr[j] == target:
            return (i, j)

# ✅ O(n) - Hash map
seen = set()
for num in arr:
    complement = target - num
    if complement in seen:
        return (target - complement, num)
    seen.add(num)
```

---

## 📚 Pour Aller Plus Loin

- **LeetCode** : https://leetcode.com/ (problèmes classiques)
- **GeeksforGeeks** : Tutoriels détaillés
- **Cracking the Coding Interview** : Livre de référence
- **Big O Cheat Sheet** : Comprendre les complexités
- Calculs modulaires

### Structures de Données
- Listes chaînées
- Piles et files
- Arbres binaires
- Graphes

### Algorithmes de Tri
- Tri fusion
- Tri rapide
- Tri par tas

### Algorithmes de Recherche
- Recherche dichotomique
- Parcours de graphes (DFS, BFS)

### Programmation Dynamique
- Fibonacci optimisé
- Plus longue sous-séquence commune
- Problème du sac à dos

### Problem Solving
Exercices de résolution de problèmes provenant de :
- **LeetCode** - Problèmes d'entretien technique
- **HackerRank** - Défis algorithmiques
- **Codeforces** - Compétitions de programmation
- **France-IOI** - Olympiades d'informatique
- **Project Euler** - Problèmes mathématiques

## 🎯 Objectifs

- ✅ Comprendre les algorithmes fondamentaux
- ✅ Analyser la complexité (temporelle et spatiale)
- ✅ Implémenter proprement en Python
- ✅ Documenter et tester le code
- ✅ S'entraîner au problem solving
- ✅ Préparer les entretiens techniques

## 📖 Organisation

```
Algorithmes-General/
├── pgcd/
│   ├── main.py
│   └── README.md
├── tri-fusion/
│   ├── main.py
│   ├── tests.py
│   └── README.md
├── Problem-Solving/
│   ├── LeetCode/
│   │   ├── Easy/
│   │   ├── Medium/
│   │   └── Hard/
│   ├── HackerRank/
│   ├── Codeforces/
│   └── France-IOI/
...
```

## 🚀 Utilisation

Chaque implémentation inclut :
1. Le code source commenté
2. Des exemples d'utilisation
3. Des tests unitaires
4. L'analyse de complexité

### Pour Problem Solving
Chaque solution de problème contient :
- L'énoncé du problème (lien vers la source)
- La solution commentée
- L'analyse de complexité
- Les cas de test

## 📦 Modules Utilisés

```bash
# Modules standards Python
import time
import unittest
import collections
import heapq
```

## 💡 Conseils pour Problem Solving

1. **Comprendre le problème** : Lire attentivement l'énoncé
2. **Exemples** : Tester avec les exemples donnés
3. **Approche** : Réfléchir à l'algorithme avant de coder
4. **Complexité** : Analyser le temps et l'espace
5. **Tester** : Valider avec différents cas
6. **Optimiser** : Améliorer si nécessaire

## 🔗 Ressources

- **LeetCode** : https://leetcode.com/
- **HackerRank** : https://www.hackerrank.com/
- **Codeforces** : https://codeforces.com/
- **France-IOI** : https://www.france-ioi.org/
- **Project Euler** : https://projecteuler.net/

---

**Dernière mise à jour :** Décembre 2025
