# Generated by Django 3.1.7 on 2021-04-22 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_address', '0001_initial'),
        ('user_profile', '0004_auto_20210420_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_address',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='customer_address.customeraddress'),
        ),
    ]
