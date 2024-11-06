from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser, Customer

@receiver(post_save, sender=CustomUser)
def manage_customer_profile(sender, instance, **kwargs):
    if instance.is_customer:
        # Get or create the Customer instance, and save it if it already exists
        customer, created = Customer.objects.get_or_create(user=instance)
        if not created:  # If the customer already existed, save it to apply updates
            customer.save()
    else:
        # Delete the Customer instance if is_customer is unchecked
        Customer.objects.filter(user=instance).delete()