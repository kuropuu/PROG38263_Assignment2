from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Paste
from .forms import PasteCreationForm
from django.db.models import Q

def home(request):
	context = {
		'pastes': Paste.objects.all()
	}
	return render(request, 'home/home.html', context)

class PasteListView(ListView):
	model = Paste
	template_name = 'home/home.html'
	context_object_name = 'pastes'
	ordering = ['-date_posted']

class PasteDetailView(DetailView):
	model = Paste

class PasteCreateView(LoginRequiredMixin, CreateView):
	model = Paste
	form_class = PasteCreationForm

	def form_valid (self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PasteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Paste
	form_class = PasteCreationForm
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		paste = self.get_object()
		if self.request.user == paste.author:
			return True
		return False

class PasteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Paste
	success_url = '/'

	def test_func(self):
		paste = self.get_object()
		if self.request.user == paste.author:
			return True
		return False

def search(request):
	query = request.GET.get('q')
	results = Paste.objects.filter(Q(title__icontains=query) |
											 Q(content__icontains=query))

	context = {
		'pastes':results
	}
	return render(request, 'home/home.html', context)
 
