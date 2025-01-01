from django.db import models

# Create your models here.
class Branches(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',default='null.jpg')

class Salons(models.Model):
    name=models.CharField(max_length=40)
    branch=models.CharField(max_length=40)
    image=models.ImageField(upload_to='images',default='null.jpg')

class Services(models.Model):
    servicename=models.CharField(max_length=50)
    salonname=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images',default='null.jpg')