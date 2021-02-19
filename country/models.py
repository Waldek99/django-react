
from django.db import models

from django.utils.html import mark_safe


# Create your models here.

class Country(models.Model):
	country_name = models.CharField(max_length=120)
	country_code2 = models.CharField(max_length=2, blank=True, null=True)
	country_code3 = models.CharField(max_length=3, blank=True, null=True)
	country_flag = models.FileField(upload_to='country/country-flag-svg', blank=True,)
	timestamps = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.country_name

	def flag_img(self):
		if self.country_flag:
			return mark_safe('<img src="{}" width="30" style="border:{}"  />'.format(self.country_flag.url, 'thin solid black'))
		else:
			return '(No image)'
		image_img.short_description = 'Thumb'