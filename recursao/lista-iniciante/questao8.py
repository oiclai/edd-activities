'''
Faça uma função recursiva chamada menores_rec() que receba como parâmetro um list de valores
numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor
inferior a key. O protótipo da função é definido por:
def menores_rec( lista, key )
'''

def menores_rec(lista, n):
    if len(lista) == 0:
        return 0
    if lista[0] < n:
        return 1 + menores_rec(lista[1:], n)
    else:
        return 0 + menores_rec(lista[1:], n)
    
# programa

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5
# e p da 4
print(menores_rec(lista, n))