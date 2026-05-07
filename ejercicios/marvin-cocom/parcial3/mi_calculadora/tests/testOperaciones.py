import unittest 
from parcial2.calculadoraBasica import suma, resta, multi, div


class testOperaciones(unittest.TestCase):

    def test_suma_positivos (self):
        self.assertEqual(suma(300,3),303)

    def test_suma_negativos (self):
        self.assertEqual(suma(10,-6), -10)



    def test_resta_negativa (self):
        self.assertEqual(resta(10,30),-20)

