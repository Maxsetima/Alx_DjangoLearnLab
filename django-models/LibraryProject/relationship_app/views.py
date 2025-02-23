# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # <-- Import login here
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Registration view using the built-in UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom Login view (using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')  # Redirect to home after successful login

# Custom Logout view (using Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
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
