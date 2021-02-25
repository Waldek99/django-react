from django.contrib import admin

from .models import Country, UserSelection

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


class UserSelectionAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'type_of_game',
		'level_of_game',
		'game_mode',

	)


admin.site.register(Country, CountryAdmin)
admin.site.register(UserSelection, UserSelectionAdmin)
