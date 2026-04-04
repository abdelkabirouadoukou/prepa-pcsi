import math
import scipy.constants
import matplotlib.pyplot as plt

G   = scipy.constants.g
RHO = 1.225
CD  = 0.47
A   = 0.007854


def get_input():
    print("=============================================")
    print("SIMULATION DE PROJECTILE — Paramètres")
    print("=============================================")
    vitesse_initiale_v0 = float(input("Vitesse Initiale v0 (m/s): "))
    angle_theta         = float(input("Angle Theta (degrés): "))
    masse_m             = float(input("Masse m (kg): "))
    print(f"v0 = {vitesse_initiale_v0} |  θ = {angle_theta}°  |  m = {masse_m} kg")
    return vitesse_initiale_v0, angle_theta, masse_m


def compute_trajectory(v0, theta_deg, m, x0=0.0, y0=0.0, dt=0.01, use_drag=False):
    theta = math.radians(theta_deg)
    vx    = v0 * math.cos(theta)
    vy    = v0 * math.sin(theta)
    x, y  = x0, y0
    xs, ys = [x], [y]

    while y >= 0:
        if use_drag:
            v      = math.sqrt(vx**2 + vy**2)
            f_drag = 0.5 * RHO * CD * A * v**2
            ax     = -(f_drag * vx / v) / m
            ay     = -G - (f_drag * vy / v) / m
        else:
            ax, ay = 0, -G

        vx += ax * dt
        vy += ay * dt
        x  += vx * dt
        y  += vy * dt
        xs.append(x)
        ys.append(y)

    return xs, ys


def comparer_trajectoires(v0, theta_deg, m):
    xs1, ys1 = compute_trajectory(v0, theta_deg, m, use_drag=False)
    xs2, ys2 = compute_trajectory(v0, theta_deg, m, use_drag=True)

    stats = {
        "portee_sans" : xs1[-1],
        "portee_avec" : xs2[-1],
        "hmax_sans"   : max(ys1),
        "hmax_avec"   : max(ys2),
        "perte"       : (1 - xs2[-1] / xs1[-1]) * 100
    }

    print("=============================================")
    print("         SANS frottement   AVEC frottement")
    print("=============================================")
    print(f"  Portée  : {stats['portee_sans']:>8.2f} m   {stats['portee_avec']:>8.2f} m")
    print(f"  H max   : {stats['hmax_sans']:>8.2f} m   {stats['hmax_avec']:>8.2f} m")
    print(f"  Perte de portée : {stats['perte']:.1f}%")
    print("=============================================")

    return xs1, ys1, xs2, ys2, stats


def plot_trajectory(v0, theta_deg, m, xs1, ys1, xs2, ys2, stats):

    fig, ax = plt.subplots(figsize=(10, 5))

    # --- les 2 courbes ---
    ax.plot(xs1, ys1, color="steelblue",  linewidth=2,   label="Sans frottement")
    ax.plot(xs2, ys2, color="tomato",     linewidth=2,   label="Avec frottement")

    # --- étoile au point de hauteur max ---
    i_max1 = ys1.index(max(ys1))
    i_max2 = ys2.index(max(ys2))
    ax.plot(xs1[i_max1], ys1[i_max1], "*", color="steelblue", markersize=14, zorder=5)
    ax.plot(xs2[i_max2], ys2[i_max2], "*", color="tomato",    markersize=14, zorder=5)

    # --- ligne du sol ---
    ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")

    # --- annotation stats (boîte de texte) ---
    texte = (
        f"Sans frottement\n"
        f"  Portée : {stats['portee_sans']:.1f} m\n"
        f"  H max  : {stats['hmax_sans']:.1f} m\n\n"
        f"Avec frottement\n"
        f"  Portée : {stats['portee_avec']:.1f} m\n"
        f"  H max  : {stats['hmax_avec']:.1f} m\n\n"
        f"Perte : {stats['perte']:.1f}%"
    )
    ax.text(
        0.98, 0.97, texte,
        transform=ax.transAxes,
        fontsize=9, verticalalignment="top", horizontalalignment="right",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="lightgray", alpha=0.9)
    )

    # --- titre et labels ---
    ax.set_title(f"Trajectoire de projectile  —  v₀={v0} m/s  |  θ={theta_deg}°  |  m={m} kg", fontsize=12, fontweight="bold")
    ax.set_xlabel("Distance horizontale (m)")
    ax.set_ylabel("Hauteur (m)")
    ax.legend(loc="upper left")
    ax.set_ylim(bottom=0)
    ax.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


# =============================================================
if __name__ == "__main__":
    v0, theta, m            = get_input()
    xs1, ys1, xs2, ys2, stats = comparer_trajectoires(v0, theta, m)
    plot_trajectory(v0, theta, m, xs1, ys1, xs2, ys2, stats)