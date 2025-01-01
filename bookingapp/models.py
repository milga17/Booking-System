from django.db import models
from adminapp.models import Services

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)

class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    message=models.CharField(max_length=150)

class Login(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class Book(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    serviceid=models.ForeignKey(Services,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    status = models.IntegerField(default=0)
    

