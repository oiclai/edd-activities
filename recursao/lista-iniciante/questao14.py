'''
14)Dado um vetor de números inteiro, escreva uma função recursiva para identificar o maior valor
armazenado no vetor.
'''

def maior(vetor, n):
    if n == 0:
        return vetor[0]
    else:
        return max(vetor[n-1], maior(vetor, n-1))
    

print(maior([1, 2, 3, 4, 5], 5))