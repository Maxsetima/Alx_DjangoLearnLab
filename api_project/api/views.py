from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.http import HttpResponse

# Root view
def home(request):
    return HttpResponse("Welcome to the Django API! Visit /api/ to see the book list.")
