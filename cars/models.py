from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    power = models.IntegerField(default=0)
    color = models.CharField(max_length=100)
