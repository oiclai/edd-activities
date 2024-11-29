from array_ifpb import Array


class PilhaVaziaException(Exception):
    pass


class PilhaCheiaException(Exception):
    pass


class Pilha:
    # solução utilizando lista do Python


    def __init__(self):
        self.__dados = []


    @property
    def estah_vazia(self) -> bool:
        return len(self.__dados) == 0


    @property
    def estah_cheia(self) -> bool:
        return False


    @property
    def tamanho(self) -> int:
        return len(self.__dados)


    def __len__(self) -> int:
        return self.tamanho


    def empilhar(self, dado: int):
        self.__dados.append(dado)


    def desempilhar(self) -> int:
        if self.estah_vazia:
            raise PilhaVaziaException()
        return self.__dados.pop(-1)


    def __str__(self) -> str:
        return str(self.__dados)


    def imprimir(self):
        print(self)




class Pilha:
    # solução utilizando arrays (sequencial)


    def __init__(self):
        self.__dados = Array(1, int)
        self.__quantidade = 0


    @property
    def estah_vazia(self) -> bool:
        return len(self) == 0


    @property
    def estah_cheia(self) -> bool:
        return len(self) == len(self.__dados)


    @property
    def tamanho(self) -> int:
        return self.__quantidade


    def __len__(self) -> int:
        return self.tamanho


    def _redimensionar(self):
        dados = self.__dados
        self.__dados = Array(len(dados) * 2, int)
        for i in range(self.tamanho):
            self.__dados[i] = dados[i]


    def empilhar(self, dado: int):
        if self.estah_cheia:
            self._redimensionar()




        self.__dados[self.__quantidade] = dado
        self.__quantidade += 1


    def desempilhar(self) -> int:
        if self.estah_vazia:
            raise PilhaVaziaException()


        valor = self.__dados[self.__quantidade - 1]
        self.__quantidade -= 1
        return valor




    def __str__(self) -> str:
        resposta = "["
        for x in range(self.tamanho):
            resposta += str(self.__dados[x])
            if x != self.tamanho - 1:
                resposta += ", "
        resposta += "]"
        return resposta


    def imprimir(self):
        print(self)




class No:


    def __init__(self, dado: int, proximo=None):
        self.dado:int = dado
        self.proximo: No|None = proximo


    def __repr__(self):
        return f"No({self.dado})"




class Pilha:
    # solução utilizando encadeamento de objetos


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
