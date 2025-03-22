from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, posts, register, profile,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Basic pages and authentication
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # CRUD operations for blog posts
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
