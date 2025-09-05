from django.urls import path
from .views import (
    PostDetailView,
    FeedView,
    PostListCreateView
)


urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Feed - posts from people you follow
    path("feed/", FeedView.as_view(), name="feed"),
         
]

