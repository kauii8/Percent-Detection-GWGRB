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
trials = 1000
lorentzorig, energyorig, time, timeindays, fluence, timezero, newlist = [], [], [], [], [], [], []
timeindays = np.logspace(-3,3, trials)
timeindays = timeindays.tolist()

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
epsilonB, epsilonE, p, nism = 10e-3, 10e-2, 2.3, 10e-4
nismmeters = converttometers(-1, nism)
R = 10e16
listnum = 0


bleh = 0
for a in range(0,trials):
    #lorentzorig = angletolorentz(theta, thetac, gammac, alphar, betar)
    #energyorig  = angletoenergy(theta, thetac, energyc, alphae, betae)
    lorentzorig = 10e4
    distance28 = distanceincentimeters/10e28
    time.append(timeindays[listnum] * 24 * 60 * 60)
    B = ((32 * math.pi * mp * epsilonB * nismmeters) ** Fraction('1/2')) * lorentzorig * c
    
    lorentzc = (3 * me) / (16 * epsilonE * sigmaT * mp * c * time[listnum] * (lorentzorig ** 3)  * nismmeters) #(6 * math.pi * me * c) / (sigmaT * lorentzorig * (B ** 2) * time[listnum])
    lorentzm = epsilonE * (mp/me) * lorentzorig * ((p - 2)/(p - 1))
    
    energyorig = (16/17) * math.pi * (lorentzorig ** 2) * (R ** 3) * (nism) * mp * (c ** 2)
    energyorig = 10e52
    energy52 = energyorig/10e52
    

    'TESTS SHIT HERE'
    v = 8000000000
    v15 = v/10e15
    vc = 2.7e12 * (epsilonB ** Fraction('-3/2')) * (energy52 ** Fraction('-1/2')) * (nism ** Fraction('-1')) * (timeindays[listnum] ** Fraction('-1/2'))
    vm = 5.7e14 * (epsilonB ** Fraction('1/2')) * (epsilonE ** 2) * (energy52 ** Fraction('1/2')) *  (timeindays[listnum] ** Fraction('-3/2'))   
    v0 = 1.8 * 10e11 * (epsilonB ** Fraction('-5/2')) * (epsilonE ** Fraction('-1')) * (energy52 ** Fraction('-1')) * (nism ** Fraction('-3/2'))    
    
    Fvmax = 1.1e5 * (epsilonB ** Fraction('1/2')) * (energy52) * (nism ** Fraction('1/2')) * (distance28 ** -2)

    t0days = 210 * (epsilonB ** 2) * (epsilonE ** 2) * energy52 * nism
    tcdays = 7.3 * 10e-6 * (1/(epsilonB ** 3)) * (1/(energy52)) * (1/(nism ** 2)) * (1/(v15 ** 2))
    tmdays = .69 * (epsilonB ** Fraction('1/3')) * (epsilonE ** Fraction('4/3')) * (energy52 ** Fraction('1/3')) * (v15 ** Fraction('-2/3'))
 
    if lorentzm > lorentzc: #Fast cooling
        if vc > v:
            fluence.append(((v/vc) ** Fraction('1/3')) * Fvmax)
            #print('a')
        elif vm > v and v > vc:
            fluence.append(((v[listnum]/vc) ** Fraction('-1/2')) * Fvmax)
            #print('b')
        elif v > vm:
            fluence.append(((vm/vc) ** Fraction('-1/2')) * (1/((v/vm) ** math.fabs((-p/2)))) * Fvmax)
            #print('c')
        else:
            fluence.append(0)
    elif lorentzc > lorentzm:
        if vm > v:
            fluence.append(((v/vm) ** Fraction('1/3')) * Fvmax)
           # print('d')
        elif vm < v and v < vc:
            fluence.append((1/((v/vm) ** (math.fabs(1-p/2)))) * Fvmax)
           # print('e')
        elif v > vm:
            fluence.append((1/((vc/vm) ** (math.fabs(1-p/2)))) * (1/((v/vc) ** math.fabs(-p/2))) * Fvmax)
          #  print('f')
        else:
            fluence.append(0)      

    listnum += 1
#GRAPH

plt.subplot(223)
plt.ylim(10e1, 10e6)
plt.loglog(timeindays, fluence)
plt.grid(True)
