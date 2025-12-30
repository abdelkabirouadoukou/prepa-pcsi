# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:30:35 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt


E=1
def a(n):#pour un signal carré ------
	return 2*E*np.sin(n*np.pi/2)/(n*np.pi)

def carre(N):#N:nombre des harmoniques
	e=0 #signal carré alternatif
	for k in range(1,N):
		e+=a(k)*np.cos(k*w*t)
	return e


def H(w): 
	return Ho/(1 + 1j*Q*(w/wo-wo/w))

def H1(w): #fonction asymptotique
	if w<=wo: # caractère dérivateur
		return (Ho/(Q*wo))*1j*w
	else: # caractère intégrateur
		return (Ho*wo/Q)/(1j*w)

def F(w): # la phase
	return np.angle(H(w))


def Sn(n):#gain Sn en amplitude 
	return np.abs(H(n*w))*a(n)
def sortie(N):#la sortie du filtre
	s=0# s(0)=H(0)*e(0)=0 car H(0)->0
	for n in range(1,N):#n>=1
		s+=Sn(n)*np.cos(n*w*t+F(n*w))
	return s


fo=1e3 ;  wo=2*np.pi*fo ; T=1/fo ; n = 30
t = np.linspace(0,T, n) 
Ho = 1 ; Q = 20 # Varier le facteur de qualité pour voir l'effet sur e(t)
N=200 #signal d'entrée purement carré
w=wo #sélection du fondamental
plt.close("all") 
fig,ax=plt.subplots(1,figsize=(4,3))
ax.plot(t,carre(N),'r-',label='e(t)')
ax.plot(t,sortie(N),'b-.',label='s(t)')
ax.legend(loc="upper right")
plt.savefig('tension_sortie.pdf')
##plt.show()