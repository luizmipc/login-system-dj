# Generated by Django 5.1.2 on 2024-11-02 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonenumbers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumber',
            old_name='user',
            new_name='users',
        ),
    ]
