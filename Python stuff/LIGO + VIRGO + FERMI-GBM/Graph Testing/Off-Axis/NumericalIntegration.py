""" Just to make it look pretty """
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    #https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


# Numerical Integration of

# " Can an off-axis gamma-ray burst jet in
# GW170817 explain all the electromagnetic
# counterparts? " --Kunihito Ioka1,∗ and Takashi Nakamura1,2

# Equation #A.4

""" Imports """
import numpy as np
import scipy.integrate as integrate
import math
import matplotlib.pyplot as plt
import csv

""" Functions """
def polarHalfAngle(thetaT):

    if thetaHalf > thetaObs[i] or 0 < thetaObs[i] <= (thetaHalf - thetaObs[i]): #Paragraph above A.3
        return np.pi

    else: #See above comment
        return np.arccos((math.cos(thetaHalf) - (math.cos(thetaT) * math.cos(thetaObs[i]))) / (math.sin(thetaObs[i]) * math.sin(thetaT)))

def deltaFunction(thetaT): #Equation A.2
    return 1 / (gamma * (1 - (beta * np.cos(thetaT))))

def bandSpectrum(frequencyPrime): #Equation A.3
    return (    
        (
            frequencyPrime / frequencySubZero
        ) ** (1 + ALPHA_SUB_BETA)
    ) * ((
        1 + (
            (frequencyPrime / frequencySubZero) ** SMOOTHNESS
        )
    ) ** ((BETA_SUB_BETA - ALPHA_SUB_BETA) / SMOOTHNESS))
    

def spectralFlux(frequency, time):
    thetaT = calcThetaT(time)

    ret = (((2 * R_SUB_ZERO * SPEED_OF_LIGHT * SCALING_ENERGY) / (distance ** 2)) * (deltaFunction(thetaT) ** 2)) * polarHalfAngle(thetaT) * bandSpectrum(frequency / deltaFunction(thetaT))

    return ret

def calcThetaT(time):
    thetaT = math.acos((1/beta) - ((SPEED_OF_LIGHT * (time - T_SUB_ZERO)) / R_SUB_ZERO))
    return thetaT

def energyIso(spectralFluxIntegrated):
    return 4 * math.pi * (distance ** 2) * spectralFluxIntegrated[0]

""" Constants """
global SPEED_OF_LIGHT
SPEED_OF_LIGHT = 299792458 * 100 #cm/s

global BETA_SUB_BETA
BETA_SUB_BETA = -2.2

global ALPHA_SUB_BETA
ALPHA_SUB_BETA = -1

global SMOOTHNESS
SMOOTHNESS = 1

global SCALING_ENERGY
SCALING_ENERGY = 7.668789593947251e+18 #1.5568789593947251e+18 #Normalization

global R_SUB_ZERO   
R_SUB_ZERO = 1e13 #cm/s

global T_SUB_ZERO
T_SUB_ZERO = 2 #seconds

""" Integral Limits """
frequencyMin = 10e3 #eV
frequencyMax = 25e6 #eV
#T limit must be placed after thetaObs becacuse it has a thetaObs component


""" Not Constants but usually will not change """
global gamma 
gamma = 100

global thetaHalf 
thetaHalf = math.radians(15) #NOTE IN RADIANS ALREADY

global beta 
beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)

global frequencySubZero
frequencySubZero = .84005e4#12505000 #Withiin integral limit value doesn't matter so much

global distance
distance = 100 * 3.086e+24 #cm

global T_OBSERVER
T_OBSERVER = T_SUB_ZERO + (R_SUB_ZERO / (SPEED_OF_LIGHT * beta))

""" Variable Initializations """
global thetaObs

trials = 100
thetaObs = np.linspace(0, math.radians(60), trials).tolist()

global i

energy = []
print("Progress")
for i in range(0, len(thetaObs)): #Calculates the integral for every thetaObs
    tStart = T_SUB_ZERO + ((R_SUB_ZERO / (SPEED_OF_LIGHT * beta)) * (1 - (beta * math.cos(max(0, thetaObs[i] - thetaHalf))))) #Equation A.5
    tEnd = T_SUB_ZERO + ((R_SUB_ZERO / (SPEED_OF_LIGHT * beta)) * (1 - (beta * math.cos(thetaObs[i] + thetaHalf)))) #Equation A.6

    spectralFluxIntegrated = integrate.dblquad(spectralFlux, tStart, tEnd, lambda frequency: frequencyMin, lambda frequency: frequencyMax) #Spectral   flux integral

    energy.append(energyIso(spectralFluxIntegrated))
    
    printProgressBar(i, trials)

for i in range(0,len(thetaObs)):
    thetaObs[i] = math.degrees(thetaObs[i])

""" CSV file """
path = "/media/n/OS/Users/Nihar/Documents/Everything/Research/LIGO/Percent-Detection-GWGRB/Python stuff/LIGO + VIRGO + FERMI-GBM/Graph Testing/Off-Axis/Nakamura.csv"

file = open(path, newline = '')
reader = csv.reader(file)

nakamuraTheta, nakamuraEnergy = [], []
for row in reader:
    nakamuraTheta.append(float(row[0]))
    nakamuraEnergy.append(float(row[1]))

myGraph = plt.plot(thetaObs, energy, label = "My data")
nakamuraGraph = plt.plot(nakamuraTheta, nakamuraEnergy, label = "Nakamura and Ioka data")
plt.xlim(0, 60)
plt.yscale('log')
plt.legend()

plt.title("Viewing angle vs Isotropic Energy of Off-Axis emission")
plt.xlabel("Viewing Angle " +r'$\theta_{obs}$' + " of the jet")
plt.ylabel(r'$E_{iso}(\theta_{obs})$' + "[erg] (10keV - 25MeV)")
plt.grid(axis = "both")

plt.show()
