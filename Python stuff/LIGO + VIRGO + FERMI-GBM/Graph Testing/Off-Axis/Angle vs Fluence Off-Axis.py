'''------IMPORTS-------'''
from __future__ import division
import numpy as np
import fractions as Fraction
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from operator import add
import random
'''------IMPORTS-------'''
'''------KNOWN DEFS------'''
Fvmax = []
'''------KNOWN DEFS------'''
'''------UNKNOWN DEFS------'''
distance = 40
distanceinmeters = 40 * 3.086e+22
distance28 = distanceinmeters/10e28
'''------UNKWOWN DEFS------'''
trials = 500
theta = np.linspace(0, math.pi, trials)
for a in range(0,trials):
    Fvmax.append(1.1e5 * (epsilonB ** Fraction('1/2')) * (energy52) * (nism ** Fraction('1/2')) * (distance28 ** -2))
    
plt.subplot(223)
plt.ylim(10e-3, 10e5)
plt.loglog(theta, Fvmax)
plt.grid(True)
plt.show()