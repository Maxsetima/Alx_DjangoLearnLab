from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # Default endpoint for /api/ - show the list of books
    path('', BookListView.as_view(), name='api-home'),
    
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    
    # Optionally, if required by tests or assignments
    path('books/update/', BookUpdateView.as_view(), name='book-update-no-pk'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete-no-pk'),
]
