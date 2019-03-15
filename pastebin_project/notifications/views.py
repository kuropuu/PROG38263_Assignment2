from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Notifications, Keywords
from .forms import AddKeywordForm
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView

class NotificationsView(ListView, ContextMixin):
	model = Notifications
	template_name = 'notifications/inbox.html'
	context_object_name = 'notifications'

	def get_queryset(self):
		return Notifications.objects.order_by('viewed')

def show_notification(request, pk):
	n = Notifications.objects.get(id=pk)
	return render(request, 'notifications/notification.html', {'notification': n})

def delete_notification(request, pk):
	n = Notifications.objects.get(id=pk)
	n.viewed = True
	n.save()

	return HttpResponseRedirect('/inbox/inbox/')

class AddKeywordView(LoginRequiredMixin, CreateView):
	model = Keywords
	form_class = AddKeywordForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
