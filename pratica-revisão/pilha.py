class PilhaVaziaException(Exception):
    pass
class No:
    def __init__(self, dado:int, proximo=None):
        self.dado = dado
        self.proximo = proximo
class Pilha:
    def __init__(self):
        self.tamanho = 0
        self.topo = None
    @property
    def pilha_vazia(self) -> bool:
        return self.tamanho==0
    def __str__(self):
        elementos = []
        atual = self.topo
        while atual != None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Pilha vazia"
# =========================================================================================    
    def add_dado(self, dado:int):
        newNo = No(dado) # instancia
        newNo.proximo = self.topo
        self.topo = newNo
        self.tamanho +=1
# =========================================================================================
    def remove_dado(self):
        if self.pilhaVazia:
            raise PilhaVaziaException() 
        else:
            self.topo = self.topo.proximo
            self.tamanho -=1
# =========================================================================================
    
pilha = Pilha()
pilha.add_dado(10)
pilha.add_dado(20)
pilha.add_dado(30)
print(pilha)