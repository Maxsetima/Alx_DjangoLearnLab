from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, register, profile
from .views import home, posts


urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    # Use Django’s built-in views for login and logout:
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # Optionally, add other paths (e.g., for posts)

]
