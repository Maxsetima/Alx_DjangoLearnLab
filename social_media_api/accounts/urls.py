from django.urls import path
from .views import RegisterView, LoginView, UserRegistrationView  # Correct views for registration and login

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register a new user
    path('login/', LoginView.as_view(), name='login'),  # Login user and get token
    path('register/user/', UserRegistrationView.as_view(), name='user-registration'),  # User registration with token
]
