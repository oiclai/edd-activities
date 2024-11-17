from functionSource import clear, pauseTime;
from createDeckOfCards import DeckOfCards; from players import Player; 

class Battle: # apenas dois jogadores
    def __init__(self, player1, player2, deckOfCards):
        self.__player1 = player1; self.__player2 = player2; 
        self.__deckOfCards = deckOfCards