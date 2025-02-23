from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (for example, "Author1")
author = Author.objects.get(name='Author1')
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library (for example, "Library1")
library = Library.objects.get(name='Library1')
books_in_library = library.books.all()
print(f"Books in {library.name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a specific library (for example, "Library1")
library = Library.objects.get(name='Library1')
librarian_for_library = library.librarian
print(f"Librarian for {library.name}: {librarian_for_library.name}")
