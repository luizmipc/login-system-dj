from django.contrib.auth import views

from django.urls import path

from accounts.views import SignUpView, ProfileDetailView, CustomLoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup'),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("profile/", ProfileDetailView.as_view(), name='profile'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
]
