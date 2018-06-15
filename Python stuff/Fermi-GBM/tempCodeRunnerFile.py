        FOn = (energyinitial)/((4 * math.pi*((((distance[a] * 3.086e+24) ** 2)))))
        deltaobs = delta_function(beta, thetaobs[a], math.radians(thetaj))
        deltazero = delta_function(beta, 0, 0)

        if math.degrees(thetaobs[a]) < thetaj:
            eta = 1
        else:
            eta = deltazero/deltaobs
            
        fluence_off.append((eta) * FOn)