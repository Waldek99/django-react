from django.contrib import admin

from .models import Country

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
	list_display = (
		'country_name',
		'country_code2',
		'country_code3',
		'flag_img',
		'country_flag',
		
	)
	search_fields = ['country_name', 'country_code3', 'country_code2']
	readonly_fields = ('flag_img',)



admin.site.register(Country, CountryAdmin)
