'''
18)Implemente uma função recursiva que converta um número da base decimal para qualquer uma das
seguintes bases: binária (2), octal (8) e hexadecimal (16). A função deve obedecer ao seguinte protótipo:
def decToBase(num, base)
'''

def decToBase(num, base):
    if base == 2:
        return bin(num)
    elif base == 8:
        return oct(num)
    elif base == 16:
        return hex(num)
    

print(decToBase(10, 16)) # desse jeito a impressap fica 0xa - mas mais rapidoq 'manualmente'
# n entendi pq usar recursiva