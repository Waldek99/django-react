from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


from .models import Country, GameplaySelection

# Create your views here.

class HomePageView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['page_welcome'] = 'Welcome!'
		return data

class GameplaySelectionDetailView(LoginRequiredMixin, DetailView):
	model = GameplaySelection

class GameplaySelectionListView(LoginRequiredMixin, ListView):
	model = GameplaySelection
	paginate_by = 25

class GameplaySelectionUpdateView(LoginRequiredMixin, UpdateView):
	model = GameplaySelection
	fields = [
		'game_name',
		'game_content',
		'game_type',
		'game_level',
		'game_mode',
		'game_template',
		'game_css',
	]

class GameplaySelectionDeleteView(LoginRequiredMixin, DeleteView):
	model = GameplaySelection
	success_url = reverse_lazy('list')

class GameplaySelectionCreate(LoginRequiredMixin, CreateView):
	model = GameplaySelection
	fields = [
		'game_name',
		'game_content',
		'game_type',
		'game_level',
		'game_mode',
		'game_template',
		'game_css',
	]

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)




