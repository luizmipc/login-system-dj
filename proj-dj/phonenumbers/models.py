from django.db import models
from django.conf import settings

# Create your models here.
class PhoneNumber(models.Model):
    users = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='phonenumbers', on_delete=models.CASCADE)

    label = models.CharField(max_length=30, blank=True, null=True)

    line_number = models.CharField(max_length=20, blank=True, null=True)

    country_code = models.CharField(max_length=3, blank=True, null=True)

    state_code = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return f"{self.label or 'Phone'}: {self.number}, State: {self.state_code}, Country: {self.country_code}"