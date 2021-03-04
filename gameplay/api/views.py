from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from ..serializers import CountrySerializer, GameplaySelectionSerializer
from ..models import Country, GameplaySelection



class SmallResultsSetPagination(PageNumberPagination):
	page_size = 20
	page_size_query_param = 'page_size'
	max_page_size = 1000

'''
Serializers for Country
'''

@permission_classes([IsAuthenticated])
class CountryList(generics.ListCreateAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer
	pagination_class = SmallResultsSetPagination

@permission_classes([IsAuthenticated])
class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Country.objects.all()
	serializer_class = CountrySerializer

'''
Serializers for GameplaySelection
'''

@permission_classes([IsAuthenticated])
class GameplaySelectionList(generics.ListCreateAPIView):
	queryset = GameplaySelection.objects.all()
	serializer_class = GameplaySelectionSerializer
	pagination_class = SmallResultsSetPagination

@permission_classes([IsAuthenticated])
class GameplaySelectionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = GameplaySelection.objects.all()
	serializer_class = GameplaySelectionSerializer