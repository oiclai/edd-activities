class CartaUnitaria:
    def __init__(self, valorNumerico, naipe):
        self.valorNumerico = valorNumerico
        self.naipe = naipe

    def __str__(self):
        return f"{self.valorNumerico} de {self.naipe}"