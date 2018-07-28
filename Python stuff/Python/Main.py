from AntennaPowerPatterns import *
from conversions import *
from OffAxisLists import *
import csv
import random


def main(inputEnergy, sensitivityGW, modelGRB, trials, iterations, minDistance, maxDistance, thetaj, alpha, thetac, gamma, thetaObsLimit):
    # Gets simulation data for Energy and puts it in tuple form
    possibleEnergyMargutti = []
    with open("/media/n/OS/Users/Nihar/Documents/Everything/Research/LIGO/Percent-Detection-GWGRB/Python stuff/Python/Margutti Data Energy.csv", 'r') as marguttiEnergyDataCSV:
        csv_reader = csv.reader(marguttiEnergyDataCSV)

        filteredEnergy = (line.replace('\n', '')
                          for line in marguttiEnergyDataCSV)

        for line in filteredEnergy:
            possibleEnergyMargutti.append(float(line))

    # Gets simulation data for Theta and puts it in tuple form
    possibleThetaMargutti = []
    with open("/media/n/OS/Users/Nihar/Documents/Everything/Research/LIGO/Percent-Detection-GWGRB/Python stuff/Python/Margutti Data Theta.csv", 'r') as marguttiThetaDataCSV:
        csv_reader = csv.reader(marguttiThetaDataCSV)

        filteredTheta = (line.replace('\n', '')
                         for line in marguttiThetaDataCSV)

        for line in filteredTheta:
            possibleThetaMargutti.append(float(line))

    possibleThetaMarguttiTuple = tuple(possibleThetaMargutti)

    # 3 different detector properties
    # chi is orientation from East in degrees, eta is opening angle usual 90
    # input different detector locations and orientations, beta and lambda are lattitude and longitude
    etaAP = math.pi/2

    # Livingston Louisiana LIGO
    betaLOUIS = math.radians(DMS_TO_DEGREES(30, 33, 46.4))
    lambdLOUIS = math.radians(DMS_TO_DEGREES(90, 46, 27.3))
    chiLOUIS = COMPASS_TO_ANGLE(math.radians(208))

    # Hanford Washington LIGO
    betaWASH = math.radians(DMS_TO_DEGREES(46, 27, 18.5))
    lambdWASH = math.radians(DMS_TO_DEGREES(119, 24, 27.6))
    chiWASH = COMPASS_TO_ANGLE(math.radians(279))

    # Italy VIRGO
    betaITALY = math.radians(DMS_TO_DEGREES(43, 37, 53))
    lambdITALY = math.radians(DMS_TO_DEGREES(10, 30, 16))
    chiITALY = COMPASS_TO_ANGLE(math.radians(333.5))

    # Converts gamma factor to beta, uneeded for most recent model
    beta = math.sqrt((-1 * ((1/gamma) ** 2)) + 1)

    for initialEnergy in inputEnergy:  # list of our energies

        # rescales margutti energy to inputted energy
        rescaleFactor = possibleEnergyMargutti[0] / initialEnergy
        # List comprehension converted to tuple
        possibleEnergyMarguttiTuple = tuple(
            [i/rescaleFactor for i in possibleEnergyMargutti])

        # Accounts for various sensitivites by changing the horizon distance
        for stage in sensitivityGW:
            if stage == 'design':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 190, 190, 145
            elif stage == 'mid low':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 80, 80, 65
            elif stage == 'mid mid':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 100, 100, 75
            elif stage == 'mid high':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 120, 120, 85
            elif stage == 'late low':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 120, 120, 65
            elif stage == 'late mid':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 145, 145, 90
            elif stage == 'late high':
                horizonDistanceLOUIS, horizonDistanceWASH, horizonDistanceITALY = 170, 170, 115
            elif stage == '3rd generation':
                horizonDistanceWASH = 190 * 10
                horizonDistanceLOUIS, horizonDistanceITALY = 1, 1

            # Final variable initializations
            finalGRBNumOff = 0
            finalGWGRBNumOff = 0
            finalGRBNumStrucBest = 0
            finalGWGRBNumStrucBest = 0
            finalGRBNumStrucSim = 0
            finalGWGRBNumStrucSim = 0

            percentMeanGW, finalGWNum = [], 0

            finalGRBPercentMeanOff = []
            finalGWGRBPercentMeanOff = []
            finalGRBPercentMeanStrucBest = []
            finalGWGRBPercentMeanStrucBest = []
            finalGRBPercentMeanStrucSim = []
            finalGWGRBPercentMeanStrucSim = []

            gbmTheta, gbmPhi, swiftTheta, swiftPhi = [], [], [], []

            # Iterations
            for i in range(0, iterations):

                #List initializations
                fPlusLOUIS, fCrossLOUIS, fPlusWASH, fCrossWASH, fPlusITALY, fCrossITALY = [], [], [], [], [], []

                a_AP_LOUIS, a_AP_WASH, a_AP_ITALY, b_AP_LOUIS, b_AP_WASH, b_AP_ITALY = [], [], [], [], [], []

                distanceFactorLOUIS, distanceFactorWASH, distanceFactorITALY = [], [], []
                phi, theta, psi, distance, thetaObs, psi = [], [], [], [], [], []

                testGRBNumOff, testGRBNumStrucBest, testGRBNumStrucSim = 0, 0, 0
                testGWBoolnum = 0

                SNRcalculatedLOUISsig, SNRcalculatedWASHsig, SNRcalculatedITALYsig, SNRcalculated, testGWBool = [], [], [], [], []

                fluenceOff, testGRBBoolOff = [], []

                realThetaList, realEnergyList, fluenceStrucSim, testGRBBoolStrucSim = [], [], [], []

                realThetaOffList, realEnergyOffList = [], []

                fluenceStrucBest, testGRBBoolStrucBest, energyStrucBest = [], [], []

                testGWBoolGRBNumOff, testGWBoolGRBNumStrucSim, testGWBoolGRBNumStrucBest, = 0, 0, 0
                # Trials
                for j in range(0, trials):  # binary neutron star merger creation
                    # Distance properties
                    distance.append(random.uniform(minDistance, maxDistance))
                    # *2.25 to account for average over polarization
                    distanceFactorLOUIS.append(
                        ((((horizonDistanceLOUIS * 12)**2))/(((distance[j]) ** 2))))
                    distanceFactorWASH.append(
                        ((((horizonDistanceWASH * 12)**2))/((distance[j]) ** 2)))
                    distanceFactorITALY.append(
                        ((((horizonDistanceITALY * 12)**2))/((distance[j]) ** 2)))

                    # Angular Properties
                    psi.append(random.uniform(0, math.pi * 2))
                    phi.append(random.uniform(0, 2 * math.pi))
                    theta.append(random.uniform(0, math.pi))
                    # GRB Observation angle and inclination angle
                    thetaObs.append(random.uniform(0, math.pi/2))

                    # creating random continuous region of space for GRB detections
                    gbmTheta.append(random.uniform(
                        1.9823131728623847, math.pi))
                    gbmPhi.append(((14 * math.pi)/5) /
                                  (-math.cos(gbmTheta[j]) + 1))

                    swiftTheta.append(random.uniform(
                        0.7953988301841436, math.pi))
                    swiftPhi.append(((3 * math.pi)/5) /
                                    (-math.cos(swiftTheta[j]) + 1))

                    # Antenna Power Pattern
                    a_AP_LOUIS.append(
                        afunction(chiLOUIS, betaLOUIS, theta[j], phi[j], lambdLOUIS))
                    a_AP_WASH.append(
                        afunction(chiWASH, betaWASH, theta[j], phi[j], lambdWASH))
                    a_AP_ITALY.append(
                        afunction(chiITALY, betaITALY, theta[j], phi[j], lambdITALY))

                    b_AP_LOUIS.append(
                        bfunction(chiLOUIS, betaLOUIS, theta[j], phi[j], lambdLOUIS))
                    b_AP_WASH.append(
                        bfunction(chiWASH, betaWASH, theta[j], phi[j], lambdWASH))
                    b_AP_ITALY.append(
                        bfunction(chiITALY, betaITALY, theta[j], phi[j], lambdITALY))

                    fPlusLOUIS.append(
                        AP_PLUS(etaAP, a_AP_LOUIS[j], b_AP_LOUIS[j], psi[j]))
                    fPlusWASH.append(
                        AP_PLUS(etaAP, a_AP_WASH[j], b_AP_WASH[j], psi[j]))
                    fPlusITALY.append(
                        AP_PLUS(etaAP, a_AP_ITALY[j], b_AP_ITALY[j], psi[j]))

                    fCrossLOUIS.append(
                        AP_CROSS(etaAP, a_AP_LOUIS[j], b_AP_LOUIS[j], psi[j]))
                    fCrossWASH.append(
                        AP_CROSS(etaAP, a_AP_WASH[j], b_AP_WASH[j], psi[j]))
                    fCrossITALY.append(
                        AP_CROSS(etaAP, a_AP_ITALY[j], b_AP_ITALY[j], psi[j]))

                    # SNR calculation
                    if stage != '3rd generation':
                        inclinationMultiplier = (
                            1/8) * (1 + (6 * (math.cos(thetaObs[j]) ** 2)) + (math.cos(thetaObs[j]) ** 4))  # Schutz eq 26

                        SNRcalculatedLOUISsig.append(math.sqrt(
                            inclinationMultiplier * ((fPlusLOUIS[j]**2) + (fCrossLOUIS[j] ** 2)) * distanceFactorLOUIS[j]))
                        SNRcalculatedWASHsig.append(math.sqrt(
                            inclinationMultiplier * ((fPlusWASH[j] ** 2) + (fCrossWASH[j] ** 2)) * distanceFactorWASH[j]))
                        SNRcalculatedITALYsig.append(math.sqrt(inclinationMultiplier * (
                            (fPlusITALY[j] ** 2) + (fCrossITALY[j] ** 2)) * distanceFactorITALY[j]))

                        SNRcalculated.append(math.sqrt((SNRcalculatedLOUISsig[j] ** 2) + (
                            SNRcalculatedWASHsig[j] ** 2) + (SNRcalculatedITALYsig[j]**2)))

                    else:
                        SNRcalculated.append(math.sqrt(
                            ((fPlusWASH[j] ** 2) + (fCrossWASH[j] ** 2)) * distanceFactorWASH[j]))  # Only 1 3rd generation

                    # network sensitivity in a network of 3 detectors is 12 SNR
                    if SNRcalculated[j] >= 12:
                        testGWBool.append(True)
                        testGWBoolnum += 1
                    else:
                        testGWBool.append(False)

                    # Off axis
                    
                    # Old model 
                    # if math.degrees(thetaObs[j]) > thetaObsLimit:
                    #     fluenceOff.append(0)
                    # else:
                    #     FOn = (initialEnergy)/((4 * math.pi *
                    #                             ((((distance[j] * 3.086e+24) ** 2)))))
                    #     deltaobs = delta_function(
                    #         beta, thetaObs[j], math.radians(thetaj))
                    #     deltazero = delta_function(beta, 0, 0)

                    #     if math.degrees(thetaObs[j]) < thetaj:
                    #         eta = 1
                    #     else:
                    #         eta = deltazero/deltaobs

                    previousDifference = 1
                    realtheta = 0
                    thetanumber = 0

                    if math.degrees(thetaObs[j]) > thetaObsLimit:
                        realEnergyOffList.append(thetaObsLimit)
                        realEnergyOffList.append(0)
                    else:
                        # Sorter
                        for k in range(0, len(thetaOffList)):

                            thetaTemp = thetaOffList[k]
                            difference = math.fabs(
                                thetaTemp - math.degrees(thetaObs[j]))
                            if previousDifference > difference:
                                previousDifference = difference
                                thetanumber = k
                                realtheta = thetaTemp
                        realThetaOffList.append(realtheta)
                        realEnergyOffList.append(
                            energyOffList[thetanumber])

                        
                    fluenceOff.append(realEnergyOffList[j] / (4 * math.pi * (distance[j] ** 2)))

                    if fluenceOff[j] > 2.5e-8 and theta[j] < gbmTheta[j] and phi[j] < gbmPhi[j]:
                        testGRBBoolOff.append(True)
                        testGRBNumOff += 1

                    elif fluenceOff[j] > 2.5e-8 and theta[j] < swiftTheta[j] and phi[j] < swiftPhi[j]:
                        testGRBBoolOff.append(True)
                        testGRBNumOff += 1
                    else:
                        testGRBBoolOff.append(False)

                    # Structured Jet simiulation
                    previousDifference = 1
                    realtheta = 0
                    thetanumber = 0

                    if math.degrees(thetaObs[j]) > thetaObsLimit:
                        realThetaList.append(thetaObsLimit)
                        realEnergyList.append(0)
                    else:
                        # Sorter
                        for k in range(0, len(possibleThetaMarguttiTuple)):

                            thetaTemp = possibleThetaMarguttiTuple[k]
                            difference = math.fabs(
                                thetaTemp - math.degrees(thetaObs[j]))
                            if previousDifference > difference:
                                previousDifference = difference
                                thetanumber = k
                                realtheta = thetaTemp
                        realThetaList.append(realtheta)
                        realEnergyList.append(
                            possibleEnergyMarguttiTuple[thetanumber])

                    fluenceStrucSim.append(
                        realEnergyList[j]/(4 * math.pi * ((distance[j] * 3.086e24) ** 2)))

                    if fluenceStrucSim[j] > 2.5e-8 and theta[j] < gbmTheta[j] and phi[j] < gbmPhi[j]:
                        testGRBBoolStrucSim.append(True)
                        testGRBNumStrucSim += 1
                    elif fluenceStrucSim[j] > 2.5e-8 and theta[j] < swiftTheta[j] and phi[j] < swiftPhi[j]:
                        testGRBBoolStrucSim.append(True)
                        testGRBNumStrucSim += 1
                    else:
                        testGRBBoolStrucSim.append(False)

                    # Structured Jet best fit
                    energyStrucBest.append(angletoenergy(
                        thetaObs[j], initialEnergy, math.radians(thetac), alpha))
                    fluenceStrucBest.append(
                        energyStrucBest[j]/(4 * math.pi * ((distance[j] * 3.086e24) ** 2)))

                    if fluenceStrucBest[j] > 2.5e-8 and theta[j] < gbmTheta[j] and phi[j] < gbmPhi[j]:
                        testGRBBoolStrucBest.append(True)
                        testGRBNumStrucBest += 1
                    elif fluenceStrucBest[j] > 2.5e-8 and theta[j] < swiftTheta[j] and phi[j] < swiftPhi[j]:
                        testGRBBoolStrucBest.append(True)
                        testGRBNumStrucBest += 1
                    else:
                        testGRBBoolStrucBest.append(False)

                    # Cross Check
                    if testGWBool[j] == True and testGRBBoolOff[j] == True:
                        testGWBoolGRBNumOff += 1
                    if testGWBool[j] == True and testGRBBoolStrucSim[j] == True:
                        testGWBoolGRBNumStrucSim += 1
                    if testGWBool[j] == True and testGRBBoolStrucBest[j] == True:
                        testGWBoolGRBNumStrucBest += 1

                # Final Values (post trial)
                finalGWNum = finalGWNum + testGWBoolnum
                percentMeanGW.append(testGWBoolnum/trials)

                finalGRBNumOff += testGRBNumOff
                finalGWGRBNumOff = finalGWGRBNumOff + testGWBoolGRBNumOff
                finalGRBPercentMeanOff.append(testGRBNumOff/trials)
                finalGWGRBPercentMeanOff.append(testGWBoolGRBNumOff/trials)

                finalGRBNumStrucSim += testGRBNumStrucSim
                finalGWGRBNumStrucSim = finalGWGRBNumStrucSim+testGWBoolGRBNumStrucSim
                finalGRBPercentMeanStrucSim.append(testGRBNumStrucSim/trials)
                finalGWGRBPercentMeanStrucSim.append(
                    testGWBoolGRBNumStrucSim/trials)

                finalGRBNumStrucBest += testGRBNumStrucBest
                finalGWGRBNumStrucBest = finalGWGRBNumStrucBest + testGWBoolGRBNumStrucBest
                finalGRBPercentMeanStrucBest.append(testGRBNumStrucBest/trials)
                finalGWGRBPercentMeanStrucBest.append(
                    testGWBoolGRBNumStrucBest/trials)

            GWPERCENT = finalGWNum / (iterations * trials)
            GWSD = uncertaintyAverage(percentMeanGW, GWPERCENT, trials, iterations)

            GRBPERCENT_off = finalGRBNumOff / (iterations * trials)
            GWGRBPERCENT_off = finalGWGRBNumOff / (iterations * trials)
            GRBSD_off = uncertaintyAverage(
                finalGRBPercentMeanOff, GRBPERCENT_off, trials, iterations)
            GWGRBSD_off = uncertaintyAverage(
                finalGWGRBPercentMeanOff, GWGRBPERCENT_off, trials, iterations)

            GRBPERCENT_struc_sim = finalGRBNumStrucSim / (iterations * trials)
            GWGRBPERCENT_struc_sim = finalGWGRBNumStrucSim / \
                (iterations * trials)
            GRBSD_struc_sim = uncertaintyAverage(
                finalGRBPercentMeanStrucSim, GRBPERCENT_struc_sim, trials, iterations)
            GWGRBSD_struc_sim = uncertaintyAverage(
                finalGWGRBPercentMeanStrucSim, GWGRBPERCENT_struc_sim, trials, iterations)

            GRBPERCENT_struc_best = finalGRBNumStrucBest / \
                (iterations * trials)
            GWGRBPERCENT_struc_best = finalGWGRBNumStrucBest / \
                (iterations * trials)
            GRBSD_struc_best = uncertaintyAverage(
                finalGRBPercentMeanStrucBest, GRBPERCENT_struc_best, trials, iterations)
            GWGRBSD_struc_best = uncertaintyAverage(
                finalGWGRBPercentMeanStrucBest, GWGRBPERCENT_struc_best, trials, iterations)

            volumeGW = volumeSphere(GWPERCENT, maxDistance, 4)

            print('GWGRBPERCENT {} {}'.format(stage, GWGRBPERCENT_off))
            print('GW Volume {} {}'.format(stage, volumeGW))

# volume

#     #Stage
#     print(' ')
#     print('---------------------------------------------' + stage + '---------------------------------------------')
#     print('---------------------------------------------' + str(initalEnergy) + '---------------------------------------------')
#     print(' ')
#     #Off-axis
#     print('---------------------------------------------Off Axis---------------------------------------------')
#     print('GW PERCENT ' + str(GWPERCENT) + '        GRB PERCENT Off Axis ' + str(GRBPERCENT_off) + '        GWGRB PERCENT Off Axis ' + str(GWGRBPERCENT_off))
#     print(' ')
#     print('GW ' + str(finalGWNum) + '        GRB Off Axis ' + str(finalGRBNumOff) + '        GWGRB Off Axis ' + str(finalGWGRBNumOff) + '        TOTAL ' + str(iterations * trials))
#     print(' ')
#     print('GW STANDARD DEVIATION ' + str(GWSD) + '        GRB STANDARD DEVIATION Off Axis ' + str(GRBSD_off) + '        GWGRB STANDARD DEVIATION Off Axis ' + str(GWGRBSD_off))
#     print(' ')
#     print('GW Volume '+ str((round(((((maxDistance)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3)),4))) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GWSD)/(1000**3)),4)))
#     print('GRB Volume Off Axis '+ str(round(((((maxDistance)**3) * math.pi * (4/3) * GRBPERCENT_off)/(1000**3)),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GRBSD_off))/(1000**3),4)))
#     print('GWGRB Volume Off Axis '+ str(round((((maxDistance)**3) * math.pi * (4/3) * GWGRBPERCENT_off)/(1000**3),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GWGRBSD_off))/(1000**3),4)))
#     print('All volumes in Gpc^3')
#     print(' ')
#     print('GWGRB/GW, percent detection Off Axis ' + str(round(100 * ((((maxDistance)**3) * math.pi * (4/3) * GWGRBPERCENT_off)/(1000**3))/(((((maxDistance)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3))),2)))
#     #Structured Simulation
#     print(' ')
#     print('---------------------------------------------Structured Simulation---------------------------------------------')
#     print('GW PERCENT ' + str(GWPERCENT) + '        GRB PERCENT Structured Simulation ' + str(GRBPERCENT_struc_sim) + '        GWGRB PERCENT Structured Simulation ' + str(GWGRBPERCENT_struc_sim))
#     print(' ')
#     print('GW ' + str(finalGWNum) + '        GRB Structured Simulation ' + str(GRBfinalnum_struc_sim) + '        GWGRB Structured Simulation ' + str(GWGRBfinalnum_struc_sim) + '        TOTAL ' + str(iterations * trials))
#     print(' ')
#     print('GW STANDARD DEVIATION ' + str(GWSD) + '        GRB STANDARD DEVIATION Structured Simulation ' + str(GRBSD_struc_sim) + '        GWGRB STANDARD DEVIATION Structured Simulation ' + str(GWGRBSD_struc_sim))
#     print(' ')
#     print('GW Volume '+ str(round(((((maxDistance)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3)),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GWSD)/(1000**3)),4)))
#     print('GRB Volume Structured Simulation '+ str(round((((maxDistance)**3) * math.pi * (4/3) * GRBPERCENT_struc_sim)/(1000**3),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GRBSD_struc_sim))/(1000**3),4)))
#     print('GWGRB Volume Structured Simulation '+ str(round((((maxDistance)**3) * math.pi * (4/3) * GWGRBPERCENT_struc_sim)/(1000**3),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GWGRBSD_struc_sim))/(1000**3),4)))
#     print('All volumes in Gpc^3')
#     print(' ')
#     print('GWGRB/GW, percent detection Structured Simulation ' + str(round(100 * ((((maxDistance)**3) * math.pi * (4/3) * GWGRBPERCENT_struc_sim)/(1000**3))/(((((maxDistance)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3))),2)))
#     #Structured Best
#     print(' ')
#     print('---------------------------------------------Structured Best---------------------------------------------')
#     print('GW PERCENT ' + str(GWPERCENT) + '        GRB PERCENT Structured Best ' + str(GRBPERCENT_struc_best) + '        GWGRB PERCENT Structured Best ' + str(GWGRBPERCENT_struc_best))
#     print(' ')
#     print('GW ' + str(finalGWNum) + '        GRB Structured Best ' + str(finalGRBNumStrucBest) + '        GWGRB Structured Best ' + str(finalGWGRBNumStrucBest) + '        TOTAL ' + str(iterations * trials))
#     print(' ')
#     print('GW STANDARD DEVIATION Structured Best ' + str(GWSD) + '        GRB STANDARD DEVIATION Structured Best ' + str(GRBSD_struc_best) + '        GWGRB STANDARD DEVIATION Structured Best ' + str(GWGRBSD_struc_best))
#     print(' ')
#     print('GW Volume '+ str(round(((((maxDistance)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3)),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GWSD)/(1000**3)),4)))
#     print('GRB Volume Structured Best '+ str(round((((maxDistance)**3) * math.pi * (4/3) * GRBPERCENT_struc_best)/(1000**3),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GRBSD_struc_best))/(1000**3),4)))
#     print('GWGRB Volume Structured Best '+ str(round((((maxDistance)**3) * math.pi * (4/3) * GWGRBPERCENT_struc_best)/(1000**3),4)) + ' +/- ' + str(round(((((maxDistance)**3) * math.pi * (4/3) * GWGRBSD_struc_best))/(1000**3),4)))
#     print('All volumes in Gpc^3')
#     print(' ')
#     print('GWGRB/GW, percent detection Structured Best ' + str(round(100 * ((((maxDistance)**3) * math.pi * (4/3) * GWGRBPERCENT_struc_best)/(1000**3))/(((((maxDistance)**3) * math.pi * (4/3) * GWPERCENT)/(1000**3))),2)))

#     # print("\n" + str(numSame) + "\n" + str(numDiff))
