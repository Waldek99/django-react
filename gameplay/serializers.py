from rest_framework import serializers

from .models import Country, GameplaySelection

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = (
			'id',
			'country_name',
			'country_code2',
			'country_code3',
			'country_flag',		
		)

class GameplaySelectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameplaySelection
		fields = [
			'user',
			'game_name',
			'game_content',
			'game_type',
			'game_level',
			'game_mode',
			'game_template',
			'game_css',
		]