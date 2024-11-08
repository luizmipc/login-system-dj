from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm

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


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')  # Replace 'home' with your desired URL name

    def form_valid(self, form):
        messages.success(self.request, "Login successful!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials. Please try again.")
        return self.render_to_response(self.get_context_data(form=form))