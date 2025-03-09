from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . views import BookViewSet
# Set up the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('', include(router.urls)),
    path('books/', views.BookList.as_view(), name='book-list'),
]
