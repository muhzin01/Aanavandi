# Generated by Django 4.1.4 on 2023-01-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_username_user_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='Username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
