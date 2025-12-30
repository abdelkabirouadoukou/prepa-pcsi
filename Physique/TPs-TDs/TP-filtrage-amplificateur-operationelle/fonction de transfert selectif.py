# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:21:37 2024

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

# Fonction de transfert
def H(w): 
	return Ho/(1 + 1j*Q*(w/wo-wo/w))

#fonction asymptotique
def H1(w): 
	if w<=wo: # caractère dérivateur
		return (Ho/(Q*wo))*1j*w
	else: # caractère intégrateur
		return (Ho*wo/Q)/(1j*w)
    
# La phase
def F(w): 
	return np.angle(H(w))

Ho=1  ; Q=10
fo=1e3 ;  wo=2*np.pi*fo
n=200;w=np.linspace(0.1*wo,10*wo,n)
G=20*np.log10(abs(H(w)))
Gs=list(20*np.log10(abs(H1(x))) for x in w)
Fs=list(np.angle(H1(x)) for x in w)
fig,(ao,a1)=plt.subplots(1,2,figsize=(6,3))
plt.subplots_adjust(left=0.07,right=0.98)
ao.semilogx(w,G)
ao.semilogx(w,Gs)
ao.set_title('$G_{dB}$')
a1.semilogx(w,F(w))
a1.semilogx(w,Fs)
a1.set_title('$\phi(\omega)$')
ao.grid(which='both')
a1.grid(which='both')
#plt.savefig('diag_bode.pdf')
#plt.show()#étudier l'effet de Q sur la bande passante du filtre.  


