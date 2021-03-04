from django.conf import settings
from django.db import models
from django.urls import reverse

from django.utils.html import mark_safe

User = settings.AUTH_USER_MODEL


# Create your models here.

TYPE_OF_GAME_CHOICES = [
	('FO', 'Football'),
	('BA', 'Basketball'),
	('HO', 'Hockey'),
	('VO', 'Vollyball'),
	('HA', 'Handball'),
	('AF', 'American Football'),
	('RF', 'Rugby Football'),
	('SJ', 'Ski jumping'),
]

LEVEL_OF_GAME_CHOICES = [
	('IN', 'International'),
	('CC', 'Club Competitions'),
	('IC', 'International Club Competitions'),
]

GAME_MODE_CHOICES = [
	('LE', 'League'),
	('CU', 'Cup'),
]

class GameplaySelection(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	game_name = models.CharField(max_length=120, null=True)
	game_content = models.TextField(blank=True, null=True)
	game_type = models.CharField(max_length=2, choices=TYPE_OF_GAME_CHOICES)
	game_level = models.CharField(max_length=2, choices=LEVEL_OF_GAME_CHOICES)
	game_mode = models.CharField(max_length=2, choices=GAME_MODE_CHOICES)
	game_template = models.CharField(max_length=120, blank=True, null=True)
	game_css = models.CharField(max_length=120, blank=True, null=True)

	def __str__(self):
		return self.user

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-id']

class Country(models.Model):
	country_name = models.CharField(max_length=120)
	country_code2 = models.CharField(max_length=2, blank=True, null=True)
	country_code3 = models.CharField(max_length=3, blank=True, null=True)
	country_flag = models.FileField(upload_to='country/country-flag-svg', blank=True,)
	timestamps = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.country_name

	class Meta:
		ordering = ['-id']

# Function shows pictures in admins.

	def flag_img(self):
		if self.country_flag:
			return mark_safe('<img src="{}" width="30" style="border:{}"  />'.format(self.country_flag.url, 'thin solid black'))
		else:
			return '(No image)'
		image_img.short_description = 'Thumb'