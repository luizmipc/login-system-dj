from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
]
