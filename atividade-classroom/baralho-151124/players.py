from createDeckOfCards import Carta;
class Jogador:


    def __init__(self, nome):
        self.nome = nome
        self.cartas: list[Carta] = []


    def add_carta_no_topo(self, carta: Carta):
        self.cartas.append(carta)


    def add_carta_na_base(self, carta: Carta):
        self.cartas.insert(0, carta)


    def remover_carta(self) -> Carta:
        return self.cartas.pop(-1)


    @property
    def possui_cartas(self) -> bool:
        return bool(self.cartas)


    @property
    def total_cartas(self) -> int:
        return len(self.cartas)


    def __str__(self):
        return self.nome

