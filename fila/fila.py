class Fila:
    def __init__(self):
        self.lista=[]
        # self.tam=0
    def add(self, livro):
        self.lista.append(livro)
    def vazio(self):
        return(len(self.lista) == 0)
        # return (self.tam == 0) # true or false
    def get(self):
        livro = self.lista[0]
        del(self.lista[0])
        return livro
    def __str__(self):
        return '-'.join(self.lista)
    
