'''
10) Um material radioativo denominado invictus, quando em contato com o oxigênio, perde metade de sua
massa a cada 50 segundos. Faça um função recursiva que receba uma quantidade de massa do invictus,
em gramas, e exiba o tempo (em segundos) necessário para que sua massa se torne menor que 0,8 g. A
função também deve retornar o o valor da massa final.
'''

# questao de meia-vida

def invictus(massa, seg= 0):
    if massa < 0.8:
        return massa, seg
    else:
        return (massa / 2, seg+ 50)

# programa

massa = 1
print(invictus(massa))