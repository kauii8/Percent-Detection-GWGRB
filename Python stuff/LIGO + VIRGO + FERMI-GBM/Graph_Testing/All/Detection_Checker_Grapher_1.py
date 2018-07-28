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
'''------CREATE POINTS------'''
trials = 1000 # input("Enter the number of points you want to test: ") + 1
iterations = 100
GRBFINALnum, GWFINALnum, GWGRBFINALnum = 0, 0, 0
fluence, fluenceonoff, theta = [], [], []
'''------CREATE POINTS-------'''
'''------GRB CALCULATOR/CHECKER------'''
gamma = 100
energy = 10**50
thetaj = 10
beta = math.sqrt(-((1/(gamma))-1))
listnumt_GRB = 0
distance = 40
for b in range(0,trials):        
    theta.append(random.uniform(0.0,math.pi))
    if theta[listnumt_GRB] <= math.radians(5) and theta[listnumt_GRB] >= -1 * math.radians(5):
        FOn = (energy)/(( (4/3) * math.pi*((((distance) ** 3)))))
        FOn = FOn/(9.521 * (10**48))
        fluence.append(FOn)
        fluenceonoff.append(True)
    else:
        '''------OFF AXIS------'''
        deltaobs = (gamma * (1 - beta * math.cos(math.radians(math.degrees(theta[listnumt_GRB]) - thetaj))))
        deltazero = (gamma * (1 - beta * math.cos(math.fabs((math.radians(thetaj))))))
        eta = (deltazero/deltaobs) * .01
        FOnn = (energy)/(( (4/3) * math.pi*((((distance) ** 3)))))
        FOff = eta * FOnn 
        FOff = FOff / (9.521 *(10**48))
        fluence.append(FOff)
        fluenceonoff.append(False)
        '''------OFF AXIS------'''            

'''------GRAPH------'''
plt.xlim(0, math.pi)
plt.ylim(10e-8, 10e-4)
plt.scatter(theta, fluence)
plt.show()
'''------GRAPH------'''