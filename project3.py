# students can borrow a book from a list of book.
class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    
    def displayAvailableBooks(self):
        print("books present in the library are:")
        for books in self.books:
            print("\t~", books)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName} please keep it safe and return it on time within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("sorry this book is either not available or has already been issued by someone else please wait until the book is available or  returned")
            return False
        
    def returnBook(self,bookName):
        self.books.append(bookName)
        self.Book=input("thanks for returning this book! hope you enjoyed reading it have a great day ahead!")
       

class Students:
    def requestBook(self):
        self.book=input("enter the name of the book you want to borrow:")
        return self.book
  
    def returnBook(self):
        self.Book=input("enter the name of the book you want to return:")
        return self.Book
    
if __name__=="__main__":
    centralLibrary=Library(["Algorithms","Django","Clrs","Python Notes"])
    student=Students()
    
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg='''\n==== welcome to central library ====
        please choose an option:
        1. list all the books
        2. request a book
        3. add/return a book
        4. exit the library'''
        print(welcomeMsg)
     
        a=int(input("enter a choice:"))
        
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
         print("thanks for choosing cental library have a great day ahead!")
         exit()
        else:
           print("invalid choice")
    