# Generated by Django 3.1.7 on 2021-04-22 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_remove_userprofile_user_address'),
        ('customer_address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='customer',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile'),
        ),
    ]
