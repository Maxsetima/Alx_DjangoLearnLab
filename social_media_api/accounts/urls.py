from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegisterView
# Add additional views for profile management if needed

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', obtain_auth_token, name='user-login'),  # DRF built-in token auth view
    # Add paths like 'profile/' for profile view/update if implemented
]
