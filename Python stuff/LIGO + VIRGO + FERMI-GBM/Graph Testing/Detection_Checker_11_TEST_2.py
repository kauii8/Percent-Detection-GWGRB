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
def AP_PLUS(eta,a,b,psi):
    ret = math.sin(eta) * ((a * math.cos(2 * psi)) + (b * math.sin(2 * psi)))
    return ret
    
def AP_CROSS(eta,a,b,psi):
    ret = math.sin(eta) * ((b * math.cos(2 * psi)) - (a * math.sin(2 * psi)))
    return ret

def afunction(chi, beta, theta, phi, lambd):
    ret = ((1/16) * math.sin(2 * chi) * (3 - math.cos(2 * beta)) * (3 - math.cos(2 * theta))
    * math.cos(2 * (phi + lambd)))
    
    + ((1/4) * math.cos(2 * chi) * math.sin(beta) * (3 - math.cos(2 * theta))
    * math.sin(2 * (phi + lambd)))
    
    + ((1/4) * math.sin(2 * chi) * math.sin(2 * beta) * math.sin(2 * theta) * math.cos(phi + lambd))
    
    + ((1/2) * math.cos(2 * chi) * math.cos(beta) * math.sin(2 * theta) * math.sin(phi + lambd))
    
    + ((3/4) * math.sin(2 * chi) * (math.cos(beta) ** 2) * (math.sin(theta) ** 2))
    return ret
    
def bfunction(chi, beta, theta, phi, lambd):
    ret = (math.cos(2 * chi) * math.sin(beta) * math.cos(theta) * math.cos(2 * (phi + lambd)))
    
    - ((1/4) * math.sin(2 * chi) * (3 - math.cos(2 * beta)) * math.cos(theta) * math.sin(2 * (phi * lambd)))
    
    + (math.cos(2 * chi) * math.cos(beta) * math.sin(theta) * math.cos(phi + lambd))
    
    - ((1/2) * math.sin(2 * chi) * math.sin(2 * beta) * math.sin(theta) * math.sin(phi + lambd))
    return ret

def COMPASS_TO_ANGLE(compassdirection):
    ret = ((5 * math.pi) / 2) - compassdirection
    return ret
    
def DMS_TO_DEGREES(degs, mins, secs):
    ret = degs + (mins/60) + (secs/3600)
    return ret

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
    
def delta_function(gamma, beta, thetaobs, thetaj):
    ret = 1/(gamma * (1 - (beta * math.cos(thetaobs - thetaj))))
    return ret
'''------FUNCTION------'''
'''------CREATE POINTS------'''
Dv = 190
trials = 100 # input("Enter the number of points you want to test: ") + 1
iterations = 100
GRBFINALnum, GWFINALnum, GWGRBFINALnum = 0, 0, 0
GWPERCENTMEAN, GRBPERCENTMEAN, GWGRBPERCENTMEAN = [], [], []
print(afunction(1,1,1,1,1))
for q in range(0,iterations):
    RHO_PLUS_LOUIS, RHO_CROSS_LOUIS, RHO_PLUS_WASH, RHO_CROSS_WASH, RHO_PLUS_VIRGO, RHO_CROSS_VIRGO = [], [], [], [], [], []
    a_AP_LOUIS, a_AP_WASH, a_AP_VIRGO, b_AP_LOUIS, b_AP_WASH, b_AP_VIRGO = [], [], [], [], [], []
    h, reach = [], []
    phi, theta, distance, rotationpercent, rotationangle, thetaobs, psi = [], [], [], [], [], [], []
    datacounter, GRBTESTnum, GWTESTnum = 0, 0, 0
    for z in range(0,trials):
        phi.append(random.uniform(0.0,2 * math.pi))
        theta.append(random.uniform(0.0, math.pi))
        distance.append(random.uniform(0.0,450.0))
        rotationangle.append(random.uniform(0, 2 * math.pi))
        rotationpercent.append((rotationangle[z])/(math.pi))
        h.append(((((Dv * 2.25)**2))/(distance[z] ** 2)))
        psi.append(random.uniform(0,math.pi * 2))
        #Fermi Observation angle set
        if ((rotationangle[z] > 0) and (theta[z] > 0)) or ((rotationangle[z] < 0) and (theta[z] < 0)):
            thetaobs.append((math.pi/2) - math.fabs(theta[z]) + math.fabs(rotationangle[z]))
        elif ((rotationangle[z] > 0) and (theta[z] < 0)) or ((rotationangle[z] < 0) and (theta[z] >  0)):
            thetaobs.append((math.pi/2) - math.fabs(theta[z]) - math.fabs(rotationangle[z]))
        elif rotationangle[z] == 0 and theta[z] != 0:
            thetaobs.append((math.pi/2) - math.fabs(theta[z]))
        else:
            thetaobs.append(0)
        if thetaobs[z] < 0:
            thetaobs[z] += 2 * math.pi
    listnum_AP_CR, listnum_AP_PL = 0, 0

    '''------CREATE POINTS-------'''
    '''------GW DETECTORS------''' #CHANGE THIS TO CLASSES LATER!!!
    eta_AP = math.pi/2
    
    #Livingston Louisiana LIGO
    beta_LOUIS = math.radians(DMS_TO_DEGREES(30,33,46.4))
    lambd_LOUIS = math.radians(DMS_TO_DEGREES(90,46,27.3))
    chi_LOUIS = COMPASS_TO_ANGLE(math.radians(208))
    
    #Hanford Washington LIGO
    beta_WASH = math.radians(DMS_TO_DEGREES(46,27,18.5))
    lambd_WASH = math.radians(DMS_TO_DEGREES(119,24,27.6))
    chi_WASH = COMPASS_TO_ANGLE(math.radians(279))
    
    #VIRGO
    beta_VIRGO = math.radians(DMS_TO_DEGREES(43,37,53))
    lambd_VIRGO = math.radians(DMS_TO_DEGREES(10,30,16))
    chi_VIRGO = COMPASS_TO_ANGLE(math.radians(333.5))
    '''------GW DETECTORS------'''     
    '''------ANTENNA PATTERNS-------'''
    for d in range(0,trials):
            a_AP_LOUIS.append(afunction(chi_LOUIS, beta_LOUIS, theta[d], phi[d], lambd_LOUIS))
            a_AP_WASH.append(afunction(chi_WASH, beta_WASH, theta[d], phi[d], lambd_WASH))
            a_AP_VIRGO.append(afunction(chi_VIRGO, beta_VIRGO, theta[d], phi[d], lambd_VIRGO))
            b_AP_LOUIS.append(bfunction(chi_LOUIS, beta_LOUIS, theta[d], phi[d], lambd_LOUIS))
            b_AP_WASH.append(bfunction(chi_WASH, beta_WASH, theta[d], phi[d], lambd_WASH))
            b_AP_VIRGO.append(bfunction(chi_VIRGO, beta_VIRGO, theta[d], phi[d], lambd_VIRGO))
            
            RHO_PLUS_LOUIS.append(AP_PLUS(eta_AP, a_AP_LOUIS[d], b_AP_LOUIS[d], psi[d]))
            RHO_PLUS_WASH.append(AP_PLUS(eta_AP, a_AP_WASH[d], b_AP_WASH[d], psi[d]))
            RHO_PLUS_VIRGO.append(AP_PLUS(eta_AP, a_AP_VIRGO[d], b_AP_VIRGO[d], psi[d]))
            
            RHO_CROSS_LOUIS.append(AP_CROSS(eta_AP, a_AP_LOUIS[d], b_AP_LOUIS[d], psi[d]))
            RHO_CROSS_WASH.append(AP_CROSS(eta_AP, a_AP_WASH[d], b_AP_WASH[d], psi[d]))
            RHO_CROSS_VIRGO.append(AP_CROSS(eta_AP, a_AP_VIRGO[d], b_AP_VIRGO[d], psi[d]))
    '''------ANTENNA PATTERNS------'''
    '''------SNR CALCULATOR/CHECKER------'''
    SNRcalculated, SNRnum, GWTEST = [], 0, []
    for f in range(0, trials):
        SNRcalculated.append(((((RHO_PLUS_LOUIS[f])**2) + ((RHO_CROSS_LOUIS[f]) ** 2)
        + ((RHO_PLUS_WASH[f]) ** 2) + ((RHO_CROSS_WASH[f]) ** 2) + ((RHO_PLUS_VIRGO[f]) ** 2)
        + ((RHO_CROSS_VIRGO[f]) ** 2)) * h[f]))
        
        if SNRcalculated[f] >= 64:
            GWTEST.append(True)
            GWTESTnum += 1
        else:
            GWTEST.append(False)
    '''------SNR CALCULATOR/CHECKER------'''
    '''------OFF AXIS------'''
    fluence, fluenceonoff, GRBTEST = [], [], []
    gamma = 100
    energyinitial = 10**50
    thetaj = math.radians(10)
    beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)
    listnumt_GRB = 0

    for a in range(0,trials):
        if thetaobs[a] <= math.radians(10):
            FOn = (energyinitial)/(( (4) * math.pi*((((distance[a] * 3.086e+24) ** 2)))))
            fluence.append(FOn)
            fluenceonoff.append(True)
        else:
            eta = delta_function(gamma, beta, thetaobs[a], thetaj)/delta_function(gamma, beta, 0, thetaj)
            FOnn = (energyinitial/eta)/(( (4) * math.pi * ((((distance[a] * 3.086e+24) ** 2)))))
            FOff = eta * FOnn * .00042
            fluence.append(FOff)
            fluenceonoff.append(False)
            '''------OFF AXIS------'''  
            '''------GRB CALCULATOR/CHECKER------'''
        if fluence[a] < (10e-7):
            GRBTEST.append(False)
        else:
            GRBTEST.append(True)    
            GRBTESTnum += 1

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
