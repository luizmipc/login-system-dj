from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models.users import CustomUser

from django import forms

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
      super(CustomUserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField()

class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model = CustomUser
    fields = ("username", "email", "description")

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model = CustomUser
    fields = ("username", "email")
