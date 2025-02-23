from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (for example, "Author1")
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Fetch the author
    books_by_author = Book.objects.filter(author=author)  # Get books written by that author
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")

# List all books in a library (for example, "Library1")
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Fetch the library by its name
    books_in_library = library.books.all()  # Get books available in that library
    print(f"Books in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")

# Retrieve the librarian for a specific library (for example, "Library1")
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Fetch the library by its name
    librarian_for_library = Librarian.objects.get(library=library)  # Get librarian via the library relation
    print(f"Librarian for {library.name}: {librarian_for_library.name}")

# Sample usage:
get_books_by_author('Author1')
get_books_in_library('Library1')
get_librarian_for_library('Library1')
