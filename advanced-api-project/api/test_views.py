from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        """
        Create a test user, two Author instances, and two Book instances for testing.
        Also, set the URLs for the book list and book create endpoints.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create Author instances
        self.author_a = Author.objects.create(name='Author A')
        self.author_b = Author.objects.create(name='Author B')
        
        # Create test Book instances using valid Author instances
        self.book1 = Book.objects.create(title='Book One', publication_year=2001, author=self.author_a)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2002, author=self.author_b)
        
        # URL for the book list view and book create view
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def test_list_books(self):
        """
        Test GET request for listing books.
        Expects status 200 and at least 2 books in the response.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)

    def test_create_book_authenticated(self):
        """
        Test creating a book with an authenticated user.
        Expects status 201 and an increase in Book count.
        """
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'Book Three',
            'publication_year': 2003,
            'author': self.author_a.id  # Pass the author id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot create a book.
        Expects status 403 Forbidden.
        """
        data = {
            'title': 'Book Four',
            'publication_year': 2004,
            'author': self.author_b.id  # Pass the author id
        }
        response = self.client.post(self.create_url, data, format='json')
        # Update expected status to 403 if using SessionAuthentication
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """
        Test updating an existing book with an authenticated user.
        Expects status 200 and the updated title to be reflected.
        """
        self.client.login(username='testuser', password='testpass')
        update_url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': 'Book One Updated',
            'publication_year': 2001,
            'author': self.author_a.id  # Use the id for the author
        }
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Book One Updated')

    def test_delete_book(self):
        """
        Test deleting a book with an authenticated user.
        Expects status 204 and that the book is removed.
        """
        self.client.login(username='testuser', password='testpass')
        delete_url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_filter_search_ordering(self):
        """
        Test filtering, searching, and ordering functionality.
        """
        # Test filtering by publication_year
        response = self.client.get(self.list_url + '?publication_year=2001')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test searching by title (and/or author name)
        response = self.client.get(self.list_url + '?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test ordering by title descending
        response = self.client.get(self.list_url + '?ordering=-title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
