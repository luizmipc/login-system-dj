# Generated by Django 5.1.2 on 2024-11-05 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_is_customer_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': [('access_page_stopwatch', 'Can access stopwatch page')]},
        ),
    ]
