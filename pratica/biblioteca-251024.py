from datetime import datetime, timedelta
'''
INFO FIXA DEFINIDA
> USER @ALUNO ASSIM QUE CRIADO APRESENTA 60 CREDITOS
> TEMPO MAXIMO PARA DEVOLUCAO = 30 DIAS 
> A CADA LIVRO PASSADO DO PRAZO CREDITO - = 1; SE OS CREDITOS SE ESGOTAREM = ALUNO PERDE A LIBERDADE DE SOLICITAR EMPRESTIMO
'''
class User_Student:
    def __init__(self, studentName, id_studentCPF, restrictionCredit = 60):
        self.studentName = studentName; self.id_studentCPF = id_studentCPF;
        self.bookAcess = True; self.restrictionCredit = restrictionCredit;

class Book:
    def __init__ (self, bookName, bookPublisher, id_book):
        self.bookName = bookName; self.bookPublisher = bookPublisher; self.id_book = id_book;
        self.toLoan = False; # inicialmente no sistema o livro nao foi emprestado
    
    def loaned(self, loanedDate): # metodo EMPRESTADO
        self.loanedDate = loanedDate; self.bookLoanedDate = datetime.strptime(loanedDate, "%d/%m/%Y");
        self.toLoan = True; # livro emprestado

    def loanReturned(self, dateReturned):
        self.dateReturned = dateReturned; self.maxReturnDate = self.loanedDate + timedelta(days=30);
        if self.dateReturned > self.maxReturnDate:
            User_Student()
        self.toLoan = False;