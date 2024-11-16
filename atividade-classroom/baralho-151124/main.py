from players import CardGame
while True:
    try:
        numberPlayers = int(input("> Quantos jogadores irão jogar? "))
        game = CardGame(numberPlayers) # instancia
        break  # se for mais de 1 jogadores o programa continua
    except ValueError as e:
        print(e)  # erro se o número for inválido

