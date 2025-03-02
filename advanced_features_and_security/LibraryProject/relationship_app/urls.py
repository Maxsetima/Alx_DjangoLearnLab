from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    # Book-related views
    path('books/', views.book_list, name='book_list'),  # Assuming you have a book list view
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
    path('register/', views.register, name='register'),

    # Role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
# LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('relationship_app.urls')),  # Include the app's URLs here
]
