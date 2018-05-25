# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:47:23 2018

@author: gupte
"""
import numpy as np
import math

trials = 100
distance = 450 * 3.086e24
thetaobs = np.linspace(0, 2 * math.pi, trials)
gamma = 100
energy = 10**50
thetaj = 10
for a in range(0,trials):
    beta = math.sqrt(-((1/(gamma))-1))
    deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(thetaobs[a] - thetaj))))
    deltazero = 1/(gamma * (1 - beta * math.cos(math.radians(0 - thetaj))))
    eta = (deltaobs/deltazero)
    FOn = energy/(4 * math.pi*((distance) ** 2))
    FOff = eta * FOn,
print(FOff)