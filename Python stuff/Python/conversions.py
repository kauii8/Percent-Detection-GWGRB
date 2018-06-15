import math

def COMPASS_TO_ANGLE(compassdirection):
    ret = ((5 * math.pi) / 2) - compassdirection
    return ret
    
def DMS_TO_DEGREES(degs, mins, secs):
    ret = degs + (mins/60) + (secs/3600)
    return ret

def uncertaintyAverage (x, mu, trials, iterations):
    summ = 0
    for deff in range(0, iterations):
        adder = (x[deff] - mu) ** 2
        summ = summ + adder
    ret = math.sqrt(summ/((trials * iterations) - 1))
    return ret

def angletoenergy(theta, energyorig, thetac, alpha):
    ret =   energyorig * math.e ** (-1 * ((theta/thetac) ** alpha))
    return ret
    
def delta_function(beta, thetaobs, thetaj):
    ret = 1 - beta * math.cos(thetaobs - thetaj)
    return ret

def volumeSphere(percent, maxDistance, roundDigit):
    return round(((4/3) * math.pi * (maxDistance ** 3) * percent)/ (1000 ** 3) , roundDigit)