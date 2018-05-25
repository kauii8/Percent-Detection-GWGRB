import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from operator import add


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

def square(list_):
    returnlist = []
    for i in list_:
        returnlist.append(i ** 2)
    return returnlist

def squareroot(list_):
    returnlist = []
    for i in list_:
        returnlist.append(i ** 1/2)
    return returnlist

def rootsumsquare(h1_, h2_):
    return(math.sqrt((h1_)**2 + (h2_)**2))

def rotate(l, n):
    return l[n:] + l[:n]




'''enable to test any particular location of n vector, 5, 5 are just random numbers I felt like checking
A = function1((math.pi)/2,(math.pi)/2,1,0)
B = function2(math.pi/2,math.pi/2,1,0)
C = function3(5,5,.001,1,0)
print(A)
print(B)
print(C)
'''

'''definitions for plus polarization'''
X, Y, Z, rho = [], [], [], []
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
        rho.append((function3(phi[listnump], theta[listnumt], mult, ex, pl)))
        listnumt = listnumt + 1
    listnump = listnump + 1





fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(X,Y,Z)
 

plt.show()

X_2, Y_2, Z_2 = [],[],[]
listnumr = 0
rho_2 = rotate(rho, 2000)
listnump, listnumt = 0, 0
while phi[listnump] <6.28:
    listnumt = 0
    while theta[listnumt] < 3.14:
        X_2.append(rho_2[listnumr] * np.cos(phi[listnump]) * np.sin(theta[listnumt]))
        Y_2.append(rho_2[listnumr] * np.sin(phi[listnump]) * np.sin(theta[listnumt]))
        Z_2.append(rho_2[listnumr] * np.cos(theta[listnumt]))
        listnumr = listnumr + 1
        listnumt = listnumt + 1
    listnump = listnump + 1





fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(X_2,Y_2,Z_2)
 

plt.show()

'''
combination_X = squareroot(map(add, square(X), square(X_2)))
combination_Y = squareroot(map(add, square(Y), square(Y_2)))
combination_Z = squareroot(map(add, square(Z), square(Z_2)))
'''
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
Average ================================================================================
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
'''======================================================================================='''

'''
===========================================================================================
Check for accuracy          
'''

predmaxrho = function3(0,0,mult,ex,pl)

if max(rho) == predmaxrho : 
    print('first check sucessful (max value of rho) ')
    print(str(max(rho)) + ' = ' + str(predmaxrho))
else:
    print('first check failed (max value of rho)')    


mover = 0 
checklist = [] 
print(len(X))
for checkcounter in range(19601):
    checklist.append(math.sqrt((X[checkcounter])**2 + (Y[checkcounter])**2 + (Z[checkcounter])**2))
avrandrho = (np.sum(checklist))/(len(checklist)) * 1.1

    
if 1.8 < avrandrho * 1.5 < 2.2:
    print('second check sucessful (2x random vectors = max rho) ')
else:
    print('second check failed (1.5x random vectors = max rho) ')  
    
'''
=========================================================================================== 
RootSumSquare
'''






'''========================================================================================'''

    
'''NOTE:
    The actual graph is a scatter plot because I could not find a better way to plot the points
    I tried plotting a surface to make it look cleaner however it did not work with the 1D arrays
    (X,Y,Z). To make this clearer I would have to import something other than matplotlib and I 
    wasn't too familiar with matplotlib in the first place so I figured I'd have trouble. 
    
    However, function3 (the function that calculates the rho if you will) is accurate and has been
    checked with the wolfram program. That is if you were to plug points into both function3 and 
    the wolfram progrom they would yeild the same values. 
'''