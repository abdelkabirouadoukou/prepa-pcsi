import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === Données expérimentales ===
V = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 
              8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5])

pH = np.array([2.50, 3.15, 3.46, 3.69, 3.88, 4.08, 4.24, 4.43, 4.65, 4.95, 5.25, 9.80, 10.23, 
               10.58, 11.08, 11.24, 11.37, 11.47, 11.58, 11.63, 11.68, 11.71, 11.76, 
               11.80, 11.82, 11.86, 11.88, 11.93, 11.95, 11.97, 12.01])

sigma = np.array([1.25, 1.10, 0.95, 0.82, 0.70, 0.60, 0.52, 0.45, 0.40, 0.36, 0.33, 0.31, 
                  0.30, 0.33, 0.40, 0.50, 0.63, 0.78, 0.95, 1.10, 1.25, 1.35, 1.42, 1.48, 
                  1.53, 1.57, 1.60, 1.62, 1.64, 1.65, 1.66])

# === Calcul de la dérivée numérique dpH/dV ===
dpH_dV = np.gradient(pH, V)

# === Graphique combiné pH et dpH/dV ===
fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.plot(V, pH, 'o-', color='blue', label='pH = f(V)')
ax1.set_xlabel('Volume de NaOH ajouté (mL)')
ax1.set_ylabel('pH', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(V, dpH_dV, 'o--', color='green', label='dpH/dV')
ax2.set_ylabel('dpH/dV (pH/mL)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

plt.title('Dosage du vinaigre : pH et dérivée dpH/dV')
plt.tight_layout()
plt.show()

# === Graphique de la conductivité ===
plt.figure(figsize=(8, 5))
plt.plot(V, sigma, 'o-', color='orange')
plt.xlabel('Volume de NaOH ajouté (mL)')
plt.ylabel('Conductivité (mS/cm)')
plt.title('Variation de la conductivité pendant le dosage')
plt.grid(True)
plt.tight_layout()
plt.show()

# === Volume d'équivalence (max du dpH/dV) ===
Ve = V[np.argmax(dpH_dV)]
print(f"Volume d'équivalence estimé = {Ve:.2f} mL")

# === Export CSV (facultatif) ===
df = pd.DataFrame({
    'V (mL)': V,
    'pH': np.round(pH, 2),
    'sigma (mS/cm)': np.round(sigma, 2),
    'dpH/dV': np.round(dpH_dV, 3)
})

# df.to_csv('TP4_vinaigre_real_data.csv', index=False)
print(df.head())
