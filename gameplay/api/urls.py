from django.urls import path


from .views import (
	CountryList,
	CountryDetail,
	GameplaySelectionList,
	GameplaySelectionDetail,
)

'''
CLIENT
Base ENDPOINT /api/Gameplay/
'''

urlpatterns = [
	path('country/', CountryList.as_view()),
    path('country/<int:pk>/', CountryDetail.as_view()),
    path('list/', GameplaySelectionList.as_view()),
    path('<int:pk>/', GameplaySelectionDetail.as_view()),
]