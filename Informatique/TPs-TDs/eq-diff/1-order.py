import matplotlib.pyplot as plt
import numpy as np
# import scipy as sy

def f(t,y):
    return -y*t

def subDiviser(a,b,n):
    h=(b-a)/n
    L=[]
    for i in range(0,n+1):
        L.append(a+i*h)
    return L

def eulerExplicite(f,a,b,n,y_0):
    h=(b-a)/n
    T=subDiviser(a,b,n)
    Y=np.zeros(len(T))
    Y[0]=y_0
    for i in range(0,n):
        Y[i+1] = Y[i] + h*f(T[i],Y[i])
    
    return T, Y

def eulerExpliciteImplicit(f,a,b,n,y_0):
    h=(b-a)/n
    T_imp=subDiviser(a,b,n)
    Y_imp=np.zeros(len(T_imp))
    Y_imp[0]=y_0
    for i in range(0,n):
        U=Y_imp[i] + h*f(T_imp[i],Y_imp[i])
        Y_imp[i+1] = Y_imp[i] + h*f(T_imp[i],U)
    
    return T_imp, Y_imp

a, b, n, y_0 = 0, 2, 100, 1
T, Y = eulerExplicite(f, a, b, n, y_0)
T_imp, Y_imp = eulerExpliciteImplicit(f, a, b, n, y_0)

T_exact = np.linspace(a, b, 200)
Y_exact = np.exp(-(T_exact**2) / 2)

plt.figure(figsize=(10, 6))
plt.plot(T, Y, 'b-', label=f"Approximation d'Euler (n={n})", linewidth=2)
plt.plot(T_imp, Y_imp, 'g-.', label=f"Approximation d'Euler implicite (n={n})", linewidth=2)
plt.plot(T_exact, Y_exact, 'r--', label="Solution exacte ($e^{-t^2/2}$)", linewidth=1.5)
    
plt.title("Méthode d'Euler Explicite pour $dy/dt = -yt$", fontsize=14)
plt.xlabel("t", fontsize=12)
plt.ylabel("y(t)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=11)

plt.show()