'''
Faça uma função recursiva chamada decToBin() que receba um número inteiro na base decimal e
imprima seu correspondente na base binária. O protótipo da função é definido por:
def decToBin( num )
'''

def decToBin(n):
    if n == 0:
        return 0
    else:
        return n % 2 +10*decToBin(n//2)
    

# testandoo
print(decToBin(10))
print(decToBin(12))
#  1010
# 1100