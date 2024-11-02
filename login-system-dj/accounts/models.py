from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    locality = models.ForeignKey(
        "localities.Locality",  # Referencing the 'Locality' model in the 'localities' app
        related_name='users',  # Gives a reverse access from Locality to CustomUser
        verbose_name="Locality",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username