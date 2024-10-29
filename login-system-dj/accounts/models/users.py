from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
  pass
  description = models.CharField(max_length=100, default="")

  def __str__(self):
    return self.username