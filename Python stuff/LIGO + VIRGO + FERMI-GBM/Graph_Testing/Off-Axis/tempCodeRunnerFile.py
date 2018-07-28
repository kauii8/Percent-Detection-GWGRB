differenceDiv = 8e51/energy[0]
for i in range(0, len(energy)):
    energy[i] *= differenceDiv
    energy[i] = math.fabs(energy[i])

    if energy[i] > 1.4e52 or energy[i] < 8e51:
        energy[i] /= 1000