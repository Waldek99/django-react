from django.shortcuts import render

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .serializers import CountrySerializer
from .models import Country

# Create your views here.

class CountryView(viewsets.ModelViewSet):
	serializer_class = CountrySerializer
	queryset = Country.objects.all()
	paginator = PageNumberPagination()
	paginator.page_size = 20
	pagination_class = paginator

