from pilha.array_ifpb import Array


class PilhaVaziaException(Exception):
    pass


class PilhaCheiaException(Exception):
    pass

class No:
    def __init__(self, dado: int, proximo=None):
        self.dado:int = dado
        self.proximo: No|None = proximo
    def __repr__(self):
        return f"No({self.dado})"

class Pilha:
    def __init__(self):
        self.__topo: No|None = None
        self.__tamanho: int = 0
    @property
    def estah_vazia(self) -> bool:
        return self.tamanho == 0
    @property
    def estah_cheia(self) -> bool:
        return False
    @property
    def tamanho(self) -> int:
        return self.__tamanho
    def __len__(self) -> int:
        return self.tamanho
    def empilhar(self, dado: int):
        no = No(dado, proximo=self.__topo)
        self.__topo = no
        self.__tamanho += 1
    def desempilhar(self) -> int:
        if self.estah_vazia:
            raise PilhaVaziaException()
        valor = self.__topo.dado
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor
    def subtopo(self):
        if self.estah_vazia:
            raise PilhaVaziaException("Pilha Vazia!!!!!!!!!!!!!!!!1")
        if self.__topo.proximo is None:  
            raise PilhaVaziaException("A pilha tem apenas um elemento.")
        return self.__topo.proximo.dado 
    def desempilha_n (self, n: int):
        if self.estah_vazia or n > self.tamanho:
            raise PilhaVaziaException()
        for x in range(n):
            self.desempilhar()
    def esvaziar(self):
        while not self.estah_vazia:
            self.desempilhar()
        self.__topo = None; self.__tamanho = 0
    def obtemBase(self) -> int:
        if self.estah_vazia:
            raise PilhaVaziaException()
        ultimoDado = self.__topo
        while ultimoDado.proximo is not None: # vai "descer" até chegar na base ('item[0]' se fosse em uma array )
            ultimoDado = ultimoDado.proximo
        return ultimoDado.dado
    def __str__(self) -> str:
        resposta = "["
        no_atual: No|None = self.__topo
        for x in range(self.tamanho):
            resposta += str(no_atual.dado)
            if x != self.tamanho - 1:
                resposta += ", "
            no_atual = no_atual.proximo
        resposta += "]"
        return resposta


    def imprimir(self):
        print(self)
