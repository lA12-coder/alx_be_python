class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
        
    def check_out(self):
        self.__is_checked_out = True
    def return_book(self):
        self.__is_checked_out = False
    def get_check_out_value(self):
        return self.__is_checked_out
        

class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self,book) -> None:
        self._books.append(book)
    def check_out_book(self,title) -> None:
        for book in self._books:
            if book.title == title:
                book.check_out()
                break                
            
    def return_book(self,title) -> None:
        for book in self._books:
            if book.title == title:
                if book.get_check_out_value()== True:
                    book.return_book()
                    break
                
                
    def list_available_books(self):
        for book in self._books:
            if book.get_check_out_value() == False:
                print(
                    f"{book.title} by {book.author}"
                )
                
                
