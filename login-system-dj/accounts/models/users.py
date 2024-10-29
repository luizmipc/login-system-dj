from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  pass
    # to add new fields
  def __str__(self):
    return self.username