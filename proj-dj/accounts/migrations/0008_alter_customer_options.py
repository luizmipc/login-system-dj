# Generated by Django 5.1.2 on 2024-11-09 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': [('can_access_page_stopwatch', 'Can access stopwatch page'), ('can_access_page_profile', 'Can access profile page'), ('can_access_page_profile_update', 'Can access profile update page')]},
        ),
    ]
