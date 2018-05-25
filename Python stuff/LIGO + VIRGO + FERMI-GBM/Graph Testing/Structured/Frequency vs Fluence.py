'''------IMPORTS-------'''
from fractions import Fraction
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

def converttometers(units, item):
    if units == 100:
        ret = item * 3.086e+22
    elif units == -1:
        ret = item/100
    elif units == 1:
        ret = item * 1000
    return ret
    
'''100 = MPC
   1 = Km
'''

def angletolorentz(theta, thetac, gammac, alphar, betar):
    ret = gammac/ ((1 + ((theta/thetac) ** (alphar * betar))) ** (1/betar))
    return ret
    
def angletoenergy(theta, thetac, energyc, alphae, betae):
    ret = energyc/ ((1 + ((theta/thetac) ** (alphae * betae))) ** (1/betae))
    return ret

theta = math.radians(16)
lorentzorig, energyorig, timeindays, fluence = [], [], [], [], 

trials = 1000
v = np.logspace(10, 18, trials)
v = v.tolist()

timeindays = 5     #CHANGEALBE


energyc, gammac = 10e53, 10e4
distance = 40
distanceinmeters = converttometers(100, distance)
distanceincentimeters = distanceinmeters * 100
diameter = 10.68
diameterinmeters = converttometers(1, diameter)
thetac = math.radians((10 * .1))
alphae, betae, betar, alphar = 2, 1, 1, 2

me, sigmaT, mp, qe = 9.10938356e-31, 6.6524587158e-29, 1.6726219e-27, 1.60217662e-19
c = 299792458

epsilonB, epsilonE, p, nism = 10e-2, 10e-3, 2.5, 10.0   #CHANGEALBE
#epsilonB, epsilonE, p, nism = 10e-3, 10e-2, 2.3, 10e-4
nismmeters = converttometers(-1, nism)
listnum = 0

for a in range(0,trials):
    #lorentzorig = angletolorentz(theta, thetac, gammac, alphar, betar)
    #energyorig  = angletoenergy(theta, thetac, energyc, alphae, betae)
    lorentzorig = 1000   #CHANGEALBE
    energyorig = 1.5e53    #CHANGEALBE
    energy52, distance28 = energyorig/10e52, distanceincentimeters/10e28
    time = timeindays * 24 * 60 * 60
    B = ((32 * math.pi * mp * epsilonB * nismmeters) ** Fraction('1/2')) * lorentzorig * c
    lorentzc = (3 * me) / (16 * epsilonE * sigmaT * mp * c * time * (lorentzorig ** 3) * nismmeters) #(6 * math.pi * me * c) / (sigmaT * lorentzorig * (B ** 2) * time[listnum])
    lorentzm = epsilonE * (mp/me) * lorentzorig * ((p - 2)/(p - 1))

    vc = 2.7e12 * (epsilonB ** Fraction('-3/2')) * (energy52 ** Fraction('-1/2')) * (nism ** Fraction('-1')) * (timeindays ** Fraction('-1/2'))
    vm = 5.7e14 * (epsilonB ** Fraction('1/2')) * (epsilonE ** 2) * (energy52 ** Fraction('1/2')) *  (timeindays ** Fraction('-3/2'))   
    Fvmax = 1.1e5 * (epsilonB ** Fraction('1/2')) * (energy52) * (nism ** Fraction('1/2')) * (distance28 ** -2)
        
    vc = 6.309e13
    vm = 12.5e15
    Fvmax = 39810
    lorentzm = 10
    lorentzc = .1
    if lorentzm > lorentzc: #Fast cooling
        if vc > v[listnum]:
            fluence.append(((v[listnum]/vc) ** Fraction('1/3')) * Fvmax)
            #print('a')
        elif vm > v[listnum] and v[listnum] > vc:
            fluence.append(((v[listnum]/vc) ** Fraction('-1/2')) * Fvmax)
            #print('b')
        elif v[listnum] > vm:
            fluence.append(((vm/vc) ** Fraction('-1/2')) * (1/((v[listnum]/vm) ** math.fabs((-p/2)))) * Fvmax)
            #print('c')
        else:
            fluence.append(0)
    elif lorentzc > lorentzm:
        if vm > v[listnum]:
            fluence.append(((v[listnum]/vm) ** Fraction('1/3')) * Fvmax)
            #print('d')
        elif vm > v[listnum] and v[listnum] > vc:
            fluence.append((1/((v[listnum]/vm) ** (math.fabs(1-p/2)))) * Fvmax)
            #print('e')
        elif v[listnum] > vm:
            fluence.append((1/((vc/vm) ** (math.fabs(1-p/2)))) * (1/((v[listnum]/vc) ** math.fabs(-p/2))) * Fvmax)
            #print('f')
        else:
            fluence.append(0)        
    listnum += 1

plt.subplot(223)
plt.ylim(10e-1, 10e5)
plt.loglog(v, fluence)
plt.grid(True)
plt.show()

fluence = []
listnum = 0
for a in range(0,trials):
    #lorentzorig = angletolorentz(theta, thetac, gammac, alphar, betar)
    #energyorig  = angletoenergy(theta, thetac, energyc, alphae, betae)
    lorentzorig = 1000   #CHANGEALBE
    energyorig = 1.5e53    #CHANGEALBE
    energy52, distance28 = energyorig/10e52, distanceincentimeters/10e28
    time = timeindays * 24 * 60 * 60
    B = ((32 * math.pi * mp * epsilonB * nismmeters) ** Fraction('1/2')) * lorentzorig * c
    lorentzc = (3 * me) / (16 * epsilonE * sigmaT * mp * c * time * (lorentzorig ** 3) * nismmeters) #(6 * math.pi * me * c) / (sigmaT * lorentzorig * (B ** 2) * time[listnum])
    lorentzm = epsilonE * (mp/me) * lorentzorig * ((p - 2)/(p - 1))
    'TESTS SHIT HERE'
    vc = 2.7e12 * (epsilonB ** Fraction('-3/2')) * (energy52 ** Fraction('-1/2')) * (nism ** Fraction('-1')) * (timeindays ** Fraction('-1/2'))
    vm = 5.7e14 * (epsilonB ** Fraction('1/2')) * (epsilonE ** 2) * (energy52 ** Fraction('1/2')) *  (timeindays ** Fraction('-3/2'))   
    Fvmax = 1.1e5 * (epsilonB ** Fraction('1/2')) * (energy52) * (nism ** Fraction('1/2')) * (distance28 ** -2)
        
    vc = 16.5e12
    vm = 11e11
    Fvmax = 22239
    lorentzm = .1
    lorentzc = 10
    if lorentzm > lorentzc: #Fast cooling
        if vc > v[listnum]:
            fluence.append(((v[listnum]/vc) ** Fraction('1/3')) * Fvmax)
            #print('a')
        elif vm > v[listnum] and v[listnum] > vc:
            fluence.append(((v[listnum]/vc) ** Fraction('-1/2')) * Fvmax)
            #print('b')
        elif v[listnum] > vm:
            fluence.append(((vm/vc) ** Fraction('-1/2')) * (1/((v[listnum]/vm) ** math.fabs((-p/2)))) * Fvmax)
            #print('c')
        else:
            fluence.append(0)
    elif lorentzc > lorentzm: #slow cooling
        if vm > v[listnum]:
            fluence.append(((v[listnum]/vm) ** Fraction('1/3')) * Fvmax)
            #print('d')
        elif vm < v[listnum] and v[listnum] < vc:
            fluence.append((1/((v[listnum]/vm) ** (math.fabs(1-p/2)))) * Fvmax)
            #print('e')
        elif v[listnum] > vm:
            fluence.append((1/((vc/vm) ** (math.fabs(1-p/2)))) * (1/((v[listnum]/vc) ** math.fabs(-p/2))) * Fvmax)
            #print('f')
        else:
            fluence.append(0)        
    listnum += 1

plt.subplot(223)
plt.ylim(10e-3, 10e5)
plt.loglog(v, fluence)
plt.grid(True)   
plt.show()