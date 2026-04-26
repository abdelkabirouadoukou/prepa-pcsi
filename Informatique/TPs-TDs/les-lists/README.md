# 📦 Les Listes - Structures de Données

> Maîtriser les listes Python - La structure de données fondamentale pour manipuler des collections d'éléments.

---

## 📚 Concepts Couverts

### Création et Accès
- Créer une liste: `[1, 2, 3]`, `list()`, list comprehension
- Accéder par indice: `lst[0]`, `lst[-1]`
- Slicing: `lst[1:3]`, `lst[::2]`
- Longueur: `len(lst)`

### Manipulation
- `append()`: Ajouter un élément
- `insert()`: Insérer à une position
- `remove()`: Supprimer par valeur
- `pop()`: Supprimer par index et retourner
- `extend()`: Ajouter plusieurs éléments
- `clear()`: Vider la liste

### Parcours et Recherche
- Itération simple: `for item in lst`
- Itération avec indice: `for i in range(len(lst))`
- `in`: Vérifier l'existence
- `index()`: Trouver la position
- `count()`: Compter les occurrences

### Opérations Avancées
- Tri: `sort()`, `sorted()`
- Inversion: `reverse()`, `lst[::-1]`
- Copie: `lst.copy()`, `lst[:]`
- List comprehension: `[x*2 for x in lst]`

---

## 📝 Exercices Préparatoires

### Niveau 1 - Création et Accès
**Fichier**: `tp-06.pdf`

#### Exercices typiques:
1. **Créer et afficher une liste**
   ```python
   nombres = [10, 20, 30, 40]
   print(nombres)
   print(nombres[0])      # 10
   print(nombres[-1])     # 40
   ```

2. **Accès par slicing**
   ```python
   lst = [1, 2, 3, 4, 5]
   print(lst[1:4])        # [2, 3, 4]
   print(lst[::2])        # [1, 3, 5]
   print(lst[::-1])       # [5, 4, 3, 2, 1]
   ```

3. **Longueur et recherche**
   ```python
   lst = [5, 2, 8, 2, 1]
   print(len(lst))        # 5
   print(2 in lst)        # True
   print(lst.index(8))    # 2
   print(lst.count(2))    # 2
   ```

### Niveau 2 - Modification
4. **Ajouter et supprimer**
   ```python
   lst = [1, 2, 3]
   lst.append(4)          # [1, 2, 3, 4]
   lst.insert(1, 99)      # [1, 99, 2, 3, 4]
   lst.remove(99)         # [1, 2, 3, 4]
   popped = lst.pop()     # lst = [1, 2, 3], popped = 4
   ```

5. **Tri et inversion**
   ```python
   lst = [3, 1, 4, 1, 5]
   lst.sort()             # [1, 1, 3, 4, 5]
   lst.reverse()          # [5, 4, 3, 1, 1]
   
   # Créer une nouvelle liste triée
   trié = sorted([3, 1, 4])  # [1, 3, 4]
   ```

### Niveau 3 - Parcours et Filtrage
6. **Parcourir et transformer**
   ```python
   nombres = [1, 2, 3, 4, 5]
   
   # Doubler chaque nombre
   doublés = []
   for n in nombres:
       doublés.append(n * 2)
   # doublés = [2, 4, 6, 8, 10]
   ```

7. **List comprehension**
   ```python
   nombres = [1, 2, 3, 4, 5]
   pairs = [n for n in nombres if n % 2 == 0]  # [2, 4]
   carrés = [n**2 for n in nombres]             # [1, 4, 9, 16, 25]
   ```

### Niveau 4 - Opérations Complexes
8. **Fusion de listes**
   ```python
   lst1 = [1, 2, 3]
   lst2 = [4, 5, 6]
   
   # Méthode 1
   lst1.extend(lst2)      # lst1 = [1, 2, 3, 4, 5, 6]
   
   # Méthode 2
   fusion = lst1 + lst2
   ```

9. **Statistiques sur liste**
   ```python
   notes = [14, 16, 12, 18, 15]
   
   total = sum(notes)     # 75
   moyenne = total / len(notes)  # 15
   minimum = min(notes)   # 12
   maximum = max(notes)   # 18
   ```

---

## 🎯 Objectifs d'Apprentissage

À la fin de cette section, vous devriez pouvoir:

✅ Créer des listes de différentes façons  
✅ Accéder aux éléments par indice et slicing  
✅ Modifier les listes (ajouter, supprimer, modifier)  
✅ Parcourir une liste complètement  
✅ Utiliser list comprehension  
✅ Trier et chercher dans des listes  
✅ Manipuler plusieurs listes ensemble  

---

## 🔍 Cas d'Usage Réels

### Collecter des Données
```python
# Lire plusieurs nombres
nombres = []
for i in range(5):
    n = int(input("Entrez un nombre: "))
    nombres.append(n)
```

### Filtrer
```python
# Garder seulement les pairs
nombres = [1, 2, 3, 4, 5, 6]
pairs = [n for n in nombres if n % 2 == 0]  # [2, 4, 6]
```

### Transformer
```python
# Convertir en pourcentages
notes = [14, 16, 12, 18]
pourcentages = [n/20 * 100 for n in notes]
```

### Analyser
```python
# Trouver la note max et sa position
notes = [14, 16, 12, 18, 15]
max_note = max(notes)
position = notes.index(max_note)
```

---

## ⚠️ Erreurs Courantes

### Index Out of Range
```python
# ❌ MAUVAIS
lst = [1, 2, 3]
print(lst[5])  # IndexError!

# ✅ BON
if len(lst) > 5:
    print(lst[5])
```

### Modification pendant Itération
```python
# ❌ MAUVAIS: peut causer des bugs
for item in lst:
    lst.remove(item)

# ✅ BON: itérer sur une copie
for item in lst[:]:
    lst.remove(item)
```

### Confondre Référence et Copie
```python
# ❌ MAUVAIS: deux références au même objet
lst2 = lst1
lst2.append(999)  # modifie lst1 aussi!

# ✅ BON: créer une copie
lst2 = lst1.copy()
lst2.append(999)  # lst1 inchangé
```

---

## 🧠 Traçage d'Exécution

### Exemple: Filtrer les pairs
```python
nombres = [1, 2, 3, 4]
pairs = [n for n in nombres if n % 2 == 0]
```

**Trace:**
```
n = 1: 1 % 2 = 1 (pas 0) → pas ajouté
n = 2: 2 % 2 = 0 (vrai) → ajouté
n = 3: 3 % 2 = 1 (pas 0) → pas ajouté
n = 4: 4 % 2 = 0 (vrai) → ajouté
Résultat: [2, 4]
```

---

## 💻 Template de Solution

```python
# Créer/Lire une liste
lst = []
n = int(input("Combien d'éléments? "))
for i in range(n):
    elem = int(input(f"Élément {i+1}: "))
    lst.append(elem)

# Traiter la liste
résultat = [x * 2 for x in lst]

# Afficher
print("Original:", lst)
print("Traité:", résultat)
print(f"Statistiques: min={min(lst)}, max={max(lst)}, moy={sum(lst)/len(lst)}")
```

---

## 📊 Comparaison: List vs Autres

| Opération | List | Tuple | Dict |
|-----------|------|-------|------|
| Créer | `[1,2,3]` | `(1,2,3)` | `{'a':1}` |
| Modifier | ✅ | ❌ | ✅ |
| Ordonné | ✅ | ✅ | ❌ |
| Rapide pour recherche | O(n) | O(n) | O(1) |

---

## 🚀 Progression

1. ✅ **Compléter tous les exercices de Niveau 1**
2. ✅ **Faire Niveau 2 - Modification**
3. ✅ **Maîtriser Niveau 3 - List Comprehension**
4. ✅ **Résoudre Niveau 4 - Opérations Complexes**
5. → **Passer à [TP03 - Fonctions](../TP03-les-fonctions/)**
6. → **Puis [TD - Tris](../TD-les-tris/)**

---

## 📚 Ressources

- **Python Docs**: [Lists](https://docs.python.org/3/tutorial/datastructures.html)
- **Visualisation**: [PythonTutor - Listes](https://pythontutor.com/)
- **Pratique**: [LeetCode Easy](https://leetcode.com/problemset/all/?difficulty=EASY) - Array problems

---

## 💡 Conseils

- **Commencez simple** avant list comprehension
- **Testez le slicing** avec print() pour comprendre
- **Utilisez `.copy()`** si vous modifiez une copie
- **Préférez list comprehension** c'est plus Pythonique!
- **Tracez sur papier** pour les opérations complexes

> **Note**: Consultez le fichier PDF fourni pour les exercices détaillés et spécifiques au cours.
