import numpy as np
import cmath
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

X, Y, Z = [], [], []

def sphertocart(rho_, phi_, theta_):
    for counter_0 in range(60):
        X.append(rho_ * np.cos(phi_) * np.sin(theta_))
        Y.append(rho_ * np.sin(phi_) * np.sin(theta_))
        Z.append(rho_ * np.cos(theta_))
        return (X, Y, Z)

def function1(phi_, theta_, pl_, ex_):
    pl_ * (((np.cos((phi_)**2)) * (np.cos((theta_)**2))) - (np.sin((phi_)**2)))
    + (2 * ex_ * np.cos(theta_) * np.cos(phi_) * np.sin(phi_))
    
def function2(phi_, theta_, pl_, ex_):
    pl_ * (((np.sin((phi_)**2)) * (np.cos((theta_)**2))) - (np.cos((phi_)**2)))
    - (2 * ex_ * np.cos(theta_) * np.cos(phi_) * np.sin(phi_))

def function3(phi_, theta_, mult_, pl_, ex_):
    math.fabs(
    (float(((function1(phi_, theta_, pl_, ex_)) * (cmath.exp(-1j * mult_ * math.pi))
    * ((math.sin(mult_ * math.pi)) + (1j * math.sin(theta_) * math.cos(phi_) 
    * math.cos(mult_ * math.pi)) - (1j * math.sin(theta_) * math.cos(phi_) 
    * cmath.exp(-1j * mult_ * math.pi * math.sin(theta_) * math.cos(phi_))))))) / (float(((mult_ * math.pi * (1 - (math.sin(theta_) * math.cos(phi_))**2)))))
    
    - (float(((function2(phi_, theta_, pl_, ex_)) * (cmath.exp(-1j * mult_ * math.pi))
    * ((math.sin(mult_ * math.pi)) + (1j * math.sin(theta_) * math.sin(phi_) 
    * math.cos(mult_ * math.pi)) - (1j * math.sin(theta_) * math.sin(phi_) 
    * cmath.exp(-1j * mult_ * math.pi * math.sin(theta_) * math.sin(phi_))))))) / (float(((mult_ * math.pi * (1 - (math.sin(theta_) * math.sin(phi_))**2)))))
    )

mult = .001
rho = []
theta = []
phi = []
list_num = 0

''' This counter is to create a data set for + polarization'''
for counter_1 in range(60):
    ex, pl = 0, 1
    theta.append(theta[list_num] + .1)
    phi.append(phi[list_num] + .1)
    rho.append(function3(phi[list_num], theta[list_num], mult, 1, 0))
    list_num = list_num + 1
    

#def function1(phi, theta, plus, times):
    
#typeofinput = input('Would you like to insert coordinates (DMS) or a preset detector? (Type C or P) ')

##if typeofinput == 'C':
 #   lattitude_Degrees = float(raw_input('enter lattitude Degrees '))
 #   lattitude_Minutes = float(raw_input('enter lattitude Minutes '))
   # lattitude_Seconds = float(raw_input('enter lattitude Seconds '))
   # longitude_Degrees = float(raw_input('enter longitude Degrees '))
   # longitude_Minutes = float(raw_input('enter longitude Minutes '))
   # longitude_Seconds = float(raw_input('enter longitude Seconds '))
#elif typeofinput == 'P':
#    detector = input('enter the detector you would like to test. ())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
#X, Y, Z = axes3d.get_test_data(1.54)
#for i in xrange(3):
#    X.append([])
#    for j in xrange(3):
#        X[i].append(i+j)


# Plot a basic wireframe.
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')


plt.show()