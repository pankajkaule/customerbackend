# Generated by Django 3.1.7 on 2021-04-22 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_userprofile_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_address',
        ),
    ]
