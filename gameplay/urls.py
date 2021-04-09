from django.urls import path


from .views import (
	HomePageView,
	GameplaySelectionCreate,
	GameplaySelectionDetailView,
	GameplaySelectionListView,
	GameplaySelectionUpdateView,
	GameplaySelectionDeleteView,
)

'''
CLIENT
Base ENDPOINT /gameplay/
'''

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('create/', GameplaySelectionCreate.as_view(), name='create'),
	path('detail/<int:pk>/', GameplaySelectionDetailView.as_view(), name='detail'),
	path('list', GameplaySelectionListView.as_view(), name='list'),
	path('update/<int:pk>/', GameplaySelectionUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', GameplaySelectionDeleteView.as_view(), name='delete'),
]