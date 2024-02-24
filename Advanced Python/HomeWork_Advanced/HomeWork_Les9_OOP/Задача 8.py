class Book:
    def __init__(self, year_published, name, author, num_pages):
        self.year_published = year_published
        self.name = name
        self.author = author
        self.num_pages = num_pages

    @staticmethod
    def count_books_public(bookses_list, targets_year):
        count = 0
        for book in bookses_list:
            if book.year_published == targets_year:
                count += 1
        return count


bookses_list = [
    Book(2024, "Зеленский и Украина", "Зеленский Володя", 2880),
    Book(1930, "Лес снов", "Алексей Михайлов", 1900),
    Book(2003, "Олег и Кринж", "Евгений и Сергей", 140),
    Book(1972, "Настя и Олег", "Неизвестный автор", 220),
]

targets_year = 2003
count_books = Book.count_books_public(bookses_list, targets_year)

print(f"Кол во книг которые вышли в {targets_year} году: {count_books}")
