'''------IMPORTS-------'''
from __future__ import division
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
    a = (math.acos(((-2 * x ** 2) + (2 * x * w * math.cos(phi))) / 
    (-2 * w * math.sqrt((x**2) + (w**2) - 2 * x * w * math.cos(phi)))))
    return a

def rotate(l, n):
    return l[n:] + l[:n]
    
def standarddev (x, mu, N):
    summ = 0
    for deff in range(0, N):
        adder = (x[deff] - mu) ** 2
        summ = summ + adder
    ret = math.sqrt(summ/(N-1))
    return ret

def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** 1.9))
    return ret
'''------FUNCTION------'''
'''------CREATE POINTS------'''
trials = 100 # input("Enter the number of points you want to test: ") + 1
iterations = 100
GRBFINALnum, GWFINALnum, GWGRBFINALnum = 0, 0, 0
GWPERCENTMEAN, GRBPERCENTMEAN, GWGRBPERCENTMEAN = [], [], []
for q in range(0,iterations):
    X_PLUS_LOUIS, Y_PLUS_LOUIS, Z_PLUS_LOUIS, RHO_PLUS_LOUIS, RHO_CROSS_LOUIS = [], [], [], [], []
    RHO_PLUS_WASH, RHO_CROSS_WASH, RHO_PLUS_VIRGO, RHO_CROSS_VIRGO, frequency, h, PSD = [], [], [], [], [], [], []
    mult = .001 
    phi, theta, distance, rotationpercent, rotationangle, thetaobs, theta_wash, phi_wash, phi_vir, theta_vir = [], [], [], [], [], [], [], [], [], []
    datacounter, GRBTESTnum, GWTESTnum = 0, 0, 0 
    for a in range(0,trials):
        phi.append(random.uniform(0.0,2 * math.pi))
        theta.append(random.uniform(0.0,math.pi))
        distance.append(random.uniform(0.0,450.0))
        rotationangle.append(random.uniform(0, 2 * math.pi))
        rotationpercent.append((rotationangle[a])/(math.pi))
        h.append(((((178)**2))/(distance[a] ** 2)))
        #Fermi Observation angle set
        if ((rotationangle[a] > 0) and (theta[a] > 0)) or ((rotationangle[a] < 0) and (theta[a] < 0)):
            thetaobs.append((math.pi/2) - math.fabs(theta[a]) + math.fabs(rotationangle[a]))
        elif ((rotationangle[a] > 0) and (theta[a] < 0)) or ((rotationangle[a] < 0) and (theta[a] >  0)):
            thetaobs.append((math.pi/2) - math.fabs(theta[a]) - math.fabs(rotationangle[a]))
        elif rotationangle[a] == 0 and theta[a] != 0:
            thetaobs.append((math.pi/2) - math.fabs(theta[a]))
        else:
            thetaobs.append(0)
    listnum_AP_CR, listnum_AP_PL = 0, 0

    '''------CREATE POINTS-------'''
    '''------ANTENNA PATTERNS-------'''
    for d in range(0,trials):
            RHO_PLUS_LOUIS.append((function3(phi[d], theta[d], mult, 0, 1)))
            RHO_PLUS_WASH = rotate(RHO_PLUS_LOUIS, 1347) #CHECK THIS!!!
            RHO_PLUS_VIRGO = rotate(RHO_PLUS_LOUIS, 849) #CHECK THIS!!!
    for e in range(0,trials):
            RHO_CROSS_LOUIS.append((function3(phi[e], theta[e], mult, 1, 0)))
            RHO_CROSS_WASH = rotate(RHO_PLUS_LOUIS, 1347)
            RHO_CROSS_VIRGO = rotate(RHO_PLUS_LOUIS, 849)
    '''------ANTENNA PATTERNS------'''
    '''------SNR CALCULATOR/CHECKER------'''
    SNRcalculated, SNRnum, GWTEST = [], 0, []
    for f in range(0, trials):
        SNRcalculated.append(2 * ((((RHO_PLUS_LOUIS[f])**2) + ((RHO_CROSS_LOUIS[f]) ** 2)
        + ((RHO_PLUS_WASH[f]) ** 2) + ((RHO_CROSS_WASH[f]) ** 2) + ((RHO_PLUS_VIRGO[f]) ** 2)
        + ((RHO_CROSS_VIRGO[f]) ** 2)) * h[f]))
        if SNRcalculated[f] >= 64:
            GWTEST.append(True)
            GWTESTnum += 1
        else:
            GWTEST.append(False)
    '''------SNR CALCULATOR/CHECKER------'''
    '''------GRB CALCULATOR/CHECKER------'''
    fluence, fluenceonoff, GRBTEST = [], [], []
    gamma = 100
    energyinitial = 10**50
    thetaj = 10
    beta = math.sqrt(-((1/(gamma))-1))
    listnumt_GRB = 0

    for a in range(0,trials):
        if thetaobs[a] <= math.radians(5) and thetaobs[a] >= -1 * math.radians(5):
            FOn = (energyinitial)/(( (4) * math.pi*((((distance[a]) ** 2)))))
            FOn = FOn/(9.521 * (10**48))
            fluence.append(FOn)
            fluenceonoff.append(True)
        else:
            '''------OFF AXIS------'''

            deltaobs = (gamma * (1 - beta * math.cos(math.radians(math.degrees(thetaobs[a]) - thetaj))))
            deltazero = (gamma * (1 - beta * math.cos(math.fabs((math.radians(thetaj))))))
            eta = (deltazero/deltaobs)
            FOnn = (energyinitial)/(( (4) * math.pi*((((distance[a]) ** 2)))))
            FOff = eta * FOnn * .01
            FOff = FOff / (9.521 *(10**48))
            fluence.append(FOff)
            fluenceonoff.append(False)
            '''------OFF AXIS------'''            
        if fluence[a] < (10e-7):
            GRBTEST.append(False)
        else:
            GRBTEST.append(True)    
            GRBTESTnum += 1
    '''------GRB CALCULATOR/CHECKER------'''
    '''------GRB CALCULATOR/CHECKER------'''
    '''------CROSS CHECK------'''
    GWGRBTESTnum = 0
    for g in range(0,trials):
        if GWTEST[g] == True and GRBTEST[g] == True:
            GWGRBTESTnum = GWGRBTESTnum + 1
    '''------CROSS CHECK------'''
    '''------MEAN AND SD AND GRAPH------'''
    GWFINALnum = GWFINALnum + GWTESTnum
    GRBFINALnum = GRBFINALnum + GRBTESTnum
    GWGRBFINALnum = GWGRBFINALnum + GWGRBTESTnum
    GWPERCENTMEAN.append(GWTESTnum/trials)
    GRBPERCENTMEAN.append(GRBTESTnum/trials)
    GWGRBPERCENTMEAN.append(GWGRBTESTnum/trials)
GWPERCENT = GWFINALnum/ (iterations * trials)
GRBPERCENT = GRBFINALnum/ (iterations * trials)
GWGRBPERCENT = GWGRBFINALnum/ (iterations * trials)
GWSD = standarddev(GWPERCENTMEAN, GWPERCENT, iterations)
GRBSD = standarddev(GRBPERCENTMEAN, GRBPERCENT, iterations)
GWGRBSD = standarddev(GWGRBPERCENTMEAN, GWGRBPERCENT, iterations)
'''------MEAN AND SD AND GRAPH------'''
'''------DATA DISPLAY------'''
print(' ')
print('GW PERCENT ' + str(GWPERCENT) + '        GRB PERCENT ' + str(GRBPERCENT) + '        GWGRB PERCENT ' + str(GWGRBPERCENT))
print(' ')
print('GW ' + str(GWFINALnum) + '        GRB ' + str(GRBFINALnum) + '        GWGRB ' + str(GWGRBFINALnum) + '        TOTAL ' + str(iterations * trials))
print(' ')
print('GW STANDARD DEVIATION ' + str(GWSD) + '        GRB STANDARD DEVIATION ' + str(GRBSD) + '        GWGRB STANDARD DEVIATION ' + str(GWGRBSD))
print(' ')
print('GW Volume '+ str(((((450)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3))) + ' +/- ' + str(((((450)**3) * math.pi * (4/3) * GWSD)/(1000**3))))
print('GRB Volume '+ str((((450)**3) * math.pi * (4/3) * GRBPERCENT)/(1000**3)) + ' +/- ' + str(((((450)**3) * math.pi * (4/3) * GRBSD))/(1000**3)))
print('GWGRB Volume '+ str((((450)**3) * math.pi * (4/3) * GWGRBPERCENT)/(1000**3)) + ' +/- ' + str(((((450)**3) * math.pi * (4/3) * GWGRBSD))/(1000**3)))
print('All volumes in Gpc^3')
print(' ')
print('GWGRB/GW, percent detection ' + str(100 * ((((450)**3) * math.pi * (4/3) * GWGRBPERCENT)/(1000**3))/(((((450)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3)))))
#input('Press enter to close')
'''------DATA DISPLAY------'''
'''------GRAPHS------'''
'''------GRAPHS------'''