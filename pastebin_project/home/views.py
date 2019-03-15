from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import ContextMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Paste, UploadPaste
from .forms import PasteCreationForm, PasteUploadForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
	return render(request, 'home/home.html')

# Pastes created the regular way
class PasteListView(ListView, ContextMixin):
	model = Paste
	template_name = 'home/home.html'
	context_object_name = 'pastes'
	ordering = ['-date_posted']
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(PasteListView, self).get_context_data(**kwargs)
		context.update({
			'uploadpastes': UploadPaste.objects.order_by('-date_posted'),
			'more_context': Paste.objects.all(),
		})
		return context

class UserPasteListView(ListView):
	model = Paste
	template_name = 'home/user_pastes.html'
	context_object_name = 'pastes'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		context = super(UserPasteListView, self).get_context_data(**kwargs)
		context.update({
			'uploadpastes': UploadPaste.objects.order_by('-date_posted'),
			'more_context': Paste.objects.filter(author=user).order_by('-date_posted'),
		})
		return context

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

# Pastes created through upload
class UploadPasteDetailView(DetailView):
	model = UploadPaste

class UploadPasteView(LoginRequiredMixin, CreateView):
	model = UploadPaste
	form_class = PasteUploadForm

	def form_valid (self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class UploadPasteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = UploadPaste
	form_class = PasteUploadForm
	
	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

	def test_func(self):
		uploadpaste = self.get_object()
		if self.request.user == uploadpaste.creator:
			return True
		return False

class UploadPasteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = UploadPaste
	success_url = '/'

	def test_func(self):
		uploadpaste = self.get_object()
		if self.request.user == uploadpaste.creator:
			return True
		return False

# Search for keywords in pastes
def search(request):
	query = request.GET.get('q')
	results = Paste.objects.filter(Q(title__icontains=query) |
											 Q(content__icontains=query))
	paginate_by = 10

	uploadResults = UploadPaste.objects.filter(Q(title__icontains=query) |
											 Q(content__icontains=query))
	context = {
		'pastes':results,
		'uploadpastes':uploadResults
	}
	return render(request, 'home/home.html', context)

def download_paste(request, slug):
	content = request.POST.get('content')
	filename = slug+'.txt'

	response = HttpResponse(content, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
	
	return response

