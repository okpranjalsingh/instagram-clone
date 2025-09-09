from django.urls import path
from .views import (
    ProfileView,
    UserProfileView,
    MyProfileView
)


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path("me/", MyProfileView.as_view(), name="my-profile"),
    path("<int:user_id>/", UserProfileView.as_view(), name="user-profile"),
]
