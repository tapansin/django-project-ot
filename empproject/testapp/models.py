from django.db import models

# Create your models here.
class Employee(models.Model):
	eno= models.IntegerField()
	ename= models.CharField(max_length=30)
	esal= models.FloatField()
	eaddr= models.CharField(max_length=30)

	class Meta:
		verbose_name  = "Employee Salary"
'''class love(object):
	"""docstring for love"""
	def __init__(self, love2):
		super(love, self).__init__()
		self.arg = arg'''
		
