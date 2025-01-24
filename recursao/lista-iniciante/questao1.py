'''
Faça uma função recursiva chamada recursiveLength()
que retorne a quantidade de caracteres de um string.
'''

def recursiveLength(palavra:str) -> int:
    if len(palavra) == 0: # ou palavra == ""
        return 0
    return 1 + recursiveLength(palavra[1:]) # -> 'desmontando' a string 

# programa

teste = 'claraaaaa'
print(recursiveLength(teste))
