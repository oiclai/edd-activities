'''
Faça uma função recursiva chamada printstr()
que imprima na tela uma string (caractere a caractere).
'''
def printstr(palavra: str) -> str:
    if len(palavra) == 0: # ou string ==""
        return # return necessario p interromper - no caso base (caso de parada)
    print(palavra[0], end="") # não colocar o '+'; joga o resto p recursão;
    printstr(palavra[1:])


# programa

teste = 'claraaaaa'
printstr(teste)
