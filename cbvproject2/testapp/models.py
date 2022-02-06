from django.db import models

# Create your models here.
class Books(models.Model):
	title=models.CharField(max_length=256)
	author=models.CharField(max_length=256)
	pages=models.PositiveIntegerField()
	price=models.FloatField()
