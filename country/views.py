from django.shortcuts import render

from rest_framework.pagination import PageNumberPagination

from rest_framework import generics

from .serializers import CountrySerializer
from .models import Country

# Create your views here.

class SmallResultsSetPagination(PageNumberPagination):
	page_size = 20
	page_size_query_param = 'page_size'
	max_page_size = 1000

class CountryList(generics.ListCreateAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer
	pagination_class = SmallResultsSetPagination

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer

