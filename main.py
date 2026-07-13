from models import Book, Library


book1 = Book("Glory of Rome",
             "Edward",
             60,
             "History",
             "11/07/2026"
             )

library = Library()

library.book_add(book1)

for book in library.books:
    print(f"Name: {book.name} - Author: {book.author} - Price: {book.price} - Genre: {book.genre} - Added on: {book.date}")

print(f"Total price: {library.total_price()}")