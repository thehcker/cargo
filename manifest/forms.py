from django import forms
from .models import Manifest

class ManifestForm(forms.ModelForm):
	class Meta:
		model = Manifest
		fields = '__all__'