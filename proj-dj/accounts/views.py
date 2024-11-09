from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  template_name = "registration/signup.html"
  success_url = reverse_lazy("login")

class ProfileDetailView(PermissionRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = "registration/profile_detail.html"  # Ensure this matches your template name
    permission_required = ["accounts.can_access_page_profile"]

    def get_object(self):
        # Fetch user by username
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.request.user
        return context

@login_required
def redirect_to_user_profile(request):
    # Redirect to the logged-in user's profile URL
    return redirect('profile', username=request.user.username)

class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    context_object_name = "user"
    template_name = "registration/profile_update.html"
    permission_required = ["accounts.can_access_page_profile_update"]

    def get_object(self):
        # Fetch user by username
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)


@login_required
def redirect_to_user_profile_update(request):
    return redirect('profile_update', username=request.user.username)

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