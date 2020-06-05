from django.db import models

# Create your models here.
class AddCity(models.Model):
	cityName = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.cityName