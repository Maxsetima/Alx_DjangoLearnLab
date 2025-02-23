# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    # Using LoginView with the custom login template
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), 
    
    # Using LogoutView with the custom logout template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
    
    # Registration view
    path('register/', views.register, name='register'),
]
# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
