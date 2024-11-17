# menu
from forthQuestion import ContaCorrente
from forth1Question import *

def menu():
    def option():
        print("1. Depositar\n2. Sacar\n3. Extrato\n4. Sair")
        opcao = int(input("Digite a opção desejada: "))
        return opcao
    match option():
        case 1:
            ContaCorrente.depositar()
        case 2:
            ContaCorrente.sacar()
        case 3:
            numConta = input("Digite o número da conta: ")
            conta_encontrada = get_conta(numConta, listandoContas)
            if conta_encontrada:
                print(f"Saldo da conta {numConta}: {conta_encontrada.saldo}")
            else:
                print("Conta não encontrada")

        case 4:
            print("Saindo...")
            return
