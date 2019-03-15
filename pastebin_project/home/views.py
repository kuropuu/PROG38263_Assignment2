from django.shortcuts import render, get_object_or_404
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
from django.contrib.auth.models import User

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
	paginate_by = 10

class UserPasteListView(ListView):
	model = Paste
	template_name = 'home/user_pastes.html'
	context_object_name = 'pastes'
	paginate_by = 10

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Paste.objects.filter(author=user).order_by('-date_posted')

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
	paginate_by = 10

	context = {
		'pastes':results
	}
	return render(request, 'home/home.html', context)
