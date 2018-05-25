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

def vfreq(lorentzmaterial, lorentz, B):
    ret = math.fabs(lorentzmaterial * (lorentz ** 2) * 1.60217662e10-19 * (B/(math.pi * 2 * 9.10938356e-31 * 299792458))) 
    return ret
    #NOTE IF LORENTZ OF SURROUNDING MATERIAL IS DIFFERENT CHANGE THE 1.7!!!
'''------FUNCTION------'''
'''------DEFINITIONS FOR STRUCTURED JET------'''
epsilonE, epsilonB, pe, nism = .02, .002, 2/13, 1.2e-5
sigmaT = 6.6524587158e-29
tobs, lorentzcritical, vcritical, lorentzmin, lorentzmaterial, vmaterial, vmin, Pvmax, Bfield = [], [], [], [], [], [], [], [], []
numelectron = (4/3) * math.pi * nism * (10000) 
'''------DEFINITIONS FOR STRUCTURED JET------'''
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
        rotationangle.append(random.uniform((-1 * math.pi) / 2, math.pi/2))
        rotationpercent.append((rotationangle[datacounter])/(math.pi))
        h.append(((((178)**2))/(distance[datacounter] ** 2)))
        #Fermi Observation angle set
        if ((rotationangle[datacounter] > 0) and (theta[datacounter] > 0)) or ((rotationangle[datacounter] < 0) and (theta[datacounter] < 0)):
            thetaobs.append((math.pi/2) - math.fabs(theta[datacounter]) + math.fabs(rotationangle[datacounter]))
        elif ((rotationangle[datacounter] > 0) and (theta[datacounter] < 0)) or ((rotationangle[datacounter] < 0) and (theta[datacounter] >  0)):
            thetaobs.append((math.pi/2) - math.fabs(theta[datacounter]) - math.fabs(rotationangle[datacounter]))
        elif rotationangle[datacounter] == 0 and theta[datacounter] != 0:
            thetaobs.append((math.pi/2) - math.fabs(theta[datacounter]))
        else:
            thetaobs.append(0)
        datacounter = datacounter + 1
    '''    
        #Washington Theta Phi set    
        if theta[datacounter] < (math.pi/2):
            theta_wash.append(transformrtol(1.42384e-16, distance[datacounter], (math.pi) + theta[datacounter]))
        else:
            theta_wash.append(transformrtol(1.4238e-16, distance[datacounter], ((3 * math.pi) / 2) - theta[datacounter]))      
        if phi[datacounter] < (math.pi/2):
            phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], (math.pi - phi[datacounter])))
        elif (phi[datacounter] > (math.pi/2)) and (phi[datacounter] < (math.pi)):
            phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], ((3 * math.pi)/2) - phi[datacounter]))
        elif (phi[datacounter] > (math.pi)) and (phi[datacounter] < ((3 * math.pi)/2)):
            phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], ((3 * math.pi)/2) - phi[datacounter]))
        elif (phi[datacounter] > ((3 * math.pi)/2)) and (phi[datacounter] < (2 * math.pi)):
            phi_wash.append(transformrtol(5.62234e-17, distance[datacounter], ((2 * math.pi) - phi[datacounter])))
    
        #VIRGO Theta Phi set
        if theta[datacounter] < (math.pi/2):
            theta_vir.append((math.pi)-transformrtol(3.07768e-16, distance[datacounter], (math.pi) + theta[datacounter]))
        else:
            theta_vir.append(math.pi-transformrtol(3.07768e-16, distance[datacounter], ((3 * math.pi) / 2) - theta[datacounter]))      
        if phi[datacounter] < (math.pi/2):
            phi_vir.append(math.pi-transformrtol(4.6001e-17, distance[datacounter], (math.pi - phi[datacounter])))
        elif (phi[datacounter] > (math.pi/2)) and (phi[datacounter] < (math.pi)):
            phi_vir.append(math.pi-transformrtol(4.6001e-17, distance[datacounter], ((3 * math.pi)/2) - phi[datacounter]))
        elif (phi[datacounter] > (math.pi)) and (phi[datacounter] < ((3 * math.pi)/2)):
            phi_vir.append(math.pi-transformrtol(4.6001e-17, distance[datacounter], ((3 * math.pi)/2) - phi[datacounter]))
        elif (phi[datacounter] > ((3 * math.pi)/2)) and (phi[datacounter] < (2 * math.pi)):
            phi_vir.append(math.pi-transformrtol(4.6001e-17, distance[datacounter], ((2 * math.pi) - phi[datacounter])))
        else:
            print(1)
    '''    
    listnum_AP_CR, listnum_AP_PL = 0, 0
    '''------CREATE POINTS-------'''
    '''------ANTENNA PATTERNS-------'''
    for d in range(0,trials):
            RHO_PLUS_LOUIS.append((function3(phi[listnum_AP_PL], theta[listnum_AP_PL], mult, 0, 1)))
            RHO_PLUS_WASH = rotate(RHO_PLUS_LOUIS, 1347)
            RHO_PLUS_VIRGO = rotate(RHO_PLUS_LOUIS, 849)
            #RHO_PLUS_WASH.append((function3(phi_wash[listnum_AP_PL], theta[listnum_AP_PL], mult, 0, 1)))
            #RHO_PLUS_VIRGO.append((function3(phi_vir[listnum_AP_PL], theta[listnum_AP_PL], mult, 0, 1)))
            listnum_AP_PL = listnum_AP_PL + 1
    for e in range(0,trials):
            RHO_CROSS_LOUIS.append((function3(phi[listnum_AP_CR], theta[listnum_AP_CR], mult, 1, 0)))
            RHO_CROSS_WASH = rotate(RHO_PLUS_LOUIS, 1347)
            RHO_CROSS_VIRGO = rotate(RHO_PLUS_LOUIS, 849)
            #RHO_PLUS_WASH.append((function3(phi_wash[listnum_AP_PL])), theta[listnum_AP_PL], mult, 1, 0)
            #RHO_PLUS_VIRGO.append((function3(phi_vir[listnum_AP_PL])), theta[listnum_AP_PL], mult, 1, 0)
            listnum_AP_CR = listnum_AP_CR + 1
    '''------ANTENNA PATTERNS------'''
    '''------SNR CALCULATOR/CHECKER------'''
    SNRcalculated, SNRnum, GWTEST = [], 0, []
    for f in range(0, trials):
        SNRcalculated.append(2 * ((((RHO_PLUS_LOUIS[SNRnum])**2) + ((RHO_CROSS_LOUIS[SNRnum]) ** 2)
        + ((RHO_PLUS_WASH[SNRnum]) ** 2) + ((RHO_CROSS_WASH[SNRnum]) ** 2) + ((RHO_PLUS_VIRGO[SNRnum]) ** 2)
        + ((RHO_CROSS_VIRGO[SNRnum]) ** 2)) * h[SNRnum]))
        if SNRcalculated[SNRnum] >= 64:
            GWTEST.append(True)
            GWTESTnum = GWTESTnum + 1
        else:
            GWTEST.append(False)
        SNRnum=  SNRnum + 1
    '''------SNR CALCULATOR/CHECKER------'''
    '''------GRB CALCULATOR/CHECKER------'''
    fluence, fluenceonoff, GRBTEST = [], [], []
    gamma = 100
    energy = 10**50
    thetaj = 10
    beta = math.sqrt(-((1/(gamma))-1))
    listnumt_GRB = 0



    for b in range(0,trials):
        '''------STRUCTURED JETS GENERATION------'''
        tobs.append((1/299792458) * (distance[listnumt_GRB] * 3.086e+22))
        lorentzmaterial.append((math.fabs(math.sin(math.radians((thetaobs[listnumt_GRB]/2)))) ** (1/7)) * 17400 )
        Bfield.append((math.sqrt(32 * math.pi * 1.6726219e-27 * epsilonB * nism)) * lorentzmaterial[listnumt_GRB] * 299792458)
        lorentzmin.append(epsilonE * ((pe-2)/(pe-1)) * (1.6726219e-27/9.10938356e-31))
        vmaterial.append(vfreq(lorentzmaterial[listnumt_GRB], lorentzmaterial[listnumt_GRB], Bfield[listnumt_GRB]))
        vmin.append(vfreq(lorentzmaterial[listnumt_GRB], lorentzmin[listnumt_GRB], Bfield[listnumt_GRB]))
        Pvmax.append((9.10938356e-31 * (299792458 ** 2) * sigmaT * lorentzmaterial[listnumt_GRB] * Bfield[listnumt_GRB]) / (3 * 1.60217662e10-19))
        lorentzcritical.append((6 * math.pi * 9.10938356e-31 * 299792458) / (sigmaT * lorentzmaterial[listnumt_GRB] * (Bfield[listnumt_GRB] ** 2) * tobs[listnumt_GRB]))
        vcritical.append(vfreq(lorentzmaterial[listnumt_GRB], lorentzcritical[listnumt_GRB], Bfield[listnumt_GRB]))
        '''------STRUCTURED JETS GENERATION------'''
        
        if thetaobs[listnumt_GRB] <= math.radians(5) and thetaobs[listnumt_GRB] >= -1 * math.radians(5):
            FOn = (energy)/(( (4/3) * math.pi*((((distance[listnumt_GRB]) ** 3)))))
            FOn = FOn/(9.521 * (10**48))
            fluence.append(FOn)
            fluenceonoff.append(True)
        else:
            '''------STRUCTURED JETS------'''
            if lorentzmin > lorentzcritical[listnumt_GRB]:
                if vcritical[listnumt_GRB] > vmaterial:
                    Fvmax = (numelectron * Pvmax[listnumt_GRB]) / (4 * math.pi * (distance[listnumt_GRB] ** 2))
                    fluence.append(((vmaterial/vcritical[listnumt_GRB]) ** (1/3)) * Fvmax  * 9.52140614e48 * 10e7)
                    print('q')
                elif vmin > vmaterial > vcritical[listnumt_GRB]:
                    Fvmax = (numelectron * Pvmax[listnumt_GRB]) / (4 * math.pi * (distance[listnumt_GRB] ** 2))
                    fluence.append(((vmaterial/vcritical[listnumt_GRB]) ** (-1/2)) * Fvmax  * 9.52140614e48  * 10e7)
                    print('qq')
                elif vmaterial > vmin:
                    Fvmax = (numelectron * Pvmax[listnumt_GRB]) / (4 * math.pi * (distance[listnumt_GRB] ** 2))
                    fluence.append(((vmin[listnumt_GRB]/vcritical[listnumt_GRB]) ** (-1/2)) * ((vmaterial[listnumt_GRB]/vmin[listnumt_GRB]) ** (pe - 2)) * Fvmax * 9.52140614e48  * 10e7)
                    print('qqq')
                else:
                    fluence.append(0)                    
            elif lorentzmin <= lorentzcritical[listnumt_GRB]:
                if vmin > vmaterial:
                    Fvmax = (numelectron * Pvmax[listnumt_GRB]) / (4 * math.pi * (distance[listnumt_GRB] ** 2))
                    fluence.append(((vmaterial/vmin) ** (1/3)) * Fvmax  * 9.52140614e48 * 10e7)
                elif vcritical[listnumt_GRB] > vmaterial > vmin:
                    Fvmax = (numelectron * Pvmax[listnumt_GRB]) / (4 * math.pi * (distance[listnumt_GRB] ** 2))
                    fluence.append(((vmaterial/vmin) ** ((1-pe)/2)) * Fvmax  * 9.52140614e48  * 10e7)
                    print('qq')
                elif vmaterial > vcritical[listnumt_GRB]:
                    Fvmax = (numelectron * Pvmax[listnumt_GRB]) / (4 * math.pi * (distance[listnumt_GRB] ** 2))
                    fluence.append(((vcritical[listnumt_GRB]/vmin) ** ((1-pe)/2)) * ((vmaterial/vcritical[listnumt_GRB]) ** ((-1 * pe)/2)) * Fvmax * 9.52140614e48  * 10e7)
                    print('qqqq')
                else:
                    fluence.append(0) 
 #       if fluence[listnumt_GRB] < 10e-30:
  #          print(fluence[listnumt_GRB], lorentzmin, lorentzcritical, listnumt_GRB)
            '''------STRUCTURED JETS------'''
            '''------OFF AXIS------'''
            '''
            deltaobs = (gamma * (1 - beta * math.cos(math.radians(math.degrees(thetaobs[listnumt_GRB]) - thetaj))))
            deltazero = (gamma * (1 - beta * math.cos(math.fabs((math.radians(thetaj))))))
            eta = (deltazero/deltaobs) * .01
            FOnn = (energy)/(( (4/3) * math.pi*((((distance[listnumt_GRB]) ** 3)))))
            FOff = eta * FOnn 
            FOff = FOff / (9.521 *(10**48))
            fluence.append(FOff)
            fluenceonoff.append(False)
            '''
            '''------OFF AXIS------'''            
        if fluence[listnumt_GRB] < (10e-7):
            GRBTEST.append(False)
        else:
            GRBTEST.append(True)
            GRBTESTnum = GRBTESTnum + 1
        listnumt_GRB = listnumt_GRB + 1
        
    '''------GRB CALCULATOR/CHECKER------'''
    '''------CROSS CHECK------'''
    GWGRBTESTnum = 0
    for g in range(0,trials):
        if GWTEST[g] == True and GRBTEST[g] == True:
            GWGRBTESTnum = GWGRBTESTnum + 1
    '''------CROSS CHECK------'''
    '''------MEAN AND SD------'''
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
'''------MEAN AND SD------'''
'''------DATA DISPLAY------'''
print('GW PERCENT ' + str(GWPERCENT) + '        GRB PERCENT ' + str(GRBPERCENT) + '        GWGRB PERCENT ' + str(GWGRBPERCENT))
print('GW ' + str(GWFINALnum) + '        GRB ' + str(GRBFINALnum) + '        GWGRB ' + str(GWGRBFINALnum) + '        TOTAL ' + str(iterations * trials))
print('GW STANDARD DEVIATION ' + str(GWSD) + '        GRB STANDARD DEVIATION ' + str(GRBSD) + '        GWGRB STANDARD DEVIATION ' + str(GWGRBSD))
print('GW Volume '+ str(((((450)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3))) + ' +/- ' + str(((((450)**3) * math.pi * (4/3) * GWSD)/(1000**3))))
print('GRB Volume '+ str((((450)**3) * math.pi * (4/3) * GRBPERCENT)/(1000**3)) + ' +/- ' + str(((((450)**3) * math.pi * (4/3) * GRBSD))/(1000**3)))
print('GWGRB Volume '+ str((((450)**3) * math.pi * (4/3) * GWGRBPERCENT)/(1000**3)) + ' +/- ' + str(((((450)**3) * math.pi * (4/3) * GWGRBSD))/(1000**3)))
print('All volumes in Gpc^3')
#input('Press enter to close')
'''------DATA DISPLAY------'''