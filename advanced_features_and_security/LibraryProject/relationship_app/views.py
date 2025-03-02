from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import BookForm

# Refactored helper function for book views
def handle_book_form(request, book=None):
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list view after saving
    else:
        form = BookForm(instance=book)
    return form
# Add this to your views.py
def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/book_list.html', {'books': books})

# View to add a book (requires permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    form = handle_book_form(request)  # Reuse the helper function for form handling
    return render(request, 'add_book.html', {'form': form})

# View to edit a book (requires permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = handle_book_form(request, book=book)  # Reuse the helper function with the book instance
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# View to delete a book (requires permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'  # Custom login template
    redirect_authenticated_user = True  # Redirect if the user is already authenticated
    success_url = reverse_lazy('home')  # Where to redirect after successful login

# Custom Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'  # Custom logout template

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role check functions for user-based views
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (restricted to Admin role)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (restricted to Librarian role)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (restricted to Member role)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
