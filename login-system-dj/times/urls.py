from django.urls import path
from .views import StopWatchView

urlpatterns = [
    path("stopwatch/", StopWatchView.as_view(), name='stopwatch'),
]