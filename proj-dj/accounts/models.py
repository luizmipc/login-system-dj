from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None):

        user = self.create_user(
            username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="username",
        max_length=30,
        unique=True,
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "date_of_birth"]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user.is_customer = True

    class Meta:
        permissions = [
            ("access_page_stopwatch", "Can access stopwatch page")
        ]