from django.db import models
from django.conf import settings

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f"{self.name}, {self.country.code}"

class Address(models.Model):
    state = models.ForeignKey(State, related_name='addresses', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    street_name = models.CharField(max_length=150)
    street_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street_name}, {self.street_number}, {self.city}, {self.state.name}, {self.state.country.name}"

class Locality(models.Model):
    additional_details = models.TextField(max_length=100)
    address = models.ForeignKey(Address, related_name='localities', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='localities')

    def __str__(self):
        return f"{self.additional_details}, {self.address}"