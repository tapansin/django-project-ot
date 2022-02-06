import email
from unicodedata import name
from django.db import models


# Create your models here.
class contactinfo(models.Model):
    name= models.CharField(max_length=256)
    email= models.EmailField()
    address = models.CharField(max_length=256)
    class Meta:
        abstract=True

class Student(contactinfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(contactinfo):
    subject=models.CharField(max_length=256)
    salary=models.FloatField()