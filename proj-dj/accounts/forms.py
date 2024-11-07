from accounts.models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils import timezone


from django import forms

""" Maintain users """
class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput,
        required=True
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
        }),
        label="Date of Birth",
        help_text="Format: mm/dd/YY"
    )
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get("date_of_birth")
        if date_of_birth > timezone.now().date():
            raise ValidationError("Date of Birth cannot be in the future.")
        return date_of_birth

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Password must contain at least 8 characters.")
        return password1

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput
    )
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    class Meta:
        model = CustomUser
        fields = ["username", "email", "date_of_birth"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model =CustomUser
        fields = ["username", "email", "password", "date_of_birth", "is_active", "is_admin"]
