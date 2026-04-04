import math
import scipy.constants

g = scipy.constants.g  # 9.80665 m/s²

# constantes aérodynamiques (balle de rayon 0.05m)
RHO = 1.225   # densité de l'air (kg/m³)
CD  = 0.47    # coefficient de traînée (sphère)
A   = 0.007854  # surface frontale πr² avec r=0.05m

def get_input():
    print("=============================================")
    print("SIMULATION DE PROJECTILE — Paramètres")
    print("=============================================")
    vitesse_initiale_v0 = float(input("Vitesse Initiale v0 (m/s): "))
    angle_theta = float(input("Angle Theta (degrés): "))
    masse_m = float(input("Masse m (kg): "))
    print(f"v0 = {vitesse_initiale_v0} |  θ = {angle_theta}°  |  m = {masse_m} kg")
    return vitesse_initiale_v0, angle_theta, masse_m

def compute_trajectory(v0, theta_deg, m, x0=0.0, y0=0.0, dt=0.01, avec_frott=False):
    theta_en_radians= math.radians(theta_deg) 
    vx=v0*math.cos(theta_en_radians)
    vy=v0*math.sin(theta_en_radians)
    x=x0
    y=y0
    xs = [x]
    ys = [y]
    while y>=0:
        if avec_frott:
            v = math.sqrt(vx**2 + vy**2)
            force_frott = 0.5 * RHO * CD * A * v**2
            ax = -(force_frott * vx / v) / m
            ay = -g - (force_frott * vy / v) / m
        else:
            ax = 0
            ay = -g
        vx += ax * dt
        vy += ay * dt
        x  += vx * dt
        xs.append(x)
        y  += vy * dt
        ys.append(y)
    return xs, ys

if __name__ == "__main__":
    v0, theta, m = get_input()
    compute_trajectory(v0, theta, m)