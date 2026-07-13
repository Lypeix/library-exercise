from models import Book
import json

def save_books(books):
    data = []

    for book in books:
        data.append({
            "name": book.name,
            "author": book.author,
            "price": book.price,
            "genre": book.genre,
            "date": book.date
            })

    with open("books.json", "w") as file:
        json.dump(data, file, indent=4)

def load_books():
    try:
        with open("books.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    books = []

    for value in data:
        book = Book(
            value['name'],
            value['author'],
            value['price'],
            value['genre'],
            value['date']
        )

        books.append(book)

    return books
