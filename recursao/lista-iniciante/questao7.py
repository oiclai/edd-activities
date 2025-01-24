'''
Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma
seria igual a 1 + 2 + 3 = 6
'''

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)
    
# programa
'''
3 - return 3 + soma(2) [3]
2 - return 2 + soma(1) [3 + 2]
1 - return 1 [3 + 2 + 1]
[6]
'''

print(soma(3))