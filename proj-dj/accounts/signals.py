# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import CustomUser, Customer

@receiver(post_save, sender=CustomUser)
def update_permissions_based_on_is_customer(sender, instance, created, **kwargs):
    if instance.is_customer:
        # Add permissions when is_customer is True
        permission = Permission.objects.get(codename='access_page_stopwatch')
        instance.user_permissions.add(permission)
        Customer.objects.get_or_create(user=instance)
    else:
        # Remove permissions when is_customer is False
        permission = Permission.objects.get(codename='access_page_stopwatch')
        instance.user_permissions.remove(permission)
        Customer.objects.filter(user=instance).delete()
