from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'blog/base.html')
def posts(request):
    # For now, render a simple placeholder template
    return render(request, 'blog/posts.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# The login and logout views are provided by Django's built-in auth system.
# For profile management, create a simple view:
@login_required
def profile(request):
    # For demonstration, simply render a profile page.
    return render(request, 'blog/profile.html')