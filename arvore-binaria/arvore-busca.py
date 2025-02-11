'''
Arvore 'BST' + comentários
'''
class Node:
    def __init__(self, bola:int):
        self.bola = bola
        self.esquerda = None
        self.direita = None

class Tree:
    def __init__(self):
        self.raiz = None

    def insert(self, bola:int): # metodo de insercao
        if self.raiz is None: # se n tiver raiz 
            self.raiz = Node(bola) # -> o novo no se torna a raíz
        else:
            self._insert(self.raiz, bola) # se ja tiver raiz, chama o metodo de inserção 'privado'

    '''
    nas arvores de busca:
    se o dado for menor q a raiz -> adc na esquerda
    se o dado for maior q a raiz -> adc na direita
    '''
    def _insert(self, node, bola:int):
        if bola < node.bola: # '.bola' acessa o valor do nó (definido previamente no 'Node')
            # ('node' sozinho é um objeto, para acessar seu valor o '.bola' é necessário)
            if node.esquerda is None:
                node.esquerda = Node(bola)
            else:
                self._insert(node.esquerda, bola) # recursaoo
        else:
            if node.direita is None:
                node.direita = Node(bola)
            else:
                self._insert(node.direita, bola) #recursao

    def search(self, bola:int):
        if self.raiz is None:
            return False #vazia - s/raiz
        else:
            return self._search(self.raiz, bola)
    def _search(self, node, bola:int):
        if bola == node.bola:
            return True
        elif bola < node.bola and node.esquerda is not None:
            return self._search(node.esquerda, bola)
        elif bola > node.bola and node.direita is not None:
            return self._search(node.direita, bola)
        return False
    def remove(self, bola:int):
        if self.raiz is not None:
            self._remove(self.raiz, bola)
    def _remove(self, node, bola:int):
        if bola < node.bola and node.esquerda is not None:
            self._remove(node.esquerda, bola)
        elif bola > node.bola and node.direita is not None:
            self._remove(node.direita, bola)
        else:
            if node.esquerda is not None and node.direita is not None:
                aux = self._maior(node.esquerda)
                node.bola = aux.bola
                self._remove(node.esquerda, aux.bola)
            elif node.esquerda is not None:
                node = node.esquerda
            elif node.direita is not None:
                node = node.direita
            else:
                node = None       
    def _maior(self, node):
        while node.direita is not None:
            node = node.direita
        return node
    def _menor(self, node):
        while node.esquerda is not None:
            node = node.esquerda
        return node
    def imprime(self):
        if self.raiz is not None:
            self._imprime(self.raiz)
    def _imprime(self, node):     
        if node is not None:
            self._imprime(node.esquerda)
            print(node.bola)
            self._imprime(node.direita)