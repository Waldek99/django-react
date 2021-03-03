from django import forms
from django.forms import ModelForm

from .models import UserSelection


class UserSelectionForm(forms.ModelForm):
	class Meta:
		model = UserSelection
		fields = [
			'user',
			'type_of_game',
			'level_of_game',
			'game_mode'
		]