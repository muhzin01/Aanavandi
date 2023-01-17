# Generated by Django 4.1.4 on 2023-01-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_user_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=101)),
                ('last_name', models.CharField(max_length=101)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]