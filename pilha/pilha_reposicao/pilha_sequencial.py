class Node:
    def __init__(self, dado:int, next=None):
        self.dado = dado; self.next = next

class Pilha:
    def __init__(self):
        self.tamanhoDefinido = 5
        self.array = []

    @property
    def estaVazia(self)->bool:
        return len(self.array)== 0
    @property
    def estaCheia(self)->bool:
        return len(self.array) == self.tamanhoDefinido
    def posicao_para_elemento(self, posicao:int):
        for x in range(posicao):
            n = n.next
# not done