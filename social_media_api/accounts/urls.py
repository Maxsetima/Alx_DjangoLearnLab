from django.urls import path
from .views import RegisterView, LoginView, UserRegistrationView  # Correct views for registration and login
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('register/', RegisterView.as_view(), name='register'),  # Register a new user
    path('login/', LoginView.as_view(), name='login'),  # Login user and get token
    path('register/user/', UserRegistrationView.as_view(), name='user-registration'),  # User registration with token
]
