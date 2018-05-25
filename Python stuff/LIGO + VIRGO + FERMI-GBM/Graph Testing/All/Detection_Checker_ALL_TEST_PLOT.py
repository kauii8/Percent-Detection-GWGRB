import matplotlib as plt
import numpy as np
import math

gamma = 100
fluence_off = []
gamma = 100
energyinitial = 1e51
thetaj = 10
trials = 100
thetaobs = np.linspace(0,math.pi)
beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)
for a in range(0,trials):
    FOn = (energyinitial)/((4 * math.pi*((((distance * 3.086e+24) ** 2)))))
    deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(thetaobs - math.radians(thetaj)))))
    deltazero = 1/(gamma * (1 - beta * math.cos(math.radians(0 - math.radians(thetaj)))))
    eta = (deltaobs/deltazero) 
    fluence_off.append(eta * FOn)