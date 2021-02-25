from django.urls import path


from .views import (
	CountryList,
	CountryDetail
)

'''
CLIENT
Base ENDPOINT /api/countries/
'''

urlpatterns = [
	path('', CountryList.as_view()),
    path('<int:pk>/', CountryDetail.as_view()),
]