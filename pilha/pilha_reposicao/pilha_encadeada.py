
class Node:
    def __init__(self, dado:int, next=None):
        self.dado = dado; self.next = next;

class Pilha:
    def __init__(self):
        self.topo = None; self.size = 0;
    @property
    def estaVazia(self)->bool:
        return self.size == 0
    @property
    def estaCheia(self)->bool:
        return False
    @property
    def tamanho(self)->int:
        return self.size
    
    def empilhar(self, dadinho:int):
        if self.estaVazia:
            self.topo = Node(dadinho)
        else:
            no = Node(dadinho, self.topo)
            self.topo = no
        self.size += 1

    def desempilhar(self)-> int:
        if self.estaVazia:
            raise Exception()
        valor = self.topo.dado
        self.topo = self.topo.next
        self.size -=1
        return valor
    def modificar(self, posicao:int, novonumero:int)->int:
        # self.novonumero = novonumero
        if self.estaVazia:
            raise Exception()
        else:
            no = self.topo
            for x in range(posicao):
                no = no.next
            no.dado = novonumero
            return no.dado


    def buscar(self, dadinho:int)->int:
        if self.estaVazia():
            raise Exception("Pilha vazia!")
        else:
            no = self.topo
            posicao = 0
            while no:
                if no.dado == dadinho:
                    return posicao
                no = no.next
                posicao +=1
            return "Não foi Encontrado"
    def __str__(self): 
        if self.estaVazia:
            return "[]"
        else:
            resposta = "["
            atual = self.topo
            for a in range(self.tamanho):
                resposta += str(atual.dado)
                if a != (self.tamanho-1):
                    resposta += ", "
                atual = atual.next
            resposta += "]"
            return resposta

    def imprimir(self):
        print(self) # internamente usa o __str__

    def show_elemento(self,  posicao:int)->int:
        if self.estaVazia():
            raise Exception("adivinha? Pilha Vazia, diva!")
        else:
           if posicao >= self.tamanho and posicao < 0:
               raise IndexError("Posição Inválida, bb")
           atual = self.topo
           for i in range(posicao):
               atual = atual.next
        return atual.dado

# ---------------------------------------------------------------------------------------
pilhinha = Pilha()
pilhinha.empilhar(10)
pilhinha.imprimir()
pilhinha.empilhar(20)
pilhinha.imprimir()
pilhinha.empilhar(30)
pilhinha.imprimir()
pilhinha.desempilhar()
pilhinha.imprimir()
pilhinha.empilhar(40)
pilhinha.imprimir()