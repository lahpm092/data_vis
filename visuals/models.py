from django.db import models

# Create your models here.
class Clinical(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Infecto(models.Model):
	name = models.CharField(max_length=50)
	agent = models.CharField(max_length=50)
	epidemiology = models.CharField(max_length=50)
	clinical = models.ManyToManyField(Clinical)
	diagnosis = models.CharField(max_length=50)
	treatment = models.CharField(max_length=50)

	def __str__(self):
		return self.name