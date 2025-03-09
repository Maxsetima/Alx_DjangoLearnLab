from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.http import HttpResponse

# Root view
def home(request):
    return HttpResponse("Welcome to the Django API! Visit /api/ to see the book list.")
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
    permission_classes = [IsAuthenticated]  # Require authentication to access this AP
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
