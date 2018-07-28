    for a in range(0, len(thetaObs)):
    realOffThetaList.append(min(thetaOffList, key=lambda x:abs(x-thetaObs[a])))
    index = min(range(len(thetaOffList)), key=lambda z: abs(thetaOffList[z]-thetaObs[a]))
    realOffEnergyList.append(energyOffList[index])

    for a in range(0,trials):
        fluence_off.append(realOffEnergyList[a]/ (4 * math.pi * ((distance[a] * 3.086e24)**2))) # Calls the energy function from class then divides by 4 pi r squared to get fluence