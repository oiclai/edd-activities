'''
Faça uma função recursiva chamada 
printInverse() que imprima uma string ao contrário
'''

def printInverse(palavra):
    if len(palavra) == 0:
        return
    print(palavra[-1], end="")
    printInverse(palavra[:-1])


#programa
printInverse("clara")