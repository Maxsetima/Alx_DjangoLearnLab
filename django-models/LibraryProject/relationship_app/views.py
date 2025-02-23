# relationship_app/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check functions
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
