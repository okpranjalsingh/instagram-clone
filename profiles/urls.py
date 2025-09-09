from django.urls import path
from .views import (
    UserProfileView,
    MyProfileView,
    FollowUserView,
    UnfollowUserView

)



urlpatterns = [
    path("me/", MyProfileView.as_view(), name="my-profile"),
    path("<int:user_id>/", UserProfileView.as_view(), name="user-profile"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),

]
