'''------HARD IMPORTS------'''
from __future__ import division
'''------HARD IMPORTS------'''
'''------STRUCTURED JET SIMULATION DATA------'''
posstheta = (0.311711013,
0.322846475,
0.341496529,
0.35869701,
0.368912082,
0.390223233,
0.40701068,
0.42154365,
0.438145142,
0.456986664,
0.478322268,
0.505945441,
0.527711271,
0.546563055,
0.574092319,
0.58839203,
0.61155437,
0.633401338,
0.665293504,
0.733988158,
0.698791461,
0.77095764,
0.827024397,
0.868679924,
0.925334616,
0.978788939,
1.042590501,
1.102836584,
1.191392623,
1.158365118,
1.242605513,
1.314387802,
1.370932913,
1.450104466,
1.544653802,
1.645395033,
1.740388129,
1.821672668,
1.981748561,
1.893352504,
2.045352018,
2.16343571,
2.24064773,
2.337040647,
2.428999368,
2.560271953,
2.708172618,
2.864569937,
3.040653322,
3.273141562,
3.462051806,
3.687662071,
3.927780415,
4.125478709,
4.487923056,
4.747022966,
5.056287154,
5.273635384,
5.461668981,
5.776795476,
6.08859465,
6.646469773,
6.417328753,
7.178869386,
6.883338902,
7.539708831,
7.863290437,
8.259076083,
8.552992973,
9.04618403,
9.335440889,
9.770807032,
10.04806921,
10.29733217,
10.62712056,
10.77666894,
11.00494667,
11.31648355,
11.63683968,
11.96547595,
12.13265844,
12.30136594,
12.55904291,
12.38659737,
12.7332597,
12.91010595,
13.04397445,
13.27185707,
13.3618308,
13.50060584,
13.64014783,
13.82913363,
14.0205068,
14.21452827,
14.51323692,
14.51036723,
14.81529273,
14.91474671,
15.01734282,
15.33342742,
15.32989031,
15.54254381,
15.64894267,
15.75555062,
16.19996958,
16.54094608,
16.77095185,
17.24628585,
17.73450758,
18.49379061,
19.01732771,
19.83218686,
20.82628822,
20.25094898,
22.02501624,
21.41867904,
22.8095753,
23.95607819,
24.63424613,
25.33077732,
26.41876873,
27.54804272,
29.13462443,
27.35893712,
28.53121961,
29.95939082,
30.59098342,
31.67858492,
32.57536779,
33.49643352,
34.20372,
35.16850899,
36.41645478,
37.44365868,
38.23429192,
38.49856821
)

possenergy = [7.97E+51,
7.97E+51,
7.97E+51,
7.97E+51,
7.97E+51,
7.97E+51,
7.97E+51,
7.88E+51,
7.97E+51,
7.88E+51,
7.88E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.97E+51,
7.97E+51,
7.97E+51,
7.88E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.80E+51,
7.63E+51,
7.71E+51,
7.80E+51,
7.63E+51,
7.63E+51,
7.63E+51,
7.63E+51,
7.55E+51,
7.47E+51,
7.47E+51,
7.31E+51,
7.39E+51,
7.31E+51,
7.31E+51,
7.31E+51,
7.15E+51,
7.00E+51,
7.00E+51,
6.92E+51,
6.85E+51,
6.85E+51,
6.78E+51,
6.70E+51,
6.56E+51,
6.35E+51,
6.15E+51,
5.76E+51,
5.64E+51,
5.52E+51,
5.40E+51,
5.17E+51,
5.06E+51,
4.85E+51,
4.64E+51,
4.40E+51,
4.17E+51,
4.21E+51,
3.74E+51,
3.95E+51,
3.50E+51,
3.28E+51,
3.21E+51,
2.95E+51,
2.76E+51,
2.56E+51,
2.48E+51,
2.32E+51,
2.23E+51,
2.13E+51,
2.04E+51,
1.91E+51,
1.72E+51,
1.54E+51,
1.32E+51,
1.19E+51,
1.02E+51,
8.23E+50,
9.47E+50,
6.92E+50,
5.89E+50,
5.12E+50,
4.40E+50,
3.70E+50,
3.25E+50,
2.76E+50,
2.30E+50,
1.89E+50,
1.56E+50,
1.31E+50,
1.15E+50,
9.68E+49,
7.80E+49,
7.00E+49,
6.02E+49,
5.17E+49,
4.35E+49,
3.82E+49,
3.28E+49,
2.76E+49,
2.37E+49,
2.04E+49,
1.87E+49,
1.68E+49,
1.48E+49,
1.32E+49,
1.19E+49,
1.02E+49,
1.07E+49,
8.98E+48,
1.00E+49,
8.41E+48,
7.88E+48,
7.08E+48,
6.21E+48,
5.95E+48,
5.01E+48,
4.49E+48,
5.46E+48,
4.90E+48,
4.03E+48,
3.54E+48,
3.18E+48,
2.85E+48,
2.51E+48,
2.25E+48,
1.89E+48,
1.63E+48,
1.37E+48,
1.23E+48,
1.13E+48
]
energyinitial = 8e51
poss_differencediv = possenergy[1] / energyinitial
for i in range(0,len(possenergy)):
    possenergy[i] /= poss_differencediv
'''------STRUCTURED JET SIMULATION DATA------'''
'''------IMPORTS-------'''
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import pylab
'''------IMPORTS-------'''
'''------FUNCTION------'''
def standarddev (x, mu, N):
    summ = 0
    for deff in range(0, N):
        adder = (x[deff] - mu) ** 2
        summ = summ + adder
    ret = math.sqrt(summ/(N-1))
    return ret

def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** alpha))
    return ret
    
def delta_function(beta, thetaobs, thetaj):
    ret = 1 - beta * math.cos(thetaobs - thetaj)
    return ret
'''------FUNCTION------'''
'''------CREATE POINTS------'''
numSame = 0
trials = 100 # input("Enter the number of points you want to test: ") + 1
iterations = 100
GRBFINALnum_off, GRBFINALnum_struc_best, GRBFINALnum_struc_sim = 0, 0, 0, 
GRBPERCENTMEAN_off, GRBPERCENTMEAN_struc_best, GRBPERCENTMEAN_struc_sim= [], [], []
GBMtheta, GBMphi = [], []
staticPercent = 0

for q in range(0,iterations):
    RHO_PLUS_LOUIS, RHO_CROSS_LOUIS, RHO_PLUS_WASH, RHO_CROSS_WASH, RHO_PLUS_VIRGO, RHO_CROSS_VIRGO = [], [], [], [], [], []
    a_AP_LOUIS, a_AP_WASH, a_AP_VIRGO, b_AP_LOUIS, b_AP_WASH, b_AP_VIRGO = [], [], [], [], [], []
    h_LOUIS, h_WASH, h_VIRGO, reach = [], [], [], []
    phi, theta, distance, rotationpercent, rotationangle, thetaobs, psi = [], [], [], [], [], [], []
    antenna_power = []
    GRBTESTnum_off, GRBTESTnum_struc_best, GRBTESTnum_struc_sim = 0, 0, 0
    
    #creating random continuous region of space
    
    for z in range(0,trials): # binary neutron star merger creation
        phi.append(random.uniform(0.0,2 * math.pi))
        theta.append(random.uniform(0.0, math.pi))
        distance.append(random.uniform(0.0,450.0))
        psi.append(random.uniform(0,math.pi * 2))
        GBMtheta.append(random.uniform(1.9823131728623847, math.pi))
        GBMphi.append(((14 * math.pi)/5) / (-math.cos(GBMtheta[z]) + 1))
        thetaobs.append(random.uniform(0,math.pi/2))#Fermi Observation angle set, a tetrehedron trig
    '''------CREATE POINTS-------'''
    '''------OFF AXIS------'''
    fluence_off, GRBTEST_off = [], []
    gamma = 100
    thetaj = 10
    beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)

    for a in range(0,trials):
        # if math.degrees(thetaobs[a]) > 38.49856821:
        #      fluence_off.append(0)
        # else:
        FOn = (energyinitial)/((4 * math.pi*((((distance[a] * 3.086e+24) ** 2)))))
        deltaobs = delta_function(beta, thetaobs[a], math.radians(thetaj))
        deltazero = delta_function(beta, 0, 0)

        if math.degrees(thetaobs[a]) < thetaj:
            eta = 1
        else:
            eta = deltazero/deltaobs
            
        fluence_off.append((eta) * FOn)
        
        if fluence_off[a] > 2.5e-8 and theta[a] < GBMtheta[a] and phi[a] < GBMphi[a]:
            GRBTEST_off.append(True)
            GRBTESTnum_off += 1
        else:
            GRBTEST_off.append(False)    
            
        if theta[a] < GBMtheta[a] and phi[a] < GBMphi[a]:
            staticPercent += 1

    '''------OFF AXIS------'''
    '''------STRUCTURED JET SIMULATION------'''
    real_theta_list, real_energy_list, fluence_struc_sim, GRBTEST_struc_sim = [], [], [], []
    thetaj = 10
    alpha = 1.9
    thetac = 9
    thetaj = 10
    for h in range(0, len(thetaobs)):
        difference_previous = 1
        realtheta = 0
        thetanumber = 0
        if math.degrees(thetaobs[h]) > 38.49856821:
            real_energy_list.append(0)
        else:
            for j in range(0,len(posstheta)):
                thetatemp = posstheta[j]
                difference = math.fabs(thetatemp - math.degrees(thetaobs[h]))
                if difference_previous > difference:
                    difference_previous = difference
                    thetanumber = j
                    realtheta = thetatemp
            real_theta_list.append(realtheta)
            real_energy_list.append(possenergy[thetanumber])
    
    for p in range(0,trials):
        fluence_struc_sim.append(real_energy_list[p]/(4 * math.pi * ((distance[p] * 3.086e24) ** 2)))
        
        if fluence_struc_sim[p] > (2.5e-8) and theta[p] < GBMtheta[p] and phi[p] < GBMphi[p]:
            GRBTEST_struc_sim.append(True)
            GRBTESTnum_struc_sim += 1
        else:
            GRBTEST_struc_sim.append(False)

    '''------STRUCTURED JETS SIMULATION------'''  
    '''------STRUCTURED JET BEST FIT------'''
    fluence_struc_best, GRBTEST_struc_best, energy_struc_best = [], [], []
    thetaj = 10
    alpha = 1.9
    thetac = 9
    thetaj = 10
    for a in range(0,trials):
        energy_struc_best.append(angletoenergy(thetaobs[a], energyinitial, math.radians(thetac), alpha))
        fluence_struc_best.append(energy_struc_best[a]/(4 * math.pi * ((distance[a] * 3.086e24) ** 2)))
        
        if fluence_struc_best[a] > (2.5e-8) and theta[a] < GBMtheta[a] and phi[a] < GBMphi[a]:
            GRBTEST_struc_best.append(True)
            GRBTESTnum_struc_best += 1
        else:
            GRBTEST_struc_best.append(False)   
    '''------STRUCTURED JET BEST FIT------'''
    '''------MEAN AND SD AND GRAPH------'''
    GRBFINALnum_off = GRBFINALnum_off + GRBTESTnum_off
    GRBPERCENTMEAN_off.append(GRBTESTnum_off/trials)
    
    GRBFINALnum_struc_sim = GRBFINALnum_struc_sim + GRBTESTnum_struc_sim
    GRBPERCENTMEAN_struc_sim.append(GRBTESTnum_struc_sim/trials)
    
    GRBFINALnum_struc_best = GRBFINALnum_struc_best + GRBTESTnum_struc_best
    GRBPERCENTMEAN_struc_best.append(GRBTESTnum_struc_best/trials)
    
GRBPERCENT_off = GRBFINALnum_off/ (iterations * trials)
GRBSD_off = standarddev(GRBPERCENTMEAN_off, GRBPERCENT_off, iterations)

GRBPERCENT_struc_sim = GRBFINALnum_struc_sim/ (iterations * trials)
GRBSD_struc_sim = standarddev(GRBPERCENTMEAN_struc_sim, GRBPERCENT_struc_sim, iterations)

GRBPERCENT_struc_best = GRBFINALnum_struc_best/ (iterations * trials)
GRBSD_struc_best = standarddev(GRBPERCENTMEAN_struc_best, GRBPERCENT_struc_best, iterations)
'''------MEAN AND SD AND GRAPH------'''
'''------DATA DISPLAY------'''
staticPercent /= trials * iterations
print(staticPercent)
print(GRBPERCENT_off)
print(GRBPERCENT_struc_sim)
print(GRBPERCENT_struc_best)

# #Stage
# print(' ')
# #Off-axis
# print('---------------------------------------------Off Axis---------------------------------------------')
# print('GRB Off Axis ' + str(GRBFINALnum_off) + '        TOTAL ' + str(iterations * trials))
# print(' ')
# print('GRB STANDARD DEVIATION Off Axis ' + str(GRBSD_off))
# print(' ')
# print('GRB Volume Off Axis '+ str(round(((((200)**3) * math.pi * (4/3) * GRBPERCENT_off)/(1000**3)),4)) + ' +/- ' + str(round(((((200)**3) * math.pi * (4/3) * GRBSD_off))/(1000**3),4)))
# print('All volumes in Gpc^3')
# print(' ')
# print('GRB percent detection Off Axis ' + str(round(100 * ((((200)**3) * math.pi * (4/3) * GRBPERCENT_off)/(1000**3))/(((((200)**3) * math.pi * (4/3))/(1000**3))),2)))
# #Structured Simulation
# print(' ')
# print('---------------------------------------------Structured Simulation---------------------------------------------')
# print('GRB PERCENT Structured Simulation ' + str(GRBPERCENT_struc_sim))
# print(' ')
# print('GRB Structured Simulation ' + str(GRBFINALnum_struc_sim) + '        TOTAL ' + str(iterations * trials))
# print(' ')
# print('GRB STANDARD DEVIATION Structured Simulation ' + str(GRBSD_struc_sim))
# print(' ')
# print('GRB Volume Structured Simulation '+ str(round((((200)**3) * math.pi * (4/3) * GRBPERCENT_struc_sim)/(1000**3),4)) + ' +/- ' + str(round(((((200)**3) * math.pi * (4/3) * GRBSD_struc_sim))/(1000**3),4)))
# print('All volumes in Gpc^3')
# print(' ')
# print('GRB percent detection Structured Simulation ' + str(round(100 * ((((200)**3) * math.pi * (4/3) * GRBPERCENT_struc_sim)/(1000**3))/(((((200)**3) * math.pi * (4/3))/(1000**3))),2)))
# #Structured Best
# print(' ')
# print('---------------------------------------------Structured Best---------------------------------------------')
# print('GRB PERCENT Structured Best ' + str(GRBPERCENT_struc_best))
# print(' ')
# print('GRB Structured Best ' + '        TOTAL ' + str(iterations * trials))
# print(' ')

# print('GRB Volume Structured Best '+ str(round((((200)**3) * math.pi * (4/3) * GRBPERCENT_struc_best)/(1000**3),4)) + ' +/- ' + str(round(((((200)**3) * math.pi * (4/3) * GRBSD_struc_best))/(1000**3),4)))
# print('All volumes in Gpc^3')
# print(' ')
# print('GRB percent detection Structured Best ' + str(round(100 * ((((200)**3) * math.pi * (4/3) * GRBPERCENT_struc_best)/(1000**3))/(((((200)**3) * math.pi * (4/3))/(1000**3))),2)))


'''------DATA DISPLAY------'''
'''------GRAPHS------'''
'''
thetaobs_struc = thetaobs
for u in range(0,len(thetaobs)):
    thetaobs[u] = math.degrees(thetaobs[u])
off_axis_graph = plt.scatter(thetaobs,fluence_off, label = 'Off Axis')
ax = plt.subplot(111)
plt.title('Theta vs Fluence at 100 Mpc')
plt.xlabel('Thetaobs (degrees)')
plt.ylabel('Fluence (erg/cm^2)')
plt.yscale('log')
plt.xlim(0, math.pi)
axes = plt.gca()
axes.set_xlim([0,38])
axes.set_ylim([1e-10,10])

structured_jet_sim_graph = plt.scatter(thetaobs, fluence_struc_sim, label = 'Structured Jet Simulation Data')

structured_jet_best_graph = plt.scatter(thetaobs, fluence_struc_best, label = 'Structured Jet Best Fit')
pylab.legend(loc='upper right')
plt.show()
'''
'''------GRAPHS------'''
