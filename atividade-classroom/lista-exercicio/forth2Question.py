# menu
from forthQuestion import ContaCorrente
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
            extrato()
        case 4:
            print("Saindo...")
            break