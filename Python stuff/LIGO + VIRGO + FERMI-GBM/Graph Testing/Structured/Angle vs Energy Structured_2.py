'''------IMPORTS-------'''
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** 1.9))
    return ret
distance = 40 * 3.086e24
energy = []
fluence = []
xi = [0, math.pi/2, math.pi, (3*math.pi)/2, 2 * math.pi]
energyorig = 10e50
lorentzorig = 100
trials = 100
alpha = 1.9
thetac = 9
#theta = np.logspace(-1, 1.4, trials)
#theta = theta.tolist()
theta = np.linspace(0, 2 * math.pi, trials)

for a in range(0,trials):
    energy.append(angletoenergy(theta[a], energyorig, thetac, alpha))
    fluence.append(energy[a]/(4 * math.pi * (distance ** 2)))
    
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


#plt.ylim(10e48, 10e53)
plt.ylabel('Fluence (ergs/cm^2) ')
plt.xlabel('Theta (rad) ')
plt.yscale('log')
plt.title('Structured Jet best fit fluence vs angle (rad) ')
plt.figure(1)
plt.plot(theta, fluence)


#plt.loglog(distance2, fluence)
plt.grid(True)
plt.figure(figsize = (20, 10))
plt.show()