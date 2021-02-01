from django.contrib import admin

from .models import Country

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
	list_display = (
		'country_name',
		'nick_name',
		'description_name',
		'country_code',
		'country_flag',
	)

admin.site.register(Country, CountryAdmin)
