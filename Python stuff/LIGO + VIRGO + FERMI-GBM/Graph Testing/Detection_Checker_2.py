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

def transformrtol(x, w, phi):
    return(math.acos(((-2 * x ** 2) + (2 * x * w * math.cos(phi))) / 
    (-2 * w * math.sqrt((x**2) + (w**2) - 2 * x * w * math.cos(phi)))))

def rotate(l, n):
    return l[n:] + l[:n]
'''------FUNCTION------'''
'''------CREATE POINTS------'''
trials = 100 # input("Enter the number of points you want to test: ") + 1
X_PLUS_LOUIS, Y_PLUS_LOUIS, Z_PLUS_LOUIS, RHO_PLUS_LOUIS, RHO_CROSS_LOUIS = [], [], [], [], []
mult = .001 
phi, theta, distance, rotationpercent, rotationangle, thetaobs, theta_wash, phi_wash = [], [], [], [], [], [], [], []
datacounter = 0 
for a in range(0,trials):
    phi.append(random.uniform(0.0,2 * math.pi))
    theta.append(random.uniform(0.0,math.pi))
    distance.append(random.uniform(0.0,450.0))
    if theta[datacounter] < (math.pi/2):
        theta_wash.append(transformrtol(1.42384e-16, distance[datacounter], (math.pi) + theta[datacounter]))
    else:
        theta_wash.append(transformrtol(1.4238e-16, distance[datacounter], ((3 * math.pi) / 2) - theta[datacounter]))
    
    if ((rotationangle[datacounter] > 0) and (theta[datacounter] > 0)) or ((rotationangle[datacounter] < 0) and (theta[datacounter] < 0)):
        thetaobs.append((math.pi/2) - math.fabs(theta[datacounter]) + math.fabs(rotationangle[datacounter]))
    elif ((rotationangle[datacounter] > 0) and (theta[datacounter] < 0)) or ((rotationangle[datacounter] < 0) and (theta[datacounter] >  0)):
        thetaobs.append((math.pi/2) - math.fabs(theta[datacounter]) - math.fabs(rotationangle[datacounter]))
    elif rotationangle[datacounter] == 0 and theta[datacounter] != 0:
        thetaobs.append((math.pi/2) - math.fabs(theta[datacounter]))
    else:
        thetaobs.append(0)
    rotationpercent.append((rotationangle[datacounter])/(math.pi))    
    if phi[datacounter] < (math.pi/2):
        phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], (math.pi - phi[datacounter])))
    elif (phi[datacounter] > (math.pi/2)) and (phi[datacounter] < (math.pi)):
        phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], ((3 * math.pi)/2) - phi[datacounter]))
    elif (phi[datacounter] > (math.pi)) and (phi[datacounter] < ((3 * math.pi)/2)):
        phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], ((3 * math.pi)/2) - phi[datacounter]))
    elif (phi[datacounter] > ((3 * math.pi)/2)) and (phi[datacounter] < (2 * math.pi)):
        phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], ((2 * math.pi) - phi[datacounter])))
    

    datacounter = datacounter + 1
    
listnump_AP_CR, listnumt_AP_CR, listnump_AP_PL, listnumt_AP_PL = 0, 0, 0, 0
'''------CREATE POINTS-------'''
'''------ANTENNA PATTERNS-------'''
for d in range(0,trials):
        RHO_PLUS_LOUIS.append((function3(phi[listnump_AP_PL], theta[listnumt_AP_PL], mult, 0, 1)))
        #RHO_PLUS_WASH.append((function3()))
        listnumt_AP_PL = listnumt_AP_PL + 1
        listnump_AP_PL = listnump_AP_PL + 1
for e in range(0,trials):
        RHO_CROSS_LOUIS.append((function3(phi[listnump_AP_CR], theta[listnumt_AP_CR], mult, 1, 0)))
        listnumt_AP_CR = listnumt_AP_CR + 1
        listnump_AP_CR = listnump_AP_CR + 1
'''------ANTENNA PATTERNS------'''
'''------SNR CALCULATOR/CHECKER------'''
'''
SNRcalculated, SNRnum, GWTEST = [], 0, []
for f in range(0, trials):
    SNRcalculated.append((math.sqrt(((RHO_PLUS_LOUIS[SNRnum])**2) + ((RHO_CROSS_LOUIS[SNRnum]) ** 2))) * 
    (math.sqrt(INSERTINNE____________________RPRODUCTHERE/2)))
    if SNRcalculated[SNRnum] <= 8:   #NOT SURE IF IT IS < OR >
        GWTEST.append(True)
    else:
        GWTEST.append(False)
    SNRnum=  SNRnum + 1
    SNRnum = SNRnum + 1
'''
'''------SNR CALCULATOR/CHECKER------'''
'''------GRB CALCULATOR/CHECKER------'''
fluence, fluenceonoff, GRBTEST = [], [], []
gamma = 100
energy = 10**50
thetaj = 10
beta = math.sqrt(-((1/(gamma))-1))
listnumt_GRB = 0

for b in range(0,trials):
    if thetaobs[listnumt_GRB] <= 0.174533:
        FOn = energy/(4*math.pi*((distance[listnumt_GRB]) ** 2))
        FOn = FOn/(9.521 * (10**48))
        fluence.append(FOn)
        fluenceonoff.append(True)
    else:
        deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(thetaobs[listnumt_GRB] - thetaj))))
        deltazero = 1/(gamma * (1 - beta * math.cos(math.radians(0 - thetaj))))
        eta = deltaobs/deltazero
        FOn = energy/(4*math.pi*((distance[listnumt_GRB]) ** 2))
        FOff = eta * FOn
        FOff = FOff / (9.521 *(10**48))
        fluence.append(FOff)
        fluenceonoff.append(False)

    if fluence[listnumt_GRB] < (.00001):
        GRBTEST.append(False)
    else:
        GRBTEST.append(True)
    listnumt_GRB = listnumt_GRB + 1

'''------GRB CALCULATOR/CHECKER------'''