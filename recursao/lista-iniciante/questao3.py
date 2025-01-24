'''
Faça uma função recursiva chamada invertString()
que retornte a sequência de caracteres de uma
string passada como argumento na ordem inversa
'''

def invertString(palavra):
    if len(palavra) == 0:
        return "" 
    return invertString(palavra[1:]) + palavra[0]

#programa
print(invertString("clara"))
