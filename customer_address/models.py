from django.db import models
from user_profile.models import UserProfile
class CustomerAddress(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='')
    contry = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    pincode = models.IntegerField(default=0)
    primobileno = models.CharField(max_length=20, default='')
    secmobileno = models.CharField(max_length=20, default='')
    town = models.CharField(max_length=255, default='')
    street = models.CharField(max_length=255, default='')
    locality = models.CharField(max_length=255, default='')
    society = models.CharField(max_length=255, default='')
    flat_no = models.CharField(max_length=255, default='')
    addresstype = models.CharField(max_length=255, default='home')