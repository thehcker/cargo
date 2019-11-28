from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			form.save()
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			messages.success(request, f'Your Account has been created succesfully {username}')
			return redirect('cargo')
	else:
		form = SignUpForm()

	return render(request, 'signup.html', {'form': form})
