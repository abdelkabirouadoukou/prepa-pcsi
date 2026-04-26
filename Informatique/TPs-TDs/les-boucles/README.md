# 🔄 Les Boucles - Contrôle de Flux

> Comprendre et maîtriser les boucles (`for`, `while`) - Essentiels pour itérer sur des données et répéter des opérations.

---

## 📚 Concepts Couverts

### Les Boucles `for`
- Itération sur une séquence (liste, string, range)
- Accès à l'indice et à la valeur
- `range()` pour générer des séquences
- Boucles imbriquées

### Les Boucles `while`
- Condition répétitive
- Danger de boucle infinie
- Actualisation de variables (i += 1)
- Cas d'usage: algorithmes interactifs

### Contrôle de Boucle
- `break`: sortir de la boucle
- `continue`: sauter à l'itération suivante
- `else` avec boucles (exécuté si pas de break)

---

## 📝 Exercices Préparatoires

### Niveau 1 - Basics
**Fichier**: `01-TP1 (1).pdf`

#### Exercices typiques:
1. **Afficher les nombres de 1 à 10**
   ```python
   for i in range(1, 11):
       print(i)
   ```

2. **Afficher la table de multiplication**
   ```python
   n = int(input("Entrez un nombre: "))
   for i in range(1, 11):
       print(f"{n} × {i} = {n * i}")
   ```

3. **Somme des entiers jusqu'à n**
   ```python
   n = int(input("Entrez n: "))
   total = 0
   for i in range(1, n + 1):
       total += i
   print(total)
   ```

### Niveau 2 - Listes et Boucles
4. **Parcourir une liste**
   ```python
   nombres = [1, 2, 3, 4, 5]
   for num in nombres:
       print(num)
   ```

5. **Modifier une liste avec boucle**
   ```python
   nombres = [1, 2, 3, 4, 5]
   for i in range(len(nombres)):
       nombres[i] = nombres[i] * 2
   ```

### Niveau 3 - Boucles Imbriquées
6. **Tableau de multiplication (5×5)**
   ```python
   for i in range(1, 6):
       for j in range(1, 6):
           print(f"{i*j:3}", end=" ")
       print()
   ```

7. **Motifs avec boucles**
   ```python
   # Triangle
   n = 5
   for i in range(1, n+1):
       print("*" * i)
   ```

---

## 🎯 Objectifs d'Apprentissage

À la fin de cette section, vous devriez pouvoir:

✅ Utiliser `for` pour itérer sur une séquence  
✅ Utiliser `while` avec une condition  
✅ Comprendre `range()` et ses paramètres  
✅ Écrire des boucles imbriquées  
✅ Utiliser `break` et `continue` correctement  
✅ Identifier et éviter les boucles infinies  
✅ Tracer une boucle sur papier (étape par étape)  

---

## 🔍 Cas d'Usage Réels

### Parcourir des Données
```python
# Calcul moyen
notes = [14, 16, 12, 18]
total = 0
for note in notes:
    total += note
moyenne = total / len(notes)
```

### Recherche
```python
# Trouver si un nombre existe
nombres = [3, 7, 2, 9]
cherche = 7
trouve = False
for n in nombres:
    if n == cherche:
        trouve = True
        break
```

### Génération
```python
# Générer une liste de nombres pairs
pairs = []
for i in range(1, 11):
    if i % 2 == 0:
        pairs.append(i)
```

---

## ⚠️ Erreurs Courantes

### Boucle Infinie
```python
# ❌ MAUVAIS: pas d'actualisation
i = 0
while i < 10:
    print(i)  # Infini!

# ✅ BON
i = 0
while i < 10:
    print(i)
    i += 1
```

### Oublier `range()`
```python
# ❌ MAUVAIS: n est pas itérable
n = 5
for i in n:  # Erreur!
    print(i)

# ✅ BON
for i in range(n):
    print(i)
```

### Index Out of Bounds
```python
# ❌ MAUVAIS
lst = [1, 2, 3]
for i in range(len(lst) + 1):
    print(lst[i])  # Erreur index 3!

# ✅ BON
for i in range(len(lst)):
    print(lst[i])
```

---

## 🧠 Traçage d'Exécution

### Exemple: Afficher 1 à 3
```python
for i in range(1, 4):
    print(i)
```

**Trace:**
```
Itération 1: i = 1 → print(1)
Itération 2: i = 2 → print(2)
Itération 3: i = 3 → print(3)
Fin: range épuisé
```

**Output:**
```
1
2
3
```

---

## 💻 Template de Solution

```python
# Lire l'entrée
n = int(input("Entrez un nombre: "))

# Initialiser
total = 0

# Boucle principale
for i in range(1, n + 1):
    total += i
    print(f"Étape {i}: total = {total}")

# Afficher le résultat
print(f"Résultat final: {total}")
```

---

## 🚀 Progression

1. ✅ **Compléter tous les exercices de Niveau 1**
2. ✅ **Faire au moins 3 exercices de Niveau 2**
3. ✅ **Résoudre les motifs (Niveau 3)**
4. → **Passer à [Les Listes](../les-lists/)**
5. → **Puis [TP03 - Fonctions](../TP03-les-fonctions/)**

---

## 📚 Ressources

- **Python Docs**: [Loops](https://docs.python.org/3/tutorial/controlflow.html)
- **Visualisation**: [PythonTutor - Boucles](https://pythontutor.com/)
- **Pratique**: [CodinGame](https://www.codingame.com/) - Chercher "loops"

---

## 💡 Conseils

- **Tracez sur papier** avant de coder
- **Utilisez des noms significatifs** (i, j pour indices, item pour valeurs)
- **Testez avec des petites valeurs** (n=3 avant n=1000)
- **Comprenez `range()`** c'est la clé!

> **Note**: Consultez le fichier PDF fourni pour les exercices détaillés et spécifiques au cours.
