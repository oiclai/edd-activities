class ContaCorrente:
    def __init__(self, numero, saldo, titular):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.sucessoSaque = False 
        if self.saldo >= valor:
            self.saldo -= valor
            self.sucessoSaque = True

    