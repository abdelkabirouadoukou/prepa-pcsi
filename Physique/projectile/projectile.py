import math
import scipy.constants

g = scipy.constants.g

def get_input():
    print("=============================================")
    print("SIMULATION DE PROJECTILE — Paramètres")
    print("=============================================")
    vitesse_initiale_v0 = float(input("Vitesse Initiale v0 (m/s): "))
    angle_theta = float(input("Angle Theta (degrés): "))
    masse_m = float(input("Masse m (kg): "))
    print(f"v0 = {vitesse_initiale_v0} |  θ = {angle_theta}°  |  m = {masse_m} kg")
    return vitesse_initiale_v0, angle_theta, masse_m

def compute_trajectory(v0, theta_deg, m, x0=0.0, y0=0.0, dt=0.01):
    theta_en_radians= math.radians(theta_deg) 
    vx=v0*math.cos(theta_en_radians)
    vy=v0*math.sin(theta_en_radians)
    x=x0
    y=y0
    xs = [x]
    ys = [y]
    while y>=0:
        vy-=g*dt
        x += vx*dt
        xs.append(x)
        y += vy*dt
        ys.append(y)
    hauteurMax = max(xs)
    proteeTot = xs[-1]
    print(f"  Portée totale  : {proteeTot:.2f} m")
    print(f"  Hauteur max    : {hauteurMax:.2f} m")
    return xs, ys

if __name__ == "__main__":
    v0, theta, m = get_input()
    compute_trajectory(v0, theta, m)