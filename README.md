# 📚 Préparation PCSI - Ressources Complètes

> Compilations de tous les travaux pratiques, travaux dirigés, révisions et ressources pour la préparation aux concours des grandes écoles PCSI (Physique, Chimie, Sciences Industrielles)

---

## 📋 Navigation Rapide

| Domaine | Contenu | Statut |
|---------|---------|--------|
| 💻 **[Informatique](./Informatique/)** | TPs, TDs, Algorithmes, AI | ✅ Complet |
| 🧪 **[Chimie](./Chimie/)** | TPs/TDs Dosage & Analyses | ✅ En cours |
| 📐 **[Mathématiques](./Mathematiques/)** | Exercices & Révisions | 📝 À completer |
| ⚛️ **[Physique](./Physique/)** | Projectiles, Filtrage, Mesures | ✅ En cours |
| 🔧 **[Sciences Ingénieur](./Sciences-Ingenieur/)** | Modélisation, Liaisons | 📝 À completer |
| 🧮 **[Algorithmes Généraux](./Algorithmes-General/)** | PGCD, Problem Solving | ✅ En cours |

---

## 🏗️ Structure du Projet

```
prepa-pcsi/
├── README.md (ce fichier)
├── index.html (vue d'ensemble)
│
├── 💻 Informatique/
│   ├── README.md (guide complet)
│   ├── ai/ (Algorithmes avancés)
│   ├── chapitres/ (Cours)
│   ├── Revisions/ (Devoirs Surveillés)
│   └── TPs-TDs/ (Travaux Pratiques)
│
├── 🧪 Chimie/
│   ├── README.md
│   └── TPs-TDs/ (Dosages, Analyses)
│
├── ⚛️ Physique/
│   ├── README.md
│   ├── projectile/ (Trajectoires)
│   └── TPs-TDs/ (Filtrage, Mesures)
│
├── 📐 Mathématiques/
│   ├── README.md
│   └── TPs-TDs/
│
├── 🔧 Sciences-Ingenieur/
│   ├── README.md
│   └── TPs-TDs/ (CAO, Modélisation)
│
├── 🧮 Algorithmes-General/
│   ├── README.md
│   ├── pgcd/ (Algorithmes classiques)
│   └── Problem-Solving/ (Exercices)
│
└── .assets/ (ressources partagées)
```

---

## 🎯 Guide d'Utilisation

### Par Domaine

#### 💻 Informatique (Priorité Haute)
Le cœur du cursus PCSI - Python, Algorithmes, Structures de Données

**Progression recommandée:**
1. [TP01 - Bases](./Informatique/TPs-TDs/TP01-exercices-base/) (Variables, Opérateurs)
2. [Contrôle de Flux](./Informatique/TPs-TDs/les-boucles/) (Boucles, Conditions)
3. [Listes et Données](./Informatique/TPs-TDs/les-lists/) (Structures)
4. [TP03 - Fonctions](./Informatique/TPs-TDs/TP03-les-fonctions/) (Récursion)
5. [TD - Tris](./Informatique/TPs-TDs/TD-les-tris/) (Complexité)
6. [Algorithmes Avancés](./Informatique/ai/) (A*, Minimax, Gradient)

#### 🧪 Chimie (Pratique Expérimentale)
TPs de dosage et analyses chimiques
- TP2: Dosage acide-base (pH-métrie)
- TP3: Dosage acide-base (Conductimétrie)
- TP4: Acidité du vinaigre
- TP5: Dosage de mélanges
- TP6: Poly-acides

#### ⚛️ Physique (Mécanique & Électronique)
- Projectiles et trajectoires
- Filtrage et amplification
- Mesures et incertitudes

#### 🔧 Sciences Ingénieur
Modélisation et conception avec CAO

---

## 🚀 Démarrage Rapide

### Installation
```bash
# Cloner le repo
git clone <repo-url>
cd prepa-pcsi

# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement
# Sur Windows:
.venv\Scripts\activate
# Sur Linux/Mac:
source .venv/bin/activate

# Installer les dépendances (si nécessaire)
pip install -r requirements.txt
```

### Exécuter un Exercice
```bash
# Aller au dossier de l'exercice
cd Informatique/TPs-TDs/TP01-exercices-base/conversion-de-temperature

# Exécuter
python main.py
```

---

## 📊 Statistiques du Projet

- **Total TPs/TDs**: 15+
- **Exercices Programmation**: 50+
- **Algorithmes Documentés**: 20+
- **Couverture**: Informatique, Chimie, Physique, Maths, Sciences Ingénieur

---

## 💡 Conseils de Travail

### Méthodologie Générale
1. 📖 **Lire** attentivement le sujet (2 fois)
2. 🎯 **Identifier** entrées/sorties et cas limites
3. 🖊️ **Dessiner** l'approche avant de coder
4. 💻 **Coder** par petites étapes testables
5. 🔍 **Vérifier** tous les cas possibles
6. 🚀 **Optimiser** et refactoriser

### Pour les Algorithmes
- Commencer par une solution brute (O(n²) acceptable)
- Analyser la complexité théorique
- Rechercher des patterns à optimiser
- Comparer avec des solutions de référence

### Pour les TPs Chimie
- Noter les observations expérimentales
- Tracer les courbes de titrage
- Calculer les incertitudes
- Vérifier les résultats par deux méthodes

---

## 🔗 Ressources Externes

| Ressource | Utilité | Lien |
|-----------|---------|------|
| Python Official | Référence Officielle | python.org/3/ |
| VisuAlgo | Visualisation d'Algos | visualgo.net |
| PythonTutor | Trace d'Exécution | pythontutor.com |
| CodinGame | Exercices Interactifs | codingame.com |
| LeetCode | Algorithmes & Structures | leetcode.com |

---

## 📝 Convention de Nommage

- **Dossiers**: `kebab-case` (ex: `TD-les-tris`)
- **Fichiers Python**: `snake_case` ou `main.py` (ex: `solution.py`, `main.py`)
- **README**: Un par dossier TP/TD principal
- **Commentaires**: Français avec clarté

---

## 🎓 Progression Type PCSI (48 semaines)

| Période | Informatique | Chimie | Physique | Maths |
|---------|--------------|--------|----------|-------|
| Trim 1 | Bases → Fonctions | Titrage | Mécanique | Analyse |
| Trim 2 | Structures → Tri | Dosage | Électronique | Algèbre |
| Trim 3 | Algorithmes | Synthèse | Thermique | Géométrie |

---

## ✨ Comment Contribuer

1. Ajouter un nouvel exercice → Créer dossier dans le TP approprié
2. Compléter un exercice → Implémenter `main.py` + `README.md`
3. Ajouter une ressource → Placer dans `.assets/`
4. Corriger une erreur → Faire une PR avec explication

---

## 📧 Questions / Support

- Consulter les README de chaque domaine
- Vérifier les solutions dans les fichiers `main.py`
- Analyser les traces d'exécution avec PythonTutor

---

**Dernière mise à jour**: Avril 2026  
**Auteur**: Abdelkabir  
**Licence**: MIT (libre d'utilisation personnelle)

> 🎯 **Objectif**: Maîtriser les fondamentaux et développer une pensée algorithmique forte pour réussir les concours PCSI!