from django.contrib import admin

from .models import Country, GameplaySelection

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


class GameplaySelectionAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'game_name',
		'game_content',
		'game_type',
		'game_level',
		'game_mode',
		'game_template',
		'game_css',

	)


admin.site.register(Country, CountryAdmin)
admin.site.register(GameplaySelection, GameplaySelectionAdmin)
