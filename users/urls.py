from django.urls import path
from .views import (
    SignupView,
    LoginView,
    LogoutView,
    FollowUnfollowView
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signin'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('follow/', FollowUnfollowView.as_view(), name='follow-unfollow'),
]
