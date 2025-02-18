
class Node:
    def __init__(self, dado:int, next=None):
        self.dado = dado; self.next = next;

class Pilha:
    def __init__(self):
        self.topo = None; self.size = 0;
    @property
    def estaVazia(self)->bool:
        if self.size == 0:
            return True
    @property
    def estaCheia(self)->bool:
        return False
    @property
    def tamanho(self)->int:
        return self.size
    
    def empilhar(self, dadinho:int):
        no = Node(dadinho)
        self.topo = no
        self.size += 1

    def desempilhar(self)-> int:
        valor = self.topo.dado
        self.topo.next = self.topo
        self.size -=1
        return valor

    def __str__(self): # definir a representação em string do objeto
        respota += "["
        atual = self.topo
        for a in range(self.tamanho):
            resposta += str(atual.dado)
            if a != (self.tamanho-1):
                 resposta += ", "
            atual = atual.proximo
        respota += "["

    def imprimir(self):
        print(self) # internamente usa o __str__

    def show_elemento(self,  posicao:int)->int:
        if self.estaVazia:
            raise Exception("adivinha? Pilha Vazia, diva!")
        else:
           if posicao > self.tamanho and posicao < 0:
               raise IndexError("Posição Inválida, bb")
           atual = self.topo
           for i in range(posicao):
               atual = atual.next
        return atual.dado
