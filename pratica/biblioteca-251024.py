from datetime import datetime, timedelta
'''
INFO FIXA DEFINIDA
> USER @ALUNO ASSIM QUE CRIADO (init) APRESENTA 60 CREDITOS
> TEMPO MAXIMO PARA DEVOLUCAO = 30 DIAS 
> A CADA LIVRO PASSADO DO PRAZO CREDITO - = 1
SE OS CREDITOS SE ESGOTAREM = ALUNO PERDE A LIBERDADE DE SOLICITAR EMPRESTIMO DE LIVROS
'''
class User_Student:
    def __init__(self, studentName, id_studentCPF, restrictionCredit = 60):
        self.studentName = studentName; self.id_studentCPF = id_studentCPF;
        self.bookAcess = True; self.restrictionCredit = restrictionCredit;

class Book:
    def __init__ (self, bookName, bookPublisher, id_book):
        self.bookName = bookName; self.bookPublisher = bookPublisher; self.id_book = id_book;
        self.toLoan = False; self.user = None; self.loanedDate = None 
        # inicialmente no sistema o livro nao foi emprestado (sem user), nao apresentando data de emprestimo (ele vai ganhando um historico de data de emprestimos)
    
    def loaned(self, user, loanedDate): # metodo EMPRESTADO
        self.user = user # quem pegou emprestado
        self.loanedDate = loanedDate; self.bookLoanedDate = datetime.strptime(loanedDate, "%d/%m/%Y");
        self.toLoan = True; # livro emprestado

    def loanReturned(self, dateReturned):
        self.dateReturned = datetime.strptime(dateReturned, "%d/%m/%Y")
        self.maxReturnDate = self.loanedDate + timedelta(days=30)
# CORREÇÃO USANDO O 'AND SELF.USER' -> A CONDICAO VERIFICA SE O SELF.USER É TRUE OU 
# FALSE (NONE == FALSE) OU SEJA, SE REALMENTE HÁ UM USUARIO SOLICITANDO O LIVRO.

        if self.dateReturned > self.maxReturnDate and self.user: 
            self.user.restrictionCredit -= 1  # reduz o credito
            print(f"{self.user.studentName} | Data de entrega máxima foi excedido.\nCréditos restantes: {self.user.restrictionCredit}")
        self.toLoan = False; self.user = None; # remove a referencia do usuario ja q o livro ja foi devolvido
            
