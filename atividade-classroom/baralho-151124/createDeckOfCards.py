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
        for suit in ['Ouros', 'Espadas', 'Copas', 'Paus']:
            # linhas
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']:
                # colunas
                self.__cardsSet.append(UnitaryCard(value, suit))


    def shuffle(self): # embaralhar
        random.shuffle(self.__cardsSet)
    
    def dealCards(self, numberOfPlayers):
        totalDeckCards = len(self.__cardsSet);
        cardsPerPlayer = totalDeckCards // numberOfPlayers;
        cardsToDeal = cardsPerPlayer * numberOfPlayers;
        self.__cardsSet = self.__cardsSet[:cardsToDeal]
        self.numberOfPlayers = numberOfPlayers;
        if not (1 <= self.numberOfPlayers <= 4):
            raise ValueError("Número de jogadores deve ser entre 1 e 4.")
        
        hands = []  # armazenará as mãos dos jogadores
        for _ in range(numberOfPlayers):
            hands.append([])  # add list vazia para cada jogador
    # distribuir as cartas do baralho entre os jogadores (maos)
        while self.__cardsSet:
            for hand in hands:
                if self.__cardsSet:
                    hand.append(self.__cardsSet.pop(0))
                    # remove a primeira carta do baralho e adiciona à mão do jogador
        return hands
    def __str__(self): # imprimir
        return f"Baralho c/ {len(self.__cardsSet)}"