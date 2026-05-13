class Cuenta:
    # Atributos: cliente, cuenta, saldo  
    
    """
    Inicializa una nueva cuenta bancaria con el nombre del cliente, número de cuenta y saldo inicial (opcional, por defecto es 0).
    Agrs:
        cliente (str):El nombre del cliente.
        cuenta (str): El número de cuenta.
        saldo (float):El saldo inicial de la cuenta (opcional, por defecto es 0).
    """
    
    def __init__(self, cliente, cuenta, saldo = 0):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
        """
    Realiza un deposito en la cuenta
    Args: 
        Cantidad (float): La cantidad a depositar. Debe ser un valor positivo.
    Returns:
        True si el deposito fue exitoso, False si la cantidad es negativa o cero.
    
    """
    #metodo para realizar un deposito  en la cuenta
    

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad 
            return True
        return False

    #metodo para realizar un retiro de la cuenta

    """
    
    Realiza un retiro de la cuenta
    Args:
    cantidad (float):La cantidad a retirar. Debe ser un valor positivo y no debe exceder el saldo disponible en la cuenta.
    Returns:
        True si el retiro fue exitoso, False si la cantidad es negativa, cero o mayor al saldo disponible.
    """
    def retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    

    def main():
        pass

    if __name__ == '__main__':
        main()
