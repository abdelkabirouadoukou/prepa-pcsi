import math
import scipy.constants
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons, Button

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
    print(f"  H max   : {stats['hmax_sans']:>8.2f} m   {stats['hmax_avoir']:>8.2f} m")
    print(f"  Perte de portée : {stats['perte']:.1f}%")
    print("=============================================")

    return xs1, ys1, xs2, ys2, stats


def plot_trajectory(v0, theta_deg, m, xs1, ys1, xs2, ys2, stats):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(xs1, ys1, color="steelblue", linewidth=2, label="Sans frottement")
    ax.plot(xs2, ys2, color="tomato",    linewidth=2, label="Avec frottement")
    i_max1 = ys1.index(max(ys1))
    i_max2 = ys2.index(max(ys2))
    ax.plot(xs1[i_max1], ys1[i_max1], "*", color="steelblue", markersize=14, zorder=5)
    ax.plot(xs2[i_max2], ys2[i_max2], "*", color="tomato",    markersize=14, zorder=5)
    ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    texte = (
        f"Sans frottement\n"
        f"  Portée : {stats['portee_sans']:.1f} m\n"
        f"  H max  : {stats['hmax_sans']:.1f} m\n\n"
        f"Avec frottement\n"
        f"  Portée : {stats['portee_avec']:.1f} m\n"
        f"  H max  : {stats['hmax_avec']:.1f} m\n\n"
        f"Perte : {stats['perte']:.1f}%"
    )
    ax.text(0.98, 0.97, texte, transform=ax.transAxes, fontsize=9,
            verticalalignment="top", horizontalalignment="right",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="lightgray", alpha=0.9))
    ax.set_title(f"Trajectoire  —  v₀={v0} m/s  |  θ={theta_deg}°  |  m={m} kg",fontsize=12, fontweight="bold")
    ax.set_xlabel("Distance horizontale (m)")
    ax.set_ylabel("Hauteur (m)")
    ax.legend(loc="upper left")
    ax.set_ylim(bottom=0)
    ax.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

# I dont know how to build app on desktop so Ai help me here ;)
def run_app():
    V0_INIT, THETA_INIT, M_INIT = 50.0, 45.0, 0.5

    # ── figure + axes ──
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.30)   # espace en bas pour les sliders

    # ── tracé initial ──
    xs1, ys1 = compute_trajectory(V0_INIT, THETA_INIT, M_INIT, use_drag=False)
    xs2, ys2 = compute_trajectory(V0_INIT, THETA_INIT, M_INIT, use_drag=True)

    line1, = ax.plot(xs1, ys1, color="steelblue", lw=2, label="Sans frottement")
    line2, = ax.plot(xs2, ys2, color="tomato",    lw=2, label="Avec frottement")
    star1, = ax.plot([], [], "*", color="steelblue", ms=13, zorder=5)
    star2, = ax.plot([], [], "*", color="tomato",    ms=13, zorder=5)
    info   = ax.text(0.98, 0.97, "", transform=ax.transAxes, fontsize=9,va="top", ha="right",bbox=dict(boxstyle="round,pad=0.5", facecolor="white",edgecolor="lightgray", alpha=0.9))

    ax.axhline(0, color="gray", lw=0.8, ls="--")
    ax.set_xlabel("Distance horizontale (m)")
    ax.set_ylabel("Hauteur (m)")
    ax.legend(loc="upper left")
    ax.grid(True, ls="--", alpha=0.4)
    titre = ax.set_title("", fontsize=11, fontweight="bold")

    # ── sliders  [left, bottom, width, height] ──
    sl_v0    = Slider(fig.add_axes([0.12, 0.18, 0.55, 0.03]), "v₀ (m/s)", 1,   100,  valinit=V0_INIT,    valstep=1,   color="steelblue")
    sl_theta = Slider(fig.add_axes([0.12, 0.12, 0.55, 0.03]), "θ (°)",    1,   89,   valinit=THETA_INIT, valstep=1,   color="steelblue")
    sl_mass  = Slider(fig.add_axes([0.12, 0.06, 0.55, 0.03]), "m (kg)",   0.1, 10,   valinit=M_INIT,     valstep=0.1, color="steelblue")

    # ── checkbox + bouton reset ──
    cb   = CheckButtons(fig.add_axes([0.72, 0.10, 0.12, 0.08]), ["Frottement"], [True])
    btn  = Button(fig.add_axes([0.87, 0.10, 0.08, 0.08]), "Reset", color="#eeeeee", hovercolor="#dddddd")

    # ── update : appelée à chaque changement ──
    def update(_=None):
        v0    = sl_v0.val
        theta = sl_theta.val
        m     = sl_mass.val
        drag  = cb.get_status()[0]

        xs1, ys1 = compute_trajectory(v0, theta, m, use_drag=False)
        xs2, ys2 = compute_trajectory(v0, theta, m, use_drag=drag)

        line1.set_data(xs1, ys1)
        line2.set_data(xs2, ys2)
        line2.set_visible(drag)

        # étoiles
        i1 = ys1.index(max(ys1))
        star1.set_data([xs1[i1]], [ys1[i1]])
        if drag:
            i2 = ys2.index(max(ys2))
            star2.set_data([xs2[i2]], [ys2[i2]])
        else:
            star2.set_data([], [])

        # rescale
        all_x = xs1 + (xs2 if drag else [])
        all_y = ys1 + (ys2 if drag else [])
        ax.set_xlim(0, max(all_x) * 1.05)
        ax.set_ylim(0, max(all_y) * 1.15)

        # titre
        titre.set_text(f"Trajectoire  —  v₀={v0:.0f} m/s  |  θ={theta:.0f}°  |  m={m:.1f} kg")

        # stats dans la boîte
        p1, h1 = xs1[-1], max(ys1)
        p2, h2 = xs2[-1], max(ys2)
        perte  = (1 - p2/p1) * 100
        if drag:
            txt = (f"Sans frottement\n  Portée : {p1:.1f} m\n  H max  : {h1:.1f} m\n\n"f"Avec frottement\n  Portée : {p2:.1f} m\n  H max  : {h2:.1f} m\n\n"f"Perte : {perte:.1f}%")
        else:
            txt = (f"Sans frottement\n  Portée : {p1:.1f} m\n  H max  : {h1:.1f} m\n\n"f"Frottement désactivé")
        info.set_text(txt)
        fig.canvas.draw_idle()

    def reset(_):
        sl_v0.reset()
        sl_theta.reset()
        sl_mass.reset()
        update()

    sl_v0.on_changed(update)
    sl_theta.on_changed(update)
    sl_mass.on_changed(update)
    cb.on_clicked(update)
    btn.on_clicked(reset)

    update()
    plt.suptitle("Simulation de projectile — PCSI", fontsize=12, fontweight="bold")
    plt.show()


if __name__ == "__main__":
    run_app()