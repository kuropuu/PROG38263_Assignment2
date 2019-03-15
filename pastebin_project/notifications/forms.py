from django import forms
from django.forms import ModelForm
from .models import Keywords
from django.db import models

class AddKeywordForm(ModelForm):
	class Meta:
		model = Keywords
		fields = ['keyword1', 'keyword2', 'keyword3']
