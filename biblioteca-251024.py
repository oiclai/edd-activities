from datetime import datetime, timedelta
class User_Student:
    def __init__(self, studentName, id_studentCPF):
        self.studentName = studentName; self.id_studentCPF = id_studentCPF;
class Book:
    def __init__ (self, bookName, bookPublisher, id_book):
        self.bookName = bookName; self.bookPublisher = bookPublisher; self.id_book = id_book;
        self.toLoan = False; # inicialmente no sistema o livro nao foi emprestado
    
    def loaned(self, loanedDate):
        self.loanedDate = loanedDate; self.bookLoanedDate =  datetime.strptime(loanedDate, "%d/%m/%Y");
        self.toLoan = True; # livro emprestado

    def loanReturned(self, dateReturned):
        self.dateReturned = dateReturned; self.maxReturnDate = self.loanedDate + timedelta(days=30);
        # if self.dateReturned > self.maxReturnDate:

        self.toLoan = False;