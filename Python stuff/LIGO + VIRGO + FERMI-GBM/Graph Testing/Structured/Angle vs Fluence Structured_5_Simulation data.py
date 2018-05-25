'''------IMPORTS-------'''
import numpy as np
import math
import matplotlib.pyplot as plt
from fractions import Fraction
    
def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** 1.9))
    return ret
energy,tp,fluence = [], [],[]
energyorig = 7e51
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

possenergy = (7.97E+51,
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
)
real_theta_list, real_energy_list = [], []
trials = 100
alpha = 1.9
thetac = 9
thetaj = 10
theta = np.logspace(-1, 1.7, trials)
theta = theta.tolist()

print(len(posstheta))
for h in range(0, len(theta)):
    difference_previous = 1
    realtheta = 0
    thetanumber = 0
    for j in range(0,len(posstheta)):
        thetatemp = posstheta[j]
        difference = math.fabs(thetatemp - theta[h])
        if difference_previous > difference:
            difference_previous = difference
            thetanumber = j
            realtheta = thetatemp
    real_theta_list.append(realtheta)
    real_energy_list.append(possenergy[thetanumber])

distance = 40 * 3.086e24

for a in range(0,trials):
    fluence.append(real_energy_list[a]/(4 * math.pi * (distance ** 2)))


plt.subplot(223)

plt.xlim(.6, 100)
plt.ylabel('Energy (ergs) ')
plt.xlabel('Theta (deg) ')
plt.xscale('log')
plt.title('Structured Jet best fit angle vs energy simulation data ')
plt.loglog(real_theta_list, fluence)
plt.grid(True)
plt.show()