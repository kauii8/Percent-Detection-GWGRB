import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as rnd
rnd.seed

def function1(phi_, theta_, pl_, ex_):
    return((pl_ * (((np.cos(phi_))**2) * ((np.cos(theta_))**2) - ((np.sin(phi_))**2)))
    + (2 * ex_ * np.cos(theta_) * np.cos(phi_) * np.sin(phi_)))
    
    
def function2(phi_, theta_, pl_, ex_):
    return((pl_ * (((np.sin(phi_))**2) * ((np.cos(theta_))**2) - ((np.cos(phi_))**2)))
    - (2 * ex_ * np.cos(theta_) * np.cos(phi_) * np.sin(phi_)))

def function3(phi_, theta_, mult_, pl_, ex_):
    return(math.fabs(
    (float(((function1(phi_, theta_, pl_, ex_)) * (cmath.exp(-1j * mult_ * math.pi))
    * ((math.sin(mult_ * math.pi)) + (1j * (math.sin(theta_)) * math.cos(phi_) 
    * math.cos(mult_ * math.pi)) - (1j * math.sin(theta_) * math.cos(phi_) 
    * cmath.exp(-1j * mult_ * math.pi * math.sin(theta_) * math.cos(phi_))))))) / (float(((mult_ * math.pi * (1 - (math.sin(theta_) * math.cos(phi_))**2)))))
    
    - (float(((function2(phi_, theta_, pl_, ex_))
    * (cmath.exp(-1j * mult_ * math.pi))
    * ((math.sin(mult_ * math.pi)) + (1j * math.sin(theta_) * math.sin(phi_) 
    * math.cos(mult_ * math.pi)) - (1j * math.sin(theta_) * math.sin(phi_) 
    * cmath.exp(-1j * mult_ * math.pi * math.sin(theta_) * math.sin(phi_))))))) / (float(((mult_ * math.pi * (1 - (math.sin(theta_) * math.sin(phi_))**2)))))
    ))



'''enable to test any particular location of n vector, 5, 5 are just random numbers I felt like checking
A = function1((math.pi)/2,(math.pi)/2,1,0)
B = function2(math.pi/2,math.pi/2,1,0)
C = function3(5,5,.001,1,0)
print(A)
print(B)
print(C)
'''

'''definitions for plus polarization'''
X, Y, Z = [],[],[]
mult = .001
ex = 0
pl = 1
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
listnump, listnumt = 0, 0
'''creates set of points to graph'''
while phi[listnump] <6.28:
    listnumt = 0
    while theta[listnumt] < 3.14:
        X.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.cos(phi[listnump]) * np.sin(theta[listnumt]))
        Y.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.sin(phi[listnump]) * np.sin(theta[listnumt]))
        Z.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.cos(theta[listnumt]))
        
        listnumt = listnumt + 1
    listnump = listnump + 1





fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(X,Y,Z)
 

plt.show()


'''definitions for cross polarization'''
X, Y, Z = [],[],[]

mult = .001   #you can change the multiplicative property of FSR frequency if wanted, on the Wolfram simulation it is set to .001
ex = 1
pl = 0
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
listnump, listnumt = 0, 0
rho = []
'''creates set of points to graph'''
while phi[listnump] <6.28:
    listnumt = 0
    while theta[listnumt] < 3.14:
        X.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.cos(phi[listnump]) * np.sin(theta[listnumt]))
        Y.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.sin(phi[listnump]) * np.sin(theta[listnumt]))
        Z.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)) * np.cos(theta[listnumt]))
        rho.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)))
        
        listnumt = listnumt + 1
    listnump = listnump + 1



'''
==============
3D scatterplot
==============
'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X,Y,Z)
 

plt.show()


'''
Root mean squared
'''
mult = .001   #you can change the multiplicative property of FSR frequency if wanted, on the Wolfram simulation it is set to .001

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
listnump, listnumt = 0, 0
rho = []
'''creates set of points to graph'''
while phi[listnump] <6.28:
    listnumt = 0
    while theta[listnumt] < 3.14:
        X.append(math.sqrt(((function3(phi[listnump], theta[listnumt], mult, 0, 1))**2) + ((function3(phi[listnump], theta[listnumt], mult, 1, 0))**2)) * np.cos(phi[listnump]) * np.sin(theta[listnumt]))
        Y.append(math.sqrt(((function3(phi[listnump], theta[listnumt], mult, 0, 1))**2) + ((function3(phi[listnump], theta[listnumt], mult, 1, 0))**2)) * np.sin(phi[listnump]) * np.sin(theta[listnumt]))
        Z.append(math.sqrt(((function3(phi[listnump], theta[listnumt], mult, 0, 1))**2) + ((function3(phi[listnump], theta[listnumt], mult, 1, 0))**2)) * np.cos(theta[listnumt]))
        rho.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)))
        
        listnumt = listnumt + 1
    listnump = listnump + 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X,Y,Z)
 

plt.show()


'''
===============
Check for accuracy
===============
'''

predmaxrho = function3(0,0,mult,ex,pl)

if max(rho) == predmaxrho : 
    print('first check sucessful (max value of rho) ')
    print(str(max(rho)) + ' = ' + str(predmaxrho))
else:
    print('first check failed (max value of rho)')    



checklist = [] 
for checkcounter in range(500):
    checklist.append(rnd.choice(rho))

avrandrho = (np.sum(checklist))/(len(checklist))

if 1.8<predmaxrho/avrandrho<2.2:
    print('second check sucessful (2x random vectors = max rho) ')
    print(predmaxrho/avrandrho)
else:
    print('second check failed (2x random vectors = max rho) ')  
    
'''NOTE:
    The actual graph is a scatter plot because I could not find a better way to plot the points
    I tried plotting a surface to make it look cleaner however it did not work with the 1D arrays
    (X,Y,Z). To make this clearer I would have to import something other than matplotlib and I 
    wasn't too familiar with matplotlib in the first place so I figured I'd have trouble. 
    
    However, function3 (the function that calculates the rho if you will) is accurate and has been
    checked with the wolfram program. That is if you were to plug points into both function3 and 
    the wolfram progrom they would yeild the same values. 
'''