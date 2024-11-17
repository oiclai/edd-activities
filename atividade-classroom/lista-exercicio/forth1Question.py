from forthQuestion import ContaCorrente
'''
Escreva um programa para criar dez instâncias de ContaCorrente, armazenando-os iem uma list.
Os valores para inicialização dos objetos deverão ser lidos do teclado;
'''
listandoContas = []
for _ in range(3):
    numero = input("Digite o número da conta: ")
    saldo = float(input("Digite o saldo inicial da conta: "))
    nome = input("Digite o nome do titular: ")
    conta = ContaCorrente(numero, saldo, nome)
    listandoContas.append(conta)

    def get_conta(numero, listandoContas):
        for conta in listandoContas:
            if conta.numero == numero:
                return conta
        return None