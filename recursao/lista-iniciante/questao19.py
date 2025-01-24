'''
Faça uma função recursiva que retorne a soma de todos os elementos de um list de inteiros passado
como argumento. O protótipo da função é definido por:
'''

def soma_rec( lista ):
    if len( lista ) == 0:
        return 0
    else:
        return lista[0] + soma_rec( lista[1:] ) # = string
    
#

print( soma_rec( [1, 2, 3, 4, 5] ) )