# 🧪 Chimie - PCSI

Travaux pratiques et travaux dirigés de chimie pour la préparation aux concours des grandes écoles.

---

## 📋 Contenu Pédagogique

### TPs-TDs (Travaux Pratiques & Travaux Dirigés)

Expériences et calculs Python pour maîtriser les concepts fondamentaux :

#### 1. **TP2 - Dosage Acide Fort / Base Fort par pH-métrie**
- **Concept** : Titrage d'une base forte par un acide fort (ou inverse)
- **Méthode** : Suivi du pH pendant l'ajout progressif du titrant
- **Analyse** : Détermination du point d'équivalence, calcul de concentrations
- **Équation** : $n_{acide} = n_{base}$ au point d'équivalence
- **Utilisation Python** : 
  - Calculs stœchiométriques
  - Traçage des courbes de titrage
  - Analyse des données expérimentales

#### 2. **TP3 - Dosage Acide Fort / Base Fort par Conductimétrie**
- **Concept** : Titrage en mesurant la conductivité de la solution
- **Avantage** : Pas besoin d'indicateur coloré, mesure plus objective
- **Principe** : La conductivité varie lors du titrage, présente un point d'inflexion
- **Utilisation Python** :
  - Lissage des données (polynomial fitting)
  - Détermination du point d'équivalence (dérivée)
  - Comparaison avec pH-métrie

#### 3. **TP4 - Degré d'Acidité d'un Vinaigre Commercial**
- **Objectif** : Déterminer la concentration d'acide acétique dans le vinaigre
- **Méthode** : Titrage par une base NaOH standard
- **Applications** : Qualité des produits alimentaires, chimie analytique
- **Calculs** : Concentration molaire → concentration massique (% massique)

#### 4. **TP5 - Dosage d'un Mélange**
- **Défi** : Une solution contient deux acides (ou deux bases) inconnus
- **Stratégie** : Titrage pour déterminer les deux concentrations
- **Mathématiques** : Résolution d'un système de 2 équations à 2 inconnues
- **Exemple** : Mélange HCl + H₂SO₄, trouver [HCl] et [H₂SO₄]

#### 5. **TP6 - Dosage pH-métrique d'un Polyacide par une Base Forte**
- **Spécificité** : Polyacide (ex: H₃PO₄ avec 3 H⁺ libérables)
- **Complexité** : Plusieurs points d'équivalence sur la courbe de titrage
- **Analyse** : Identification des différents pK_a, calcul des concentrations
- **Courbe de titrage** : Plusieurs sauts de pH caractéristiques

---

## 🎯 Objectifs Pédagogiques

✅ **Concepts Fondamentaux**
- Comprendre la stœchiométrie et les bilans de matière
- Maîtriser les calculs de concentrations molaires et massiques
- Analyser les courbes de titrage (point d'équivalence, zones tampons)
- Différencier les méthodes d'analyse (pH-métrie vs conductimétrie)

✅ **Méthodes Expérimentales**
- Technique de titrage (burette, pipette jaugée)
- Utilisation des indicateurs colorés et des capteurs (pH, conductivité)
- Mesure précise et calcul d'incertitudes

✅ **Programmation Python**
- Traitement de données expérimentales
- Visualisation graphique (matplotlib)
- Calculs numériques et algèbre linéaire
- Ajustement de courbes (curve fitting)

---

## 🛠️ Outils et Bibliothèques Python Utilisées

- **numpy** : Calculs numériques et tableaux
- **matplotlib** : Représentation graphique des courbes
- **scipy** : Interpolation, dérivation numérique
- **pandas** : Gestion de données tabulaires

---

## 📝 Structure des Fichiers
```
Chimie/
├── README.md (ce fichier)
└── TPs-TDs/
    ├── TP2-Dosage acide fort_base fort par pH-métrie/
    ├── TP3-Dosage acide fort_base fort par conductimétrie/
    ├── TP4-Degré d'acidité d'un vinaigre commercial/
    ├── TP5-Dosage d'un mélange/
    └── TP6-Dosage pHmétrique d'un polyacide par une base forte/
```

---

## 💡 Conseils pour les Calculs

1. **Point d'équivalence** : Volume du titrant où le nombre de moles ajoutées = nombre de moles initiales
2. **Stœchiométrie** : Beaucoup d'erreurs viennent des coefficients (1:1, 2:1, 3:1...)
3. **Unités** : Toujours vérifier les conversions (mL ↔ L, g ↔ mol)
4. **Incertitudes** : Les erreurs s'accumulent, documenter chaque mesure
- Cinétique chimique
- Équilibres chimiques
- Diagrammes de phases
- Exercices de calculs et résolutions numériques

**Thèmes couverts :**
- Thermochimie
- Cinétique chimique
- Équilibres acido-basiques
- Oxydoréduction
- Atomistique et structure de la matière
- Cristallographie

## 🎯 Compétences Développées

- ✅ Modélisation de réactions chimiques
- ✅ Calculs thermodynamiques
- ✅ Analyse cinétique
- ✅ Visualisation de diagrammes
- ✅ Traitement de données expérimentales

## 📖 Organisation

```
TPs-TDs/
├── TP01-thermochimie/
│   ├── calculs.py
│   └── README.md
├── TD01-cinetique/
│   └── exercices.py
...
```

## 🧪 Modules Utilisés

```bash
pip install numpy matplotlib scipy pandas
```

### Applications typiques :
- Calculs de pH et pKa
- Courbes de titrage
- Diagrammes d'Ellingham
- Cinétique de réactions
- Équilibres chimiques

---

**Dernière mise à jour :** Décembre 2025
