'''
Calculadora.

Escreve um algoritmo em Python para realizar operações matemáticas encontradas em uma calculadora. 
> O seu programa deve exibir um menu contendo as operações de
 (i) soma,
 (ii)subtração,
 (iii)multiplicação e
 (iv) divisão. 
 
 Ao iniciar o programa,  o usuário deve ser consultado sobre seu nome e em seguida, em um loop, informar qual operação deseja realizar. Após escolher a operação o usuário deverá informar os dois operandos da operação e receber o resultado. Em seguida, o usuário deve ser consultado se deseja realizar uma nova operação ou encerrar a calculadora. No final do programa, ao usuário escolher a opção de sair, deve ser listada todas as operações realizadas contendo 
 (i) o nome da operação; (ii) os operandos envolvidos e (3) o resultado obtido.
'''
import os
def clear():
    os.system('clear||cls') # FUNCAO P/LIMPAR CONTEUDO DO TERMINAL 

class Calculadora: # CLASSE -> DEFINE AS CARACTERISTICAS (ATRIBUTOS) & COMPORTAMENTOS (MÉTODOS) QUE OS OBJETOS CRIADOS A PARTIR DELA TERÃO
    def __init__(self): # '__init__' : INVOCADO QUANDO NOVA INSTANCIA DE CLASSE É CRIADA *(METODO CONSTRUTOR)
        self.sequencia_operacoes = [] #-> ATRIBUTO DA CLASSE CALCULADORA
    
    def operacoes(self, user_operacao, numero1, numero2): # METODO ( DEFINE COMPORTAMENTO DO OBJETO)
        match (user_operacao):
            case 'i': # soma
                return 'SOMA', numero1+(numero2)
            case 'ii': #substracao
                return 'SUBSTRAÇÃO', numero1-(numero2)
            case 'iii': #multip
                return 'MULTIPLICAÇÃO', numero1*(numero2)
            case 'iv': #div
                    if numero2 !=0:
                        return 'DIVISÃO', numero1/(numero2)
                    else:
                        return 'Error: DIVISÃO POR ZERO. TENTE NOVAMENTE.', None
            case _:
                return 'Error: ESSA OPÇÃO NÃO EXISTE. TENTE NOVAMENTE.', None
                
    def print_informacoes(self, user_name): # METODO
        user_name=user_name.upper()
        print(f'''
        -------------------------- [ OPERAÇÕES FEITAS POR {user_name} ] ---------------------------------
        ''')
        if not self.sequencia_operacoes:
            print('Error: NO HISTÓRICO NÃO HOUVE NENHUMA OPERAÇÃO.')

        else:
            for operacao in self.sequencia_operacoes:
                nomeOperacao, numero1, numero2, resultado = operacao
                print(f"{nomeOperacao}: {numero1} e {numero2} = {resultado}")
            print(f'Obrigado por usar a calculadora, {user_name.upper()}!')
            print("----------------------------------------------------------------------------------------------")
# MENU DA CALCULADORA
calculadora=Calculadora() # INSTANCIA (variavel criada a partir..) -> DA CLASSE Calculadora; O 1º METODO CHAMADO É O '__init__' QUE VEM COM UMA LISTA VAZIA PARA ARMAZ. AS OPERAÇÕES
# -> INSTANCIA PERMITE ACESSAR ATRIBUTOS E METODOS DA CLASSE; *PODEMOS ACESSAR OS METODOS ACIMA COM ELA
print('''
         ----------------------------------------
        |    ANTES DO PROGRAMA SE INICIAR . . .  |
         ----------------------------------------
              ''')
user_name=input('> DIGITE SEU NOME: ')
clear()
while True:
    print('''
         -----------------------------------------------------------------
        | PROGRAMA CALCULADORA -> ESCOLHA A OPERACAO QUE DESEJA REALIZAR! |
         -----------------------------------------------------------------

                                (i) SOMA
                                (ii) SUBSTRACAO
                                (iii) MULTIPLICACAO
                                (iv)  DIVISAO
              ''')
    user_operacao=input('> ')
    numero1=float(input('DIGITE O 1º NÚMERO:\n>'))
    numero2=float(input('DIGITE o 2º NÚMERO:\n>'))
    clear()
    nomeOperacao, resultado = calculadora.operacoes(user_operacao, numero1, numero2) # ex.: 'soma', numero
    if resultado is not None:
        # adic a operação ao historico
        calculadora.sequencia_operacoes.append((nomeOperacao, numero1, numero2, resultado))
    continuar = input("Deseja realizar outra operação? (S/N): ").upper()
    if continuar != 'S':
        break  # encerra
calculadora.print_informacoes(user_name)