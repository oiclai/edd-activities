'''
Considere que todas as estruturas devem ser implementadas de forma encadeada
Implemente o método para inserir um elemento na fila.
Implemente o método para remover um elemento na fila.
Implemente o método para concatenar para a fila.
Implemente o método para imprimir os elementos da fila.
Implemente o método para inserir um elemento na pilha.
Implemente o método para remover um elemento na pilha.
Implemente o método para obter um elemento da posição X da pilha.
Implemente o método para inverter a pilha.
Implemente o método para inserir um elemento na lista.
Implemente o método para remover um elemento na lista.
Implemente o método para checar_duplicidade da lista.
Implemente o método para obter um elemento da posição X da lista.
Implemente o método para alterar o valor de uma posição X da lista.
'''
class Node:
    def __init__(self, dado, proximo=None): # proximo = opcional, None = indicando final da pilha
        self.dado = dado
        self.proximo = None|Node = proximo
class Pilha:
    def __init__(self):
        self.topo = None
    def empilhar(self, dado):
        self.topo = Node(dado, self.topo)
    def desempilhar(self):
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado
    def inverter(self):
        pilhaAuxiliar = Pilha()
        while not self.estah_vazia():
            pilhaAuxiliar.empilhar(self.desempilhar())
        while not pilhaAuxiliar.estah_vazia():
            self.empilhar(pilhaAuxiliar.desempilhar())