# ⚛️ Physique - PCSI

> Travaux pratiques et travaux dirigés de physique pour la préparation aux concours PCSI. Mécanique, électronique, thermique.

---

## 📋 Navigation Rapide

| Sujet | Contenu | Niveau |
|-------|---------|--------|
| **Projectiles** | Trajectoires, portée, temps de vol | ⭐ |
| **Filtrage & Ampli** | Filtres RC, opérateurs, Bode | ⭐⭐ |
| **Mesures** | Incertitudes, Monte Carlo | ⭐⭐ |

---

## 📋 Contenu Pédagogique

### 1️⃣ **Projectile** (`projectile/`)

#### 🎯 Objectif
Simuler et analyser le mouvement d'un projectile sous l'effet de la gravité.

#### 📖 Théorie
Mouvements 2D en présence de la gravité :
- **Équations du mouvement** :
  - $x(t) = x_0 + v_{0x} \cdot t$
  - $y(t) = y_0 + v_{0y} \cdot t - \frac{1}{2}g t^2$
- **Vitesses** :
  - $v_x(t) = v_{0x}$ (constant)
  - $v_y(t) = v_{0y} - g \cdot t$ (décroissant)

#### 🔍 Ce que vous ferez
1. Entrer conditions initiales (position, vitesse, angle)
2. Calculer la trajectoire (liste de points)
3. Tracer la parabole
4. Déterminer :
   - **Portée** : Distance horizontale maximale
   - **Hauteur maximale** : Altitude atteinte
   - **Temps de vol** : Quand le projectile touche le sol
5. Analyser l'influence de l'angle de tir sur la trajectoire

#### 📊 Extensions possibles
- Ajouter la résistance de l'air (frottement proportionnel à v²)
- Mouvement en 3D
- Impact sur un plan incliné

---

### 2. **TPs-TDs Avancés**

#### **TP - Filtrage et Amplificateur Opérationnel**

**Concepts Abordés** :
- Circuits passifs et actifs
- Réponse fréquentielle (basses fréquences, hautes fréquences)
- Bande passante et atténuation
- Utilisation de filtres en électronique

**Fichiers** :
- **Analyse spectral.py** : Décomposition d'un signal en ses composantes fréquentielles (transformée de Fourier)
- **Filtrage selectif.py** : Application de filtres pour isoler certaines bandes de fréquences
- **Fonction de transfert selectif.py** : Analyse mathématique des filtres (gain, phase)

**Utilisation Python** :
```python
import numpy as np
import matplotlib.pyplot as plt
# Générer un signal
# Appliquer une transformée de Fourier
# Afficher le spectre de fréquences
# Appliquer un filtre passe-bas ou passe-haut
```

---

#### **TP - Mesure et Incertitude**

**Objectif** : Comprendre et quantifier les erreurs expérimentales.

**Fichier** : **Incertitude Monte Carlo.py**

**Concept** :
Lorsqu'on mesure une grandeur physique, on a une incertitude sur chaque mesure.
Comment cette incertitude se propage dans les calculs ?

**Méthode Monte Carlo** :
1. Générer N valeurs aléatoires suivant une distribution normale autour de chaque mesure
2. Calculer le résultat final N fois
3. Analyser la distribution des résultats (moyenne, écart-type)
4. L'écart-type est l'incertitude sur le résultat

**Exemple** :
```
Si on mesure R = 100 Ω ± 1 Ω
Et on calcule P = V²/R avec V = 10 V
Quelle est l'incertitude sur P ?
→ Générer 10000 valeurs de R aléatoires
→ Calculer P pour chaque valeur
→ Trouver σ(P)
```

---

## 🎯 Objectifs Pédagogiques

✅ **Modélisation Physique**
- Traduire des lois physiques en équations mathématiques
- Résoudre des équations différentielles (analytiquement ou numériquement)
- Simuler des phénomènes réels

✅ **Traitement de Données**
- Acquisition et visualisation de données
- Analyse fréquentielle (transformée de Fourier)
- Propagation d'erreurs et incertitudes

✅ **Programmation Scientifique**
- Simulation numérique
- Représentation graphique
- Optimisation et paramétrage

---

## 📚 Bibliothèques Principales

- **numpy** : Calculs numériques, tableaux, résolution d'équations
- **matplotlib** : Visualisation (courbes, histogrammes, spectres)
- **scipy** : Transformée de Fourier, résolution d'EDO, interpolation

---

## 🛠️ Structure des Fichiers
```
Physique/
├── README.md (ce fichier)
├── projectile/
│   ├── projectile.py
│   └── requirements.txt
└── TPs-TDs/
    ├── TP-filtrage-amplificateur-operationelle/
    │   ├── Analyse spectral.py
    │   ├── Filtrage selectif.py
    │   └── Fonction de transfert selectif.py
    └── TP-mesure-et-incertitude/
        └── Incertutude Monte Carlo.py
```

---

## 💡 Conseils Pratiques

1. **Projectile** : Visualisez toujours la trajectoire pour vérifier que ça a du sens physique
2. **Fourier** : Une image vaut mille mots → toujours tracer l'avant/après filtrage
3. **Incertitudes** : Monte Carlo est puissant mais lent (N grand = plus précis mais plus long)
- Analyse de données expérimentales
- Traitement de signaux
- Résolution numérique d'équations physiques
- Exercices de résolution et calculs numériques

**Thèmes couverts :**
- Mécanique (cinématique, dynamique, énergétique)
- Électromagnétisme
- Thermodynamique
- Optique
- Ondes et vibrations

## 🎯 Compétences Développées

- ✅ Modélisation de phénomènes physiques
- ✅ Simulation numérique
- ✅ Analyse et visualisation de données
- ✅ Résolution d'équations différentielles
- ✅ Traitement du signal

## 📖 Organisation

```
TPs-TDs/
├── TP01-nom-descriptif/
│   ├── simulation.py
│   ├── data/
│   └── README.md
├── TD01-nom-descriptif/
│   └── exercices.py
...
```

## 🧪 Modules Utilisés

```bash
pip install numpy matplotlib scipy pandas
```

### Modules courants :
- `numpy` : Calculs numériques
- `matplotlib` : Visualisation
- `scipy` : Intégration, optimisation, équations différentielles
- `pandas` : Analyse de données expérimentales

---

**Dernière mise à jour :** Décembre 2025
