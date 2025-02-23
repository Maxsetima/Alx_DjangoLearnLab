# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # <-- Import LoginView and LogoutView

urlpatterns = [
    # Use the CustomLoginView class for login
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    
    # Use the CustomLogoutView class for logout
    path('logout/', views.CustomLogoutView.as_view(), name='logout'), 
    
    # Use the register function from views.py for registration
    path('register/', views.register, name='register'),
]
