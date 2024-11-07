from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from accounts.forms import CustomUserCreationForm

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  template_name = "registration/signup.html"
  success_url = reverse_lazy("login")
