from rest_framework import serializers

from .models import Country

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = (
			'id',
			'country_name',
			'nick_name',
			'description_name',
			'country_code',
			'country_flag',
			
		)