'''
15)Dado um vetor de números inteiro, escreva uma função recursiva para verificar se um vetor está ordenado
ou não.
'''
def ordenado(vetor, n):
    if n == 1:
        return True
    else:
        return vetor[n-1] >= vetor[n-2] and ordenado(vetor, n-1)



print(ordenado([1, 2, 3, 4, 5], 5))