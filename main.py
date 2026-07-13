from models import Book, Library
from storage import save_books, load_books

book1 = Book("Glory of Rome",
             "Edward",
             60,
             "History",
             "11/07/2026"
             )

library = Library()
library.books = load_books()

library.book_add(book1)
save_books(library.books)


for book in library.books:
    print(f"Name: {book.name} - Author: {book.author} - Price: {book.price} - Genre: {book.genre} - Added on: {book.date}")

print(f"Total price: {library.total_price()}")
