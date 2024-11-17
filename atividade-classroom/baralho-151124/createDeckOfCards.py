'''
relação suit - (value/card)
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
paus: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
copas: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
ouros: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
espadas: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
'''
import random; from predefCard import UnitaryCard; from players import Player;
# representa o Baralho (o "cria") + métodos para embaralhar e distribuir cartas p 'n' jogadores.
class DeckOfCards:
    # definida antes de uma instancia ser criada
    value_cardRelationship = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Dama': 12, 'Rei': 13
    }
    def __init__(self): 
    # método construtor - que nesse caso cria o baralho assim q uma instancia for criada
        self.__cardsSet = []
        # "arquitetura de matriz"
        for suit in ["Ouros", "Espadas", "Copas", "Paus"]: # linhas
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]: # colunas
                self.__cardsSet.append(UnitaryCard(value, suit))


    def shuffle(self): # embaralhar
        random.shuffle(self.__cardsSet)
    
    def dealCards(self, numberOfPlayers):
        for player in players:
            for i in range(len(self.__cardsSet)):
                player.addCard(self.__cardsSet.pop())

    def __str__(self): # imprimir
        return f"Baralho c/ {len(self.__cardsSet)} cartas"