from django.contrib import admin
from .models import Book

# Define a custom admin class
class BookAdmin(admin.ModelAdmin):
    # Display the following fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for 'author' and 'publication_year' in the admin interface
    list_filter = ('author', 'publication_year')

    # Add search functionality for 'title' and 'author'
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)

