# Generated by Django 3.1.7 on 2021-07-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_address', '0005_auto_20210720_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='primobileno',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='secmobileno',
            field=models.CharField(default='', max_length=20),
        ),
    ]
