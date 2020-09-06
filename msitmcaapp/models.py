from django.db import models

# Create your models here.
class Student(models.Model):
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	class Meta:
		db_table="personal"