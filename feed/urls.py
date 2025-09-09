from django.urls import path
from .views import (
    PostDetailView,
    FeedView,
    PostListCreateView,
    PostUpdateView,
    CommentListCreateView,
    CommentDetailView,
    LikePostView,
    UnlikePostView,
    PostLikesView,
)

urlpatterns = [
    # Posts
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:post_id>/update/", PostUpdateView.as_view(), name="post-update"),

    # Feed (posts from people you follow)
    path("feed/", FeedView.as_view(), name="feed"),

    # Comments
    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("posts/<int:post_id>/like/", LikePostView.as_view(), name="like-post"),
    path("posts/<int:post_id>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
    path("posts/<int:post_id>/likes/", PostLikesView.as_view(), name="post-likes"),

]
