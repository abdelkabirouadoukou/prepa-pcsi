# ⚙️ Sciences de l'Ingénieur (SI) - PCSI

Travaux pratiques et travaux dirigés de sciences de l'ingénieur pour maîtriser la modélisation, l'analyse et la conception de systèmes mécaniques et automatisés.

---

## 📚 Contenu Pédagogique

### TPs-TDs (Travaux Pratiques & Travaux Dirigés)

Exercices pratiques et simulations pour comprendre les systèmes techniques :

---

## 🎯 Thèmes Principaux

### 1. **Modélisation des Liaisons Mécaniques**

#### 📌 Objectif
Comprendre les différents types de liaisons entre pièces mécaniques et leurs propriétés cinématiques.

#### 🔧 Types de Liaisons Étudiées

| Liaison | Symbole | DDL | Blocages | Applications |
|---------|---------|-----|----------|-----|
| **Pivot** | Charnière | 1 (rotation) | 5 | Portes, engrenages |
| **Glissière** | Rail | 1 (translation) | 5 | Seringues, tiroirs |
| **Pivot Glissant** | - | 2 (rotation + translation dans même axe) | 4 | Cylindre, alésage |
| **Appui Plan** | Surface plane | 3 (2 transl. + 1 rot.) | 3 | Table sur sol |
| **Linéaire Rectiligne** | Ressort guidé | 2 | 4 | Rails de guidage |
| **Linéaire Annulaire** | Bague sur axe | 4 (3 rot. + 1 transl. axiale) | 2 | Joints universels |
| **Ponctuelle** | Bille dans cavité | 5 | 1 | Roulements |
| **Hélicoïdale** | Hélice | 1 (rotation ↔ translation) | 5 | Vis-écrou |

#### 📖 Concepts Clés

**Degrés de Liberté (DDL)** :
- Translation : 3 axes (X, Y, Z)
- Rotation : 3 axes (Rx, Ry, Rz)
- Total : 6 DDL max pour un solide en 3D

**Analyse des Liaisons** :
1. Identifier chaque liaison
2. Compter les DDL (ce qui peut bouger)
3. Compter les blocages (ce qui ne peut pas bouger)
4. Vérifier : DDL + blocages = 6

#### 🎬 Fichiers d'Apprentissage
```
TP03-modélisation-des-liaisons/
├── Modélisation des liaisons-anim.htm
├── Liaisons animations/
│   ├── PIVOT.SWF
│   ├── GLISSIERE.SWF
│   ├── PIVOT GLISSANT.SWF
│   ├── APPUI PLAN.SWF
│   ├── LINER ECTILIGNE.SWF
│   ├── LINER ANNULAIRE.SWF
│   ├── HELICOIDALE.SWF
│   └── PONCTUELLE.SWF
└── Images - Raccourci.lnk
```

#### 💡 Activités Pratiques

1. **Identification** : Donné un système, identifier toutes les liaisons
2. **Modélisation** : Dessiner le schéma cinématique
3. **Calcul DDL** : Vérifier le fonctionnement cinématique
4. **Conception** : Proposer des liaisons pour une application donnée

---

### 2. **Mécanismes et Cinématique**

#### Concepts Abordés

- **Mécanismes plans/spatiaux** : Analyse des mouvements
- **Chaîne cinématique fermée** : Boucles fermées de liaisons
- **Mobilité** : Nombre de paramètres indépendants pour décrire l'état du système
  - Formule de Grübler : $m = 6(n-1) - \sum_{i=1}^{J} (6-f_i)$
    - n = nombre de pièces
    - J = nombre de liaisons
    - f_i = DDL de la liaison i

#### Applications Pratiques

- Mécanismes à 4 barres (système de manivelle-bielle)
- Moteurs à piston
- Robots industriels
- Suspensions automobiles

---

### 3. **Automatique et Asservissement** (optionnel avancé)

#### Concepts de Base

- **Systèmes de contrôle** : Feedback, boucle fermée
- **Fonction de transfert** : Modèle dynamique d'un système
- **Régulateurs** : PID (Proportionnel-Intégral-Dérivé)
- **Stabilité** : Critères de Routh, diagramme de Bode

#### Cas d'Étude

- Asservissement de vitesse d'un moteur
- Régulation de température
- Pilote automatique
- Robots collaboratifs

---

## 🎓 Objectifs Pédagogiques

✅ **Modélisation Mécanique**
- Identifier et classifier les liaisons
- Compter les degrés de liberté
- Tracer des schémas cinématiques normalisés
- Analyser la mobilité d'un mécanisme

✅ **Analyse Cinématique**
- Résoudre des problèmes de vitesses et accélérations
- Utiliser les méthodes graphiques et analytiques
- Comprendre les singularités cinématiques

✅ **Conception**
- Choisir les bonnes liaisons selon les contraintes
- Dimensionner les organes de transmission
- Vérifier la faisabilité mécanique

✅ **Simulation Numérique**
- Utiliser les logiciels CAO (SolidWorks, Fusion 360)
- Analyser les simulations cinématiques
- Interpréter les résultats

---

## 📊 Structure des Fichiers

```
Sciences-Ingenieur/
├── README.md (ce fichier)
└── TPs-TDs/
    └── TP03-modélisation-des-liaisons/
        ├── Modélisation des liaisons-anim.htm
        ├── Liaisons animations/
        │   ├── *.SWF (fichiers Flash animés)
        │   └── Images/
        └── Modélisation des liaisons-anim_fichiers/
```

---

## 🛠️ Outils Utilisés

- **Schémas normalisés ISO** : Représentation universelle
- **Logiciels CAO** : SolidWorks, Fusion 360, FreeCAD
- **Simulations** : ADAMS, Abaqus (niveau supérieur)
- **Vidéos pédagogiques** : Animations Flash pour visualiser

---

## 💡 Conseils de Travail

### Pour Maîtriser les Liaisons

1. **Visualiser** : Regarder les animations (+plusieurs fois)
2. **Manipuler** : Avec des objets réels (boîtes, cahiers, balle)
3. **Dessiner** : Schémas cinématiques à la main d'abord
4. **Vérifier** : DDL + blocages = 6 toujours

### Pièges à Éviter

- ❌ Confondre "pivot" et "pivot glissant"
- ❌ Oublier de compter les rotations dans les blocages
- ❌ Croire qu'une liaison "appui plan" permet 4 DDL (c'est 3 !)
- ❌ Négliger les pièces intermédiaires dans la modélisation

### Vérification d'un Schéma

```
Pour chaque liaison :
- Vérifier le symbole ✓
- Compter ses DDL ✓
- Vérifier ses blocages ✓
- Total DDL du système cohérent ? ✓
```

---

## 📚 Pour Progresser

- **Schémas cinématiques** : S'entraîner régulièrement
- **Mécanismes réels** : Observer autour de soi (portes, tiroirs, vélos)
- **Projets P8X** : Appliquer sur du matériel réel
- **Norme ISO 1219** : Symbolique standard en mécanique
- Analyse de systèmes dynamiques
- Traitement du signal
- Robotique et mécatronique
- Exercices d'analyse et de conception de systèmes

**Thèmes couverts :**
- Cinématique et statique
- Dynamique des systèmes
- Automatique (PID, boucles fermées)
- Analyse fréquentielle
- Modélisation multi-physique
- Systèmes embarqués

## 🎯 Compétences Développées

- ✅ Modélisation de systèmes multi-corps
- ✅ Simulation dynamique
- ✅ Analyse de performances
- ✅ Conception d'asservissements
- ✅ Traitement de données capteurs

## 📖 Organisation

```
TPs-TDs/
├── TP01-cinematique/
│   ├── simulation.py
│   ├── models/
│   └── README.md
├── TD01-statique/
│   └── exercices.py
...
```

## 🔧 Modules Utilisés

```bash
pip install numpy matplotlib scipy control-python
```

### Modules spécifiques :
- `numpy` : Calculs matriciels et numériques
- `matplotlib` : Visualisation (diagrammes de Bode, Nyquist)
- `scipy` : Analyse de systèmes dynamiques
- `control` : Théorie du contrôle et automatique
- `sympy` : Calculs symboliques

## 🤖 Applications Typiques

- Analyse de stabilité de systèmes asservis
- Diagrammes de Bode et Black
- Simulation de trajectoires
- Calculs de torseurs
- Modélisation CAO/simulation

---

**Dernière mise à jour :** Décembre 2025
