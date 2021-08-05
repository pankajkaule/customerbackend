from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default='')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    mobile_no = models.CharField(max_length=20, default='')
    otp = models.IntegerField(default=0)
    isemailverified = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name

