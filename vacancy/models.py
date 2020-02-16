from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prof(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	qualifications = models.TextField()
	experience = models.TextField()
	salary = models.IntegerField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.fname