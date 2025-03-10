class No:
    def __init__(self, dado, next=None):
        self.dado = dado; self.next = next
class Lista:
    def __init__(self):
        self.primeiro = None; self.ultimo = None; self.size = 0
    
    @property
    def tamanho(self):
        return self.size
    @property
    def listaCheia(self):
        return False
    @property
    def listaVazia(self):
        return self.size == 0
    
    def achar_posicao(self, no):
        atual = self.primeiro
        posicao = 0
        while atual != no:
            atual = atual.next
            posicao += 1
        return posicao
    def achar_antecessor(self, no):
        posicao_antecessor = self.achar_antecessor(no) -1
        atual = self.primeiro
        for x in range(posicao_antecessor):
            atual = atual.next
        return atual.dado
    def adicionandoElemento(self, posicao:int, dadinho:int):
        if self.listaVazia:
            no = No(dadinho)
            self.primeiro = no
            self.ultimo = no
        # parei d mexer