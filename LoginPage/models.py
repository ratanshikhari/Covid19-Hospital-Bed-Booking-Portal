from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
    userName = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=100)

    def __str__(self):
        return self.userName + " " + self.userPassword

class extendeduser(models.Model):
    age = models.CharField(max_length=200, null=True)
    phone_no = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    aadhar = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
