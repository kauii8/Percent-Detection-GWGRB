""" Imports """
import numpy as np
import scipy.integrate as integrate
import math


def offAxisEnergy(_thetaObs, _gamma, _thetaHalf, _distance, _energy):
    
    """ Constants """
    global SPEED_OF_LIGHT, BETA_SUB_BETA, ALPHA_SUB_BETA, SMOOTHNESS, R_SUB_ZERO, T_SUB_ZERO
    SPEED_OF_LIGHT = 299792458 * 100 #cm/s

    BETA_SUB_BETA = -2.2

    ALPHA_SUB_BETA = -1

    SMOOTHNESS = 1

    R_SUB_ZERO = 1e13 #cm/s

    T_SUB_ZERO = 2 #seconds

    #Defines variables we came in with
    global thetaObs, gamma, thetaHalf, distance, scalingEnergy
    thetaObs = _thetaObs
    gamma = _gamma
    thetaHalf = _thetaHalf
    distance = _distance
    scalingEnergy = (_energy/2.4041508820803505e+53) * 7.668789593947251e+18 #Normalization

    global beta, frequencySubZero, T_OBSERVER
    #Not constants but usually will not change
    beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)

    frequencySubZero = 8.4005e3 #Withiin integral limit value doesn't matter so much

    T_OBSERVER = T_SUB_ZERO + (R_SUB_ZERO / (SPEED_OF_LIGHT * beta))


    global tStart, tEnd
    tStart = T_SUB_ZERO + ((R_SUB_ZERO / (SPEED_OF_LIGHT * beta)) * (1 - (beta * math.cos(max(0, thetaObs - thetaHalf))))) #Equation A.5
    tEnd = T_SUB_ZERO + ((R_SUB_ZERO / (SPEED_OF_LIGHT * beta)) * (1 - (beta * math.cos(thetaObs + thetaHalf)))) #Equation A.6

    """ Integral Limits """
    global frequencyMin, frequencyMin
    frequencyMin = 10e3 #eV
    frequencyMax = 25e6 #eV
    #T limit must be placed after thetaObs becacuse it has a thetaObs component

    return 4 * math.pi * (distance ** 2) * (integrate.dblquad(spectralFlux, tStart, tEnd, lambda frequency: frequencyMin, lambda frequency: frequencyMax, epsabs=.1, epsrel=.1)[0]) #Spectral  flux

# Numerical Integration of

# " Can an off-axis gamma-ray burst jet in
# GW170817 explain all the electromagnetic
# counterparts? " --Kunihito Ioka1,∗ and Takashi Nakamura1,2

# Equation #A.4

def polarHalfAngle(thetaT):

    if thetaHalf > thetaObs or 0 < thetaObs <= (thetaHalf - thetaObs): #Paragraph above A.3
        return np.pi

    else: #See above comment
        return np.arccos((math.cos(thetaHalf) - (math.cos(thetaT) * math.cos(thetaObs))) / (math.sin(thetaObs) * math.sin(thetaT)))


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
    

def calcThetaT(time):
    thetaT = math.acos((1/beta) - ((SPEED_OF_LIGHT * (time - T_SUB_ZERO)) / R_SUB_ZERO))
    return thetaT

def spectralFlux(frequency, time):
    thetaT = calcThetaT(time)

    ret = (((2 * R_SUB_ZERO * SPEED_OF_LIGHT * scalingEnergy) / (distance ** 2)) * (deltaFunction(thetaT) ** 2)) * polarHalfAngle(thetaT) * bandSpectrum(frequency / deltaFunction(thetaT))

    return ret 
