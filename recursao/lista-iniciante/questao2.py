'''
Faça uma função recursiva chamada printstr()
que imprima na tela uma string (caractere a caractere).
'''
def printstr(palavra):
    if len(palavra) == 0:
        return
    print(palavra[0], end="")
    printstr(palavra[1:])


# programa

teste = 'claraaaaa'
printstr(teste)