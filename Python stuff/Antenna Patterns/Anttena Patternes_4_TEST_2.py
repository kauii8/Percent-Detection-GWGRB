import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as rnd


def AP_PLUS(eta,a,b,psi):
    ret = math.sin(eta) * ((a * math.cos(2 * psi)) + (b * math.sin(2 * psi)))
    return ret
    
def AP_CROSS(eta,a,b,psi):
    ret = math.sin(eta) * ((b * math.cos(2 * psi)) - (a * math.sin(2 * psi)))
    return ret

def afunction(chi, beta, theta, phi, lambd):
    ret = ((1/16) * math.sin(2 * chi) * (3 - math.cos(2 * beta)) * (3 - math.cos(2 * theta))
    * math.cos(2(phi + lambd)))
    
    + ((1/4) * math.cos(2 * chi) * math.sin(beta) * (3 - math.cos(2 * theta))
    * math.sin(2 * (phi + lambd)))
    
    + ((1/4) * math.sin(2 * chi) * math.sin(2 * beta) * math.sin(2 * theta) * math.cos(phi + lambd))
    
    + ((1/2) * math.cos(2 * chi) * math.cos(beta) * math.sin(2 * theta) * math.sin(phi + lambd))
    
    + ((3/4) * math.sin(2 * chi) * (math.cos(beta) ** 2) * (math.sin(theta) ** 2))
    return ret


def COMPPAS_TO_ANGLE(compassdirection):
    ret = ((5 * math.pi) / 2) - compassdirection
    return ret
    
def DMS_TO_DEGREES(degs, mins, secs):
    ret = degs + (mins/60) + (secs/3600)
    return ret


psi = math.pi/2
eta = math.pi/2



X, Y, Z, rho = [],[],[],[]
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
listnump = 0
while phi[listnump] <6.28:
    listnumt = 0
    while theta[listnumt] < 3.14:
        X.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.cos(phi[listnump]) * np.sin(theta[listnumt]))
        Y.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.sin(phi[listnump]) * np.sin(theta[listnumt]))
        Z.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.cos(theta[listnumt]))
        rho.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)))
        
        listnumt = listnumt + 1
    listnump = listnump + 1


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X,Y,Z)
plt.show()

'''definitions for cross polarization'''
'''
===============
Check for accuracy
===============
'''

predmaxrho = function3(0,0,mult,ex,pl)

if max(rho) == predmaxrho : 
    print('first check sucessful (max value of rho) ')
    print(str(max(rho)) + ' = ' + str(predmaxrho))
else:
    print('first check failed (max value of rho)')    



checklist = [] 
for checkcounter in range(500):
    checklist.append(rnd.choice(rho))

avrandrho = (np.sum(checklist))/(len(checklist))

if 1.8<predmaxrho/avrandrho<2.2:
    print('second check sucessful (2x random vectors = max rho) ')
    print(predmaxrho/avrandrho)
else:
    print('second check failed (2x random vectors = max rho) ')  
    
'''NOTE:
    The actual graph is a scatter plot because I could not find a better way to plot the points
    I tried plotting a surface to make it look cleaner however it did not work with the 1D arrays
    (X,Y,Z). To make this clearer I would have to import something other than matplotlib and I 
    wasn't too familiar with matplotlib in the first place so I figured I'd have trouble. 
    
    However, function3 (the function that calculates the rho if you will) is accurate and has been
    checked with the wolfram program. That is if you were to plug points into both function3 and 
    the wolfram progrom they would yeild the same values. 
'''