# Generated by Django 3.1.7 on 2021-07-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_address', '0004_auto_20210704_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='primobileno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='secmobileno',
            field=models.IntegerField(default=0),
        ),
    ]