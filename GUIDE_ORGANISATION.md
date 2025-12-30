# 🎯 Guide d'Organisation - Prépa PCSI

Ce guide vous aide à organiser efficacement vos TPs, TDs et problèmes dans ce repository.

---

## 📁 Structure Recommandée

### Pour chaque nouveau TP/TD :

```
Matiere/TPs-TDs/TPxx-nom-descriptif/
├── main.py              # Code principal
├── README.md            # Documentation
├── data/                # Données (optionnel)
├── results/             # Résultats (optionnel)
└── tests.py             # Tests (optionnel)
```

---

## 🆕 Créer un Nouveau TP/TD

### Étape 1 : Identifier la matière
Choisir le bon dossier :
- `Mathematiques/` pour les maths
- `Physique/` pour la physique
- `Chimie/` pour la chimie
- `Informatique/` pour l'informatique
- `Sciences-Ingenieur/` pour SI

### Étape 2 : Choisir le type
- `TPs-TDs/` pour les Travaux Pratiques et Travaux Dirigés
- `Problemes/` pour les problèmes complexes

### Étape 3 : Nommer le dossier
**Convention :** `TPxx-nom-descriptif` ou `TDxx-nom-descriptif`

**Exemples :**
- ✅ `TP01-equations-differentielles`
- ✅ `TD03-cinematique-point-materiel`
- ✅ `TP05-equilibres-chimiques`
- ❌ `tp1` (trop vague)
- ❌ `nouveau_tp` (pas de numéro)

### Étape 4 : Copier les templates
```bash
# Copier le README template
cp .templates/TEMPLATE_TP_TD.md Matiere/TPs/TPxx-nom/README.md

# Copier le template Python
cp .templates/template_main.py Matiere/TPs/TPxx-nom/main.py
```

### Étape 5 : Personnaliser
1. Remplir le README avec l'énoncé
2. Adapter le code Python
3. Ajouter vos fonctions
4. Documenter votre travail

---

## 📝 Convention de Nommage

### Dossiers
- **Minuscules** avec **tirets** : `tp01-nom-descriptif`
- **Numérotation** : TP01, TP02, ... TP10, TP11, ...
- **Nom descriptif** : explicite sur le contenu

### Fichiers Python
- `main.py` : Programme principal
- `utils.py` : Fonctions utilitaires
- `tests.py` : Tests unitaires
- `config.py` : Configuration (constantes)

### Fonctions
- **snake_case** : `calculer_moyenne()`, `afficher_resultats()`
- **Verbes à l'infinitif** : `calculer`, `afficher`, `resoudre`

---

## 📖 Documentation

### Dans le README :
```markdown
# TP01 - Titre Explicite

> **Date :** XX/XX/2025  
> **Matière :** [Matière]  
> **Thème :** [Thème]

## Énoncé
[Énoncé complet]

## Utilisation
\```bash
python main.py
\```

## Résultats
[Résultats attendus]
```

### Dans le code Python :
```python
def ma_fonction(param1: float, param2: str) -> bool:
    """
    Description courte.
    
    Args:
        param1: Description du paramètre 1
        param2: Description du paramètre 2
    
    Returns:
        Description du retour
        
    Examples:
        >>> ma_fonction(3.14, "test")
        True
    """
    pass
```

---

## 🔄 Workflow Recommandé

### Pour un nouveau TP :

1. **Lire l'énoncé** 📖
   - Comprendre les objectifs
   - Identifier les compétences

2. **Créer la structure** 📁
   ```bash
   mkdir -p Matiere/TPs-TDs/TPxx-nom
   cd Matiere/TPs-TDs/TPxx-nom
   ```

3. **Copier les templates** 📄
   ```bash
   cp ../../.templates/TEMPLATE_TP_TD.md README.md
   cp ../../.templates/template_main.py main.py
   ```

4. **Développer** 💻
   - Écrire le code
   - Tester régulièrement
   - Documenter au fur et à mesure

5. **Valider** ✅
   - Vérifier les résultats
   - Relire le code
   - Compléter la documentation

6. **Commit** 🚀
   ```bash
   git add .
   git commit -m "Ajout TPxx: nom descriptif"
   git push
   ```

---

## 🎨 Bonnes Pratiques

### Code
- ✅ Noms de variables explicites : `temperature_celsius`, `vitesse_ms`
- ✅ Commentaires pour les parties complexes
- ✅ Constantes en MAJUSCULES : `GRAVITE = 9.81`
- ✅ Fonctions courtes et focalisées
- ❌ Variables à une lettre (sauf i, j pour boucles)

### Organisation
- ✅ Un dossier par TP/TD
- ✅ README pour chaque TP
- ✅ Séparer données et code
- ✅ Garder les versions qui fonctionnent
- ❌ Mélanger plusieurs TPs dans un dossier

### Révisions
- ✅ Dossier `Revisions/` pour les DS
- ✅ Exercices types par thème
- ✅ Corrections détaillées
- ✅ Notes sur erreurs courantes

---

## 📦 Dépendances Communes

### Installation globale
```bash
pip install numpy matplotlib scipy pandas sympy
```

### Pour SI spécifiquement
```bash
pip install control-python
```

### Pour notebooks (optionnel)
```bash
pip install jupyter notebook
```

---

## 🔗 Ressources

- **Templates** : `.templates/`
- **Exemples** : Voir les TPs existants
- **Documentation Python** : https://docs.python.org/fr/3/
- **NumPy** : https://numpy.org/doc/
- **Matplotlib** : https://matplotlib.org/

---

## 💡 Astuces

### Trouver un ancien TP
```bash
# Rechercher par mot-clé
grep -r "mot-clé" Mathematiques/TPs-TDs/

# Lister tous les TPs
ls -d */TPs-TDs/TP*
```

### Sauvegarder son travail
```bash
# Commit réguliers
git add .
git commit -m "TP05: Ajout calcul matriciel"

# Backup important
git push origin main
```

### Réutiliser du code
Créer `utils.py` pour fonctions réutilisables :
```python
# Dans utils.py
def fonction_commune():
    pass

# Dans main.py
from utils import fonction_commune
```

---

## ❓ FAQ

**Q : Où mettre un TP qui combine plusieurs matières ?**  
R : Dans la matière principale, mentionner dans le README les autres matières.

**Q : Comment organiser les révisions de DS ?**  
R : Mettre dans `Informatique/Revisions/` pour l'informatique.

**Q : Où mettre des exercices LeetCode/HackerRank ?**  
R : Dans `Algorithmes-General/Problem-Solving/`.

---

**Dernière mise à jour :** Décembre 2025  
**Maintenu par :** Abdelkabir
