import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# TABLE A - COCA-COLA (theoretical smooth values)
# =============================================================================
V_coke = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 
                   6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10], dtype=float)

pH_coke = np.array([2.20, 2.28, 2.35, 2.50, 2.70, 3.00, 3.40, 4.20, 5.00, 
                    6.80, 7.05, 7.30, 7.60, 8.10, 8.50, 8.90, 9.20, 9.55, 
                    9.90, 10.20, 10.50])

dph_coke = np.gradient(pH_coke, V_coke)

# =============================================================================
# TABLE B - PURE PHOSPHORIC ACID
# =============================================================================
V_h3po4 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 
                    6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10], dtype=float)

pH_h3po4 = np.array([1.50, 1.60, 1.70, 1.85, 2.05, 2.35, 2.75, 3.40, 4.20, 
                     6.80, 7.05, 7.40, 7.95, 8.55, 9.30, 10.10, 11.10, 
                     11.60, 11.90, 12.05, 12.12])

dph_h3po4 = np.gradient(pH_h3po4, V_h3po4)

# =============================================================================
# FIGURE 1 - COCA-COLA
# =============================================================================
plt.figure(figsize=(10, 5))
plt.plot(V_coke, pH_coke, 'o-', label="pH (Coca-Cola)")
plt.plot(V_coke, dph_coke, 'o-', label="d(pH)/dV (Coca-Cola)")
plt.xlabel("Volume NaOH ajouté (mL)")
plt.ylabel("Grandeurs")
plt.title("Dosage pHmétrique - Coca-Cola")
plt.grid(True)
plt.legend()
plt.show()

# =============================================================================
# FIGURE 2 - PHOSPHORIC ACID
# =============================================================================
plt.figure(figsize=(10, 5))
plt.plot(V_h3po4, pH_h3po4, 'o-', label="pH (H₃PO₄)")
plt.plot(V_h3po4, dph_h3po4, 'o-', label="d(pH)/dV (H₃PO₄)")
plt.xlabel("Volume NaOH ajouté (mL)")
plt.ylabel("Grandeurs")
plt.title("Dosage pHmétrique - Acide Phosphorique Pur")
plt.grid(True)
plt.legend()
plt.show()
