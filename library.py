#Building library using only OOP (Object Oriented Programming)
class Book:
    def __init__(self, title, author):
        self.avaiable = True
        self.title = title
        self.author = author
    def checkout(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
        
    def return_book(self):
        self.avaiable = True
    def display_info(self):
        print(f"Title: {self.title}\n Author: {self.author}\n Available: {'Yes' if self.avaiable else 'No'}")
book1 = Book("SE601", "Munawwar")
book2 = Book("SE602", "Ahmed")
book3 = Book("CS615", "Abdul Rehman")

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def display_books(self):
        for book in self.books:
            book.display_info()
    def get_book_by_title(self,title):
        for book in self.books:
            if book.tiltle == title:
                return title
        return None
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
