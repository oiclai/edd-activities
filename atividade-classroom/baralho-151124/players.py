# não compreendi bem a função de um montante, 
# mas acredito que seja uma lista que armazena as cartas
# que o jogador tirou do baralho
class Player:
    def __init__(self, name):
        self.__name = name; self.points = 0; self.montante = []; self.__hand = []
    def addCard(self, card):
        self.__hand.append(card)
    def pushCard(self):
        return self.__hand.pop()
    def cardsInHand(self):
        return len(self.__hand)
    def getCardValue(self, card):
        return card.numericValue
    def drawCard(self, card):
        self.montante.insert(0, card)
    def getCards(self):
        return self.__cards
    def showCards(self):
        print(F"Cartas de {self.nome}:")
        for card in self.__hand:
            print(f'{card}\n')
    def getPoints(self):
        return self.points
    def __str__(self):
        return self.__name
