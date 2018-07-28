'''------HARD IMPORTS------'''
'''------HARD IMPORTS------'''
'''------STRUCTURED JET SIMULATION DATA------'''
energyinitial = 5.35e46
'''------STRUCTURED JET SIMULATION DATA------'''
'''------IMPORTS-------'''
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from operator import add
import random
import pylab
'''------IMPORTS-------'''
'''------FUNCTION------'''
def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** alpha))
    return ret
    
def delta_function(beta, thetaobs, thetaj):
    ret = 1 - beta * math.cos(thetaobs - thetaj)
    return ret

def curlyDelta(gamma, beta, thetaobs, thetaj):
    return 1 / (gamma * (1 - (beta * math.cos(thetaobs - thetaj))))
    #return (gamma * 2) / (1 + ((gamma * (thetaobs - thetaj)) ** 2))

def regularDelta(gamma, beta, thetaobs):
    return 1 / (gamma * (1 - (beta * math.cos(thetaobs))))

def limitDelta(gamma, thetaobs, thetaj):
    return (2 * gamma) / (1 + (gamma ** 2) * ((thetaobs - thetaj) ** 2))
'''------FUNCTION------'''
'''------CREATE POINTS------'''
Dv_LOUIS, Dv_WASH, Dv_VIRGO = 145, 145, 90
trials = 100 # input("Enter the number of points you want to test: ") 
distance = 100
thetaobs = []
for z in range(0,trials):
    #thetaobs.append(random.uniform(0, math.pi))
    thetaobs = np.linspace(0, math.pi/2, trials).tolist()

'''------CREATE POINTS-------'''
'''------OFF AXIS------'''
fluence_off, GRBTEST_off = [], []
gamma = 100
thetaj = 15
beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)


for a in range(0,trials):

    FOn = (energyinitial)/((4 * math.pi*((distance * 3.086e+24) ** 2)))

    firstScaler = 471130.1263539437
    secondScaler = 11.778253158848592
    thirdScaler = 2407.068288869093
    limitScaler = 2355.6506317697185

    if thetaobs[a] < math.radians(thetaj): 
        eta = firstScaler

    elif math.radians(thetaj) < thetaobs[a] <= (2 * math.radians(thetaj)):
        
        if gamma > 90 and thetaobs[a] - math.radians(thetaj) < .01:
            eta = limitDelta(gamma, thetaobs[a], math.radians(thetaj)) * limitScaler
        
        else:
            eta = (curlyDelta(gamma, beta, thetaobs[a], math.radians(thetaj)) ** 2) * secondScaler
            

    elif (2 * math.radians(thetaj)) <= thetaobs[a]:
        eta = (regularDelta(gamma, beta, thetaobs[a]) ** 3) * thirdScaler

        
    fluence_off.append(eta * energyinitial)
        
'''------OFF AXIS------'''

thetaobs_struc = thetaobs
for u in range(0,len(thetaobs)):
    thetaobs[u] = math.degrees(thetaobs[u])

off_axis_graph = plt.plot(thetaobs,fluence_off, label = 'Off Axis')
ax = plt.subplot(111)
#plt.title(r'$\theta_{obs}$' +' vs Fluence at ' + str(distance) + ' Mpc' + ' and energy = ' + str(energyinitial))
plt.title(r'$\theta_{obs}$' + ' vs ' r'$E_{iso}$')
plt.xlabel(r'$\theta_{obs}$' + '[deg]')
#plt.ylabel('Fluence (' + str(distance) + 'Mpc / d)'+r'$^2$'+' [erg/'+'cm' + r'$^2$' + '] ')
plt.ylabel(r'$E_{iso}(\theta_{obs})$' +' [erg]')
plt.yscale('log')
plt.xlim(0, math.pi)
axes = plt.gca()
axes.set_xlim([0,60])

GBM_SENS, SWIFT_SENS = [], []
for u in range(0, trials):
    GBM_SENS.append(2.5e-8)
    SWIFT_SENS.append(4.22e-10)
    
#Fermi_GBM_Sensitivity = plt.plot(thetaobs, GBM_SENS, linestyle='--', color='k')

ax.annotate('Fermi-GBM sensitivity', xy=(1, .000000003), xytext=(2, .00000004), color='k')
ax.grid(color='k', linestyle='-', linewidth=.2)

pylab.legend(loc='upper right')
plt.show()

