from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django import forms

class SignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_user = True
		user.save()

		return user