# Admin Integration for Book Model

## Register the Book Model
In the `bookshelf/admin.py` file, we registered the `Book` model with the Django admin interface:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
