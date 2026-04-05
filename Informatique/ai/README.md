# Algorithmes d'IA et Recherche

## 📚 Description
Cette section contient des implémentations d'algorithmes fondamentaux en informatique et intelligence artificielle.

---

## 📂 Contenu

### 1. **A* (A-star) Pathfinding** (`astar_pathfinding.py`)

#### 🎯 Objectif
Trouver le chemin le plus court entre deux points sur une grille avec obstacles.

#### 📖 Théorie
L'algorithme A* combine le **coût réel** (g) et une **heuristique** (h) pour une recherche efficace :
```
f(n) = g(n) + h(n)
```
- **g(n)** = coût du chemin depuis le point de départ jusqu'au nœud n
- **h(n)** = estimation (heuristique) de la distance du nœud n jusqu'à l'arrivée

#### 🔧 Fonctions Principales

##### `heuristique(case, arrivee)` 
**But :** Estimer la distance restante jusqu'à l'arrivée

**Méthode :** Distance de Manhattan
```python
Distance = |x1 - x2| + |y1 - y2|
```

**Paramètres :**
- `case` (tuple) : Position actuelle (x, y)
- `arrivee` (tuple) : Position cible (x, y)

**Retour :** Entier représentant la distance estimée

---

##### `case_valide(grille, pos)`
**But :** Vérifier si une case est accessible

**Conditions d'accessibilité :**
1. La case doit être **dans les limites** de la grille
2. La case **ne doit pas être un mur** (valeur = 0, pas 1)

**Paramètres :**
- `grille` (list) : Matrice 2D où 0=accessible, 1=mur
- `pos` (tuple) : Position à vérifier (x, y)

**Retour :** `True` si accessible, `False` sinon

---

##### `reconstruire_chemin(came_from, arrivee)`
**But :** Reconstruire le chemin complet du départ à l'arrivée

**Algorithme (Backtracking) :**
1. Commence à l'arrivée
2. Remonte en arrière à l'aide du dictionnaire `came_from` 
3. Enregistre chaque case visitée
4. Inverse la liste pour obtenir le chemin du départ à l'arrivée

**Exemple :**
```python
# Si came_from = {(1,0): (0,0), (2,0): (1,0), ...}
# Et arrivee = (2,0)
# Alors le chemin = [(0,0), (1,0), (2,0)]
```

**Paramètres :**
- `came_from` (dict) : Mappage {case: case_précédente}
- `arrivee` (tuple) : Point d'arrivée

**Retour :** Liste de tuples formant le chemin

---

##### `astar(grille, depart, arrivee)`
**But :** Algorithme principal A* pour la recherche de chemin

**Fonctionnement :**
1. **Initialisation :** Ajouter le départ à la liste d'attente avec f=0
2. **Boucle principale :**
   - Extraire la case avec le plus petit f (priorité)
   - Si c'est l'arrivée → reconstruire et retourner le chemin
   - Sinon → explorer les 4 voisins (haut, bas, gauche, droite)
3. **Pour chaque voisin valide :**
   - Calculer le nouveau coût g
   - Si c'est un meilleur chemin → ajouter à la liste d'attente
4. **Si aucun chemin :** retourner `None`

**Paramètres :**
- `grille` (list) : Matrice 2D (0=libre, 1=obstacle)
- `depart` (tuple) : Position de départ (x, y)
- `arrivee` (tuple) : Position cible (x, y)

**Retour :** Liste de positions du chemin, ou `None` si impossible

#### ⏱️ Complexité
- **Temps :** O(b^d) dans le pire cas (b = facteur de branchement, d = profondeur)
- **Espace :** O(b^d) pour stocker les nœuds

#### 💡 Cas d'Usage
- Jeux vidéo (pathfinding pour IA)
- Robotique (navigation d'obstacles)
- Systèmes GPS et planification d'itinéraires
- Résolution de labyrinthes

---

### 2. **Minimax avec Alpha-Beta Pruning** (`minimax_tictactoe.py`)
- **Objectif :** IA pour Tic-Tac-Toe optimal
- **Concept :** Arbre de jeu minimax avec élagage alpha-beta
- **Complexité :** O(b^d) sans élagage → O(b^(d/2)) avec élagage

---

### 3. **Gradient Descent** (`gradient_descent.py`)
- **Objectif :** Optimisation de fonctions via descente de gradient
- **Concept :** Algorithme itératif pour minimiser une fonction de coût
- **Cas d'usage :** Machine Learning, réseaux de neurones

---

## 🎓 Objectifs Pédagogiques PCSI
- ✅ Comprendre les algorithmes de recherche et optimisation
- ✅ Implémenter des structures de données efficaces (heaps, graphes, dictionnaires)
- ✅ Analyser la complexité temporelle et spatiale
- ✅ Utiliser les heuristiques pour optimiser la recherche
- ✅ Maîtriser le backtracking et la reconstruction de solutions

---

## 🚀 Utilisation

```bash
# Exécuter A* pathfinding
python astar_pathfinding.py

# Résultat attendu
# Chemin trouvé (18 pas) :
# [(0, 1), (0, 2), (1, 2), ..., (9, 9)]
```

---

## 📝 Notes Importantes

### Grille de représentation
```python
grille = [
    [0, 0, 1],  # 0 = accessible, 1 = mur
    [1, 0, 0],
    [0, 0, 0]
]
```

### Système de coordonnées
- Position = (ligne, colonne) = (x, y)
- (0, 0) = angle supérieur gauche
- (9, 9) = angle inférieur droit (pour une grille 10x10)

### Directions possibles
```python
DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
# Haut, Bas, Gauche, Droite
```

---

