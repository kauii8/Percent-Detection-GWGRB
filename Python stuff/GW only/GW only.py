from __future__ import division

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import pylab

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

def standarddev (x, mu, N):
    summ = 0
    for deff in range(0, N):
        adder = (x[deff] - mu) ** 2
        summ = summ + adder
    ret = math.sqrt(summ/(N-1))
    return ret

def VolumeSphere(r):
    ret = (4/3) * math.pi * (r ** 3)
    return ret

def VolumeShell(min, max):
    ret = VolumeSphere(max) - VolumeSphere(min)
    return ret

def VolumeGpc(min, max, percent):
    ret = str((VolumeShell(min, max) * percent) / (1000 ** 3))
    return ret

def AntennaPowerSingle(theta, phi):
    ret = ((1/4) * ((1 + (math.cos(theta) ** 2)) ** 2) * (math.cos(2 * phi) ** 2)) + ((math.cos(theta) ** 2) * (math.sin(2 * phi) ** 2))
    return ret

Dv_LOUIS, Dv_WASH, Dv_VIRGO = 190, 190, 145
trials = 100 # input("Enter the number of points you want to test: ") + 1
iterations = 100
GWPERCENTMEAN, GWFINALnum = [], 0
minDistance = 0 #Min distance of generation in Mpc
maxDistance = 450 #Max distance of generation in Mpc

antennaPowerPatternLouis = []
antennaPowerPatternSingle = []
inclinationMultiplier = []
for q in range(0,iterations):
    RHO_PLUS_LOUIS, RHO_CROSS_LOUIS, RHO_PLUS_WASH, RHO_CROSS_WASH, RHO_PLUS_VIRGO, RHO_CROSS_VIRGO = [], [], [], [], [], []
    a_AP_LOUIS, a_AP_WASH, a_AP_VIRGO, b_AP_LOUIS, b_AP_WASH, b_AP_VIRGO = [], [], [], [], [], []
    h_LOUIS, h_WASH, h_VIRGO, reach = [], [], [], []
    phi, theta, distance, rotationpercent, rotationangle, thetaobs, psi = [], [], [], [], [], [], []
    GRBTESTnum_off, GRBTESTnum_struc_best, GRBTESTnum_struc_sim = 0, 0, 0
    GWTESTnum = 0

    #Phi and Theta uniformly distributed 
    for z in range(0,trials): # binary neutron star merger creation
        distance.append(random.uniform(minDistance,maxDistance))
        h_LOUIS.append(((((Dv_LOUIS * 12)** 2)))/(((distance[z]) ** 2))) #*2.25 to account for average over polarization
        h_WASH.append(((((Dv_WASH * 12)** 2)))/(((distance[z]) ** 2)))
        h_VIRGO.append((((((Dv_VIRGO * 12) ** 2)))/((distance[z]) ** 2)))
        
        psi.append(random.uniform(0,2 * math.pi))
        phi.append(random.uniform(0, 2 * math.pi))
        theta.append(random.uniform(0, math.pi))


        thetaobs.append(random.uniform(0,math.pi/2)) #GRB Observation angle and inclination angle
    '''------CREATE POINTS-------'''
    '''------GW DETECTORS------''' #chi is orientation from East in degrees
    #input different detector locations and orientations, beta and lambda are lattitude and longitude
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

            antennaPowerPatternSingle.append(AntennaPowerSingle(theta[d], phi[d]))
    '''------ANTENNA PATTERNS------'''
    '''------SNR CALCULATOR/CHECKER------'''
    SNRcalculatedLOUISsig, SNRcalculatedWASHsig, SNRcalculatedVIRGOsig, SNRcalculated, GWTEST = [], [], [], [], []
    SNRnum = 0
    for f in range(0, trials):
        inclinationMultiplier.append((1/8) * (1 + (6 * (math.cos(thetaobs[f]) ** 2)) + (math.cos(thetaobs[f]) ** 4))) #Schutz eq 26
        antennaPowerPatternLouis.append(AntennaPowerSingle(theta[f], phi[f]))#((RHO_PLUS_LOUIS[f]**2) + (RHO_CROSS_LOUIS[f] ** 2)))
        #SNRcalculatedLOUISsig.append(math.sqrt(inclinationMultiplier[f] * antennaPowerPatternLouis[f]))
        SNRcalculatedLOUISsig.append(math.sqrt(inclinationMultiplier[f] * ((RHO_PLUS_LOUIS[f]**2) + (RHO_CROSS_LOUIS[f] ** 2)) * h_LOUIS[f]))
        SNRcalculatedWASHsig.append(math.sqrt(inclinationMultiplier[f] * ((RHO_PLUS_WASH[f] ** 2) + (RHO_CROSS_WASH[f] ** 2)) * h_WASH[f]))
        SNRcalculatedVIRGOsig.append(math.sqrt(inclinationMultiplier[f] * ((RHO_PLUS_VIRGO[f] ** 2) + (RHO_CROSS_VIRGO[f] ** 2)) * h_VIRGO[f]))


        SNRcalculated.append(math.sqrt((SNRcalculatedLOUISsig[f] ** 2)))#+ (SNRcalculatedWASHsig[f] ** 2# + (SNRcalculatedVIRGOsig[f]**2)))
        #SNRcalculated.append(math.sqrt(antennaPowerPatternLouis[f] * h_LOUIS[f]))
        
        if SNRcalculated[f] >= 12: #network sensitivity in a network of 3 detectors is 12 SNR''
            GWTEST.append(True)
            GWTESTnum += 1  
        else:
            GWTEST.append(False)
    '''------MEAN AND SD AND GRAPH------'''
    GWFINALnum = GWFINALnum + GWTESTnum
    GWPERCENTMEAN.append(GWTESTnum/trials)
    
GWPERCENT = GWFINALnum / (iterations * trials)
GWSD = standarddev(GWPERCENTMEAN, GWPERCENT, iterations)

'''------MEAN AND SD AND GRAPH------'''
'''------SNR CALCULATOR/CHECKER------'''
'''------DATA DISPLAY------'''
#print(antennaPowerPatternLouis)
print('GW PERCENT ' + str(GWPERCENT))
print(' ')
print('GW ' + str(GWFINALnum))
print(' ')
print('GW Volume '+ VolumeGpc(minDistance, maxDistance, GWPERCENT) + ' +/- ' + str((((maxDistance**3) * math.pi * (4/3) * GWSD)/(1000**3))))
# print(VolumeShell(minDistance, maxDistance))
print(max(RHO_CROSS_VIRGO))
print(max(RHO_PLUS_VIRGO))
print(max(antennaPowerPatternSingle))
print(sum(antennaPowerPatternLouis)/len(antennaPowerPatternLouis))
print(max(antennaPowerPatternLouis))
print(sum(inclinationMultiplier)/len(inclinationMultiplier))
print(max(inclinationMultiplier))
# print(max(SNRcalculatedLOUISsig))
# print(max(SNRcalculatedWASHsig))
# print(max(SNRcalculatedVIRGOsig))
# print(max(SNRcalculated))
'''------DATA DISPLAY------'''
