# Generated by Django 4.1.4 on 2023-01-12 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_password_user_password1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus_booking',
            name='password',
        ),
    ]