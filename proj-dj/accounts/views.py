from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomAuthenticationForm

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  template_name = "registration/signup.html"
  success_url = reverse_lazy("login")

class ProfileDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
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

    def get_success_url(self):
        # Redirect to the updated user's profile page
        return reverse_lazy('profile', kwargs={'username': self.object.username})

@login_required
def redirect_to_user_profile(request):
    # Redirect to the logged-in user's profile URL
    return redirect('profile', username=request.user.username)

class CustomUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    context_object_name = "user"
    template_name = "registration/profile_update.html"
    permission_required = ["accounts.can_access_page_profile_update"]

    def get_object(self):
        # Fetch user by username from URL kwargs
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)

    def get_form_kwargs(self):
        # Get default form kwargs
        kwargs = super().get_form_kwargs()

        # Inject user_id into form kwargs
        kwargs['user_id'] = self.request.user.pk  # Pass the user ID (primary key)
        return kwargs

    def form_valid(self, form):
        # Explicitly save the form
        form.save()
        # Display success message
        messages.success(self.request, "Your profile was updated successfully!")

        # Refresh user session after form save
        login(self.request, self.request.user)

        # Redirect to the updated user's profile page
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the updated user's profile page
        return reverse_lazy('profile', kwargs={'username': self.object.username})



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