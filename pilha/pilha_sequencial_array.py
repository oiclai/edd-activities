class Pilha:
    def __init__(self):
        self.lista=[]
        # self.tam=0
    def add(self, livro):
        self.lista.append(livro)
    def vazio(self):
        return(len(self.lista) == 0)
        # return (self.tam == 0) # true or false
    def get(self):
        livro = self.lista[-1]
        del(self.lista[-1])
        return livro
    def __str__(self):
        return '-'.join(self.lista)
    
caixa = Pilha()
caixa.add('livro1')
caixa.add('livro2')
caixa.add('livro3')
print(caixa)
print(caixa.get())
print(caixa)
cx2 = Pilha()
while not caixa.vazio():
    cx2.add(caixa.get())
print(caixa) # imprime vazio
print(cx2)