class CardGame:
    def __init__(self, numberPlayers):
        if numberPlayers < 2:
            raise ValueError("> O jogo precisa de pelo menos 2 jogadores")
        self.numberPlayers = numberPlayers
        print(f"> Jogo iniciado com {self.numberPlayers} jogadores.")
