# relationship_app/views.py
# Import the DetailView correctly
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book, Library

def list_books(request):
    # Get all books from the database
    books = Book.objects.all()
    # Render the template and pass the books to the template
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for Library Detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # The context variable to refer to the library in the template

from django.shortcuts import render
from .models import Book

def list_books(request):
    # Get all books from the database
    books = Book.objects.all()
    # Render the template and pass the books to the template
    return render(request, 'relationship_app/list_books.html', {'books': books})
# relationship_app/views.py

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # The context variable name to refer to the library in the template
# relationship_app/views.py

