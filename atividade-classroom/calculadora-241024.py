# recursos importados para melhor experiencia;
import os; import time;
def clear():
    os.system('clear||cls') # limpar terminal - unix e windows
def pauseTime():
    time.sleep(0.5)

# formação de classes e metodos
class Calculator:
    def __init__ (self, num1, num2, operacao, operationName, resultado):
        self.num1 = num1; self.num2 = num2;
        self.operacao = operacao; self.operationName = operationName; self.resultado = resultado;
    
    def __str__(self): # -> dificuldade; como o objeto retorna quando impresso (print()) como string
        return f'OPERAÇÃO: {self.operationName} | NÚMEROS: {self.num1} e {self.num2} | RESULTADO: {self.resultado}'
    # operacoes
    def addition (self):
        return self.num1 +(self.num2)
    def subtraction (self):
        return self.num1 -(self.num2)
    def multiplication (self):
        return self.num1 *(self.num2)
    def division (self):
        return self.num1 / self.num2

    
# programa 
clear()
print('''
         ----------------------------------------
        |    ANTES DO PROGRAMA SE INICIAR . . .  |
         ----------------------------------------
              ''')
user_name=input('> DIGITE SEU NOME: '); pauseTime(); clear();
historicoOperacoes = []
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
    operacao = input('> ').lower()
    num1=float(input('DIGITE O 1º NÚMERO:\n>'))
    num2=float(input('DIGITE o 2º NÚMERO:\n>'))

    if operacao == 'i': # (add)
            resultado = Calculator(num1, num2, operacao, 'ADIÇÃO', num1 + num2).addition()
            operationName = 'ADIÇÃO'
    elif operacao == 'ii': # (sub)
            resultado = Calculator(num1, num2, operacao, 'SUBTRAÇÃO', num1 - num2).subtraction()
            operationName = 'SUBSTRAÇÃO'
    elif operacao == 'iii': # (mult)
            resultado = Calculator(num1, num2, operacao, 'MULTIPLICAÇÃO', num1 * num2).multiplication()
            operationName = 'MULTIPLICAÇÃO'
    elif operacao == 'iv': # (div)
            if num2==0:
                print('Error: NÃO É PERMITIDO DIVISÃO COM ZERO! TENTE NOVAMENTE.')
                operationName = 'ERROR: TENTATIVA DE DIVISÃO'
                historicoOperacoes.append(operationName) # erro adc no historico
                continue
            else:
                resultado = Calculator(num1, num2, operacao, 'DIVISÃO', num1 / num2).division()
                operationName = 'DIVISÃO'
    else:
        print('Error: OPERAÇÃO INVÁLIDA! TENTE NOVAMENTE.')
        operationName = 'ERROR: OPERAÇÃO INVÁLIDA'
        historicoOperacoes.append(operationName) # erro adic no historico
        continue

    calcInstance = Calculator(num1, num2, operacao, operationName, resultado)
    historicoOperacoes.append(calcInstance)

    continueLoop = input("DESEJA REALIZAR OUTRA OPERAÇÃO? (S/N):\n> ").upper()
    clear()
    if continueLoop != 'S':
        break

print(f'''
        -------------------------- [ OPERAÇÕES FEITAS POR {user_name.upper()} ] ---------------------------------
        ''')
for _ in historicoOperacoes:
    print(_)
print("----------------------------------------------------------------------------------------------")
pauseTime()
print(f'''
                                OBRIGADA POR USAR A CALCULADORA, {user_name.upper()}!
                  ''')