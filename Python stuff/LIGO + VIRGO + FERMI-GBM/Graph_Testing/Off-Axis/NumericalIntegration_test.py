import unittest 
from NumericalIntegration import *

class TestNumericalIntegration(unittest.TestCase):
    def test_bandSpectrum(self):
        self.assertAlmostEqual(bandSpectrum(10e4), 0.9904875368855045)
        self.assertAlmostEqual(bandSpectrum(25e6), 0.2676661372206671)
        self.assertAlmostEqual(bandSpectrum(10e3), 0.9990412272515992)

    def test_calcThetaT(self):
        self.assertAlmostEqual(calcThetaT(2.5), 0.05383887704165026, places = 5)
        self.assertAlmostEqual(calcThetaT(60), 0.5985200127752338, places = 5)
        self.assertAlmostEquals(calcThetaT(421), 1.8297615319064182, places = 5)

    def test_deltaFunction(self):
        self.assertAlmostEqual(deltaFunction(0.05383887704165026), 0.01056899433458287)