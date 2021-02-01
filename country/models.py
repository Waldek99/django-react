from django.db import models

# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=120)
	nick_name = models.CharField(max_length=300)
	description_name = models.TextField(blank=True, null=True)
	country_code = models.CharField(max_length=3)
	country_flag = models.ImageField(upload_to='image/', blank=True, null=True)
	timestamps = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.country_name
