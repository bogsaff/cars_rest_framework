from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    power = models.IntegerField(default=0)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)