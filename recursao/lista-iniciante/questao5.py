'''
5) Faça uma função recursiva chamada
compareStr(char *str1, char *str2) que retorne:
0: str1 é igual a str2;
1: str1 é maior que str2;
-1: str1 é menor que str2;
'''
# entendi como comparação de valor de caract.
def compareStr(str1, str2):
    if not str1 and not str2: # caso base e nesse casp é quando as str sao iguais (se tornam vazias com o passar da 'chamada da ufncao')
        return 0
    if not str1:
        return -1
    if not str2:
        return 1
    if str1[0]< str2[0]:
        return -1
    elif str1[0] > str2[0]:
        return 1
    return compareStr(str1[1:], str2[1:])

# teste

str1 = 'claraaaaa'
str2 = 'clareeeee'
print(compareStr(str1, str2))
# ------------------------------------------------------------------------------------------

