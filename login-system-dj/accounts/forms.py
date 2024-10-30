from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser

from django import forms

""" Maintain users """
class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
      super(CustomUserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField()

class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model = CustomUser
    fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model = CustomUser
    fields = ("username", "email")
