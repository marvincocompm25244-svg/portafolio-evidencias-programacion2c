class Cuenta:
    # Atributos: cliente, cuenta, saldo  

    def __init__(self, cliente, cuenta, saldo = 0):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
    """
    inicializa una nueva cuenta bancaria con el nombre del cliente, número de cuenta y saldo inicial (opcional, por defecto es 0).
    agrs:   cliente (str): El nombre del cliente.
            cuenta (str): El número de cuenta.
            saldo (float): El saldo inicial de la cuenta (opcional, por defecto es 0).
    """
    #metodo para realizar un deposito  en la cuenta

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad 
            return True
        return False
    """
     realiza un deposito en la cuenta
    args: cantidad (float): La cantidad a depositar. Debe ser un valor positivo.
    returns: True si el deposito fue exitoso, False si la cantidad es negativa o cero.
    """

    #metodo para realizar un retiro de la cuenta


    def retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    """
    realiza un retiro de la cuenta
    args: cantidad (float): La cantidad a retirar. Debe ser un valor positivo y no debe exceder el saldo disponible en la cuenta.
    returns: True si el retiro fue exitoso, False si la cantidad es negativa, cero o mayor al saldo disponible.
    """
    

    def main():
        pass

    if __name__ == '__main__':
        main()