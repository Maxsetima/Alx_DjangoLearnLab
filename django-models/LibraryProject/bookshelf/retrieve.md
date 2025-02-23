# Retrieve Operation
Retrieve and display all attributes of the book you just created.

book = Book.objects.get(title="1984") print(book.title, book.author, book.publication_year)
## Python Command
```python
book = Book.objects.get(title="1984")
print(book)
