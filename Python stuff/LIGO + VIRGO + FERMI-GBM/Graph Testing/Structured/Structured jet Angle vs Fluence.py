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
#theta = np.logspace(-1, 1.4, trials)
#theta = theta.tolist()
theta1, theta2, theta3, theta4, theta5, theta6, theta7, theta8, theta9, theta10, theta11, theta12 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

for a in range(0,trials):
    energy1.append(angletoenergy(theta1, energyorig, thetac, alpha))
    energy2.append(angletoenergy(theta2, energyorig, thetac, alpha))
    energy3.append(angletoenergy(theta3, energyorig, thetac, alpha))
    energy4.append(angletoenergy(theta4, energyorig, thetac, alpha))
    energy5.append(angletoenergy(theta5, energyorig, thetac, alpha))
    energy6.append(angletoenergy(theta6, energyorig, thetac, alpha))
    energy7.append(angletoenergy(theta7, energyorig, thetac, alpha))
    energy8.append(angletoenergy(theta8, energyorig, thetac, alpha))
    energy9.append(angletoenergy(theta9, energyorig, thetac, alpha))
    energy10.append(angletoenergy(theta10, energyorig, thetac, alpha))
    energy11.append(angletoenergy(theta11, energyorig, thetac, alpha))
    energy12.append(angletoenergy(theta12, energyorig, thetac, alpha))
    distance1.append(random.uniform(0.0,450.0) * 3.086e24)
    distance2.append(random.uniform(0.0,450.0) * 3.086e24)
    distance3.append(random.uniform(0.0,450.0) * 3.086e24)
    distance4.append(random.uniform(0.0,450.0) * 3.086e24)
    distance5.append(random.uniform(0.0,450.0) * 3.086e24)
    distance6.append(random.uniform(0.0,450.0) * 3.086e24)
    distance7.append(random.uniform(0.0,450.0) * 3.086e24)
    distance8.append(random.uniform(0.0,450.0) * 3.086e24)
    distance9.append(random.uniform(0.0,450.0) * 3.086e24)
    distance10.append(random.uniform(0.0,450.0) * 3.086e24)
    distance11.append(random.uniform(0.0,450.0) * 3.086e24)
    distance12.append(random.uniform(0.0,450.0) * 3.086e24)
    fluence1.append(energy1[a]/(4 * math.pi * (distance1[a] ** 2)))
    fluence2.append(energy2[a]/(4 * math.pi * (distance2[a] ** 2)))
    fluence3.append(energy3[a]/(4 * math.pi * (distance3[a] ** 2)))
    fluence4.append(energy4[a]/(4 * math.pi * (distance4[a] ** 2)))
    fluence5.append(energy5[a]/(4 * math.pi * (distance5[a] ** 2)))
    fluence6.append(energy6[a]/(4 * math.pi * (distance6[a] ** 2)))
    fluence7.append(energy7[a]/(4 * math.pi * (distance7[a] ** 2)))
    fluence8.append(energy8[a]/(4 * math.pi * (distance8[a] ** 2)))
    fluence9.append(energy9[a]/(4 * math.pi * (distance9[a] ** 2)))
    fluence10.append(energy10[a]/(4 * math.pi * (distance10[a] ** 2)))
    fluence11.append(energy11[a]/(4 * math.pi * (distance11[a] ** 2)))
    fluence12.append(energy12[a]/(4 * math.pi * (distance12[a] ** 2)))
    
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
plt.xlabel('Distance (cm) ')
plt.yscale('log')
plt.title('Structured Jet best fit fluence vs energy ')
plt.figure(1)
plt.scatter(distance1, fluence1)

plt.scatter(distance2, fluence2)

plt.scatter(distance4, fluence4)

plt.scatter(distance6, fluence6)

plt.scatter(distance8, fluence8)

plt.scatter(distance10, fluence10)

plt.scatter(distance12, fluence12)


#plt.loglog(distance2, fluence)
plt.grid(True)
plt.figure(figsize = (20, 10))
plt.show()