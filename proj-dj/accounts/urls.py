from django.contrib.auth import views
from django.urls import path
from accounts.views import SignUpView, ProfileDetailView, CustomLoginView, CustomUserUpdateView, redirect_to_user_profile, redirect_to_user_profile_update

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup'),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("profile/", redirect_to_user_profile, name='profile'),
    path("profile/<str:username>/", ProfileDetailView.as_view(), name='profile'),  # Profile with username
    path("profile/update/", redirect_to_user_profile_update, name='profile_update'),
    path("profile/<str:username>/update/", CustomUserUpdateView.as_view(), name='profile_update'),  # For specific user profiles
    path("logout/", views.LogoutView.as_view(), name='logout'),
]
