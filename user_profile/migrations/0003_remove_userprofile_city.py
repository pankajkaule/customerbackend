# Generated by Django 3.1.7 on 2021-04-19 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210419_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
    ]
