class Book:
    def __init__(self, name, author, price, genre, date):
        self.name = name
        self.author = author
        self.price = price
        self.genre = genre
        self.date = date

class Library:
    def __init__(self):
        self.books = []

    def book_add(self, book):
        self.books.append(book)

    def total_price(self):
        total = 0

        for book in self.books:
            total += book.price

        return total

