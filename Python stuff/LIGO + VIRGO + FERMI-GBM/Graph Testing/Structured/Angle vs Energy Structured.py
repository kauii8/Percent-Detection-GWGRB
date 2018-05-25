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
energy,tp = [], []
energyorig = 10e51

trials = 100
alpha = 1.9
thetac = 9
thetaj = 10
theta = np.logspace(-1, 1.4, trials)
theta = theta.tolist()

for a in range(0,trials):
    energy.append(angletoenergy(theta[a], energyorig, thetac, alpha))
    tp.append(2.1 * (energy[a] ** Fraction('1/3')) * ((10e-5) ** Fraction(-1,3)) * ((math.fabs(theta[a] - thetaj)/10) ** Fraction('8/3')))

plt.subplot(223)
plt.ylim(10e48, 10e52)
plt.ylabel('Energy (ergs) ')
plt.xlabel('Theta (deg) ')
plt.title('Structured Jet best fit angle vs energy ')
plt.loglog(theta, energy)
plt.grid(True)

