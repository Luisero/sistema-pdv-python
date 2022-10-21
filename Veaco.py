class Veaco():
    def __init__(self, cliente, divida):
        self.cliente = cliente
        self.divida = divida

    def pagar_divida(self, pagamento):
        self.divida -= pagamento