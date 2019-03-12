from django import forms
from django.forms import ModelForm
from .models import Paste

class DateInput(forms.DateInput):
	input_type = 'date'

class PasteCreationForm(ModelForm):
	
	class Meta:
		model = Paste
		fields = ['privacy', 'title','content', 'invited_users', 'expiry']
		widgets = {
			'expiry': DateInput(),
		}
