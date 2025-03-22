from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home, posts, register, profile,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    search_posts, 
    edit_comment, delete_comment,
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
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Comment actions using class-based views
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

     # Advanced features: search and tag filtering
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag>/', lambda request, tag: render(request, 'blog/tag_posts.html', {
        'tag': tag,
        'posts': Post.objects.filter(tags__name__iexact=tag)
    }), name='tag-posts'),
]
