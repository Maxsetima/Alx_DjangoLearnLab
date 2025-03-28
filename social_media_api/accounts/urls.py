from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginView  # Correct views for registration and login

# Add additional views for profile management if needed

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register a new user
    path('login/', LoginView.as_view(), name='login'),  # Login user and get token
    # Optional: Add paths like 'profile/' for profile view/update if implemented
]
