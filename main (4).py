""" Сарибекян Милена 43ИС """
""" Класс Библиотека должен содержать список книг и методы для добавления и удаления книг, а также для отображения списка книг. """
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(book)

# Пример использования
library = Library()
book1 = Book("Rule №1 don't be №2", "Daniel Milstein", 2017)
book2 = Book("The Picture of Dorian Gray", "Oscar Wilde", 1891)

library.add_book(book1)
library.add_book(book2)

library.display_books()  
