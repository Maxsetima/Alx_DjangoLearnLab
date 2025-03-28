from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import PostListView, PostDetailView, CommentListView, CommentDetailView
from .views import FeedView
from accounts.views import FollowUserView, UnfollowUserView


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Get, update, or delete a single post
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),  # List all comments for a post
    path('<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),  # Get, update, or delete a comment
]
