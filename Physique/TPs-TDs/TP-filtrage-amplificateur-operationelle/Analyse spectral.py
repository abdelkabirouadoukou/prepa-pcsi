# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:00:28 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt


E=1

#pour un signal carré ------
def a(n):
	return 2*E*np.sin(n*np.pi/2)/(n*np.pi)

def carre(N):#N:nombre des harmoniques
	e=0 #signal carré alternatif
	for k in range(1,N):
		e+=a(k)*np.cos(k*w*t)
	return e

#----------------------------------------------------------
#signal triangulaire 


def b(n):  
	return 8*E*np.sin(n*np.pi/2)/(n*np.pi)**2

def triangulaire(N):
	h=0 #signal alternatif
	for k in range(1,N):
		h+=b(k)*np.sin(k*w*t)
	return h
#----------------------------------------------------------

f=1e2 ; w =2*np.pi*f ; T=1/f
n = 100







#--------------Changer b(k) par a(k) et inversement ---------

t = np.linspace(0,T, n)


#Affichage signal carré
fig,(a0,a1)=plt.subplots(2,1,figsize=(6,3))
a0.bar(np.arange(1, 30),abs(a(np.arange(1, 30))),width=0.2)
plt.plot(t,carre(100))




#Affichage signal triangulaire
#fig,(b0,b1)=plt.subplots(2,1,figsize=(6,3))
#b0.bar(np.arange(1, 30),abs(b(np.arange(1, 30))),width=0.2)
#plt.plot(t,triangulaire(100))




