class No:
    def __init__(self, dado:int, next=None):
        self.dado = dado; self.next = next 
class Fila:
    def __init__(self):
        self.primeiro = None; self.ultimo = None; self.size = 0
    @property
    def fila_vazia(self):
        return self.tamanho == 0
    @property
    def filaCheia(self):
        return False
    @property
    def tamanho(self):
        return self.size

    def enfileirar(self, dadinho:int):
        no = No(dadinho)
        if self.fila_vazia:
            self.primeiro = no
            self.ultimo = no
        else:
            self.ultimo.next = no
            self.ultimo = no
        self.size +=1

    def desenfileirar(self):
        no = self.primeiro.dado
        self.primeiro = self.primeiro.next
        self.size -=1
        return no
    def mostrar_numero(self, posicao:int):
        if self.fila_vazia:
            raise Exception("Fila Vazia")
        else:
            if posicao<=0 and posicao> self.tamanho:
                raise Exception(IndexError)
            else:
                no = self.primeiro
                for x in range(posicao):
                    no = no.next
        return no.dado
    
    def posicao_numero(self, dadinho):
        if self.fila_vazia:
            raise Exception("Fila Vazia")
        else:
            no = self.primeiro
            posicao = 0
            while no == self.ultimo:
                if no.dado == dadinho:
                    return posicao
                posicao+=1
                no = no.next
            return "Não Existe"
    def modificar(self, posicao:int, dado:int):
        if self.fila_vazia:
            raise Exception
        else:
            no = self.primeiro
            for a in range(posicao):
                no = no.next
            no.dado = dado

    def __str__(self):
        resposta = "["
        no = self.primeiro
        for x in range(self.tamanho):
            if x < self.tamanho - 1:
                resposta += str(no.dado)
                resposta += ", "
                no = no.next
            else:
                resposta += str(no.dado)
        resposta += "]"
        return resposta
    def imprimir(self):
        print(self)

filinha = Fila()
filinha.enfileirar(10)
filinha.enfileirar(20)
filinha.imprimir()
filinha.enfileirar(30)
filinha.imprimir()
filinha.desenfileirar()
filinha.imprimir()
filinha.enfileirar(40)
filinha.imprimir()