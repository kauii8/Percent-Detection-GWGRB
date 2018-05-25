# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 22:41:36 2018

@author: gupte
"""

'''------IMPORTS-------'''
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** 1.9))
    return ret
distance1, distance2, distance3, distance4, distance5, distance6, distance7, distance8, distance9, distance10, distance11, distance12 = [], [], [], [], [], [], [], [], [], [], [], []
energy1,energy2, energy3, energy4, energy5, energy6, energy7, energy8, energy9, energy10, energy11, energy12 = [], [], [], [], [], [], [], [], [], [], [], []
fluence1, fluence2, fluence3, fluence4, fluence5, fluence6, fluence7, fluence8, fluence9, fluence10, fluence11, fluence12 = [], [], [], [], [], [], [], [], [], [], [], []
energyorig = 10e52
lorentzorig = 100
trials = 100
alpha = 1.9
thetac = 9
theta1 = np.logspace(-1, 1.4, trials)
theta1 = theta1.tolist()
distance1 = 450 * 3.086e24

for a in range(0,trials):
    energy1.append(angletoenergy(theta1[a], energyorig, thetac, alpha))

    #distance1.append(random.uniform(0.0,450.0) * 3.086e24)

    fluence1.append(energy1[a]/(4 * math.pi * (distance1 ** 2)))


'''
plt.subplot(223)
plt.ylim(10e48, 10e53)
plt.ylabel('Energy (ergs) ')
plt.xlabel('Theta (deg) ')
plt.title('Structured Jet best fit angle vs energy ')
plt.loglog(theta, energy)
plt.grid(True)
plt.show()
'''

plt.subplot(223)
#plt.ylim(10e48, 10e53)
plt.ylabel('Fluence (ergs/cm^2) ')
plt.xlabel('Theta (deg) ')
plt.yscale('log')
plt.title('Structured Jet best fit angle vs energy ')
plt.plot(theta1, fluence1)

#plt.loglog(distance2, fluence)
plt.grid(True)
plt.figure(figsize = (20, 10))
plt.show()