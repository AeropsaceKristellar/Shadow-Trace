from django.db import models

# Create your models here.
class User(models.Model):
    User_Name = models.CharField(max_length=30) 
    First_Name = models.CharField(max_length = 30)
    Last_Name = models.CharField(max_length = 30)
    Email = models.EmailField(max_length = 30)
    Password = models.CharField(max_length = 30)

