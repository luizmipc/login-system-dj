from accounts.models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils import timezone


from django import forms

""" Maintain users """
class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput,
        required=True,
        max_length=30,
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")

        if len(username) < 5:
            raise ValidationError("Username too short. It must be at least 5 characters.")
        return username

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date"
        }),
        label="Birthday",
        help_text="Format: mm/dd/YY"
    )
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get("date_of_birth")
        if date_of_birth > timezone.now().date():
            raise ValidationError("Birthday cannot be in the future.")
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
            raise ValidationError("Passwords don't match.")
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

class CustomUserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput,
        required=True,
        max_length=30,
    )

    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text="You cannot change the password here. Use the password reset option instead."
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Birthday",
        help_text="Format: mm/dd/YY"
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "date_of_birth"]

    def __init__(self, *args, **kwargs):
        # Capture the current user's ID for uniqueness checks, if passed in kwargs
        self.user_id = kwargs.pop("user_id", None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get("username")

        # If user_id is provided, perform exclusion check for uniqueness
        if self.user_id:
            if CustomUser.objects.filter(username=username).exclude(pk=self.user_id).exists():
                raise ValidationError("Username already exists.")

        if len(username) < 5:
            raise ValidationError("Username too short. It must be at least 5 characters.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # If user_id is provided, perform exclusion check for uniqueness
        if self.user_id:
            if CustomUser.objects.filter(email=email).exclude(pk=self.user_id).exists():
                raise ValidationError("Email already exists.")

        return email

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get("date_of_birth")
        if date_of_birth > timezone.now().date():
            raise ValidationError("Birthday cannot be in the future.")
        return date_of_birth

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Email",
        widget=forms.TextInput
    )
    def clean_password(self):
        """Check if the provided password is correct for the given username/email."""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Attempt to authenticate the user
        user = authenticate(self.request, username=username, password=password)

        if user is None:
            raise ValidationError(_("Invalid email or password"), code='invalid_login')

        return password

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput
    )

    def confirm_login_allowed(self, user):
        """Override to customize login restrictions."""
        if not user.is_active:
            raise ValidationError("This account is inactive.")