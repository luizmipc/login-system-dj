from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission

from accounts.models import CustomUser, Customer
from accounts.forms import CustomUserUpdateForm, CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserUpdateForm
    add_form = CustomUserCreationForm
    list_display = ["username", "email", "date_of_birth", "is_admin"]
    list_filter = ["is_admin", "groups"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Personal info", {"fields": ["date_of_birth"]}),
        ("Permissions", {"fields": ["is_admin", "is_superuser","groups", "user_permissions"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "date_of_birth", "password1", "password2", "is_admin", "is_superuser", 'groups', 'user_permissions'],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ["groups", "user_permissions"]



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer)

