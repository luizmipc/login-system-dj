from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render


class StopWatchView(PermissionRequiredMixin, TemplateView):
    template_name = "times/stopwatch.html"
    permission_required = ["accounts.access_page_stopwatch"]
