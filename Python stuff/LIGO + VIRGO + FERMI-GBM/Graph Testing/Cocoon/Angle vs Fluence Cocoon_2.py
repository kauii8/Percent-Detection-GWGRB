import numpy as np
import math
import matplotlib.pyplot as plt
#https://arxiv.org/pdf/1610.05362.pdf
initialenergy = 10e51
c = 299792458
trials = 100
distance = 40 * 3.086e24
theta = np.linspace(.01, 2 * math.pi, trials)
theta = theta.tolist()
thetaj = math.radians(10)
energy, fluence = [], []
for a in range(0,trials):
    energy.append((2 * initialenergy * (c**2.7)) / (distance * ((theta[a]/thetaj) ** 2)))
    fluence.append(energy[a]/ (4 * math.pi * (distance ** 2)))

plt.ylabel('Fluence (ergs/cm^2) ')
plt.xlabel('Theta (rad) ')
plt.yscale('log')
plt.title('Cocoon best fit fluence vs angle (rad) ')
plt.figure(1)
plt.plot(theta, fluence)

#plt.loglog(distance2, fluence)
plt.grid(True)
plt.figure(figsize = (20, 10))
plt.show()