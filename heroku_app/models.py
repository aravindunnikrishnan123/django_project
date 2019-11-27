from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=15)

class UserDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=15)
    gender     = models.CharField(max_length=10)
    dob        = models.DateField()
    fk_login   = models.ForeignKey(Login, on_delete=models.CASCADE)
   