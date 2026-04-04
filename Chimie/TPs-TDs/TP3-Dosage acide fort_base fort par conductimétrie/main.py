import matplotlib.pyplot as plt

# === Données expérimentales corrigées ===
V = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 
     5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]

sigma = [3.40, 3.05, 2.75, 2.50, 2.30, 2.10, 1.90, 1.75, 1.65, 1.55, 
         1.45, 1.38, 1.32, 1.28, 1.25, 1.23, 1.22, 1.23, 1.27, 1.35, 1.45]

# Dérivée dsigma/dV (mS/cm/mL)
dsigma_dV = [-0.70, -0.65, -0.55, -0.45, -0.40, -0.40, -0.35, -0.25, -0.20, -0.20, 
             -0.17, -0.13, -0.10, -0.07, -0.05, -0.02, 0.00, 0.02, 0.08, 0.16, 0.20]

# === Création du graphique ===
fig, ax1 = plt.subplots(figsize=(8, 6))

# --- Courbe de la conductivité
ax1.plot(V, sigma, 'o-', color='blue', label='Conductivité σ (mS/cm)')
ax1.set_xlabel('Volume de NaOH ajouté (mL)')
ax1.set_ylabel('Conductivité σ (mS/cm)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.axvline(8.0, color='red', linestyle='--', label='Équivalence = 8 mL')

# --- Deuxième axe Y pour la dérivée
ax2 = ax1.twinx()
ax2.plot(V, dsigma_dV, 's--', color='green', label='Dérivée dσ/dV')
ax2.set_ylabel('dσ/dV (mS/cm/mL)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# --- Titre et légendes
plt.title("Dosage conductimétrique HCl / NaOH - σ(V) et sa dérivée")
fig.legend(loc="upper right", bbox_to_anchor=(0.85, 0.9))
ax1.grid(True)

plt.show()
