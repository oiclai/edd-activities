from functionSource import clear, pauseTime
from createDeckOfCards import DeckOfCards
from players import Player

class Battle:
    def __init__(self):
        self.__player1 = Player("Jogador 1")
        self.__player2 = Player("Jogador 2")
        self.__players = [self.__player1, self.__player2]
        self.__deckOfCards = DeckOfCards()

    def startBattle(self):
        print("Batalha iniciada!")
        print("Embaralhando cartas...")
        pauseTime()
        self.__deckOfCards.shuffle()
        print("Distribuindo cartas...")
        pauseTime()
        self.__deckOfCards.dealCards(self.__player1, self.__player2)

    class Battle:
        def __init__(self):
            self.__player1 = Player()  # Defina a classe Player adequadamente
            self.__player2 = Player()
            self.cardsDraw = []

        def round(self):
            clear()
            print(f'''Rodada iniciada!
                Jogador 1 puxa carta...''')
            card1 = self.__player1.drawCard()
            print(f'''Carta puxada: {card1}
                Jogador 2 puxa carta...''')
            card2 = self.__player2.drawCard()
            print(f'''Carta puxada: {card2}
                Comparando cartas...''')

            card1_value = self.__player1.getCardValue(card1)
            card2_value = self.__player2.getCardValue(card2)

            if card1_value > card2_value:
                print("Jogador 1 ganha a rodada!")
                if self.cardsDraw:
                    for carta in self.cardsDraw:
                        self.__player1.addCard(carta)
                    self.cardsDraw = []
                self.__player1.addCard(card1)
                self.__player1.addCard(card2)

            elif card2_value > card1_value:
                print("Jogador 2 ganha a rodada!")
                if self.cardsDraw:
                    for carta in self.cardsDraw:
                        self.__player2.addCard(carta)
                    self.cardsDraw = []
                self.__player2.addCard(card1)
                self.__player2.addCard(card2)

            else:
                print("Empate!")
                self.cardsDraw.append(card1)
                self.cardsDraw.append(card2)

            print("Rodada encerrada!")

        def determineWinner(self):
            player1_points = sum(self.__player1.getCardValue(card) for card in self.__player1.getHand())
            player2_points = sum(self.__player2.getCardValue(card) for card in self.__player2.getHand())

            if player1_points > player2_points:
                return f'''{self.__player1.name} venceu!
                {player1_points} pontos X {player2_points} pontos'''
            elif player2_points > player1_points:
                return f'''{self.__player2.name} venceu!
                {player2_points} pontos X {player1_points} pontos'''
            else:
                return f"Empate! - {player1_points} pontos contra {player2_points} pontos"

# Simulação da batalha
battle = Battle()  # Criando a batalha (instância da classe Battle)
battle.startBattle()

winners = []
while battle.__player1.cardsInHand() > 0 and battle.__player2.cardsInHand() > 0:
    battle.round()

# Calculando os pontos após todas as rodadas
if battle.__player1.cardsInHand() == 0 or battle.__player2.cardsInHand() == 0:
    for player in [battle.__player1, battle.__player2]:
        for card in player.getHand():
            player.addPoints(battle.getCardValue(card))

    if battle.__player1.getPoints() > battle.__player2.getPoints():
        winners.append(f"{battle.__player1.name} venceu! - {battle.__player1.getPoints()} pontos contra {battle.__player2.getPoints()} pontos")
    elif battle.__player1.getPoints() < battle.__player2.getPoints():
        winners.append(f"{battle.__player2.name} venceu! - {battle.__player2.getPoints()} pontos contra {battle.__player1.getPoints()} pontos")
    else:
        winners.append(f"Empate! - {battle.__player1.getPoints()} pontos contra {battle.__player2.getPoints()} pontos")

for winner in winners:
    print(winner)