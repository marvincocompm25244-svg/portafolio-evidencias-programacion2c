import unittest
from cuenta import Cuenta 

class TestCuenta(unittest.TestCase):

    def setUp(self):
        self.cuenta = Cuenta("Fulanito Perez Megano", "001")

        #------PRUEBAS DEL CONSTRUCTOR-------

    def test_validad_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0, "el saldo inicial deberia ser 0 por defecto")

        def test_validar_cliente(self):
            self.assertEqual(self.cuenta.cliente, "Fulanito Perez Megano", "el  nombre del cliente no es correcto")


        #-------PRUEBAS DEPOSITOS-------

    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500.00)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500.00, "el saldo actual deberia ser de 500.00")

    def test_depositar_cantidad_negativa(self):
        result = self.cuenta.deposito(-200.00)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "el saldo actual deberia ser 0")

        #test para validar deposito en 0 

        #------------PRUEBAS DE RETIROS-------

        #1.- test para validar retiro con cantidad 0
        #2.- test para validar retiro con cantidad negativa
        #3.- test para validar retiro con cantidad mayor al saldo

    def test_retirar_cantidad_0(self):
        result = self.cuenta.retiro(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "el saldo actual deberia ser 0")

    def test_retirar_cantidad_negativa(self):
        result = self.cuenta.retiro(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "el saldo actual deberia ser 0")

    def test_retirar_cantidad_mayor_al_saldo(self):
        self.cuenta.deposito(500)
        result = self.cuenta.retiro(1000)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 500, "el saldo actual deberia seguir siendo 500 ")
    
if __name__ == '__main__':
    unittest.main()
    