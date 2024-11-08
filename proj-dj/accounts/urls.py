from django.contrib.auth import views

from django.urls import path

from accounts.views import SignUpView, ProfileDetailView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("profile/", ProfileDetailView.as_view(), name='profile'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
]
