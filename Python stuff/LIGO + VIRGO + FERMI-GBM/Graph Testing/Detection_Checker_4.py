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
'''------FUNCTION------'''
'''------CREATE POINTS------'''
trials = 1000 # input("Enter the number of points you want to test: ") + 1
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
    h.append(((((80)**2))/(distance[datacounter] * 2)))
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
    SNRcalculated.append(((((RHO_PLUS_LOUIS[SNRnum])**2) + ((RHO_CROSS_LOUIS[SNRnum]) ** 2)
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
    if thetaobs[listnumt_GRB] <= math.radians(5) and thetaobs[listnumt_GRB] >= -1 * math.radians(5):
        FOn = energy/(( (4/3) * math.pi*((((distance[listnumt_GRB]/2.2435) ** 3)) * (1-math.cos(thetaj)))))
        FOn = FOn/(9.521 * (10**48))
        fluence.append(FOn)
        fluenceonoff.append(True)
    else:
        deltaobs = 1/(gamma * (1 - beta * math.cos(math.radians(thetaobs[listnumt_GRB] - thetaj))))
        deltazero = 1/(gamma * (1 - beta * math.cos(math.fabs((math.radians(0 - thetaj))))))
        eta = deltaobs/deltazero
        FOnn = energy/((4/3)*math.pi*((distance[listnumt_GRB]) ** 3))
        FOff = eta * FOnn
        FOff = FOff / (9.521 *(10**48))
        fluence.append(FOff)
        fluenceonoff.append(False)
    if fluence[listnumt_GRB] < (10e-7):
        GRBTEST.append(False)
    else:
        GRBTEST.append(True)
        GRBTESTnum = GRBTESTnum + 1
    listnumt_GRB = listnumt_GRB + 1
    
'''------GRB CALCULATOR/CHECKER------'''
'''------CROSS CHECK------'''
GW_GRB_TEST = 0
for g in range(0,trials):
    if GWTEST[g] == True and GRBTEST[g] == True:
        GW_GRB_TEST = GW_GRB_TEST + 1
'''------CROSS CHECK------'''
'''------DATA DISPLAY------'''
print(GW_GRB_TEST)
print(GWTESTnum, GRBTESTnum)
print((GWTESTnum * (450**3) * math.pi * (4/3)) / trials)
print((GRBTESTnum * (450**3) * math.pi * (4/3)) / trials)
print((GW_GRB_TEST* (450**3) * math.pi * (4/3)) / trials)

print("First matrix is GRBtest, second is GWtest, third is distance, fourth is rotation angle in radians (orientation) ")
#input('Press enter to close')
'''------DATA DISPLAY------'''