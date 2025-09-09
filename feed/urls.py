from django.urls import path
from .views import (
    PostDetailView,
    FeedView,
    PostListCreateView,
    PostUpdateView,
    CommentListCreateView,
    CommentDetailView
)


urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Feed - posts from people you follow
    path("feed/", FeedView.as_view(), name="feed"),
     # List all posts / create new
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    # Retrieve / delete a post by owner
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # Update post by owner
    path("posts/<int:post_id>/update/", PostUpdateView.as_view(), name="post-update"),
    # Feed - posts from people you follow
    path("feed/", FeedView.as_view(), name="feed"),
    
    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),

]

