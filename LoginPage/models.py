from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
    userName = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=100)

    def __str__(self):
        return self.userName + " " + self.userPassword

class extendeduser(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    phone_no = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    reportFile = models.FileField()
    aadhar = models.IntegerField(null=True, unique=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    hSelectedName = models.CharField(max_length=200, null=True, default='Hospital not yet booked')
    hBooked = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
