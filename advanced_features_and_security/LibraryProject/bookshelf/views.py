from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import CustomUser
from ..relationship_app.forms import ExampleForm
from django.contrib.auth import login, authenticate, hashers
from django.shortcuts import render, redirect
from .forms import BookForm
from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data (like sending an email, etc.)
            return render(request, 'bookshelf/success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book
            return redirect('book_list')  # Redirect to a list of books or another view
    else:
        form = BookForm()

    return render(request, 'bookshelf/add_book.html', {'form': form})

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    all_books = [
        {'id': 1, 'title': 'Python', 'author': 'Guido Van Rossum'},
        {'id': 2, 'title': 'Django', 'author': 'Guido Van Rossum'},
        {'id': 3, 'title': 'Flask', 'author': 'Guido Van Rossum'}
    ]
    return render(request, 'bookshelf/book_list.html', {'all_books': all_books})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/create.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/edit.html')

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/delete.html')

# Login authentication
def login_user(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = get_object_or_404(CustomUser, email)
            print(user)
            if user:
                if hashers(password, user.password):
                    authenticated_user = authenticate(request, email=email, password=user.password)
                    print(authenticated_user)
                    if authenticated_user:
                        print(True)
                        login(request, user=user)
                        return redirect('book_list')
                else:
                    form.add_error(None, 'Email or Password is incorrect!')
            else:
                form.add_error('email', 'User with this email does not exist!')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
    