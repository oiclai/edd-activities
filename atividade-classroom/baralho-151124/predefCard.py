# representando uma carta individual
class UnitaryCard:
    def __init__(self, numericValue, suit):
        self.numericValue = numericValue # A-13
        self.suit = suit # ouro, espada, copa, paus

    def __str__(self):
        return f"{self.numericValue} de {self.suit}"