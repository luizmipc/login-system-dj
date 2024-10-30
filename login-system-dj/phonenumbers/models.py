from django.db import models
from django.conf import settings

# Create your models here.
class PhoneNumber(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='phone_numbers'

    )
    label = models.CharField(max_length=30, blank=True, null=True)

    number = models.CharField(max_length=20)

    country_code = models.ForeignKey(
        'localities.Country',
        on_delete=models.SET_NULL,
        related_name='phone_numbers',
        null=True,
        blank=True
    )

    state_code = models.ForeignKey(
        'localities.State',
        on_delete=models.SET_NULL,
        related_name='phone_numbers',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.label or 'Phone'}: {self.number}, State: {self.state_code}, Country: {self.country_code}"