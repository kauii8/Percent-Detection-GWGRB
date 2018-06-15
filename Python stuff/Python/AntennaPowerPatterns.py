import math 

#Plus orientation for Antenna Power Pattern
def AP_PLUS(eta,a,b,psi): 
    ret = math.sin(eta) * ((a * math.cos(2 * psi)) + (b * math.sin(2 * psi)))
    return ret
    
#Cross orientation for Antenna Power Pattern
def AP_CROSS(eta,a,b,psi): 
    ret = math.sin(eta) * ((b * math.cos(2 * psi)) - (a * math.sin(2 * psi)))
    return ret

#Detector Dependancies
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

#Detector Conversions
def COMPASS_TO_ANGLE(compassDirection):
    ret = ((5 * math.pi) / 2) - compassDirection
    return ret
    
def DMS_TO_DEGREES(degs, mins, secs):
    ret = degs + (mins/60) + (secs/3600)
    return ret