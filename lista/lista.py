# mais generica
# list do python n é uma lista mas faz tudo q ela faria
# implementação diferente da fila, pilha
# nó da lista == tipo de dados + coisas auxiliares
'''
(L= NONE---->)[] --> [] --> [] --> [] --> X
L já representa o final da lista
'''
# lista simplesmente encadeada
class Node:
    def __init__(self, pessoa = "MMC"):
        self.p = pessoa
        self.next = None
    def __str__(self):
        return self.p
    
def print_lista(lista):
    print("LISTA: [", end=" ")
    p = lista
    while p != None:
        print(p, end=" ")
        p = p.next # atenção aqui
    print("]")

def insere_inicio(head, pessoa): # head != L ( head= copia de L)
    # L ---> X [] ----> X (n foi feita a ligação ainda)
    auxiliar = head 
    head = Node(pessoa)
    head.next = auxiliar # L ---> [] ---> X
    return head
L = None # criando  vazia # Tipo simples (sao passados por copia)
L = insere_inicio(L, "Thiago") # transforma L  na copia
L = insere_inicio(L, "Mariana") # transforma L  na copia
L = insere_inicio(L, "Claras") # transforma L  na copia
print_lista(L)
'''
referencia != copia
None não passa cmo referencia, so como copia
a = []
b = []
a = b
a.append(10)
b.append(70)
print(a, b)
'''

'''
tipo complexo = referencia
so exsite 1 lista, mas varias variaveis podem representalas

mas qunado sao interios???
'''
# ---------------------------------------------------------------
def insere_final (head, nome):
    p = head
    if p == None: # estrategia p driblar o erro da lista vazia
        return Node(nome)
    # se a lista estiveer vazia vai dar errado!!!!!! n existe next 
    while p.next != None:
        p = p.next
    p.next = Node(nome)

L = insere_final(L, "Davis")
L = insere_final(L, "Arthur")
# HEAD NAO TEM VALOR NESSE CASO
#         /--------
# no0 --| [no1]  |--> [no2] ----> [no3] -----> None
L = L.next.next # (no0)---->(no2) APAGA NO2
L.next = L.next.next # (no1) ---> (no3)
print_lista(L)

# como deletar 

def inserir(self, dado, indice)
# Inserção no índice desejado
    novo_no = No(dado, indice)

    # Caso especial: inserir no início (índice 0)
    if indice == 0:
        novo_no.proximo = self.head
        self.head = novo_no
    else:
        # Percorre até o nó anterior à posição onde o novo nó será inserido
        atual = self.head
        for _ in range(indice - 1):
            atual = atual.proximo
        
        # Insere o novo nó
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    # Atualiza a posição dos nós subsequentes
    atual = novo_no.proximo
    while atual:
        atual.posicao += 1  # Aumenta a posição de cada nó subsequente
        atual = atual.proximo
