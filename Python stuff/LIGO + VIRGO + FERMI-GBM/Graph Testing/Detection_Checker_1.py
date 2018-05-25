'''------IMPORTS-------'''
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from operator import add
import random
'''------IMPORTS-------'''
'''------FUNCTION------'''
def function1(phi_, theta_, pl_, ex_):
    return((pl_ * (((np.cos(phi_))**2) * ((np.cos(theta_))**2) - ((np.sin(phi_))**2)))
    + (2 * ex_ * np.cos(theta_) * np.cos(phi_) * np.sin(phi_)))
    
def function2(phi_, theta_, pl_, ex_):
    return((pl_ * (((np.sin(phi_))**2) * ((np.cos(theta_))**2) - ((np.cos(phi_))**2)))
    - (2 * ex_ * np.cos(theta_) * np.cos(phi_) * np.sin(phi_)))

def function3(phi_, theta_, mult_, pl_, ex_):
    return(math.fabs((
    (float(((function1(phi_, theta_, pl_, ex_)) * (cmath.exp(-1j * mult_ * math.pi))
    * ((math.sin(mult_ * math.pi)) + (1j * (math.sin(theta_)) * math.cos(phi_) 
    * math.cos(mult_ * math.pi)) - (1j * math.sin(theta_) * math.cos(phi_) 
    * cmath.exp(-1j * mult_ * math.pi * math.sin(theta_) * math.cos(phi_))))))) / (float(((mult_ * math.pi * (1 - (math.sin(theta_) * math.cos(phi_))**2)))))
    
    - (float(((function2(phi_, theta_, pl_, ex_))
    * (cmath.exp(-1j * mult_ * math.pi))
    * ((math.sin(mult_ * math.pi)) + (1j * math.sin(theta_) * math.sin(phi_) 
    * math.cos(mult_ * math.pi)) - (1j * math.sin(theta_) * math.sin(phi_) 
    * cmath.exp(-1j * mult_ * math.pi * math.sin(theta_) * math.sin(phi_))))))) / (float(((mult_ * math.pi * (1 - (math.sin(theta_) * math.sin(phi_))**2)))))
    )/2))

def rotate(l, n):
    return l[n:] + l[:n]
'''------FUNCTION------'''
'''------CREATE POINTS------'''
trials = 1000 # input("Enter the number of points you want to test: ") + 1
X_PLUS_LOUIS, Y_PLUS_LOUIS, Z_PLUS_LOUIS, RHO_PLUS_LOUIS = [], [], [], []
mult = .001 
phi, theta, distance, ex, pl = [], [], [], 0, 1
for a in range(0,trials):
    phi.append(random.uniform(0.0,2 * math.pi))
    theta.append(random.uniform(0.0,math.pi))
    distance.append(random.uniform(0.0,450.0))
listnump_AP, listnumt_AP = 0, 0
'''------CREATE POINTS-------'''
'''------ANTENNA PATTERNS-------'''
for d in range(0,trials):
        RHO_PLUS_LOUIS.append((function3(phi[listnump_AP], theta[listnumt_AP], mult, ex, pl)))
        listnumt_AP = listnumt_AP + 1
        listnump_AP = listnump_AP + 1
'''------ANTENNA PATTERNS------'''
'''------GRB CALCULATOR/CHECKER------'''
fluence, fluenceonoff, GRBTEST = [], [], []
gamma = 100
energy = 10**50
thetaj = 10
beta = math.sqrt(-((1/(gamma))-1))
listnumt_GRB = 0

for b in range(0,trials):
    if theta[listnumt_GRB] <= 0.174533:
        FOn = energy/(4*math.pi*((distance[listnumt_GRB]) ** 2))
        FOn = FOn/(9.521 * (10**48))
        fluence.append(FOn)
        fluenceonoff.append(True)
    else:
        deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(theta[listnumt_GRB] - thetaj))))
        deltazero = 1/(gamma * (1 - beta * math.cos(math.radians(0 - thetaj))))
        eta = deltaobs/deltazero
        FOn = energy/(4*math.pi*((distance[listnumt_GRB]) ** 2))
        FOff = eta * FOn
        FOff = FOff / (9.521 *(10**48))
        fluence.append(FOff)
        fluenceonoff.append(False)

    if fluence[listnumt_GRB] < (1/(10**7)):
        GRBTEST.append(False)
    else:
        GRBTEST.append(True)
        listnumt_GRB = listnumt_GRB + 1
print(GRBTEST)
'''------GRB CALCULATOR/CHECKER------'''