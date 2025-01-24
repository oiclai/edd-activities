'''
13)Dado um vetor de números reais, escreva uma função recursiva para determinar a soma dos elementos
do vetor.
'''
# n = tamanho
def soma(vetor, n):
    if n == 0:
        return 0
    else:
        return vetor[n-1] + soma(vetor, n-1)
    

print(soma([1, 2, 3, 4, 5], 5))