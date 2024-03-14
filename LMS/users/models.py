from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    phone_number = models.CharField(max_length = 11 , null = True , unique = True , blank = True)
    adress = models.CharField(max_length = 50)




