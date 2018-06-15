from Main import *

main(
    (8e51, 1e51, 1e50),  # Energies
    ('3rd generation', 'desgin', 'late low', 'late mid', 'late high', 'mid low', 'mid mid', 'mid high'),  # Sensitivities
    ('Off-Axis', 'Structured Simulation', 'Structured Best Fit'),  # Models
    100,  # Trials
    100,  # Iterations
    0,  # Minimum Distance
    450,  # Maximum Distance
    10,  # Jet Opening Half Angle
    1.9,  # Alpha Best Fit
    9,  # Critical Angle Best Fit
    100,  # Gamma Factor
    38.49856821  # Limit past (input 90 for no limit)
)



# What you can input for sensitivities:
# 3rd generation
# design
# late low
# late mid
# late high
# mid low
# mid mid
# mid high

# What you can input for Models
# Off-Axis
# Structured Simulation
# Structured Best Fit

# Recommend 38.49856821 for limitor, that is what it is in the margutti paper
# If you want to change number of detectors used or an a detector must do it through Main.py
