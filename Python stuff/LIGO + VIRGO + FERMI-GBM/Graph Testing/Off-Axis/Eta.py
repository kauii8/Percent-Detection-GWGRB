# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:08:52 2018

@author: Nihar
"""

import math
import matplotlib.pyplot as plt


Gamma = 100
beta = math.sqrt(1-(1/Gamma**2))
theta_j = 10 # [deg]
delta_0 = 1 / (Gamma * (1 - beta))

eta = []
for i in range(theta_j):
    eta.append(1) # since within the jet we have constant flux. Note that I am not normalizing to the flux you expect off axis, you have to add that.

for i in range(100):
    theta_obs = i+theta_j # [deg]
    delta_obs = 1 / (Gamma * (1 - beta*math.cos(math.radians(theta_obs - theta_j))))
    eta.append(delta_obs / delta_0)

fig = plt.figure("1")
plt.plot(range(100+theta_j), eta)
plt.yscale('log')
plt.show()
