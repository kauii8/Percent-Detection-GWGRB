import math
import random

for x in range(0,30):
    x = random.uniform(0, math.pi)
    y = ((4*math.pi*.7) - 1)/(-math.cos(x))
    print(str(x) + "\n" + str(y) + "\n")