'''
Faça uma função recursiva chamada ispalindrome() que
retorne verdadeiro caso uma string seja palíndrome, ou 
falso caso contrário. O protótipo da operação é definido por:
def ispalindrome(str)
'''

def isPalindrome(str:str) -> bool:
    if not str or len(str) == 1: # string[0] != string[-1]
        # nem precisava do len(str) == 1 => arara (o 'a' iria p if str[0]==str[1]
        return True
    if str[0] == str[-1]:
        return isPalindrome(str[1:-1]) # 'retiranod' as beiradas da palavra
    return False

'''
arara - return isPalindrome(arara[1:-1])
rar - return isPalindrome(rar[1:-1])
a - return True ( len(str) == 1 )
'''
print(isPalindrome('arara'))
