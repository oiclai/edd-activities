class No:
    def __init__(self, dado, proximo=None):
        self.dado = dado
        self.proximo = proximo

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
    @property
    def vazio(self) -> bool:
        # ou self.tamanho == 0
        return self.primeiro == None
    def add_dado(self, dado):
        newNo = No(dado)
        if self.vazio():
            self.primeiro = newNo
            self.ultimo = newNo
        else:
            self.ultimo.proximo = newNo
            self.ultimo = newNo
        self.tamanho += 1

    def remove_dado(self):
        if self.vazio():
            raise Exception("Fila vazia")
        dado = self.primeiro.dado
        self.primeiro = self.primeiro.proximo
        self.tamanho -= 1
        return dado

    def __str__(self):
        elementos = []
        atual = self.primeiro
        while atual != None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos)
    