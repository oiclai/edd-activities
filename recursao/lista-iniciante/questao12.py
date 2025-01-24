'''
12) Faça uma função recursiva denominada seqTermos2() que calcule a soma dos n termos da série:

2
4 +
5
5 +
10
6 +
17
7 +
26
8 +⋯+ (�ଶ + 1)
(� + 3)

def seqTermos2( n);
'''

def seqTermos2(n, seq=1):
    if seq > n:
        return 0
    formula = (seq**2 + 1) / seq + 3
    return formula + seqTermos2(n, seq + 1)

# Teste
n = 5
print(seqTermos2(n))
