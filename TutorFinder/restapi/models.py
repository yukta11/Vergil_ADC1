from django.db import models

# Create your models here.

class Tutors(models.Model):
	tutor_name = models.CharField(max_length=50)
	tutor_location = models.CharField(max_length=50)

	def __str__(slef):
		return str(tutor_name)