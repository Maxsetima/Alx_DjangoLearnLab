from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import PostListView, PostDetailView, CommentListView, CommentDetailView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Get, update, or delete a single post
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),  # List all comments for a post
    path('<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),  # Get, update, or delete a comment
]
