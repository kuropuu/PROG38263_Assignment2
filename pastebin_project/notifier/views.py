from django.views.generic import TemplateView
from django.shortcuts import render

def inbox(request):
	return render(request, 'inbox.html')
class InboxView(TemplateView):
	template_name = "inbox.html"
