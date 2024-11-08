from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  template_name = "registration/signup.html"
  success_url = reverse_lazy("login")

class ProfileDetailView(PermissionRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = "registration/profile.html"  # Ensure this matches your template name
    permission_required = ["accounts.can_access_page_profile"]

    def get_object(self):
        # Return the currently logged-in user
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
        return context

