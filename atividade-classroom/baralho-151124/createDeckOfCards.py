from random import shuffle
from players import Jogador; from predefCard import *
class Baralho:


    def __init__(self):
        self.cartas: list[Carta] = []
        for naipe in Naipe:
            for valor in range(Carta.AS, Carta.REI + 1):
                self.cartas.append(
                    Carta(valor=valor, naipe=naipe)
                )


    def embaralhar(self):
        shuffle(self.cartas)


    def distribuir(self, jogadores: list['Jogador']):
        if not 1 <= len(jogadores) <= 4:
            raise NumJogadoresInvalido()


        cartas_por_jogador = len(self.cartas) // len(jogadores)
        for jogador in jogadores:
            for c in range(cartas_por_jogador):
                jogador.add_carta_no_topo(self.cartas.pop())

