class PilhaVaziaException(Exception):
    pass
class PosicaoInvalida(Exception):
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
    def add_dado(self, dado:any):
        newNo = No(dado) # instancia
        newNo.proximo = self.topo
        self.topo = newNo
        self.tamanho +=1
# =========================================================================================
    def remove_dado(self):
        if self.pilha_vazia:
            raise PilhaVaziaException("Pilha vazia")
        else:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -=1
        return no
# =========================================================================================
    def mostre_no_especifico (self, posicao):
        if posicao < 0 or posicao > self.tamanho - 1:
           raise PosicaoInvalida()
        posicaoQueQueroChegar = self.topo # inicio
        if self.tamanho == 1:
           return self.topo
        for _ in range(posicao):
           posicaoQueQueroChegar = posicaoQueQueroChegar.proximo
        return posicaoQueQueroChegar
# =========================================================================================
    def inverter_pilha(self):
        if self.pilha_vazia:
            raise PilhaVaziaException("Pilha vazia")
        pilhaAux = Pilha()
        while not self.pilha_vazia:
            pilhaAux.add_dado(self.remove_dado().dado)
        while not pilhaAux.pilha_vazia:
            self.add_dado(pilhaAux.remove_dado().dado)
        return self
# ============================== TESTE =====================================================
pilha = Pilha()
pilha.add_dado(10)
pilha.add_dado(20)
pilha.add_dado(30)
print(pilha)
teste = pilha.mostre_no_especifico(1)
print(teste)            
