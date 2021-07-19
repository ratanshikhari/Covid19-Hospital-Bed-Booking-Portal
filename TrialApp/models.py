from django.db import models

class SignUp(models.Model):
    userName = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=100)

    def __str__(self):
        return self.userName + " " + self.userPassword
