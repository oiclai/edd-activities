'''
relação naipe - valor
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
paus: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
copas: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
ouros: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
espadas: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
'''
class Baralho:
    # definida antes de uma instancia ser criada
    relacaoValorCarta = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13
    }
    def __init__(self): # método construtor e cria o baralho
        self.__cartas = []
        for naipe in ["Ouros", "Espadas", "Copas", "Paus"]:
            for valor in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]:
                self.__cartas.append(Carta(valor, naipe))