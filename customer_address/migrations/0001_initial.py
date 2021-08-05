# Generated by Django 3.1.7 on 2021-04-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contry', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('town', models.CharField(default='', max_length=255)),
                ('street', models.CharField(default='', max_length=255)),
                ('locality', models.CharField(default='', max_length=255)),
                ('society', models.CharField(default='', max_length=255)),
                ('flat_no', models.CharField(default='', max_length=255)),
            ],
        ),
    ]