'''
Faça uma função recursiva denominada seqTermos1() que calcule a soma dos n termos da série:
n = 1 2 3 4 5 n
série: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
def seqTermos1(n) , onde n é o número de termos
def seqTermos1(n):
if( n == 1 )
return 1
'''

def seqTermos1(n):
    if n == 1:
        return 1
    else:
        return 1 / n + seqTermos1(n-1)
    
# prog

n = 5
print(seqTermos1(n))