from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account created for %s. You may now sign in with your credentials.' % username)
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', { 'form': form })

@login_required
def profile(request):
	return render(request, 'users/profile.html')

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated.')
			return redirect('login')
		else:
			messages.error(request, 'Please enter the correct password.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'users/change_password.html', { 'form': form })
