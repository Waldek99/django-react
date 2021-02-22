from rest_framework import serializers

from .models import Country

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