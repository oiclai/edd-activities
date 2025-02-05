'''
Arvore 'BST'
'''
class Node:
    def __init__(self, bola:int):
        self.bola = bola
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, bola:int):
        if self.root is None:
            self.root = Node(bola)
        else:
            self._insert(self.root, bola)

    def _insert(self, node, bola:int):
        if bola < node.bola:
            if node.left is None:
                node.left = Node(bola)
            else:
                self._insert(node.left, bola)
        else:
            if node.right is None:
                node.right = Node(bola)
            else:
                self._insert(node.right, bola)

    def search(self, bola:int):
        if self.root is None:
            return False #vazia - s/raiz
        else:
            return self._search(self.root, bola)
    def _search(self, node, bola:int):
        if bola == node.bola:
            return True
        elif bola < node.bola and node.left is not None:
            return self._search(node.left, bola)
        elif bola > node.bola and node.right is not None:
            return self._search(node.right, bola)
        return False
        