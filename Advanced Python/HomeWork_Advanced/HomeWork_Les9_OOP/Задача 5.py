class Book:
    def __init__(self, author, born, title):
        self.author = author
        self.born = born
        self.title = title

    def __str__(self):
        return f"Автор хуйни {self.author}, название хуйни {self.title}, год издания хуйни {self.born}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        if not self.books:
            return "Нихуя нету! ПУСТО БЛЯТЬ"

        book_list = "\n".join(str(book) for book in self.books)
        return f"Книги в бибилиии:\n{book_list}"


library = Library()

book_1 = Book("Олег Артур Женя Миша Серега",1941, "Хуйня постная")
book_2 = Book("Степан", 2001, "Как создать себя?")
book_3 = Book("Алексей", 1932, "Психология Фрейда")

library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)

print(library)