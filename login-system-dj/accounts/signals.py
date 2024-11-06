from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser, Customer

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_customer:
            Customer.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_customer:
        instance.customer.save()