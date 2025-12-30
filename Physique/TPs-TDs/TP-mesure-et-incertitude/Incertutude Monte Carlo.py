# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:32:04 2025

@author: User
"""

#Activité numérique : simuler, à l’aide d’un langage de programmation ou d’un tableur,
#                     un processus aléatoire de variation des valeurs expérimentales de 
#                        l’une des grandeurs – simulation Monte-Carlo – pour évaluer
#                            l’incertitude sur les paramètres du modèle.



#Exe : Supposons qu’on mesure une concentration [H⁺] plusieurs fois avec une incertitude 
#      sur la mesure (ex : ±5%).
#On veut estimer le pH moyen et son écart type via Monte Carlo.


import numpy as np
import matplotlib.pyplot as plt

# Paramètre : vraie concentration en H+ (mol/L)
true_concentration = 1e-4  # correspond à pH = 4

# Nombre de simulations Monte Carlo
N = 1000000

# Incertitude relative (5 % ici)
relative_uncertainty = 0.05

# Générer N mesures bruitées de [H+]
np.random.seed(0)  # pour reproductibilité
simulated_concentrations = np.random.normal(
    loc=true_concentration,
    scale=relative_uncertainty * true_concentration,
    size=N
)

# Éliminer les valeurs négatives (non physiques)
simulated_concentrations = simulated_concentrations[simulated_concentrations > 0]

# Calcul des pH simulés
simulated_pH = -np.log10(simulated_concentrations)

# Analyse statistique
mean_pH = np.mean(simulated_pH)
std_pH = np.std(simulated_pH)

print(f"pH moyen : {mean_pH:.3f}")
print(f"Incertitude (écart type) sur pH : ±{std_pH:.3f}")

# Affichage des résultats
plt.hist(simulated_pH, bins=50, color='skyblue', edgecolor='black')
plt.axvline(mean_pH, color='red', linestyle='dashed', label=f'pH moyen = {mean_pH:.2f}')
plt.title('Distribution du pH simulé (Méthode de Monte Carlo)')
plt.xlabel('pH')
plt.ylabel('Fréquence')
plt.legend()
plt.grid(True)
plt.show()
