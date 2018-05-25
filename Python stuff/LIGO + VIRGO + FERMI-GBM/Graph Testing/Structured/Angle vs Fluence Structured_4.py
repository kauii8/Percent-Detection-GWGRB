'''------IMPORTS-------'''
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection
from fractions import Fraction
    
def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** 1.9))
    return ret
energy,tp,fluence = [], [],[]
energyorig = 7e51

trials = 100
alpha = 1.9
thetac = 9
thetaj = 10
theta = np.logspace(-1, 2, trials-10)
theta = theta.tolist()
thetacounter = 0 
for i in range(0,10):  
    theta = theta[:thetacounter] + [0 + (float(thetacounter)/100)] + theta[thetacounter:]
    thetacounter += 1
distance = 40 * 3.086e24
 

for a in range(0,trials):
    energy.append(angletoenergy(theta[a], energyorig, thetac, alpha))
    tp.append(2.1 * (energy[a] ** Fraction('1/3')) * ((10e-5) ** Fraction(-1,3)) * ((math.fabs(theta[a] - thetaj)/10) ** Fraction('8/3')))
    fluence.append(energy[a]/(4 * math.pi * (distance ** 2)))

plt.subplot(223)
plt.ylim(10e47, 10e52)
plt.ylabel('Energy (ergs) ')
plt.xlabel('Theta (deg) ')
plt.xscale('log')
plt.title('Structured Jet best fit angle vs energy ')
plt.loglog(theta, energy)
plt.grid(True)
plt.show()