from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .serializers import CountrySerializer
from .models import Country

# Create your views here.

class HomePageView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['page_welcome'] = 'Welcome!'
		return data



