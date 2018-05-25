# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:47:23 2018

@author: gupte
"""
import math
'''
def betaf(gamma_):
    a = math.sqrt(-((1/(gamma_))-1))
    return a
    
def deltaf(thetaobs_, beta_, thetaj_):
    b = 1/(30(1 - beta_ * math.cos(math.radians(thetaobs_ - thetaj_))))
    return b
    
def etaf(deltaobs_, deltazero_):
    c = deltaobs_/deltazero_
    return c
    
def FOnf(energy_, distance_):
    d = energy_/(4*math.pi((distance_)^2))
    return d
    
def FOfff(eta_, FOn_):
    e = eta_ * FOn_
    return e
'''
gamma = float(input('Please enter the Lorentz gamma factor '))
thetaobs = float(input('Please enter the off angle axis (in degrees) '))
distance = float(input('Please enter the distance (in Mpc) '))
energy = 1e51
thetaj = float(input('Please enter the jet opening half-angle (between 3-10 degrees) '))

beta = math.sqrt(-((1/(gamma))-1))
deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(thetaobs - thetaj))))
deltazero = 1/(gamma * (1 - beta * math.cos(math.radians(0 - thetaj))))
eta = deltaobs/deltazero
FOn = energy/(4*math.pi*((distance * 3.086e24) ** 2))
FOff = eta * FOn

print(eta)
print(FOff)

