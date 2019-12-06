from django import forms
from .models import Manifest

class ManifestForm(forms.ModelForm):
	class Meta:
		model = Manifest
		exclude = ['shipper', 'ref_no']