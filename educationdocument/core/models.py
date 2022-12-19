from django.db import models
import random

class UserDetail (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    point1=models.IntegerField()
    point2=models.IntegerField()
    
    date=models.DateTimeField(auto_now_add=True)
    fin = models.CharField(max_length=7)
    number = random.randint(10000,100000)

