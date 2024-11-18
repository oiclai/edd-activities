from functionSource import clear, pauseTime
from createDeckOfCards import DeckOfCards
from players import Player

class Battle:
    def __init__(self):
        self.__player1 = Player('JOGADOR 1')
        self.__player2 = Player('JOGADOR 2')
        self.players = [self.__player1, self.__player2]
        self.__deckOfCards = DeckOfCards()
        self.cardsDraw = []

    def startBattle(self):
        print('> INICIANDO BATALHA !')
        pauseTime()
        clear()
        print('> EMBARALHANDO AS CARTAS ...')
        pauseTime()
        clear()
        self.__deckOfCards.shuffle()
        print('> DISTRIBUINDO AS CARTAS PARA OS JOGADORES ...')
        pauseTime()
        clear()
        self.__deckOfCards.dealCards(self.__player1, self.__player2)

    def round(self):
        clear()
        print(f'''RODADA INICIADA !
            JOGADOR 1 PEGA CARTA ...''')
        pauseTime()
        clear()
        card1 = self.__player1.drawCard()
        print(f'''CARTA PUXADA: {card1}
            JOGADOR 2 PEGA CARTA ...''')
        pauseTime()
        clear()
        card2 = self.__player2.drawCard()
        print(f'''CARTA PUXADA: {card2}
            COMPARANDO AS CARTAS...''')
        pauseTime()
        clear()
        card1_value = self.__player1.getCardValue(card1)
        card2_value = self.__player2.getCardValue(card2)

        if card1_value > card2_value:
            print('> O GANHADOR DA RODADA: JOGADOR 1 !')
            if self.cardsDraw:
                for card in self.cardsDraw:
                    self.__player1.addCard(card)
                self.cardsDraw = []
            self.__player1.addCard(card1)
            self.__player1.addCard(card2)

        elif card2_value > card1_value:
            print('> O GANHADOR DA RODADA: JOGADOR 2 !')
            if self.cardsDraw:
                for card in self.cardsDraw:
                    self.__player2.addCard(card)
                self.cardsDraw = []
            self.__player2.addCard(card1)
            self.__player2.addCard(card2)

        else:
            print('> EMPATE !')
            self.cardsDraw.append(card1)
            self.cardsDraw.append(card2)

        print('Rodada encerrada!')

    def determineWinner(self):
        # pontuação do Jogador 1: soma das cartas na mão e no montante
        player1_points = sum(self.__player1.getCardValue(card) for card in self.__player1.getHand()) + \
                         sum(self.__player1.getCardValue(card) for card in self.__player1.getMontante())

        # pontuação do Jogador 2: soma das cartas na mão e no montante
        player2_points = sum(self.__player2.getCardValue(card) for card in self.__player2.getHand()) + \
                         sum(self.__player2.getCardValue(card) for card in self.__player2.getMontante())

        # quem é oencedor 
        if player1_points > player2_points:
            return f'> {self.__player1.name} VENCEU! {player1_points} PONTOS X {player2_points} PONTOS'
        elif player2_points > player1_points:
            return f'> {self.__player2.name} VENCEU! {player2_points} PONTOS X {player1_points} PONTOS'
        else:
            return f'> ATENÇÃO: EMPATE! {player1_points} PONTOS X {player2_points} PONTOS'

# Simulação da batalha
battle = Battle()
battle.startBattle()


while battle.__player1.cardsInHand() > 0 and battle.__player2.cardsInHand() > 0:
    battle.round()

print(battle.determineWinner())
