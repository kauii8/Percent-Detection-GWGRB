import math
import numpy as np
import matplotlib.pyplot as plt
def delta_function(gamma, beta, thetaobs, thetaj):
    ret = 1/(gamma * (1 - (beta * math.cos(thetaobs - thetaj))))
    return ret

trials = 100
fluence_off, GRBTEST_off = [], []
gamma = 100
energyinitial = 10**50
thetaj = 10
beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)
eta = []
thetaobs = np.linspace(0,math.pi,trials).tolist()

for a in range(0,trials):

    FOn = (energyinitial)/((4 * math.pi*((((100 * 3.086e+24) ** 2)))))
    deltaobs = delta_function(gamma, beta, thetaobs[a], math.radians(thetaj))
    deltazero = delta_function(gamma, beta, 0, 0)
    eta.append(deltaobs/deltazero) 
    fluence_off.append(eta[a] * FOn)
    

plt.plot(thetaobs, eta)
plt.yscale('log')
plt.show()
