import numpy as np
import matplotlib.pyplot as plt

# --- Données expérimentales ---
Volume_mL = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 
                      5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 
                      11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 
                      15.5, 16.0, 16.5, 17.0])

pH = np.array([1.95, 2.15, 2.32, 2.48, 2.65, 2.80, 2.92, 3.03, 3.14, 3.24, 
               3.34, 3.43, 3.51, 3.58, 3.65, 3.71, 3.77, 3.82, 3.87, 3.91, 
               3.96, 4.10, 4.35, 6.85, 8.70, 9.35, 9.62, 9.82, 9.97, 10.08, 
               10.17, 10.25, 10.31, 10.37, 10.42])

Conductivity_mS_per_cm = np.array([3.60, 3.45, 3.20, 2.90, 2.58, 2.28, 2.02, 
                                   1.80, 1.62, 1.48, 1.37, 1.30, 1.25, 1.22, 
                                   1.20, 1.18, 1.17, 1.16, 1.16, 1.15, 1.15, 
                                   1.15, 1.18, 1.70, 1.92, 2.08, 2.20, 2.30, 
                                   2.42, 2.52, 2.65, 2.76, 2.88, 2.98, 3.08])

# --- Calcul de dpH/dV ---
dpH_dV = np.zeros(len(pH))
for i in range(1, len(pH)):
    dpH_dV[i] = (pH[i] - pH[i-1]) / (Volume_mL[i] - Volume_mL[i-1])

# --- Création de la figure ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Premier subplot : pH et dérivée
ax1_twin = ax1.twinx()
line1 = ax1.plot(Volume_mL, pH, 'b-o', linewidth=2, markersize=4, label='pH')
line2 = ax1_twin.plot(Volume_mL, dpH_dV, 'r-s', linewidth=2, markersize=4, label='dpH/dV', alpha=0.7)

ax1.set_xlabel('Volume de 0.1M NaOH (mL)', fontsize=12)
ax1.set_ylabel('pH', fontsize=12, color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1_twin.set_ylabel('dpH/dV', fontsize=12, color='r')
ax1_twin.tick_params(axis='y', labelcolor='r')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 18)
ax1.set_ylim(0, 12)
ax1_twin.set_ylim(0, max(dpH_dV) * 1.2)

# Légende combinée
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')
ax1.set_title('pH and dpH/dV vs Volume of NaOH', fontsize=14, fontweight='bold')

# Second subplot : Conductivité
ax2.plot(Volume_mL, Conductivity_mS_per_cm, 'g-o', linewidth=2, markersize=4)
ax2.set_xlabel('Volume de 0.1M NaOH (mL)', fontsize=12)
ax2.set_ylabel('Conductivity σ (mS/cm)', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 18)
ax2.set_ylim(0, max(Conductivity_mS_per_cm) * 1.2)
ax2.set_title('Conductivity vs Volume of NaOH', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# --- Analyse du point d'équivalence ---
equiv_point_idx = np.argmax(dpH_dV)
print("Equivalence Point Analysis:")
print(f"Volume at equivalence point: {Volume_mL[equiv_point_idx]:.1f} mL")
print(f"pH at equivalence point: {pH[equiv_point_idx]:.2f}")
