import unittest
from main import suma, resta, multiplicacion, division

class TestOperacionesBasicas(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, -3), 2)
        self.assertEqual(suma(25, 2), 27)

    def test_resta(self):
        self.assertEqual(resta(5, -3), 8)
        self.assertEqual(resta(9, 8), 1)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(5, -3), -15)
        self.assertEqual(multiplicacion(-2, 20), -40)

    def test_division(self):
        self.assertAlmostEqual(division(10, -2), -5)
        self.assertEqual(division(60, 2), 30)

