# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:47:23 2018

@author: gupte
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

trials = 100
distance = 40 * 3.086e24
thetaobs = np.linspace(0, math.pi, trials)
gamma = 100
energy = 10**50
thetaj = 10
fluence = []
for a in range(0,trials):
    beta = math.sqrt(-((1/(gamma))-1))
    deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(thetaobs[a] - thetaj))))
    deltazero = 1/(gamma * (1 - beta * math.cos(math.radians(0 - thetaj))))
    eta = 1/(deltaobs/deltazero)
    FOn = energy/(4 * math.pi*((distance) ** 2))
    fluence.append(eta * FOn)
    print(eta)
    
plt.ylabel('Fluence (ergs/cm^2) ')
plt.xlabel('Theta (rad) ')
plt.yscale('log')
plt.title('Off axis best fit fluence vs angle (rad) ')
plt.figure(1)
plt.plot(thetaobs, fluence)

#plt.loglog(distance2, fluence)
plt.grid(True)
plt.figure(figsize = (20, 10))
plt.show()
